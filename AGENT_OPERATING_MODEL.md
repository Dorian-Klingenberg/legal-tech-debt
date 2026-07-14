# Agent Operating Model

This repository is used by Codex, Claude Code, and GitHub Copilot. They are different helpers, but they share one project memory and one source of truth.

## Purpose

Keep the three agents aligned on:

- what the current project state is,
- where durable memory lives,
- which agent is best suited for which kind of work,
- and how to avoid documentation drift.

## Shared Truth Sources

Truth is type-specific. A newer historical note does not automatically override a current decision or status surface.

1. **Runtime rules:** `BOOTSTRAP.md`, the active tool entry file, and any tool-specific constraint profile.
2. **Current project state:** `README.md` and `AGENT_CONTEXT.json`.
3. **Accepted architecture:** accepted ADRs, including explicit supersession or correction notes.
4. **Sandbox state:** the sandbox README, stage plan, closure record, and latest explicitly current handoff.
5. **Work queue:** `BACKLOG.md` and the current stage document. A historical implementation brief does not reopen completed work.
6. **History and evidence:** journals, older handoffs, generated reports, external reports, and archived conversations.

Within the same type, prefer the newest record explicitly labeled current. Historical records explain how the project got somewhere, but they do not override current context, accepted ADRs, closure docs, or backlog state unless a current document explicitly incorporates them.

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

When recording counts, name the scope. Corpus inventory, an ingestion run, a filtered detector run, and a downstream historical snapshot are different measurements even when they refer to the same project.

If a document is historical, mark it as historical or superseded so it cannot be mistaken for active guidance.

## Research and Sourcing Standards

This project is building toward a published academic paper on legal tech debt. All research must meet that bar from the start.

**Primary sources:** peer-reviewed academic papers, court records, regulatory filings, enforcement actions, published NAIC data, state insurance department decisions.

**Secondary sources only:** blog posts, news articles, Wikipedia, and accessible explainers may be referenced to help general readers orient, but must never serve as primary evidentiary backing for a claim.

**Synthetic examples:** all published examples illustrating code smells must be synthetic (purpose-built to exhibit the pattern). Real corpus analysis informs the taxonomy; real policy text is never published. The identities of the guilty parties have been protected.

If no academic source exists for a claim, flag the gap explicitly. Do not substitute an accessible source silently.
