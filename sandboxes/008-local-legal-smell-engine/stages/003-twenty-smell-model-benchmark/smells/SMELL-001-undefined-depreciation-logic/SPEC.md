# SMELL-001 — Undefined Depreciation Logic

- **ID:** `SMELL-001`
- **Name:** Undefined Depreciation Logic
- **Taxonomy source:** `insurance_claims_smells.md`, Section 2 — Valuation & Payment Smells
- **Complexity:** Low

## Definition

The supplied policy, claim calculation, or valuation rule authorizes a depreciation deduction but does not specify the method or the inputs needed to reproduce that deduction. This is a review smell, not a determination that any particular claim payment is unlawful.

## Positive signal

A scoped, sufficiently complete loss-settlement or calculation node states that depreciation is deducted/applied, and its metadata explicitly records that the method or required inputs are unspecified. A second node may show the resulting valuation consequence, but the absence must be supported by the fixture's explicit completeness/absence assertion rather than inferred from a short excerpt.

## Negative signal

The evidence either does not deduct depreciation, or it specifies a reproducible method and relevant inputs such as straight-line or condition-based treatment, useful life, age, condition, or a documented schedule.

## Insufficiency / abstention rule

Return `insufficient` when the evidence mentions depreciation but does not establish both (1) an actual allowance/deduction and (2) a complete scoped clause or explicit assertion about whether the method and inputs are specified. Do not treat an omitted method in a fragment as a positive smell.

## Evidence contract

Required roles for a positive finding:

1. `depreciation_allowance` — policy or calculation text that applies, deducts, or permits depreciation.
2. `complete_clause_scope` — metadata showing the relevant clause/configuration was supplied as a complete review scope.
3. `missing_method_assertion` — explicit metadata or structured calculation evidence that method/inputs are unspecified.

Optional `valuation_consequence` evidence can show why the ambiguity matters. The smallest positive set is normally two nodes: the allowance and the scoped absence assertion.

## Provenance requirements

Every cited node must retain a stable local `node_id`, `metadata.source_id`, `metadata.source_type`, `metadata.document_version`, and `metadata.section_path`. Any completeness or absence assertion must be identified as synthetic fixture metadata, not presented as a legal authority.

## Known limitations

The packet cannot decide whether a method is commercially reasonable or legally required. A method embedded in an external schedule is only verifiable if that schedule is supplied. Real claims may use condition assessments or vendor estimates that are not represented in this low-complexity fixture.
