# 2026-06-03 Sandbox 002 Discovery And Instrumentation Path

## Summary

Sandbox 002 documentation was updated to remove ambiguity between the older fixture-first sequence and the new path.

The current path is:

> Build Stage 002 discovery-and-instrumentation before detector findings. Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist, and treat parser/reference uncertainty as part of the evidence layer.

## What Changed

Added path ADR:

- `skills/legal-rag-builder/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`

Added artifact-contract ADR after follow-up review:

- `skills/legal-rag-builder/adr/ADR-004-schema-run-identity-and-id-stability.md`

Updated canonical Sandbox 002 docs:

- `sandboxes/002-claims-regulatory-automation/002-claims-regulatory-automation-README.md`
- `sandboxes/002-claims-regulatory-automation/002-ROADMAP-revised.md`
- `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- `sandboxes/002-claims-regulatory-automation/002-RAG-SUBSYSTEM-PLAN.md`
- `sandboxes/002-claims-regulatory-automation/002-RAG-PHASE-PLAN.md`
- `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`

Updated support and startup docs:

- `BOOTSTRAP.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `sandboxes/002-claims-regulatory-automation/002-CARRY-FORWARD-FROM-001.md`
- `sandboxes/002-claims-regulatory-automation/002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md`
- `sandboxes/002-claims-regulatory-automation/002-ROI-CASES-FIVE-SMELLS.md`
- `sandboxes/002-claims-regulatory-automation/002-ROADMAP.md`
- `sandboxes/002-claims-regulatory-automation/stages/001-foundation-import/STAGE.md`
- `skills/legal-rag-builder/SKILL.md`
- `skills/legal-rag-builder/adr/ADR-001-rag-substrate-reuses-001-structure.md`
- `skills/legal-rag-builder/references/docling-local-stack-boundary.md`
- `skills/legal-rag-builder/references/rag-substrate-boundary-lesson.md`

## Decision

Stage 002 is now:

```text
stages/002-homeowners-discovery-instrumentation/
```

Its first outputs should include:

- `sources.jsonl`
- `parser_runs.jsonl`
- `blocks.jsonl`
- `block_stats.jsonl`
- `nodes.jsonl`
- `citations.jsonl`
- `references.jsonl`
- `edges.jsonl`
- `table_failures.jsonl`
- `parse_warnings.jsonl`
- `candidate_evidence.jsonl`
- `retrieval_bundles.json`
- `discovery_report.md`

Fixture examples should be curated from candidate evidence outputs. Synthetic seeds remain allowed only when clearly marked and traceable to real source context.

Follow-up delta from external review added:

- schema version and run identity for every JSON/JSONL artifact
- JSON Schemas under `schema/`
- stable `source_id` and deterministic `node_id` expectations
- `output/run_manifest.json`
- `data/heuristics.md`
- stronger parser block fields and table failure types
- sharper citation/reference enums
- conservative extra graph edge types for schedules, declarations, incorporation, state amendments, versions, exceptions, conditions, and sublimits
- candidate/retrieval bundle boundary fields such as heuristic IDs, evidence spans, supporting nodes, signal scores, and parser penalties
- Stage 002 guardrails against silent schema fields, unsupported edge types, semantic retrieval before a gold set, reviewer annotations in the substrate, and cross-document topic-modeling edges

Final clarification pass added:

- `source_hash` and `content_hash` definitions
- failed parse handling through `parser_runs.jsonl.status = failed` and `failure_reason`
- optional `char_span` / `token_span`, `retrievable_text`, and `stable_anchor`
- extra domain references and edges for coverage parts and notice periods
- node-centric retrieval bundle wording
- LLM usage constraints for Stage 002
- JSONL encoding/line conventions
- compact minimum schema outlines for nodes, candidate evidence, and retrieval bundles

## Validation

Ran repository text scans for stale path language:

- old `002-homeowners-policy-layer-smells` path
- old `003-homeowners-rag-ingestion` path
- `Stage 002 fixture` / fixture-first wording
- premature vector-store phrasing such as pgvector-first or Qdrant-first

The remaining matches were expected: the new ADR's rejected alternatives and tool-verification notes.

Ran `git diff --check`; it reported only line-ending warnings, no whitespace errors.

## Open Notes

`SECRET_SCAN_REPORT.md` was already modified in the worktree to mark the earlier scan findings as reviewed false positives. This journal did not modify that report.

## Closeout

Created current resume handoff:

- `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-03.md`

Final current path:

1. Stage 002 discovery-and-instrumentation
2. Stage 003 retrieval baseline and fixture curation
3. Stage 004 deterministic detectors
4. Stage 005 reviewer report
5. Stage 006 optional semantic retrieval experiment
6. Stage 007 optional visual drill-down

The next practical implementation move is to create the Stage 002 folder and wire the tiniest source slice through schema files, run manifest, parser diagnostics, JSONL evidence records, and a small discovery report.

No code implementation was started in this documentation pass.
