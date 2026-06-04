# Granular Agent Workflow Skills Proposal

Status: draft implemented

## Recurring Workflow

The project needs reusable agent behaviors that are smaller than a single broad "project memory" or "coding preferences" skill. Other projects should be able to copy only the pieces they need.

## Axes Of Change

The useful split is by agent action:

- implementation defaults
- ADR writing
- journal writing
- lesson writing
- handoff writing
- agent-context maintenance

This is different from splitting by file extension. The same Markdown file type can serve very different purposes.

## Why These Should Be Skills

Skills are appropriate for reusable procedures:

- how to decide what to read
- how to structure an artifact
- what guardrails to preserve
- what validation or discovery surfaces to update
- what not to do

They should not be the only place for current project state or canonical decisions.

## Mechanism Boundary

Use skills for procedures and agent behavior.

Use other mechanisms for durable state:

- `AGENT_CONTEXT.json` for compact current state and startup hints
- startup docs for cross-agent contracts
- ADRs for accepted decisions and rejected alternatives
- journals for chronological point-in-time session memory
- lessons for reusable learning and patterns
- handoffs for resume points and next-agent instructions
- templates for stable output shapes

## Draft Skills Created

- [x] `skills/apply-implementation-defaults/SKILL.md`
- [x] `skills/write-adr/SKILL.md`
- [x] `skills/write-journal-entry/SKILL.md`
- [x] `skills/write-lesson/SKILL.md`
- [x] `skills/write-handoff/SKILL.md`
- [x] `skills/maintain-agent-context/SKILL.md`

## Discovery Updates

- [x] Add rows to `skills/registry.csv`
- [x] Add a granular skills section to `skills/README.md`
- [x] Add routing notes to `skills/project-coding-preferences/SKILL.md`
- [x] Add routing notes to `skills/project-memory-artifacts/SKILL.md`
- [x] Add mechanism boundaries to `AGENT_CONTEXT.json`
- [x] Add the granular skill set to `BOOTSTRAP.md`

## First Validation Tasks

- [ ] Use `write-adr` for a real future decision record.
- [ ] Use `write-journal-entry` for a real session journal.
- [ ] Use `write-lesson` for a real reusable lesson.
- [ ] Use `write-handoff` for a real constrained-agent handoff.
- [ ] Use `maintain-agent-context` for a real context update.
- [ ] Use `apply-implementation-defaults` for a real implementation or review task.

After at least one real validation pass per skill, consider marking the relevant skill `active`.
