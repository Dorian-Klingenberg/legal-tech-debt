"""Extract formal KRS and KAR citations from node text.

KRS pattern:  KRS 304.12-230  KRS 304.1-050(1)  KRS Chapter 304  KRS 304
KAR pattern:  806 KAR 14:006  806 KAR 12:095
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Iterator

import ids as id_gen
from models import SCHEMA_VERSION, Citation, Node

# KRS: "KRS 304.12-230", "KRS 304.1-050(1)", "KRS Chapter 304 Subtitle 14", "KRS 304"
_KRS_RE = re.compile(
    r"\bKRS\s+"
    r"(?:Chapter\s+\d+\s+Subtitle\s+\d+|Chapter\s+\d+|\d{3}(?:\.\d+(?:-\d+)?)?(?:\(\d+\))?)",
    re.IGNORECASE,
)

# KAR: "806 KAR 14:006", "806 KAR 12:095"
_KAR_RE = re.compile(r"\b\d{3}\s+KAR\s+\d+:\d+", re.IGNORECASE)

# Normalization helpers
_KRS_NUM_RE = re.compile(r"KRS\s+(\d{3}(?:\.\d+(?:-\d+)?)?(?:\(\d+\))?)", re.IGNORECASE)
_KAR_NUM_RE = re.compile(r"(\d{3})\s+KAR\s+(\d+):(\d+)", re.IGNORECASE)


def _normalize_krs(raw: str) -> str:
    raw = raw.strip()
    m = re.search(r"Chapter\s+(\d+)\s+Subtitle\s+(\d+)", raw, re.IGNORECASE)
    if m:
        return f"KRS Chapter {m.group(1)} Subtitle {m.group(2)}"
    m = re.search(r"Chapter\s+(\d+)", raw, re.IGNORECASE)
    if m:
        return f"KRS Chapter {m.group(1)}"
    m = _KRS_NUM_RE.search(raw)
    if m:
        return f"KRS {m.group(1)}"
    return raw


def _normalize_kar(raw: str) -> str:
    m = _KAR_NUM_RE.search(raw)
    if m:
        return f"{m.group(1)} KAR {m.group(2)}:{m.group(3)}"
    return raw.strip()


def _chapter_subtitle_section(normalized: str) -> tuple[str | None, str | None, str | None]:
    m = re.match(r"KRS Chapter (\d+) Subtitle (\d+)", normalized, re.IGNORECASE)
    if m:
        return m.group(1), m.group(2), None
    m = re.match(r"KRS Chapter (\d+)", normalized, re.IGNORECASE)
    if m:
        return m.group(1), None, None
    m = re.match(r"KRS (\d{3})\.(\d+)-(\d+)", normalized)
    if m:
        return m.group(1), m.group(2), f"{m.group(2)}-{m.group(3)}"
    m = re.match(r"KRS (\d{3})\.(\d+)", normalized)
    if m:
        return m.group(1), m.group(2), None
    m = re.match(r"KRS (\d{3})", normalized)
    if m:
        return m.group(1), None, None
    return None, None, None


def extract_citations(nodes: list[Node], run_id: str) -> list[Citation]:
    now = datetime.now(timezone.utc).isoformat()
    citations: list[Citation] = []
    seen: set[str] = set()

    for node in nodes:
        text = node.text

        for match in _KRS_RE.finditer(text):
            raw = match.group(0).strip()
            normalized = _normalize_krs(raw)
            key = f"{node.node_id}::krs::{normalized}"
            if key in seen:
                continue
            seen.add(key)
            chapter, subtitle, section_number = _chapter_subtitle_section(normalized)
            cid = id_gen.citation_id(node.node_id, raw)
            citations.append(Citation(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                citation_id=cid,
                source_id=node.source_id,
                node_id=node.node_id,
                citation_type="krs_statute",
                raw_text=raw,
                normalized=normalized,
                chapter=chapter,
                subtitle=subtitle,
                section_number=section_number,
                resolved=True,  # in-corpus source files are presumed resolvable
            ))

        for match in _KAR_RE.finditer(text):
            raw = match.group(0).strip()
            normalized = _normalize_kar(raw)
            key = f"{node.node_id}::kar::{normalized}"
            if key in seen:
                continue
            seen.add(key)
            cid = id_gen.citation_id(node.node_id, raw)
            citations.append(Citation(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                citation_id=cid,
                source_id=node.source_id,
                node_id=node.node_id,
                citation_type="kar_regulation",
                raw_text=raw,
                normalized=normalized,
                chapter=None,
                subtitle=None,
                section_number=None,
                resolved=True,
            ))

    return citations
