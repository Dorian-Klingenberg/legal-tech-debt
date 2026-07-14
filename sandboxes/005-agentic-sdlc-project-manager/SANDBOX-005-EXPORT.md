# Sandbox 005 — Agentic SDLC Project Manager: Full Context Export

> Historical export from 2026-06-10. It intentionally embeds then-current documents and may contain statuses superseded by later work. Do not update embedded copies to simulate current state; use `README.md`, `DOCUMENTATION-MAP.md`, and `HANDOFF-2026-07-13.md` in this sandbox.

**Exported from:** `legal-tech-debt` repository  
**Export date:** 2026-06-10  
**Sandbox status at export:** Active concept sandbox  
**Original path:** `sandboxes/005-agentic-sdlc-project-manager/`  
**Originating project:** Legal Tech Debt (insurance policy smell detection research)

---

## Purpose of This Document

This document collects every piece of project context related to Sandbox 005 — the Agentic SDLC Project Manager — from across the `legal-tech-debt` repository. It is intended to stand alone and bootstrap a new repository focused on this concept.

The document includes:

- The sandbox README, stage plan, and Stage 001 design
- All artifact template sketches from Stage 001
- The architectural decision (ADR-012) that separates the SDLC stack from the product runtime
- The SDLC/agentic product stack separation planning note
- Session journal entries covering all Sandbox 005 work
- Cross-repository context explaining how the project arrived here

---

## Table of Contents

