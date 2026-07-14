# Sandbox 005 Stage Plan

Status: Current primary plan; Stage 002 ready but owner-gated
Last updated: 2026-07-13

## Sandbox Goal

Design and test a lightweight, repo-native agentic SDLC project-manager stack for Legal Tech Debt.

This sandbox should produce a disciplined operating model before any dashboard or orchestration implementation is attempted. The model must support requirements discovered through conversation and through experimentation, including sandbox probes, prototype behavior, failed runs, surprising outputs, and playtest-style observations. It must also treat experimentation as a validation and verification method in the V-model sense: experimental probes can confirm, falsify, or refine whether an implemented behavior satisfies the domain need.

Documentation map: [`DOCUMENTATION-MAP.md`](DOCUMENTATION-MAP.md)

## Stage 001: Stack Concept And Artifact Contract

Status: Complete (2026-07-13)

Stage document:
[`stages/001-stack-concept/STAGE.md`](stages/001-stack-concept/STAGE.md)

Purpose:

Define the first-pass SDLC stack, artifact model, gate model, and agent role model.

Checklist:

- [x] Create Sandbox 005.
- [x] Separate SDLC stack exploration from agentic product runtime exploration.
- [x] Record initial candidate stack layers.
- [x] Define the minimum disciplined task contract.
- [x] Define how experiment observations become requirement candidates.
- [x] Define an evidence bundle format.
- [x] Define how experiments support V&V evidence, not only requirements discovery.
- [x] Define which work types require Gherkin and which do not.
- [x] Define hard gates, advisory gates, and human-only gates.
- [x] Define the first agent role set.
- [x] Define the project-manager dashboard read model.
- [x] Identify existing repo artifacts the dashboard should ingest.
- [x] Identify artifact conflicts or duplicate truth risks.
- [x] Compare Agile V skills/scaffold, SwarmForge, and Codex CLI against this
      repository's needs.
- [x] Record upstream maturity, licensing, and local prerequisite findings.
- [x] Produce a Stage 001 decision note or ADR candidate if the stack direction hardens.
- [x] Decide that Stage 002 should pilot a real project item.

Expected outputs:

- `stages/001-stack-concept/STAGE.md`
- `stages/001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md`
- `stages/001-stack-concept/LESSON.md`
- Optional artifact sketches under `stages/001-stack-concept/examples/`
- Follow-up ADR only if a durable architecture decision is made.

Decision:

Use a provisional repo-native hybrid. Keep current repo artifacts canonical,
borrow selected Agile V assurance concepts, use Codex CLI as the first execution
engine, use manual worktrees and one writer initially, and defer executable
SwarmForge adoption to Stage 004. This remains a pilot decision, so no ADR is
warranted yet.

## Stage 002: Manual Pilot On One Real Project Item

Status: Ready; next stage

Stage document:
[`stages/002-manual-pilot/STAGE.md`](stages/002-manual-pilot/STAGE.md)

Purpose:

Run the proposed SDLC stack manually on one small project item before building tooling.

Checklist:

- [x] Select one low-to-medium risk project item: `S005-PILOT-001`.
- [ ] Write the task contract.
- [ ] Identify whether the task came from conversation, experiment evidence, or both.
- [ ] Write Gherkin only if the selected item has behavior worth specifying.
- [ ] Produce implementation evidence bundle.
- [ ] Run validation appropriate to the risk.
- [ ] Identify whether any experimental probe is needed for validation or verification.
- [ ] Capture human review outcome.
- [ ] Record friction, ambiguity, and missing artifact fields.
- [ ] Update the artifact contract based on the pilot.

Selected pilot:

- `S005-PILOT-001` will define and validate a manifest contract for the future
  synthetic public demo corpus, without building the corpus itself.
- [x] Create the detailed pilot stage plan at
      `stages/002-manual-pilot/STAGE.md`.
- [ ] Complete the WSL-native Codex CLI and clean-worktree preflight.

Gate:

Do not build a dashboard before completing at least one manual pilot.

## Stage 003: Generated Status Surface

Status: Planned

Stage document:
[`stages/003-generated-status-surface/STAGE.md`](stages/003-generated-status-surface/STAGE.md)

Purpose:

Generate a simple status view from repo truth.

Checklist:

- [x] Create the dedicated Stage 003 document.
- [ ] Decide the first status output format: Markdown, HTML, JSON, or all three.
- [ ] Read existing artifacts rather than creating a new planning database.
- [ ] Show active lane, open risks, open decisions, latest validation, and stale handoffs.
- [ ] Show traceability from experiment or conversation to requirement to task to verification evidence.
- [ ] Mark missing evidence explicitly.
- [ ] Keep output generated and disposable.

Gate:

The generated surface must not become canonical truth.

## Stage 004: Agent Role And Worktree Experiment

Status: Planned

Stage document:
[`stages/004-agent-role-worktree-experiment/STAGE.md`](stages/004-agent-role-worktree-experiment/STAGE.md)

Purpose:

Evaluate whether SwarmForge-style orchestration improves actual work in this repo.

Checklist:

- [x] Create the dedicated Stage 004 document.
- [ ] Define minimal role prompts: planner, implementer, reviewer.
- [ ] Define file allowlist expectations per role.
- [ ] Define branch/worktree naming rules.
- [ ] Run a small coordinated task with separate worktrees.
- [ ] Measure whether the coordination helped or added overhead.
- [ ] Compare Codex built-in subagents plus manual worktrees against a
      SwarmForge-style topology on similarly shaped work.
- [ ] Resolve SwarmForge licensing or obtain permission before copying or
      adapting upstream code or prompts.
- [ ] Pin tools and dependencies; do not procure unpinned latest versions at
      role startup.
- [ ] Decide whether to adopt SwarmForge, borrow its pattern, or stay with simpler manual coordination.

Gate:

Do not adopt a multi-agent orchestration tool until the manual role model is useful.

## Stage 005: Phase A Integration Plan

Status: Planned

Stage document:
[`stages/005-phase-a-integration-plan/STAGE.md`](stages/005-phase-a-integration-plan/STAGE.md)

Purpose:

Convert sandbox findings into a Phase A-ready SDLC stack plan.

Checklist:

- [x] Create the dedicated Stage 005 document.
- [ ] Produce SDLC stack concept of operations.
- [ ] Define SDLC requirements categories.
- [ ] Define traceability model.
- [ ] Define verification evidence model.
- [ ] Define agent governance model.
- [ ] Define dashboard/control-surface role.
- [ ] Identify ADRs needed for accepted stack choices.
- [ ] Close or carry forward Sandbox 005.
