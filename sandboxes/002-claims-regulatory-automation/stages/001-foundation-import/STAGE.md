# Stage 001: Foundation Import

Created: 2026-05-29
Source: `../../001-legal-debt-primitives`
Status: Imported foundation; refocused on homeowners discovery-and-instrumentation

## Completion Checklist

- [x] Import the useful plain-Python Sandbox 001 foundation.
- [x] Reframe the next stage around Kentucky homeowners evidence.
- [x] Preserve this stage as a completed bridge, not an active detector lane.

## Purpose

Carry the useful Sandbox 001 probe into Sandbox 002 as a runnable starting point for Kentucky homeowners insurance.

This stage is intentionally not a new detector yet. It preserves the known-good plain-Python probe shape so the next 002 stages can adapt it toward the five active Kentucky homeowners policy-layer smells.

## Question

Can the 001 legal debt primitives be moved into 002 without adding infrastructure or losing the quick, readable proof-of-concept style?

## Imported Artifacts

- `src/legal_debt_probe.py`
- `data/corpus/homeowners_claims_manual.md`
- `data/corpus/homeowners_property_reference.md`

## Run

From this stage folder:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Expected outputs:

- `output/findings.json`
- `output/report.md`
- `output/section_index.csv`
- `output/adjacency_matrix.csv`
- `output/two_hop_matrix.csv`
- `output/transitive_closure.csv`
- `output/dependency_roots.json`

## What This Stage Carries Forward

- section extraction
- reference extraction
- dangling/null reference detection
- circular reference detection
- orphan definition detection
- unversioned external authority detection
- graph/matrix outputs
- JSON/Markdown/CSV evidence outputs

## What This Stage Does Not Claim

- It does not yet detect the five active homeowners policy-layer smells.
- It uses only a tiny synthetic homeowners-oriented fixture, not real Kentucky insurance material.
- It does not include regulatory feed ingestion.
- It does not introduce a database, service, or production architecture.

## Next Stage

Create a narrow Kentucky homeowners discovery-and-instrumentation stage and adapt this imported probe style toward source-traceable candidate evidence for the five active smells:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

That next stage should keep the same plain local execution style and emit legal nodes, citations, broader references, conservative graph edges, parser diagnostics, retrieval bundles, and candidate evidence before promoting anything into detector findings.
