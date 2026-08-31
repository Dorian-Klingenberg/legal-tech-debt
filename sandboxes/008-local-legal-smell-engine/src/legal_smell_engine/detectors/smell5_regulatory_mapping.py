"""Smell 5: Regulatory Mapping Smells.

The detector preserves the two-tier behavior from Sandbox 002 Stage 006:
lexical citation smells (H001-H003), source-level graph gaps (H004-H006),
and the package-level missing Kentucky amendatory check (H007).
"""
from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Iterator

from ..contracts import DetectionRun, Finding, Node

SMELL_ID = 5
SMELL_NAME = "Regulatory Mapping Smells"

_CARRIER_TYPES = {
    "serff_form_filing",
    "serff_rate_rule_filing",
    "serff_correspondence",
}
_REGULATORY_EDGE_TYPES = {"cites_statute", "cites_regulation", "cites_bulletin"}

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
_H003_PATTERN = re.compile(r"\bKRS\s+(\d{2,3})\b(?!\s*[.\-]\d)", re.IGNORECASE)

_H004_PATTERN = re.compile(
    r"\b(base\s+premium|premium\s+(computation|revision|calculation)|"
    r"rate\s+(change|revision|factor|information|filing)|"
    r"rating\s+factor|deductible\s+factor|"
    r"surcharge|discount\s+factor|classification\s+(factor|code)|"
    r"inflation\s+guard|manual\s+premium|"
    r"in\s+accordance\s+with\s+(the\s+)?following\s+procedures|"
    r"as\s+announced)\b",
    re.IGNORECASE,
)
_H005_PATTERN = re.compile(
    r"\b(mandatory\s+coverage|mandatory\s+endorsement|"
    r"special\s+state\s+requirements?|"
    r"use\s+this\s+endorsement\s+with\s+all|"
    r"required\s+endorsement|"
    r"it\s+shall\s+not\s+be\s+permissible|"
    r"must\s+be\s+endorsed)\b",
    re.IGNORECASE,
)
_H006_PATTERN = re.compile(
    r"\b(actual\s+cash\s+value|replacement\s+cost\s+(coverage|basis|value)?|"
    r"loss\s+settlement|depreciation\s+(method|basis|applied|calculated)?|"
    r"cost\s+to\s+repair\s+or\s+replace|"
    r"index\s+of\s+construction\s+costs?|"
    r"national\s+appraisal\s+company)\b",
    re.IGNORECASE,
)

_WINDOW = 300
_H007_MULTISTATE_PATTERN = re.compile(
    r"\b(state\s+amendatory|all\s+states?|"
    r"state\s+exceptions?|state\s+special\s+provisions?|"
    r"amendatory\s+endorsement|"
    r"[a-z]{2,}\s+amendatory|"
    r"state\s+variations?|"
    r"applicable\s+state\s+endorsements?)\b",
    re.IGNORECASE,
)
_H007_KY_PRESENT_PATTERN = re.compile(
    r"\b(kentucky\s+amendatory|ky\s+amendatory|"
    r"kentucky\s+special\s+provisions?|"
    r"special\s+provisions?\s*[-–—]\s*kentucky|"
    r"amendatory\s*[-–—]\s*kentucky)\b",
    re.IGNORECASE,
)


def _snippet(text: str, match: re.Match[str], context: int = 120) -> str:
    return text[max(0, match.start() - context) : min(len(text), match.end() + context)].strip()


def _window_around(text: str, match: re.Match[str], size: int = _WINDOW) -> str:
    return text[max(0, match.start() - size) : min(len(text), match.end() + size)]


def _first_match_snippet(text: str, pattern: re.Pattern[str], context: int = 120) -> str:
    match = pattern.search(text)
    return _snippet(text, match, context) if match else text[:context].strip()


def _supporting_nodes(node_snippets: list[tuple[Node, str]]) -> list[dict[str, str]]:
    return [
        {
            "node_id": node.node_id,
            "section_path": node.section_path,
            "evidence_text": evidence,
        }
        for node, evidence in node_snippets
    ]


