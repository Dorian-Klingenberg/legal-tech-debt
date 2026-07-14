---
name: maintain-agent-context
description: Maintain shared agent context and startup instructions. Use when updating AGENTS-style files, Claude or Copilot instructions, compact agent context JSON, skill registries, bootstrap docs, cross-agent memory, startup reading order, current focus, active scope, or constraints that future agents must inherit.
---

# Maintain Agent Context

## Startup

1. Read the repository startup instructions, compact context file, and current agent entry files.
2. Inspect the source event that changed context: user decision, handoff, ADR, stage status, corpus change, validation run, or new skill.
3. Decide which surfaces need canonical updates and which only need point-in-time notes.

## Context Surfaces

Common surfaces:

- `AGENTS.md` or equivalent general agent entry
- `CLAUDE.md`, Copilot instructions, or tool-specific entry files
- bootstrap/startup contract files
- compact machine-readable context such as `AGENT_CONTEXT.json`
- skill registry and skill README files
- latest handoff, journal, ADR, lesson, roadmap, or stage status

## Update Rules

- Put durable project memory where all agents can read it.
- Keep compact context current but concise; link to canonical docs for detail.
- Keep tool-specific instructions synchronized without copying more prose than needed.
- Preserve startup order and hard constraints.
- When constraints and startup requirements conflict, resolve the conflict explicitly instead of relying on agent inference.
- Validate JSON or machine-readable context after edits.
- Include checkboxes when updating planning or roadmap docs.

## Do Not

- Do not hide durable memory in a private assistant profile.
- Do not make a point-in-time handoff the only canonical source.
- Do not loosen tool constraints broadly when a narrow startup or memory-task exception will work.
- Do not update one agent entry file and leave the others stale when the memory is cross-agent.

## Output

Report which context surfaces changed, why, what was validated, and what still needs human review.
