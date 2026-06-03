# Roadmap: Sandbox 002 Kentucky Homeowners Policy-Layer Smells

Version: 4.0
Status: Active roadmap
Controlling scope: `002-five-policy-layer-phish.md`
Path decision: `../../skills/legal-rag-builder/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
Artifact contract: `../../skills/legal-rag-builder/adr/ADR-004-schema-run-identity-and-id-stability.md`

## Current Scope

Sandbox 002 is focused on Kentucky homeowners insurance and the five policy-layer smells documented in `002-five-policy-layer-phish.md`.

The active smells are:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

Do not pursue personal auto, motor vehicle, no-fault, PIP, broad claims platforms, live regulatory feeds, PAS integration, or production infrastructure unless the user explicitly reopens that scope.

## Stage 001: Foundation Import

Status: Complete bridge stage
Location: `stages/001-foundation-import`

Purpose:

- import the useful Sandbox 001 probe shape
- confirm it runs against a tiny homeowners-oriented fixture
- preserve the fast local workflow for later stages

What it proves:

- plain Python is enough for the current sandbox style
- Markdown fixtures and JSON/Markdown/CSV outputs are reviewable
- section/reference extraction remains useful as a supporting primitive

What it does not prove:

- it does not implement the five active homeowners smells
- it does not validate real Kentucky filings
- it does not justify infrastructure

## Stage 002: Homeowners Discovery And Instrumentation

Status: Next recommended stage
Suggested location: `stages/002-homeowners-discovery-instrumentation`

Objective:

Build a deterministic, JSONL-first discovery-and-instrumentation pipeline over a tiny Kentucky homeowners corpus subset.

This stage is the first discovery pass. It should turn selected real corpus sources into source-traceable legal evidence records, parser diagnostics, conservative graph edges, future-compatible retrieval bundles, and candidate evidence for the five active smells.

The fixture is curated from these outputs. It is not a separate manual-first stage.

Inputs:

- selected Kentucky homeowners source excerpts from `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- known source gaps from `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`
- one or two documents per useful source type where practical
- source metadata with access dates, URLs, filing metadata, and effective dates where available

Deliverables:

- `STAGE.md` documenting scope and limitations
- `LESSON.md` documenting what discovery and instrumentation taught
- `schema/` JSON Schemas for every JSON/JSONL artifact type
- `data/source_manifest_subset.csv`
- `data/heuristics.md`
- `output/run_manifest.json`
- `output/sources.jsonl`
- `output/parser_runs.jsonl`
- `output/blocks.jsonl`
- `output/block_stats.jsonl`
- `output/nodes.jsonl`
- `output/citations.jsonl`
- `output/references.jsonl`
- `output/edges.jsonl`
- `output/table_failures.jsonl`
- `output/parse_warnings.jsonl`
- `output/candidate_evidence.jsonl`
- `output/retrieval_bundles.json`
- `output/discovery_report.md`
- curated fixture excerpts or clearly marked synthetic seeds only where the discovery pass cannot support a smell example directly
- lightweight ROI notes for candidate evidence, using `002-ROI-CASES-FIVE-SMELLS.md`

Success criteria:

- every JSON/JSONL artifact carries schema version, run identity, and creation timestamp
- IDs are stable under a fixed parsing strategy, with version bumps and migration notes for strategy changes that break ID stability
- selected real corpus files become source-traceable blocks, nodes, references, citations, graph edges, and parser diagnostics
- parser uncertainty is visible through parser runs, block stats, table failures, and parse warnings
- citations and broader references are separated
- graph edges are conservative and auditable
- retrieval bundles are shaped for future lexical, semantic, metadata, graph, and citation signals even though the first implementation is file-backed and lexical-first
- candidate evidence exists for each active smell, or the stage explains why the selected corpus slice did not support one
- candidate evidence identifies the relevant cost pool and reviewer question without presenting legal conclusions
- transparent heuristic rules are documented in `data/heuristics.md`
- no auto/no-fault/PIP material is included except as explicitly noted homeowners context
- manual SERFF gaps are not chased unless candidate evidence or reviewer questions require missing current-state carrier evidence
- the stage remains runnable and understandable on a laptop
- the stage targets 5-10 unique source files; expansion beyond that requires a stage note

Non-goals:

