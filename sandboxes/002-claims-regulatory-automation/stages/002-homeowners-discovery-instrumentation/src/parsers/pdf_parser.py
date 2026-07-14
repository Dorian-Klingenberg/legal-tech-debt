"""PDF parser using Docling 2.93.0.

Used for true PDFs and for .html files that contain PDF binary content
(KRS statute pages saved with wrong extension).

Returns (parser_run, blocks, block_stats, table_failures, parse_warnings).
"""
from __future__ import annotations

import time
from datetime import datetime, timezone
from pathlib import Path

import ids as id_gen
from models import (
    SCHEMA_VERSION,
    Block,
    BlockStats,
    ParseWarning,
    ParserRun,
    TableFailure,
)

PARSER_NAME = "docling_2.93.0"

# Docling label → block_type mapping
_LABEL_MAP = {
    "title": "heading",
    "section_header": "heading",
    "text": "paragraph",
    "list_item": "list_item",
    "table": "table",
    "caption": "caption",
    "footnote": "paragraph",
    "code": "paragraph",
    "picture": "unknown",
    "page_header": "unknown",
    "page_footer": "unknown",
    "formula": "paragraph",
}


def parse(
    source_id: str,
    source_hash: str,
    path: Path,
    run_id: str,
    extension_mismatch: bool = False,
) -> tuple[ParserRun, list[Block], BlockStats, list[TableFailure], list[ParseWarning]]:
    now = datetime.now(timezone.utc).isoformat()
    prun_id = id_gen.parser_run_id(source_id, PARSER_NAME, run_id)
    t0 = time.perf_counter()

    blocks: list[Block] = []
    table_failures: list[TableFailure] = []
    warnings: list[ParseWarning] = []
    block_index = 0

    def make_block(block_type: str, text: str, level: int | None,
                   page_number: int | None, element_ref: str | None) -> Block:
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

    if extension_mismatch:
        warn(
            "extension_mismatch",
            f"File has .html extension but PDF magic bytes detected; routing to Docling PDF parser. Source: {path.name}",
        )

    try:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        result = converter.convert(str(path))
        doc = result.document
    except Exception as e:
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
            warning_count=len(warnings),
            table_failure_count=0,
            reading_order_uncertain=False,
            notes="Docling conversion failed",
        )
        return pr, [], _empty_stats(source_id, source_hash, prun_id, run_id, now), [], warnings

    # Walk the document items
    reading_order_uncertain = False
    try:
        items = list(doc.iterate_items())
    except AttributeError:
        # Fallback: export to markdown and treat as paragraphs
        try:
            text = doc.export_to_markdown()
            for i, line in enumerate(text.splitlines()):
                line = line.strip()
                if not line:
                    continue
                btype = "heading" if line.startswith("#") else "paragraph"
                text_clean = line.lstrip("#").strip()
                b = make_block(btype, text_clean, None, None, f"markdown_line:{i}")
                blocks.append(b)
        except Exception as e2:
            warn("other", f"Docling export_to_markdown failed: {e2}")
        reading_order_uncertain = True
        items = []

    for item, level in items:
        label = str(getattr(item, "label", "text")).lower()
        text = getattr(item, "text", "") or ""
        text = text.strip()
        if not text:
            continue

        # Page number from provenance
        page_number = None
        try:
            prov = getattr(item, "prov", None) or []
            if prov:
                page_number = getattr(prov[0], "page_no", None)
        except Exception:
            pass

        block_type = _LABEL_MAP.get(label, "unknown")

        # Tables: attempt to get cell text; record failure if unavailable
        if label == "table":
            try:
                table_text = item.export_to_markdown() if hasattr(item, "export_to_markdown") else text
                if not table_text.strip():
                    tf = TableFailure(
                        schema_version=SCHEMA_VERSION,
                        run_id=run_id,
                        created_at=now,
                        failure_id=id_gen.failure_id(source_id, len(table_failures)),
                        source_id=source_id,
                        source_hash=source_hash,
                        parser_run_id=prun_id,
                        block_id=None,
                        failure_type="empty_table",
                        description=f"Table on page {page_number} yielded no text",
                        page_number=page_number,
                    )
                    table_failures.append(tf)
                    continue
                text = table_text
            except Exception as te:
                tf = TableFailure(
                    schema_version=SCHEMA_VERSION,
                    run_id=run_id,
                    created_at=now,
                    failure_id=id_gen.failure_id(source_id, len(table_failures)),
                    source_id=source_id,
                    source_hash=source_hash,
                    parser_run_id=prun_id,
                    block_id=None,
                    failure_type="parse_error",
                    description=f"Table export failed: {te}",
                    page_number=page_number,
                )
                table_failures.append(tf)
                warn("table_parse_failed", f"Table on page {page_number}: {te}")
                continue

        # Skip navigation/boilerplate block types
        if block_type == "unknown":
            continue

        heading_level = level if block_type == "heading" else None
        b = make_block(block_type, text, heading_level, page_number, f"docling:{label}:{block_index}")
        blocks.append(b)

    # Stats
    heading_count = sum(1 for b in blocks if b.block_type == "heading")
    paragraph_count = sum(1 for b in blocks if b.block_type == "paragraph")
    list_item_count = sum(1 for b in blocks if b.block_type == "list_item")
    table_count = sum(1 for b in blocks if b.block_type == "table")
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
        table_count=table_count,
        table_failure_count=len(table_failures),
        empty_block_count=empty_count,
        total_chars=total_chars,
    )

    duration = time.perf_counter() - t0
    status = "failed" if not blocks else ("partial" if warnings or table_failures else "success")
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
        reading_order_uncertain=reading_order_uncertain,
        notes=f"Docling PDF parser; {len(blocks)} blocks; {len(table_failures)} table failures",
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
