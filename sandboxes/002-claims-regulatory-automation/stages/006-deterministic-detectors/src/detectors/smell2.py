"""
Smell 2: Magic Number / Magic Valuation Terms

Heuristics:
  SMELL2-H001: "reasonable/reasonably" in payment/settlement/valuation context
  SMELL2-H002: "current manual/edition/guidelines" without version or date
  SMELL2-H003: "actual cash value/replacement cost/market value" without adjacent definition
"""
from __future__ import annotations

import re
from collections import defaultdict
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

# H004: Definitions Section cross-reference
# Identifies Definitions Section nodes by section_path keyword or opening text.
_DEFINITIONS_SECTION_PAT = re.compile(r"\bdefinitions?\b", re.IGNORECASE)
# Extracts explicitly defined terms: "Term" means / refers to / is defined
_DEFINITION_ENTRY_PAT = re.compile(
    r'"([A-Za-z][^"]{1,59})"\s+(?:means|refer[s]?\s+to|is\s+defined)',
    re.IGNORECASE,
)
# Extracts any quoted string that could be a defined term (body or definitions)
_QUOTED_TERM_PAT = re.compile(r'"([A-Za-z][^"]{1,59})"')

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
    # --- H004 pre-pass: Definitions Section cross-reference ---
    # Scans carrier nodes once to:
    #   1. Extract defined terms from Definitions Section nodes (by section_path or opening text).
    #   2. Collect quoted terms from body nodes.
    # Emits one LOW-confidence finding per (source, term) where a quoted term appears
    # in the policy body but has no matching entry in the same source's Definitions Section.
    # Guards: only fires when a Definitions Section is found AND terms were successfully extracted.

    defs_terms_by_source: dict[str, set[str]] = defaultdict(set)
    sources_with_definitions: set[str] = set()
    body_hits_by_source: dict[str, list[tuple[dict, str, str]]] = defaultdict(list)

    for node in nodes:
        if node.get("node_type") == "document":
            continue
        if node.get("source_type", "") not in _CARRIER_SOURCE_TYPES:
            continue
        text = node.get("text") or ""
        if not text:
            continue
        source_id = node.get("source_id", "")
        section_path = (node.get("section_path") or "").lower()

        is_def_node = (
            "definition" in section_path
            or bool(_DEFINITIONS_SECTION_PAT.search(text[:300]))
        )

        if is_def_node:
            sources_with_definitions.add(source_id)
            # Explicit entries: "Term" means / refers to / is defined
            for m in _DEFINITION_ENTRY_PAT.finditer(text):
                defs_terms_by_source[source_id].add(m.group(1).strip().lower())
            # Collect all quoted strings in the Definitions Section as defined terms
            for m in _QUOTED_TERM_PAT.finditer(text):
                term = m.group(1).strip()
                if len(term) >= 4:
                    defs_terms_by_source[source_id].add(term.lower())
        else:
            # Body node: collect quoted terms for cross-check
            for m in _QUOTED_TERM_PAT.finditer(text):
                term = m.group(1).strip()
                if len(term) >= 4:
                    body_hits_by_source[source_id].append((node, term, _snippet(text, m)))

    # Emit one finding per (source_id, term) missing from Definitions Section
    _seen: set[tuple[str, str]] = set()
    for source_id, hits in body_hits_by_source.items():
        if source_id not in sources_with_definitions:
            continue  # No Definitions Section found — cannot check
        defs = defs_terms_by_source.get(source_id, set())
        if not defs:
            continue  # Definitions Section found but zero terms extracted (parsing gap) — skip
        for node, term, snippet in hits:
            key = (source_id, term.lower())
            if key in _seen or term.lower() in defs:
                continue
            _seen.add(key)
            yield make_finding(
                run_id=run_id,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id="SMELL2-H004",
                node=node,
                evidence_text=snippet,
                confidence="LOW",
                rationale=(
                    f'"{term}" appears as a quoted term in policy body text '
                    "but has no matching entry in the Definitions Section of the same source. "
                    "A reviewer cannot confirm the term's meaning from this filing alone."
                ),
                reviewer_question=(
                    f'Is "{term}" formally defined in this filing, in a related endorsement, '
                    "or in a base form incorporated by reference? "
                    "If it is a defined term, the definition should be traceable from this filing package."
                ),
                false_positive_risk=(
                    "This heuristic is most meaningful for carriers using a PROPRIETARY base form "
                    "(e.g., KFBM HO 04 93) — those carriers own their definition domain and have no "
                    "ISO fallback. For ISO-adopting carriers (e.g., KNIC), missing definitions in "
                    "endorsements are almost certainly covered by ISO HO 00 03 by reference; those "
                    "findings should be downgraded or suppressed during review. "
                    "PDF text extraction may also have altered quotation marks or split a definition "
                    "across nodes. Confidence is LOW — treat as a corpus-completeness lead for "
                    "proprietary-form carriers, not a confirmed gap."
                ),
                finding_counter=counter,
            )

    # --- per-node H001, H002, H003 ---
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
                        "discretionary and unverifiable. Under 806 KAR 12:095 Section 9(2)(a), "
                        "ACV for residential fire and extended coverage losses must be calculated "
                        "as replacement cost minus depreciation. Critically, that regulation "
                        "permits labor depreciation ONLY 'if provided for in the policy' — meaning "
                        "a carrier applying labor depreciation without an explicit policy provision "
                        "authorizing it may be in violation of Kentucky regulation, not merely "
                        "failing a disclosure standard."
                    ),
                    reviewer_question=(
                        f"How is '{m.group(0)}' calculated? Is the methodology defined in this "
                        "document, a referenced filing, or a filed rate manual? "
                        "Can a claimant reproduce the calculation? "
                        "Specifically under 806 KAR 12:095 Section 9(2)(a): does this filing "
                        "contain an explicit provision authorizing labor depreciation? "
                        "If labor is being depreciated without such a provision, the practice "
                        "may violate Kentucky regulation independent of any disclosure question."
                    ),
                    false_positive_risk=(
                        "The term may be defined in a different section of the same document "
                        "not captured in the current node — check sibling nodes. "
                        "806 KAR 12:095 Section 9(2)(a) applies to residential fire and "
                        "extended coverage losses; confirm the claim type before citing this regulation."
                    ),
                    finding_counter=counter,
                )
