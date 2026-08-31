# SMELL-004 — Unversioned Proof-of-Loss Form

- **ID:** `SMELL-004`
- **Name:** Unversioned Proof-of-Loss Form
- **Taxonomy source:** `insurance_claims_smells.md`, Section 3 — Notice & Procedure Smells
- **Complexity:** Low

## Definition

A claims workflow or system uses or generates a proof-of-loss form by an unversioned/generic identifier even though supplied authoritative evidence identifies a superseding or required edition. The smell concerns traceability and workflow alignment; it is not a conclusion that a filing is invalid.

## Positive signal

The workflow's form reference explicitly lacks an edition/version, and a supplied DOI, filed-form, or other clearly marked authority node identifies a current edition and states that the prior/generic form is superseded or must no longer be used. The references must be joined by a form concept or typed edge.

## Negative signal

The workflow stores a specific form edition/version that matches the supplied current authority, or the evidence contains no supersession conflict and therefore does not establish the smell.

## Insufficiency / abstention rule

Return `insufficient` when the workflow reference is incomplete or the authoritative current/superseding edition is absent, unclear, or not linked to the same form. Do not infer a supersession conflict from the words “proof of loss” alone.

## Evidence contract

Required roles for a positive finding:

1. `unversioned_workflow_reference` — complete workflow/configuration evidence with no edition/version.
2. `authoritative_current_form` — authority evidence naming the required/current edition.
3. `supersession_conflict` — explicit text or edge establishing that the generic/old reference conflicts with the current edition.
4. `same_form_join` — shared form identifier/concept or typed relationship connecting the two artifacts.

The smallest positive set is the workflow reference and authority node plus their form-identity/supersession relationship.

## Provenance requirements

Cited nodes must retain stable local IDs, `source_id`, `source_type`, `document_version`, and `section_path`. Authority nodes must state their authority role and effective date when supplied. Synthetic fixture metadata may assert `version_present: false`, but that assertion is not a claim about any real DOI or carrier.

## Known limitations

This packet does not determine whether a jurisdiction requires a particular form, whether an edition was properly filed, or whether a transition/grace period applies. Real forms may be identified by a state-specific number, carrier form number, or electronic template hash rather than a simple edition string.
