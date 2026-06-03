# Stage 004: Gold Set Evaluation

Phase: 3 — Tiny Gold Set And Retrieval Evaluation
Status: Complete (statute/regulation/DOI tier; policy/endorsement/rate tiers blocked on corpus additions)
Depends on: Stage 002 pipeline run output, Stage 003 retrieval package

## Purpose

Evaluate exact-phrase and BM25 retrieval recall against a structured gold set.
Document failures, missed hits, and false positives. Produce a semantic retrieval
decision (defer/investigate/pursue) based on measured gaps.

## Usage

```
python src/evaluator.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
python src/evaluator.py --run-dir <path> --goldset data/goldsets/goldset-002.2.json
```

Outputs are written back into the Stage 002 run directory:
- `evaluation_results.json`
- `evaluation_report.md`

## Current results (run 996e36af)

- Phrase recall: 90% (19/21 items)
- BM25 recall: 95% (20/21 items)
- Semantic decision: INVESTIGATE — eval-011 (DOI Advisory Opinion aerial imagery) missed by both modes
- Gold set: 21 items across doi_bulletin, kar_regulation, krs_statute, rate_manual_fragments, policy_manual_clauses, endorsement_form_fragments tiers
- Corpus gaps: all three blocked tiers now partial (3–4 items each); full 10/5/5 targets need base policy form and additional endorsements

## Components

- `src/evaluator.py` — evaluation runner
- `data/goldsets/goldset-002.2.json` — 21 evaluation items with expected node IDs and test queries; 3 corpus gap tiers (partial)

## Cross-stage dependencies

- Uses: Stage 003 `src/retrieval/` package (via relative path)
- Reads: Stage 002 run output directory (JSONL artifacts)
- Writes: into the Stage 002 run directory
