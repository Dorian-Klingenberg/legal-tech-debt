# Stage 001: Stack Concept And Artifact Contract

Status: Active
Started: 2026-06-05

## Purpose

Stage 001 defines the first-pass concept for an agentic SDLC project-manager stack.

The stage should answer:

- What artifacts make a task disciplined enough for agent implementation?
- How do sandbox experiments, prototype surprises, and failed probes become requirement candidates?
- How do experiments support validation and verification after implementation?
- What gates prevent agent speed from turning into documentation drift or unverified code?
- Which checks are deterministic, which are semantic, and which require human approval?
- What should a future project-manager dashboard read from the repo?

## Initial Architecture Hypothesis

The project-manager stack has seven cooperating layers:

1. **Conversation capture:** raw human/agent discussion, brainstorming, and open questions.
2. **Experiment capture:** sandbox runs, prototype behavior, failed probes, playtest observations, generated outputs, and surprising system behavior are recorded as evidence.
3. **Requirement promotion:** selected conversation or experiment evidence is promoted into a requirement candidate, risk, backlog item, ADR candidate, lesson, or task contract.
4. **Contract formation:** promoted work is turned into a task contract with scope, acceptance criteria, risks, file boundaries, and validation plan.
5. **Implementation control:** an agent works in an isolated branch/worktree with narrow file scope.
6. **Verification evidence:** the agent records tests, lint, schema checks, experimental probes, generated outputs, screenshots, reviewer notes, and unresolved risk.
7. **Status surface:** a generated dashboard summarizes current state from repo artifacts.

## Candidate Artifact Contract

Every implementation task should eventually have:

- task ID or backlog reference,
- owner or acting agent,
- objective,
- origin: conversation, experiment, backlog, ADR, external requirement, or mixed,
- source evidence path or conversation reference,
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
- experimental probes run,
- validation outputs or counts,
- generated artifacts,
- screenshots or report paths when visual output changed,
- risks accepted,
- known limitations,
- and next recommended action.

This can start as Markdown. Do not build a database until plain files fail.

## Experiment-To-Requirement Boundary

Experiments are allowed to be messy. Requirements should not be.

Use experiment capture for:

- sandbox probes,
- prototype behavior,
- failed runs,
- surprising outputs,
- playtest observations,
- corpus discovery,
- generated reports,
- screenshots or UI observations,
- and user reactions to experimental artifacts.

Promote experiment evidence into requirements only when it identifies durable behavior, a repeatable risk, a missing capability, a validation need, or a product/design constraint.

Do not promote every interesting surprise. Some surprises should become journal notes, lessons, risk records, or follow-up experiments instead.

When an experiment does become a requirement candidate, preserve:

- evidence path,
- observation summary,
- why it matters,
- affected system boundary,
- proposed requirement or task,
- validation idea,
- and human approval state.

## Experiment-Backed V&V Boundary

Experiments are not only a way to discover requirements. They are also a way to validate and verify them.

Use experiment-backed V&V when:

- deterministic tests pass but domain behavior still needs a probe,
- a prototype must be compared against real or expected system behavior,
- a simulation/playtest can reveal unintended consequences,
- a corpus probe can confirm whether a detector behaves across real sources,
- a generated report must be inspected for usefulness and failure modes,
- or a hypothesis needs to be falsified before it becomes a product claim.

V&V experiment records should preserve:

- requirement or task under test,
- experiment setup,
- expected behavior,
- observed behavior,
- pass/fail/ambiguous result,
- artifacts produced,
- domain interpretation,
- follow-up requirement, risk, or defect if the experiment surprises the team.

Do not treat a successful experiment as a substitute for ordinary validation gates. Treat it as additional domain evidence.

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
- regression-prone behavior that benefits from executable examples,
- experiment-derived behavior that has stabilized enough to become an acceptance example.

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
- experiment-backed V&V where domain behavior requires it,
- human approval,
- or source-traceable evidence.

## Stage 001 Checklist

- [x] Create initial Stage 001 document.
- [x] Sketch `task-contract.md` example.
- [x] Sketch experiment-to-requirement candidate fields.
- [x] Sketch `evidence-bundle.md` example.
- [x] Sketch experiment-backed V&V evidence fields.
- [x] Sketch `risk-register.md` fields.
- [x] Sketch `dashboard-read-model.md`.
- [x] Compare against existing `BACKLOG.md`, `AGENT_CONTEXT.json`, journals, handoffs, and ADRs for duplicate-truth risk.
- [ ] Decide whether Stage 002 should pilot a real backlog item.
