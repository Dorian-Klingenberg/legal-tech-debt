# Journal - June 1, 2026 - Legal RAG Skill Architecture Closeout

## Summary

This session closed the loop on the `legal-rag-builder` planning work and created a repeatable memory workflow for future agents.

The main architectural correction was:

> The Legal RAG Builder should reuse Sandbox 001's proven graph/data representation style, but it should not confuse RAG storage with downstream smell findings or prematurely choose a vector store.

## What Changed

### 1. Created The Project Memory Artifacts Skill

Added a draft repo-visible skill:

- `skills/project-memory-artifacts/SKILL.md`
- `skills/project-memory-artifacts/agents/openai.yaml`
- `skills/project-memory-artifacts/references/grannies-memory-patterns.md`
- `skills/proposals/project-memory-artifacts.md`

Purpose:

- write shared handoffs
- write journals
- write lessons
- update agent context/bootstrap records
- keep durable memory visible to Codex, GitHub Copilot, Claude Code, and future agents

### 2. Clarified The Legal RAG Architecture

Added planning docs:

- `sandboxes/002-claims-regulatory-automation/002-RAG-SUBSYSTEM-PLAN.md`
- `sandboxes/002-claims-regulatory-automation/002-RAG-PHASE-PLAN.md`

The RAG subsystem is now framed as an evidence substrate:

- source records
- legal nodes
- citations
- references
- typed edges
- retrieval bundles
- parser warnings

Findings, smell classifications, severity, ROI mapping, and reviewer state belong downstream in detector and reporting layers.

### 3. Added Legal RAG Builder ADRs

Added skill-level ADRs under:

```text
skills/legal-rag-builder/adr/
```

ADRs:

- `ADR-001-rag-substrate-reuses-001-structure.md`
- `ADR-002-semantic-vector-retrieval-deferred-not-dropped.md`

These intentionally live under the skill, not the sandbox, because they describe Legal RAG Builder architecture first and Sandbox 002 implementation second.

### 4. Preserved Semantic Retrieval Without Starting There

Semantic/vector retrieval remains expected.

The sequence is now:

1. file-backed sources, nodes, citations, references, and edges
2. exact phrase, lexical, metadata, and graph-expanded retrieval bundles
3. tiny gold-set evaluation
4. semantic retrieval experiment
5. retrieval store decision

Qdrant and Postgres plus pgvector are later candidates, not first-stage commitments.

### 5. Realigned The Roadmap

`002-ROADMAP-revised.md` now uses this order:

1. Stage 001 - Foundation Import
2. Stage 002 - Homeowners Five-Smell Fixture
3. Stage 003 - Homeowners RAG Ingestion
4. Stage 004 - Deterministic Pattern Detectors
5. Stage 005 - Reviewer Report
6. Stage 006 - Optional Semantic Retrieval Experiment
7. Stage 007 - Optional Visual Drill-Down

## Validation

- `skills/legal-rag-builder` validates cleanly with the Codex skill validation script.
- `skills/project-memory-artifacts` validates cleanly with the Codex skill validation script.
- References to the moved ADRs now point to `skills/legal-rag-builder/adr/`.
- The old sandbox-local `adr/` directory was removed.

## Current State

Sandbox 002 remains focused on Kentucky homeowners insurance and the five policy-layer smells.

The next implementation step is still Stage 002 fixture construction:

```text
sandboxes/002-claims-regulatory-automation/stages/002-homeowners-policy-layer-smells/
```

After that, Stage 003 should build the file-backed RAG ingestion slice:

```text
sandboxes/002-claims-regulatory-automation/stages/003-homeowners-rag-ingestion/
```

## Commit Message

Recommended commit message:

```text
Add Legal RAG skill architecture and project memory workflow docs
```

