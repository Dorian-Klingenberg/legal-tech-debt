# ADR-001: Keep Sandbox 002 Stage 006 Frozen During Local Engine Extraction

**Date**: 2026-08-06  
**Status**: Accepted  
**Scope**: Sandbox 008 local legal smell engine

## Context

Sandbox 002 Stage 006 contains the first working implementation of five
policy-layer smell detector families. It is complete, has preserved outputs,
and is part of the project's evidence substrate. The detector runner is useful
as a reference but is coupled to Sandbox 002's `RunIndex`, JSONL artifacts,
Kentucky source-ID conventions, and carrier identifiers.

Sandbox 007 is active and has a separate Stage 002 plan for four additional
smell families. Extending either closed Stage 006 or Sandbox 007's planned
scope would make the experiment history and acceptance criteria ambiguous.

## Decision

Do **not** reopen or mutate Sandbox 002 Stage 006 for the generic-engine work.
Create Sandbox 008 and implement the local engine as a separately scoped stage.

Use Stage 006 as reference material for:

- detector behavior and heuristic identifiers;
- the `Finding` evidence and reviewer contract;
- confidence and false-positive handling;
- the 31-finding preserved baseline;
- lessons about outer-layer filtering and graph-gap detection.

The first implementation target is a dependency-light Python package and CLI.
Codex skills, MCP, Azure Functions, and Foundry adapters remain downstream
integration surfaces, not core-engine dependencies.

## Consequences

- Stage 006 remains a stable comparison point.
- Sandbox 008 can evolve its generic contracts without changing historical evidence.
- The same detector logic can eventually be exposed through Python, CLI, Codex,
  MCP, Azure Functions, or Foundry adapters.
- A small amount of porting and parity work is required.
- The generic engine must explicitly model what Stage 006 received implicitly
  from `RunIndex` and the Kentucky corpus.

## Rejected alternatives

1. **Reopen Stage 006 and refactor in place** — rejected because it would mix
   historical evidence-substrate maintenance with new productization work.
2. **Put the generic engine in Sandbox 007 Stage 002** — rejected because that
   stage is already scoped to four new smell families and has its own success
   criteria.
3. **Build deployment adapters first** — rejected because the local contract and
   evidence behavior must be stable before hosting surfaces are evaluated.

## Follow-up checklist

- [ ] Create the generic input and result contracts.
- [ ] Port one detector and validate it with fixtures.
- [ ] Port the remaining four detector families.
- [ ] Compare appropriate outputs with the preserved Stage 006 run.
- [ ] Add CLI and Python API documentation.
- [ ] Plan Codex/MCP/Azure/Foundry adapters only after the local engine gate passes.

