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

## Status Update — 2026-06-04

All three re-open conditions are now met. Stage 005 is formally reopened.

**Condition 2 — documented BM25 failure:** Smell 5 (Regulatory Mapping) produces zero findings across the entire 353-node corpus. Investigation confirmed that the failure is not a filtering bug — the H001/H002/H003 regex patterns produce zero raw matches. Carrier policy forms and rate manuals do not use "as required by state law" type language; they either cite a specific KRS section directly or don't reference law at all. Lexical/deterministic methods cannot surface regulatory-mapping smell in carrier-form language. This is the BM25 miss that earns semantic retrieval.

**Condition 3 — paraphrase-style gold set queries:** The following reviewer-perspective queries have been approved for addition to the Smell 5 gold set tier:

1. "Does this policy tell me which specific law or regulation requires this provision?"
2. "Which regulatory filing or approval number governs this rate or rule?"
3. "If I needed to verify this against a Kentucky statute, where would I look?"
4. "Does this endorsement explain what regulatory authority permits it to limit coverage this way?"
5. "Is there a traceable link between this policy condition and a filed, approved rule?"

These are example queries representing the reviewer register — outcome-oriented, plain-language — not exhaustive. Each must be paired with an expected node from run `18b0dec5` before the gold set items are finalized.

**Stage 005 re-run completed 2026-06-04. Results:**

- 325 nodes embedded with `text-embedding-3-small`; evaluated against 26-item gold set (21 original + 5 Smell 5 paraphrase items)
- Overall semantic recall: 14/26 (54%) → Decision: PURSUE
- Smell 5 paraphrase items (eval-022 through eval-026): 0/5 hits with both `text-embedding-3-small` and `text-embedding-3-large`
- Model diagnostic confirmed the miss is architectural, not model capability: both models correctly retrieve regulatory source nodes (KAR/KRS) but cannot retrieve carrier policy nodes based on what they *lack*

**Conclusion:** Vector similarity is the wrong tool for gap-detection smells. Smell 5 requires graph-based gap detection — identifying carrier nodes that make regulatory-sounding claims but have no outbound edges to regulatory source nodes. See ADR-010 for the architectural decision.

Vector retrieval remains appropriate for cross-carrier paraphrase matching (future use case) and general evidence retrieval. The vector store selection question is deferred until that use case is active.
