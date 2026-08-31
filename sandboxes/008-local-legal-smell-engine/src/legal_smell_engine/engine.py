from __future__ import annotations

from collections.abc import Iterable

from .contracts import DetectionRun, EvidenceCorpus, Finding
from .registry import detect_for, registered_smells


class DetectorEngine:
    """Run registered deterministic detectors over a generic local corpus."""

    def __init__(self, corpus: EvidenceCorpus, created_at: str | None = None):
        self.run = DetectionRun(corpus, created_at=created_at)

    def run_detectors(self, smell_ids: Iterable[str] | None = None) -> list[Finding]:
        selected = tuple(smell_ids) if smell_ids is not None else registered_smells()
        findings: list[Finding] = []
        for smell_id in selected:
            findings.extend(detect_for(smell_id, self.run))
        return findings

