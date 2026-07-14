# 2026-07-13 Sandbox 005 Stage Documents And Lesson

## Session Summary

Completed the missing Sandbox 005 stage documentation and made the sandbox
lesson discoverable.

The user correctly observed that `STAGE-PLAN.md` described five stages while
only Stages 001 and 002 had dedicated `STAGE.md` files. The previously created
lesson was also stage-local and easy to miss.

## What Changed

- Added `sandboxes/005-agentic-sdlc-project-manager/DOCUMENTATION-MAP.md` as the
  discovery surface and truth-ownership guide.
- Added `sandboxes/005-agentic-sdlc-project-manager/LESSON.md` as the
  sandbox-level reusable lesson.
- Added the dedicated Stage 003 document:
  `stages/003-generated-status-surface/STAGE.md`.
- Added the dedicated Stage 004 document:
  `stages/004-agent-role-worktree-experiment/STAGE.md`.
- Added the dedicated Stage 005 document:
  `stages/005-phase-a-integration-plan/STAGE.md`.
- Updated the sandbox README with a visible five-stage table and lesson link.
- Updated `STAGE-PLAN.md` with a documentation-map link, direct links to every
  stage, and checked documentation-completeness items.
- Updated the current handoff with all stage and lesson paths.
- Updated `AGENT_CONTEXT.json` with the latest journal and documentation state.

## Decisions Made

- `STAGE-PLAN.md` remains canonical for stage order and status.
- Each stage `STAGE.md` owns detailed scope, entry gate, checklist,
  measurements, and completion criteria.
- `DOCUMENTATION-MAP.md` is the first discovery surface, not another status
  store.
- `LESSON.md` is the sandbox-wide teaching artifact.
- `stages/001-stack-concept/LESSON.md` remains the narrower system-selection
  lesson and is linked instead of duplicated or deleted.
- Creating a stage document does not start that stage. Stages 003-005 remain
  planned, and Stage 002 remains ready but not started.

## Lesson Captured

The sandbox-level lesson is:

> Control AI-assisted engineering by adopting evidence-backed controls one at a
> time, while keeping one canonical project truth. The control system must stay
> lighter than the work and must not become a second project beside the code.

The lesson also preserves Sandbox 005's distinctive model:

- conversation and experiments can originate requirements;
- experiments can provide V&V evidence after implementation;
- deterministic checks precede semantic review;
- roles and ceremony scale with risk;
- generated status remains disposable;
- development SDLC agents remain separate from product runtime agents.

## Validation Performed

- [x] Validate `AGENT_CONTEXT.json` with `python3 -m json.tool`.
- [x] Run `git diff --check` on tracked touched files.
- [x] Check every current Sandbox 005 Markdown relative link (40 checked).
- [x] Check touched files for trailing whitespace and final newlines.
- [x] Review focused status and confirm all five stage documents exist.

The scoped Git check passed. A repository-wide `git diff --check` remains noisy
because the pre-existing dirty worktree contains unrelated CRLF and trailing-
whitespace changes; those files were not modified as part of this work.

## Current State

- Stage 001: complete.
- Stage 002: ready, not started.
- Stage 003: planned, dedicated document present.
- Stage 004: planned, dedicated document present.
- Stage 005: planned, dedicated document present.

No implementation, dashboard, orchestration runtime, production infrastructure,
or product runtime agent was added.

## What Comes Next

- [ ] Begin Stage 002 only after explicit owner direction.
- [ ] Complete the clean-worktree and native WSL Codex preflight.
- [ ] Run `S005-PILOT-001` and measure whether the proposed controls reduce
      ambiguity and improve evidence.
- [ ] Revise the provisional lesson from pilot evidence rather than assumption.
