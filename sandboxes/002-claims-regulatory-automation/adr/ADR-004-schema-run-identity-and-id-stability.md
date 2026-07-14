# ADR-004: Schema, Run Identity, And ID Stability For Stage 002

Date: 2026-06-03
Status: Accepted
Scope: Sandbox 002 discovery-and-instrumentation artifacts

## Context

Stage 002 will emit many JSON/JSONL artifacts that later stages consume. Without schema versioning, run identity, and stable source/node IDs, later retrieval baselines, fixture curation, detector outputs, and reviewer reports could silently drift when parser configuration or segmentation changes.

Parser uncertainty is also part of the evidence layer. That means records need enough identity and provenance to compare runs and understand whether an apparent evidence change came from the source text, parser behavior, schema change, or candidate-generation heuristic.

## Decision

Every Stage 002 JSON/JSONL artifact must carry:

- `schema_version`
- `run_id`
- `created_at`
- `source_hash` or `content_hash` where applicable

Stage 002 must emit:

- artifact-specific JSON Schemas under `schema/`
- `output/run_manifest.json`
- stable `source_id` values across runs when document identity does not change
- deterministic `node_id` values under a fixed parsing and segmentation strategy

Parser or segmentation changes that break ID stability require a schema/version bump, `run_mode` or equivalent run note, and migration notes.

Stage 003 and later stages must conform to the Stage 002 schemas or explicitly version and document any extension. They must not silently add fields that downstream consumers rely on.

If an artifact is not listed under `schema/`, it is experimental and not part of the Stage 002 contract. Experimental artifacts must not become Stage 003+ dependencies until they are added to `schema/` and versioned.

## Consequences

Positive:

- makes run-to-run comparisons possible
- protects later retrieval and detector stages from silent field drift
- allows parser or segmentation changes to be audited
- gives candidate evidence and retrieval bundles durable node references

Tradeoffs:

- Stage 002 has slightly more upfront schema work
- deterministic node IDs may need adjustment if parser block IDs are unstable
- schema changes need intentional versioning even in a proof-of-concept

## Follow-Up

- Stage 002 implementation should create JSON Schemas for each artifact type.
- Stage 002 implementation should create `output/run_manifest.json` for each run.
- `data/heuristics.md` should document heuristic rule IDs and versions so candidate evidence can be traced to the rule that generated it.
