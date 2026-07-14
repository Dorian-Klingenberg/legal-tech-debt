# Stage 001 Lesson: Select An SDLC Stack By Layer

Status: Provisional lesson pending Stage 002 pilot
Captured: 2026-07-13

## Problem

Agile V, SwarmForge, and Codex CLI initially looked like competing choices for
one agentic SDLC system.

Treating them as direct substitutes obscured the actual decision because each
candidate primarily owns a different layer:

- lifecycle assurance;
- execution;
- orchestration and isolation;
- or durable project truth.

## Why It Mattered

Installing one complete framework would not remove the need for the others. It
could also create a second backlog, task state store, instruction hierarchy, or
evidence model beside the repository's existing shared memory.

For this project, duplicate truth is a larger near-term risk than missing
orchestration features.

## Reusable Pattern

Evaluate agentic SDLC systems in this order:

1. **Canonical truth:** Which artifacts remain authoritative if every agent
   session and generated dashboard is deleted?
2. **Assurance method:** How are requirements, risks, tests, evidence, waivers,
   and human gates represented?
3. **Execution runtime:** Which agent reads the contract, changes files, runs
   tools, and emits inspectable results?
4. **Isolation and orchestration:** How are writers separated, work handed off,
   and concurrency controlled?
5. **Status projection:** How is current state generated from canonical truth
   without becoming another truth store?

Choose one owner per layer. Integrate through small file contracts. Do not merge
frameworks by copying all of their state, prompts, and conventions into one
repository.

## Concrete Application

Sandbox 005 currently assigns the layers as follows:

| Layer | Current owner |
|---|---|
| Canonical truth | Existing Legal Tech Debt repo artifacts |
| Assurance method | Existing task/evidence sketches plus selected Agile V concepts |
| Execution runtime | Codex CLI first |
| Isolation | Manual Git worktrees and one writer |
| Orchestration experiment | SwarmForge-style topology in Stage 004 |
| Status projection | Future generated Stage 003 output |

## Evidence

The comparison study found:

- Agile V has strong task, risk, evidence, and verifier ideas but introduces a
  parallel state tree and has material maturity and licensing caveats.
- SwarmForge has concrete worktree and handoff machinery but no lifecycle
  artifact model, no detected license, and defaults that do not fit this Python
  repository without adaptation.
- Codex CLI has the execution primitives needed for a first pilot but does not
  supply the lifecycle contract or Git isolation automatically.
- Sandbox 005 already models experiment-derived requirements and
  experiment-backed V&V, which none of the candidates should overwrite.

See
[`SDLC-SYSTEM-SELECTION-STUDY.md`](SDLC-SYSTEM-SELECTION-STUDY.md)
for primary-source links, commits, tests, and local readiness evidence.

## Limitations

- The layer model is a reasoned design, not yet a proven local workflow.
- The comparative evidence is a 2026-07-13 snapshot of fast-moving projects.
- A single bounded pilot cannot establish enterprise scalability.
- Avoiding framework installation may defer useful automation; Stage 004 must
  evaluate that tradeoff rather than assuming manual worktrees are permanent.

## Reuse Checklist

- [x] Name the canonical truth before selecting an agent runtime.
- [x] Separate method, runtime, orchestration, and status layers.
- [x] Preserve project-specific requirement origins and evidence semantics.
- [x] Check maturity, tests, license, and local prerequisites before adoption.
- [ ] Validate the layer boundaries on `S005-PILOT-001`.
- [ ] Remove fields or roles that the pilot does not use.
- [ ] Revisit orchestration only after one-writer manual coordination is
      measured.
