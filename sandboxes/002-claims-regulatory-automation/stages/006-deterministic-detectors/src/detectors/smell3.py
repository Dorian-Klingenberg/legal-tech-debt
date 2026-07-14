"""
Smell 3: Coverage Inversion / Contradictory Conditions

Heuristics:
  SMELL3-H001: Broad grant ("all risk", "all direct loss") followed by hollowing language
  SMELL3-H002: Open-ended conditioning ("subject to all terms", "except as provided")
"""
from __future__ import annotations

import re
from typing import Generator

from models import Finding, make_finding

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


def _snippet(text: str, match: re.Match, context: int = 150) -> str:
    start = max(0, match.start() - context)
    end = min(len(text), match.end() + context)
    return text[start:end].strip()


def detect(nodes: list[dict], run_id: str, counter: list[int]) -> Generator[Finding, None, None]:
    for node in nodes:
        if node.get("node_type") == "document":
            continue
        text = node.get("text") or ""
        if not text:
            continue

        # H001: broad grant followed by hollowing language
        for m in _H001_GRANT.finditer(text):
            forward = text[m.end(): min(len(text), m.end() + _HOLLOW_WINDOW)]
            hollow = _H001_HOLLOW.search(forward)
            if hollow:
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL3-H001",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        f"A broad coverage grant ('{m.group(0)}') is followed by hollowing language "
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
                    finding_counter=counter,
                )

        # H002: open-ended conditioning in coverage context
        for m in _H002_PATTERN.finditer(text):
            window = text[max(0, m.start() - 300): min(len(text), m.end() + 300)]
            if _COVERAGE_CONTEXT.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL3-H002",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="LOW",
                    rationale=(
                        f"'{m.group(0)}' conditions coverage on terms that are not scoped or "
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
                    finding_counter=counter,
                )
