# SMELL-014 — Sunset Obligation Smell

- **ID:** `SMELL-014`
- **Name:** Sunset Obligation Smell
- **Taxonomy source:** `insurance_claims_smells.md` §3, Notice & Procedure Smells
- **Complexity:** Medium

## Definition

Temporary or emergency claims language remains active or callable after its stated period, while the supplied workflow lacks a valid retirement condition, expired-date guard, or completed deactivation record.

## Positive signal

The evidence joins temporary/emergency authority or waiver language to a current claims workflow reference and proves that its sunset is missing, past due while still active, or not enforced by the execution control. A past date alone is not enough unless current workflow status or invocation evidence is also supplied.

## Negative signal

The temporary procedure has a valid future or completed retirement control that governs current invocation, or the procedure is expressly permanent and contains no temporary/emergency obligation. Historical emergency text retained for reference is not positive when the workflow cannot call it.

## Insufficiency / abstention rule

Return `insufficient` when the packet has emergency language but lacks a reliable effective-date/current-date context, workflow status, or retirement-control evidence. Do not infer that an old document is still active merely because it exists in the supplied evidence.

## Evidence contract

Required roles:

- `temporary_authority`: emergency, temporary, waiver, or relief language and its stated scope.
- `current_workflow_reference`: current claims procedure, feature flag, job, or invocation that can apply the temporary rule.
- `temporal_context`: effective, expiration, current-as-of, or version information.
- `retirement_control`: a missing, expired, bypassed, or valid deactivation/sunset mechanism.

The smallest positive set contains all four roles and shows both temporary status and current applicability. A negative set must show a valid guard or an explicitly non-temporary rule.

## Provenance requirements

Nodes must carry synthetic `source_id`, `source_type`, `document_version`, `section`, `jurisdiction`, `effective_from`, `effective_to` where known, and `provenance_status`. Date claims must state the fixture's `as_of` context. Evidence must separate retained historical text from executable workflow metadata.

## Known limitations

The smell does not determine whether an emergency order legally expired or whether a regulator extended it. It flags an evidence and control inconsistency for human verification against the authoritative order, filing, or current procedure.

