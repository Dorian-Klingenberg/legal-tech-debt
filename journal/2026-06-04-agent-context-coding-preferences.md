# Journal: Agent Context And Coding Preferences

Date: 2026-06-04
Scope: Cross-agent startup memory, skill workbench, Claude continuation constraints

## Session Summary

The user observed that Codex had implicit coding and implementation preferences that were not visible to Claude Code, GitHub Copilot, or future agents. This session converted those preferences into repo-visible artifacts.

## What Changed

- Created `AGENT_CONTEXT.json` as a compact current-state context file for fast startup and constrained-agent orientation.
- Created draft skill `skills/project-coding-preferences/SKILL.md` to capture shared implementation defaults.
- Generated Codex metadata at `skills/project-coding-preferences/agents/openai.yaml`.
- Added source proposal `skills/proposals/project-coding-preferences.md`.
- Registered the skill in `skills/registry.csv`.
- Linked the skill and context file from `skills/README.md`.
- Updated `BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` so future agents read the new context and skill.
- Updated `CLAUDE_CONSTRAINTS.md` with bounded startup and explicit memory-review exceptions so Claude can obey the repo startup contract without disabling ordinary task constraints.

## Decisions Made

- Keep `project-coding-preferences` in `draft` status until validated against a real implementation, review, or constrained-agent handoff task.
- Keep the new skill repo-visible only; do not install it into `$CODEX_HOME/skills` yet.
- Use `AGENT_CONTEXT.json` as the compact current-state source, while canonical detail remains in Markdown docs, ADRs, handoffs, and skills.
- Preserve strict Claude behavior for ordinary coding tasks, but allow named startup reads and explicit memory-review tasks to exceed the old 3-tool/60-second threshold.

## Validation Performed

- `quick_validate.py skills/project-coding-preferences` passed.
- `python -m json.tool AGENT_CONTEXT.json` passed.
- Generated `agents/openai.yaml` with the skill creator metadata script.
- Reviewed `git status --short` to confirm existing Sandbox 002 code/schema changes were already present and left untouched.

## Current State

The repository now has a shared implementation-preference layer:

- `AGENT_CONTEXT.json`
- `skills/project-coding-preferences/SKILL.md`
- `skills/proposals/project-coding-preferences.md`

Future agents should read these alongside the existing startup contract before coding or reviewing code.

## What Comes Next

- [ ] Validate the draft skill on a real follow-up task, such as Smell 5 detector calibration, gold set re-evaluation on run `87283951`, or a Claude context-freeze handoff.
- [ ] After validation, consider changing `project-coding-preferences` from `draft` to `active` in `skills/registry.csv`.
- [ ] Install or mirror the skill into `$CODEX_HOME/skills` only if the user wants Codex auto-discovery.
