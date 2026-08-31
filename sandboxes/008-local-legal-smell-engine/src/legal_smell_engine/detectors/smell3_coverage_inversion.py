"""Smell 3: Coverage Inversion / Contradictory Conditions."""
from __future__ import annotations

import re
from collections.abc import Iterator

from ..contracts import DetectionRun, Finding, Node

SMELL_ID = 3
SMELL_NAME = "Coverage Inversion / Contradictory Conditions"

_H001_GRANT = re.compile(
    r"\b(all[\s-]+risk|all\s+direct\s+physical\s+loss|all\s+direct\s+loss|"
    r"open[\s-]+peril|risks?\s+of\s+direct\s+physical\s+loss)\b",
    re.IGNORECASE,
)
_H001_HOLLOW = re.compile(
    r"\b(except|unless|subject\s+to|not\s+including|excluding|however|"
    r"provided\s+that|but\s+not|other\s+than)\b",
    re.IGNORECASE,
)

_H002_PATTERN = re.compile(
    r"\b(subject\s+to\s+(the\s+)?terms|subject\s+to\s+all\s+terms|"
    r"subject\s+to\s+any|except\s+as\s+(otherwise\s+)?provided|"
    r"as\s+otherwise\s+limited)\b",
    re.IGNORECASE,
)
_COVERAGE_CONTEXT = re.compile(
    r"\b(cover(age|ed|s)?|insur(ed|ance|es?)|pay|loss|claim|benefit|protect)\b",
    re.IGNORECASE,
)

_HOLLOW_WINDOW = 600


def _snippet(text: str, match: re.Match[str], context: int = 150) -> str:
    start = max(0, match.start() - context)
    end = min(len(text), match.end() + context)
    return text[start:end].strip()


def detect(run: DetectionRun) -> Iterator[Finding]:
    """Yield human-reviewable leads for coverage inversion language."""
    for node in run.corpus.nodes:
        if node.node_type == "document":
            continue
        text = node.text or ""
        if not text:
            continue

        # H001: broad grant followed by hollowing language.
        for match in _H001_GRANT.finditer(text):
            forward = text[match.end() : min(len(text), match.end() + _HOLLOW_WINDOW)]
            hollow = _H001_HOLLOW.search(forward)
            if hollow:
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL3-H001",
                    evidence_text=_snippet(text, match),
                    confidence="MEDIUM",
                    rationale=(
                        f"A broad coverage grant ('{match.group(0)}') is followed by hollowing language "
                        f"('{hollow.group(0)}'). If the exceptions are broader than the grant, "
                        "coverage may be illusory."
                    ),
                    reviewer_question=(
                        "Do the exceptions or conditions following this broad grant effectively "
                        "eliminate coverage for the most common loss scenarios? "
                        "Can a claimant identify a loss that is covered after all exceptions apply?"
                    ),
                    false_positive_risk=(
                        "Structured policies legitimately use broad grants followed by exclusions. "
                        "Human review is required to determine whether the exceptions invert coverage."
                    ),
                )

        # H002: open-ended conditioning in coverage context.
        for match in _H002_PATTERN.finditer(text):
            window = text[max(0, match.start() - 300) : min(len(text), match.end() + 300)]
            if _COVERAGE_CONTEXT.search(window):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL3-H002",
                    evidence_text=_snippet(text, match),
                    confidence="LOW",
                    rationale=(
                        f"'{match.group(0)}' conditions coverage on terms that are not scoped or "
                        "enumerated here. Open-ended conditioning can shift coverage scope "
                        "without specifying the limits of that shift."
                    ),
                    reviewer_question=(
                        "Which specific terms or conditions does this phrase refer to? "
                        "Are those terms defined or filed? Can a claimant locate them?"
                    ),
                    false_positive_risk=(
                        "This is standard policy language in many legitimate forms. "
                        "The smell is when the conditioning terms are themselves undefined or unfiled, "
                        "not when the phrase is used with properly scoped conditions."
                    ),
                )
