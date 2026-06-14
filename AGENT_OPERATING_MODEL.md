# Agent Operating Model

This repository is used by Codex, Claude Code, and GitHub Copilot. They are different helpers, but they share one project memory and one source of truth.

## Purpose

Keep the three agents aligned on:

- what the current project state is,
- where durable memory lives,
- which agent is best suited for which kind of work,
- and how to avoid documentation drift.

## Shared Truth Sources

When there is a conflict, prefer current repo-visible records over historical notes. Within the same tier, prefer the newest explicitly current record.

1. `BOOTSTRAP.md`
2. `AGENT_CONTEXT.json`
3. The relevant agent entry file: `AGENTS.md`, `CLAUDE.md`, or `.github/copilot-instructions.md`
4. The current sandbox README, roadmap, ADRs, handoff, and closure docs
5. `BACKLOG.md`
6. The top-level `journal/` history

Journals are point-in-time session memory. They explain how the project got somewhere, but they do not override current context, handoffs, ADRs, closure docs, or backlog items unless a current document explicitly incorporates them.

Do not rely on private assistant memory when repo-visible memory exists.

## Agent Roles

### Codex

Best for:

- repo-wide audits and drift cleanup
- cross-file refactors and documentation alignment
- validation, consistency checks, and handoff repair
- stitching together the final project state

### Claude Code

Best for:

- focused implementation when given tight scope
- local reasoning over a constrained set of files
- edits that benefit from strong step-by-step follow-through

Claude Code must still obey the shared repo memory and the Claude constraint profile when active.

### GitHub Copilot

Best for:

- inline assistance while editing
- local suggestions and small completions
- lightweight code drafting inside the editor

Copilot should not be treated as the canonical memory holder for the project.

## Operating Rules

- For Claude Code, read `CLAUDE_CONSTRAINTS.md` before any exploration, file reads, planning, or edits.
- Then read `BOOTSTRAP.md`, `AGENT_CONTEXT.json`, `AGENT_OPERATING_MODEL.md`, and the relevant agent entry file.
- Read the relevant sandbox docs before touching a sandbox.
- Keep journals in the top-level `journal/` folder.
- Keep handoffs, lessons, ADRs, and closure docs near the sandbox or component they describe.
- Use ADRs for named architectural choices, not for routine plan updates.
- Put checklists in plans and roadmaps, including items that are already complete.
- Update journal, handoff, lesson, and context records at major pause points, scope changes, corpus changes, and stage transitions.
- Do not let any agent keep an undocumented private version of the truth.

## Drift Prevention

Before wrapping up a session, verify:

- the current lane is clear,
- the latest handoff points to the right next step,
- the journal records what changed and why,
- the backlog reflects any newly deferred work,
- and old docs are labeled historical if they are no longer current.

If a document is historical, mark it as historical or superseded so it cannot be mistaken for active guidance.

## Research and Sourcing Standards

This project is building toward a published academic paper on legal tech debt. All research must meet that bar from the start.

**Primary sources:** peer-reviewed academic papers, court records, regulatory filings, enforcement actions, published NAIC data, state insurance department decisions.

**Secondary sources only:** blog posts, news articles, Wikipedia, and accessible explainers may be referenced to help general readers orient, but must never serve as primary evidentiary backing for a claim.

**Synthetic examples:** all published examples illustrating code smells must be synthetic (purpose-built to exhibit the pattern). Real corpus analysis informs the taxonomy; real policy text is never published. The identities of the guilty parties have been protected.

If no academic source exists for a claim, flag the gap explicitly. Do not substitute an accessible source silently.
