"""
Smell 5: Regulatory Mapping Smells

Heuristics:
  SMELL5-H001: "as required by state/applicable/Kentucky law" without KRS/KAR citation
  SMELL5-H002: "as permitted by law / to the extent permitted" without KRS/KAR citation
  SMELL5-H003: KRS reference with only chapter number, no section
"""
from __future__ import annotations

import re
from typing import Generator

from models import Finding, make_finding

SMELL_ID = 5
SMELL_NAME = "Regulatory Mapping Smells"

_KRS_KAR = re.compile(r"\bK[AR]S\s+\d{3}[.\-]\d", re.IGNORECASE)

_H001_PATTERN = re.compile(
    r"\bas\s+required\s+by\s+(state\s+law|applicable\s+law|law|Kentucky\s+law|"
    r"applicable\s+regulations?|statute)\b",
    re.IGNORECASE,
)

_H002_PATTERN = re.compile(
    r"\b(as\s+permitted\s+by\s+law|as\s+allowed\s+by\s+law|"
    r"to\s+the\s+extent\s+permitted\s+(by\s+(applicable\s+)?law)?|"
    r"as\s+authorized\s+by\s+law)\b",
    re.IGNORECASE,
)

# KRS followed by chapter only (e.g. "KRS 304") but NOT a section number
_H003_PATTERN = re.compile(r"\bKRS\s+(\d{2,3})\b(?!\s*[.\-]\d)", re.IGNORECASE)

_WINDOW = 300


def _snippet(text: str, match: re.Match, context: int = 120) -> str:
    start = max(0, match.start() - context)
    end = min(len(text), match.end() + context)
    return text[start:end].strip()


def _window_around(text: str, match: re.Match, size: int = _WINDOW) -> str:
    return text[max(0, match.start() - size): min(len(text), match.end() + size)]


def detect(nodes: list[dict], run_id: str, counter: list[int]) -> Generator[Finding, None, None]:
    for node in nodes:
        if node.get("node_type") == "document":
            continue
        text = node.get("text") or ""
        if not text:
            continue

        # H001: required by law without citation
        for m in _H001_PATTERN.finditer(text):
            window = _window_around(text, m)
            if not _KRS_KAR.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL5-H001",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        f"'{m.group(0)}' asserts a legal requirement without citing the specific "
                        "KRS or KAR provision. Reviewers cannot verify whether the requirement "
                        "is real, current, or correctly interpreted."
                    ),
                    reviewer_question=(
                        "Which specific KRS or KAR provision creates this requirement? "
                        "Is the provision currently in force? "
                        "Does the insurer's implementation match the statutory or regulatory text?"
                    ),
                    false_positive_risk=(
                        "General preambles and recitals commonly reference 'applicable law' without "
                        "a specific citation. The smell is stronger when the phrase governs a "
                        "substantive obligation (payment timing, notice, valuation)."
                    ),
                    finding_counter=counter,
                )

        # H002: permitted by law without citation
        for m in _H002_PATTERN.finditer(text):
            window = _window_around(text, m)
            if not _KRS_KAR.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL5-H002",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="LOW",
                    rationale=(
                        f"'{m.group(0)}' invokes permissive authority without citing the specific "
                        "KRS or KAR provision. Without a citation, the scope of the permission "
                        "cannot be verified."
                    ),
                    reviewer_question=(
                        "Which law or regulation permits this? "
                        "Does the permission have limits that are not stated here?"
                    ),
                    false_positive_risk=(
                        "Common boilerplate in regulatory filings. Many instances are standard "
                        "without being a smell. Higher risk when the permission relates to "
                        "limiting coverage or increasing rates."
                    ),
                    finding_counter=counter,
                )

        # H003: chapter-only KRS citation
        for m in _H003_PATTERN.finditer(text):
            yield make_finding(
                run_id=run_id,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id="SMELL5-H003",
                node=node,
                evidence_text=_snippet(text, m),
                confidence="LOW",
                rationale=(
                    f"'KRS {m.group(1)}' is a chapter-level citation with no section number. "
                    "A chapter can span hundreds of provisions — this citation provides no "
                    "actionable regulatory anchor for a reviewer."
                ),
                reviewer_question=(
                    f"Which specific section of KRS {m.group(1)} applies here? "
                    "Is the full section number available in the source document?"
                ),
                false_positive_risk=(
                    "Chapter-level citations are appropriate in preambles and authority blocks "
                    "where a general statutory grant is being cited, not a specific obligation."
                ),
                finding_counter=counter,
            )
