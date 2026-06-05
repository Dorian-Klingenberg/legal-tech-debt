"""
Smell 5: Regulatory Mapping Smells

Approach: two-tier detection.

Tier 1 — Lexical (H001-H003): retained for corpora that contain explicit
  "as required by law" type language. Produces zero hits on the current
  carrier-form corpus but kept for completeness.

Tier 2 — Graph gap detection (H004-H006): carrier nodes that make
  regulatory-sounding claims (rate-setting, mandatory coverage,
  loss-settlement methodology) but have no outbound regulatory edge
  (cites_statute, cites_regulation, cites_bulletin) within a 2-hop
  radius from the node or its parent. Absence of a traceable regulatory
  link is the smell. Requires RunIndex to walk the edge graph.

Heuristics:
  H001: "as required by state/applicable/Kentucky law" without KRS/KAR citation
  H002: "as permitted by law / to the extent permitted" without KRS/KAR citation
  H003: KRS reference with only chapter number, no section
  H004: Carrier node makes a rate-setting claim with no regulatory edge
  H005: Carrier node makes a mandatory-coverage/endorsement claim with no regulatory edge
  H006: Carrier node references loss-settlement methodology with no regulatory edge (LOW)

Source-type filtering:
  H004-H006 fire only on carrier source types:
    serff_form_filing, serff_rate_rule_filing, serff_correspondence
  They are suppressed on regulatory sources (krs_statute, kar_regulation,
  doi_bulletin, doi_guidance) where absence of self-citation is expected.
"""
from __future__ import annotations

import re
from typing import Generator, Optional

from models import Finding, make_finding

SMELL_ID = 5
SMELL_NAME = "Regulatory Mapping Smells"

# --- Source type sets ---
_CARRIER_TYPES = {
    "serff_form_filing",
    "serff_rate_rule_filing",
    "serff_correspondence",
}
_REGULATORY_EDGE_TYPES = {"cites_statute", "cites_regulation", "cites_bulletin"}
_REGULATORY_SOURCE_TYPES = {"krs_statute", "kar_regulation", "doi_bulletin", "doi_guidance"}

# --- Tier 1 patterns (lexical) ---
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

# --- Tier 2 patterns (graph gap) ---

# H004: rate-setting claims
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

# H005: mandatory coverage / mandatory endorsement claims
_H005_PATTERN = re.compile(
    r"\b(mandatory\s+coverage|mandatory\s+endorsement|"
    r"special\s+state\s+requirements?|"
    r"use\s+this\s+endorsement\s+with\s+all|"
    r"required\s+endorsement|"
    r"it\s+shall\s+not\s+be\s+permissible|"
    r"must\s+be\s+endorsed|"
    r"is\s+not\s+mandatory)\b",
    re.IGNORECASE,
)

# H006: loss-settlement methodology (lower confidence — high false-positive risk)
_H006_PATTERN = re.compile(
    r"\b(actual\s+cash\s+value|replacement\s+cost\s+(coverage|basis|value)?|"
    r"loss\s+settlement|depreciation\s+(method|basis|applied|calculated)?|"
    r"cost\s+to\s+repair\s+or\s+replace|"
    r"index\s+of\s+construction\s+costs?|"
    r"national\s+appraisal\s+company)\b",
    re.IGNORECASE,
)

_WINDOW = 300

# --- H007 patterns (source-level missing Kentucky amendatory) ---

# Cues that a filing uses a multi-state master jacket or state-variable structure.
_H007_MULTISTATE_PATTERN = re.compile(
    r"\b(state\s+amendatory|all\s+states?|"
    r"state\s+exceptions?|state\s+special\s+provisions?|"
    r"amendatory\s+endorsement|"
    r"[a-z]{2,}\s+amendatory|"
    r"state\s+variations?|"
    r"applicable\s+state\s+endorsements?)\b",
    re.IGNORECASE,
)

# Indicators that a Kentucky amendatory or special-provisions form IS present in the package.
_H007_KY_PRESENT_PATTERN = re.compile(
    r"\b(kentucky\s+amendatory|ky\s+amendatory|"
    r"kentucky\s+special\s+provisions?|"
    r"special\s+provisions?\s*[-–—]\s*kentucky|"
    r"amendatory\s*[-–—]\s*kentucky)\b",
    re.IGNORECASE,
)


