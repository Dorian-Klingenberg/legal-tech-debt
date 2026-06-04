# ADR-002: Semantic Vector Retrieval Is Expected But Store Selection Is Deferred

Date: 2026-06-01
Status: Accepted
Scope: Legal RAG Builder skill architecture; first applied to Sandbox 002

## Context

The RAG subsystem will need semantic retrieval for questions where legally relevant language appears in different words across policies, endorsements, bulletins, statutes, and manuals.

Examples likely to need semantic retrieval include:

- broad exclusion language
- valuation and calculation terms
- matching and replacement language
- coverage grants hollowed out by exclusions
- regulatory mapping phrases such as "per state law"
- claim denial or underwriting language that expresses the same concept without matching exact phrases

However, the sandbox is still proof-of-concept work. Starting with a vector database risks turning an evidence-model question into an infrastructure question too early.

## Decision

Semantic/vector retrieval remains an expected subsystem, but it will be added after the legal-structure substrate and retrieval bundle contract are stable.

The build order is:

1. file-backed sources, nodes, citations, references, and edges
2. exact phrase, lexical, metadata, and graph-expanded retrieval bundles
3. tiny gold-set evaluation
4. semantic retrieval experiment
5. retrieval store decision

No vector store is selected in Phase 1.

Possible later stores:

- SQLite FTS5 for embedded lexical retrieval and local inspectability
- Qdrant for hybrid dense/sparse retrieval quality experiments
- Postgres plus pgvector if relational joins, metadata, citations, and graph edges dominate

## Consequences

Positive:

- semantic retrieval is preserved as part of the architecture
- vector store choice is tied to measured retrieval needs
- the first stages remain local, readable, and rollback-friendly
- graph and provenance remain attached to semantic hits

Tradeoffs:

- no immediate vector search in the first stage
- Phase 1 cannot answer semantic recall questions
- an additional evaluation stage is required before choosing Qdrant or pgvector

## Rejected Alternatives

- Drop semantic retrieval entirely.
- Choose Qdrant before the node model and gold set exist.
- Choose Postgres plus pgvector because relational storage is familiar.
- Use vector hits as orphan chunks without graph expansion and provenance.

## Follow-Up

- Add a tiny retrieval gold set before embeddings.
- Record exact/lexical/graph failures that semantic retrieval should address.
- Evaluate Qdrant and Postgres plus pgvector only after semantic retrieval improves the measured workload.

## Status Update — 2026-06-03

Phase 3 gold set evaluation (Stage 004) and Phase 4 semantic experiment (Stage 005) are both complete.

Final metrics (21-item gold set, run 996e36af, corrected after gold set labeling fix):

| Mode | Recall |
|---|---|
| Phrase | 95% (20/21) |
| BM25 | 100% (21/21) |
| Semantic cosine@10 (text-embedding-3-small) | 76% (16/21) |
| Hybrid (any mode) | 100% (21/21) |

**Conclusion: defer vector store selection.**

BM25 is already perfect on this corpus. Semantic retrieval adds nothing on top of BM25 — the 5 items semantic misses are all BM25 hits, and semantic rescues zero items BM25 missed. The 76% semantic recall is not evidence that embeddings are weak; it is evidence that the gold set queries were written using document vocabulary (phrase-matchable), not plain-language paraphrases of legal concepts.

The real gate condition for a vector store is not yet met:

- No gold set items where BM25 fails and a plain-language query would succeed
- No multi-carrier corpus where the same concept appears in different words across policies
- No reviewer-perspective queries (outcome-based, not terminology-based)

**What would re-open this decision:**

1. A second carrier's homeowners policy covering the same smells in different language
2. Gold set items written as plain-English reviewer questions, not document phrases
3. At least one documented case where BM25 misses and a concept-level query would find it

Until those conditions exist, file-backed BM25 + phrase search is the correct retrieval stack.

## Status Update — 2026-06-03 (Evening)

Re-open condition 1 is now partially met: Kentucky Farm Bureau Mutual Insurance Company (KFBM) homeowners filings have been added to the corpus (11 documents, 28-source manifest). Stage 002 re-run produced 353 nodes across two carriers.

However, conditions 2 and 3 remain unmet:

- The gold set (goldset-002.2.json) still uses document-vocabulary queries, not plain-English paraphrases. A query like "refer to the Manual for that state" is phrase-matchable; BM25 finds it trivially. A fair semantic evaluation needs queries like "unversioned rate reference in multi-state coverage" — which a reviewer would actually type.
- No documented BM25 failure has been identified on the expanded corpus.

**Revised status: deferred, re-open conditions 2 and 3 remain unmet.** Do not begin Stage 005 re-evaluation until both are addressed in Sandbox 003 or a later session.
