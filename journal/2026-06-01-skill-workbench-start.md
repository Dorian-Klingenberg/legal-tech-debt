# Journal - June 1, 2026: Skill Workbench Started

## Focus

Skill creation is now being treated as a repeatable project practice, similar to sandbox creation.

The goal is not to create private assistant memory. The goal is to create repo-visible skill workflows that Codex, GitHub Copilot, Claude Code, and future agents can all understand.

## What Changed

Added a top-level `skills/` workbench with:

- `skills/README.md` for the project skill model.
- `skills/SKILL-DEVELOPMENT.md` for lifecycle, validation, and cross-agent rules.
- `skills/registry.csv` for tracking proposed, draft, active, installed, and retired skills.
- `skills/templates/SKILL.md` for Codex-compatible skill drafts.
- `skills/templates/agents/openai.yaml` for optional Codex UI metadata.
- `skills/templates/skill-proposal.md` for early skill ideas.
- `skills/proposals/legal-rag-builder.md` as the first proposed skill.

Updated shared agent startup files so all agents know to read the skill workbench before creating or changing skills:

- `BOOTSTRAP.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`

## Current Decision

The repo remains the source of truth. Installable Codex skills should point back to repo docs and should not become the only place where durable project knowledge lives.

The first likely skill is `legal-rag-builder`, but it should not be drafted as an installable skill until the repo-level RAG ingestion and retrieval spec exists.

## Next Good Step

Create:

```text
sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md
```

Then derive the `legal-rag-builder` skill from that spec.

## Update

The next step was completed.

Created:

- `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- `skills/legal-rag-builder/SKILL.md`
- `skills/legal-rag-builder/agents/openai.yaml`

The registry now marks `legal-rag-builder` as `draft`, not installed. The original proposal and pasted source notes remain preserved at `skills/proposals/legal-rag-builder.md`.
