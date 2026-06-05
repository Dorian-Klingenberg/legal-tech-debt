# Stage 006: Deterministic Pattern Detectors

Status: Complete
Depends on: Stage 002 pipeline run output, Stage 003 retrieval package

## Purpose

Run smell-specific deterministic detectors over Stage 002 nodes. Each detector emits
structured `Finding` records with confidence, rationale, reviewer question, and false
positive risk. Findings are distinct from Stage 002 candidate evidence — they carry
an explicit confidence level and are intended for a reviewer, not just a pipeline.

## Usage

```
python src/detector_runner.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
```

Outputs are written into the Stage 002 run directory:
- `detector_findings.jsonl` — one Finding per line; carries schema_version, run_id, created_at
- `detector_report.md` — human-readable summary by smell and confidence

## Current results (run 18b0dec5, 252 carrier nodes after regulatory filter, 2026-06-05)

| Smell | Name | Findings | HIGH | MEDIUM | LOW |
|---|---|---|---|---|---|
| 1 | Overbroad / Non-deterministic Exclusions | 1 | 0 | 0 | 1 |
| 2 | Magic Number / Magic Valuation Terms | 17 | 0 | 17 | 0 |
| 3 | Coverage Inversion / Contradictory Conditions | 0 | 0 | 0 | 0 |
| 4 | Calculation Rule Drift / Unversioned Rate Reference | 1 | 1 | 0 | 0 |
| 5 | Regulatory Mapping Smells | 12 | 0 | 7 | 5 |
| **Total** | | **31** | **1** | **24** | **6** |

**Note on H007 (SMELL5-H007 — Missing State Amendatory):** Heuristic added 2026-06-05. Zero findings on current corpus. Confirmed correct: multi-state cue patterns (`state amendatory`, `all states`, `amendatory endorsement`, etc.) match zero carrier nodes across KFBM and KNIC. KFBM uses a proprietary Kentucky-specific base form (HO 04 93); KNIC licenses ISO by reference. Neither form set in the current corpus contains multi-state jacket language. H007 will fire if a multi-state master jacket filing is added to the corpus. See BACKLOG-019.

**Note on H004 (SMELL2-H004 — Broken Definitions Loop):** Heuristic added 2026-06-05. Zero findings on current corpus. Confirmed correct: only 4 carrier nodes contain "definitions" in section path or opening text — all are rate manual construction/zone definition sections, not insurance policy Definitions Sections. Only 7 carrier nodes contain any double-quote characters (rate table entries). The base policy forms (KFBM HO 04 93, KNIC HO 00 03) with properly formatted Definitions Sections and defined-term quotation marks are not present in the corpus in parsed form. H004 will fire when those forms are added. See BACKLOG-020.

**BACKLOG-011 structure node filter (2026-06-05):** `_has_substantive_text()` pre-filter added to `detector_runner.py`. Strips section heading from node text, checks remainder >= 50 chars. Result: 109 structure/header nodes skipped (252 → 143 carrier nodes passed to detectors). Total findings unchanged at 31; 0 short-evidence findings (was 2). HIGH finding SMELL4-H001 confirmed intact. Two consolidated Smell 5 findings now show substantive evidence text instead of section headers.

## Components

- `src/models.py` — `Finding` dataclass; `make_finding()` factory
- `src/detectors/smell1.py` — H001, H002, H003 (exclusion patterns)
- `src/detectors/smell2.py` — H001, H002, H003 (valuation terms)
- `src/detectors/smell3.py` — H001, H002 (coverage inversion)
- `src/detectors/smell4.py` — H001, H002, H003 (unversioned rate references)
- `src/detectors/smell2.py` — H001, H002, H003 (valuation terms); H004 (broken definitions loop, 2026-06-05)
- `src/detectors/smell5.py` — H001, H002, H003 (regulatory mapping); H004-H006 (graph gap); H007 (missing state amendatory, 2026-06-05)
- `src/detector_runner.py` — CLI runner; runs all detectors; writes findings and report

## Heuristics

All detectors implement heuristics defined in:
```
stages/002-homeowners-discovery-instrumentation/data/heuristics.md
```
Heuristic IDs and versions are stable across runs within schema_version 1.0.0.

## Cross-stage dependencies

- Reads: Stage 002 run output (JSONL artifacts, via RunIndex from Stage 003)
- Writes: into the Stage 002 run directory
