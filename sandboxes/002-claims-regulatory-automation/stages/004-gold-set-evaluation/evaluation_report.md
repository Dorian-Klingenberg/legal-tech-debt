# Stage 002 Retrieval Evaluation Report

Gold set: `goldset-002.2`
Run ID: `unknown`
Created: 2026-06-03T18:26:20.740268+00:00

---

## Overall Results

- Items evaluated: **11**
- Corpus gap tiers (not evaluated): **3**

| Mode | Items Hit | Recall | Avg Rank |
|---|---|---|---|
| phrase | 0/11 | 0% | — |
| bm25 | 0/11 | 0% | — |

### Recall by Smell (any mode)

- **Smell 1** (Overbroad / Non-deterministic Exclusions): 0%
- **Smell 2** (Magic Number / Magic Valuation Terms): 0%
- **Smell 3** (Coverage Inversion / Contradictory Conditions): not evaluated (corpus gap)
- **Smell 4** (Calculation Rule Drift / Unversioned Rate Reference): 0%
- **Smell 5** (Regulatory Mapping Smells): 0%

---

## Item-by-Item Results

### ✗ eval-001 — Smell 2 (doi_bulletin)

**Source**: `KY-DOI-BULLETIN-2026-01` / BULLETIN 2026-01
**Summary**: DOI requirement for 'reasonable investigation' — magic valuation term with no defined threshold
**Expected node**: `4daa7817e31a758c56d8`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `reasonable investigation` | miss | miss |
| `reasonable` | miss | miss |
| `refuse to pay a claim` | miss | miss |

- WARNING: expected_node_id 4daa7817e31a758c56d8 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-002 — Smell 4 (doi_bulletin)

**Source**: `KY-DOI-BULLETIN-2026-01` / BULLETIN 2026-01
**Summary**: DOI reference to 'underwriting guidelines' without requiring those guidelines to be versioned or filed
**Expected node**: `4daa7817e31a758c56d8`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `underwriting guidelines` | miss | miss |
| `guidelines` | miss | miss |
| `nonrenewal` | miss | miss |

- WARNING: expected_node_id 4daa7817e31a758c56d8 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-003 — Smell 2 (kar_regulation)

**Source**: `KY-KAR-806-13-150` / Section 6.
**Summary**: KAR filing requirement referencing replacement cost — the regulatory anchor for valuation terms
**Expected node**: `f01b63bb04e71f0168cf`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `replacement cost` | miss | miss |
| `actual cash value` | miss | miss |
| `replacement cost value` | miss | miss |

- WARNING: expected_node_id f01b63bb04e71f0168cf not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-004 — Smell 2 (kar_regulation)

**Source**: `KY-KAR-806-13-150` / Section 1. Definitions.
**Summary**: KAR definitions section — defines 'loss cost', 'rate', and filing terms; regulatory vocabulary anchor
**Expected node**: `e3a5934b2e3ba1f9b4ae`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `loss cost` | miss | miss |
| `definitions` | miss | miss |
| `rate` | miss | miss |

- WARNING: expected_node_id e3a5934b2e3ba1f9b4ae not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-005 — Smell 5 (kar_regulation)

**Source**: `KY-KAR-806-13-150` / Section 12. Incorporation by Reference.
**Summary**: KAR incorporation by reference section — defines how regulatory anchors are established; the standard a carrier 'applicable law' reference should meet
**Expected node**: `a901b9d3ba6f3f6ec504`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `incorporation by reference` | miss | miss |
| `applicable law` | miss | miss |
| `in accordance with applicable law` | miss | miss |

- WARNING: expected_node_id a901b9d3ba6f3f6ec504 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-006 — Smell 4 (kar_regulation)

**Source**: `KY-KAR-806-13-150` / Section 10.
**Summary**: KAR section on rate/loss cost filings — establishes what versioned rate references look like under regulation
**Expected node**: `76b3bb9916c8e155fe14`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `rate filing` | miss | miss |
| `loss cost` | miss | miss |
| `supplementary rating` | miss | miss |

