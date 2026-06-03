"""
Smell 4: Calculation Rule Drift / Unversioned Rate Reference

Heuristics:
  SMELL4-H001: "the manual" / "the rating manual" without version or date
  SMELL4-H002: "as amended / from time to time" in rate/premium/fee context
  SMELL4-H003: "guidelines / underwriting guidelines" without version, date, or filing reference
"""
from __future__ import annotations

import re
from typing import Generator

from models import Finding, make_finding

SMELL_ID = 4
SMELL_NAME = "Calculation Rule Drift / Unversioned Rate Reference"

_RATE_CONTEXT = re.compile(
    r"\b(rate|premium|fee|surcharge|discount|factor|charge|price|calculation|"
    r"rating|underwriting|eligib|classif)\b",
    re.IGNORECASE,
)

_H001_PATTERN = re.compile(
    r"\bthe\s+(current\s+)?(rating\s+|company\s+|bureau\s+|homeowners?\s+)?manual\b",
    re.IGNORECASE,
)
_VERSION_ANCHOR = re.compile(
    r"\b(version|edition|dated?|effective|v\d|rev\.?|filing\s+no\.?|docket|"
    r"KY[A-Z]{2}\d{4}|SERFF|tracking\s+no)\b",
    re.IGNORECASE,
)

_H002_PATTERN = re.compile(
    r"\b(as\s+amended|from\s+time\s+to\s+time|as\s+may\s+be\s+amended|"
    r"as\s+it\s+may\s+be\s+amended|as\s+revised)\b",
    re.IGNORECASE,
)

_H003_PATTERN = re.compile(
    r"\b(underwriting\s+guidelines?|rating\s+guidelines?|guidelines?)\b",
    re.IGNORECASE,
)
_FILING_ANCHOR = re.compile(
    r"\b(filed|filing|docket|SERFF|approved|version|edition|dated?|effective|"
    r"KRS|KAR|bulletin|circular)\b",
    re.IGNORECASE,
)

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

        # H001: unversioned manual reference
        for m in _H001_PATTERN.finditer(text):
            window = _window_around(text, m)
            if not _VERSION_ANCHOR.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL4-H001",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="HIGH",
                    rationale=(
                        f"'{m.group(0)}' references a manual without a specific version, edition, "
                        "date, or filing number. The applicable rate or rule may change without "
                        "notice, making it unauditable at the time of loss."
                    ),
                    reviewer_question=(
                        "Which specific version or edition of this manual was in effect at the "
                        "time of the loss? Is that version publicly filed with the DOI? "
                        "Does the SERFF filing include the full manual text?"
                    ),
                    false_positive_risk=(
                        "A version anchor may exist in a nearby section or in the SERFF filing "
                        "index rather than the manual text itself."
                    ),
                    finding_counter=counter,
                )

        # H002: as-amended calculation input
        for m in _H002_PATTERN.finditer(text):
            window = _window_around(text, m)
            if _RATE_CONTEXT.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL4-H002",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        f"'{m.group(0)}' in a rate or calculation context means the input can be "
                        "silently changed without a new filing, creating drift between the rate "
                        "on file and the rate actually applied."
                    ),
                    reviewer_question=(
                        "When this rate or calculation input is amended, is a new DOI filing "
                        "required? Is there a process for notifying policyholders of the change?"
                    ),
                    false_positive_risk=(
                        "'As amended' is standard statutory boilerplate for references to statutes "
                        "and regulations. In that context it is expected and not a smell."
                    ),
                    finding_counter=counter,
                )

        # H003: unanchored guidelines reference
        for m in _H003_PATTERN.finditer(text):
            window = _window_around(text, m)
            if not _FILING_ANCHOR.search(window):
                yield make_finding(
                    run_id=run_id,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL4-H003",
                    node=node,
                    evidence_text=_snippet(text, m),
                    confidence="MEDIUM",
                    rationale=(
                        f"'{m.group(0)}' is referenced without a version, date, or filing anchor. "
                        "Unversioned guidelines used as rate or eligibility inputs create invisible "
                        "dependencies that cannot be audited."
                    ),
                    reviewer_question=(
                        "Are these guidelines publicly filed with the DOI? "
                        "What version was in effect at the time of the loss? "
                        "Can a claimant access them?"
                    ),
                    false_positive_risk=(
                        "In regulatory text, guidelines are often expected to be publicly filed. "
                        "Confirm that this is a carrier-internal reference, not a regulatory citation."
                    ),
                    finding_counter=counter,
                )
