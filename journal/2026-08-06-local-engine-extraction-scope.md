# 2026-08-06 — Local Legal Smell Engine Scope

## Session Summary

The user asked whether the five already-prototyped legal smell detectors
required reopening Sandbox 002 Stage 006 before being generalized into a local
Python tool.

## What We Did

Inspected the preserved Stage 006 detector code, stage documentation, output
run `20260604_130606_18b0dec5`, Sandbox 007's active strategy scope, and the
repository's current sandbox index.

Stage 006 contains five detector modules, a shared `Finding` model, a runner,
and a 31-finding JSONL baseline. It is complete and coupled to the Sandbox 002
evidence substrate. Sandbox 007 Stage 002 is reserved for four different smell
families and should remain separate.

## Decision

Do not reopen Stage 006. Create Sandbox 008 as a new local-engine extraction
experiment and use Stage 006 as the behavioral and evidence-contract reference.

The first implementation target is a dependency-light Python package and CLI.
Cloud, MCP, Codex, and Foundry surfaces are later adapters rather than core
dependencies.

## Validation Performed

- Confirmed Stage 006 is marked complete in its stage document.
- Confirmed the five detector modules and shared runner exist.
- Inspected the preserved output and counted 31 findings: Smell 1 = 1,
  Smell 2 = 17, Smell 3 = 0, Smell 4 = 1, Smell 5 = 12.
- Confirmed the worktree was clean before documentation changes.
- No detector code was rerun; the preserved runner writes output into the
  evidence tree and the closed stage was intentionally left untouched.

## Current State

- [x] Sandbox 008 README created.
- [x] Sandbox 008 Stage 001 extraction plan created.
- [x] ADR-001 records the stage-boundary decision.
- [x] Sandbox index updated.
- [x] This journal records the decision and evidence.
- [ ] Generic package implementation has not started.

## Next Useful Work

- [ ] Define generic node, edge, evidence, and finding contracts.
- [ ] Port Magic Number / Magic Valuation Terms first.
- [ ] Add positive, negative, and insufficient-evidence fixtures.
- [ ] Validate local Python and CLI execution before porting the remaining detectors.

