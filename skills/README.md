# Project Skills

Status: Active project workbench

This folder holds shared, repo-visible skill development artifacts for the Legal Tech Debt project.

Skills are becoming a repeatable project artifact, similar to sandboxes. A skill is a reusable agent workflow: it tells an agent how to approach a recurring project task, what source-of-truth documents to read, what guardrails to preserve, and what outputs to produce.

## Important Distinction

Project skills are not private assistant memory.

- This folder is the cross-agent source of truth for skill development.
- Codex-installable skills may later be copied or generated into `$CODEX_HOME/skills`.
- GitHub Copilot and Claude Code should still be able to understand the skill intent by reading this folder.
- Durable project knowledge belongs in repo docs first; an installed Codex skill should point back to those docs rather than becoming the only copy.

## Current Skill Workflow

Use [USING-SKILLS.md](USING-SKILLS.md) if you want to know which skill to ask for and how to prompt an agent to use it.

Use [SKILL-DEVELOPMENT.md](SKILL-DEVELOPMENT.md) before creating or changing a skill.

Use [registry.csv](registry.csv) to track proposed, drafted, active, or installed skills.

Use templates under [templates](templates/) when creating a new skill artifact.

## Lifecycle

| Status | Meaning |
|---|---|
| proposed | The recurring workflow is identified, but the skill has not been drafted. |
| draft | A `SKILL.md` exists, but it has not been validated against real project work. |
| active | The skill is ready to use as a repo-visible workflow guide. |
| installed | A Codex-compatible copy has been installed or mirrored into `$CODEX_HOME/skills`. |
| retired | The skill has been superseded or is no longer useful. |

## Current Direction

The first project skill is `legal-rag-builder`: the repo-visible workflow used to build and maintain the completed local-first legal evidence substrate for Sandbox 002. Use it only when that sandbox is explicitly reopened.

Current artifacts:

- Active repo-visible skill: [legal-rag-builder/SKILL.md](legal-rag-builder/SKILL.md)
- Source proposal and raw notes: [proposals/legal-rag-builder.md](proposals/legal-rag-builder.md)
- Source-of-truth spec: [../sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md](../sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md)
- Architecture decisions: [Sandbox 002 ADRs](../sandboxes/002-claims-regulatory-automation/adr/)
- Boundary lesson: [rag-substrate-boundary-lesson.md](../sandboxes/002-claims-regulatory-automation/references/rag-substrate-boundary-lesson.md)
- Docling/local stack boundary: [docling-local-stack-boundary.md](../sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md)

The skill has been validated through the completed Sandbox 002 pipeline. It is not installed into `$CODEX_HOME/skills`; installation remains optional because repo visibility is the cross-agent requirement.

The second project skill is `project-memory-artifacts`: a workflow for creating shared handoffs, journals, lessons, and agent context updates that Codex, GitHub Copilot, Claude Code, and future agents can all read.

Current artifacts:

- Active repo-visible skill: [project-memory-artifacts/SKILL.md](project-memory-artifacts/SKILL.md)
- Source proposal and raw notes: [proposals/project-memory-artifacts.md](proposals/project-memory-artifacts.md)
- Pattern reference: [project-memory-artifacts/references/grannies-memory-patterns.md](project-memory-artifacts/references/grannies-memory-patterns.md)

This skill has been validated through repeated journal, handoff, lesson, and context updates. It is not installed into `$CODEX_HOME/skills`.

The third project skill is `project-coding-preferences`: a workflow for applying shared implementation preferences that were previously implicit in Codex context.

Current artifacts:

- Active repo-visible skill: [project-coding-preferences/SKILL.md](project-coding-preferences/SKILL.md)
- Source proposal and raw notes: [proposals/project-coding-preferences.md](proposals/project-coding-preferences.md)
- Fast cross-agent context: [../AGENT_CONTEXT.json](../AGENT_CONTEXT.json)

This skill has been used in implementation and review work. It is not installed into `$CODEX_HOME/skills`.

## Granular Reusable Skills

Some agent behaviors are better split into small skills that other projects can copy independently:

| Skill | Use When |
|---|---|
| [apply-implementation-defaults/SKILL.md](apply-implementation-defaults/SKILL.md) | Coding, reviewing, refactoring, validating, or choosing tools in sandbox/prototype work. |
| [write-adr/SKILL.md](write-adr/SKILL.md) | Recording accepted decisions, rejected alternatives, scope decisions, or context-freeze ADRs. |
| [write-journal-entry/SKILL.md](write-journal-entry/SKILL.md) | Capturing a chronological session, research pass, implementation pass, validation run, or user decision. |
| [write-lesson/SKILL.md](write-lesson/SKILL.md) | Capturing reusable learning, patterns, warnings, or failure modes. |
| [write-handoff/SKILL.md](write-handoff/SKILL.md) | Preparing a resume point, next-agent brief, stage transition, or constrained-agent handoff. |
| [maintain-agent-context/SKILL.md](maintain-agent-context/SKILL.md) | Updating compact context, startup instructions, registries, and cross-agent memory surfaces. |

Use these granular skills directly when the task is narrow. Use `project-memory-artifacts` or `project-coding-preferences` as umbrella skills when the task spans multiple artifact types.

Source proposal and rationale: [proposals/granular-agent-workflow-skills.md](proposals/granular-agent-workflow-skills.md).

## Mechanism Boundaries

Skills are best for reusable procedures and agent behavior.

Other mechanisms are better for durable state:

- `AGENT_CONTEXT.json` — compact current state and startup hints.
- `BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` — cross-agent startup contract.
- ADRs — accepted decisions and rejected alternatives.
- Journals — chronological point-in-time session memory.
- Lessons — reusable learning and patterns.
- Handoffs — resume points and next-agent instructions.
- Templates — stable document shapes when the output form matters more than the workflow.
