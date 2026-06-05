# 2026-06-05 — Sandbox 005 Agentic SDLC Project Manager

## Summary

Opened Sandbox 005 to explore the development SDLC/project-manager stack for Legal Tech Debt.

The concept is a repo-native project manager that turns conversation into task contracts, task contracts into implementation slices, implementation into verification evidence, and verification evidence into human-approved progress.

## What Changed

- Created `sandboxes/005-agentic-sdlc-project-manager/README.md`.
- Created `sandboxes/005-agentic-sdlc-project-manager/STAGE-PLAN.md`.
- Created `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/STAGE.md`.
- Added Sandbox 005 to `sandboxes/README.md`.
- Added Sandbox 005 to `AGENT_CONTEXT.json` as an active project thread.

## Decision Context

The owner rejected a generic shared dashboard/blueprint as too sloppy and clarified the actual target:

- combine Agile iteration with Agile V / V&V discipline,
- use Gherkin where it helps behavior and acceptance criteria,
- borrow Uncle Bob / Clean AI agentic discipline,
- evaluate SwarmForge-style worktree/role orchestration,
- use LLM-as-judge only as a semantic sensor,
- and eventually build a project-manager/control surface over repo truth.

The sandbox explicitly separates this SDLC stack from the future agentic product runtime stack, following ADR-012.

## Current State

Stage 001 is active and focused on the artifact contract:

- minimum disciplined task contract,
- evidence bundle format,
- Gherkin boundary,
- gate model,
- agent role set,
- dashboard read model,
- and duplicate-truth risks.

No implementation tooling has been built yet. The stage plan intentionally requires a manual pilot before any dashboard or orchestration implementation.

## Next Useful Work

Start Stage 001 by sketching:

- `task-contract.md`,
- `evidence-bundle.md`,
- `risk-register.md`,
- and `dashboard-read-model.md`.

Then run Stage 002 manually on one real low-to-medium risk backlog item before building a status surface.

## Validation

Ran `git diff --check` on the new sandbox docs, `sandboxes/README.md`, and `AGENT_CONTEXT.json`. It passed with only existing CRLF normalization warnings.
