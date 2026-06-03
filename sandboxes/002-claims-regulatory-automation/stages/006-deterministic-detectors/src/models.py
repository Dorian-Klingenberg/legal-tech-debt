"""Shared data models for Stage 006 detector findings."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


SCHEMA_VERSION = "1.0.0"


@dataclass
class Finding:
    """A single detector finding. Distinct from candidate_evidence: carries confidence + rationale."""
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
    evidence_text: str      # verbatim excerpt that triggered the finding
    confidence: str         # HIGH | MEDIUM | LOW
    rationale: str          # why this pattern is a smell in this context
    reviewer_question: str  # specific question for a human reviewer
    false_positive_risk: str  # known reasons this might be benign

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "run_id": self.run_id,
            "created_at": self.created_at,
            "finding_id": self.finding_id,
            "smell_id": self.smell_id,
            "smell_name": self.smell_name,
            "heuristic_id": self.heuristic_id,
            "heuristic_version": self.heuristic_version,
            "node_id": self.node_id,
            "source_id": self.source_id,
            "source_type": self.source_type,
            "section_path": self.section_path,
            "evidence_text": self.evidence_text,
            "confidence": self.confidence,
            "rationale": self.rationale,
            "reviewer_question": self.reviewer_question,
            "false_positive_risk": self.false_positive_risk,
        }


def make_finding(
    run_id: str,
    smell_id: int,
    smell_name: str,
    heuristic_id: str,
    node: dict,
    evidence_text: str,
    confidence: str,
    rationale: str,
    reviewer_question: str,
    false_positive_risk: str,
    finding_counter: list[int],
) -> Finding:
    finding_counter[0] += 1
    return Finding(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=datetime.now(timezone.utc).isoformat(),
        finding_id=f"{run_id[:8]}-s{smell_id}-{finding_counter[0]:04d}",
        smell_id=smell_id,
        smell_name=smell_name,
        heuristic_id=heuristic_id,
        heuristic_version="1.0.0",
        node_id=node["node_id"],
        source_id=node.get("source_id", ""),
        source_type=node.get("source_type", ""),
        section_path=node.get("section_path", ""),
        evidence_text=evidence_text,
        confidence=confidence,
        rationale=rationale,
        reviewer_question=reviewer_question,
        false_positive_risk=false_positive_risk,
    )
