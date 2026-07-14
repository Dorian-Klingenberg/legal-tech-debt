# Stage 003: Generated Status Surface

Status: Planned
Entry gate: Stage 002 completed and its artifact contract updated from evidence

## Purpose

Generate a small status projection from canonical repository artifacts so the
owner can see active work, evidence, risks, decisions, and stale context without
manually reading every file.

This stage tests whether useful project visibility can be generated without
creating a second planning database or editable dashboard state.

## Controlling Question

Can a disposable status artifact answer "where are we, what is proven, and what
needs a human decision?" using only existing repo truth?

## Inputs

The first implementation may read only documented inputs, including:

- `AGENT_CONTEXT.json`;
- `STAGE-PLAN.md` and stage documents;
- current handoff and recent top-level journals;
- approved task contracts;
- evidence bundles and verifier reports;
- experiment requirement candidates and experiment-backed V&V records;
- risk records and ADRs.

The initial read model is sketched in
[`../001-stack-concept/examples/dashboard-read-model.md`](../001-stack-concept/examples/dashboard-read-model.md).

## Expected Output

Start with the smallest useful combination of:

- machine-readable JSON as the normalized projection;
- generated Markdown for quick review;
- static HTML only if it materially improves scanning.

Every generated output must identify its generation time, input files, missing
or unreadable evidence, and the command that reproduced it.

## In Scope

- Parse a narrow, versioned set of repo artifacts.
- Detect stale pointers, missing files, and incomplete evidence.
- Show traceability from origin to task to requirement to evidence.
- Show open human decisions and accepted risks.
- Produce deterministic, disposable output.
- Test parser and rendering behavior with small fixtures.

## Out Of Scope

- Editing canonical status from the generated surface.
- A database, service, queue, scheduler, or hosted dashboard.
- Replacing `AGENT_CONTEXT.json`, the backlog, ADRs, journals, or handoffs.
- Product-runtime telemetry or customer activity.
- Inferring completion when evidence is absent.
- Using an LLM as the parser for canonical status fields.

## Design Rules

- Canonical files are read-only inputs.
- Missing evidence must remain visible, not be summarized away.
- Deterministic parsers own structured fields.
- Free-text summaries must cite their source artifact.
- Deleting generated output must not lose project truth.
- Output schemas must be versioned if another stage consumes them.
- The stage must remain explainable in plain Python and static files.

## Entry Checklist

- [ ] Stage 002 is complete.
- [ ] The pilot artifact contract has been revised from measured evidence.
- [ ] At least one approved task contract, evidence bundle, and verifier report
      exists to exercise the read model.
- [ ] Canonical input ownership is documented.
- [ ] The owner approves the first output format.

## Design Checklist

- [ ] Inventory exact input files and fields.
- [ ] Define precedence when summaries disagree with canonical records.
- [ ] Define a normalized status projection schema.
- [ ] Define stale-pointer and missing-evidence rules.
- [ ] Define traceability links and unresolved-reference behavior.
- [ ] Decide whether Markdown alone is sufficient for the first run.
- [ ] Specify generated-output paths and cleanup behavior.
- [ ] Write focused positive and negative fixtures.

## Implementation Checklist

- [ ] Implement the smallest deterministic reader.
- [ ] Validate input failures without silently dropping records.
- [ ] Generate the normalized JSON projection.
- [ ] Generate the selected human-readable projection.
- [ ] Include source paths and generation metadata.
- [ ] Keep generated outputs outside canonical input paths.
- [ ] Add a single reproducible command.

## Verification Checklist

- [ ] Unit-test parsing and precedence rules.
- [ ] Test stale handoff and stale context detection.
- [ ] Test missing task, evidence, risk, and decision records.
- [ ] Test that generated output cannot become an input loop.
- [ ] Compare the projection against the Stage 002 records manually.
- [ ] Confirm deleting and regenerating output preserves the same status.
- [ ] Record false positives, false negatives, and ambiguous source text.
- [ ] Obtain human review of usefulness and scanability.

## Measurements

- [ ] Time needed to answer current-state questions before and after generation.
- [ ] Number of stale or missing references detected.
- [ ] Number of fields requiring manual interpretation.
- [ ] Number of duplicate-truth temptations or edit requests.
- [ ] Regeneration stability from unchanged inputs.
- [ ] Owner rating of usefulness versus maintenance burden.

## Completion Criteria

- [ ] One reproducible generated status artifact exists.
- [ ] It reads canonical files without modifying them.
- [ ] Missing and stale evidence is explicit.
- [ ] Traceability from origin through verification is visible for the pilot.
- [ ] Generated output is disposable and regeneration is tested.
- [ ] A lesson records what the projection could and could not infer.
- [ ] `STAGE-PLAN.md`, the handoff, journal, and documentation map are updated.

## Rejection Criteria

Do not promote the status surface if it requires a parallel state database,
manual synchronization, hidden LLM interpretation, or more maintenance than
reading the canonical pilot artifacts directly.
