"""Smell 2: Magic Number / Magic Valuation Terms."""
from __future__ import annotations

import re
from collections.abc import Iterator

from ..contracts import DetectionRun, Finding, Node

SMELL_ID = 2
SMELL_NAME = "Magic Number / Magic Valuation Terms"
_TARGET_SOURCE_TYPES = {"serff_form_filing", "serff_rate_rule_filing", "serff_correspondence"}
_REASONABLE = re.compile(r"\breasonabl[ey]\b", re.IGNORECASE)
_CURRENT = re.compile(
    r"\b(current\s+(manual|edition|guidelines|rate|standards?)|latest\s+(manual|edition|guidelines))\b",
    re.IGNORECASE,
)
_VALUATION = re.compile(
    r"\b(actual\s+cash\s+value|replacement\s+cost|fair\s+market\s+value|market\s+value)\b",
    re.IGNORECASE,
)
_VERSION = re.compile(r"\b(20\d{2}|v(?:ersion)?\.?\s*\d+(?:\.\d+)*|edition\s+\d+|dated?\s+\w+\s+\d{4})\b", re.IGNORECASE)
_FORMULA = re.compile(r"\b(calculat(?:e|ed|ion)|formula|defined\s+as|means)\b", re.IGNORECASE)
_CONTEXT = re.compile(r"\b(pay|paid|payment|settlement|valuation|loss|claim|time\s+limit|repair|replace)\b", re.IGNORECASE)
_DEFINITIONS = re.compile(r"\bdefinitions?\b", re.IGNORECASE)
_QUOTED_TERM = re.compile(r'["“”]([^"“”]{2,80})["“”]')


def _is_target(node: Node) -> bool:
    return not node.source_type or node.source_type in _TARGET_SOURCE_TYPES


def _snippet(text: str, match: re.Match[str], context: int = 120) -> str:
    return text[max(0, match.start() - context) : min(len(text), match.end() + context)].strip()


def _nearby(text: str, match: re.Match[str], radius: int = 350) -> str:
    return text[max(0, match.start() - radius) : min(len(text), match.end() + radius)]


def _definition_loop(nodes: list[Node], run: DetectionRun) -> Iterator[Finding]:
    defined: set[str] = set()
    for node in nodes:
        if _DEFINITIONS.search(node.section_path) or _DEFINITIONS.search(node.text[:160]):
            for match in _QUOTED_TERM.finditer(node.text):
                defined.add(match.group(1).strip().lower())
    for node in nodes:
        if not _is_target(node) or node.node_type == "document":
            continue
        for term in sorted(defined):
            if re.search(rf"\b{re.escape(term)}\b", node.text, re.IGNORECASE) and (
                _DEFINITIONS.search(node.section_path) or _DEFINITIONS.search(node.text[:160])
            ):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL2-H004",
                    evidence_text=node.text[:240].strip(),
                    confidence="LOW",
                    rationale="A term appears to participate in its own definition domain; verify that the definition adds meaning rather than echoing the term.",
                    reviewer_question="Does this definition resolve the term independently, or does it create a circular definition loop?",
                    false_positive_risk="Quoted terms in a definitions section may be ordinary drafting labels; a literal echo is only a review lead.",
                    missing_evidence=["A typed definition dependency or package-complete base form is not available to this local detector."],
                )


def detect(run: DetectionRun) -> Iterator[Finding]:
    nodes = [node for node in run.corpus.nodes if node.node_type != "document" and node.text.strip() and _is_target(node)]
    yield from _definition_loop(nodes, run)

    for node in nodes:
        text = node.text
        for match in _REASONABLE.finditer(text):
            if not _CONTEXT.search(_nearby(text, match, 220)):
                continue
            yield run.finding(
                node=node,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id="SMELL2-H001",
                evidence_text=_snippet(text, match),
                confidence="MEDIUM",
                rationale="A reasonableness standard appears in a payment, settlement, valuation, or timing context without a computable threshold or defined method.",
                reviewer_question="What objective standard, formula, or documented practice determines what is reasonable here?",
                false_positive_risk="Reasonable may have an accepted legal or procedural meaning; context and surrounding definitions require human review.",
            )

        for match in _CURRENT.finditer(text):
            window = _nearby(text, match, 180)
            if _VERSION.search(window):
                continue
            yield run.finding(
                node=node,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id="SMELL2-H002",
                evidence_text=_snippet(text, match),
                confidence="MEDIUM",
                rationale="A current or latest manual, edition, guideline, rate, or standard is referenced without a nearby version or date anchor.",
                reviewer_question="Which edition or version applied at the relevant policy or claim date?",
                false_positive_risk="A version may be anchored elsewhere in the filing package or source metadata.",
                missing_evidence=["The detector received no package-level version manifest."],
            )

        for match in _VALUATION.finditer(text):
            window = _nearby(text, match, 260)
            if _FORMULA.search(window):
                continue
            yield run.finding(
                node=node,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id="SMELL2-H003",
                evidence_text=_snippet(text, match),
                confidence="MEDIUM",
                rationale="A valuation term is used without an adjacent calculation method, formula, or definition in the supplied evidence.",
                reviewer_question="Where is this valuation term defined, and what calculation method applies at the relevant date?",
                false_positive_risk="The term may be defined in a base form, endorsement, or external manual not included in the input.",
                missing_evidence=["The detector received only the supplied node window, not the complete policy package."],
            )
