"""Resolve sandbox-level output paths for downstream stages.

Each stage writes to:
    sandboxes/002-claims-regulatory-automation/output/<stage_num>/<run_id>/

The run_id is read from the Stage 002 run_manifest.json.
"""
from __future__ import annotations

import json
from pathlib import Path


def sandbox_root(stage_src: Path) -> Path:
    """Return the sandbox root from any stage src/ directory."""
    # stage_src is e.g. .../stages/003-retrieval-baseline/src
    return stage_src.resolve().parent.parent.parent


def stage_output_dir(stage_num: str, run_dir: Path) -> Path:
    """Return and create the output directory for a downstream stage run.

    Args:
        stage_num: zero-padded stage number string, e.g. "003"
        run_dir:   path to the Stage 002 timestamped run directory
    """
    manifest_path = run_dir / "run_manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"No run_manifest.json in {run_dir}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    run_id = manifest.get("run_id", run_dir.name)

    # Use the timestamp-prefixed dir name from Stage 002 as the run key
    run_key = run_dir.name  # e.g. 20260603_180716_996e36af

    root = sandbox_root(Path(__file__).parent)
    out = root / "output" / stage_num / run_key
    out.mkdir(parents=True, exist_ok=True)
    return out
