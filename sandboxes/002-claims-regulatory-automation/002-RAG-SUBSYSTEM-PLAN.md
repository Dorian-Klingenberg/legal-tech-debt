# Legal RAG Subsystem Plan

Status: Active planning document
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Updated: 2026-06-03
Related skill: `skills/legal-rag-builder/SKILL.md`
Path decision: `adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
Artifact contract: `adr/ADR-004-schema-run-identity-and-id-stability.md`

## Purpose

Build a local-first discovery, instrumentation, and retrieval evidence substrate that can ingest selected Kentucky homeowners corpus files, preserve legal structure and provenance, expose parser/reference uncertainty, extract citations and broader references, create conservative graph relationships, surface candidate evidence, and return evidence bundles for later smell analysis.

This is not a chatbot, detector engine, or production storage service. It is the evidence substrate that downstream detectors and reviewer reports will consume.

## Design Center

The first useful result is not a vector hit. It is a source-traceable evidence bundle plus visible machinery confidence:

- schema version and run identity
- source metadata
- parser run provenance
- parser quality signals
- legal node text
- section or page location where available
- parent context
- adjacent nodes
- citations and unresolved references
- broader references and partial normalizations
- graph edges
- why the node was retrieved
- parser or reference uncertainty that affects trust

Semantic retrieval remains expected later, but it must attach to this legal-structure model instead of replacing it.

## What Already Exists

| Existing Asset | Location | Reuse |
|---|---|---|
| Sandbox 001 probe model | `sandboxes/001-legal-debt-primitives/stages/004-typed-edge-study/src/legal_debt_probe.py` | Proven local data structures and graph/matrix outputs. |
| Matrix direction and root notes | `sandboxes/001-legal-debt-primitives/MATRIX_NOTES.md` | Keep dependency direction and missing-node representation. |
| Typed edge study | `sandboxes/001-legal-debt-primitives/stages/004-typed-edge-study/study/` | Reuse the lesson that a reference is not yet a relationship. |
| Real corpus | `corpus/kentucky-homeowners-policy-smells/` | Current source base for ingestion. |
| RAG engineering spec | `002-RAG-INGESTION-RETRIEVAL-SPEC.md` | Source-of-truth technical contract. |
| Legal RAG skill | `skills/legal-rag-builder/SKILL.md` | Agent workflow guide. |

## Core Components

### 1. Source Registry

Reads corpus manifest rows and emits stable `Source` records.

Responsibilities:

- source ID
- title
- source type
- smell mapping
- URL
- downloaded path
- hash
- dates and carrier metadata where available
- parse warnings

Source IDs should be stable across runs as long as document identity does not change.

### 2. Parser Layer

Converts source files into structured blocks.

Initial tools:

- Docling for supported PDF/document conversion when useful
- simple HTML/text fallback using local Python libraries
- no OCR by default unless a selected source requires it

Parser output is not parser truth. Every parser adapter should emit parser-run metadata, block stats, table failures, parse warnings, and reading-order uncertainty where available.

### 3. Normalizer

Converts parser output into project-owned records instead of leaking parser-specific objects through the system.

Core records:

- `Source`
- `Document`
- `Block`
- `ParserRun`
- `BlockStats`
- `Node`
- `Citation`
- `Reference`
- `Edge`
- `TableFailure`
- `ParseWarning`
- `CandidateEvidence`
- `RetrievalBundle`

All JSON/JSONL records should carry `schema_version`, `run_id`, and `created_at`. Node IDs should be deterministic under a fixed parsing strategy. Parser or segmentation changes that break ID stability require a version bump and migration note.

### 4. Structure-First Segmenter

Creates legal nodes from structure before token windows.

Primary node boundaries:

- document
- section
- subsection
- clause
- list item
- definition
- table
- endorsement
- citation or authority reference

### 5. Citation And Reference Extractor

Extracts formal citations and broader domain-specific references into separate records.

Initial custom extractors:

- Kentucky statutes: `KRS xxx.xxx-xxx`
- Kentucky regulations: `806 KAR xx:xxx`
- DOI bulletins and advisory opinions
- SERFF tracking numbers
- form IDs
- endorsement IDs
- policy manual identifiers
- generic law references
- current-guideline and current-manual references

Eyecite remains a candidate for formal legal citation coverage after the first custom extractor pass.

### 6. Graph Builder

Builds typed graph relationships between nodes.

Initial edge types:

- `contains`
- `next`
- `references`
- `defines_term`
- `uses_defined_term`
- `cites_statute`
- `cites_regulation`
- `cites_bulletin`
- `amends`
- `overrides`
- `same_topic`
- `unresolved_reference`

Do not treat all references as legally equivalent. Where a relationship type cannot be determined, keep it visible with lower confidence.

### 7. Candidate Evidence Scanner

Runs exact and lexical candidate scans for the five active smells over nodes and references.

Responsibilities:

- emit `candidate_evidence.jsonl`
- attach source, node, why-flagged reason, parser confidence, reference confidence, machinery confidence, cost pool, and reviewer question
- avoid final legal findings
- document under-recall for paraphrased or distributed smells
- document heuristic rule IDs, versions, purposes, and failure modes in `data/heuristics.md`

### 8. Retrieval Index

Phase 1 retrieval starts with exact phrase, lexical scoring, and graph expansion over local files.

Likely progression:

1. JSONL records and simple exact/lexical search
2. optional SQLite FTS5 if local lexical search becomes awkward
3. embeddings over nodes after a gold set proves semantic retrieval is needed
4. Qdrant or Postgres plus pgvector only after the vector experiment has a clear question

### 9. Bundle Composer

Returns evidence bundles, not orphan chunks.

Every bundle should include:

- query
- filters
- hit node
- source metadata
- section path or page range
- why-retrieved reasons
- parent context
- adjacent nodes
- citations and unresolved references
- parser diagnostics
- broader references and reference confidence
- graph-expanded authority or amendment context when available

## Layer Boundary

The RAG subsystem does not own smell findings.

RAG owns:

- source records
- nodes
- citations
- references
- typed edges
- retrieval bundles
- parser warnings

Downstream detectors own:

- findings
- smell classification
- severity
- ROI mapping
- reviewer questions
- human-review state

## First Build Target

Create a file-backed discovery-and-instrumentation slice under:

```text
sandboxes/002-claims-regulatory-automation/stages/002-homeowners-discovery-instrumentation/
```

This stage should prove that selected real corpus documents can become source-traceable blocks, nodes, citations, references, parser diagnostics, conservative edges, candidate evidence, and retrieval bundles before any vector store is selected.

It should also emit JSON Schemas, `output/run_manifest.json`, and `data/heuristics.md`, and keep the source slice to roughly 5-10 unique source files unless the stage note explains why more are needed.
