from __future__ import annotations

import argparse
import uuid
from pathlib import Path

from .contracts import EvidenceCorpus, Node
from .engine import DetectorEngine
from .io import load_corpus, write_findings
from .registry import registered_smells
from .report import render_markdown


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local deterministic legal smell detectors")
    source = parser.add_mutually_exclusive_group(required=False)
    source.add_argument("--nodes", type=Path, help="JSONL file containing generic node records")
    source.add_argument("--text", help="Analyze one text value as a synthetic node")
    parser.add_argument("--edges", type=Path, help="Optional JSONL file containing typed edges")
    parser.add_argument("--run-id", default=None, help="Stable run identity; defaults to a random UUID")
    parser.add_argument("--smell", action="append", dest="smells", help="Smell ID, e.g. SMELL2; repeatable")
    parser.add_argument("--output", type=Path, help="Write findings as JSONL instead of stdout")
    parser.add_argument("--report", type=Path, help="Write a human-readable Markdown report")
    parser.add_argument("--list-smells", action="store_true", help="List registered smell IDs and exit")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.list_smells:
        print("\n".join(registered_smells()))
        return 0
    if not args.nodes and args.text is None:
        _parser().error("one of the arguments --nodes --text is required")
    run_id = args.run_id or uuid.uuid4().hex
    if args.nodes:
        corpus = load_corpus(args.nodes, args.edges, run_id)
    else:
        corpus = EvidenceCorpus(
            run_id=run_id,
            nodes=[Node(node_id="text-001", source_id="cli-text", text=args.text or "", source_type="")],
        )
    findings = DetectorEngine(corpus).run_detectors(args.smells)
    write_findings(findings, args.output)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(render_markdown(findings, run_id), encoding="utf-8")
    return 0