def _snippet(text: str, match: re.Match, context: int = 120) -> str:
    start = max(0, match.start() - context)
    end = min(len(text), match.end() + context)
    return text[start:end].strip()


def _window_around(text: str, match: re.Match, size: int = _WINDOW) -> str:
    return text[max(0, match.start() - size): min(len(text), match.end() + size)]


def _has_regulatory_edge(node_id: str, idx, hops: int = 2) -> bool:
    """
    Return True if node_id has a regulatory outbound edge within `hops` hops.
    Uses RunIndex.edges_from (keyed by from_id).
    """
    visited = set()
    frontier = {node_id}
    for _ in range(hops):
        next_frontier = set()
        for nid in frontier:
            if nid in visited:
                continue
            visited.add(nid)
            for edge in idx.edges_from.get(nid, []):
                if edge.get("edge_type") in _REGULATORY_EDGE_TYPES:
                    return True
                next_frontier.add(edge.get("to_id", ""))
        frontier = next_frontier - visited
    return False


def _first_match_snippet(text: str, pattern: re.Pattern, context: int = 120) -> str:
    m = pattern.search(text)
    if not m:
        return text[:context].strip()
    return _snippet(text, m, context)


def detect(
    nodes: list[dict],
    run_id: str,
    counter: list[int],
    idx=None,
) -> Generator[Finding, None, None]:
    # --- Tier 2 pre-pass: collect carrier nodes by (source_id, heuristic) ---
    # We emit one consolidated finding per source per heuristic rather than
    # one finding per node, to avoid noise from repetitive rate-manual sections.
    # All triggering nodes are preserved in supporting_nodes for reviewer drill-down.
    from collections import defaultdict

    # h_buckets[heuristic_id][source_id] = list of (node, evidence_snippet)
    h_buckets: dict[str, dict[str, list[tuple[dict, str]]]] = {
        "SMELL5-H004": defaultdict(list),
        "SMELL5-H005": defaultdict(list),
        "SMELL5-H006": defaultdict(list),
    }

    if idx is not None:
        for node in nodes:
            if node.get("node_type") == "document":
                continue
            if node.get("source_type", "") not in _CARRIER_TYPES:
                continue
            text = node.get("text") or ""
            if not text:
                continue
            node_id = node.get("node_id", "")
            source_id = node.get("source_id", "")
            if _has_regulatory_edge(node_id, idx):
                continue
            for heuristic_id, pattern in [
                ("SMELL5-H004", _H004_PATTERN),
                ("SMELL5-H005", _H005_PATTERN),
                ("SMELL5-H006", _H006_PATTERN),
            ]:
                if pattern.search(text):
                    snippet = _first_match_snippet(text, pattern)
                    h_buckets[heuristic_id][source_id].append((node, snippet))

    # Emit one consolidated finding per (heuristic, source)
    _H004_RATIONALE = (
        "This carrier filing contains rate-setting or premium-computation nodes "
        "with no traceable edge to a KRS statute, KAR regulation, or DOI bulletin. "
        "The regulatory basis for these rate rules cannot be verified from the filing. "
        "See supporting_nodes for the full list of affected sections."
    )
    _H004_QUESTION = (
        "Which KRS provision, KAR regulation, or DOI filing approval authorizes or "
        "governs the rate and premium rules in this filing? "
        "Is the specific version of the governing authority identifiable?"
    )
    _H004_FP = (
        "Many rate manual rules are actuarially derived rather than directly mandated "
        "by statute. The smell is strongest for rules that set thresholds, factors, or "
        "methodologies affecting claim payments or coverage eligibility."
    )

    _H005_RATIONALE = (
        "This carrier filing contains mandatory-coverage or mandatory-endorsement claims "
        "with no traceable edge to a regulatory source. "
        "The provision making these coverages or endorsements mandatory cannot be verified."
    )
    _H005_QUESTION = (
        "Which specific statute or regulation makes these coverages or endorsements mandatory? "
        "Can each requirement be traced to a specific KRS section, KAR provision, or DOI bulletin?"
    )
    _H005_FP = (
        "Some endorsements are made mandatory by carrier underwriting policy rather than statute. "
        "The smell is strongest when language implies a state regulatory mandate rather than a carrier choice."
    )

    _H006_RATIONALE = (
        "This carrier filing references loss-settlement methodology (ACV, replacement cost, "
        "depreciation, or an external index) with no traceable edge to KRS or KAR provisions "
        "governing how homeowners losses must be settled in Kentucky."
    )
    _H006_QUESTION = (
        "Which KRS or KAR provision governs this loss-settlement methodology? "
        "Is the methodology consistent with Kentucky regulatory requirements?"
    )
    _H006_FP = (
        "High. Loss-settlement terms commonly appear in policy forms without inline regulatory "
        "citations — the citation may exist elsewhere in the filing package. "
        "Treat as a lead for further review, not a confirmed gap."
    )

    h_meta = {
        "SMELL5-H004": ("MEDIUM", _H004_RATIONALE, _H004_QUESTION, _H004_FP),
        "SMELL5-H005": ("MEDIUM", _H005_RATIONALE, _H005_QUESTION, _H005_FP),
        "SMELL5-H006": ("LOW",    _H006_RATIONALE, _H006_QUESTION, _H006_FP),
    }

    for heuristic_id, source_map in h_buckets.items():
        confidence, rationale, reviewer_question, false_positive_risk = h_meta[heuristic_id]
        for source_id, node_snippets in source_map.items():
            if not node_snippets:
                continue
            # Representative node: first hit; evidence: first snippet
            rep_node, rep_snippet = node_snippets[0]
            supporting = [
                {
                    "node_id": n["node_id"],
                    "section_path": n.get("section_path", ""),
                    "evidence_text": s,
                }
                for n, s in node_snippets
            ]
            yield make_finding(
                run_id=run_id,
                smell_id=SMELL_ID,
                smell_name=SMELL_NAME,
                heuristic_id=heuristic_id,
                node=rep_node,
                evidence_text=rep_snippet,
                confidence=confidence,
                rationale=f"{rationale} ({len(node_snippets)} triggering node(s) in this source.)",
                reviewer_question=reviewer_question,
                false_positive_risk=false_positive_risk,
                finding_counter=counter,
                supporting_nodes=supporting,
            )

    # --- H007: source-level missing Kentucky amendatory check ---
    # Single scan over carrier nodes:
    #   - Collect multi-state cue hits grouped by source_id.
    #   - Track which source_ids contain Kentucky amendatory text.
    # Emit one consolidated finding per source where multi-state cues are present
    # but no Kentucky amendatory/special-provisions text is found in the package.
    # No edge graph required — purely text-presence detection.
    _multistate_by_source: dict[str, list[tuple[dict, str]]] = defaultdict(list)
    _ky_sources: set[str] = set()

    for node in nodes:
        if node.get("node_type") == "document":
            continue
        if node.get("source_type", "") not in _CARRIER_TYPES:
            continue
        text = node.get("text") or ""
        if not text:
            continue
        source_id = node.get("source_id", "")
        if _H007_KY_PRESENT_PATTERN.search(text):
            _ky_sources.add(source_id)
        m = _H007_MULTISTATE_PATTERN.search(text)
        if m:
            _multistate_by_source[source_id].append((node, _snippet(text, m)))

    for source_id, node_snippets in _multistate_by_source.items():
        if source_id in _ky_sources:
            continue
        rep_node, rep_snippet = node_snippets[0]
        supporting = [
            {
                "node_id": n["node_id"],
                "section_path": n.get("section_path", ""),
                "evidence_text": s,
            }
            for n, s in node_snippets
        ]
        yield make_finding(
            run_id=run_id,
            smell_id=SMELL_ID,
            smell_name=SMELL_NAME,
            heuristic_id="SMELL5-H007",
            node=rep_node,
            evidence_text=rep_snippet,
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
            finding_counter=counter,
            supporting_nodes=supporting,
        )

    # --- Tier 1: lexical (all source types, per-node as before) ---
    for node in nodes:
        if node.get("node_type") == "document":
            continue
        text = node.get("text") or ""
        if not text:
            continue

        source_type = node.get("source_type", "")

        # --- Tier 1: lexical (all source types) ---

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

        # Tier 2 (H004-H006) is handled by the pre-pass above; no per-node loop needed.
