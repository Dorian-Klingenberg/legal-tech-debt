---
name: legal-rag-builder
description: Build or modify the Legal Tech Debt local-first legal RAG ingestion and retrieval workflow for Sandbox 002. Use when working on legal document ingestion, parsing, normalization, structure-aware chunking, Kentucky citation extraction, graph-linked nodes, retrieval bundles, or RAG evaluation for the Kentucky homeowners corpus.
---

# Legal RAG Builder

## Startup

1. Read `BOOTSTRAP.md`.
2. Read `skills/SKILL-DEVELOPMENT.md`.
3. Read `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`.
4. Read `sandboxes/002-claims-regulatory-automation/002-RAG-SUBSYSTEM-PLAN.md` and `sandboxes/002-claims-regulatory-automation/002-RAG-PHASE-PLAN.md`.
5. Read the RAG ADRs in `skills/legal-rag-builder/adr/`.
6. Read `skills/legal-rag-builder/references/rag-substrate-boundary-lesson.md` when clarifying RAG layer boundaries, findings, or vector-store sequencing.
7. Read `skills/legal-rag-builder/references/docling-local-stack-boundary.md` when working on Docling, local parsing models, VLM enrichment, embeddings, or retrieval-store assumptions.
8. Read `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`.
9. Inspect `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` and `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before assuming more source collection is needed.

## Workflow

1. Confirm the task maps to Kentucky homeowners insurance and the five Sandbox 002 policy-layer smells.
2. Prefer the next smallest file-backed proof-of-concept stage before adding storage, services, APIs, or UI.
3. Preserve original source text and provenance before normalizing or segmenting.
4. Segment by legal structure first: headings, sections, subsections, clauses, definitions, list items, tables, endorsements, and citations.
5. Extract citations and domain references into explicit records.
6. Create graph edges for containment, order, citations, references, definitions, amendments, and overrides where detectable.
7. Return retrieval bundles with source metadata, why-retrieved reasons, parent context, adjacent nodes, and citations.
8. Keep findings, smell classifications, severity, ROI mapping, and reviewer decisions in downstream detector/reporting layers, not in the core RAG substrate.
9. Validate with a tiny gold set before broadening the corpus or introducing infrastructure.

## Guardrails

- Do not start with a chatbot or polished UI.
- Do not use naive fixed-window chunking as the primary strategy.
- Do not rely on pure vector search alone.
- Do not collapse ingestion, retrieval, and legal reasoning into one opaque prompt.
- Do not add Qdrant, Postgres, pgvector, services, or APIs unless a stage explicitly earns that choice.
- Do not drop semantic/vector retrieval; defer vector storage until the legal node model and retrieval evaluation justify it.
- Do not treat Docling, Docling VLM enrichment, or cached Docling model artifacts as a general local LLM or vector database.
- Do not chase manual SERFF gaps unless the active experiment needs missing evidence documented in `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`.
- Do not frame automated retrieval or findings as legal advice.

## First Implementation Bias

For the first RAG stage, prefer:

- plain local Python
- explicit config
- `JSONL`, `JSON`, `CSV`, and Markdown outputs
- exact phrase and lexical retrieval before embeddings
- graph expansion through local edge files
- small tests against real corpus excerpts

## Output Expectations

When finishing work, report:

- what source documents or manifest rows were used
- what nodes, citations, edges, or retrieval bundles were produced
- what validation passed
- what remains a known gap or open decision


