# Legal RAG Subsystem Plan

Status: Active planning document
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Related skill: `skills/legal-rag-builder/SKILL.md`

## Purpose

Build a local-first legal RAG subsystem that can ingest the Kentucky homeowners corpus, preserve legal structure and provenance, extract citations and graph relationships, and return evidence bundles for later smell analysis.

This is not a chatbot, detector engine, or production storage service. It is the evidence substrate that downstream detectors and reviewer reports will consume.

## Design Center

The first useful RAG result is not a vector hit. It is a source-traceable evidence bundle:

- source metadata
- legal node text
- section or page location where available
- parent context
- adjacent nodes
- citations and unresolved references
- graph edges
- why the node was retrieved

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

### 2. Parser Layer

Converts source files into structured blocks.

Initial tools:

- Docling for supported PDF/document conversion when useful
- simple HTML/text fallback using local Python libraries
- no OCR by default unless a selected source requires it

### 3. Normalizer

Converts parser output into project-owned records instead of leaking parser-specific objects through the system.

Core records:

- `Source`
- `Document`
- `Block`
- `Node`
- `Citation`
- `Reference`
- `Edge`
- `RetrievalBundle`

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

Extracts formal and domain-specific references.

Initial custom extractors:

- Kentucky statutes: `KRS xxx.xxx-xxx`
- Kentucky regulations: `806 KAR xx:xxx`
- DOI bulletins and advisory opinions
- SERFF tracking numbers
- form IDs
- endorsement IDs
- policy manual identifiers

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

### 7. Retrieval Index

Phase 1 retrieval starts with exact phrase, lexical scoring, and graph expansion over local files.

Likely progression:

1. JSONL records and simple exact/lexical search
2. optional SQLite FTS5 if local lexical search becomes awkward
3. embeddings over nodes after a gold set proves semantic retrieval is needed
4. Qdrant or Postgres plus pgvector only after the vector experiment has a clear question

### 8. Bundle Composer

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

Create a file-backed ingestion and retrieval slice under:

```text
sandboxes/002-claims-regulatory-automation/stages/003-homeowners-rag-ingestion/
```

This stage should prove that real corpus documents can become source-traceable nodes, citations, edges, and retrieval bundles before any vector store is selected.
