# Journal: Granular Agent Workflow Skills

Date: 2026-06-04
Scope: Skill workbench; reusable documentation and implementation workflows

## Session Summary

The user asked whether Codex's documentation-side behaviors should be split into pick-and-choose skills, and whether skills are the right mechanism. This session split the broad agent behavior into granular, portable skills and documented the boundary between skills and other project-memory mechanisms.

## What Changed

- Created `skills/apply-implementation-defaults/SKILL.md`.
- Created `skills/write-adr/SKILL.md`.
- Created `skills/write-journal-entry/SKILL.md`.
- Created `skills/write-lesson/SKILL.md`.
- Created `skills/write-handoff/SKILL.md`.
- Created `skills/maintain-agent-context/SKILL.md`.
- Added Codex-facing `agents/openai.yaml` metadata for each new skill via `init_skill.py`.
- Added `skills/proposals/granular-agent-workflow-skills.md`.
- Updated `skills/registry.csv` with six new draft skills.
- Updated `skills/README.md` with the granular skill table and mechanism boundaries.
- Updated `skills/project-coding-preferences/SKILL.md` and `skills/project-memory-artifacts/SKILL.md` with routing to narrower skills.
- Updated `BOOTSTRAP.md` and `AGENT_CONTEXT.json` so future agents can discover the granular skill set.
- Added `skills/USING-SKILLS.md` as a human-facing guide for choosing, prompting, and combining skills.
- Linked `skills/USING-SKILLS.md` from `skills/README.md`.

## Mechanism Decision

Skills are appropriate for reusable procedures and agent behavior. They are not the best home for current project state or canonical decisions.

Use:

- `AGENT_CONTEXT.json` for compact current state and startup hints.
- startup docs for cross-agent contracts.
- ADRs for accepted decisions and rejected alternatives.
- journals for chronological session memory.
- lessons for reusable learning.
- handoffs for resume points.
- templates when the artifact shape matters more than the workflow.

## Validation Performed

- Ran `quick_validate.py` for all six new granular skills.
- Re-ran validation for `project-coding-preferences` and `project-memory-artifacts`.
- Validated `AGENT_CONTEXT.json` with `python -m json.tool`.
- Parsed `skills/registry.csv` and confirmed all six new skill rows exist.
- Added usage documentation after the initial split so humans know how to ask agents to use the skills.

## Current State

All six granular skills are valid and registered, but remain `draft` because they have not yet been validated on real tasks.

## What Comes Next

- [ ] Use each granular skill on at least one real project task.
- [ ] Mark individual skills `active` after validation, not as a batch by default.
- [ ] Decide whether to install or mirror any of these into `$CODEX_HOME/skills` after they prove useful.
