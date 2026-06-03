# ADR-001: Reuse Sandbox 001 Structures For The Legal RAG Substrate

Date: 2026-06-01
Status: Accepted
Scope: Legal RAG Builder skill architecture; first applied to Sandbox 002

## Context

Sandbox 002 needs a legal RAG subsystem for the Kentucky homeowners corpus. The early planning conversation considered parser, chunking, vector, and storage components such as Docling, LlamaIndex, Qdrant, and Postgres plus pgvector.

Sandbox 001 already proved a smaller set of data structures and evidence outputs:

- section-like nodes
- references
- matrix nodes
- missing/unresolved targets
- adjacency matrices
- transitive closure
- dependency roots
- JSON, CSV, and Markdown outputs
- typed-edge study materials

The major Sandbox 001 lesson is that a reference is not yet a legal relationship. That lesson is directly relevant to legal RAG because retrieval must return legally meaningful evidence bundles, not disconnected text chunks.

## Decision

The Legal RAG Builder skill will start from the proven Sandbox 001 representation style when guiding RAG substrate work, first adapted for real Kentucky homeowners corpus documents in Sandbox 002.

The first RAG data model should include:

- `Source`
- `Document`
- `Block`
- `Node`
- `Citation`
- `Reference`
- `Edge`
- `RetrievalBundle`

The RAG substrate will not treat domain smell findings as core storage records. Findings belong to downstream detector and reviewer layers.

The first implementation will use file-backed JSONL, JSON, CSV, and Markdown outputs before introducing a database or service.

## Consequences

Positive:

- preserves the proven local proof-of-concept style
- avoids premature store/framework decisions
- keeps provenance and graph relationships first-class
- gives future detectors stable evidence objects to consume
- aligns with the Sandbox 001 closure guidance

Tradeoffs:

- some parser and retrieval code will be project-owned initially
- storage backend decisions are deferred
- downstream detector code must explicitly consume retrieval bundles instead of relying on findings baked into the RAG layer

## Rejected Alternatives

- Start with a vector database as the primary data model.
- Start with LlamaIndex as the dominant abstraction before project-owned records are stable.
- Carry forward Sandbox 001 `Finding` as a core RAG storage type.
- Treat all references as equal graph edges.

## Follow-Up

- Build `stages/002-homeowners-discovery-instrumentation/` under the path decision in `ADR-003-discovery-instrumentation-before-fixture-detectors.md`.
- Keep unresolved references visible as targets.
- Add typed edge fields only where relationship meaning is supported by evidence.
- Update downstream detector plans to consume retrieval bundles rather than raw chunks.
