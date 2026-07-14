"""Graph expansion: parent node, sibling nodes, citations, references."""
from __future__ import annotations

from dataclasses import dataclass, field

from .index import RunIndex


@dataclass
class Expansion:
    node_id: str
    parent_node_id: str | None
    parent_text: str | None
    adjacent_node_ids: list[str]
    citation_ids: list[str]
    citation_details: list[dict]
    reference_ids: list[str]
    reference_details: list[dict]
    parser_confidence: str
    notes: list[str] = field(default_factory=list)


def expand(index: RunIndex, node_id: str) -> Expansion:
    n = index.node_by_id.get(node_id, {})
    notes: list[str] = []

    # Parent
    parent_id = n.get("parent_node_id")
    parent = index.node_by_id.get(parent_id) if parent_id else None
    parent_text = (parent.get("text") or "")[:300] if parent else None

    # Siblings via parent's contains edges (same source, not self)
    siblings: list[str] = []
    if parent_id:
        for e in index.edges_from.get(parent_id, []):
            if e["edge_type"] == "contains" and e["to_id"] != node_id:
                sib = index.node_by_id.get(e["to_id"])
                if sib and sib.get("source_id") == n.get("source_id"):
                    siblings.append(e["to_id"])
    siblings = siblings[:3]

    # Citations on this node
    cites = index.cites_by_node.get(node_id, [])
    cite_ids = [c["citation_id"] for c in cites]
    if cites:
        normalized = [c.get("normalized", "") for c in cites[:4]]
        notes.append(f"{len(cites)} citation(s): {', '.join(normalized)}")

    # Broader references on this node
    refs = index.refs_by_node.get(node_id, [])
    ref_ids = [r["reference_id"] for r in refs]
    if refs:
        unresolved = sum(1 for r in refs if not r.get("resolved"))
        notes.append(
            f"{len(refs)} reference(s)"
            + (f", {unresolved} unresolved" if unresolved else "")
        )

    # Parser confidence from source's parser run
    pr = index.pr_by_source.get(n.get("source_id", ""), {})
    status = pr.get("status", "")
    if status == "success":
        pconf = "high"
    elif status == "partial":
        pconf = "medium"
        notes.append(f"parser=partial ({pr.get('warning_count', 0)} warnings)")
    else:
        pconf = "low"

    return Expansion(
        node_id=node_id,
        parent_node_id=parent_id,
        parent_text=parent_text,
        adjacent_node_ids=siblings,
        citation_ids=cite_ids,
        citation_details=cites,
        reference_ids=ref_ids,
        reference_details=refs,
        parser_confidence=pconf,
        notes=notes,
    )
