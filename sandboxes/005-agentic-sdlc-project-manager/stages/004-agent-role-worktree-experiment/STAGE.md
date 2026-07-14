# Stage 004: Agent Role And Worktree Experiment

Status: Planned
Entry gate: Stage 002 proves the manual role model useful; Stage 003 remains
repo-truth-only

## Purpose

Evaluate whether explicit multi-agent orchestration improves real work in this
repository after the manual role and evidence model has been tested.

This is an experiment about development coordination. It is not a product-agent
runtime experiment.

## Controlling Question

Does a SwarmForge-style role, worktree, and handoff topology improve quality,
elapsed time, or human oversight enough to justify its setup and coordination
cost over Codex subagents plus manual worktrees?

## Baseline And Candidate

Baseline:

- one lead/specifier;
- one implementation writer in a manual worktree;
- one fresh, read-only verifier;
- Codex CLI subagents used mainly for read-heavy parallel work;
- repo-native task and evidence artifacts.

Candidate:

- equivalent roles launched through a SwarmForge-style topology or a clean-room
  local adapter;
- dedicated worktrees;
- commit-linked handoffs;
- the same task and evidence contract as the baseline.

Do not compare different lifecycle methods while comparing orchestration. The
artifact contract, acceptance criteria, and validation expectations must remain
constant.

## Licensing And Prerequisite Gate

The Stage 001 study found no detected license grant for SwarmForge at the
reviewed commit. Before copying, modifying, or running upstream project code:

- [ ] Recheck the current repository license.
- [ ] Obtain permission if no adequate license exists.
- [ ] Record the exact upstream commit or release.
- [ ] Inspect installation and startup scripts.
- [ ] Pin every dependency and quality tool.
- [ ] Run upstream tests in a disposable environment.
- [ ] Confirm native WSL Codex, `zsh`, tmux, Git, and Babashka prerequisites.

If the license gate fails, test only independently authored orchestration
concepts. Do not copy upstream scripts or prompts.

## In Scope

- Planner/specifier, implementer, and verifier roles.
- Optional read-only researcher when the task has separable research.
- Worktree naming, branch ownership, and file allowlists.
- Commit-based handoffs and evidence references.
- Recovery from restart, failed role, rejected verification, and stale handoff.
- Comparison of setup cost, human interventions, defects, and conflicts.

## Out Of Scope

- Product runtime agents or customer data.
- Six permanent roles by default.
- Autonomous merge, release, deployment, or external communication.
- Unpinned tool installation at role startup.
- Multiple concurrent implementation writers unless separately approved.
- Treating agent consensus as human approval.

## Experimental Design

Use two tasks of similar size and risk, or one replayable fixture task:

1. Run the baseline with Codex plus manual worktrees.
2. Run the candidate topology with the same artifact contract and gates.
3. Keep model, reasoning level, repository snapshot, and validation commands as
   comparable as practical.
4. Record deviations rather than hiding them.
5. Have the human owner compare the evidence and coordination burden.

## Role Checklist

- [ ] Define a project-neutral lead/specifier prompt.
- [ ] Define a single-writer implementer prompt.
- [ ] Define a read-only verifier prompt.
- [ ] Define optional researcher activation criteria.
- [ ] Define which role may create commits.
- [ ] Define which role may merge or request human approval.
- [ ] Define blocked-task behavior and forbidden silent handoffs.
- [ ] Keep canonical prompts outside tool-private storage.

## Worktree And Handoff Checklist

- [ ] Define branch and worktree naming conventions.
- [ ] Exclude the dirty main checkout from writer roles.
- [ ] Define starting commit and synchronization rules.
- [ ] Define file allowlists per role.
- [ ] Define a compact, validated handoff envelope.
- [ ] Link handoffs to task ID, commit, and expected receiver action.
- [ ] Keep runtime queue state uncommitted and non-canonical.
- [ ] Test restart and stale-handoff recovery.
- [ ] Test rejection and repair without bypassing verification.

## Verification Checklist

- [ ] Run all task-level deterministic checks in both configurations.
- [ ] Use the same verifier rubric in both configurations.
- [ ] Check for out-of-scope edits and branch contamination.
- [ ] Check whether handoff summaries omit required evidence.
- [ ] Check whether parallel reads improved elapsed time.
- [ ] Check whether role separation found defects self-review missed.
- [ ] Check whether orchestration introduced merge conflicts or duplicated work.
- [ ] Capture human approval and unresolved risk.

## Measurements

- [ ] Environment and configuration setup time.
- [ ] Total wall-clock time and agent-active time where available.
- [ ] Human interventions and approval prompts.
- [ ] Agent runs, retries, and failed handoffs.
- [ ] Defects found before and after implementation.
- [ ] Verifier-only findings.
- [ ] Merge conflicts, duplicated work, and out-of-scope changes.
- [ ] Token or usage cost where the tools expose it reliably.
- [ ] Evidence completeness and stale-state count.
- [ ] Owner rating of visibility, anxiety reduction, and process burden.

## Completion Criteria

- [ ] Baseline and candidate evidence bundles are comparable.
- [ ] The role topology and worktree rules are documented.
- [ ] Licensing and dependency decisions are explicit.
- [ ] Measured benefits and costs are recorded.
- [ ] The project chooses one outcome: adopt tool, adopt concepts, or retain the
      simpler baseline.
- [ ] An ADR is written only if a durable architecture choice is accepted.
- [ ] A lesson, journal, handoff, stage plan, and documentation map are updated.

## Decision Rule

Prefer the simpler baseline unless orchestration produces a material,
repeatable improvement in quality, elapsed time, recoverability, or human
oversight without creating duplicate truth or unsafe parallel writing.

The source-backed candidate assessment is in
[`../001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md`](../001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md).
