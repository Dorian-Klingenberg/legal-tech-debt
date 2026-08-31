# Sandbox 008: Local Legal Smell Engine

**Status**: Active; Stages 001–002 implemented, Stage 003 benchmark ready for model runs  
**Started**: 2026-08-06  
**Scope**: Extract and generalize the five preserved Sandbox 002 Stage 006 detector families into a local-first Python engine.

## Purpose

Sandbox 002 Stage 006 proves that five policy-layer smell families can produce
structured, source-traceable findings. Its code is still coupled to the
Kentucky homeowners evidence substrate and its closed stage layout.

This sandbox evaluates the next boundary: a small, open-source-friendly Python
engine that can be used locally from Python or a CLI, while leaving Codex,
MCP, Azure Functions, and Microsoft Foundry as later adapters.

## Relationship to preserved work

- Sandbox 002 Stage 006 remains complete and frozen.
- Its detector modules, `Finding` contract, runner behavior, heuristics, and
  preserved 31-finding run are reference material for this sandbox.
- Sandbox 007 remains focused on its own Phase 1 MVP: Circular Definition,
  Rule Duplication, Hardcoded Jurisdiction Logic, and Null Reference Clause.
- New engine artifacts must not be written into Sandbox 002 Stage 006 output or
  silently added to Sandbox 007's planned implementation.

## Initial smell scope

The first engine slice covers the five already-prototyped families:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

The engine will preserve the distinction between a detector candidate and a
legal conclusion. Every result remains a human-reviewable lead with evidence,
provenance, uncertainty, and false-positive context.

## Boundaries

- [x] Local Python is the first execution target.
- [x] Deterministic heuristics are the first implementation target.
- [x] Existing Stage 006 code is reference material, not a file-edit target.
- [x] No Azure, Foundry, MCP, web service, database, vector store, or hosted
      deployment is required for Stage 001.
- [x] No cloud credentials or LLM are required for the core engine.
- [ ] Optional adapters may be planned after the local contract is stable.
- [ ] Additional smell families are out of scope until the five-smell engine
      contract is proven.

## Navigation

- [Stage 001: Engine Extraction](stages/001-engine-extraction/STAGE.md)
- [Stage 002: Integration Adapters](stages/002-adapters/STAGE.md)
- [Stage 003: Twenty-Smell Model Benchmark](stages/003-twenty-smell-model-benchmark/README.md)
- [ADR-001: Keep Stage 006 Frozen](adr/ADR-001-keep-stage-006-frozen.md)
- [ADR-002: Local Engine Implementation Decisions](adr/ADR-002-local-engine-implementation-decisions.md)
- [ADR-003: Integration Adapter Boundaries](adr/ADR-003-integration-adapter-boundaries.md)
- [Usage](docs/USAGE.md)

## Current implementation

Stage 001 now contains a dependency-free Python engine, JSONL input/output,
Markdown reporting, a Python API, a local CLI, five detector families, and
synthetic positive/negative/insufficient-evidence fixtures. The preserved
Stage 006 baseline remains unchanged and is used only for comparison.

Stage 003 is a separate benchmark lane for twenty new claims and cross-domain
smells. Its packets, prompts, and model outputs stay under the Stage 003
directory and are not part of the five-detector engine calibration.
