"""Data models for Stage 001 enriched findings."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TriageAnnotation:
    plain_english: str
    dispute_scenario: str
    fp_assessment: str
    model: str
    prompt_version: str


@dataclass
class JudgmentAnnotation:
    business_severity: str          # HIGH | MEDIUM | LOW
    severity_rationale: str
    remediation_direction: str
    triage_verdict: str             # one-sentence combined signal for the reviewer
    model: str
    prompt_version: str


@dataclass
class EnrichedFinding:
    # original finding fields preserved verbatim
    original: dict[str, Any]
    triage: TriageAnnotation
    judgment: JudgmentAnnotation

    def to_dict(self) -> dict[str, Any]:
        d = dict(self.original)
        d["triage"] = {
            "plain_english": self.triage.plain_english,
            "dispute_scenario": self.triage.dispute_scenario,
            "fp_assessment": self.triage.fp_assessment,
            "model": self.triage.model,
            "prompt_version": self.triage.prompt_version,
        }
        d["judgment"] = {
            "business_severity": self.judgment.business_severity,
            "severity_rationale": self.judgment.severity_rationale,
            "remediation_direction": self.judgment.remediation_direction,
            "triage_verdict": self.judgment.triage_verdict,
            "model": self.judgment.model,
            "prompt_version": self.judgment.prompt_version,
        }
        return d