def detect(run: DetectionRun) -> Iterator[Finding]:
    """Yield human-reviewable regulatory-mapping leads for one detection run."""
    nodes = [node for node in run.corpus.nodes if node.node_type != "document" and node.text.strip()]

    # Tier 2: consolidate graph-gap findings by heuristic and source. The
    # representative node/evidence remains the first triggering node; all
    # triggering nodes are retained for reviewer drill-down.
    graph_patterns = (
        ("SMELL5-H004", _H004_PATTERN),
        ("SMELL5-H005", _H005_PATTERN),
        ("SMELL5-H006", _H006_PATTERN),
    )
    graph_buckets: dict[str, dict[str, list[tuple[Node, str]]]] = {
        heuristic_id: defaultdict(list) for heuristic_id, _ in graph_patterns
    }

    for node in nodes:
        if node.source_type not in _CARRIER_TYPES:
            continue
        if run.corpus.has_edge_within(node.node_id, _REGULATORY_EDGE_TYPES, hops=2):
            continue
        for heuristic_id, pattern in graph_patterns:
            if pattern.search(node.text):
                graph_buckets[heuristic_id][node.source_id].append(
                    (node, _first_match_snippet(node.text, pattern))
                )

    graph_metadata = {
        "SMELL5-H004": (
            "MEDIUM",
            "This carrier filing contains rate-setting or premium-computation nodes "
            "with no traceable edge to a KRS statute, KAR regulation, or DOI bulletin. "
            "The regulatory basis for these rate rules cannot be verified from the filing. "
            "See supporting_nodes for the full list of affected sections.",
            "Which KRS provision, KAR regulation, or DOI filing approval authorizes or "
            "governs the rate and premium rules in this filing? "
            "Is the specific version of the governing authority identifiable?",
            "Many rate manual rules are actuarially derived rather than directly mandated "
            "by statute. The smell is strongest for rules that set thresholds, factors, or "
            "methodologies affecting claim payments or coverage eligibility.",
        ),
        "SMELL5-H005": (
            "MEDIUM",
            "This carrier filing contains mandatory-coverage or mandatory-endorsement claims "
            "with no traceable edge to a regulatory source. "
            "The provision making these coverages or endorsements mandatory cannot be verified.",
            "Which specific statute or regulation makes these coverages or endorsements mandatory? "
            "Can each requirement be traced to a specific KRS section, KAR provision, or DOI bulletin?",
            "Two distinct contexts produce mandatory-coverage language: "
            "(1) a statement of provision — a policy clause asserting a coverage or endorsement is required "
            "(real smell if no regulatory citation is present); "
            "(2) a filing instruction — a rate manual or underwriting guideline telling agents or underwriters "
            "how to structure a policy (e.g., 'use this endorsement with all new-business policies'). "
            "The heuristic cannot reliably distinguish these without node-level language context annotation "
            "(see ADR-013). Terms 'special state requirements,' 'use this endorsement with all,' and "
            "'must be endorsed' frequently appear in filing-instruction context — verify the node is a "
            "policy provision, not a rate manual instruction, before escalating. "
            "The smell is strongest when language explicitly implies a state statutory or regulatory mandate.",
        ),
        "SMELL5-H006": (
            "LOW",
            "This carrier filing references loss-settlement methodology (ACV, replacement cost, "
            "depreciation, or an external index) with no traceable edge to KRS or KAR provisions "
            "governing how homeowners losses must be settled in Kentucky.",
            "Which KRS or KAR provision governs this loss-settlement methodology? "
            "Is the methodology consistent with Kentucky regulatory requirements?",
            "High. Loss-settlement terms commonly appear in policy forms without inline regulatory "
            "citations — the citation may exist elsewhere in the filing package. "
            "Treat as a lead for further review, not a confirmed gap.",
        ),
    }
    graph_missing = (
        "No outbound cites_statute, cites_regulation, or cites_bulletin edge was found "
        "within two hops of the triggering node in the supplied evidence graph."
    )

    for heuristic_id, source_map in graph_buckets.items():
        confidence, rationale, reviewer_question, false_positive_risk = graph_metadata[heuristic_id]
        for source_id, node_snippets in source_map.items():
            representative, evidence = node_snippets[0]
            yield run.finding(
                node=representative,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id=heuristic_id,
                evidence_text=evidence,
                confidence=confidence,
                rationale=f"{rationale} ({len(node_snippets)} triggering node(s) in this source.)",
                reviewer_question=reviewer_question,
                false_positive_risk=false_positive_risk,
                missing_evidence=[graph_missing],
                supporting_nodes=_supporting_nodes(node_snippets),
            )

    # H007: package-level missing Kentucky amendatory/special-provisions check.
    multistate_by_source: dict[str, list[tuple[Node, str]]] = defaultdict(list)
    ky_sources: set[str] = set()
    for node in nodes:
        if node.source_type not in _CARRIER_TYPES:
            continue
        if _H007_KY_PRESENT_PATTERN.search(node.text):
            ky_sources.add(node.source_id)
        match = _H007_MULTISTATE_PATTERN.search(node.text)
        if match:
            multistate_by_source[node.source_id].append((node, _snippet(node.text, match)))

    for source_id, node_snippets in multistate_by_source.items():
        if source_id in ky_sources:
            continue
        representative, evidence = node_snippets[0]
        yield run.finding(
            node=representative,
            smell_id=SMELL_ID,
            smell_name=SMELL_NAME,
            heuristic_id="SMELL5-H007",
            evidence_text=evidence,
            confidence="MEDIUM",
            rationale=(
                "This carrier filing package contains language suggesting a multi-state "
                "master jacket or state-variable endorsement structure, but no Kentucky "
                "amendatory or Kentucky special provisions form was found in the package. "
                f"({len(node_snippets)} multi-state cue node(s) detected.)"
            ),
            reviewer_question=(
                "Is there a Kentucky Amendatory Endorsement or Kentucky Special Provisions "
                "form in this filing package or in a related SERFF attachment list? "
                "If this is a multi-state master jacket, 806 KAR 14:006 may require a "
                "state-specific amendatory endorsement for Kentucky. If the base form is "
                "proprietary and Kentucky-only, that should be documented explicitly in the filing."
            ),
            false_positive_risk=(
                "Kentucky-specific provisions may be embedded in a proprietary base form "
                "(e.g., KFBM HO 04 93) that does not use the 'Amendatory' or 'Special Provisions' "
                "label. They may also appear in a separate SERFF filing not present in the current "
                "corpus. Treat as a package-completeness lead requiring manual review, not a "
                "confirmed regulatory gap."
            ),
            missing_evidence=[
                "The supplied carrier nodes contain no Kentucky amendatory or Kentucky special provisions cue; separate attachments or a proprietary base form may be absent."
            ],
            supporting_nodes=_supporting_nodes(node_snippets),
        )

    # Tier 1: lexical findings remain per node and apply to all source types.
    for node in nodes:
        text = node.text
        for match in _H001_PATTERN.finditer(text):
            if not _KRS_KAR.search(_window_around(text, match)):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL5-H001",
                    evidence_text=_snippet(text, match),
                    confidence="MEDIUM",
                    rationale=(
                        f"'{match.group(0)}' asserts a legal requirement without citing the specific "
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
                )

        for match in _H002_PATTERN.finditer(text):
            if not _KRS_KAR.search(_window_around(text, match)):
                yield run.finding(
                    node=node,
                    smell_id=SMELL_ID,
                    smell_name=SMELL_NAME,
                    heuristic_id="SMELL5-H002",
                    evidence_text=_snippet(text, match),
                    confidence="LOW",
                    rationale=(
                        f"'{match.group(0)}' invokes permissive authority without citing the specific "
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
                )

        for match in _H003_PATTERN.finditer(text):
            yield run.finding(
                node=node,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id="SMELL5-H003",
                evidence_text=_snippet(text, match),
                confidence="LOW",
                rationale=(
                    f"'KRS {match.group(1)}' is a chapter-level citation with no section number. "
                    "A chapter can span hundreds of provisions — this citation provides no "
                    "actionable regulatory anchor for a reviewer."
                ),
                reviewer_question=(
                    f"Which specific section of KRS {match.group(1)} applies here? "
                    "Is the full section number available in the source document?"
                ),
                false_positive_risk=(
                    "Chapter-level citations are appropriate in preambles and authority blocks "
                    "where a general statutory grant is being cited, not a specific obligation."
                ),
            )
