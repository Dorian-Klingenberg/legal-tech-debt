# Stage 002 Retrieval Report

Run ID: `unknown`
Created: 2026-06-03T18:26:19.783518+00:00

This report documents what exact-phrase and lexical retrieval modes return
for each of the five active homeowners policy-layer smells.

---

## Corpus Summary


## Corpus Gaps

The following smells cannot be meaningfully evaluated because the required
source types are not present in this corpus slice:

- **Smell 1** (Overbroad / Non-deterministic Exclusions): requires `homeowners_form`, `endorsement` — not present
- **Smell 2** (Magic Number / Magic Valuation Terms): requires `homeowners_form`, `endorsement`, `doi_bulletin`, `kar_regulation` — not present
- **Smell 3** (Coverage Inversion / Contradictory Conditions): requires `homeowners_form`, `endorsement` — not present
- **Smell 4** (Calculation Rule Drift / Unversioned Rate Reference): requires `homeowners_form`, `serff_filing`, `rate_manual` — not present
- **Smell 5** (Regulatory Mapping Smells): requires `homeowners_form`, `endorsement`, `serff_filing` — not present

---

## Results by Smell

### Smell 1: Overbroad / Non-deterministic Exclusions

> **Corpus gap**: Smell 1 requires source types ['homeowners_form', 'endorsement']; corpus only contains [].

No retrieval hits in this corpus slice.

### Smell 2: Magic Number / Magic Valuation Terms

> **Corpus gap**: Smell 2 requires source types ['homeowners_form', 'endorsement', 'doi_bulletin', 'kar_regulation']; corpus only contains [].

No retrieval hits in this corpus slice.

### Smell 3: Coverage Inversion / Contradictory Conditions

> **Corpus gap**: Smell 3 requires source types ['homeowners_form', 'endorsement']; corpus only contains [].

No retrieval hits in this corpus slice.

### Smell 4: Calculation Rule Drift / Unversioned Rate Reference

> **Corpus gap**: Smell 4 requires source types ['homeowners_form', 'serff_filing', 'rate_manual']; corpus only contains [].

No retrieval hits in this corpus slice.

### Smell 5: Regulatory Mapping Smells

> **Corpus gap**: Smell 5 requires source types ['homeowners_form', 'endorsement', 'serff_filing']; corpus only contains [].

No retrieval hits in this corpus slice.

---

## Retrieval Mode Assessment

| Mode | Strengths | Weaknesses |
|---|---|---|
| Exact phrase | High precision; zero false positives for legal terms | Misses paraphrases and variant spellings |
| BM25 lexical | Catches term co-occurrence; handles varied phrasing | High false-positive rate on common legal words ("reasonable", "manual") |
| Graph expansion | Attaches parent section and sibling nodes for context | Only intra-document edges exist in Stage 002 |
| Metadata filter | Source-type scoping reduces noise immediately | Requires carrier form sources not yet in corpus |

---

_This report is generated output. Do not edit manually._
_Retrieval bundles are not legal findings._
