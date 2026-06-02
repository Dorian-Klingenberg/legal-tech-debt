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

The first project skill is `legal-rag-builder`: a workflow for building the local-first legal document ingestion and retrieval system for Sandbox 002 without drifting into chatbot-first design, naive chunking, or premature infrastructure.

Current artifacts:

- Draft skill: [legal-rag-builder/SKILL.md](legal-rag-builder/SKILL.md)
- Source proposal and raw notes: [proposals/legal-rag-builder.md](proposals/legal-rag-builder.md)
- Source-of-truth spec: [../sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md](../sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md)
- Architecture decisions: [legal-rag-builder/adr](legal-rag-builder/adr)
- Boundary lesson: [legal-rag-builder/references/rag-substrate-boundary-lesson.md](legal-rag-builder/references/rag-substrate-boundary-lesson.md)
- Docling/local stack boundary: [legal-rag-builder/references/docling-local-stack-boundary.md](legal-rag-builder/references/docling-local-stack-boundary.md)

Do not install the skill into `$CODEX_HOME/skills` until it has been validated against a real or dry-run Sandbox 002 RAG task.

The second project skill is `project-memory-artifacts`: a workflow for creating shared handoffs, journals, lessons, and agent context updates that Codex, GitHub Copilot, Claude Code, and future agents can all read.

Current artifacts:

- Draft skill: [project-memory-artifacts/SKILL.md](project-memory-artifacts/SKILL.md)
- Source proposal and raw notes: [proposals/project-memory-artifacts.md](proposals/project-memory-artifacts.md)
- Pattern reference: [project-memory-artifacts/references/grannies-memory-patterns.md](project-memory-artifacts/references/grannies-memory-patterns.md)

Do not install the skill into `$CODEX_HOME/skills` until it has been validated against a real journal, handoff, lesson, or agent-context update task.
