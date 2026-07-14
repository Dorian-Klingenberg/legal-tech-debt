# Sandbox 005 Lesson: Control AI Work Without Creating A Second Project

Status: Provisional; Stage 001 evidence complete, Stage 002 pilot pending
Captured: 2026-07-13

## Problem

AI coding tools can make implementation faster, but speed does not create a
trustworthy software lifecycle. A multi-agent setup can still lose requirements,
duplicate project state, approve its own assumptions, or produce attractive
reports without durable evidence.

The obvious response - installing a comprehensive SDLC framework and a large
agent swarm - can create a second problem. The framework may introduce its own
backlog, IDs, state files, prompts, dashboard, and definition of completion
beside the repository's existing truth.

## Why It Matters Here

Legal Tech Debt already uses Codex, Claude Code, and GitHub Copilot. It also has
repo-visible startup rules, ADRs, journals, handoffs, sandbox stages, preserved
runs, and source-traceable evidence artifacts.

Any SDLC system that ignores or replaces those records would reduce trust rather
than improve it. The development control system also cannot be confused with the
future product runtime that analyzes legal and insurance documents.

## Reusable Lesson

The useful unit of adoption is a control that proves its value, not an entire
framework.

For each implementation slice:

1. Preserve why the work exists: conversation, experiment, backlog, ADR, or
   external requirement.
2. Form a bounded task contract before implementation.
3. Keep one canonical project state in the repository.
4. Use one implementation writer until parallel writing proves safe.
5. Require deterministic evidence before semantic review.
6. Use a fresh verifier for risk-appropriate independent review.
7. Record uncertainty, skipped validation, and human approval explicitly.
8. Promote only durable experiment findings into requirements or risks.
9. Generate status from canonical artifacts; never make the dashboard canonical.
10. Add ceremony only when it catches ambiguity, prevents a defect, preserves
    evidence, or makes review materially easier.

## Concrete Sandbox Design

Sandbox 005 separates the system into layers:

| Layer | Current choice |
|---|---|
| Project truth | Existing Git, Markdown, JSON/JSONL, ADRs, backlog, journals, handoffs, and sandbox records |
| Assurance method | Repo-native task/evidence artifacts with selected Agile V concepts |
| Execution | Codex CLI first |
| Isolation | Manual Git worktrees and one implementation writer |
| Verification | Deterministic checks, fresh-context verifier, and human gates where required |
| Orchestration experiment | SwarmForge-style comparison in Stage 004 |
| Status | Disposable generated projection in Stage 003 |

The narrower selection lesson is in
[`stages/001-stack-concept/LESSON.md`](stages/001-stack-concept/LESSON.md).
The primary evidence and candidate comparison are in
[`stages/001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md`](stages/001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md).

## Evidence So Far

- Stage 001 defined a task contract, evidence bundle, experiment-to-requirement
  record, experiment-backed V&V record, risk register, and dashboard read model.
- The candidate comparison showed that Agile V, SwarmForge, and Codex CLI solve
  different layers rather than acting as complete substitutes.
- Agile V supplied useful assurance concepts but also showed maturity, state
  duplication, and licensing concerns.
- SwarmForge supplied useful isolation and handoff concepts but did not supply
  the lifecycle artifact model and is not ready for direct code adoption.
- Codex CLI supplied practical execution primitives but does not create the
  lifecycle contract or worktree isolation by itself.
- The existing repository model uniquely preserves experimentation as both a
  source of requirements and a form of V&V evidence.

## Limits

- Stage 002 has not tested whether the proposed controls are worth their cost.
- No dashboard or orchestration implementation exists yet.
- A fresh model context is not the same as organizational, vendor, or human
  independence.
- A single pilot will establish local usefulness, not enterprise scalability or
  regulatory compliance.
- External tools and licenses can change; recheck before adoption.

## What To Reuse

- [x] Keep canonical truth separate from agent sessions and dashboards.
- [x] Keep the SDLC stack separate from product runtime agents.
- [x] Treat conversation and experiments as requirement origins.
- [x] Treat experiments as possible V&V evidence after implementation.
- [x] Scale roles, gates, and testing to risk.
- [x] Prefer independently authored local contracts over wholesale framework
      imports.
- [ ] Validate the proposed artifact chain on `S005-PILOT-001`.
- [ ] Remove controls that produce no useful decision or evidence in the pilot.
- [ ] Add orchestration only if Stage 004 measures a real benefit.
- [ ] Promote the lesson from provisional after the manual pilot confirms or
      corrects it.
