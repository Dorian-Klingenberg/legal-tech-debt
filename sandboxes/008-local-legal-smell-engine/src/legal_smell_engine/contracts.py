"""Versioned, dependency-free contracts for local smell detection."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable

SCHEMA_VERSION = "1.0.0"


@dataclass(frozen=True)
class Node:
    """A source-traceable unit of text presented to detectors."""

    node_id: str
    source_id: str
    text: str
    source_type: str = ""
    section_path: str = ""
    node_type: str = "section"
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Node":
        return cls(
            node_id=str(value.get("node_id", "")),
            source_id=str(value.get("source_id", "")),
            text=str(value.get("text", "")),
            source_type=str(value.get("source_type", "")),
            section_path=str(value.get("section_path", "")),
            node_type=str(value.get("node_type", "section")),
            metadata=dict(value.get("metadata", {})),
        )


@dataclass(frozen=True)
class Edge:
    """An optional typed relationship between evidence nodes."""

    from_id: str
    to_id: str
    edge_type: str
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Edge":
        return cls(
            from_id=str(value.get("from_id", value.get("from", ""))),
            to_id=str(value.get("to_id", value.get("to", ""))),
            edge_type=str(value.get("edge_type", "")),
            metadata=dict(value.get("metadata", {})),
        )


@dataclass
class EvidenceCorpus:
    """Generic local evidence input; no parser or storage dependency required."""

    run_id: str
    nodes: list[Node]
    edges: list[Edge] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._nodes_by_id = {node.node_id: node for node in self.nodes}
        self._edges_from: dict[str, list[Edge]] = {}
        for edge in self.edges:
            self._edges_from.setdefault(edge.from_id, []).append(edge)

    def node(self, node_id: str) -> Node | None:
        return self._nodes_by_id.get(node_id)

    def edges_from(self, node_id: str) -> list[Edge]:
        return list(self._edges_from.get(node_id, []))

    def has_edge_within(self, node_id: str, edge_types: set[str], hops: int = 2) -> bool:
        visited: set[str] = set()
        frontier = {node_id}
        for _ in range(max(hops, 0)):
            next_frontier: set[str] = set()
            for current in frontier:
                if current in visited:
                    continue
                visited.add(current)
                for edge in self.edges_from(current):
                    if edge.edge_type in edge_types:
                        return True
                    if edge.to_id:
                        next_frontier.add(edge.to_id)
            frontier = next_frontier - visited
        return False


@dataclass
class Finding:
    """A human-reviewable detector lead, not a legal conclusion."""

    schema_version: str
    run_id: str
    created_at: str
    finding_id: str
    smell_id: int
    smell_name: str
    heuristic_id: str
    heuristic_version: str
    node_id: str
    source_id: str
    source_type: str
    section_path: str
    evidence_text: str
    confidence: str
    rationale: str
    reviewer_question: str
    false_positive_risk: str
    missing_evidence: list[str] = field(default_factory=list)
    supporting_nodes: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        if not self.missing_evidence:
            value.pop("missing_evidence")
        if not self.supporting_nodes:
            value.pop("supporting_nodes")
        return value


class DetectionRun:
    """Run-scoped identity and finding factory used by every detector."""

    def __init__(self, corpus: EvidenceCorpus, created_at: str | None = None):
        self.corpus = corpus
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self._counter = 0

    def finding(
        self,
        *,
        node: Node,
        smell_id: int,
        smell_name: str,
        heuristic_id: str,
        evidence_text: str,
        confidence: str,
        rationale: str,
        reviewer_question: str,
        false_positive_risk: str,
        missing_evidence: Iterable[str] = (),
        supporting_nodes: Iterable[dict[str, str]] = (),
    ) -> Finding:
        self._counter += 1
        return Finding(
            schema_version=SCHEMA_VERSION,
            run_id=self.corpus.run_id,
            created_at=self.created_at,
            finding_id=f"{self.corpus.run_id[:8]}-s{smell_id}-{self._counter:04d}",
            smell_id=smell_id,
            smell_name=smell_name,
            heuristic_id=heuristic_id,
            heuristic_version="1.0.0",
            node_id=node.node_id,
            source_id=node.source_id,
            source_type=node.source_type,
            section_path=node.section_path,
            evidence_text=evidence_text,
            confidence=confidence,
            rationale=rationale,
            reviewer_question=reviewer_question,
            false_positive_risk=false_positive_risk,
            missing_evidence=list(missing_evidence),
            supporting_nodes=list(supporting_nodes),
        )

