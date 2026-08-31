# SMELL-016 — Lack of Coverage Test Logging

- **ID:** `SMELL-016`
- **Name:** Lack of Coverage Test Logging
- **Taxonomy source:** `insurance_claims_smells.md` §6, Regulatory & Bad Faith Exposure Smells
- **Complexity:** Medium

## Definition

A claims coverage-decision workflow runs or requires coverage tests, but its decision record does not capture the test names, inputs, and outcomes needed to reconstruct which tests were applied.

## Positive signal

The evidence establishes a coverage-decision workflow and an explicit set of coverage tests or test categories, then shows a complete output/schema or audit inventory that records only a final decision, generic note, or reason code without test names, inputs, and outcomes.

## Negative signal

The workflow's structured decision log requires each applicable test name or stable test ID, its relevant inputs, and its outcome, with a claim-level record or audit rule showing those fields are retained.

## Insufficiency / abstention rule

Return `insufficient` when the packet contains a denial or coverage decision without the underlying workflow/schema, or when the supplied record is only a partial extract. Do not infer lack of logging from a single absent field unless the complete decision-record contract is supplied.

## Evidence contract

Required roles:

- `coverage_decision_workflow`: the process that determines coverage.
- `coverage_test_inventory`: named tests, test IDs, or explicit test categories used by the workflow.
- `decision_record_schema`: complete record fields or retention contract.
- `test_logging_check`: explicit presence or absence of test names, inputs, and outcomes in the record.

The smallest positive set contains all four roles and an explicit complete-schema check. A negative set must show retained test identity, inputs, and outcomes, not merely a final decision status.

## Provenance requirements

Nodes must carry synthetic `source_id`, `source_type`, `document_version`, `section`, `jurisdiction`, `claim_context` where applicable, and `provenance_status`. Distinguish workflow specification, record schema, and sample claim record. Evidence selections must use supplied node IDs and quote only supplied text.

## Known limitations

The smell does not determine whether the selected coverage tests were legally correct or whether a free-text note contains enough detail for a human reviewer. It flags a structured auditability gap; external logs or vendor systems not included in the packet may change the conclusion.

