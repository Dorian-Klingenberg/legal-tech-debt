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

## Current results (run 996e36af, 251 content nodes, 7 sources)

| Smell | Name | Findings | HIGH | MEDIUM | LOW |
|---|---|---|---|---|---|
| 1 | Overbroad / Non-deterministic Exclusions | 0 | 0 | 0 | 0 |
| 2 | Magic Number / Magic Valuation Terms | 13 | 0 | 13 | 0 |
| 3 | Coverage Inversion / Contradictory Conditions | 3 | 0 | 0 | 3 |
| 4 | Calculation Rule Drift / Unversioned Rate Reference | 1 | 1 | 0 | 0 |
| 5 | Regulatory Mapping Smells | 0 | 0 | 0 | 0 |
| **Total** | | **17** | **1** | **13** | **3** |

**Notes on zero-finding smells:**
- Smell 1: No exclusion language in corpus (regulatory/statute sources + rate manual; no base policy form)
- Smell 5: All KRS references in corpus are fully qualified (section numbers present); no null citations found

## Components

- `src/models.py` — `Finding` dataclass; `make_finding()` factory
- `src/detectors/smell1.py` — H001, H002, H003 (exclusion patterns)
- `src/detectors/smell2.py` — H001, H002, H003 (valuation terms)
- `src/detectors/smell3.py` — H001, H002 (coverage inversion)
- `src/detectors/smell4.py` — H001, H002, H003 (unversioned rate references)
- `src/detectors/smell5.py` — H001, H002, H003 (regulatory mapping)
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
