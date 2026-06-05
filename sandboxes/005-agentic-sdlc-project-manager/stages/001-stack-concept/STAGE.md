# Stage 001: Stack Concept And Artifact Contract

Status: Active
Started: 2026-06-05

## Purpose

Stage 001 defines the first-pass concept for an agentic SDLC project-manager stack.

The stage should answer:

- What artifacts make a task disciplined enough for agent implementation?
- What gates prevent agent speed from turning into documentation drift or unverified code?
- Which checks are deterministic, which are semantic, and which require human approval?
- What should a future project-manager dashboard read from the repo?

## Initial Architecture Hypothesis

The project-manager stack has five cooperating layers:

1. **Conversation capture:** raw human/agent discussion, brainstorming, and open questions.
2. **Contract formation:** a selected conversation is turned into a task contract with scope, acceptance criteria, risks, file boundaries, and validation plan.
3. **Implementation control:** an agent works in an isolated branch/worktree with narrow file scope.
4. **Verification evidence:** the agent records tests, lint, schema checks, generated outputs, screenshots, reviewer notes, and unresolved risk.
5. **Status surface:** a generated dashboard summarizes current state from repo artifacts.

## Candidate Artifact Contract

Every implementation task should eventually have:

- task ID or backlog reference,
- owner or acting agent,
- objective,
- scope and non-scope,
- allowed files or modules,
- requirements or acceptance criteria,
- Gherkin feature link when behavior warrants it,
- validation commands,
- expected evidence bundle,
- risk classification,
- human approval state,
- and handoff/journal update requirements.

## Candidate Evidence Bundle

An evidence bundle should include:

- task ID,
- implementation summary,
- changed files,
- tests run,
- validation outputs or counts,
- generated artifacts,
- screenshots or report paths when visual output changed,
- risks accepted,
- known limitations,
- and next recommended action.

This can start as Markdown. Do not build a database until plain files fail.

## Gate Model

Hard gates:

- repository startup rules followed,
- no unrelated user changes reverted,
- tests or validation appropriate to the change run,
- `git diff --check` clean for touched files,
- schema/golden/regression checks for artifact contract changes,
- human approval before phase transitions or external-facing claims.

Advisory gates:

- mutation testing,
- LLM-as-judge,
- broad refactor review,
- dashboard freshness checks.

Human-only gates:

- product claim approval,
- legal/compliance posture,
- procurement-risk acceptance,
- scope expansion,
- Phase A entry,
- external distribution.

## Gherkin Boundary

Use Gherkin for:

- user-visible product behavior,
- deterministic workflows,
- acceptance criteria that business/domain reviewers should read,
- regression-prone behavior that benefits from executable examples.

Do not require Gherkin for:

- ADRs,
- journals,
- handoffs,
- corpus procurement notes,
- research spikes,
- architecture exploration,
- documentation cleanup,
- or exploratory sandbox notes.

## LLM-As-Judge Boundary

LLM-as-judge may be useful for:

- semantic report quality,
- completeness against a rubric,
- whether a generated explanation answers a reviewer question,
- readability and audience fit,
- weak-signal triage.

LLM-as-judge must not replace:

- unit tests,
- schema checks,
- golden fixtures,
- deterministic parsing/detector validation,
- human approval,
- or source-traceable evidence.

## Stage 001 Checklist

- [x] Create initial Stage 001 document.
- [ ] Sketch `task-contract.md` example.
- [ ] Sketch `evidence-bundle.md` example.
- [ ] Sketch `risk-register.md` fields.
- [ ] Sketch `dashboard-read-model.md`.
- [ ] Compare against existing `BACKLOG.md`, `AGENT_CONTEXT.json`, journals, handoffs, and ADRs for duplicate-truth risk.
- [ ] Decide whether Stage 002 should pilot a real backlog item.

