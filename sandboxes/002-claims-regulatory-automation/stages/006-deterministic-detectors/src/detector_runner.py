"""
Stage 006: Deterministic Pattern Detector Runner

Runs all five smell detectors over a Stage 002 run directory and writes:
  - detector_findings.jsonl  (one Finding per line)
  - detector_report.md       (human-readable summary)

Usage:
    python src/detector_runner.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

_STAGE_003_SRC = (
    Path(__file__).resolve().parent.parent.parent
    / "003-retrieval-baseline" / "src"
)
if str(_STAGE_003_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_003_SRC))

_STAGE_006_SRC = Path(__file__).resolve().parent
if str(_STAGE_006_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_006_SRC))

from retrieval.index import RunIndex  # type: ignore
from paths import stage_output_dir  # type: ignore
from models import Finding
from detectors import smell1, smell2, smell3, smell4, smell5

DETECTORS = [smell1, smell2, smell3, smell4, smell5]

SMELL_NAMES = {
    1: "Overbroad / Non-deterministic Exclusions",
    2: "Magic Number / Magic Valuation Terms",
    3: "Coverage Inversion / Contradictory Conditions",
    4: "Calculation Rule Drift / Unversioned Rate Reference",
    5: "Regulatory Mapping Smells",
}


def run_detectors(run_dir: Path) -> list[Finding]:
    print(f"[detector-runner] Loading index from {run_dir}...")
    idx = RunIndex(run_dir)
    # Enrich nodes with source_type from the source registry so detectors can filter by document type.
    source_type_by_id = {s["source_id"]: s.get("source_type", "") for s in idx.sources}
    nodes = [
        {**n, "source_type": source_type_by_id.get(n.get("source_id", ""), "")}
        for n in idx.content_nodes
    ]
    print(f"[detector-runner] {len(nodes)} content nodes")

    counter = [0]
    all_findings: list[Finding] = []

    for detector in DETECTORS:
        smell_id = detector.SMELL_ID
        import inspect
        sig = inspect.signature(detector.detect)
        if "idx" in sig.parameters:
            findings = list(detector.detect(nodes, idx.run_id, counter, idx=idx))
        else:
            findings = list(detector.detect(nodes, idx.run_id, counter))
        all_findings.extend(findings)
        print(f"[detector-runner]   Smell {smell_id}: {len(findings)} findings")

    print(f"[detector-runner] Total: {len(all_findings)} findings")
    return all_findings


def write_findings(findings: list[Finding], run_dir: Path) -> None:
    out_path = stage_output_dir("006", run_dir) / "detector_findings.jsonl"
    lines = [json.dumps(f.to_dict(), ensure_ascii=False) for f in findings]
    out_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    print(f"[detector-runner] Written -> {out_path}")


def write_report(findings: list[Finding], run_dir: Path, run_id: str) -> None:
    out_dir = stage_output_dir("006", run_dir)
    by_smell: dict[int, list[Finding]] = defaultdict(list)
    for f in findings:
        by_smell[f.smell_id].append(f)

    by_confidence: dict[str, int] = defaultdict(int)
    for f in findings:
        by_confidence[f.confidence] += 1

    lines = [
        "# Detector Findings Report",
        "",
        f"Run: `{run_id}`",
        f"Total findings: {len(findings)}",
        f"HIGH: {by_confidence['HIGH']}  MEDIUM: {by_confidence['MEDIUM']}  LOW: {by_confidence['LOW']}",
        "",
        "## Summary By Smell",
        "",
        "| Smell | Name | Findings | HIGH | MEDIUM | LOW |",
        "|---|---|---|---|---|---|",
    ]

    for smell_id in sorted(SMELL_NAMES):
        fs = by_smell.get(smell_id, [])
        h = sum(1 for f in fs if f.confidence == "HIGH")
        m = sum(1 for f in fs if f.confidence == "MEDIUM")
        l = sum(1 for f in fs if f.confidence == "LOW")
        lines.append(f"| {smell_id} | {SMELL_NAMES[smell_id]} | {len(fs)} | {h} | {m} | {l} |")

    lines += ["", "## Findings By Smell", ""]

    for smell_id in sorted(SMELL_NAMES):
        fs = by_smell.get(smell_id, [])
        lines += [f"### Smell {smell_id}: {SMELL_NAMES[smell_id]}", ""]
        if not fs:
            lines += ["No findings.", ""]
            continue
        for f in sorted(fs, key=lambda x: (x.confidence != "HIGH", x.confidence != "MEDIUM", x.node_id)):
            lines += [
                f"#### {f.finding_id} [{f.confidence}] `{f.heuristic_id}`",
                "",
                f"**Source:** {f.source_id}  ",
                f"**Node:** `{f.node_id}`  ",
                f"**Section:** {f.section_path or '—'}",
                "",
                f"**Evidence:**",
                f"> {f.evidence_text.replace(chr(10), ' ')}",
                "",
                f"**Rationale:** {f.rationale}",
                "",
                f"**Reviewer question:** {f.reviewer_question}",
                "",
                f"**False positive risk:** {f.false_positive_risk}",
                "",
                "---",
                "",
            ]

    report_path = out_dir / "detector_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[detector-runner] Written -> {report_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all smell detectors over a Stage 002 run")
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()

    findings = run_detectors(args.run_dir)
    idx = RunIndex(args.run_dir)
    write_findings(findings, args.run_dir)
    write_report(findings, args.run_dir, idx.run_id)

    print()
    print("=" * 60)
    print("DETECTOR SUMMARY")
    print("=" * 60)
    by_smell: dict[int, list] = defaultdict(list)
    for f in findings:
        by_smell[f.smell_id].append(f)
    for smell_id in sorted(SMELL_NAMES):
        fs = by_smell.get(smell_id, [])
        h = sum(1 for f in fs if f.confidence == "HIGH")
        m = sum(1 for f in fs if f.confidence == "MEDIUM")
        l = sum(1 for f in fs if f.confidence == "LOW")
        print(f"  Smell {smell_id}: {len(fs):3d} findings  (H:{h} M:{m} L:{l})")
    print(f"  Total:   {len(findings):3d} findings")
    print("=" * 60)
