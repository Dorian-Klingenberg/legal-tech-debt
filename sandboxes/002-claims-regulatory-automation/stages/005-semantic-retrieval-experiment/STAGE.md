# Stage 005: Semantic Retrieval Experiment

Phase: 4 — Semantic Retrieval Experiment
Status: In progress
Depends on: Stage 002 pipeline run output, Stage 003 retrieval package, Stage 004 gold set

## Purpose

Test whether OpenAI embeddings improve recall for the one item that phrase and BM25 both miss:
`eval-011` — DOI Advisory Opinion aerial imagery (`bdfadc8c3e7aec8ab312`).

Gate condition (from ADR-002): tiny gold set exists + documented lexical failures exist. Both are met.

## Usage

```
# Step 1: embed all Stage 002 nodes (cached after first run)
python src/embedder.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>

# Step 2: evaluate against the gold set
python src/semantic_evaluator.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
```

Outputs are written into the Stage 002 run directory:
- `semantic_embeddings.npy` — float32 matrix (nodes × dims)
- `semantic_embed_index.json` — node_id order, model, run_id
- `semantic_evaluation_results.json`
- `semantic_evaluation_report.md`

## Components

- `src/embedder.py` — calls OpenAI text-embedding-3-small; caches to .npy + index JSON
- `src/semantic_searcher.py` — cosine similarity search over cached embeddings
- `src/semantic_evaluator.py` — evaluation runner; writes results and report

## Model

- `text-embedding-3-small` (1536-dim, OpenAI)
- Requires `OPENAI_API_KEY` in `.env` at repo root

## Cross-stage dependencies

- Reads: Stage 002 run output (JSONL artifacts, via RunIndex)
- Reads: Stage 003 `src/retrieval/` package (RunIndex import path)
- Reads: Stage 004 gold set (`data/goldsets/goldset-002.2.json`)
- Writes: into the Stage 002 run directory

## Decision thresholds

| Recall | Decision |
|---|---|
| ≥ 95% | DEFER — lexical is sufficient |
| 80–94% | INVESTIGATE — marginal gains |
| < 80% | PURSUE — earns a vector store ADR |

## Current results (run 996e36af)

| Mode | Recall |
|---|---|
| Phrase | 95% (20/21) |
| BM25 | 100% (21/21) |
| Semantic cosine@10 | 76% (16/21) |
| Hybrid (any) | 100% (21/21) |

**Decision: DEFER** — BM25 is already perfect. Semantic adds nothing on top of BM25 for this corpus.
The 76% semantic recall reflects gold set queries written in document vocabulary (phrase-matchable),
not plain-language paraphrases. A fair semantic evaluation needs paraphrase queries and multi-carrier corpus.
See ADR-002 for re-open conditions.