- WARNING: expected_node_id 76b3bb9916c8e155fe14 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-007 — Smell 2 (kar_regulation)

**Source**: `KY-KAR-806-14-006` / KY-KAR-806-14-006::meta::6fdb16291505b9feefbd
**Summary**: KAR statutory authority block — 'reasonable administrative regulations' without defining reasonableness
**Expected node**: `6e567f744686f431d174`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `reasonable administrative regulations` | miss | miss |
| `reasonable` | miss | miss |
| `commissioner` | miss | miss |

- WARNING: expected_node_id 6e567f744686f431d174 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-008 — Smell 5 (kar_regulation)

**Source**: `KY-KAR-806-14-006` / Section 3.
**Summary**: KAR Section 3 filing requirements — references applicable law; tests whether KRS citations are present
**Expected node**: `832d76b2d75deece7b0a`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `applicable law` | miss | miss |
| `filing requirements` | miss | miss |
| `KRS` | miss | miss |

- WARNING: expected_node_id 832d76b2d75deece7b0a not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-009 — Smell 2 (krs_statute)

**Source**: `KY-KRS-304-14` / 304.14-120   Filing and approval of forms.
**Summary**: KRS form filing statute — 'reasonably to inform the insurer'; the statutory source of the reasonableness standard in claims communication
**Expected node**: `77855c73ea11759acde2`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `filing and approval` | miss | miss |
| `reasonably inform` | miss | miss |
| `grounds therefor` | miss | miss |

- WARNING: expected_node_id 77855c73ea11759acde2 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-010 — Smell 1 (krs_statute)

**Source**: `KY-KRS-304-12-230` / 12-010   Unfair competition -- Unfair, deceptive practices prohibited.
**Summary**: KRS unfair practices statute — lists prohibited practices; tests whether BM25 retrieves this for exclusion-related queries despite parser quality being medium (PDF-as-HTML source)
**Expected node**: `37be60fad2665fbfe5c5`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `unfair deceptive practices` | miss | miss |
| `prohibited practices` | miss | miss |
| `unfair competition` | miss | miss |

- WARNING: expected_node_id 37be60fad2665fbfe5c5 not found in index
- Both modes missed — likely needs semantic retrieval or different query

### ✗ eval-011 — Smell 4 (doi_bulletin)

**Source**: `KY-DOI-AO-2023-08` / Opinion
**Summary**: DOI Advisory Opinion on property inspection and aerial imaging — references insurer practices without versioning requirements
**Expected node**: `bdfadc8c3e7aec8ab312`

| Query | Phrase | BM25 Rank |
|---|---|---|
| `aerial imagery` | miss | miss |
| `property inspection` | miss | miss |
| `available information` | miss | miss |

- WARNING: expected_node_id bdfadc8c3e7aec8ab312 not found in index
- Both modes missed — likely needs semantic retrieval or different query

---

## Corpus Gaps

The following tiers could not be evaluated due to missing source types:

_(See goldset-002.2.json for details)_

---

## Semantic Retrieval Decision

**Decision**: PURSUE — multiple items missed by both modes

11 gold set items were missed by both exact-phrase and BM25 search. These represent queries where semantic similarity might bridge the vocabulary gap. Items missed: eval-001, eval-002, eval-003, eval-004, eval-005, eval-006, eval-007, eval-008, eval-009, eval-010, eval-011.

---

## Retrieval Mode Assessment

| Finding | Implication |
|---|---|
| Exact phrase: high precision, moderate recall | Good for known legal terms; misses paraphrase |
| BM25: moderate precision, higher recall | Catches co-occurrence but noisy on common words ("reasonable", "law") |
| Graph expansion: adds context, not new hits | Valuable for reviewer bundles; doesn't change recall |
| Corpus now includes carrier filings | Form/manual evidence is present; remaining risk is paraphrase-style reviewer queries and Smell 5 calibration |

---

_This report is generated output. Do not edit manually._
_Retrieval results are not legal findings._
