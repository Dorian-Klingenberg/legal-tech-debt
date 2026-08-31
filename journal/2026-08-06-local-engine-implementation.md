# 2026-08-06 — Local Legal Smell Engine Implementation

## Session Summary

Implemented Sandbox 008 Stage 001: a dependency-light local Python engine for
the five preserved policy-layer smell families.

## What Changed

- Added a `src/legal_smell_engine` package with versioned node, edge, corpus,
  run, and finding contracts.
- Added Python API, detector registry, JSONL input/output, CLI, and Markdown
  reporting.
- Ported all five detector families. Smells 1, 3, 4, and 5 were implemented in
  parallel in disjoint detector files.
- Added synthetic positive, negative, and insufficient-evidence fixtures.
- Added focused unit tests and a preserved Stage 006 baseline adapter test.
- Added usage documentation and ADR-002 with implementation decisions.

## Validation

`python -B -m unittest discover -s tests -v` passed all 6 tests.

The preserved Stage 006 output remains 31 findings: S1=1, S2=17, S3=0,
S4=1, S5=12. The generic adapter ran against the preserved source/node/edge
artifacts and produced 54 leads: S1=2, S2=39, S3=0, S4=1, S5=12.

The difference is recorded as a calibration result. It is primarily a reminder
that the generic engine does not yet reproduce every Kentucky-specific context
filter from Stage 006.

## Decisions

The implementation decisions and rationale are canonicalized in
[ADR-002](../sandboxes/008-local-legal-smell-engine/adr/ADR-002-local-engine-implementation-decisions.md).
The main choices were standard-library-only runtime behavior, generic typed
node/edge contracts, a run-scoped detector interface, explicit missing
evidence, JSONL plus Markdown outputs, and deferred hosting adapters.

## Current State

- [x] Local Python package implemented.
- [x] All five detector families ported.
- [x] Python API and CLI implemented.
- [x] Fixtures and tests implemented.
- [x] Preserved Stage 006 comparison performed.
- [x] ADR-002 created for review.
- [ ] Baseline count deltas calibrated.
- [ ] Codex, MCP, Azure Functions, and Foundry adapters designed or implemented.

