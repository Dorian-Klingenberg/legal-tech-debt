# Skill Development Workflow

Status: Active guidance

Use this workflow when creating, updating, validating, or installing project skills.

## Principles

- Keep the repo as the source of truth. Codex skills, Claude instructions, and Copilot instructions should reference shared project docs rather than hiding durable knowledge in one tool.
- Keep skills lean. A skill should contain procedural guidance and pointers to the right project documents, not duplicate entire reports.
- Prefer deterministic project artifacts over broad agent prompts.
- Do not use skills to bypass the sandbox discipline. If a skill proposes implementation work, the work still needs a stage, lesson, and clear scope.
- Do not create production infrastructure just because a skill mentions a tool. Infrastructure still needs an explicit stage decision.

## Creation Steps

1. Identify the recurring workflow.
2. Write or confirm the repo-level source-of-truth spec.
3. Add or update a row in `skills/registry.csv`.
4. Draft the skill with `templates/SKILL.md`.
5. Add optional `agents/openai.yaml` metadata from `templates/agents/openai.yaml` if the skill may be installed for Codex.
6. Validate the draft against one real project task or a realistic dry run.
7. Mark the skill `active` only after it is clear, short, and useful.
8. If needed, install or mirror the skill into `$CODEX_HOME/skills`, then mark it `installed`.

## Required Skill Folder Shape

For a repo-visible skill:

```text
skills/
  skill-name/
    SKILL.md
    agents/
      openai.yaml
    references/
    scripts/
    assets/
```

Only create `references`, `scripts`, or `assets` when the skill actually needs them.

Avoid extra files inside an installable skill folder. Do not add local READMEs, changelogs, or broad notes inside a skill unless they are directly loaded as references by `SKILL.md`.

## Cross-Agent Rule

When a skill captures important project knowledge, update the shared docs too:

- `BOOTSTRAP.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- the relevant sandbox README or handoff

The goal is that Codex, GitHub Copilot, Claude Code, and future agents all start with the same project memory.

## Validation Checklist

Before calling a skill active:

- The `name` is lowercase hyphen-case and under 64 characters.
- The frontmatter has only `name` and `description`.
- The description clearly says when the skill should trigger.
- The body is short enough to load comfortably.
- The body points to repo source-of-truth docs instead of duplicating them.
- The skill says what not to do when that matters.
- Any scripts have been run at least once.
- Any generated or installed copy is traceable back to this repo.
- The registry row is current.

