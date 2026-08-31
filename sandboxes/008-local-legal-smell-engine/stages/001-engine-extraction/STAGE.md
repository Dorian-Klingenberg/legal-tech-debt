# Stage 001: Local Engine Extraction

**Status**: Complete with baseline-calibration follow-up  
**Sandbox**: 008-local-legal-smell-engine  
**Reference**: Sandbox 002 Stage 006 deterministic detectors  
**Decision record**: [ADR-001](../../adr/ADR-001-keep-stage-006-frozen.md)
**Implementation decisions**: [ADR-002](../../adr/ADR-002-local-engine-implementation-decisions.md)

## Objective

Extract the reusable detector behavior from Sandbox 002 Stage 006 into a
small, generic, local Python engine. The stage should prove that the five
detector families can run against a generic document/node input contract
without requiring the Kentucky Stage 002 `RunIndex` or cloud services.

## What is already complete

- [x] Five detector families exist in preserved Stage 006 code.
- [x] Stage 006 emits structured JSONL findings and Markdown reports.
- [x] Stage 006 records confidence, rationale, reviewer questions, and false-positive risk.
- [x] A preserved baseline run exists: 31 findings from run `20260604_130606_18b0dec5`.
- [x] The decision not to reopen or mutate Stage 006 is recorded in ADR-001.
- [x] Sandbox 007 is explicitly kept separate because its Stage 002 has a different smell scope.

## Planned deliverables

- [x] Define a versioned generic input contract for documents, nodes, and optional graph edges.
- [x] Define a versioned finding/result contract that preserves source and node provenance.
- [x] Extract the five detectors behind one small Python detector interface.
- [x] Replace Kentucky-specific source prefixes and carrier names with configurable policy.
- [x] Provide a local Python API and a simple CLI over local JSON/JSONL or Markdown input.
- [x] Add positive, negative, and insufficient-evidence fixtures for each smell family.
- [x] Add focused tests or executable probes for detector behavior and schema output.
- [x] Compare the generic engine's findings against the preserved Stage 006 baseline where
      the generic input adapter represents the same evidence.
- [x] Document false-positive boundaries and the difference between candidate, finding,
      and legal conclusion.

## Proposed shape

```text
src/legal_smell_engine/
  contracts.py       # generic node, edge, evidence, and finding models
  engine.py          # detector registration and execution
  profiles.py        # smell names, heuristic metadata, configurable rules
  detectors/
    smell1_exclusions.py
    smell2_valuation.py
    smell3_coverage_inversion.py
    smell4_calculation_drift.py
    smell5_regulatory_mapping.py
  adapters/
    jsonl.py
    cli.py
fixtures/
tests/
docs/
```

The exact package location and naming can change during implementation, but the
engine must remain importable without the Sandbox 002 source tree on
`PYTHONPATH`.

## Acceptance gates

- [x] `python` can import the engine from a clean local checkout without Azure,
      Foundry, MCP, LangChain, vector, or proprietary dependencies.
- [x] A caller can run one detector and all five detectors through Python.
- [x] A caller can run the same operation through a local CLI.
- [x] Outputs are deterministic apart from explicitly documented run/timestamp fields.
- [x] Every finding carries a stable smell/heuristic identifier, evidence text,
      provenance, confidence, reviewer question, and false-positive risk.
- [x] Missing graph or authority evidence is represented as uncertainty rather
      than silently treated as a confirmed defect.
- [x] Fixture validation demonstrates that zero findings means only that the
      detector found no supported candidate in the supplied evidence.
- [x] The preserved Stage 006 source and output remain unchanged.

## Explicit non-goals

- [x] Do not reopen Sandbox 002 Stage 006.
- [x] Do not rewrite the closed Stage 002 artifact schema.
- [x] Do not add hosted deployment or production infrastructure.
- [x] Do not claim that lexical matches establish legal noncompliance.
- [x] Do not implement the additional Sandbox 007 smell families in this stage.

## Validation results

Command:

```text
python -B -m unittest discover -s tests -v
```

Result: **6 tests passed**.

The preserved Stage 006 output remains **31 findings** with counts S1=1,
S2=17, S3=0, S4=1, S5=12. The generic engine ran against the preserved
nodes/edges after a source-type adapter and produced **54 review leads**:
S1=2, S2=39, S3=0, S4=1, S5=12. This is a portability/calibration result,
not a claim of parity. The higher S1/S2 counts reflect the generic port's
broader context and remaining source/package filtering work.

## Next mechanical step

Next, calibrate the generic engine against the preserved baseline: make source
layer policy explicit, decide which Stage 006 context filters belong in the
generic contract, and add targeted regression cases for the S1/S2 deltas.
