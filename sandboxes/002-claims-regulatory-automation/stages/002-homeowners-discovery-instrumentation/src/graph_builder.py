"""Build typed graph edges between nodes, citations, and references.

Edges are conservative: every edge must have explicit text or structural evidence.
No cross-document edges in Stage 002.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

import ids as id_gen
from models import SCHEMA_VERSION, Citation, Edge, Node, Reference

_DEFINITION_RE = re.compile(r'"([^"]+)"\s+(?:means|is defined)', re.IGNORECASE)
_USES_TERM_RE = re.compile(r'"([^"]+)"', re.IGNORECASE)
_AMENDS_RE = re.compile(r"\bamend(?:s|ed|ing)?\b|\bsupersed(?:es|ed)?\b|\breplace(?:s|d)?\b", re.IGNORECASE)
_OVERRIDES_RE = re.compile(r"\bnotwithstanding\b|\bin\s+lieu\s+of\b|\boverride(?:s)?\b", re.IGNORECASE)


def build_edges(
    nodes: list[Node],
    citations: list[Citation],
    references: list[Reference],
    run_id: str,
) -> list[Edge]:
    now = datetime.now(timezone.utc).isoformat()
    edges: list[Edge] = []

    # Index nodes by id for quick lookup
    node_by_id: dict[str, Node] = {n.node_id: n for n in nodes}
    # Index citations by node_id
    citations_by_node: dict[str, list[Citation]] = {}
    for c in citations:
        citations_by_node.setdefault(c.node_id, []).append(c)
    # Index references by node_id
    refs_by_node: dict[str, list[Reference]] = {}
    for r in references:
        refs_by_node.setdefault(r.node_id, []).append(r)

    # 1. Containment edges (parent → child)
    for node in nodes:
        if node.parent_node_id and node.parent_node_id in node_by_id:
            eid = id_gen.edge_id(node.parent_node_id, "contains", node.node_id)
            edges.append(Edge(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                edge_id=eid,
                source_id=node.source_id,
                source_hash=node.source_hash,
                from_id=node.parent_node_id,
                from_type="node",
                to_id=node.node_id,
                to_type="node",
                edge_type="contains",
                evidence_text=None,
                confidence="high",
            ))

    # 2. Sequential (next) edges among siblings
    siblings: dict[str | None, list[Node]] = {}
    for node in nodes:
        siblings.setdefault(node.parent_node_id, []).append(node)

    for sibling_list in siblings.values():
        ordered = sorted(sibling_list, key=lambda n: n.depth)
        for i in range(len(ordered) - 1):
            a, b = ordered[i], ordered[i + 1]
            if a.parent_node_id == b.parent_node_id and a.source_id == b.source_id:
                eid = id_gen.edge_id(a.node_id, "next", b.node_id)
                edges.append(Edge(
                    schema_version=SCHEMA_VERSION,
                    run_id=run_id,
                    created_at=now,
                    edge_id=eid,
                    source_id=a.source_id,
                    source_hash=a.source_hash,
                    from_id=a.node_id,
                    from_type="node",
                    to_id=b.node_id,
                    to_type="node",
                    edge_type="next",
                    evidence_text=None,
                    confidence="high",
                ))

    # 3. Citation edges (node → citation record)
    for node in nodes:
        for c in citations_by_node.get(node.node_id, []):
            edge_type = "cites_statute" if c.citation_type == "krs_statute" else "cites_regulation"
            eid = id_gen.edge_id(node.node_id, edge_type, c.citation_id)
            edges.append(Edge(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                edge_id=eid,
                source_id=node.source_id,
                source_hash=node.source_hash,
                from_id=node.node_id,
                from_type="node",
                to_id=c.citation_id,
                to_type="citation",
                edge_type=edge_type,
                evidence_text=c.raw_text,
                confidence="high",
            ))

    # 4. Reference edges (node → reference record)
    for node in nodes:
        for r in refs_by_node.get(node.node_id, []):
            if r.reference_type == "doi_bulletin":
                etype = "cites_bulletin"
            elif r.reference_type == "generic_law":
                etype = "unresolved_reference"
            else:
                etype = "references"
            eid = id_gen.edge_id(node.node_id, etype, r.reference_id)
            edges.append(Edge(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                edge_id=eid,
                source_id=node.source_id,
                source_hash=node.source_hash,
                from_id=node.node_id,
                from_type="node",
                to_id=r.reference_id,
                to_type="reference",
                edge_type=etype,
                evidence_text=r.raw_text,
                confidence="medium" if r.resolved else "low",
            ))

    # 5. Definition edges
    defined_terms: dict[str, str] = {}  # term_lower → node_id
    for node in nodes:
        m = _DEFINITION_RE.search(node.text)
        if m:
            term = m.group(1).lower()
            defined_terms[term] = node.node_id
            eid = id_gen.edge_id(node.node_id, "defines_term", term)
            edges.append(Edge(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                edge_id=eid,
                source_id=node.source_id,
                source_hash=node.source_hash,
                from_id=node.node_id,
                from_type="node",
                to_id=node.node_id,
                to_type="node",
                edge_type="defines_term",
                evidence_text=m.group(0)[:100],
                confidence="high",
            ))

    # 6. Uses-defined-term edges (only within same source)
    for node in nodes:
        for term, def_node_id in defined_terms.items():
            if def_node_id == node.node_id:
                continue
            # Only link within same source
            def_node = node_by_id.get(def_node_id)
            if def_node and def_node.source_id != node.source_id:
                continue
            if re.search(rf'\b"{re.escape(term)}"\b', node.text, re.IGNORECASE):
                eid = id_gen.edge_id(node.node_id, "uses_defined_term", def_node_id)
                edges.append(Edge(
                    schema_version=SCHEMA_VERSION,
                    run_id=run_id,
                    created_at=now,
                    edge_id=eid,
                    source_id=node.source_id,
                    source_hash=node.source_hash,
                    from_id=node.node_id,
                    from_type="node",
                    to_id=def_node_id,
                    to_type="node",
                    edge_type="uses_defined_term",
                    evidence_text=f'"{term}"',
                    confidence="medium",
                ))

    # 7. Amends / overrides edges (intra-document, low confidence)
    for node in nodes:
        if _AMENDS_RE.search(node.text):
            # We can't resolve the target without more context — emit unresolved
            eid = id_gen.edge_id(node.node_id, "amends", "unresolved")
            edges.append(Edge(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                edge_id=eid,
                source_id=node.source_id,
                source_hash=node.source_hash,
                from_id=node.node_id,
                from_type="node",
                to_id="unresolved",
                to_type="node",
                edge_type="amends",
                evidence_text=_AMENDS_RE.search(node.text).group(0),
                confidence="low",
            ))
        if _OVERRIDES_RE.search(node.text):
            eid = id_gen.edge_id(node.node_id, "overrides", "unresolved")
            edges.append(Edge(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                edge_id=eid,
                source_id=node.source_id,
                source_hash=node.source_hash,
                from_id=node.node_id,
                from_type="node",
                to_id="unresolved",
                to_type="node",
                edge_type="overrides",
                evidence_text=_OVERRIDES_RE.search(node.text).group(0),
                confidence="low",
            ))

    return edges
