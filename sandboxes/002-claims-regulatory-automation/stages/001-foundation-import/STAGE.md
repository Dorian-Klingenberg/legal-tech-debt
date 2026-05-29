# Stage 001: Foundation Import

Created: 2026-05-29
Source: `../../001-legal-debt-primitives`
Status: Imported foundation; refocused on homeowners fixtures

## Purpose

Carry the useful Sandbox 001 probe into Sandbox 002 as a runnable starting point for Kentucky homeowners insurance.

This stage is intentionally not a new detector yet. It preserves the known-good plain-Python probe shape so the next 002 stages can adapt it toward high-value homeowners policy and claims smells.

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

- It does not yet detect homeowners-specific policy or claims smells.
- It does not yet implement Calculation Rule Drift.
- It uses only a tiny synthetic homeowners-oriented fixture, not real Kentucky insurance material.
- It does not include regulatory feed ingestion.
- It does not introduce a database, service, or production architecture.

## Next Stage

Create a narrow Kentucky homeowners fixture and adapt this imported probe into a dual-detector experiment:

1. Broken Link / Null Reference Clause
2. Calculation Rule Drift

That next stage should keep the same plain local execution style.
