---
name: write-adr
description: Write or update architecture decision records. Use when a user asks for an ADR, decision record, context freeze ADR, architectural choice, accepted/rejected alternatives, stage-scope decision, tooling decision, or durable record explaining why a project chose one path over another.
---

# Write ADR

## Startup

1. Read the repository startup instructions and current context.
2. Read only the documents needed to understand the decision: controlling roadmap, stage doc, prior ADRs, handoff, and relevant diffs.
3. Identify whether the ADR is canonical decision history or a mechanical context freeze.

## Decision ADR Shape

Use this shape for ordinary architectural or scope decisions:

- Title with ADR number and decision name
- Date, status, and scope
- Context
- Decision
- Consequences
- Rejected alternatives
- Follow-up checklist with checkboxes

## Context Freeze Shape

Use this shape when the next agent needs a mechanical resume point:

- System State
- Completed Work (Do Not Re-do)
- Immediate Next Mechanical Step
- Forbidden Actions
- Exact Files To Read First

## Rules

- Keep ADRs dense and objective.
- Record decisions, not general brainstorming.
- Include alternatives only when they were plausible.
- Distinguish accepted decisions from parked possibilities.
- Do not rewrite old ADRs for new work unless the user explicitly asks; add a new ADR or an addendum when the project changed.
- Include actionable checklists with checkboxes when the ADR creates follow-up work.

## Output

Report the ADR path, decision status, source docs read, and any open follow-up items.
