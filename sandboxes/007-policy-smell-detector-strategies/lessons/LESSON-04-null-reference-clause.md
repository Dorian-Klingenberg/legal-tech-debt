# Lesson 4: Reference Validity Is Identity Plus Time Plus Applicability

Date: 2026-07-14

Status: Boundary lesson; no real null-reference instance validated

Scope: Sandbox 007 — Null Reference Clause

Related: [strategy matrix](../DETECTION_STRATEGY_MATRIX.md),
[policy-smell taxonomy](../../../insurance_policy_smells.md),
[corpus known gaps](../../../corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md),
[Sandbox 002 reference extractor](../../002-claims-regulatory-automation/stages/002-homeowners-discovery-instrumentation/src/extractors/references.py)

## Problem or Question

A Null Reference Clause is not merely a citation that the local parser failed to
resolve. The smell requires an explicit reference whose target is retired,
withdrawn, repealed, superseded without an applicable transition, or otherwise
inapplicable to the relevant policy period.

Three nearby problems must stay separate:

- no explicit citation at all, which is a traceability or unversioned-reference
  question;
- a target absent from the local corpus, which is an evidence-collection gap;
  and
- a resolved target that was not live or applicable at the relevant time, which
  may support a Null Reference candidate.

## Why It Mattered

The current Sandbox 002 reference extractor initializes references as
unresolved and supplies manual-check notes. It does not query an official
authority index or determine effective, withdrawal, or supersession dates.

If `resolved: false`, a missing file, or a dead URL were treated as proof of a
null authority, ordinary corpus gaps and moved web pages would become false
legal findings.

## Pattern or Solution

Resolve reference identity first, then evaluate time and applicability:

1. Extract and normalize the explicit citation, including jurisdiction and
   authority type.
2. Resolve it against authoritative current and archival indexes.
3. Record `effective_from`, `effective_to`, status, successor, transition rule,
   lookup source, and `checked_at`.
4. Align the authority interval with the form, filing, policy, issuance, or loss
   interval relevant to the review question.
5. Preserve a witness path from the clause to the authority and, when present,
   through `superseded_by` or `renumbered_to` relationships.
6. Classify the result precisely:

| Status | Meaning |
|---|---|
| `no_explicit_reference` | Route to hardcoded or unversioned-reference review. |
| `source_not_in_corpus` | Collection gap; authority status unknown. |
| `resolved_live` | Target exists and overlaps the relevant interval. |
| `resolved_historical` | Target was live for the reviewed historical interval. |
| `referential_drift` | Target moved or was renumbered and a successor is known. |
| `null_reference_candidate` | Target was not live or applicable for the reviewed interval, subject to transition review. |

## Concrete Example — Synthetic

Assume an invented endorsement effective January 1, 2025 states:

```text
Cancellation reviews shall follow DOI Bulletin SYN-2019-04.
```

The invented authority record says:

```text
SYN-2019-04
  status: withdrawn
  effective_to: 2023-06-30
  superseded_by: SYN-2023-07

SYN-2023-07
  effective_from: 2023-07-01
```

The nonoverlapping dates support a `null_reference_candidate`. They do not by
themselves prove noncompliance: a reviewer must still check transition
provisions, subject-matter applicability, and the complete filing package.

## Evidence or Validation

| Evidence status | What the repository supports |
|---|---|
| Observed | The Sandbox 002 extractor normalizes some citation strings but leaves every extracted reference unresolved and directs manual checks. Its source schema has download metadata but no authority effective, withdrawal, or supersession fields. |
| Observed | The corpus records known version and acquisition gaps, including a newer KNIC manual needed to supersede an older filing for current-state analysis. That proves a temporal evidence dependency, not a Null Reference Clause in a policy. |
| Inherited | Sandbox 001 proved seeded dangling-reference and unversioned-reference mechanics. It did not validate live bulletin or regulation supersession. |
| Proposed | The matrix's citation resolution, archive check, temporal comparison, and labeled citation-fixture target have not been implemented or measured. The claim that current corpus bulletins are null references remains unvalidated. |

## Limitations

- A 404 or changed URL can mean a document moved, not that its authority ended.
- Current status today is different from applicability at policy issuance or
  loss.
- Renumbering, repeal, withdrawal, supersession, and sunset provisions have
  different legal effects.
- OCR and citation-normalization errors can create false unresolved records.
- A historical form may properly reference an authority that was live during
  its effective period.
- Classification can overlap Referential Drift, Filing Dependency, and Sunset
  Clause smells.
- Expert review is required before stating legal effect or noncompliance.

## What To Reuse Next Time

- [ ] Require an explicit reference before applying the Null Reference label.
- [ ] Normalize target identity, authority type, and jurisdiction.
- [ ] Check authoritative current and archival sources.
- [ ] Record lookup source and timestamp.
- [ ] Capture both authority and reviewed-artifact effective intervals.
- [ ] Identify successors, renumbering, and transition provisions.
- [ ] Distinguish corpus absence, dead URLs, and legal retirement.
- [ ] Preserve the temporal witness path and uncertainty.
- [ ] Require expert review before stating noncompliance.
