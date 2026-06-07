# Sandbox 005 Stage Plan

Status: Active
Last updated: 2026-06-07

## Sandbox Goal

Design and test a lightweight, repo-native agentic SDLC project-manager stack for Legal Tech Debt.

This sandbox should produce a disciplined operating model before any dashboard or orchestration implementation is attempted. The model must support requirements discovered through conversation and through experimentation, including sandbox probes, prototype behavior, failed runs, surprising outputs, and playtest-style observations. It must also treat experimentation as a validation and verification method in the V-model sense: experimental probes can confirm, falsify, or refine whether an implemented behavior satisfies the domain need.

## Stage 001: Stack Concept And Artifact Contract

Status: Active

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
- [ ] Define the first agent role set.
- [x] Define the project-manager dashboard read model.
- [x] Identify existing repo artifacts the dashboard should ingest.
- [x] Identify artifact conflicts or duplicate truth risks.
- [ ] Produce a Stage 001 decision note or ADR candidate if the stack direction hardens.

Expected outputs:

- `stages/001-stack-concept/STAGE.md`
- Optional artifact sketches under `stages/001-stack-concept/examples/`
- Follow-up ADR only if a durable architecture decision is made.

## Stage 002: Manual Pilot On One Real Backlog Item

Status: Planned

Purpose:

Run the proposed SDLC stack manually on one small backlog item before building tooling.

Checklist:

- [ ] Select one low-to-medium risk backlog item.
- [ ] Write the task contract.
- [ ] Identify whether the task came from conversation, experiment evidence, or both.
- [ ] Write Gherkin only if the selected item has behavior worth specifying.
- [ ] Produce implementation evidence bundle.
- [ ] Run validation appropriate to the risk.
- [ ] Identify whether any experimental probe is needed for validation or verification.
- [ ] Capture human review outcome.
- [ ] Record friction, ambiguity, and missing artifact fields.
- [ ] Update the artifact contract based on the pilot.

Gate:

Do not build a dashboard before completing at least one manual pilot.

## Stage 003: Generated Status Surface

Status: Planned

Purpose:

Generate a simple status view from repo truth.

Checklist:

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

Purpose:

Evaluate whether SwarmForge-style orchestration improves actual work in this repo.

Checklist:

- [ ] Define minimal role prompts: planner, implementer, reviewer.
- [ ] Define file allowlist expectations per role.
- [ ] Define branch/worktree naming rules.
- [ ] Run a small coordinated task with separate worktrees.
- [ ] Measure whether the coordination helped or added overhead.
- [ ] Decide whether to adopt SwarmForge, borrow its pattern, or stay with simpler manual coordination.

Gate:

Do not adopt a multi-agent orchestration tool until the manual role model is useful.

## Stage 005: Phase A Integration Plan

Status: Planned

Purpose:

Convert sandbox findings into a Phase A-ready SDLC stack plan.

Checklist:

- [ ] Produce SDLC stack concept of operations.
- [ ] Define SDLC requirements categories.
- [ ] Define traceability model.
- [ ] Define verification evidence model.
- [ ] Define agent governance model.
- [ ] Define dashboard/control-surface role.
- [ ] Identify ADRs needed for accepted stack choices.
- [ ] Close or carry forward Sandbox 005.