1. [Origin and Motivation](#1-origin-and-motivation)
2. [Sandbox 005 README](#2-sandbox-005-readme)
3. [Stage Plan (5 Stages)](#3-stage-plan)
4. [Stage 001: Stack Concept and Artifact Contract](#4-stage-001-stack-concept-and-artifact-contract)
5. [Artifact Templates](#5-artifact-templates)
   - [Task Contract](#51-task-contract)
   - [Experiment-to-Requirement Candidate](#52-experiment-to-requirement-candidate)
   - [Evidence Bundle](#53-evidence-bundle)
   - [Experiment-Backed V&V Evidence](#54-experiment-backed-vv-evidence)
   - [Risk Register](#55-risk-register)
   - [Dashboard Read Model](#56-dashboard-read-model)
6. [Architecture Decision: SDLC vs. Product Stack Separation](#6-architecture-decision-sdlc-vs-product-stack-separation)
7. [SDLC and Agentic Product Stack Separation Planning Note](#7-sdlc-and-agentic-product-stack-separation-planning-note)
8. [Session History](#8-session-history)
9. [Backlog and Cross-Reference Notes](#9-backlog-and-cross-reference-notes)
10. [Positioning and Framing Notes](#10-positioning-and-framing-notes)

---

## 1. Origin and Motivation

Sandbox 005 was created on 2026-06-05, promoted from a backlog item (`BACKLOG-005: Phase A Entry — Agile V Framework Integration and SE Stack`). The item was closed as a standalone backlog entry and elevated to an active experiment sandbox because the scope was too rich for a single backlog item.

The triggering context: the `legal-tech-debt` project was moving from exploratory sandbox research toward a more disciplined Phase A engineering posture. The owner wanted to design the development SDLC stack before implementing it — specifically a repo-native project manager that integrates:

- Agile iteration
- V-model verification and validation (Agile V)
- Gherkin/BDD acceptance specifications where useful
- SwarmForge-style multi-agent coordination (worktrees, role prompts, file allowlists)
- Uncle Bob / Clean AI engineering discipline
- Risk-adaptive testing
- LLM-as-judge as a semantic sensor only

The project also runs multiple AI assistants in parallel — Codex, Claude Code, GitHub Copilot — on the same repository. The SDLC stack must be visible to all of them, not locked in any one assistant's private memory.

A key architectural decision was made concurrently (ADR-012): the development SDLC stack and the agentic product runtime stack must stay explicitly separate. The SDLC stack governs how the product is built. The product stack is what gets built.

On 2026-06-07, the sandbox was updated to formally model **experiment-driven requirements** — the recognition that in this project (and in AI-assisted development generally), requirements are not only written in advance through discussion; they are also *discovered* through sandbox probes, failed experiments, prototype behavior, and surprising generated outputs.

---

## 2. Sandbox 005 README

*Source: `sandboxes/005-agentic-sdlc-project-manager/README.md`*

---

### Sandbox 005: Agentic SDLC Project Manager

Status: Active concept sandbox  
Started: 2026-06-05  
Scope: Development SDLC stack, agent coordination, Agile V control surface

#### Purpose

This sandbox explores the development-side project manager for Legal Tech Debt: a repo-native SDLC control system that turns human/agent conversation and experiment evidence into requirements, implementation slices, verification evidence, risk records, and human-approved progress.

This is the SDLC stack, not the agentic product runtime stack. See ADR-012 in Section 6 and the separation planning note in Section 7.

Working thesis:

> Build a project manager that treats the repository as the source of truth. The project manager reads and writes disciplined artifacts, coordinates agents, tracks verification evidence, and makes project state visible without becoming a second competing planning universe.

#### Why This Exists

The project is moving from exploratory sandbox work toward a more disciplined Phase A posture. The owner wants to combine:

- Agile iteration,
- V-model verification and validation,
- Gherkin/BDD acceptance specifications where useful,
- SwarmForge-style multi-agent coordination,
- Uncle Bob / Clean AI engineering discipline,
- risk-adaptive testing,
- and LLM-as-judge for semantic review only where deterministic checks are insufficient.

The goal is not to adopt a generic dashboard template. The goal is to design a stack that can become a practical project-manager layer for this repo and, later, for the product engineering lifecycle.

#### Scope

In scope:

- SDLC artifact model: goals, requirements, Gherkin specs, tasks, risks, ADRs, verification evidence, handoffs, journals, and release decisions.
- Agent role model: planner/specifier, implementer, reviewer/verifier, researcher, release/handoff coordinator.
- Work isolation model: branches, worktrees, file allowlists, dirty-worktree protection, and agent handoff rules.
- Verification model: deterministic tests first, schema/golden/regression evidence, risk-adaptive mutation testing, experiment-backed V&V, and optional LLM review.
- Project-manager control surface: dashboard/report generated from repo truth.
- Conversation-to-contract gate: when exploratory chat becomes actionable work.
- Experiment-to-requirement gate: when sandbox observations, failed probes, surprising outputs, or prototype behavior become requirements, risks, or backlog items.

Out of scope:

- Product runtime agents that analyze legal documents for customers.
- Customer-data permissions, tenant memory, production agent audit logs, or product runtime architecture.
- Replacing `BOOTSTRAP.md`, `AGENT_CONTEXT.json`, `AGENT_OPERATING_MODEL.md`, or agent-specific startup files.
- Mandating Gherkin for research notes, ADRs, corpus procurement, documentation cleanup, or exploratory spikes.
- Treating LLM-as-judge as a hard correctness oracle.

#### Design Principles

- **Repo truth first.** Dashboards summarize canonical files; they do not become canonical.
- **Conversation and experimentation before contract.** Exploration is allowed, and requirements may be discovered through sandbox runs, prototypes, playtests, corpus probes, or failed experiments. Implementation starts only after the discovered work has a clear artifact contract.
- **Verification is risk-adaptive.** Unit tests and fixtures are common; mutation testing and LLM judges are used when the risk justifies them.
- **Experimentation supports both sides of the V.** Experiments can discover requirements before implementation and can validate/verify whether built behavior matches real domain expectations after implementation.
- **Agents leave evidence.** Every substantive agent run should leave a readable trail: what changed, why, what was validated, and what remains uncertain.
- **Experiments leave requirements candidates.** A surprising sandbox result should be captured as evidence first, then promoted deliberately into a requirement, risk, backlog item, ADR, or lesson when it proves durable.
- **Gherkin is for behavior.** Use it when acceptance behavior benefits from executable specification, not as universal paperwork.
- **Swarm discipline can be adopted incrementally.** Start with roles, work isolation, and prompts before depending on any one orchestration tool.

#### Candidate Stack

| Layer | Candidate Tools / Artifacts | Notes |
|---|---|---|
| Source of truth | Git, Markdown, JSON/JSONL, ADRs, backlog, journals, handoffs | Existing repo pattern; preserve it. |
| Experiment evidence | Sandbox outputs, playtest notes, probe results, failed runs, screenshots, generated reports | Requirements can be discovered by experiment, not only written before implementation. |
| Requirements | `requirements/`, `features/`, traceability records | Design in this sandbox before creating globally. |
| BDD | Gherkin, `pytest-bdd` or `behave` for Python slices | Use for product behavior and acceptance tests. |
| Tests | `pytest`, golden fixtures, schema validation, regression snapshots | Default hard gate. |
| Static checks | `ruff`, optional `mypy`, future `eslint`/`tsc` if TypeScript appears | Match actual implementation languages. |
| Mutation | `mutmut` for Python, later equivalents if needed | Risk-adaptive, not default ceremony. |
| Agent orchestration | SwarmForge-style worktrees and role prompts | Evaluate before adopting. |
| Semantic review | LLM-as-judge rubrics for report quality, semantic completeness, reviewer usefulness | Sensor only; not final authority. |
| Dashboard | Generated Markdown/HTML/JSON status view over repo artifacts | No separate planning database at first. |

#### Starting Questions

- What is the minimum artifact contract for a disciplined implementation slice?
- How should experiment observations become requirement candidates without turning every surprise into scope creep?
- What work requires Gherkin, and what work should stay in Markdown task/ADR/risk form?
- What is the smallest useful traceability model from requirement to test to evidence?
- What agent roles are actually useful for this repo, and which create coordination overhead?
- What should count as an evidence bundle?
- What gates should be hard, advisory, or human-only?
- What should the project-manager dashboard read, and what should it be forbidden to edit?

#### Future Sibling Concept

A likely future sandbox or project should explore the agentic product runtime stack: product agents, legal evidence processing, customer-data boundaries, runtime audit logs, and product-agent permissions. That is deliberately not started here.

#### References

- SwarmForge: `https://github.com/unclebob/swarm-forge`
- Cucumber/Gherkin reference: `https://cucumber.io/docs/gherkin/reference`
- IEEE 1012 V&V overview: `https://standards.ieee.org/ieee/1012/7324/`
- CMU SEI V-model testing discussion: `https://www.sei.cmu.edu/blog/using-v-models-for-testing/`
- Clean AI course overview: `https://www.oreilly.com/videos/clean-ai-agentic/9780135968819/`

---

## 3. Stage Plan

*Source: `sandboxes/005-agentic-sdlc-project-manager/STAGE-PLAN.md`*  
*Last updated: 2026-06-07*

---

### Stage 001: Stack Concept and Artifact Contract

**Status: Active**

Purpose: Define the first-pass SDLC stack, artifact model, gate model, and agent role model.

The stage should produce a disciplined operating model before any dashboard or orchestration implementation is attempted. The model must support requirements discovered through conversation and through experimentation, including sandbox probes, prototype behavior, failed runs, surprising outputs, and playtest-style observations. It must also treat experimentation as a validation and verification method in the V-model sense.

Checklist:

- [x] Create Sandbox 005.
- [x] Separate SDLC stack exploration from agentic product runtime exploration.
- [x] Record initial candidate stack layers.
- [x] Define the minimum disciplined task contract.
- [x] Define how experiment observations become requirement candidates.
- [x] Define an evidence bundle format.
- [x] Define how experiments support V&V evidence, not only requirements discovery.
- [x] Define which work types require Gherkin and which do not.
- [x] Define hard gates, advisory gates, and human-only gates.
- [ ] Define the first agent role set.
- [x] Define the project-manager dashboard read model.
- [x] Identify existing repo artifacts the dashboard should ingest.
- [x] Identify artifact conflicts or duplicate truth risks.
- [ ] Produce a Stage 001 decision note or ADR candidate if the stack direction hardens.

Expected outputs:

- `stages/001-stack-concept/STAGE.md`
- Optional artifact sketches under `stages/001-stack-concept/examples/`
- Follow-up ADR only if a durable architecture decision is made.

---

### Stage 002: Manual Pilot on One Real Backlog Item

**Status: Planned**

Purpose: Run the proposed SDLC stack manually on one small backlog item before building tooling.

Checklist:

- [ ] Select one low-to-medium risk backlog item.
- [ ] Write the task contract.
- [ ] Identify whether the task came from conversation, experiment evidence, or both.
- [ ] Write Gherkin only if the selected item has behavior worth specifying.
- [ ] Produce implementation evidence bundle.
- [ ] Run validation appropriate to the risk.
- [ ] Identify whether any experimental probe is needed for validation or verification.
- [ ] Capture human review outcome.
- [ ] Record friction, ambiguity, and missing artifact fields.
- [ ] Update the artifact contract based on the pilot.
- [ ] During Stage 002, pilot at least one task whose origin is experiment evidence.

**Gate:** Do not build a dashboard before completing at least one manual pilot.

---

### Stage 003: Generated Status Surface

**Status: Planned**

Purpose: Generate a simple status view from repo truth.

Checklist:

- [ ] Decide the first status output format: Markdown, HTML, JSON, or all three.
- [ ] Read existing artifacts rather than creating a new planning database.
- [ ] Show active lane, open risks, open decisions, latest validation, and stale handoffs.
- [ ] Show traceability from experiment or conversation to requirement to task to verification evidence.
- [ ] Mark missing evidence explicitly.
- [ ] Keep output generated and disposable.

**Gate:** The generated surface must not become canonical truth.

---

### Stage 004: Agent Role and Worktree Experiment

**Status: Planned**

Purpose: Evaluate whether SwarmForge-style orchestration improves actual work in this repo.

Checklist:

- [ ] Define minimal role prompts: planner, implementer, reviewer.
- [ ] Define file allowlist expectations per role.
- [ ] Define branch/worktree naming rules.
- [ ] Run a small coordinated task with separate worktrees.
- [ ] Measure whether the coordination helped or added overhead.
- [ ] Decide whether to adopt SwarmForge, borrow its pattern, or stay with simpler manual coordination.

**Gate:** Do not adopt a multi-agent orchestration tool until the manual role model is useful.

---

### Stage 005: Phase A Integration Plan

**Status: Planned**

Purpose: Convert sandbox findings into a Phase A-ready SDLC stack plan.

Checklist:

- [ ] Produce SDLC stack concept of operations.
- [ ] Define SDLC requirements categories.
- [ ] Define traceability model.
- [ ] Define verification evidence model.
- [ ] Define agent governance model.
- [ ] Define dashboard/control-surface role.
- [ ] Identify ADRs needed for accepted stack choices.
- [ ] Close or carry forward Sandbox 005.

---

## 4. Stage 001: Stack Concept and Artifact Contract

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/STAGE.md`*

---

### Initial Architecture Hypothesis

The project-manager stack has seven cooperating layers:

1. **Conversation capture:** raw human/agent discussion, brainstorming, and open questions.
2. **Experiment capture:** sandbox runs, prototype behavior, failed probes, playtest observations, generated outputs, and surprising system behavior are recorded as evidence.
3. **Requirement promotion:** selected conversation or experiment evidence is promoted into a requirement candidate, risk, backlog item, ADR candidate, lesson, or task contract.
4. **Contract formation:** promoted work is turned into a task contract with scope, acceptance criteria, risks, file boundaries, and validation plan.
5. **Implementation control:** an agent works in an isolated branch/worktree with narrow file scope.
6. **Verification evidence:** the agent records tests, lint, schema checks, experimental probes, generated outputs, screenshots, reviewer notes, and unresolved risk.
7. **Status surface:** a generated dashboard summarizes current state from repo artifacts.

### Candidate Artifact Contract

Every implementation task should eventually have:

- task ID or backlog reference
- owner or acting agent
- objective
- origin: conversation, experiment, backlog, ADR, external requirement, or mixed
- source evidence path or conversation reference
- scope and non-scope
- allowed files or modules
- requirements or acceptance criteria
- Gherkin feature link when behavior warrants it
- validation commands
- expected evidence bundle
- risk classification
- human approval state
- handoff/journal update requirements

### Candidate Evidence Bundle

An evidence bundle should include:

- task ID
- implementation summary
- changed files
- tests run
- experimental probes run
- validation outputs or counts
- generated artifacts
- screenshots or report paths when visual output changed
- risks accepted
- known limitations
- next recommended action

This can start as Markdown. Do not build a database until plain files fail.

### Experiment-To-Requirement Boundary

Experiments are allowed to be messy. Requirements should not be.

Use experiment capture for:

- sandbox probes
- prototype behavior
- failed runs
- surprising outputs
- playtest observations
- corpus discovery
- generated reports
- screenshots or UI observations
- user reactions to experimental artifacts

Promote experiment evidence into requirements only when it identifies durable behavior, a repeatable risk, a missing capability, a validation need, or a product/design constraint.

Do not promote every interesting surprise. Some surprises should become journal notes, lessons, risk records, or follow-up experiments instead.

When an experiment does become a requirement candidate, preserve:

- evidence path
- observation summary
- why it matters
- affected system boundary
- proposed requirement or task
- validation idea
- human approval state

### Experiment-Backed V&V Boundary

Experiments are not only a way to discover requirements. They are also a way to validate and verify them.

Use experiment-backed V&V when:

- deterministic tests pass but domain behavior still needs a probe
- a prototype must be compared against real or expected system behavior
- a simulation/playtest can reveal unintended consequences
- a corpus probe can confirm whether a detector behaves across real sources
- a generated report must be inspected for usefulness and failure modes
- a hypothesis needs to be falsified before it becomes a product claim

V&V experiment records should preserve:

- requirement or task under test
- experiment setup
- expected behavior
- observed behavior
- pass/fail/ambiguous result
- artifacts produced
- domain interpretation
- follow-up requirement, risk, or defect if the experiment surprises the team

Do not treat a successful experiment as a substitute for ordinary validation gates. Treat it as additional domain evidence.

### Gate Model

**Hard gates:**

- repository startup rules followed
- no unrelated user changes reverted
- tests or validation appropriate to the change run
- `git diff --check` clean for touched files
- schema/golden/regression checks for artifact contract changes
- human approval before phase transitions or external-facing claims

**Advisory gates:**

- mutation testing
- LLM-as-judge
- broad refactor review
- dashboard freshness checks

**Human-only gates:**

- product claim approval
- legal/compliance posture
- procurement-risk acceptance
- scope expansion
- Phase A entry
- external distribution

### Gherkin Boundary

Use Gherkin for:

- user-visible product behavior
- deterministic workflows
- acceptance criteria that business/domain reviewers should read
- regression-prone behavior that benefits from executable examples
- experiment-derived behavior that has stabilized enough to become an acceptance example

Do not require Gherkin for:

- ADRs
- journals
- handoffs
- corpus procurement notes
- research spikes
- architecture exploration
- documentation cleanup
- exploratory sandbox notes

### LLM-As-Judge Boundary

LLM-as-judge may be useful for:

- semantic report quality
- completeness against a rubric
- whether a generated explanation answers a reviewer question
- readability and audience fit
- weak-signal triage

LLM-as-judge must not replace:

- unit tests
- schema checks
- golden fixtures
- deterministic parsing/detector validation
- experiment-backed V&V where domain behavior requires it
- human approval
- source-traceable evidence

### Stage 001 Checklist

- [x] Create initial Stage 001 document.
- [x] Sketch `task-contract.md` example.
- [x] Sketch experiment-to-requirement candidate fields.
- [x] Sketch `evidence-bundle.md` example.
- [x] Sketch experiment-backed V&V evidence fields.
- [x] Sketch `risk-register.md` fields.
- [x] Sketch `dashboard-read-model.md`.
- [x] Compare against existing `BACKLOG.md`, `AGENT_CONTEXT.json`, journals, handoffs, and ADRs for duplicate-truth risk.
- [ ] Decide whether Stage 002 should pilot a real backlog item.

---

## 5. Artifact Templates

### 5.1 Task Contract

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/task-contract.md`*

Purpose: define the minimum fields needed before an agent starts implementation.

```yaml
task_id: BACKLOG-000
title: Short imperative title
owner_or_agent: Codex | Claude Code | GitHub Copilot | human | mixed
origin: conversation | experiment | backlog | ADR | external_requirement | mixed
source_evidence:
  - path_or_reference: path/to/source.md
    note: Why this source matters
objective: >
  One paragraph describing what should be true when the task is complete.
scope:
  in:
    - File, module, behavior, or artifact in scope
  out:
    - Explicit non-goal
allowed_files:
  - path/or/glob
requirements_or_acceptance:
  - Requirement or acceptance criterion
gherkin_feature: path/to/feature.feature | none
risk_class: low | medium | high
validation_plan:
  deterministic:
    - command or check
  experimental:
    - probe or scenario, if needed
  semantic:
    - LLM-as-judge rubric, if justified
expected_evidence_bundle: path/to/evidence-bundle.md
human_approval:
  required: true | false
  reason: Why human approval is or is not needed
handoff_or_journal_required: true | false
```

**Notes:**

- `origin` is mandatory so the control surface can distinguish conversation-driven tasks from experiment-derived work.
- `source_evidence` should point to the conversation summary, journal, sandbox output, generated report, failing run, screenshot, or external requirement that justifies the task.
- Experimental validation is optional. Use it when tests alone cannot show domain behavior.

---

### 5.2 Experiment-to-Requirement Candidate

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/experiment-requirement-candidate.md`*

Purpose: capture a surprising or durable experiment observation before deciding whether it becomes a requirement, risk, backlog item, ADR candidate, lesson, or follow-up experiment.

```yaml
candidate_id: EXPREQ-000
source_experiment:
  path: path/to/experiment-or-output
  run_id: optional-run-id
  observed_at: 2026-06-07T00:00:00-04:00
observation_summary: >
  What happened in the experiment, prototype, playtest, corpus probe, generated
  report, or failed run?
why_it_matters: >
  Why is the observation durable enough to consider for project control?
affected_boundary:
  - product_behavior
  - SDLC_tooling
  - agent_runtime
  - evidence_substrate
  - UX
  - documentation
promotion_decision: requirement | risk | backlog_item | ADR_candidate | lesson | follow_up_experiment | no_promotion_yet
proposed_requirement_or_task: >
  If promoted, state the requirement or task in testable language.
validation_idea: >
  How would we confirm that the promoted requirement is satisfied?
risk_if_ignored: low | medium | high
human_approval_state: proposed | approved | rejected | needs_more_evidence
```

**Promotion Rule:** Promote experiment evidence only when it identifies durable behavior, a repeatable risk, a missing capability, a validation need, or a product/design constraint. Do not promote every interesting surprise. Some surprises should stay as journal notes, lessons, risk records, or follow-up experiments.

---

### 5.3 Evidence Bundle

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/evidence-bundle.md`*

Purpose: record what changed, what was validated, what evidence was produced, and what remains uncertain after a task.

```yaml
task_id: BACKLOG-000
title: Task title
completed_by: Codex | Claude Code | GitHub Copilot | human | mixed
completed_at: 2026-06-07T00:00:00-04:00
implementation_summary: >
  Concise summary of what changed.
changed_files:
  - path/to/file
tests_run:
  - command: pytest path/to/tests
    result: pass | fail | not_run
    notes: concrete counts or reason not run
validation_outputs:
  - path: path/to/output
    description: What this output proves or fails to prove
experimental_probes_run:
  - probe_id: optional
    path: path/to/experiment-vv-evidence.md
    result: pass | fail | ambiguous | not_run
generated_artifacts:
  - path/to/artifact
screenshots_or_visual_checks:
  - path/to/screenshot-or-report
risks_accepted:
  - risk_id: optional
    note: Accepted risk and owner approval, if any
known_limitations:
  - limitation
next_recommended_action:
  - action
human_approval_state: not_required | pending | approved | rejected
```

**Notes:** Evidence bundles are task-local records, not canonical project truth. Generated dashboards should read evidence bundles, but dashboards must not replace them. If validation was not run, the bundle should say why.

---

### 5.4 Experiment-Backed V&V Evidence

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/experiment-vv-evidence.md`*

Purpose: record experimental validation or verification evidence when tests alone cannot show whether the implemented behavior satisfies the domain need.

```yaml
vv_id: EXPVV-000
requirement_or_task_under_test: BACKLOG-000 | REQ-000 | task-contract-path
experiment_type: sandbox_probe | corpus_probe | simulation | playtest | generated_report_review | UI_probe | benchmark | other
source_context:
  - path: path/to/requirement-or-task
  - path: path/to/experiment-setup
setup: >
  What was run, generated, simulated, reviewed, or observed?
expected_behavior: >
  What should happen if the requirement or implementation is valid?
observed_behavior: >
  What actually happened?
result: pass | fail | ambiguous
artifacts_produced:
  - path/to/output
domain_interpretation: >
  What does the result mean in project/domain terms?
surprises:
  - surprise or none
follow_up:
  requirement_candidate: path/to/experiment-requirement-candidate.md | none
  risk: risk-id | none
  defect: issue-or-backlog-id | none
  lesson: path/to/lesson.md | none
human_review_state: proposed | accepted | rejected | needs_more_evidence
```

**Use when:**

- Deterministic checks pass but the behavior still needs domain proof.
- A simulation/playtest can reveal unintended consequences.
- A corpus probe can show whether a detector generalizes across real sources.
- A generated report must be judged for usefulness and failure modes.
- A hypothesis must be falsified before it becomes a product claim.

---

### 5.5 Risk Register

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/risk-register.md`*

Purpose: track risks discovered through conversation, implementation, experiments, validation, and review.

| Risk ID | Source | Description | Impact | Likelihood | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| RISK-000 | conversation | Example risk | low / medium / high | low / medium / high | Planned mitigation | owner | open / accepted / closed |

**Source values:** conversation, experiment, implementation, validation, review, external_requirement, backlog, ADR

**Rules:**

- Risks should reference source evidence when possible.
- Accepted risks need human approval when they affect product claims, legal/compliance posture, phase transitions, or external distribution.
- Generated dashboards may summarize risks, but this register or the canonical backlog/ADR/journal source remains the durable record.

---

### 5.6 Dashboard Read Model

*Source: `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/dashboard-read-model.md`*

Purpose: define what a future generated status surface may read from repo truth and what it must not own.

**Allowed Inputs:**

| Source | What To Read | Notes |
|---|---|---|
| `AGENT_CONTEXT.json` | compact current focus, active lanes, latest handoff/journal pointers | Read-only summary, not full truth. |
| `BACKLOG.md` | backlog items, open questions, deferred work | Respect current backlog semantics. |
| ADRs | accepted decisions and rejected alternatives | Prefer newer/current ADRs over historical notes. |
| top-level `journal/` | chronological session evidence | Point-in-time memory; does not override current docs. |
| sandbox handoffs | resume instructions and local state | Scope-specific. |
| task contracts | scoped work waiting for implementation | Future artifact. |
| evidence bundles | validation and implementation evidence | Future artifact. |
| experiment requirement candidates | promoted or pending experiment observations | Future artifact. |
| experiment-backed V&V records | domain validation/verification evidence | Future artifact. |
| risk register | open/accepted/closed risks | Future artifact or existing backlog equivalents. |

**Must Show:**

- active lane and active sandbox
- open task contracts
- latest validation evidence
- experiment-derived requirement candidates
- experiment-backed V&V records
- open risks and accepted risks
- stale handoffs or stale context pointers
- missing evidence explicitly
- trace from conversation/experiment to requirement to task to verification evidence when available

**Forbidden To Own:**

- canonical project scope
- backlog truth
- ADR decisions
- human approval decisions
- source corpus truth
- product runtime memory
- private assistant memory

**Duplicate-Truth Risks:**

- A dashboard status field could drift from `AGENT_CONTEXT.json`.
- Generated summaries could look more authoritative than ADRs or handoffs.
- Task state could be split between backlog, task contract, evidence bundle, and dashboard.
- Experiment observations could become requirements without human promotion.

**Guardrail:** The dashboard must be disposable. If deleting generated dashboard output loses project truth, the design is wrong.

---

## 6. Architecture Decision: SDLC vs. Product Stack Separation

*Source: `ADR-012-separate-sdlc-stack-from-agentic-product-stack.md`*  
*Date: 2026-06-05 | Status: Accepted*

---

### Context

The project uses multiple AI assistants during development, including Codex, Claude Code, and GitHub Copilot. The eventual product may also include agentic runtime components that ingest documents, retrieve evidence, run analysis, draft reports, or assist human reviewers.

Those are different systems.

The development SDLC stack is the engineering and governance environment used to create the product. The agentic product stack is part of the delivered product. If they are blurred together, the project risks confusing development convenience with product architecture, private assistant memory with product memory, and repository permissions with runtime permissions.

### Decision

Keep the development SDLC stack and the agentic product stack explicitly separate.

The accepted principle is:

> The SDLC stack builds and governs the product. The agentic stack is part of the product being governed.

### Consequences

- Product-agent architecture must not rely on Codex, Claude, Copilot, or chat-session private memory.
- Product-agent memory must live in product artifacts such as corpus records, nodes, edges, candidate evidence, findings, reviewer decisions, reports, and audit logs.
- Development memory must remain repo-visible in startup docs, backlog, ADRs, journals, handoffs, and context files.
- SDLC requirements and product requirements must be written separately.
- SDLC validation and product validation must be measured separately.
- Runtime product agents need narrower permissions than development agents.
- Phase A should include separate concept-of-operations and requirements work for SDLC tooling and product agent runtime.

### Rejected Alternatives

**Treat all agent usage as one shared agent stack** — Rejected because development assistants and product agents have different users, permissions, memory, audit requirements, and failure modes.

**Let development agent practices become product architecture by default** — Rejected because repository workflow shortcuts are not necessarily acceptable runtime product behavior, especially for customer data, legal review, and auditability.

**Defer the distinction until implementation** — Rejected because Phase A will need clear requirements boundaries. Recording the separation now prevents early planning artifacts from mixing SDLC governance with product runtime design.

### Follow-Up Checklist

- [ ] Create an SDLC stack plan during Phase A.
- [ ] Create an agentic product runtime stack plan during Phase A.
- [ ] Decide whether project-level ADRs should move into a root `adr/` directory.
- [ ] Define product-agent permission, memory, and audit-log requirements.
- [ ] Define development-agent permission and handoff requirements.
- [ ] Keep SDLC requirements separate from product runtime requirements.
- [ ] Keep SDLC validation separate from product behavior validation.

---

## 7. SDLC and Agentic Product Stack Separation Planning Note

*Source: `SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md`*  
*Date: 2026-06-05 | Status: Planning note*

---

### Purpose

The project will eventually have two different technology stacks:

- **Development SDLC stack:** the engineering system used to plan, build, test, trace, release, govern, and maintain the product.
- **Agentic product stack:** the runtime system inside the product that ingests documents, retrieves evidence, runs detectors, drafts reports, and assists reviewers.

Core principle:

> The SDLC stack builds and governs the product. The agentic stack is part of the product being governed.

### Separation Rules

**1. Separate Architecture Surfaces**

Keep separate architecture records for:
- product architecture
- agent runtime architecture
- SDLC/tooling architecture
- data/evidence architecture
- security/compliance architecture

Do not let "we use agents while developing" imply that those development agents are part of the product runtime.

**2. Separate Requirements**

Product requirements describe what the delivered product must do for users:
- Every finding must include source text and provenance.
- Reviewer reports must distinguish candidate evidence from legal conclusions.
- Product agents must not leak customer corpus data across tenants.

SDLC requirements describe how the engineering process must produce trustworthy software:
- Detector changes must run regression validation on preserved corpus runs.
- Requirements must trace to Gherkin scenarios and test evidence during Phase A.
- Release candidates must pass schema, provenance, and report-render validation gates.

**3. Separate Validation**

Product validation asks whether the product behavior is useful, traceable, and safe:
- false positive / false negative review
- finding provenance review
- reviewer usefulness
- report correctness
- source traceability

SDLC validation asks whether engineering controls were followed:
- unit and integration tests
- schema validation
- CI gates
- requirements traceability
- release readiness checks
- auditability of changes

**4. Separate Agent Roles**

Development agents help build the system: Codex, Claude Code, GitHub Copilot.

Product agents are product components: ingestion assistant, retrieval assistant, reviewer assistant, report drafter, workflow assistant.

Development agents may have repository access. Product agents should have constrained runtime permissions, explicit memory boundaries, logged tool calls, and customer-data isolation.

**5. Separate Memory**

Development memory lives in repo-visible project records: `BOOTSTRAP.md`, `AGENT_CONTEXT.json`, `AGENT_OPERATING_MODEL.md`, `BACKLOG.md`, ADRs, handoffs, top-level `journal/`.

Product memory lives in product artifacts: source corpus records, parser runs, nodes and edges, candidate evidence, detector findings, reviewer decisions, report drafts, product audit logs.

Product behavior must never depend on private Codex, Claude, Copilot, or chat-session memory.

**6. Separate Permissions**

Development agents can be granted repository permissions appropriate to the current task.

Product agents should default to narrow runtime permissions:
- read approved tenant corpus
- write structured product artifacts
- call approved retrieval and analysis tools
- log evidence and decisions
- avoid arbitrary filesystem access
- avoid unapproved external network calls
- avoid cross-tenant memory

**7. Separate ADR Streams or Tags**

During Phase A, use either separate ADR folders or explicit ADR scope tags.

Possible folders: `adr/sdlc/`, `adr/product/`, `adr/agent-runtime/`, `adr/data-evidence/`, `adr/security/`

Possible scope tags: `Scope: SDLC`, `Scope: Product Agent Runtime`, `Scope: Evidence Substrate`, `Scope: Security / Governance`

### Phase A Implications

Phase A should explicitly define:
- SDLC stack concept of operations
- product agent runtime concept of operations
- requirements traceability model
- Gherkin/BDD acceptance criteria strategy
- product evidence and audit-log model
- agent permission and memory model
- release and validation gates

### Checklist

- [ ] Decide whether root ADRs should live in `adr/` folders or use root-level project ADR files.
- [ ] Draft SDLC stack plan.
- [ ] Draft product agent runtime stack plan.
- [ ] Define requirements categories: product, SDLC, data/evidence, security, agent runtime.
- [ ] Define traceability between requirements, Gherkin scenarios, tests, and evidence artifacts.
- [ ] Define product-agent permission model.
- [ ] Define development-agent permission model.
- [ ] Define audit-log requirements for product agent actions.
- [ ] Define customer/tenant memory boundaries for product runtime.

---

## 8. Session History

### 2026-06-05: Sandbox 005 Created

*Source: `journal/2026-06-05-sandbox-005-agentic-sdlc-project-manager.md`*

Opened Sandbox 005 to explore the development SDLC/project-manager stack. The concept is a repo-native project manager that turns conversation into task contracts, task contracts into implementation slices, implementation into verification evidence, and verification evidence into human-approved progress.

**What Changed:**
- Created `sandboxes/005-agentic-sdlc-project-manager/README.md`
- Created `sandboxes/005-agentic-sdlc-project-manager/STAGE-PLAN.md`
- Created `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/STAGE.md`
- Added Sandbox 005 to `sandboxes/README.md`
- Added Sandbox 005 to `AGENT_CONTEXT.json` as an active project thread

**Decision Context:**

The owner rejected a generic shared dashboard/blueprint as too sloppy and clarified the actual target:
- combine Agile iteration with Agile V / V&V discipline
- use Gherkin where it helps behavior and acceptance criteria
- borrow Uncle Bob / Clean AI agentic discipline
- evaluate SwarmForge-style worktree/role orchestration
- use LLM-as-judge only as a semantic sensor
- eventually build a project-manager/control surface over repo truth

The sandbox explicitly separates the SDLC stack from the future agentic product runtime stack, following ADR-012.

**Stage 001 Current State:** Active, focused on artifact contract. No implementation tooling built yet. The stage plan intentionally requires a manual pilot before any dashboard or orchestration implementation.

---

### 2026-06-05: SDLC/Agentic Stack Separation Captured

*Source: `journal/2026-06-05-sdlc-agentic-stack-separation.md`*

Captured the project-level separation-of-concerns rule. Added `SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md` and `ADR-012`. This is a planning/architecture boundary only — it does not implement a SDLC stack or product agent runtime. Phase A should turn the principle into requirements, concept-of-operations documents, validation gates, and permission models.

---

### 2026-06-07: Experiment-Derived Requirements Added

*Source: `journal/2026-06-07-sandbox-005-experiment-derived-requirements.md`*

Updated Sandbox 005 so the agentic SDLC project-manager stack treats experimentation as a first-class source of requirements and as a first-class validation/verification method.

**Triggering observation:** The user clarified that their work style derives requirements through experiments as well as through human/agent discussion. Both the `legal-tech-debt` sandboxes and the "Grannies House Trials" game project show this pattern: prototypes, failed probes, surprising outputs, playtests, and generated reports reveal durable requirements, risks, and design constraints.

**Decisions Made:**
- Requirements may originate from conversation, experiments, backlog items, ADRs, external constraints, or mixed sources.
- Sandbox 005 now includes an experiment-to-requirement gate alongside conversation-to-contract.
- Sandbox 005 now treats experiment-backed V&V as part of the Agile V / V-model approach.
- Experiment observations should be captured as evidence first, then deliberately promoted.
- Not every interesting surprise becomes a requirement. Some remain journal notes, lessons, risk records, or follow-up experiments.
- Experiments can also confirm, falsify, or refine whether implemented behavior satisfies the domain need after deterministic tests pass.

**Stage 001 example artifacts added:**
- `task-contract.md`
- `experiment-requirement-candidate.md`
- `evidence-bundle.md`
- `experiment-vv-evidence.md`
- `risk-register.md`
- `dashboard-read-model.md`

**Portfolio framing note (recorded in journal):**

The stronger public framing for this concept is not "digital twin of an SE team." The stronger public framing is:

> **Agentic SDLC Control System**  
> or: **Repo-Native AI Software Engineering Manager**

That framing keeps the focus on the company pain: AI-assisted development work needs traceability, artifact contracts, experiment-derived requirements, V&V evidence, risk records, and human approval gates.

**Still open after 2026-06-07:**
- [ ] Define the first agent role set.
- [ ] Decide whether Stage 002 should pilot a real backlog item.
- [ ] During Stage 002, pilot at least one task whose origin is experiment evidence.
- [ ] If developed for portfolio use, build a small demo from messy conversation/experiment note through task contract, evidence bundle, V&V record, and generated status surface.

---

## 9. Backlog and Cross-Reference Notes

**BACKLOG-005** (original entry, now closed): "Phase A Entry — Agile V Framework Integration and SE Stack." Closed 2026-06-05, superseded by Sandbox 005. The item tracked the Phase A entry milestone and SE stack configuration; it was elevated to a full sandbox because the scope required iterative exploration rather than a single backlog implementation.

**`sandboxes/README.md` entry:**

> | 005-agentic-sdlc-project-manager | Explore the development SDLC/project-manager stack: Agile V, Gherkin/BDD, Clean AI discipline, SwarmForge-style agent roles, verification evidence, and repo-native status surfaces. | Active concept sandbox |

**`AGENT_CONTEXT.json` references:**

- Listed under `active_scope`: "Agentic SDLC project-manager stack exploration in Sandbox 005"
- Listed under `open_threads`: "SANDBOX-005 (ACTIVE): Agentic SDLC project-manager stack exploration. Goal: define repo-native Agile V + Gherkin/BDD + Clean AI + SwarmForge-style role/worktree discipline, evidence bundles, experiment-to-requirement promotion, experiment-backed V&V, and generated status surfaces without confusing SDLC tooling with product runtime agents."

---

## 10. Positioning and Framing Notes

These notes were recorded during the 2026-06-07 session and represent the product/portfolio framing that emerged from the sandbox work.

**The problem this solves:**

AI-assisted development teams (using Codex, Claude Code, GitHub Copilot, or similar) face a governance gap: the AI can produce code fast, but it cannot enforce traceability, artifact contracts, experiment-derived requirements, V&V evidence, or human approval gates on its own output. There is no "engineering manager" layer that brings discipline to multi-agent development work.

**What this is:**

A repo-native SDLC control system that:

1. Treats the git repository as the single source of project truth
2. Requires task contracts before implementation starts
3. Captures experiment observations as first-class requirement candidates
4. Enforces evidence bundles after implementation
5. Supports experiment-backed V&V alongside deterministic tests
6. Generates a status surface from repo artifacts without becoming a second planning universe
7. Distinguishes development agent work from product agent work

**What this is not:**

- A generic project management dashboard
- A replacement for the product runtime
- A tool that trusts AI output without human gates
- A solution that requires any particular orchestration framework (SwarmForge is evaluated, not mandated)

**Candidate target personas:**

- Engineering teams using multiple AI coding assistants who need governance without bureaucracy
- Teams building AI products who need to keep development discipline separate from product runtime discipline
- Solo developers or small teams running "AI-first" development who need traceability

**Current status of the concept:**

Stage 001 (artifact contract design) is substantially complete. Stage 002 (manual pilot on a real task) is next. No implementation tooling exists yet; the design-first approach is intentional.

---

*End of export document. Generated 2026-06-10.*
