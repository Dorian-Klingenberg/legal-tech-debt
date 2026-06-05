# Agent Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. These instructions apply to Codex and to any general coding agent that reads `AGENTS.md`.

Key reminders:

- The user uses Codex, GitHub Copilot, and Claude Code. Durable memory must be visible to all of them.
- Read `AGENT_OPERATING_MODEL.md` after `BOOTSTRAP.md` and `AGENT_CONTEXT.json` to keep the shared role split and drift rules in view.
- Read `AGENT_CONTEXT.json` after `BOOTSTRAP.md` when it exists; it is the compact current-state context for constrained agents and fast startup.
- This is currently sandbox proof-of-concept work, not infrastructure work.
- Read the relevant project and sandbox documentation before starting changes.
- Before substantive code changes or reviews, read `skills/project-coding-preferences/SKILL.md` and apply its shared implementation defaults.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Sandbox 002 is closed as a discovery/retrieval/detector/reviewer-report proof of concept. Preserved repaired run: `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/` (28 sources, 353 nodes, 121 candidate evidence items, 39 Stage 003 retrieval bundles, 35 findings across all five smells). Smell 5 resolved via graph-based gap detection (ADR-010). Sandbox 003 and Sandbox 004 are also complete. Active lane: choose BACKLOG-019 Missing State Amendatory detector or BACKLOG-015 case library; latest handoff is `sandboxes/004-expert-drilldown/HANDOFF-2026-06-04.md`.
- Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist. Treat parser/reference uncertainty as part of the evidence layer.
- Stage 002 JSON/JSONL artifacts should carry schema version, run identity, creation timestamp, and stable source/node IDs under a fixed parsing strategy.
- For Sandbox 002 corpus work, read `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md` for the canonical source index and file locations. All unique source files live in `corpus/kentucky-homeowners-policy-smells/sources/` — do not reference smell subdirectory paths in pipeline code. Also read `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before procuring or assuming missing sources.
- For Sandbox 002 RAG parser/model work, read `sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md`; Docling is a parser/enrichment adapter, not a vector database or verified general local LLM runtime.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal, handoff, lesson, and context records so all future agents inherit the current state. Use `skills/project-memory-artifacts/SKILL.md` for that workflow.
- Write chronological journal entries under the top-level `journal/` folder. Do not add new `JOURNAL-*.md` files inside sandbox folders; sandbox-local files should be handoffs, lessons, closure docs, or stage docs.
- When you update a specification, stage plan, roadmap, or architecture document, capture what changed and why in the end-of-session journal entry. Decision tracking — knowing when, why, and what changed — is the goal. ADRs are reserved for architectural choices between named alternatives, not routine plan updates. Silent plan edits with no session record are not acceptable.
- Keep `sandboxes/002-claims-regulatory-automation/002-RAG-STAGE-PLAN.md` up to date as work progresses: check off completed items when they are done, add new items if work goes beyond the original list, and update the stage status line when a stage completes.
- When creating any planning, phase, or roadmap document, include actionable checklists with checkboxes — including items that are already complete (checked off). The user wants to see what has been done and what remains without reading prose.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Keep experiments quick, clean, readable, and well documented.
- Before starting substantive work, read `SECRET_SCAN_REPORT.md` if it exists and remind the user to review or resolve any open secret-scan findings.

