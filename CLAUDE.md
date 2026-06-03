# Claude Code Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. Do not rely only on Claude-specific memory; project instructions must stay visible to Codex, GitHub Copilot, and other future agents too.

Key reminders:

- The current work is sandbox research and proof-of-concept experimentation.
- Avoid production infrastructure unless a stage explicitly evaluates it.
- Read the relevant project and sandbox documentation before starting.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Sandbox 002 Stages 002–005 are all complete. BM25 retrieval is 100% on the gold set; semantic retrieval (Phase 4) was run and deferred — it adds nothing on top of BM25 for this corpus. Vector store selection is deferred until ADR-002 re-open conditions are met. Read `HANDOFF-2026-06-03c.md` for full state and next-step options.
- Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist. Treat parser/reference uncertainty as part of the evidence layer.
- Stage 002 JSON/JSONL artifacts should carry schema version, run identity, creation timestamp, and stable source/node IDs under a fixed parsing strategy.
- For Sandbox 002 corpus work, read `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md` for the canonical source index and file locations. All unique source files live in `corpus/kentucky-homeowners-policy-smells/sources/` — do not reference smell subdirectory paths in pipeline code. Also read `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before procuring or assuming missing sources.
- For Sandbox 002 RAG parser/model work, read `sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md`; Docling is a parser/enrichment adapter, not a vector database or verified general local LLM runtime.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal, handoff, lesson, and context records so Codex, GitHub Copilot, Claude Code, and future agents inherit the same project state. Use `skills/project-memory-artifacts/SKILL.md` for that workflow.
- Keep `sandboxes/002-claims-regulatory-automation/002-RAG-STAGE-PLAN.md` up to date as work progresses: check off completed items when they are done, add new items if work goes beyond the original list, and update the stage status line when a stage completes.
- When creating any planning, phase, or roadmap document, include actionable checklists with checkboxes — including items that are already complete (checked off). The user wants to see what has been done and what remains without reading prose.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Keep outputs readable and document what each experiment teaches.
- Before starting substantive work, read `SECRET_SCAN_REPORT.md` if it exists and remind the user to review or resolve any open secret-scan findings.

