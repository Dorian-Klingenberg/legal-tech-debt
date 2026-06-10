# Claude Code Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. Do not rely only on Claude-specific memory; project instructions must stay visible to Codex, GitHub Copilot, and other future agents too.

## Mandatory Runtime Constraint Profile

- Read `CLAUDE_CONSTRAINTS.md` before any exploration, file reads, planning, or tool use.
- Treat `CLAUDE_CONSTRAINTS.md` as an active, hard constraint profile for the full session.
- If `CLAUDE_CONSTRAINTS.md` is unavailable, unreadable, or conflicts cannot be resolved, stop immediately and ask for human instruction.
- Do not proceed under inferred policy.

## Environment & Tool Constraints

- Never use visual or GUI tools (such as File Explorer, native application windows, or browser screenshots) if a command-line alternative is available.
- Always prefer executing commands within Windows Subsystem for Linux (WSL) over any other interface.
- If a task cannot be handled within WSL, fall back to standard CLI tools or PowerShell commands.
- Use text-based terminal utilities (e.g., `ls`, `grep`, `find`, `cat`, `Get-ChildItem`) exclusively for navigating file systems and managing project tasks.

Key reminders:

- The current work is sandbox research and proof-of-concept experimentation.
- Read `AGENT_CONTEXT.json` after `BOOTSTRAP.md` when it exists; it is the compact current-state context intended to reduce broad exploratory reads.
- Read `AGENT_OPERATING_MODEL.md` after `BOOTSTRAP.md` and `AGENT_CONTEXT.json` so the shared role split and drift rules stay in view.
- Always read the `latest_handoff` and `latest_backlog_plan` paths named in `AGENT_CONTEXT.json` before implementing backlog work. If either path is missing or unreadable, stop and ask for human instruction instead of proceeding from memory.
- Claude has broad read access during startup for repo-visible planning, instruction, source-code, schema, and memory files. This does not grant broad write access: edits remain limited to the active task's explicit file allowlist, user-named paths, or paths named by the current handoff/backlog plan.
- Avoid production infrastructure unless a stage explicitly evaluates it.
- Read the relevant project and sandbox documentation before starting.
- Before substantive code changes or reviews, read `skills/project-coding-preferences/SKILL.md` and apply its shared implementation defaults.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Sandbox 002 is closed as a discovery/retrieval/detector/reviewer-report proof of concept. Preserved repaired run: `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/` (28 sources, 353 nodes, 121 candidate evidence items, 39 Stage 003 retrieval bundles, 35 findings across all five smells). Smell 5 resolved via graph-based gap detection (ADR-010).
- Sandbox 003 is closed. Executive summary complete (prospect-ready pending final human read). Latest handoff: `sandboxes/003-findings-triage/HANDOFF-2026-06-04b.md`.
- Sandbox 004 is closed as expert drill-down report PoC. Three entries built (S4-H001, S5-H004, S4-H003). Static HTML at `sandboxes/004-expert-drilldown/output/drilldown_report.html`. Latest handoff: `sandboxes/004-expert-drilldown/HANDOFF-2026-06-04.md`.
- Active lane: BACKLOG-019 (Missing State Amendatory detector) or BACKLOG-015 (case library). See `BACKLOG.md` and `AGENT_CONTEXT.json`.
- Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist. Treat parser/reference uncertainty as part of the evidence layer.
- Stage 002 JSON/JSONL artifacts should carry schema version, run identity, creation timestamp, and stable source/node IDs under a fixed parsing strategy.
- For Sandbox 002 corpus work, read `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md` for the canonical source index and file locations. All unique source files live in `corpus/kentucky-homeowners-policy-smells/sources/` — do not reference smell subdirectory paths in pipeline code. Also read `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before procuring or assuming missing sources.
- For Sandbox 002 RAG parser/model work, read `sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md`; Docling is a parser/enrichment adapter, not a vector database or verified general local LLM runtime.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal, handoff, lesson, and context records so Codex, GitHub Copilot, Claude Code, and future agents inherit the same project state. Use `skills/project-memory-artifacts/SKILL.md` for that workflow.
- Write chronological journal entries under the top-level `journal/` folder. Do not add new `JOURNAL-*.md` files inside sandbox folders; sandbox-local files should be handoffs, lessons, closure docs, or stage docs.
- When you update a specification, stage plan, roadmap, or architecture document, capture what changed and why in the end-of-session journal entry. Decision tracking — knowing when, why, and what changed — is the goal. ADRs are reserved for architectural choices between named alternatives, not routine plan updates. Silent plan edits with no session record are not acceptable.
- Keep `sandboxes/002-claims-regulatory-automation/002-RAG-STAGE-PLAN.md` up to date as work progresses: check off completed items when they are done, add new items if work goes beyond the original list, and update the stage status line when a stage completes.
- When creating any planning, phase, or roadmap document, include actionable checklists with checkboxes — including items that are already complete (checked off). The user wants to see what has been done and what remains without reading prose.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Keep outputs readable and document what each experiment teaches.
