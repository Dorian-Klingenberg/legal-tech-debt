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
