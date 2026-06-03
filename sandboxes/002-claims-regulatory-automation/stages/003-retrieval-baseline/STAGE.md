# Stage 003: Retrieval Baseline

Phase: 2 — Retrieval Baseline And Fixture Curation
Status: Complete
Depends on: Stage 002 pipeline run output

## Purpose

Run exact-phrase and BM25 retrieval over a Stage 002 discovery run. Produce
retrieval bundles with graph expansion (parent, siblings, citations, references)
for each of the five active smells. Document corpus gaps where required source
types are absent.

## Usage

```
python src/retrieval_runner.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
```

Outputs are written back into the Stage 002 run directory:
- `retrieval_bundles.json`
- `retrieval_report.md`

## Components

- `src/retrieval/index.py` — in-memory index over JSONL artifacts
- `src/retrieval/searcher.py` — exact phrase + BM25 search
- `src/retrieval/expander.py` — parent/sibling/citation/reference graph expansion
- `src/retrieval/composer.py` — RetrievalBundle assembly
- `src/retrieval_runner.py` — CLI runner; smell-specific queries; corpus gap detection
- `data/goldsets/goldset-002.1.json` — Phase 2 fixture gold set (confirmed interesting items)

## Cross-stage dependencies

- Reads: Stage 002 `src/models.py`, `src/ids.py` (via relative path)
- Reads: Stage 002 run output directory (JSONL artifacts)
- Writes: into the Stage 002 run directory
