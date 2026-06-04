# ADR-006: Smell Heuristics Must Be Suppressed On Regulatory Source Types

Date: 2026-06-03
Status: Accepted
Scope: Stage 006 deterministic detectors; applies to all future smell heuristics

## Context

After expanding the corpus from 7 to 28 sources and re-running Stage 006, Smell 2 produced 44 findings — up from 13. On inspection, 27 of the 44 new findings were false positives: the H001 heuristic ("reasonable/reasonably" near valuation context) was firing on `kar_regulation`, `krs_statute`, `doi_bulletin`, and `doi_guidance` source types.

The reason is that "reasonable" means different things in different document types:

- In a **carrier policy form or rate filing** (`serff_form_filing`, `serff_rate_rule_filing`): "reasonable" is a dispute gate. "Within a reasonable time" determines whether a claimant gets replacement cost or actual cash value. "Reasonably likely" gates whether GC overhead and profit are included in an estimate. These terms create real financial uncertainty for claimants because they are undefined.
- In a **regulation or statute** (`kar_regulation`, `krs_statute`): "reasonable" is legal standard language with established judicial interpretation. "A reasonable investigation" means what courts say it means; it is not a policy ambiguity. It does not create the same type of claim dispute uncertainty.
- In a **DOI bulletin or advisory opinion** (`doi_bulletin`, `doi_guidance`): "reasonably" appears in the DOI's own interpretation of what insurers must do. It is definitional guidance, not a policy term open to carrier discretion.

The same logic applies to H003 (valuation terms: actual cash value, replacement cost, market value). In a regulation, these terms are being defined or referenced as regulatory requirements. In a carrier filing, they are being used without definition in a claims settlement context — which is the actual smell.

## Decision

Smell heuristics H001 and H003 in `detectors/smell2.py` are suppressed for the following source types:

```python
_CARRIER_SOURCE_TYPES = {
    "serff_form_filing",
    "serff_rate_rule_filing",
    "serff_correspondence",
}
```

Heuristics only fire when `node.get("source_type")` is in `_CARRIER_SOURCE_TYPES`.

The detector runner (`detector_runner.py`) enriches each node with `source_type` from `idx.source_by_id` before passing nodes to detectors, since `source_type` lives in `sources.jsonl` (from the manifest) and not on individual nodes in `nodes.jsonl`.

This pattern — carrier-only suppression — should be applied as the default design principle for any new heuristic that uses qualitative language terms (reasonable, appropriate, adequate, material, significant) that have established legal meaning in regulatory contexts.

## Consequences

Positive:
- 44 → 23 findings; all Smell 2 findings now from carrier documents only
- False positive rate drops substantially for valuation term heuristics
- Reviewers see findings that are actually actionable — the uncertainty is in carrier language, not regulatory definitions
- Pattern is reusable: any future heuristic operating on qualitative language can check source_type

Tradeoffs:
- Regulatory sources will never generate H001/H003 findings even if they contain genuinely undefined terms — this is intentional; the regulatory review workflow is different from the policy review workflow
- New source types added to the manifest must be categorized correctly or they will be suppressed by default (an empty string is not in `_CARRIER_SOURCE_TYPES`)
- H002 (unversioned "current manual/edition" references) was not suppressed — it is equally problematic whether it appears in a carrier filing or a regulation, because both should version their manual references. This is a deliberate asymmetry.

## Rejected Alternatives

- Remove H001 entirely — would lose real carrier-form findings about "reasonable time" and "reasonably likely" that are genuine smells
- Keep H001 for all source types and rely on reviewer judgment — produces too much noise; reviewers cannot act on 44 findings where 27 are obvious regulatory boilerplate
- Filter by confidence level instead of source type — doesn't work because the heuristic cannot distinguish "reasonable time" in a statute from "reasonable time" in a policy form without the source type context
- Add a separate "regulatory context" qualifier to the H001 pattern — too brittle; the same word appears in both contexts and the distinction is in the document type, not the surrounding text

## Follow-Up

- All future smell heuristics that use qualitative language terms should document their source-type assumptions in the detector module header
- When new source types are added to the manifest, review all existing heuristics to determine whether suppression applies
- The same source-type filter should be considered for Smell 1 (exclusion language) and Smell 3 (coverage inversion) if those detectors start firing on regulatory sources as the corpus grows
- Smell 5 (regulatory mapping) is an exception: it should fire on carrier filings that fail to cite KRS/KAR, but suppression logic is the opposite direction — it should fire MORE aggressively on carrier sources, not less
