# Stage 002: Manual Hybrid Pilot

Status: Ready; not started
Selected: 2026-07-13

## Purpose

Test the provisional Sandbox 005 hybrid on one bounded, real project task before
building a dashboard, installing an orchestration framework, or formalizing
schemas globally.

The system under test is:

- repo-native task and evidence artifacts;
- selected Agile V-style traceability, risk, gate, and verifier concepts;
- Codex CLI as the execution engine;
- manual Git worktree isolation;
- one implementation writer;
- deterministic validation before semantic or human review.

SwarmForge is not part of this stage. Its orchestration mechanics remain a
Stage 004 experiment.

## Selected Pilot Task

Pilot ID: `S005-PILOT-001`

Define and validate a manifest contract for the future synthetic public demo
corpus described in
[`../../../../journal/2026-06-11-demo-dataset-strategy.md`](../../../../journal/2026-06-11-demo-dataset-strategy.md).

Expected implementation slice:

- a small JSON Schema for demo-corpus manifest records;
- one valid synthetic fixture;
- one intentionally invalid synthetic fixture;
- a plain, deterministic validation command;
- focused automated tests;
- task, evidence, and verifier records local to this pilot.

The pilot does not create the synthetic corpus, production infrastructure,
customer data paths, authentication, billing, deployment, or a status dashboard.

## Why This Pilot Fits

- It advances a documented production-aligned portfolio need.
- It originated from explicit project evidence and owner direction.
- It is small enough to expose process overhead clearly.
- It has both positive and negative deterministic behavior.
- It has a meaningful data-boundary risk without handling real customer data.
- It does not need Gherkin; ordinary acceptance criteria and tests are clearer.

## Role Contract

| Role | Work | Boundary |
|---|---|---|
| Lead/specifier | Create the task contract, requirement IDs, risk decision, and acceptance criteria | May edit pilot control artifacts only before approval |
| Implementer | Implement schema, fixtures, validator, and tests | Sole implementation writer in a dedicated worktree |
| Verifier | Read the approved contract, diff, and resulting evidence; rerun deterministic checks | Read-only fresh context; does not repair its own findings |
| Human owner | Approve scope, evaluate process usefulness, and accept or reject the pilot | Human-only gate |

## Intended Trace

```text
demo strategy journal
  -> S005-PILOT-001 task contract
  -> requirement and acceptance IDs
  -> changed schema, fixtures, validator, and tests
  -> deterministic run evidence
  -> fresh-context verification report
  -> human pilot decision
```

## Preflight Checklist

- [ ] Commit or otherwise isolate the current dirty checkout before creating
      pilot worktrees; do not make the dirty root a coordinator workspace.
- [ ] Install the official Codex CLI natively inside WSL.
- [ ] Record the Codex CLI version and authentication mode without recording
      credentials.
- [ ] Verify a read-only `codex exec` smoke test inside a disposable Git
      worktree.
- [ ] Confirm `approval_policy = "on-request"` and the least-required sandbox.
- [ ] Define project-local specifier, implementer, and verifier role prompts in
      repo-neutral canonical files before any Codex-specific adapter.
- [ ] Confirm the verifier is read-only.
- [ ] Record start time and setup effort.

## Task Contract Checklist

- [ ] Create the `S005-PILOT-001` task contract from the Stage 001 template.
- [ ] Link the demo strategy journal and production-aligned documentation as
      source evidence.
- [ ] Assign stable requirement and acceptance IDs.
- [ ] Record in-scope and out-of-scope paths.
- [ ] Classify implementation risk and public-demo/reputational risk separately.
- [ ] List deterministic validation commands before implementation starts.
- [ ] State why Gherkin is not required.
- [ ] Define the expected evidence bundle and verifier output.
- [ ] Obtain human approval before implementation.

## Execution Checklist

- [ ] Create one clean implementation branch and worktree.
- [ ] Run the implementer as the only implementation writer.
- [ ] Prevent unrelated changes and generated-state churn.
- [ ] Create the smallest schema, fixtures, validator, and test slice that meets
      the approved contract.
- [ ] Run focused tests and schema validation.
- [ ] Capture commands, exit codes, concrete counts, and artifact paths.
- [ ] Produce the evidence bundle without relying on the agent transcript as
      project truth.

## Verification Checklist

- [ ] Start the verifier from a fresh context with the approved contract, diff,
      and evidence bundle.
- [ ] Keep the verifier read-only.
- [ ] Rerun the deterministic checks independently.
- [ ] Confirm the invalid fixture fails for the intended reason.
- [ ] Check every acceptance ID against implementation and evidence.
- [ ] Record missing evidence, untested assumptions, and residual risk.
- [ ] Have the lead or human decide whether fixes require a new implementation
      turn.
- [ ] Record final human approval or rejection.

## Pilot Measurements

- [ ] Human time spent preparing the contract.
- [ ] Setup time caused by Codex CLI, worktrees, or role configuration.
- [ ] Number of agent runs and human interventions.
- [ ] Number of defects or ambiguities found before implementation.
- [ ] Number of defects found only by the verifier.
- [ ] Number of missing or stale trace links.
- [ ] Merge conflicts or out-of-scope edits.
- [ ] Fields completed mechanically but never used.
- [ ] Whether a future agent can reconstruct the decision and evidence without
      reading the original conversation.
- [ ] Owner rating: process reduced anxiety, was neutral, or added friction.

## Decision Gates

Continue with the hybrid if the pilot shows that the artifact chain:

- makes scope and acceptance clearer;
- exposes evidence and uncertainty honestly;
- catches at least one meaningful ambiguity, omission, or defect, or gives a
  clearly reviewable proof that none was found;
- remains easier to understand than the task itself;
- and does not create duplicate canonical state.

Simplify or reject parts of the hybrid if:

- role and artifact ceremony outweighs the bounded task;
- verifier independence produces no useful difference;
- task state has to be synchronized across multiple competing files;
- Codex-specific configuration becomes the only place the workflow is defined;
- or a normal single-agent implementation plus review is clearer and equally
  reliable.

## Stage Completion Checklist

- [ ] Complete every required pilot checklist item or record why it was skipped.
- [ ] Update the Stage 001 artifact sketches only for fields proven useful.
- [ ] Write a reusable lesson describing helpful and unhelpful controls.
- [ ] Update `STAGE-PLAN.md` with measured results.
- [ ] Add a top-level journal entry.
- [ ] Decide whether Stage 003 should generate a status surface from the pilot
      artifacts.
- [ ] Leave SwarmForge adoption undecided until Stage 004.
