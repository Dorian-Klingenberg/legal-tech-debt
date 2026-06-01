# Lesson: RAG Is The Evidence Substrate, Not The Finding Layer

## Problem

It is easy to let a legal RAG plan drift into either a vector-store decision or a detector/reporting design.

Both are premature if the system has not first proven a stable legal evidence substrate.

## Key Lesson

The Legal RAG Builder should first answer:

> Can the corpus become source-traceable legal nodes, citations, references, typed edges, and retrieval bundles?

It should not first answer:

- Which vector database should we use?
- Which smell findings should we emit?
- What UI should reviewers see?

Those questions matter later, but only after the substrate exists.

## Boundary

The RAG layer owns:

- `Source`
- `Document`
- `Block`
- `Node`
- `Citation`
- `Reference`
- `Edge`
- `RetrievalBundle`
- parse warnings

The downstream detector/reporting layer owns:

- findings
- smell classification
- severity
- ROI mapping
- reviewer questions
- human-review status

## Reuse From Sandbox 001

Sandbox 001 already proved the useful representation style:

- graph nodes
- references
- unresolved targets
- adjacency and closure outputs
- dependency roots
- typed-edge thinking
- JSON/CSV/Markdown evidence outputs

Carry that style forward. Do not carry forward the auto/no-fault synthetic domain content as active Sandbox 002 scope.

## Semantic Retrieval

Semantic retrieval is still expected.

It should be added after:

1. the node model is stable
2. exact/lexical/graph retrieval has a baseline
3. a tiny gold set shows where semantic retrieval helps

This keeps vector search attached to legal structure and provenance instead of returning orphan chunks.

## Practical Rule

Before adding a retrieval store, ask:

> What measured retrieval failure does this store solve?

If the answer is not clear, stay file-backed or embedded-local for the current stage.

