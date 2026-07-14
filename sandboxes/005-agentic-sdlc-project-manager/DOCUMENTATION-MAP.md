# Sandbox 005 Documentation Map

Status: Current
Updated: 2026-07-13

## Purpose

This is the discovery surface for Sandbox 005. It answers where to start, where
each stage is documented, and which file owns which kind of truth.

## Start Here

1. [`README.md`](README.md) - purpose, scope, design principles, and current
   system selection.
2. [`STAGE-PLAN.md`](STAGE-PLAN.md) - canonical stage sequence, status, gates,
   and overview checklists.
3. [`HANDOFF-2026-07-13.md`](HANDOFF-2026-07-13.md) - current resume point and
   exact next step.
4. [`LESSON.md`](LESSON.md) - sandbox-level reusable lesson and current limits.

## Stage Documents

| Stage | Status | Detailed document | Purpose |
|---|---|---|---|
| 001 - Stack concept and artifact contract | Complete | [`stages/001-stack-concept/STAGE.md`](stages/001-stack-concept/STAGE.md) | Define the repo-native control model and provisional hybrid. |
| 002 - Manual hybrid pilot | Ready; not started | [`stages/002-manual-pilot/STAGE.md`](stages/002-manual-pilot/STAGE.md) | Test the model on one bounded real project task. |
| 003 - Generated status surface | Planned | [`stages/003-generated-status-surface/STAGE.md`](stages/003-generated-status-surface/STAGE.md) | Generate disposable status from canonical repo artifacts. |
| 004 - Agent role and worktree experiment | Planned | [`stages/004-agent-role-worktree-experiment/STAGE.md`](stages/004-agent-role-worktree-experiment/STAGE.md) | Compare lightweight manual coordination with SwarmForge-style orchestration. |
| 005 - Phase A integration plan | Planned | [`stages/005-phase-a-integration-plan/STAGE.md`](stages/005-phase-a-integration-plan/STAGE.md) | Convert proven sandbox results into a Phase A-ready plan. |

## Stage 001 Supporting Evidence

- [`stages/001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md`](stages/001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md)
  - source-backed Agile V, SwarmForge, and Codex CLI comparison.
- [`stages/001-stack-concept/LESSON.md`](stages/001-stack-concept/LESSON.md)
  - narrow lesson about selecting an SDLC system by layer.
- [`stages/001-stack-concept/examples/`](stages/001-stack-concept/examples/)
  - task contract, evidence bundle, experiment-to-requirement, experiment-backed
    V&V, risk register, and dashboard read-model sketches.

## Project-Level Boundaries

- [`../../ADR-012-separate-sdlc-stack-from-agentic-product-stack.md`](../../ADR-012-separate-sdlc-stack-from-agentic-product-stack.md)
  - accepted separation between development SDLC tooling and product runtime
    agents.
- [`../../SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md`](../../SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md)
  - longer planning note and future checklist.
- [`../../AGENT_CONTEXT.json`](../../AGENT_CONTEXT.json)
  - compact current project context and active-sandbox pointer.

## Session Records

- [`../../journal/2026-07-13-sandbox-005-sdlc-system-selection.md`](../../journal/2026-07-13-sandbox-005-sdlc-system-selection.md)
  - system-selection research and Stage 001 closure.
- [`../../journal/2026-07-13-sandbox-005-stage-docs-and-lesson.md`](../../journal/2026-07-13-sandbox-005-stage-docs-and-lesson.md)
  - completion of all stage documents and the sandbox-level lesson.

## Truth And Drift Rules

- `STAGE-PLAN.md` owns stage order and current status.
- Each stage `STAGE.md` owns that stage's detailed scope, entry gate, plan,
  measurements, and completion criteria.
- `README.md` owns the sandbox purpose and current high-level direction.
- `LESSON.md` teaches reusable understanding; it does not change canonical
  scope or status.
- Handoffs are point-in-time resume notes; they do not override current stage
  documents.
- Generated Stage 003 outputs will be disposable projections, never canonical
  project state.
- `SANDBOX-005-EXPORT.md` is a historical 2026-06-10 export and is not current
  guidance.

## Documentation Completeness Checklist

- [x] Sandbox README exists and links the map.
- [x] Canonical stage plan exists.
- [x] Every planned stage has a dedicated `STAGE.md`.
- [x] Stage 001 evidence and local lesson are linked.
- [x] Sandbox-level lesson exists.
- [x] Current handoff is linked.
- [x] Session journals are discoverable.
- [ ] Stage 002 execution artifacts will be linked after the pilot begins.
- [ ] Generated Stage 003 outputs will be linked only after they exist.
