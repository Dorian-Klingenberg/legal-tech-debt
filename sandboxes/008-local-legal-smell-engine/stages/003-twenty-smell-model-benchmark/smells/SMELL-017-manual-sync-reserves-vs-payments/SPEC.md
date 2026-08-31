# SMELL-017 — Manual Sync — Reserves vs. Payments

- **ID:** SMELL-017
- **Name:** Manual Sync — Reserves vs. Payments
- **Taxonomy source:** `insurance_claims_smells.md`, Section 4 (Adjuster Workflow & Decision Smells), “Manual Sync — Reserves vs. Payments”
- **Complexity:** High

## Definition

Two authoritative-looking claims systems maintain related reserve and payment
state separately, and a person must repeatedly export, copy, reconcile, or
resolve the records manually. The smell is the absence of a reliable,
traceable synchronization boundary—not merely the existence of two systems.

## Positive signal

A supplied evidence set joins the same claim or financial exposure to both a
reserve record and a payment record, identifies both as authoritative or
operationally relied upon, and shows a recurring manual reconciliation step
with no automated link, durable ownership, or controlled exception trail.

## Negative signal

Separate systems are not positive when an automated, versioned reconciliation
or event/API integration keeps the records aligned, assigns an owner, and
retains an auditable exception path. A one-time human review of an automated
exception is not itself manual synchronization.

## Insufficiency / abstention rule

Abstain when the packet does not contain both reserve and payment evidence for
the same claim/exposure, or does not establish whether reconciliation is
manual versus automated. Do not infer the smell from a reserve discrepancy
alone.

## Evidence contract

Positive support requires the smallest join containing:

1. `claim_or_exposure_identity` — stable claim/exposure key shared by both systems;
2. `reserve_record` — amount, timestamp/version, and system role;
3. `payment_record` — paid/authorized amount, timestamp/version, and system role;
4. `reconciliation_process` — recurring manual action or copy path;
5. `control_gap` — missing integration, ownership, audit trail, or unresolved divergence.

Negative support should include the same two records plus an integration or
controlled reconciliation record. Insufficient cases must identify which join
role is missing.

## Provenance requirements

Every node must identify its synthetic source/artifact, version or snapshot,
claim/exposure key, effective or observed timestamp when material, and
authority status. Edges must show the claim-to-system and process-to-system
relationships. Manual assertions must be traceable to a workflow, runbook,
audit record, or system metadata node rather than inferred from amount
differences.

## Known limitations

The packet cannot prove accounting materiality, financial-reporting impact,
or legal noncompliance. It also cannot distinguish acceptable operational
segregation from harmful duplication without reliable authority metadata and
current process evidence. Synthetic fixtures omit vendor-specific APIs and
real reconciliation tolerances.
