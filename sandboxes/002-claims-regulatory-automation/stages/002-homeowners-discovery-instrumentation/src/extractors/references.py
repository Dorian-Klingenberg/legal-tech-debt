"""Extract broader domain references from node text.

Covers: DOI bulletins, DOI advisory opinions, SERFF tracking numbers,
form IDs, manual references, generic law phrases, and internal cross-references.
These are separate records from formal KRS/KAR citations.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

import ids as id_gen
from models import SCHEMA_VERSION, Node, Reference

# DOI Bulletin: "Bulletin 2026-01", "DOI Bulletin 2026-01"
_DOI_BULLETIN_RE = re.compile(r"\bBulletin\s+\d{4}-\d{2,3}\b", re.IGNORECASE)

# DOI Advisory Opinion: "Advisory Opinion 2023-08", "AO 2023-08"
_DOI_AO_RE = re.compile(r"\bAdvisory\s+Opinion\s+\d{4}-\d{2,3}\b", re.IGNORECASE)

# SERFF tracking: typical pattern XXXX-123456789
_SERFF_RE = re.compile(r"\b[A-Z]{3,6}-\d{9,12}\b")

# Form IDs: ISO form-like "HO 00 03 05 11", "ISO HO-3"
_FORM_ID_RE = re.compile(r"\b(?:ISO\s+)?(?:HO|DP|CP|CG|BP|GL)\s*\d{2}[\s\-]\d{2}[\s\-]\d{2}[\s\-]\d{2}(?:\s+\d{2})?\b", re.IGNORECASE)

# Manual references: "the manual", "rate manual", "rating manual", "current manual"
_MANUAL_RE = re.compile(r"\b(?:current\s+)?(?:rate\s+|rating\s+|program\s+|policy\s+|underwriting\s+)?manual\b", re.IGNORECASE)

# Current guideline / current edition
_CURRENT_GUIDELINE_RE = re.compile(r"\bcurrent\s+(?:edition|guidelines?|standards?|rates?|rules?)\b", re.IGNORECASE)

# Generic law phrases (null regulatory references — potential smell 5 hits)
_GENERIC_LAW_RE = re.compile(
    r"\b(?:as\s+required\s+by|pursuant\s+to|in\s+accordance\s+with|as\s+permitted\s+by|as\s+provided\s+by)\s+"
    r"(?:state\s+law|applicable\s+law|Kentucky\s+law|law|applicable\s+regulations?|applicable\s+statutes?)\b",
    re.IGNORECASE,
)

# SERFF (System for Electronic Rate and Form Filing) — system name reference
_SERFF_NAME_RE = re.compile(r"\bSERFF\b")

_PATTERNS: list[tuple[re.Pattern, str]] = [
    (_DOI_BULLETIN_RE, "doi_bulletin"),
    (_DOI_AO_RE, "doi_advisory_opinion"),
    (_SERFF_RE, "serff_tracking"),
    (_FORM_ID_RE, "form_id"),
    (_MANUAL_RE, "manual_reference"),
    (_CURRENT_GUIDELINE_RE, "current_guideline"),
    (_GENERIC_LAW_RE, "generic_law"),
    (_SERFF_NAME_RE, "other"),
]


def extract_references(nodes: list[Node], run_id: str) -> list[Reference]:
    now = datetime.now(timezone.utc).isoformat()
    references: list[Reference] = []
    seen: set[str] = set()

    for node in nodes:
        text = node.text
        for pattern, ref_type in _PATTERNS:
            for match in pattern.finditer(text):
                raw = match.group(0).strip()
                key = f"{node.node_id}::{ref_type}::{raw.lower()}"
                if key in seen:
                    continue
                seen.add(key)

                normalized: str | None = None
                resolved = False
                resolution_note: str | None = None

                if ref_type == "doi_bulletin":
                    normalized = raw.upper()
                    resolution_note = "DOI bulletin — check insurance.ky.gov/ppc for current version"
                elif ref_type == "doi_advisory_opinion":
                    normalized = raw.title()
                    resolution_note = "DOI advisory opinion — check insurance.ky.gov/ppc"
                elif ref_type == "serff_tracking":
                    normalized = raw.upper()
                    resolution_note = "SERFF tracking number — manual retrieval required"
                elif ref_type == "form_id":
                    normalized = re.sub(r"\s+", " ", raw).upper()
                elif ref_type == "manual_reference":
                    resolution_note = "Unversioned manual reference — no version or filing date anchors this reference"
                elif ref_type == "current_guideline":
                    resolution_note = "Unversioned current-edition reference — no version or date anchor"
                elif ref_type == "generic_law":
                    resolution_note = "Generic law reference without KRS/KAR citation — potential Regulatory Mapping Smell"
                elif ref_type == "other":
                    normalized = raw

                rid = id_gen.reference_id(node.node_id, raw)
                references.append(Reference(
                    schema_version=SCHEMA_VERSION,
                    run_id=run_id,
                    created_at=now,
                    reference_id=rid,
                    source_id=node.source_id,
                    node_id=node.node_id,
                    reference_type=ref_type,
                    raw_text=raw,
                    normalized=normalized,
                    resolved=resolved,
                    resolution_note=resolution_note,
                ))

    return references
