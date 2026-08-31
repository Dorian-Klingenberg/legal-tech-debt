"""
Smell 1: Overbroad / Non-deterministic Exclusions

Heuristics:
  SMELL1-H001: Sweeping conjunction ("including but not limited to") near exclusion keyword
  SMELL1-H002: Broad subject ("any loss", "all losses") near exclusion keyword
  SMELL1-H003: Causation sweep ("arising out of", "directly or indirectly") near exclusion keyword
"""
from __future__ import annotations

import re
from collections.abc import Iterator

from ..contracts import DetectionRun, Finding

SMELL_ID = 1
SMELL_NAME = "Overbroad / Non-deterministic Exclusions"

_EXCLUSION_KEYWORDS = re.compile(
    r"\b(exclud\w*|does not cover|not covered|will not pay|not payable|no coverage|"
    r"coverage does not apply|this policy does not)\b",
    re.IGNORECASE,
)

_H001_PATTERN = re.compile(
    r"\bincluding\s+but\s+not\s+limited\s+to\b",
    re.IGNORECASE,
)

_H002_PATTERN = re.compile(
    r"\b(any\s+loss|any\s+damage|any\s+claim|all\s+losses|any\s+and\s+all)\b",
    re.IGNORECASE,
)

_H003_PATTERN = re.compile(
    r"\b(arising\s+from\s+or\s+related\s+to|arising\s+out\s+of|directly\s+or\s+indirectly)\b",
    re.IGNORECASE,
)

_WINDOW = 300  # chars to check around each keyword hit


def _nearby_exclusion(text: str, match_start: int, match_end: int) -> bool:
    window_start = max(0, match_start - _WINDOW)
    window_end = min(len(text), match_end + _WINDOW)
    window = text[window_start:window_end]
    return bool(_EXCLUSION_KEYWORDS.search(window))


def _snippet(text: str, match: re.Match[str], context: int = 120) -> str:
    start = max(0, match.start() - context)
    end = min(len(text), match.end() + context)
    return text[start:end].strip()


def detect(run: DetectionRun) -> Iterator[Finding]:
    for node in run.corpus.nodes:
        if node.node_type == "document" or not node.text:
            continue
        text = node.text

        # H001
        for match in _H001_PATTERN.finditer(text):
            if _nearby_exclusion(text, match.start(), match.end()):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL1-H001",
                    evidence_text=_snippet(text, match),
                    confidence="MEDIUM",
                    rationale=(
                        "'Including but not limited to' makes an exclusion list non-exhaustive. "
                        "Reviewers cannot enumerate what falls outside coverage."
                    ),
                    reviewer_question=(
                        "Is this exclusion list intended to be open-ended? "
                        "If so, can a claimant know in advance what is excluded?"
                    ),
                    false_positive_risk=(
                        "Phrase may appear in coverage grants (what IS covered), not exclusions. "
                        "Confirm the surrounding context is exclusionary."
                    ),
                )

        # H002
        for match in _H002_PATTERN.finditer(text):
            if _nearby_exclusion(text, match.start(), match.end()):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL1-H002",
                    evidence_text=_snippet(text, match),
                    confidence="LOW",
                    rationale=(
                        "A broad subject ('any loss', 'all losses') in an exclusion context "
                        "may override narrow coverage grants without explicit scoping."
                    ),
                    reviewer_question=(
                        "Does this exclusion scope limit 'any' or 'all' to a specific peril or cause, "
                        "or does it sweep broadly across loss types?"
                    ),
                    false_positive_risk=(
                        "Very common phrase — high false positive rate. "
                        "Many legitimate exclusions use 'any loss' with appropriate scoping elsewhere."
                    ),
                )

        # H003
        for match in _H003_PATTERN.finditer(text):
            if _nearby_exclusion(text, match.start(), match.end()):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL1-H003",
                    evidence_text=_snippet(text, match),
                    confidence="MEDIUM",
                    rationale=(
                        "Open causation language ('arising out of', 'directly or indirectly') "
                        "stretches the exclusion trigger far beyond proximate cause."
                    ),
                    reviewer_question=(
                        "Does this causation chain have a stopping condition? "
                        "Could a covered peril trigger this exclusion through an indirect causal chain?"
                    ),
                    false_positive_risk=(
                        "Causation language is common in regulatory text describing prohibited practices. "
                        "Confirm the context is a coverage exclusion, not a regulatory prohibition."
                    ),
                )
