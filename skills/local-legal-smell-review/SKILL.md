---
name: local-legal-smell-review
description: Run and interpret the local deterministic legal smell engine over policy or regulatory evidence. Use when reviewing local JSONL/JSON evidence, testing one of the five Sandbox 008 smell families, producing source-traceable findings, or preparing the engine for a Python, CLI, Codex, MCP, Azure Functions, or Foundry integration.
---

# Local Legal Smell Review

Use the repository-local engine as the execution source of truth. It produces
human-reviewable leads, not legal conclusions.

## Source of truth

- Engine: `sandboxes/008-local-legal-smell-engine/`
- Usage: `sandboxes/008-local-legal-smell-engine/docs/USAGE.md`
- Stage contract: `sandboxes/008-local-legal-smell-engine/stages/001-engine-extraction/STAGE.md`
- Adapter boundary: `sandboxes/008-local-legal-smell-engine/stages/002-adapters/STAGE.md`
- Decision records: `sandboxes/008-local-legal-smell-engine/adr/`
- Cross-agent skill workflow: `skills/SKILL-DEVELOPMENT.md`

## Workflow

1. Confirm the active input scope and whether the evidence is synthetic,
   preserved, or incomplete.
2. Read the engine usage and stage documents before changing code or inputs.
3. Run one detector first when diagnosing a smell; run all five only when the
   user wants a broad review.
4. Preserve `run_id`, `source_id`, `node_id`, `source_type`, evidence text, and
   missing-evidence details in any handoff or report.
5. Treat findings as review leads. Ask the reviewer to verify package
   completeness, authority identity, applicability, and effective dates.
6. Use the Python API or CLI for local work. Keep MCP, Azure Functions, and
   Foundry as adapters over the same engine contract.
7. Run the focused test suite after code or fixture changes:
   `python -B -m unittest discover -s tests -v` from the engine directory.

## Five supported families

- `SMELL1`: Overbroad / Non-deterministic Exclusions
- `SMELL2`: Magic Number / Magic Valuation Terms
- `SMELL3`: Coverage Inversion / Contradictory Conditions
- `SMELL4`: Calculation Rule Drift / Unversioned Rate Reference
- `SMELL5`: Regulatory Mapping Smells

## Guardrails

- Do not reopen or mutate Sandbox 002 Stage 006 for local-engine work.
- Do not treat zero findings as proof that a smell is absent.
- Do not treat lexical matches, graph gaps, or unresolved citations as legal
  noncompliance without human and package-level review.
- Do not hide missing source material, authority uncertainty, or parser limits.
- Do not add cloud, vector, database, or hosted infrastructure to the core
  engine.

## Output expectations

Return the output path or JSONL result count, the smell and heuristic IDs,
source/node provenance, confidence, evidence limitations, and the next human
review question. Update shared journals, handoffs, or ADRs when the work changes
the project state.
