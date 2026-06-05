# 2026-06-05 - Backlog implementation plan for Claude

## Summary

Created a root-level backlog implementation plan so Claude Code can pick up unblocked backlog items with detailed, constrained instructions instead of broad exploratory prompts.

## What Changed

- Added `BACKLOG-IMPLEMENTATION-PLAN.md`.
- Linked the plan from `BACKLOG.md`.
- Added `latest_backlog_plan` to `AGENT_CONTEXT.json`.
- Updated `latest_memory_journal` to this entry.

## Why

The project now has several viable backlog lanes, and the user wants to use Claude Code for implementation. Claude performs best when given:

- exact startup reading,
- item-specific file allowlists,
- acceptance criteria,
- validation commands,
- and forbidden actions.

The new plan turns the backlog into that kind of context freeze.

## Current Recommendation

Start with `BACKLOG-019` as the first Claude task. It is the cleanest code-oriented lane and should produce either a conservative detector or a well-documented "current corpus does not support this yet" result.

Keep `BACKLOG-015` as the next research/product-evidence lane.

## Validation

Documentation-only change. Final validation should include:

- `git diff --check`
- search for the plan path from `BACKLOG.md` and `AGENT_CONTEXT.json`
