# Project Memory Artifacts Skill Proposal

Status: draft implemented

## Purpose

Create a reusable workflow for writing shared, repo-visible memory artifacts:

- handoffs
- journals
- lessons
- agent context updates
- bootstrap/startup record updates

The skill exists because the user works across Codex, GitHub Copilot, and Claude Code. Durable project memory must be readable by all of them, not trapped in one assistant's private memory.

## Source Pattern

The pattern is based on a review of the `grannies-house-trials` project, especially:

- `AGENTS.md`
- `AGENT_CONTEXT.json`
- `handoff/README.md`
- dated handoff and journal files
- lesson catalogs and subproject lesson files
- `.github/instructions/*.instructions.md`

## Intended Triggers

Use the skill when the user asks for:

- "add a journal entry"
- "write a handoff"
- "capture lessons"
- "make a note for future agents"
- "update all agent contexts"
- "close this stage/sandbox"
- "pause and document where we are"
- "make sure Codex, Copilot, and Claude can all read this"

## Design Notes

- Keep `SKILL.md` short.
- Put the Grannies-derived pattern notes in a reference file.
- Do not create automation or infrastructure yet.
- Keep canonical truth separate from point-in-time snapshots.
- Always update discovery surfaces when creating a new artifact.

