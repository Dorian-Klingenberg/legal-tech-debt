# 2026-06-04: Sandbox 002 Artifact Contract Repair

## Session Summary

We reviewed the Claude Code implementation of Sandbox 002 against the original discovery-and-instrumentation spec and found implementation drift in the Stage 002 artifact contract. The repaired path keeps the original design: deterministic JSON/JSONL artifacts, durable provenance, parser/reference uncertainty as evidence, and retrieval bundles shaped for future hybrid retrieval without adding vector infrastructure now.

This was treated as a contract repair, not a redesign. The decision is recorded in `sandboxes/002-claims-regulatory-automation/adr/ADR-008-stage-002-artifact-contract-repair.md`.

After validation, we also closed Sandbox 002 as complete for its discovery/retrieval/detector/reviewer-report purpose. That closure decision is recorded in `sandboxes/002-claims-regulatory-automation/adr/ADR-009-close-sandbox-002-with-smell-5-limitation.md` and `sandboxes/002-claims-regulatory-automation/CLOSURE.md`.

## What Changed

- Restored distinct `source_hash` and `content_hash` semantics.
- Added `source_hash` to source-derived parser, block, node, citation, reference, edge, warning, table-failure, and candidate-evidence records.
- Changed candidate evidence identity back to `candidate_id`.
- Expanded `run_manifest.json` to include parsers used, schema versions, config snapshot, and parse statistics.
- Repaired Stage 002 retrieval bundles to use `hits[]` with lexical, semantic, graph, citation/reference, metadata, parser-penalty, parser diagnostics, and expanded-context signal slots.
- Repaired Stage 003 retrieval bundles to match the same schema.
- Updated Stage 003 expected source types to the actual expanded corpus source types.
- Removed stale report language that implied carrier SERFF filings were still absent.
- Added ADR-008 and updated the RAG stage plan, bootstrap map, agent entry files, and compact agent context.
- Added ADR-009 and `CLOSURE.md` so Sandbox 002 closes cleanly while carrying Smell 5 as a documented limitation.

## Decisions Made

- The simplified artifact shape from implementation is implementation drift unless a later ADR explicitly accepts it.
- Stage 002 schemas are the contract for downstream stages.
- Stage 003 retrieval bundles must remain compatible with the Stage 002 retrieval-bundle schema.
- Vector infrastructure remains deferred, but semantic signal slots stay in the evidence substrate as `null`/reserved fields.
- Smell 5 remains an open detector-calibration problem, not evidence that regulatory mapping risk is absent.
- Smell 5 calibration is not a blocker to starting Sandbox 003, but Sandbox 003 must not claim five-smell completeness unless Smell 5 is calibrated.

## Validation Performed

- `python -m compileall src` succeeded for Stages 003, 004, 006, and 007 after patches.
- Stage 002 repaired run created: `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/`.
- Stage 002 schema validation passed:
  - 28 sources
  - 2,103 blocks
  - 353 nodes
  - 100 citations
  - 55 references
  - 797 edges
  - 0 table failures
  - 6 parse warnings
  - 121 candidate evidence items
  - 41 Stage 002 discovery retrieval bundles
- Stage 003 retrieval rerun passed and emitted 39 schema-valid retrieval bundles under `output/003/20260604_130606_18b0dec5/`.
- Stage 004 gold-set evaluation rerun preserved the previous result:
  - exact phrase: 20/21 items hit, 95% recall
  - BM25: 21/21 items hit, 100% recall
  - semantic decision: defer
- Gold-set validator passed against run 18b0dec5: all 21 expected nodes exist, sources match, and query terms match.
- Stage 006 detectors reran with 23 findings:
  - Smell 1: 1 LOW
  - Smell 2: 17 MEDIUM
  - Smell 3: 4 LOW
  - Smell 4: 1 HIGH
  - Smell 5: 0
- Stage 007 reviewer reports regenerated under `output/007/20260604_130606_18b0dec5/`.

## Current State

Sandbox 002 Stages 002-007 are complete and aligned with the repaired artifact contract. Sandbox 002 is now closed as a proof of concept. The preserved repaired run is `output/002/20260604_130606_18b0dec5/`.

The gold-set re-evaluation loose thread is closed for the expanded corpus: BM25 still hits 21/21. Stage 005 semantic retrieval remains deferred because the project still lacks paraphrase-style reviewer queries and a documented BM25 failure.

## What Comes Next

- [ ] Calibrate the Smell 5 detector against the expanded KFBM/KNIC corpus.
- [ ] Keep vector infrastructure deferred until paraphrase queries plus a BM25 miss justify reopening Stage 005.
- [ ] Use Sandbox 003 for findings triage/reporting design rather than continuing to reshape Sandbox 002.
- [ ] Leave manual SERFF source gaps parked unless a concrete Sandbox 003 question requires them.
