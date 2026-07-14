---
name: apply-implementation-defaults
description: Apply shared implementation defaults before coding, reviewing, refactoring, or choosing tooling in a sandbox, prototype, research, or proof-of-concept repository. Use when an agent needs to infer coding style, decide between small deterministic changes and infrastructure, preserve schema/provenance contracts, choose validation, or avoid broad refactors.
---

# Apply Implementation Defaults

## Startup

1. Read the repository entry instructions and any compact agent context file.
2. Inspect `git status --short` before edits.
3. Read the nearest stage, roadmap, ADR, or handoff that controls the task.
4. Identify the smallest changed surface that can satisfy the request.

## Defaults

- Prefer small, readable, deterministic implementation over clever abstractions.
- Prefer local scripts, plain data files, explicit configuration, and command-line probes in early research work.
- Extend existing file-local patterns before introducing new frameworks.
- Keep changes scoped to the active stage, feature, artifact, or review surface.
- Preserve IDs, timestamps, schema versions, provenance, and original source text when downstream work depends on artifacts.
- Add new schema fields, model fields, edge types, or public contracts only when a consumer or validation need exists.
- Separate raw evidence, candidate signals, findings, annotations, and final reports.
- Treat generated outputs as evidence of what happened, not as canonical truth unless the repo says so.

## Tooling Bias

- Choose the lightest reliable validation: a focused test, schema check, runner, report build, or diff inspection.
- Report concrete validation results: counts, run IDs, output paths, and what was not validated.
- Do not add infrastructure, services, databases, queues, deployment, or background automation unless an explicit decision record or stage evaluates that choice.
- Do not treat LLM output as verified truth when deterministic evidence or human review is required.

## Review Bias

- Prioritize behavioral bugs, broken contracts, false positives, missing validation, and untracked assumptions.
- Treat unrelated dirty-worktree changes as user or prior-agent work. Do not revert them.
- When a change affects shared memory or future work, update the appropriate handoff, journal, lesson, context, or index.

## Output

Summarize what changed, what was validated, what remains open, and which unrelated changes were left untouched.
