---
name: legal-rag-builder
description: Build or modify the Legal Tech Debt local-first legal discovery, instrumentation, and retrieval workflow for Sandbox 002. Use when working on legal document ingestion, parser diagnostics, normalization, structure-aware chunking, Kentucky citation/reference extraction, graph-linked nodes, candidate evidence, retrieval bundles, or RAG evaluation for the Kentucky homeowners corpus.
---

# Legal RAG Builder

## Startup

1. Read `BOOTSTRAP.md`.
2. Read `skills/SKILL-DEVELOPMENT.md`.
3. Read `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`.
4. Read `sandboxes/002-claims-regulatory-automation/002-RAG-SUBSYSTEM-PLAN.md` and `sandboxes/002-claims-regulatory-automation/002-RAG-PHASE-PLAN.md`.
5. Read the RAG ADRs in `skills/legal-rag-builder/adr/`.
   - `ADR-003-discovery-instrumentation-before-fixture-detectors.md` controls the current Sandbox 002 path.
   - `ADR-004-schema-run-identity-and-id-stability.md` controls Stage 002 schema, run identity, and stable-ID requirements.
6. Read `skills/legal-rag-builder/references/rag-substrate-boundary-lesson.md` when clarifying RAG layer boundaries, findings, or vector-store sequencing.
7. Read `skills/legal-rag-builder/references/docling-local-stack-boundary.md` when working on Docling, local parsing models, VLM enrichment, embeddings, or retrieval-store assumptions.
8. Read `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`.
9. Inspect `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` and `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before assuming more source collection is needed.

## Workflow

1. Confirm the task maps to Kentucky homeowners insurance and the five Sandbox 002 policy-layer smells.
2. Prefer the next smallest file-backed discovery-and-instrumentation stage before adding storage, services, APIs, or UI.
3. Preserve original source text and provenance before normalizing or segmenting.
4. Treat parser output as evidence that needs instrumentation, not as parser truth: emit parser runs, block stats, table failures, parse warnings, and reading-order uncertainty where available.
5. Include schema version, run identity, creation timestamp, and stable source/node IDs in JSON/JSONL records.
6. Segment by legal structure first: headings, sections, subsections, clauses, definitions, list items, tables, endorsements, and citations.
7. Extract formal citations and broader domain references into separate explicit records.
8. Create graph edges for containment, order, citations, references, definitions, amendments, and overrides where detectable.
9. Emit candidate evidence for the five active smells with source, node, why-flagged reason, heuristic rule ID/version, parser/reference confidence, cost pool, and reviewer question.
10. Return retrieval bundles with source metadata, why-retrieved reasons, parent context, adjacent nodes, citations, references, parser diagnostics, and future-compatible retrieval signal slots.
11. Keep final findings, smell classifications, severity, ROI mapping, and reviewer decisions in downstream detector/reporting layers, not in the core discovery/RAG substrate.
12. Validate with a tiny gold set before broadening the corpus or introducing infrastructure.

## Guardrails

- Do not start with a chatbot or polished UI.
- Do not use naive fixed-window chunking as the primary strategy.
- Do not rely on pure vector search alone.
- Do not collapse ingestion, retrieval, and legal reasoning into one opaque prompt.
- Do not add Qdrant, Postgres, pgvector, services, or APIs unless a stage explicitly earns that choice.
- Do not drop semantic/vector retrieval; defer vector storage until the legal node model and retrieval evaluation justify it.
- Do not treat Docling, Docling VLM enrichment, or cached Docling model artifacts as a general local LLM or vector database.
- Do not treat Docling output as parser truth without diagnostics.
- Do not treat all references as citations.
- Do not treat lexical candidate scans as sufficient discovery for the harder smells.
- Do not add schema fields or edge types without an identified downstream consumer or parser-uncertainty instrumentation need.
- Do not write manual reviewer annotations back into the Stage 002 substrate.
- Do not create cross-document topic-modeling or cluster-level graph edges in Stage 002.
- Do not use LLMs in the main Stage 002 pipeline; any one-off LLM helper output must be isolated in a non-standard artifact and must not mutate standard outputs.
- Do not chase manual SERFF gaps unless the active experiment needs missing evidence documented in `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`.
- Do not frame automated retrieval or findings as legal advice.

## First Implementation Bias

For the first RAG stage, prefer:

- plain local Python
- explicit config
- `JSONL`, `JSON`, `CSV`, and Markdown outputs
- UTF-8 JSONL with one JSON object per line
- JSON Schemas for every JSON/JSONL artifact type
- `output/run_manifest.json`
- `data/heuristics.md`
- exact phrase and lexical retrieval before embeddings
- graph expansion through local edge files
- small tests against real corpus excerpts
- parser/reference uncertainty as first-class output
- candidate evidence before final findings

## Output Expectations

When finishing work, report:

- what source documents or manifest rows were used
- what schema versions, run manifest, parser runs, nodes, citations, references, edges, candidate evidence, or retrieval bundles were produced
- what validation passed
- what remains a known gap or open decision


