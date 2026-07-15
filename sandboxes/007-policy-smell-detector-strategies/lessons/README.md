# Sandbox 007 Smell Lessons

Status: Detector-design lessons captured after Stage 001; Stage 002 has not started

These lessons turn the five rows of the
[Detection Strategy Matrix](../DETECTION_STRATEGY_MATRIX.md) into reusable
detector-design guidance. They do not claim that the proposed detectors have
met the sandbox's precision targets or that every candidate signal is a legal
or policy defect.

## Evidence Labels

- **Observed** means a repository artifact or corpus source was inspected and
  supports the narrow statement made.
- **Inherited** means an earlier sandbox established a reusable engineering
  pattern, such as typed witness paths or stable run identity.
- **Proposed** means Sandbox 007 has a detector design or validation target but
  no implementation result yet.

## Lessons

| Smell | Lesson | Current evidence boundary |
|---|---|---|
| Circular Definition | [Detect Definition Dependencies, Not Generic Graph Cycles](LESSON-01-circular-definition.md) | One literal term-echo candidate is observed; no Sandbox 007 detector result exists. |
| Rule Duplication | [Similarity Finds Candidates; Divergence Makes Them Actionable](LESSON-02-rule-duplication.md) | Shared structure and cross-form fan-out are observed; independent-copy lineage and update drift remain unvalidated. |
| Hardcoded Jurisdiction Logic | [A Missing Inline Citation Is a Traceability Question](LESSON-03-hardcoded-jurisdiction-logic.md) | State-scoped rule candidates are observed; package-level authority resolution is not complete. |
| Null Reference Clause | [Reference Validity Is Identity Plus Time Plus Applicability](LESSON-04-null-reference-clause.md) | Reference-lifecycle dependencies are known; no null-reference instance has been validated. |
| Spec-Code Divergence | [Spec-Code Divergence Requires Versioned Paired Evidence](LESSON-05-spec-code-divergence.md) | The corpus has no PAS or configuration comparator, so no divergence instance can be established. |

## Shared Guardrails

- All teaching examples in these lessons are synthetic.
- Real corpus materials are referenced by source ID and paraphrased only.
- Findings are reviewer candidates, not automated legal conclusions.
- Success thresholds in Sandbox 007 are future validation targets, not achieved
  measurements.
- Sandbox 002 is a preserved evidence substrate. A future implementation may
  reuse its patterns and artifacts, but must not silently mutate its closed
  schemas or detector outputs.

