# 2026-06-02 Docling Local Stack Verification

## Session Summary

Verified the local parsing and model environment for Sandbox 002 RAG planning, then documented the boundary for future agents.

## What We Checked

- Project skill docs: `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`
- RAG skill and ADRs under `skills/legal-rag-builder/`
- Grannies-derived memory reference at `skills/project-memory-artifacts/references/grannies-memory-patterns.md`
- Source Grannies project at `D:\Repos\Games\TheGame\projects\grannys-house-trials`
- Local Python package environment
- Local executable availability for Ollama, LM Studio CLI, and vLLM
- Hugging Face cache for Docling model artifacts

## Findings

The Grannies carry-forward in this repo is a memory and handoff pattern, not an inherited RAG or vector database stack.

The local environment has Docling and related local document model packages installed:

- `docling` 2.93.0
- `docling-core` 2.74.1
- `docling-slim` 2.93.0
- `docling-parse` 5.10.1
- `docling-ibm-models` 3.13.2
- `transformers` 5.8.0
- `torch` 2.11.0

The local environment did not show a verified general local LLM runtime or vector database stack for this repo:

- no `ollama` on `PATH`
- no `lmstudio` or `lms` on `PATH`
- no `vllm` on `PATH`
- no `qdrant-client`, `chromadb`, `faiss-cpu`, `sentence-transformers`, or `llama-index-core` Python packages detected

## Documentation Updated

- Added `skills/legal-rag-builder/references/docling-local-stack-boundary.md`
- Updated `skills/legal-rag-builder/SKILL.md`
- Updated `BOOTSTRAP.md`
- Updated `AGENTS.md`
- Updated `CLAUDE.md`
- Updated `.github/copilot-instructions.md`
- Updated `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- Updated `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`

## Current Rule

Use Docling as a parser or optional document enrichment adapter. Do not treat Docling, cached Docling model artifacts, or VLM parsing as a legal RAG store, vector database, or verified general local LLM runtime.

## Next Useful Work

When Stage 003 begins, run a tiny Docling parse against one selected corpus file and normalize its output into project-owned `Source`, `Block`, `Node`, `Citation`, and `Edge` records before adding embeddings or any retrieval store.
