# 2026-06-02 Docling/RAG Architecture Pause

## Session Summary

This session clarified how Docling fits into the Sandbox 002 legal RAG plan and closed the loop on whether the Grannies House Trials patterns conflict with the newer Legal Tech Debt framework.

The conclusion: Docling is useful as a local parser and document enrichment adapter, while Grannies contributes shared-memory discipline. Neither should become the legal RAG storage model, vector database, or legal reasoning layer.

## What We Learned

Docling can run locally in the current environment and has local document AI/model artifacts available. It can parse PDFs and other document formats, extract or preserve layout, tables, OCR output, and optional enrichment hints.

Docling is not a general-purpose local LLM workflow. No verified Ollama, LM Studio CLI, vLLM, Qdrant, Chroma, FAISS, sentence-transformers, or LlamaIndex install was found for this repo during the check.

The Grannies House Trials carry-forward is compatible with the Legal Tech Debt framework when treated as a memory and handoff pattern:

- canonical human-readable docs
- compact agent context ideas
- handoffs as point-in-time snapshots
- journals for session history
- lessons for reusable understanding
- startup instructions that force agents to read project truth before acting

The Grannies runtime and simulation model do not carry over directly. They should not be treated as a RAG implementation precedent.

## Decisions Preserved

- Keep the RAG substrate project-owned: `Source`, `Document`, `Block`, `Node`, `Citation`, `Reference`, `Edge`, and `RetrievalBundle`.
- Use Docling only before normalization, as a parser or optional enrichment adapter.
- Keep exact, lexical, metadata, and graph-expanded retrieval before embeddings.
- Treat semantic/vector retrieval as expected later work, but require a tiny gold-set failure mode before choosing a vector store.
- Do not assume a local general LLM runtime exists just because Docling has local document models.
- Keep Grannies-derived memory patterns, but do not import Grannies implementation assumptions.

## Documentation Updated

Added:

- `skills/legal-rag-builder/references/docling-local-stack-boundary.md`
- `journal/2026-06-02-docling-local-stack-verification.md`

Updated:

- `BOOTSTRAP.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `skills/README.md`
- `skills/legal-rag-builder/SKILL.md`
- `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`

## Validation Performed

- Confirmed Python package versions for Docling and supporting model libraries.
- Confirmed absence of common vector database and local LLM runtime packages/commands in the current environment.
- Confirmed Docling CLI availability and option surface.
- Located the source Grannies project under `D:\Repos\Games\TheGame\projects\grannys-house-trials`.
- Searched the Legal Tech Debt repo for Docling, vector, LLM, and Grannies references.
- Confirmed new cross-agent references are discoverable from startup and skill docs.

## Current State

The repository now has explicit cross-agent guidance that:

```text
Docling/parser output
  -> project-owned normalizer
  -> legal RAG substrate
  -> retrieval bundles
  -> downstream smell detectors/reviewer layer
```

No production infrastructure, vector database, or new runtime dependency was added.

## Next Useful Work

Resume with Sandbox 002 Stage 002 unless the user explicitly redirects:

```text
sandboxes/002-claims-regulatory-automation/stages/002-homeowners-policy-layer-smells/
```

Build a small source-traceable fixture with at least one Kentucky homeowners example for each of the five active policy-layer smells. Stop before detector infrastructure.

After that, Stage 003 can run a tiny Docling parse against one selected corpus file and normalize it into project-owned records before embeddings or any retrieval store are considered.

## Open Notes

- `SECRET_SCAN_REPORT.md` still asks the repo owner to review and classify scanner findings, mostly from archived third-party captures under `sources/`.
- No machine-readable Legal Tech Debt `AGENT_CONTEXT` file exists yet. If future agents need one, create it deliberately as a separate memory artifact rather than smuggling context into private assistant memory.

