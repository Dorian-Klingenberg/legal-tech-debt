# Lesson 2: Similarity Finds Candidates; Divergence Makes Them Actionable

Date: 2026-07-14

Status: Design lesson; structural candidates observed, detector unimplemented

Scope: Sandbox 007 — Rule Duplication

Related: [strategy matrix](../DETECTION_STRATEGY_MATRIX.md),
[policy-smell taxonomy](../../../insurance_policy_smells.md),
[Sandbox 002 stable-identity decision](../../002-claims-regulatory-automation/adr/ADR-004-schema-run-identity-and-id-stability.md)

## Problem or Question

Repeated language is common in insurance forms. Some repetition is deliberate:
standard wording may be inherited from a bureau form, and one endorsement may
intentionally amend several base forms. The maintainability smell arises when
the same business rule is maintained as separate copies and those copies can
drift.

Text similarity therefore answers only the candidate-generation question. It
does not prove independent duplication, inconsistency, or a defect.

## Why It Mattered

A detector that reports every similar clause will mostly rediscover boilerplate
and form families. A useful detector must tell a reviewer:

- whether the clauses share a known lineage;
- whether one centrally maintained clause fans out to several forms;
- whether multiple independently maintained copies exist;
- which material condition differs; and
- which versions and effective dates were compared.

The actionable evidence is not merely high similarity. It is high similarity
plus a maintenance relationship or meaningful divergence.

## Pattern or Solution

Use similarity for recall, then add structure and provenance:

1. Segment sources into clause-sized units and retain source, form, section,
   edition, filing, and effective-date identity.
2. Normalize layout noise, headers, page numbers, defined-term typography, and
   other nondispositive variation. Preserve the original text alongside the
   normalized representation.
3. Use a fingerprint or similarity measure to create candidate clusters.
4. Classify each cluster as `shared_lineage`, `central_amendment_fanout`,
   `independent_copy`, or `lineage_unknown` before calling it duplication.
5. Align corresponding conditions and emit a semantic diff: thresholds,
   covered forms, exceptions, dates, operators, and incorporated references.
6. Report the cluster only with a witness set showing the compared clauses and
   the exact material divergence or maintenance fan-out.

Cross-reference fan-out is valuable evidence about blast radius, but it is not
itself proof that five independent copies exist. A single endorsement applied
to five forms may be better centralized than five retyped clauses.

## Concrete Example — Synthetic

Assume an invented form family contains these rules:

```text
Form SYN-HO-3: Apply settlement method S when roof age is more than 10 years.
Form SYN-HO-5: Apply settlement method S when roof age is more than 12 years.
Endorsement SYN-E1: Replaces the same settlement paragraph in six listed forms.
```

The first two clauses are a duplication candidate with a material threshold
difference. The endorsement is a fan-out dependency: one rule affects six
forms, but the text is maintained once.

A useful result separates them:

```text
cluster SYN-DUP-01
  relationship: independent_copy_candidate
  divergence: threshold 10 years vs 12 years
  lineage_status: unresolved

cluster SYN-FANOUT-01
  relationship: central_amendment_fanout
  affected_forms: 6
  duplication_finding: false
```

## Evidence or Validation

| Evidence status | What the repository supports |
|---|---|
| Observed | Direct extraction from `KY-SERFF-KFBM-134503212-HO-FORM-MARKUP` and `ISO-HO-04-93-1000` shows substantial shared structure while the KFBM markup adds a seven-year applicability condition. This is a comparison candidate; exact edition lineage and drafting intent remain unvalidated. The redacted `134503212-HO-FORM` public-view artifact is not the comparison source. |
| Observed | KNIC source `132500003-HO-04-95` applies one replacement paragraph across five named forms, and KFBM source `134827992-ENDORSEMENT` applies one endorsement across six forms. Those examples establish fan-out, not independent duplicated copies. |
| Inherited | Sandbox 002's stable source and node identity rules provide the provenance pattern needed for repeatable comparisons across runs. |
| Proposed | Similarity thresholds, normalized clause boundaries, duplicate-cluster accuracy, lineage classification, and the Sandbox 007 precision target have not been implemented or measured. |

The Stage 001 matrix supplies strategy hypotheses. Its projected count of five
clusters is a future success threshold, not a result.

## Limitations

- Standard or legally required wording may be intentionally identical.
- Copyright and bureau-form lineage can limit what may be republished and what
  can be inferred from textual similarity.
- OCR, columns, headers, and form numbers can distort fingerprints.
- A short common clause can score highly without representing the same business
  rule.
- A wording difference can be immaterial, while a one-character operator or
  threshold difference can be decisive.
- Without edition and effective-date alignment, a diff may compare an old form
  with its legitimate successor.
- Human policy review is required before labeling a cluster inconsistent or
  harmful.

## What To Reuse Next Time

- [ ] Use similarity to generate candidates, not conclusions.
- [ ] Preserve original text, normalized text, fingerprint method, and detector
      version.
- [ ] Align product, jurisdiction, form family, edition, and effective dates.
- [ ] Distinguish shared lineage, central fan-out, and independent copies.
- [ ] Emit the material semantic diff, not only a similarity score.
- [ ] Treat one-to-many amendments as blast-radius evidence, not automatic
      duplication.
- [ ] Require a witness set and human lineage review before escalating drift.
- [ ] Report projected precision and count thresholds as unvalidated until an
      evaluation run exists.
