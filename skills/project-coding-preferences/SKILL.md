---
name: project-coding-preferences
description: Use shared Legal Tech Debt implementation preferences before coding, reviewing, refactoring, handoff planning, or agent-context work in this repository. Triggers when an agent needs to infer project coding style, choose between quick proof-of-concept code and infrastructure, preserve schema/provenance contracts, validate sandbox outputs, or prepare work so Codex, Claude Code, GitHub Copilot, and future agents can continue without private assistant memory.
---

# Project Coding Preferences

## Startup

1. Read `BOOTSTRAP.md`, then `AGENT_CONTEXT.json` if present.
2. Read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv` before changing skills.
3. Read the active sandbox README, stage plan, ADRs, and latest handoff named by `BOOTSTRAP.md` or `AGENT_CONTEXT.json`.
4. Inspect `git status --short` before edits and preserve unrelated user or prior-agent changes.
5. If work will create or update handoffs, journals, lessons, or agent context, also use `skills/project-memory-artifacts/SKILL.md`.

## Granular Skill Routing

Use a narrower skill when the task is specifically one of these:

- `skills/apply-implementation-defaults/SKILL.md` for implementation, review, refactoring, validation, or tooling choices.
- `skills/write-adr/SKILL.md` for ADRs and context-freeze decision records.
- `skills/write-journal-entry/SKILL.md` for dated chronological project journals.
- `skills/write-lesson/SKILL.md` for reusable lessons and learning artifacts.
- `skills/write-handoff/SKILL.md` for handoffs, resume notes, and constrained-agent briefs.
- `skills/maintain-agent-context/SKILL.md` for `AGENT_CONTEXT.json`, startup docs, registries, and cross-agent memory surfaces.

## Implementation Defaults

- Treat the repo as a sandbox research workbench. Prefer small, local, readable experiments over architecture.
- Prefer plain Python, explicit dataclasses or simple models, local files, JSON/JSONL/CSV/Markdown, and deterministic command-line probes.
- Do not add databases, services, schedulers, Docker, web APIs, queues, vector stores, or production scaffolding unless a stage or ADR explicitly earns that choice.
- Read existing file-local patterns before editing. Extend the current shape instead of introducing a new framework or broad abstraction.
- Keep changes narrowly scoped to the active stage, detector, schema, skill, or memory artifact.
- Preserve source text, provenance, source IDs, node IDs, source type, run identity, timestamps, schema versions, and parser/reference uncertainty whenever artifacts feed later stages.
- Prefer structured parsers, schema-aware reads, and project-owned models over ad hoc string manipulation when the repo already provides them.
- Add fields, edge types, or schema changes only when there is an identified downstream consumer or evidence-layer need.
- Separate evidence layers: parser outputs and candidate evidence are not final findings; detector findings are not legal conclusions; reviewer reports surface questions for human judgment.

## Sandbox 002 Bias

- Keep active work aligned to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Use canonical corpus paths under `corpus/kentucky-homeowners-policy-smells/sources/`; do not point pipeline code at smell subdirectories.
- Treat manual SERFF sources as known gaps, not blockers, unless the active experiment needs them.
- For qualitative-language heuristics, check `source_type` before flagging. Carrier filings and regulatory documents use words like "reasonable" differently.
- Use exact phrase, lexical, metadata, citation/reference, and graph-expanded baselines before embeddings.
- Defer vector infrastructure until retrieval evaluation shows a concrete failure it can fix.

## Validation Preferences

- Run the smallest reliable validation for the changed layer: schema validation, focused unit tests, a stage runner, detector runner, or report builder.
- Prefer real corpus snippets and existing gold sets over invented fixtures.
- If validation is not run, say exactly what was not run and why.
- When outputs change, report counts and run IDs, not just "it worked."
- Do not claim a stage, detector, or skill is complete unless the checklist, outputs, and validation support it.

## Handoff To Constrained Agents

When preparing work for Claude Code or another constrained agent:

- Name the exact files to read and edit.
- State the exact next mechanical step.
- List forbidden actions, especially broad refactors, infrastructure, corpus expansion, and unrelated scans.
- Include current run IDs, output directories, stage status, and loose threads.
- Prefer a dense context-freeze shape when the next task is mechanical.

## Guardrails

- Do not store durable project knowledge only in private assistant memory.
- Do not flatten project nuance into generic best practices.
- Do not expand active scope beyond the controlling sandbox documents.
- Do not overwrite or revert unrelated dirty-worktree changes.
- Do not make automated legal advice claims.
- Do not optimize for cleverness when a readable probe answers the stage question.
