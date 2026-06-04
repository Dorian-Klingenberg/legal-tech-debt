# Using Project Skills

Status: Draft user guide

This guide explains how to use the repo-visible skills in this project, especially the new granular agent workflow skills.

## What A Skill Is

A skill is a reusable workflow for an agent.

Use a skill when you want an agent to behave in a particular way on a recurring task: write an ADR, make a handoff, preserve coding preferences, update shared context, or build a legal RAG artifact.

A skill is not the same as current project state. Current state belongs in handoffs, journals, ADRs, roadmaps, and `AGENT_CONTEXT.json`.

## Quick Start

When asking an agent to use a skill, name the skill and the target artifact or task.

Examples:

```text
Use write-handoff to create a resume note for the current Sandbox 002 state.
```

```text
Use write-adr to document why we are deferring vector infrastructure.
```

```text
Use apply-implementation-defaults while reviewing this detector change.
```

```text
Use maintain-agent-context to update AGENT_CONTEXT.json and the startup docs after this stage closes.
```

For Codex, the skill metadata may eventually auto-trigger after installation. Until then, naming the skill explicitly is the safest way to make sure it is used.

For Claude Code or GitHub Copilot, point them at the repo path:

```text
Read skills/write-lesson/SKILL.md and use it to create a lesson from this validation failure.
```

## Which Skill Should I Use?

| If you want... | Use this skill |
|---|---|
| Code changes, code review, implementation taste, validation choices, avoiding infrastructure drift | `apply-implementation-defaults` |
| An architecture decision, scope decision, tooling decision, or context-freeze ADR | `write-adr` |
| A dated record of what happened in a session, research pass, or implementation pass | `write-journal-entry` |
| A reusable learning artifact, pattern, warning, or failure mode | `write-lesson` |
| A resume note for the next agent or next work session | `write-handoff` |
| Updates to `AGENT_CONTEXT.json`, `AGENTS.md`, `CLAUDE.md`, Copilot instructions, skill registry, or startup order | `maintain-agent-context` |
| Sandbox 002 legal document ingestion, parsing, retrieval, citations, evidence bundles, or RAG work | `legal-rag-builder` |
| A broader memory task that may involve several artifact types | `project-memory-artifacts` |
| A broader coding-preference task that may involve implementation, validation, and handoff behavior | `project-coding-preferences` |

## Common Combinations

Use more than one skill when the task crosses artifact boundaries.

| Situation | Recommended skills |
|---|---|
| Closing a sandbox stage | `write-journal-entry`, `write-lesson`, `write-handoff`, `maintain-agent-context` |
| Making a code change that creates a new project convention | `apply-implementation-defaults`, then `write-lesson` |
| Preparing Claude to continue a mechanical task | `write-handoff`, then `maintain-agent-context` if startup docs need updating |
| Recording a decision that changes future implementation | `write-adr`, then `maintain-agent-context` |
| Creating a new skill | Use `skills/SKILL-DEVELOPMENT.md`; optionally use `maintain-agent-context` afterward |

## What To Ask For

Good prompts are specific about the skill, source material, and output path.

```text
Use write-journal-entry. Summarize today's work on the Smell 5 detector and write it under journal/ with today's date.
```

```text
Use write-handoff. Create a constrained-agent handoff for Claude. Include exact files to read, exact files it may edit, the next mechanical step, and forbidden actions.
```

```text
Use maintain-agent-context. Update AGENT_CONTEXT.json after the active run changes to output/002/<run_id>/, and update any startup docs that reference the old run.
```

Less useful:

```text
Make the docs better.
```

That can still work, but the agent has to infer which mechanism you want.

## Mechanism Boundaries

Use skills for reusable procedures.

Use other artifacts for state and history:

- `AGENT_CONTEXT.json` — compact current state and startup hints.
- `BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` — startup contracts.
- ADRs — decisions and rejected alternatives.
- Journals — chronological point-in-time records.
- Lessons — reusable learning.
- Handoffs — resume points.
- Templates — stable document shapes.

If a skill captures durable knowledge that all agents need, update the shared docs too. Do not leave important project memory only in a skill body.

## Lifecycle

The current granular skills are `draft`.

That means:

- They are valid skill folders.
- They can be used now.
- They should be validated against real work before being marked `active`.
- They are not installed into `$CODEX_HOME/skills` yet.

After a skill works well on a real task, update `skills/registry.csv` from `draft` to `active`.

## Installed Versus Repo-Visible

Repo-visible skills live under `skills/` and can be read by Codex, Claude Code, GitHub Copilot, and humans.

Installed Codex skills live under `$CODEX_HOME/skills` and may auto-trigger in Codex. Installation is optional. The repo should remain the source of truth either way.

## Safe Defaults

- Prefer naming the skill explicitly in the prompt.
- Prefer one narrow skill for one narrow task.
- Use umbrella skills only when the work spans multiple artifact types.
- Keep installable skill folders lean; put user guides in repo-level docs like this file.
- Validate machine-readable context after edits.
- Update discovery surfaces when adding or changing memory artifacts.
