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

## Re-open Decision — 2026-06-04

Stage 005 is formally reopened. All three re-open conditions are met:

1. ✅ Second carrier corpus (KFBM, 11 documents) — met 2026-06-03
2. ✅ Documented BM25 failure — Smell 5 detector produces zero findings across 353 nodes; regex/lexical cannot surface regulatory-mapping smell in carrier policy language
3. ✅ Paraphrase-style gold set queries approved — five reviewer-perspective Smell 5 queries ready for gold set pairing

**Next steps:**
- [ ] Pair the five Smell 5 paraphrase queries with expected nodes from run `18b0dec5`; add as new gold set items to `goldset-002.2.json`
- [ ] Re-embed 353 nodes from run `18b0dec5` (prior cache was 251 nodes on run `996e36af`)
- [ ] Re-run semantic evaluator against updated gold set
- [ ] Record whether semantic retrieval surfaces Smell 5 candidate nodes that BM25 misses
- [ ] Update ADR-005 (vector store selection) based on result
