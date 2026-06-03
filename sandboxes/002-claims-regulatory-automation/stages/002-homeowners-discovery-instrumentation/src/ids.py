"""Deterministic ID generation for Stage 002 records.

node_id and all derived IDs are stable as long as the parsing
strategy does not change. Strategy changes that break IDs require
a schema_version bump and migration note in STAGE.md.
"""
from __future__ import annotations

import hashlib
import uuid


def run_id() -> str:
    return str(uuid.uuid4())


def node_id(source_id: str, section_path: str) -> str:
    key = f"{source_id}::{section_path}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def block_id(source_id: str, block_index: int) -> str:
    key = f"{source_id}::block::{block_index}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def citation_id(node_id: str, raw_text: str) -> str:
    key = f"{node_id}::cite::{raw_text}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def reference_id(node_id: str, raw_text: str) -> str:
    key = f"{node_id}::ref::{raw_text}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def edge_id(from_id: str, edge_type: str, to_id: str) -> str:
    key = f"{from_id}::{edge_type}::{to_id}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def evidence_id(node_id: str, heuristic_id: str, span_start: int) -> str:
    key = f"{node_id}::evidence::{heuristic_id}::{span_start}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def bundle_id(query: str, node_id: str) -> str:
    key = f"{query}::bundle::{node_id}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def parser_run_id(source_id: str, parser_name: str, run_id: str) -> str:
    key = f"{source_id}::{parser_name}::{run_id}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def warning_id(source_id: str, warning_type: str, index: int) -> str:
    key = f"{source_id}::warn::{warning_type}::{index}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]


def failure_id(source_id: str, index: int) -> str:
    key = f"{source_id}::tablefail::{index}"
    return hashlib.sha256(key.encode()).hexdigest()[:20]
