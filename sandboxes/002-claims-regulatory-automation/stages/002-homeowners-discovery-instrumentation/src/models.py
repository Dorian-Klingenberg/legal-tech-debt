"""Dataclasses for all Stage 002 record types.

Every record carries schema_version, run_id, and created_at.
Node IDs are deterministic under a fixed parsing strategy.
"""
from __future__ import annotations

from dataclasses import dataclass, field

SCHEMA_VERSION = "1.0.0"
PIPELINE_VERSION = "002.1.0"


@dataclass
class RunManifest:
    schema_version: str
    run_id: str
    created_at: str
    pipeline_version: str
    corpus_root: str
    subset_manifest: str
    source_ids: list[str]
    output_dir: str
    total_sources: int
    parsers_used: list[str]
    schema_versions: dict[str, str]
    config_snapshot: dict
    parse_stats: dict


@dataclass
class Source:
    schema_version: str
    run_id: str
    created_at: str
    source_id: str
    title: str
    source_type: str
    smell_ids: list[int]
    url: str
    downloaded_path: str
    file_bytes: int
    downloaded_at: str
    source_hash: str
    content_hash: str
    detected_file_type: str  # "html" | "pdf" | "unknown"
    extension_matches_type: bool


@dataclass
class ParserRun:
    schema_version: str
    run_id: str
    created_at: str
    parser_run_id: str
    source_id: str
    source_hash: str
    parser_name: str
    status: str  # "success" | "partial" | "failed"
    failure_reason: str | None
    duration_seconds: float
    block_count: int
    warning_count: int
    table_failure_count: int
    reading_order_uncertain: bool
    notes: str


@dataclass
class Block:
    schema_version: str
    run_id: str
    created_at: str
    block_id: str
    source_id: str
    source_hash: str
    parser_run_id: str
    block_index: int
    block_type: str  # "heading"|"paragraph"|"list_item"|"table"|"metadata"|"citation_header"|"history"|"unknown"
    level: int | None
    text: str
    page_number: int | None
    element_ref: str | None
    reading_order_uncertain: bool


@dataclass
class BlockStats:
    schema_version: str
    run_id: str
    created_at: str
    source_id: str
    source_hash: str
    parser_run_id: str
    total_blocks: int
    heading_count: int
    paragraph_count: int
    list_item_count: int
    table_count: int
    table_failure_count: int
    empty_block_count: int
    total_chars: int


@dataclass
class Node:
    schema_version: str
    run_id: str
    created_at: str
    node_id: str
    source_id: str
    source_hash: str
    node_type: str  # "document"|"section"|"subsection"|"clause"|"list_item"|"definition"|"table"|"metadata_block"
    section_path: str
    title: str | None
    text: str
    retrievable_text: str
    page_number: int | None
    element_ref: str | None
    parent_node_id: str | None
    depth: int
    block_ids: list[str]


@dataclass
class Citation:
    schema_version: str
    run_id: str
    created_at: str
    citation_id: str
    source_id: str
    source_hash: str
    node_id: str
    citation_type: str  # "krs_statute" | "kar_regulation"
    raw_text: str
    normalized: str | None
    chapter: str | None
    subtitle: str | None
    section_number: str | None
    resolved: bool


@dataclass
class Reference:
    schema_version: str
    run_id: str
    created_at: str
    reference_id: str
    source_id: str
    source_hash: str
    node_id: str
    reference_type: str
    raw_text: str
    normalized: str | None
    resolved: bool
    resolution_note: str | None


@dataclass
class Edge:
    schema_version: str
    run_id: str
    created_at: str
    edge_id: str
    source_id: str
    source_hash: str
    from_id: str
    from_type: str  # "node" | "citation" | "reference"
    to_id: str
    to_type: str
    edge_type: str
    evidence_text: str | None
    confidence: str  # "high" | "medium" | "low"


@dataclass
class TableFailure:
    schema_version: str
    run_id: str
    created_at: str
    failure_id: str
    source_id: str
    source_hash: str
    parser_run_id: str
    block_id: str | None
    failure_type: str
    description: str
    page_number: int | None


@dataclass
class ParseWarning:
    schema_version: str
    run_id: str
    created_at: str
    warning_id: str
    source_id: str
    source_hash: str
    parser_run_id: str
    warning_type: str
    description: str
    block_id: str | None


@dataclass
class CandidateEvidence:
    schema_version: str
    run_id: str
    created_at: str
    candidate_id: str
    source_id: str
    source_hash: str
    node_id: str
    smell_id: int
    smell_name: str
    heuristic_id: str
    why_flagged: str
    evidence_text: str
    evidence_span: list[int] | None
    parser_confidence: str
    cost_pool: str
    reviewer_question: str


@dataclass
class RetrievalBundle:
    schema_version: str
    run_id: str
    created_at: str
    bundle_id: str
    query_text: str
    task_description: str
    filters: dict
    hits: list[dict]
