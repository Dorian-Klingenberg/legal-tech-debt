# SMELL-019 — Regulatory Drift in Claim Handling

- **ID:** SMELL-019
- **Name:** Regulatory Drift in Claim Handling
- **Taxonomy source:** `insurance_claims_smells.md`, Section 6 (Regulatory & Bad Faith Exposure Smells), “Regulatory Drift in Claim Handling”
- **Complexity:** High

## Definition

A dated, jurisdictionally applicable authority changes a claim-handling
obligation or standard, but the deployed workflow, decision rule, form, or
control remains on an older behavior and the change has not been propagated.
The smell concerns an evidence-backed version mismatch, not a difference in
writing style or an unverified claim that a regulator changed something.

## Positive signal

The packet contains an authoritative version transition with an effective
date, the old and current workflow/configuration versions, and an explicit
comparison showing that the new obligation is absent, stale, or contradicted
in production. A pending change ticket or failed compliance test strengthens
the signal but is not required if deployment evidence is clear.

## Negative signal

No drift exists when the current authority version is mapped to a deployed
workflow version that implements the changed obligation, with release/test
evidence. An archived old workflow or a pending future rule does not make the
current deployed workflow stale when dates and applicability are explicit.

## Insufficiency / abstention rule

Abstain unless both sides of the comparison are supplied: a versioned,
effective authority change and a dated current workflow/deployment snapshot.
Do not infer regulatory drift from a generic “new guidance” note, an old
version without deployment status, or an unexplained workflow difference.

## Evidence contract

Required roles:

1. `authority_change` — jurisdiction, source/version, effective date, old/new obligation;
2. `prior_or_expected_behavior` — what the workflow must do after the change;
3. `current_workflow_version` — deployed version and effective/release date;
4. `mismatch` — direct field, step, threshold, or branch comparison;
5. `propagation_status` — release, mapping, test, or ticket evidence showing absent or completed propagation.

Positive cases should use an edge from the authority change to the expected
workflow behavior and from the behavior to the deployed version. Negative
cases should show the updated implementation and verification. Insufficient
cases must make the missing version/effective/deployment evidence apparent.

## Provenance requirements

Authority nodes must use synthetic regulator artifacts in this benchmark and
carry jurisdiction, version, publication/effective dates, and source type.
Workflow nodes must carry version, deployment environment, release date, and
the relevant field/step text. Comparison or ticket nodes must cite the IDs of
the compared artifacts. Do not use absence without a schema, test, mapping,
or inventory statement that makes the absence inspectable.

## Known limitations

The packet does not determine whether an authority is legally valid, whether
an exception or grace period applies, or whether a workflow change was
operationally effective in every region. It tests version-aware evidence
selection and propagation reasoning. Real regulatory programs may have
multiple overlapping sources and manual controls omitted from a fixture.
