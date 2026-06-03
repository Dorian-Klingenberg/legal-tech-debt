# ADR-003: Discovery And Instrumentation Comes Before Fixture Detectors

Date: 2026-06-03
Status: Accepted
Scope: Sandbox 002 path; Legal RAG Builder evidence substrate

## Context

Sandbox 002 originally described the next implementation step as a five-smell fixture stage followed by a later RAG ingestion stage. That created an artificial split: in this corpus, ingestion is itself the first discovery pass.

Parser adapters, structure-aware segmentation, citation/reference extraction, graph edges, and parse diagnostics reveal which Kentucky homeowners sources are usable, which candidate five-smell evidence appears in the corpus, and where the machinery is uncertain.

The project still must avoid premature infrastructure. Choosing Qdrant, Postgres plus pgvector, Chroma, a graph database, a chatbot, or a production service before the evidence model is stable would turn a proof-of-concept question into an infrastructure question.

## Decision

The next active Sandbox 002 implementation path is a deterministic, JSONL-first **discovery-and-instrumentation** stage.

This stage will emit source-traceable legal evidence records, parser/reference diagnostics, conservative graph edges, future-compatible retrieval bundles, and candidate evidence for the five active Kentucky homeowners policy-layer smells.

The fixture is no longer a purely manual first step. Five-smell fixture examples should be curated from discovery-and-instrumentation outputs, supplemented by clearly marked synthetic seeds only when needed.

The guiding principle is:

> Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist, and treat parser/reference uncertainty as part of the evidence layer.

## Consequences

Positive:

- keeps the first implementation local, deterministic, and inspectable
- lets ingestion discover real candidate evidence instead of relying on manual fixture guesses
- makes parser quality, table failures, reading-order uncertainty, and partial reference normalization visible from day one
- preserves a future path for lexical, semantic, graph, citation, and metadata retrieval without selecting a vector store now
- separates candidate evidence from final legal findings

Tradeoffs:

- Stage 002 is slightly more structured than a manual fixture-only pass
- the first implementation must define more output contracts up front
- lexical candidate scans remain a baseline and will under-recall paraphrased or distributed smells until later retrieval evaluation

## Required First-Stage Outputs

The first discovery-and-instrumentation stage should produce, at minimum:

- `schema/` JSON Schemas for every JSON/JSONL artifact type
- `data/heuristics.md`
- `output/run_manifest.json`
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

Every JSON/JSONL artifact should carry `schema_version`, `run_id`, and `created_at`. Source IDs and node IDs should be stable under a fixed parsing strategy; parser or segmentation changes that break ID stability require a version bump and migration note.

## Boundaries

The discovery-and-instrumentation layer may emit candidate evidence such as:

- generic legal-reference language with no nearby Kentucky citation
- valuation or timing terms with no nearby formula, schedule, date, or cross-reference
- unversioned current-guideline or current-manual references
- explicit endorsement, amendment, override, citation, or reference signals
- parser failures or uncertainty that reduce reviewer trust

It must not emit final legal conclusions or claim that a policy is unlawful. Downstream detector and reviewer-report layers own findings, smell classification, severity, ROI mapping, reviewer questions, and human-review status.

## Rejected Alternatives

- Keep Stage 002 as a purely manual fixture stage.
- Move directly to a vector database or full RAG framework.
- Treat Docling output as parser truth without instrumentation.
- Treat all references as legal citations.
- Treat lexical discovery as sufficient for the harder smells.
- Add schema fields or edge types without downstream consumers.
- Write manual reviewer annotations back into the Stage 002 substrate.
- Use LLM output to mutate standard Stage 002 artifacts.

## Follow-Up

- Update Sandbox 002 README, roadmap, RAG plan, phase plan, handoff, and cross-agent startup docs to make this path canonical.
- Keep `ADR-002` in force: semantic retrieval is expected, but vector store selection remains deferred until evidence records and retrieval evaluation justify it.
