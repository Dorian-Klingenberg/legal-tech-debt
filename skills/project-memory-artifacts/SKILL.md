---
name: project-memory-artifacts
description: Create or update shared project memory artifacts. Use when the user asks for a handoff, journal entry, lesson, project memory update, agent context update, durable notes for future agents, stage closure notes, pause/resume documentation, or cross-agent records for Codex, GitHub Copilot, Claude Code, and future agents.
---

# Project Memory Artifacts

## Startup

1. Read `BOOTSTRAP.md`.
2. Read `skills/SKILL-DEVELOPMENT.md`.
3. Read the active sandbox, skill, corpus, roadmap, handoff, or stage docs that match the work being summarized.
4. Inspect `git status --short` and, when useful, focused diffs/logs to separate completed work from unrelated pending changes.
5. If the user references the Grannies memory style, read `references/grannies-memory-patterns.md`.

## Granular Skill Routing

Use a narrower skill when the artifact type is clear:

- `skills/write-adr/SKILL.md` for ADRs and context-freeze ADRs.
- `skills/write-journal-entry/SKILL.md` for chronological journals.
- `skills/write-lesson/SKILL.md` for reusable lessons.
- `skills/write-handoff/SKILL.md` for handoffs and next-agent briefs.
- `skills/maintain-agent-context/SKILL.md` for startup docs, compact context files, and registries.

## Decision Rules

- Create a **journal** when capturing what happened in a session, day, research pass, implementation pass, or experiment.
- Create a **handoff** when future work needs a resume point after a pause, scope shift, stage transition, sandbox closure, corpus change, or major context transfer.
- Create a **lesson** when the work produced reusable understanding, a repeatable pattern, a caution, or a teaching artifact that should outlive the session.
- Update **agent context or bootstrap records** when project scope, startup reading order, active exclusions, current focus, canonical docs, or cross-agent instructions change.
- Update indexes, readmes, registries, catalogs, or documentation maps when adding an artifact that future agents must discover.

Use more than one artifact when the event has more than one purpose. For example, a stage closure may need a journal for the day, a handoff for resume context, and a lesson for the reusable insight.

## Artifact Workflow

1. Identify the artifact purpose before writing.
2. Gather evidence from current docs, changed files, user decisions, validation output, and known gaps.
3. Choose the repo-visible location that matches existing conventions.
4. Write concise, dated Markdown with concrete file paths, scope boundaries, validation performed, and open questions.
5. Preserve the difference between canonical truth and point-in-time notes.
6. Update discovery surfaces so all agents can find the artifact.
7. Report what was created, what was verified, and what remains unresolved.

## Expected Shapes

For a **journal**, prefer:

- title with date and scope
- summary
- what changed
- decisions made
- validation performed
- current state
- next useful work

For a **handoff**, prefer:

- title with date and scope
- purpose
- current state
- active scope and exclusions
- files changed or touched
- validation performed and not performed
- known gaps, risks, or drift
- recommended next steps
- startup reading list for the next agent

For a **lesson**, prefer:

- problem or question
- why it mattered
- pattern or solution
- concrete example
- validation or evidence
- limitations
- what to reuse next time
- catalog/index update when a lesson system exists

For **agent context**, prefer structured, cross-agent files already used by the repo: `BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, skill registries, sandbox roadmaps, handoffs, and machine-readable context files when present.

## Guardrails

- Do not store durable project memory only in private assistant memory.
- Do not treat a handoff as canonical truth; update canonical docs when the underlying project state changed.
- Do not mark work complete unless docs, repository state, and validation support it.
- Do not erase known unknowns. Record them explicitly.
- Do not add infrastructure for memory capture unless the user explicitly asks for it.
- Do not overwrite unrelated user changes while summarizing work.

## Output Expectations

When finished, tell the user:

- which artifact files were created or updated
- which source docs or changed files informed the record
- what validation, if any, was performed
- any remaining open decisions or known gaps
