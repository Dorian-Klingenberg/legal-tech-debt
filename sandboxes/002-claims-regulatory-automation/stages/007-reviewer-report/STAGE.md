# Stage 007: Reviewer Report

Status: Complete
Depends on: Stage 002 pipeline run output, Stage 003 retrieval package, Stage 006 detector findings

## Purpose

Assemble detector findings, candidate evidence, and corpus gap information into a
human-readable report for a legal reviewer. The report surfaces patterns for
judgment — it does not claim any policy is unlawful.

## Usage

```
python src/report_builder.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
```

Run Stage 006 first (`detector_findings.jsonl` must exist in the run directory).

Outputs are written into the Stage 002 run directory:
- `reviewer_report.html` — single-file dark-theme HTML with Summary, Findings, Corpus Gaps tabs
- `reviewer_report.md` — plain-text version for diff and version control

## Current results (run 996e36af)

- 17 findings from Stage 006 across 5 smells
- 47 candidate evidence items from Stage 002
- 3 corpus gap tiers documented (policy/endorsement/rate)
- HTML report: Summary stats, per-smell findings with confidence badges, corpus gap section

## Components

- `src/report_builder.py` — assembler; reads Stage 002 JSONL + Stage 006 findings; writes HTML and MD

## Cross-stage dependencies

- Reads: Stage 002 run output (JSONL artifacts, via RunIndex from Stage 003)
- Reads: Stage 006 `detector_findings.jsonl`
- Writes: into the Stage 002 run directory
