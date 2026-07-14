# Docling Local Stack And Boundary

Date verified: 2026-06-02
Scope: Sandbox 002 Legal RAG Builder

## Purpose

This note records what was verified locally about Docling, local model support, and retrieval tooling so future agents do not confuse parser capability with RAG storage or legal reasoning.

## Verified Local Environment

The current Windows Python environment at verification time had:

- Python 3.12.10
- `docling` 2.93.0
- `docling-core` 2.74.1
- `docling-slim` 2.93.0
- `docling-parse` 5.10.1
- `docling-ibm-models` 3.13.2
- `transformers` 5.8.0
- `torch` 2.11.0
- `scipy` 1.17.1
- `numpy` 2.4.4
- `langchain` 1.2.17
- `langchain-openai` 1.2.1

Docling CLI was available and reported support for:

- standard parsing pipeline
- VLM parsing pipeline
- OCR controls
- table extraction controls
- optional enrichment flags for code, formula, picture classification, picture description, and chart data
- local or remote model options, with remote services disabled by default unless explicitly enabled

Hugging Face cache contained Docling model artifacts:

- `models--docling-project--CodeFormulaV2`
- `models--docling-project--docling-layout-heron`
- `models--docling-project--docling-models`
- `models--docling-project--DocumentFigureClassifier-v2.5`

This means the local environment is prepared for Docling-based parsing and some Docling model-backed document understanding. It does not mean the project has a general local chat LLM workflow.

## Not Detected Locally

At verification time, these were not detected:

- `ollama` on `PATH`
- `lmstudio` or `lms` on `PATH`
- `vllm` on `PATH`
- `qdrant-client` Python package
- `chromadb` Python package
- `faiss-cpu` Python package
- `sentence-transformers` Python package
- `llama-index-core` Python package

Do not assume a local general-purpose LLM runtime or a vector database exists unless a later stage verifies and documents it.

## Grannies House Carry-Forward

The Grannies project was found at:

```text
D:\Repos\Games\TheGame\projects\grannys-house-trials
```

The Legal Tech Debt repo currently carries forward the Grannies-style memory pattern through:

```text
skills/project-memory-artifacts/references/grannies-memory-patterns.md
```

That carry-forward is about shared project memory, handoffs, journals, lessons, and machine-readable agent context. It is not evidence that this repo inherited a vector database, RAG stack, or installed local LLM runtime from Grannies.

The Grannies docs mention possible future local SLM operation through Ollama or llama.cpp, but that is a portability note in the source project, not a verified installed dependency for Legal Tech Debt.

## Architectural Boundary

Use Docling as a parser or document enrichment adapter:

```text
raw corpus file
  -> Docling conversion or extraction
  -> parser run / block stats / table failures / parse warnings
  -> project-owned normalizer
  -> Source / Document / Block / Node / Citation / Reference / Edge / CandidateEvidence
  -> exact, lexical, metadata, graph-expanded retrieval
  -> optional later semantic retrieval
  -> RetrievalBundle
```

Docling may provide:

- converted text
- Markdown, JSON, YAML, HTML, text, or DocTags exports
- page/layout/table information
- OCR output
- chunk metadata
- optional VLM/enrichment hints

Docling does not own:

- Kentucky-specific source metadata
- corpus manifest mapping
- KRS/KAR citation normalization
- policy form, endorsement, SERFF, or DOI bulletin resolution
- typed legal graph edges
- sparse matrices or lexical indexes
- vector storage
- retrieval bundle composition
- legal smell findings
- human reviewer state

Docling output should be treated as parser evidence, not parser truth. Discovery-and-instrumentation stages should record parser provenance, parse warnings, reading-order uncertainty, and table failures instead of hiding them behind normalized nodes.

## Retrieval Implication

The first discovery/RAG stage should stay file-backed, structural, and instrumented. Use Docling only if it improves extraction for the selected source subset, and expose Docling-specific uncertainty in the output records.

If semantic retrieval becomes necessary, verify the embedding library and storage choice in the stage that introduces it. Do not infer that Docling's VLM features or cached model artifacts are a vector database.

## Verification Commands

Useful checks for future agents:

```powershell
python --version
python -m pip show docling docling-core docling-slim docling-parse docling-ibm-models transformers torch scipy numpy
python -m pip show qdrant-client chromadb faiss-cpu sentence-transformers llama-index-core 2>$null
Get-Command ollama,lmstudio,lms,vllm -ErrorAction SilentlyContinue
docling --help
Get-ChildItem -LiteralPath $env:USERPROFILE\.cache\huggingface\hub -Directory -ErrorAction SilentlyContinue
```
