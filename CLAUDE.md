# Claude Code Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. Do not rely only on Claude-specific memory; project instructions must stay visible to Codex, GitHub Copilot, and other future agents too.

## Mandatory Runtime Constraint Profile

- Read `CLAUDE_CONSTRAINTS.md` before any exploration, file reads, planning, or tool use.
- Treat `CLAUDE_CONSTRAINTS.md` as an active, hard constraint profile for the full session.
- If `CLAUDE_CONSTRAINTS.md` is unavailable, unreadable, or conflicts cannot be resolved, stop immediately and ask for human instruction.
- Do not proceed under inferred policy.

Key reminders:

- The current work is sandbox research and proof-of-concept experimentation.
- Avoid production infrastructure unless a stage explicitly evaluates it.
- Read the relevant project and sandbox documentation before starting.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Sandbox 002 Stages 002–007 are all complete. Corpus expanded to 28 sources (added KFBM SERFF filings + 10 unparsed KY sources). Active run: `output/002/20260603_210315_87283951/` (353 nodes, 23 findings). Smell 2 detector tightened: H001/H003 suppressed for regulatory source types. Read `HANDOFF-2026-06-03d.md` for full state. Loose threads: Smell 5 detector, gold set re-eval on new run. Next: Sandbox 003 (`sandboxes/003-findings-triage/`).
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

