# ADR-008: Repair Stage 002 Artifact Contract After Implementation Drift

Date: 2026-06-04
Status: Accepted
Scope: Sandbox 002 Stage 002 discovery-and-instrumentation artifacts, schemas, and downstream retrieval bundles

## Context

Sandbox 002's controlling path is a deterministic, JSONL-first discovery-and-instrumentation pipeline for the Kentucky homeowners corpus. ADR-003 established that discovery and instrumentation come before detector findings. ADR-004 established that Stage 002 artifacts need schema version, run identity, creation timestamp, stable source/node IDs, and parser/reference uncertainty under a fixed parsing strategy.

During implementation, parts of the Stage 002 artifact shape drifted away from the original spec without an ADR. The drift mostly simplified provenance and retrieval-bundle structure:

- `source_hash` and `content_hash` were not clearly separated.
- Several source-derived artifacts did not carry `source_hash`.
- candidate evidence used `evidence_id` instead of the specified candidate identity.
- retrieval bundles were flattened around a single node instead of using a future-compatible `hits[]` shape.
- retrieval signal fields did not consistently reserve space for lexical, semantic, graph, citation/reference, metadata, and parser-penalty signals.
- some downstream reports still described the pre-expansion corpus as if carrier filings were absent.

Those changes may have been pragmatic implementation choices, but no ADR records them as accepted design changes. The safer interpretation is implementation drift, not a new canonical plan.

## Decision

Restore the Stage 002 artifact contract as the controlling design.

The repaired contract is:

- `source_hash` is a stable canonical-document identity hash.
- `content_hash` is the file-byte content hash.
- source-derived records carry `source_id` and `source_hash` wherever they need durable provenance.
- candidate evidence uses `candidate_id`.
- retrieval bundles use `hits[]`, even when the current bundle contains one primary hit.
- each retrieval hit carries full signal slots for future hybrid retrieval: lexical, semantic, graph, citation/reference, metadata, parser penalty, parser diagnostics, and expanded context.
- semantic signal fields are allowed to be present but `null` while semantic/vector infrastructure remains deferred.
- Stage 003 retrieval bundles must remain compatible with the Stage 002 retrieval-bundle schema.
- stale corpus-gap and source-type language must be updated when the corpus expands.

This preserves the principle: defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist.

## Consequences

- Stage 002 schemas now enforce the repaired provenance and retrieval-bundle shape.
- Stage 002 code now emits `source_hash`, `content_hash`, `candidate_id`, run manifest parser/config/schema metadata, and schema-shaped retrieval bundles.
- Stage 003 retrieval output now uses the same `hits[]` retrieval-bundle contract.
- Stage 004 and Stage 007 no longer imply that carrier SERFF filings are absent from the active corpus.
- Future agents should treat unexplained divergence from the Stage 002 schema as a bug unless a later ADR changes the contract.

## Rejected Alternatives

- Accept the simplified implementation shape as canonical.
  - Rejected because it would make later semantic/graph/citation retrieval harder and would contradict ADR-004 without an explicit decision.
- Patch only the docs and leave generated artifacts loose.
  - Rejected because downstream stages consume these artifacts and should fail loudly when contract fields disappear.
- Add a vector database now to force the retrieval shape.
  - Rejected because Stage 005 still supports deferring vector infrastructure until paraphrase queries and a documented BM25 failure justify it.

## Follow-Up Checklist

- [x] Repair Stage 002 models and writers to emit contract fields.
- [x] Repair JSON Schemas for source, parser, block, node, citation, reference, edge, warning, table failure, candidate evidence, retrieval bundle, and run manifest artifacts.
- [x] Repair Stage 003 retrieval bundles to use the same `hits[]` shape.
- [x] Re-run Stage 002 on the 28-source corpus.
- [x] Validate Stage 002 output against schemas.
- [x] Re-run Stage 003 retrieval baseline on the repaired run.
- [x] Validate Stage 003 retrieval bundles against the Stage 002 retrieval-bundle schema.
- [x] Re-run Stage 004 gold-set evaluation on the repaired run.
- [x] Re-run Stage 006 deterministic detectors on the repaired run.
- [x] Re-run Stage 007 reviewer report on the repaired run.
- [ ] Calibrate Smell 5 detector behavior against the expanded KFBM/KNIC corpus.
- [ ] Decide in Sandbox 003 whether triage/reporting needs a richer finding schema.
