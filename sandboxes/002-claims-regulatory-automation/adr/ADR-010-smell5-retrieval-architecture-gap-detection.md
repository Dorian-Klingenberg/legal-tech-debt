# ADR-010: Smell 5 Requires Gap Detection, Not Vector Similarity

Date: 2026-06-04
Status: Accepted
Scope: Sandbox 002 Stage 005 semantic retrieval; Smell 5 detector architecture

---

## Context

Smell 5 (Regulatory Mapping) produces zero deterministic findings across the full 353-node corpus (run `18b0dec5`). Investigation confirmed this is not a filtering bug — the H001/H002/H003 heuristics produce zero raw matches because carrier policy forms do not use "as required by state law" type language. Regulatory-mapping failure in carrier documents takes a different form: provisions that imply regulatory grounding without providing a traceable citation.

Stage 005 was reopened to test whether semantic/vector retrieval could surface these nodes using five reviewer-perspective paraphrase queries (eval-022 through eval-026 in goldset-002.2.json).

A model diagnostic was run comparing `text-embedding-3-small` (1536-dim) and `text-embedding-3-large` (3072-dim) on all five paraphrase queries against all 325 corpus nodes.

**Results:**

| Query | Expected node | small rank | large rank |
|---|---|---|---|
| "Does this policy tell me which specific law or regulation requires this provision?" | `176e1f63ad696b0a8166` (KNIC Special State Requirements) | 22 | 11 |
| "Which regulatory filing or approval number governs this rate or rule?" | `615cdc5d11be8d20f6a2` (KNIC Manual Premium Revision) | 63 | 49 |
| "If I needed to verify this against a Kentucky statute, where would I look?" | `86f5d845167490e38f55` (KNIC Changes or Cancellations) | 277 | 156 |
| "Does this endorsement explain what regulatory authority permits it to limit coverage this way?" | `f68f6a64438a142fa351` (KFBM roof ACV endorsement) | 57 | 11 |
| "Is there a traceable link between this policy condition and a filed, approved rule?" | `edd9e1e74c8a3f4843e9` (KFBM Inflation Guard) | 135 | 57 |

Neither model surfaces any expected node in the top 10. The large model shows marginal improvement in rank on some items but not enough to constitute a retrieval hit.

**Key observation:** Both models consistently retrieve the correct *type* of content — KAR statutory authority blocks, KRS filing sections, regulatory source documents. The semantic signal is working correctly. The problem is that both models rank regulatory source documents (which *answer* the question) higher than carrier policy nodes (which *fail to answer* it). This is expected behavior for cosine similarity — it measures what is present in a node, not what is absent.

---

## Decision

Smell 5 retrieval is an architectural mismatch with vector similarity search. The smell is defined by a *gap* — regulatory traceability is missing from a node — and no embedding model can retrieve a node based on what it does not contain.

The correct architecture for Smell 5 detection is **graph-based gap detection**, not vector similarity:

1. Build a bipartite graph connecting carrier policy nodes to regulatory nodes via citation and reference edges.
2. Identify carrier nodes that make regulatory-sounding claims (rate-setting, mandatory coverage, filing compliance, loss settlement methodology) but have no outbound edges to KRS, KAR, DOI, or SERFF source nodes within a defined hop radius.
3. Surface those carrier nodes as Smell 5 candidates — not because they semantically resemble a regulatory failure, but because the graph shows the expected regulatory link is absent.

This approach uses the existing edge substrate (Stage 002 `edges.jsonl`) rather than adding a vector store. It is deterministic, inspectable, and aligned with the project's evidence-substrate design.

---

## Consequences

**Positive:**
- Smell 5 detector can be rebuilt without vector infrastructure.
- Graph-based gap detection produces inspectable, source-traceable findings.
- Reuses the existing Stage 002 edge substrate — no new data artifacts required.
- Consistent with the project's deferred-vector-infrastructure policy (ADR-002).

**Tradeoffs:**
- Requires defining what constitutes a "regulatory-sounding claim" in carrier nodes — likely a new heuristic set or keyword classifier to identify candidate nodes before gap-checking.
- The graph edge coverage is conservative by design (ADR-004); some regulatory links may be missing from the substrate, producing false negatives.
- Vector similarity remains the right tool for other retrieval tasks (cross-document smell evidence, paraphrase matching across carriers); it is only wrong for gap detection specifically.

---

## Rejected Alternatives

**Use a larger or domain-specific embedding model.**
Tested `text-embedding-3-large`. Marginal rank improvement on some items, zero top-10 hits. The problem is architectural, not model capability. A domain-fine-tuned insurance model would face the same fundamental issue: absence cannot be embedded.

**Use hybrid dense/sparse retrieval (BM25 + embeddings).**
BM25 already produces zero matches for these queries. Adding dense retrieval on top of BM25 does not fix an absence-detection problem. Hybrid retrieval improves recall for paraphrase matching; it does not help when the target node contains no relevant signal.

**Defer Smell 5 entirely.**
Not acceptable. The regulatory traceability pattern is commercially important (market-conduct exams, filing objections, bad-faith exposure). The right answer is to use the correct architecture, not to abandon the smell.

---

## Follow-Up

- [ ] Redesign Smell 5 detector as a graph-based gap detector:
  - Identify carrier nodes making rate-setting, mandatory-coverage, loss-settlement, or filing-compliance claims (new heuristic or keyword classifier)
  - Check each candidate node for outbound edges to KRS, KAR, DOI, or SERFF nodes within a 2-hop radius
  - Surface nodes with no regulatory link as Smell 5 candidates with confidence MEDIUM
- [ ] Update Stage 006 `smell5.py` with the graph-based approach
- [ ] Re-run Stage 006 detectors and Stage 007 reviewer report after Smell 5 redesign
- [ ] Update ADR-002 with the conclusion that vector retrieval is not the right tool for gap-detection smells; note that it remains appropriate for cross-carrier paraphrase matching (a future use case)
- [ ] Update BACKLOG-001 to reflect this architectural decision
