# 2026-06-05 - Claude handoff startup tightening

## Summary

Tightened Claude Code startup instructions after Claude did not automatically read the current handoff/backlog plan before beginning backlog work.

## What Changed

- Updated `CLAUDE_CONSTRAINTS.md` to pre-authorize the current root handoff and backlog implementation plan.
- Added an explicit rule that Claude must read `latest_handoff` and `latest_backlog_plan` from `AGENT_CONTEXT.json` when present and relevant.
- Updated `CLAUDE.md` with the same operational reminder.
- Updated `AGENT_CONTEXT.json` startup order to include the latest handoff and backlog plan.
- Broadened Claude startup read access for repo-visible planning, instruction, source-code, schema, and memory files while keeping write access limited to the active task file allowlist.

## Why

The backlog implementation plan was repo-visible and linked from compact context, but Claude's hard constraint profile made extra reads easy to treat as optional. The fix moves the requirement into Claude's constrained startup path and gives Claude enough read access to understand repo-visible memory without one-off allowlist patches.

## Current State

The next Claude session should read:

- `HANDOFF-2026-06-05-backlog-planning.md`
- `BACKLOG-IMPLEMENTATION-PLAN.md`

before implementing backlog work.