- no database
- no vector store
- no chatbot
- no production service
- no final legal findings
- no LLM boundary adjudication by default
- no cross-document topic modeling or cluster-level graph edges
- no manual reviewer annotations written back into the Stage 002 substrate

## Stage 003: Retrieval Baseline And Fixture Curation

Status: Planned

Objective:

Use Stage 002 evidence records to curate five-smell fixture examples and evaluate exact, lexical, graph-expanded, citation/reference, and metadata retrieval baselines.

Controlling documents:

- `002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- `002-RAG-SUBSYSTEM-PLAN.md`
- `002-RAG-PHASE-PLAN.md`
- `../../skills/legal-rag-builder/adr/ADR-001-rag-substrate-reuses-001-structure.md`
- `../../skills/legal-rag-builder/adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md`
- `../../skills/legal-rag-builder/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
- `../../skills/legal-rag-builder/adr/ADR-004-schema-run-identity-and-id-stability.md`

Expected outputs:

- curated five-smell fixture excerpts
- tiny retrieval gold set under `data/goldsets/`, created from Stage 002 outputs and real snippets only
- lexical and graph-expanded retrieval comparison report
- updated `retrieval_bundles.json`
- notes on exact/lexical/graph failures that semantic retrieval should address

Success criteria:

- every active smell has a source-traceable candidate fixture example or a documented source limitation
- retrieval bundles include why-retrieved reasons, parent context, adjacent nodes, citations, references, and parser uncertainty where relevant
- exact and lexical baselines are measured before embeddings
- semantic retrieval remains designed for, but no vector store is selected
- findings are not stored in the RAG substrate; they remain downstream detector outputs

## Stage 004: Deterministic Pattern Detectors

Status: Planned

Objective:

Adapt Stage 002/003 candidate evidence and retrieval bundles into lightweight detectors for the five active smells.

Detector approach:

- regex and phrase lists for known trigger language
- simple section and endorsement indexing
- simple reference/citation checks
- small clause relationship graph where it helps coverage inversion
- no heavy NLP unless a detector cannot be made useful without it

Expected outputs:

- `output/findings.json`
- `output/report.md`
- `output/section_index.csv`
- optional matrix outputs only when they explain a smell

Success criteria:

- the probe promotes at least one candidate evidence item or curated fixture example for each active smell
- findings include location, smell type, evidence text, cost pool, why it matters, and reviewer questions
- false-positive limitations are explicit
- the code stays small enough for future agents to read quickly

## Stage 005: Reviewer Report

Status: Planned

Objective:

Turn detector output into a practical review artifact for a policy, claims, compliance, or product reviewer.

Deliverables:

- smell-by-smell summary
- source traceability
- concise reviewer questions
- explicit non-legal-advice limitation
- list of missing sources or human-review blockers

Success criteria:

- a reviewer can understand why each finding was flagged without reading the code
- the report distinguishes detected text risk from legal conclusions
- the report makes clear which findings need human review

## Stage 006: Optional Semantic Retrieval Experiment

Status: Parked until retrieval evaluation earns it

Objective:

Evaluate whether embeddings improve recall for homeowners policy-layer smell research beyond exact, lexical, and graph-expanded retrieval.

Allowed if earned:

- local embeddings attached to RAG nodes
- small gold-set comparison
- Qdrant or Postgres plus pgvector experiment only after the evaluation question is explicit

Success criteria:

- semantic retrieval improves gold-set recall or reviewer usefulness
- semantic hits still return source provenance and graph-expanded context
- vector storage choice is documented in a follow-up ADR before implementation

## Stage 007: Optional Visual Drill-Down

Status: Parked until the report earns it

Objective:

Create a static, local visual drill-down only if Stage 005 shows that a visual surface would make the findings easier to review.

Allowed if earned:

- static HTML generated from local outputs
- simple tables and links from findings to source excerpts
- no server, database, scheduled job, or product shell

## Parked Work

These ideas may be useful later, but they are not part of active Sandbox 002 work:

- live statute or regulatory feed ingestion
- Neo4j or other graph database
- Docker or deployment packaging
- PAS or claim system integration
- broad claim decision audit trails
- multi-carrier pilots
- production citation validation
- LLM extraction pipelines
- go-to-market platform planning

## Decision Gate

Before adding any new tool, stage, or detector, ask:

> Does this directly help evaluate one of the five Kentucky homeowners policy-layer smells?

If the answer is no, leave it parked.

