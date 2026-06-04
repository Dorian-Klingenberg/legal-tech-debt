---
name: write-handoff
description: Write handoffs, resume notes, pause records, context freezes, and next-agent briefs. Use when future work needs a reliable restart point after a session, stage transition, partial implementation, blocked task, corpus change, validation run, or constrained-agent handoff.
---

# Write Handoff

## Startup

1. Read the repository startup instructions and current context.
2. Inspect focused diffs, outputs, logs, and stage docs needed to distinguish completed work from pending work.
3. Identify the target audience: human, general agent, constrained agent, or specific tool.

## Handoff Shape

Prefer:

- Title with date and scope
- Purpose
- Current State
- Active Scope and Exclusions
- Files Changed or Touched
- Validation Performed and Not Performed
- Known Gaps, Risks, or Drift
- Recommended Next Steps
- Startup Reading List for the Next Agent

## Context Freeze

For constrained or mechanical continuation, include:

- Core objective
- Architecture and scope constraints
- Explicit file allowlist
- Completed work not to redo
- Immediate next mechanical step
- Forbidden actions

## Rules

- Be concrete: include paths, run IDs, output counts, command snippets, and validation status.
- Keep handoffs factual and point-in-time.
- Distinguish blockers from ordinary open questions.
- Include checkboxes for follow-up work.
- Update discovery surfaces when the handoff becomes the latest resume point.

## Do Not

- Do not use a handoff as the only place for canonical project changes.
- Do not omit unrelated dirty-worktree changes if they affect the next agent.
- Do not tell the next agent to broadly explore when exact files are known.

## Output

Report the handoff path, source evidence used, exact next step, and any unresolved risks.
