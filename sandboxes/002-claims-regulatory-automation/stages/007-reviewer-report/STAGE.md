# Stage 007: Reviewer Report

Status: Complete
Depends on: Stage 002 pipeline run output, Stage 003 retrieval package, Stage 006 detector findings

## Completion Checklist

- [x] Assemble findings, candidate evidence, and limitations into reviewer-facing Markdown and HTML.
- [x] Regenerate the preserved report from the current 31-finding output.
- [x] Keep the report framed as human-review evidence, not legal advice.

## Purpose

Assemble detector findings, candidate evidence, and corpus gap information into a
human-readable report for a legal reviewer. The report surfaces patterns for
judgment — it does not claim any policy is unlawful.

## Usage

```
python src/report_builder.py --run-dir ../../output/002/<run_key>
```

Run Stage 006 first (`detector_findings.jsonl` must exist in the run directory).

Outputs are written under `output/007/<run_key>/` at the sandbox root:
- `reviewer_report.html` — single-file dark-theme HTML with Summary, Findings, Corpus Gaps tabs
- `reviewer_report.md` — plain-text version for diff and version control

## Current results (run 18b0dec5)

- 31 findings from Stage 006 across four currently firing smell families; Smell 3 has zero after source-layer filtering
- 121 candidate-evidence items from Stage 002
- 3 corpus-gap tiers documented without the obsolete claim that Smell 5 has zero findings
- HTML report: Summary stats, per-smell findings with confidence badges, corpus gap section

## Components

- `src/report_builder.py` — assembler; reads Stage 002 JSONL + Stage 006 findings; writes HTML and MD

## Cross-stage dependencies

- Reads: Stage 002 run output (JSONL artifacts, via RunIndex from Stage 003)
- Reads: Stage 006 `detector_findings.jsonl`
- Writes: `output/007/<run_key>/`
