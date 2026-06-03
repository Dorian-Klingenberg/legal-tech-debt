# GitHub Copilot Instructions

This repository uses shared cross-agent project memory.

Before suggesting or making changes, read `BOOTSTRAP.md` and follow its startup contract. Do not rely on Copilot-only context; project memory must remain visible to Codex, Claude Code, and future agents.

Key reminders:

- Current work is sandbox proof-of-concept development and experimentation.
- Prefer quick, clean, readable implementations over infrastructure.
- Read the relevant project and sandbox documentation before starting work.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Sandbox 002 Stage sequence: Stage 002 (discovery/instrumentation), Stage 003 (retrieval baseline), and Stage 004 (gold set evaluation) are all complete. Phases 1–3 done. Current path: Phase 4 (semantic retrieval experiment, now earned) or corpus expansion for the remaining gold set tiers. Read `HANDOFF-2026-06-03b.md` for full state.
- Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist. Treat parser/reference uncertainty as part of the evidence layer.
- Stage 002 JSON/JSONL artifacts should carry schema version, run identity, creation timestamp, and stable source/node IDs under a fixed parsing strategy.
- For Sandbox 002 corpus work, read `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md` for the canonical source index and file locations. All unique source files live in `corpus/kentucky-homeowners-policy-smells/sources/` — do not reference smell subdirectory paths in pipeline code. Also read `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before procuring or assuming missing sources.
- For Sandbox 002 RAG parser/model work, read `sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md`; Docling is a parser/enrichment adapter, not a vector database or verified general local LLM runtime.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal, handoff, lesson, and context records so Codex, Claude Code, GitHub Copilot, and future agents inherit the same project state. Use `skills/project-memory-artifacts/SKILL.md` for that workflow.
- Keep `sandboxes/002-claims-regulatory-automation/002-RAG-PHASE-PLAN.md` up to date as work progresses: check off completed items when they are done, add new items if work goes beyond the original list, and update the phase status line when a phase completes.
- When creating any planning, phase, or roadmap document, include actionable checklists with checkboxes — including items that are already complete (checked off). The user wants to see what has been done and what remains without reading prose.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Preserve the numbered sandbox stage workflow and document lessons.

