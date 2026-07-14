"""HTML parser for Kentucky legislature KAR regulation pages.

Targets the specific structure used by apps.legislature.ky.gov:
  <h1 class="citation">  — regulation citation and title
  <div class="metadata-item">  — RELATES TO, STATUTORY AUTHORITY, etc.
  <section class="section" data-level="N">  — numbered sections

Returns (blocks, table_failures, parse_warnings).
"""
from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup

import ids as id_gen
from models import (
    SCHEMA_VERSION,
    Block,
    BlockStats,
    ParseWarning,
    ParserRun,
    TableFailure,
)

PARSER_NAME = "html_bs4_kar_v1"


def parse(
    source_id: str,
    source_hash: str,
    path: Path,
    run_id: str,
) -> tuple[ParserRun, list[Block], BlockStats, list[TableFailure], list[ParseWarning]]:
    now = datetime.now(timezone.utc).isoformat()
    prun_id = id_gen.parser_run_id(source_id, PARSER_NAME, run_id)
    t0 = time.perf_counter()

    blocks: list[Block] = []
    table_failures: list[TableFailure] = []
    warnings: list[ParseWarning] = []
    block_index = 0

    def make_block(block_type: str, text: str, level: int | None = None,
                   element_ref: str | None = None, page_number: int | None = None) -> Block:
        nonlocal block_index
        b = Block(
            schema_version=SCHEMA_VERSION,
            run_id=run_id,
            created_at=now,
            block_id=id_gen.block_id(source_id, block_index),
            source_id=source_id,
            source_hash=source_hash,
            parser_run_id=prun_id,
            block_index=block_index,
            block_type=block_type,
            level=level,
            text=text.strip(),
            page_number=page_number,
            element_ref=element_ref,
            reading_order_uncertain=False,
        )
        block_index += 1
        return b

    def warn(warning_type: str, description: str, block_id: str | None = None) -> None:
        w = ParseWarning(
            schema_version=SCHEMA_VERSION,
            run_id=run_id,
            created_at=now,
            warning_id=id_gen.warning_id(source_id, warning_type, len(warnings)),
            source_id=source_id,
            source_hash=source_hash,
            parser_run_id=prun_id,
            warning_type=warning_type,
            description=description,
            block_id=block_id,
        )
        warnings.append(w)

    try:
        html = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        duration = time.perf_counter() - t0
        pr = ParserRun(
            schema_version=SCHEMA_VERSION,
            run_id=run_id,
            created_at=now,
            parser_run_id=prun_id,
            source_id=source_id,
            source_hash=source_hash,
            parser_name=PARSER_NAME,
            status="failed",
            failure_reason=str(e),
            duration_seconds=round(duration, 3),
            block_count=0,
            warning_count=0,
            table_failure_count=0,
            reading_order_uncertain=False,
            notes="",
        )
        return pr, [], _empty_stats(source_id, source_hash, prun_id, run_id, now), [], []

    soup = BeautifulSoup(html, "html.parser")

    # Pull content from the #regular-content div if present (KAR pages have
    # both a regular and alternate/markup view; we want the regular one).
    content_div = soup.find("div", id="regular-content") or soup.find("div", class_="regulation-content")
    if content_div is None:
        content_div = soup

    # --- Document-level citation heading ---
    citation_h1 = content_div.find("h1", class_="citation")
    if citation_h1:
        header_text = citation_h1.get_text(separator=" ", strip=True)
        b = make_block("citation_header", header_text, level=0, element_ref="h1.citation")
        blocks.append(b)
    else:
        warn("missing_structure", "No <h1 class='citation'> found — may not be a KAR regulation page")

    # --- Metadata items (RELATES TO, STATUTORY AUTHORITY, etc.) ---
    for meta_div in content_div.find_all("div", class_="metadata-item"):
        header_el = meta_div.find(class_="metadata-item-header")
        text_el = meta_div.find(class_="metadata-item-text")
        header_text = header_el.get_text(strip=True) if header_el else ""
        body_text = text_el.get_text(strip=True) if text_el else ""
        if body_text and body_text.strip():
            combined = f"{header_text} {body_text}".strip() if header_text else body_text
            b = make_block("metadata", combined, level=0, element_ref=f"div.metadata-item[{header_text}]")
            blocks.append(b)

    # --- Section elements ---
    table_count = 0
    for section in content_div.find_all("section", class_="section"):
        level_attr = section.get("data-level")
        level = int(level_attr) if level_attr is not None else None
        headers_el = section.find("h2", class_="headers")
        text_el = section.find("span", class_="section-text")
        header_text = headers_el.get_text(strip=True) if headers_el else ""
        body_text = text_el.get_text(strip=True) if text_el else ""

        # Skip sections that are purely whitespace
        full_text = (f"{header_text} {body_text}").strip() if header_text else body_text.strip()
        if not full_text:
            warn("empty_section", f"Empty section at level {level}", block_id=None)
            continue

        # Map level to block_type
        if level == 0:
            btype = "heading"
        elif level == 1:
            btype = "paragraph"
        else:
            btype = "list_item"

        b = make_block(
            btype,
            full_text,
            level=level,
            element_ref=f"section[data-level={level}]",
        )
        blocks.append(b)

    # --- History footer ---
    history = content_div.find("div", class_="history-content")
    if history:
        history_text = history.get_text(strip=True)
        if history_text:
            b = make_block("history", history_text, level=None, element_ref="div.history-content")
            blocks.append(b)

    # Stats
    heading_count = sum(1 for b in blocks if b.block_type == "heading")
    paragraph_count = sum(1 for b in blocks if b.block_type == "paragraph")
    list_item_count = sum(1 for b in blocks if b.block_type == "list_item")
    table_count_actual = sum(1 for b in blocks if b.block_type == "table")
    empty_count = sum(1 for b in blocks if not b.text)
    total_chars = sum(len(b.text) for b in blocks)

    stats = BlockStats(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        source_id=source_id,
        source_hash=source_hash,
        parser_run_id=prun_id,
        total_blocks=len(blocks),
        heading_count=heading_count,
        paragraph_count=paragraph_count,
        list_item_count=list_item_count,
        table_count=table_count_actual,
        table_failure_count=len(table_failures),
        empty_block_count=empty_count,
        total_chars=total_chars,
    )

    duration = time.perf_counter() - t0
    status = "partial" if warnings else "success"
    pr = ParserRun(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        parser_run_id=prun_id,
        source_id=source_id,
        source_hash=source_hash,
        parser_name=PARSER_NAME,
        status=status,
        failure_reason=None,
        duration_seconds=round(duration, 3),
        block_count=len(blocks),
        warning_count=len(warnings),
        table_failure_count=len(table_failures),
        reading_order_uncertain=False,
        notes=f"KAR HTML parsed via BeautifulSoup; {len(blocks)} blocks",
    )
    return pr, blocks, stats, table_failures, warnings


def _empty_stats(source_id: str, source_hash: str, prun_id: str, run_id: str, now: str) -> BlockStats:
    return BlockStats(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        source_id=source_id,
        source_hash=source_hash,
        parser_run_id=prun_id,
        total_blocks=0,
        heading_count=0,
        paragraph_count=0,
        list_item_count=0,
        table_count=0,
        table_failure_count=0,
        empty_block_count=0,
        total_chars=0,
    )
