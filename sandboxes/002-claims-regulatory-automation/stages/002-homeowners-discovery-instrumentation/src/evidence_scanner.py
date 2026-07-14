"""Scan nodes for candidate evidence of the five active Sandbox 002 smells.

Each heuristic ID maps to a rule defined in data/heuristics.md.
Produces CandidateEvidence records — not findings.
Parser confidence reflects the quality of the source parser run.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import NamedTuple

import ids as id_gen
from models import SCHEMA_VERSION, CandidateEvidence, Node, ParserRun

# ---------------------------------------------------------------------------
# ROI context per smell (lightweight — full ROI is in 002-ROI-CASES-FIVE-SMELLS.md)
# ---------------------------------------------------------------------------
_SMELL_META = {
    1: {
        "name": "Overbroad / Non-deterministic Exclusions",
        "cost_pool": "Underpaid or denied claim disputes; litigation exposure from broad exclusion trigger language",
        "reviewer_question": "Does this exclusion have a defined, bounded trigger, or does the language expand beyond the coverage grant?",
    },
    2: {
        "name": "Magic Number / Magic Valuation Terms",
        "cost_pool": "Valuation disputes; ACV/RCV disagreements; bad-faith exposure from undefined calculation terms",
        "reviewer_question": "Is this term defined in the policy or by a specific versioned standard a reviewer can locate at time of loss?",
    },
    3: {
        "name": "Coverage Inversion / Contradictory Conditions",
        "cost_pool": "Denied claim reversals; coverage ambiguity litigation; regulatory disapproval risk",
        "reviewer_question": "Does this exclusion or condition effectively hollow out the coverage grant? Can both provisions be read consistently?",
    },
    4: {
        "name": "Calculation Rule Drift / Unversioned Rate Reference",
        "cost_pool": "Rate audit exposure; unversioned calculation inputs that change without notice; regulatory rate filing disputes",
        "reviewer_question": "Is the calculation rule or referenced manual anchored to a specific version, edition, or filing date?",
    },
    5: {
        "name": "Regulatory Mapping Smells",
        "cost_pool": "Regulatory compliance penalties; DOI examination findings; null references that cannot be audited",
        "reviewer_question": "Which specific KRS section or KAR provision does this obligation or permission map to? Is the citation complete enough to verify compliance?",
    },
}

# ---------------------------------------------------------------------------
# Heuristic patterns
# ---------------------------------------------------------------------------
class Heuristic(NamedTuple):
    heuristic_id: str
    smell_id: int
    pattern: re.Pattern
    context_pattern: re.Pattern | None  # optional proximity filter
    context_chars: int  # chars to search around match for context_pattern
    why_template: str  # f-string with {match} placeholder


_EXCLUSION_CONTEXT = re.compile(
    r"\bexclud|does\s+not\s+cover|not\s+covered|will\s+not\s+pay|not\s+payable|excluded\b",
    re.IGNORECASE,
)
_COVERAGE_CONTEXT = re.compile(
    r"\bwe\s+(?:will\s+)?(?:pay|cover|insure)\b|coverage\s+(?:is\s+)?provided|insuring\s+agreement",
    re.IGNORECASE,
)

HEURISTICS: list[Heuristic] = [
    # Smell 1
    Heuristic(
        "SMELL1-H001", 1,
        re.compile(r"\bincluding\s+but\s+not\s+limited\s+to\b", re.IGNORECASE),
        _EXCLUSION_CONTEXT, 200,
        'Phrase "including but not limited to" near exclusion language creates a non-exhaustive exclusion list',
    ),
    Heuristic(
        "SMELL1-H002", 1,
        re.compile(r"\bany\s+(?:loss|damage|claim|liability)\b|\ball\s+(?:losses|damages|claims)\b", re.IGNORECASE),
        _EXCLUSION_CONTEXT, 200,
        'Sweeping subject "{match}" near exclusion language may override a bounded coverage grant',
    ),
    Heuristic(
        "SMELL1-H003", 1,
        re.compile(r"\barising\s+(?:from|out\s+of)\s+or\s+related\s+to\b|\bdirectly\s+or\s+indirectly\b", re.IGNORECASE),
        _EXCLUSION_CONTEXT, 200,
        'Open causation language "{match}" near exclusion expands trigger beyond proximate cause',
    ),
    # Smell 2
    Heuristic(
        "SMELL2-H001", 2,
        re.compile(r"\breasonabl[ye]\b", re.IGNORECASE),
        None, 0,
        '"Reasonable" without a defined standard or formula is a magic valuation term',
    ),
    Heuristic(
        "SMELL2-H002", 2,
        re.compile(r"\bcurrent\s+(?:manual|edition|guidelines?|rates?|standards?)\b", re.IGNORECASE),
        None, 0,
        '"Current {match}" without a version or date anchor is an unversioned calculation input',
    ),
    Heuristic(
        "SMELL2-H003", 2,
        re.compile(r"\b(?:actual\s+cash\s+value|replacement\s+cost(?:\s+value)?|fair\s+market\s+value|market\s+value)\b", re.IGNORECASE),
        None, 0,
        'Valuation term "{match}" without an adjacent definition or formula reference',
    ),
    # Smell 3
    Heuristic(
        "SMELL3-H001", 3,
        re.compile(r"\ball\s+(?:risk|direct\s+physical\s+loss|direct\s+loss)\b", re.IGNORECASE),
        re.compile(r"\bexcept\b|\bunless\b|\bsubject\s+to\b|\bnot\s+including\b|\bexclud", re.IGNORECASE), 500,
        'Broad coverage grant "{match}" followed by exception language suggests potential coverage inversion',
    ),
    Heuristic(
        "SMELL3-H002", 3,
        re.compile(r"\bsubject\s+to\s+(?:the\s+)?(?:terms|all\s+terms|any\s+|all\s+)\b|\bexcept\s+as\s+provided\b", re.IGNORECASE),
        _COVERAGE_CONTEXT, 300,
        'Open-ended conditioning phrase "{match}" in coverage context may shift scope without specifying limits',
    ),
    # Smell 4
    Heuristic(
        "SMELL4-H001", 4,
        re.compile(r"\b(?:the\s+)?(?:current\s+)?(?:rate\s+|rating\s+|program\s+|company\s+|bureau\s+)?manual\b", re.IGNORECASE),
        None, 0,
        '"Manual" reference without adjacent version or date — potential unversioned calculation input',
    ),
    Heuristic(
        "SMELL4-H002", 4,
        re.compile(r"\bas\s+amended\b|\bfrom\s+time\s+to\s+time\b|\bas\s+may\s+be\s+amended\b", re.IGNORECASE),
        re.compile(r"\brate\b|\bpremium\b|\bfee\b|\bcalculat|\bformula\b|\bmethod", re.IGNORECASE), 200,
        'Calculation input modified by "{match}" allows silent drift without notice',
    ),
    Heuristic(
        "SMELL4-H003", 4,
        re.compile(r"\b(?:underwriting\s+|rating\s+|internal\s+)?guidelines?\b", re.IGNORECASE),
        None, 0,
        '"Guidelines" reference without version or filing anchor — unversioned calculation dependency',
    ),
    # Smell 5
    Heuristic(
        "SMELL5-H001", 5,
        re.compile(
            r"\bas\s+required\s+by\s+(?:state\s+law|applicable\s+law|Kentucky\s+law|law)\b"
            r"|\bpursuant\s+to\s+(?:state\s+law|applicable\s+law|law)\b",
            re.IGNORECASE,
        ),
        None, 0,
        '"As required by law" phrase without adjacent KRS/KAR citation — null regulatory reference',
    ),
    Heuristic(
        "SMELL5-H002", 5,
        re.compile(
            r"\bas\s+permitted\s+by\s+(?:law|applicable\s+law|state\s+law)\b"
            r"|\bto\s+the\s+extent\s+permitted\s+by\s+(?:law|applicable\s+law)\b",
            re.IGNORECASE,
        ),
        None, 0,
        '"As permitted by law" without a citation — permission scope cannot be verified',
    ),
    Heuristic(
        "SMELL5-H003", 5,
        re.compile(r"\bKRS\s+\d{3}\b(?!\.\d)", re.IGNORECASE),
        None, 0,
        'KRS chapter-only citation without subtitle/section — insufficient regulatory anchor',
    ),
]

# KRS citation check (to filter SMELL5-H001/H002 false positives where a KRS
# citation appears nearby)
_KRS_NEARBY_RE = re.compile(r"\bKRS\s+\d{3}\.\d", re.IGNORECASE)


def _parser_confidence(parser_run: ParserRun | None) -> str:
    if parser_run is None:
        return "low"
    if parser_run.status == "success":
        return "high"
    if parser_run.status == "partial":
        return "medium"
    return "low"


def scan(
    nodes: list[Node],
    parser_runs: list[ParserRun],
    run_id: str,
) -> list[CandidateEvidence]:
    now = datetime.now(timezone.utc).isoformat()
    evidence: list[CandidateEvidence] = []

    # Map source_id → most recent parser run confidence
    run_by_source: dict[str, ParserRun] = {}
    for pr in parser_runs:
        run_by_source[pr.source_id] = pr

    for node in nodes:
        if node.node_type in ("document",):
            continue  # skip root document nodes
        text = node.text
        pr = run_by_source.get(node.source_id)
        pconf = _parser_confidence(pr)

        for h in HEURISTICS:
            for match in h.pattern.finditer(text):
                match_text = match.group(0)
                span_start = match.start()
                span_end = match.end()

                # Apply context filter if defined
                if h.context_pattern is not None:
                    window = h.context_chars
                    ctx_start = max(0, span_start - window)
                    ctx_end = min(len(text), span_end + window)
                    context_window = text[ctx_start:ctx_end]
                    if not h.context_pattern.search(context_window):
                        continue

                # For SMELL5-H001/H002: skip if a proper KRS cite is nearby
                if h.heuristic_id in ("SMELL5-H001", "SMELL5-H002"):
                    ctx_start = max(0, span_start - 150)
                    ctx_end = min(len(text), span_end + 150)
                    if _KRS_NEARBY_RE.search(text[ctx_start:ctx_end]):
                        continue

                why = h.why_template.replace("{match}", match_text)
                eid = id_gen.evidence_id(node.node_id, h.heuristic_id, span_start)
                meta = _SMELL_META[h.smell_id]

                evidence.append(CandidateEvidence(
                    schema_version=SCHEMA_VERSION,
                    run_id=run_id,
                    created_at=now,
                    candidate_id=eid,
                    source_id=node.source_id,
                    source_hash=node.source_hash,
                    node_id=node.node_id,
                    smell_id=h.smell_id,
                    smell_name=meta["name"],
                    heuristic_id=h.heuristic_id,
                    why_flagged=why,
                    evidence_text=text[max(0, span_start - 80):span_end + 80].strip(),
                    evidence_span=[span_start, span_end],
                    parser_confidence=pconf,
                    cost_pool=meta["cost_pool"],
                    reviewer_question=meta["reviewer_question"],
                ))

    return evidence
