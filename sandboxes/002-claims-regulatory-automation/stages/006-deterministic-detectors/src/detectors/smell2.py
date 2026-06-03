"""
Smell 2: Magic Number / Magic Valuation Terms

Heuristics:
  SMELL2-H001: "reasonable/reasonably" in payment/settlement/valuation context
  SMELL2-H002: "current manual/edition/guidelines" without version or date
  SMELL2-H003: "actual cash value/replacement cost/market value" without adjacent definition
"""
from __future__ import annotations

import re
from typing import Generator

from models import Finding, make_finding

SMELL_ID = 2
SMELL_NAME = "Magic Number / Magic Valuation Terms"

_VALUATION_CONTEXT = re.compile(
    r"\b(pay|payment|settle|settlement|value|valued|valuation|loss|claim|reimburse|"
    r"compensat|indemnif|cost|amount|limit|deductible|depreciation|appraisal)\b",
    re.IGNORECASE,
)

_H001_PATTERN = re.compile(r"\breasonabl[ey]\b", re.IGNORECASE)

_H002_PATTERN = re.compile(
    r"\bcurrent\s+(manual|edition|guidelines?|rate|standards?|schedule)\b",
    re.IGNORECASE,
)
_VERSION_ANCHOR = re.compile(
    r"\b(version|edition|dated?|effective|v\d|rev\.?|filing\s+no|docket)\b",
    re.IGNORECASE,
)

_H003_TERMS = re.compile(
    r"\b(actual\s+cash\s+value|replacement\s+cost(?:\s+value)?|market\s+value|"
    r"fair\s+market\s+value|agreed\s+value|stated\s+value)\b",
    re.IGNORECASE,
)
_DEFINITION_ANCHOR = re.compile(
    r"\b(means|is\s+defined|shall\s+mean|defined\s+as|as\s+defined|"
    r"determined\s+by|calculated\s+(?:as|by|using)|formula|methodology)\b",
    re.IGNORECASE,
)

_WINDOW = 300

# H001 and H003 fire only on carrier documents where "reasonable" / valuation terms
# are dispute gates, not regulatory/statutory language with established legal meaning.
_CARRIER_SOURCE_TYPES = {
    "serff_form_filing",
    "serff_rate_rule_filing",
    "serff_correspondence",
}


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

        source_type = node.get("source_type", "")

        # H001: reasonable in valuation context — carrier docs only
        for m in _H001_PATTERN.finditer(text):
            if source_type not in _CARRIER_SOURCE_TYPES:
                continue
            window = _window_around(text, m)
            if _VALUATION_CONTEXT.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL2-H001",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        "'Reasonable' without a defined standard or formula is a magic valuation term. "
                        "A claimant or reviewer cannot compute what satisfies this requirement."
                    ),
                    reviewer_question=(
                        "Is 'reasonable' defined or anchored to a measurable standard anywhere in this "
                        "document or a referenced filing? If not, how does a claimant know when the "
                        "insurer's response meets this threshold?"
                    ),
                    false_positive_risk=(
                        "'Reasonable' has an accepted legal meaning in many contexts (e.g., "
                        "'reasonable time' in statutory notice requirements). "
                        "Confirm the term is applied to a quantifiable obligation."
                    ),
                    finding_counter=counter,
                )

        # H002: unversioned current reference
        for m in _H002_PATTERN.finditer(text):
            window = _window_around(text, m)
            if not _VERSION_ANCHOR.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL2-H002",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        f"'{m.group(0)}' references a document or standard without a version, "
                        "date, or filing anchor. The referenced content can change without notice, "
                        "making the rate or rule unauditable at the time of loss."
                    ),
                    reviewer_question=(
                        "Which specific edition or version of this manual/guidelines is in effect "
                        "at the time of a claim? Is that version publicly filed?"
                    ),
                    false_positive_risk=(
                        "May fire when the version anchor appears in a nearby section not captured "
                        "in the current node window."
                    ),
                    finding_counter=counter,
                )

        # H003: valuation term without definition — carrier docs only
        seen_terms = set()
        for m in _H003_TERMS.finditer(text):
            if source_type not in _CARRIER_SOURCE_TYPES:
                continue
            term = m.group(0).lower()
            if term in seen_terms:
                continue
            seen_terms.add(term)
            window = _window_around(text, m)
            if not _DEFINITION_ANCHOR.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL2-H003",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        f"'{m.group(0)}' is used without an adjacent definition, formula, or "
                        "methodology reference. Without a calculation rule, the valuation is "
                        "discretionary and unverifiable."
                    ),
                    reviewer_question=(
                        f"How is '{m.group(0)}' calculated? Is the methodology defined in this "
                        "document, a referenced filing, or a filed rate manual? "
                        "Can a claimant reproduce the calculation?"
                    ),
                    false_positive_risk=(
                        "The term may be defined in a different section of the same document "
                        "not captured in the current node. Check sibling nodes."
                    ),
                    finding_counter=counter,
                )
