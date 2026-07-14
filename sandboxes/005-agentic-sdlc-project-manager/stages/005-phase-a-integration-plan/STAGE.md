# Stage 005: Phase A Integration Plan

Status: Planned
Entry gate: Stages 002-004 completed or explicitly closed with evidence

## Purpose

Convert proven Sandbox 005 findings into a Phase A-ready SDLC concept of
operations and an explicit adoption plan.

This stage integrates evidence. It does not implement production infrastructure
or declare Phase A started.

## Controlling Question

Which Sandbox 005 controls are useful and mature enough to become formal Phase A
requirements, architecture decisions, verification gates, and agent governance?

## Required Inputs

- Stage 001 artifact model and system-selection evidence.
- Stage 002 manual-pilot measurements and revised artifact contract.
- Stage 003 status-surface findings or rejection record.
- Stage 004 orchestration comparison and adoption decision.
- Current project architecture boundaries and production-aligned documentation.
- Human decisions about Phase A scope, timing, and acceptable process cost.

## Expected Outputs

- SDLC concept of operations.
- SDLC requirement categories and initial requirement set.
- Traceability model from origin through verification and release decision.
- Verification evidence model and risk-adaptive gate policy.
- Development-agent roles, permissions, memory, and handoff model.
- Status-surface role and canonical-truth boundary.
- Tool adoption, rejection, and deferral record.
- ADR candidates for durable choices between named alternatives.
- Sandbox closure or carry-forward decision.

## In Scope

- Development SDLC requirements.
- Artifact ownership and precedence.
- Risk classes and required evidence.
- Human approval boundaries.
- Agent permissions, roles, isolation, and audit expectations.
- CI and local validation concepts grounded in completed experiments.
- Migration from sandbox sketches to Phase A specifications.

## Out Of Scope

- Product runtime agent requirements except as a documented boundary.
- Customer tenancy, billing, deployment, or production operations.
- Claiming ISO, GxP, security, or regulatory compliance without an applicable
  assessment.
- Converting every sandbox idea into a mandatory process.
- Selecting tools without experiment evidence or an owner decision.
- Beginning Phase A coursework or formal entry automatically.

## Integration Principles

- Promote evidence-backed controls, not aspirational framework features.
- Keep SDLC and product-runtime requirements separate.
- Preserve conversation and experiment origins in traceability.
- Keep deterministic evidence distinct from semantic and human review.
- Make waivers, skipped gates, and accepted risks explicit.
- Keep canonical project truth repo-visible and cross-agent.
- Prefer the least ceremony that achieved the measured assurance benefit.

## Entry Checklist

- [ ] Stage 002 has a human-reviewed outcome.
- [ ] Stage 003 is completed or rejected with a lesson.
- [ ] Stage 004 is completed or rejected with a measured comparison.
- [ ] Open contradictions among stage records are resolved.
- [ ] Phase A prerequisites in current project context are rechecked.
- [ ] The owner approves beginning integration planning.

## Concept Of Operations Checklist

- [ ] Define actors: owner, lead/specifier, implementer, verifier, optional
      specialist, and release decision-maker.
- [ ] Define the normal task lifecycle.
- [ ] Define conversation-to-contract and experiment-to-requirement paths.
- [ ] Define experiment-backed V&V after implementation.
- [ ] Define blocked, rejected, waived, and abandoned task paths.
- [ ] Define single-writer and multi-writer boundaries.
- [ ] Define local, CI, and human gates.
- [ ] Define status generation and stale-state handling.

## Requirements Checklist

- [ ] Separate product, SDLC, data/evidence, security, and agent-runtime
      requirement categories.
- [ ] Assign stable IDs without replacing existing project identifiers.
- [ ] Define requirement origin and source-evidence fields.
- [ ] Define acceptance and verification links.
- [ ] Define risk classification and evidence obligations.
- [ ] Define approval, waiver, and residual-risk fields.
- [ ] Define schema-version and migration expectations for consumed artifacts.
- [ ] Define which requirements warrant Gherkin.

## Governance Checklist

- [ ] Define canonical artifacts and precedence.
- [ ] Define development-agent permissions and file boundaries.
- [ ] Define model/provider-neutral role contracts.
- [ ] Define Codex-, Claude-, and Copilot-specific adapters separately.
- [ ] Define worktree, branch, commit, and handoff rules.
- [ ] Define credential and secret boundaries for automation.
- [ ] Define external research and source-citation requirements.
- [ ] Define human-only decisions.

## Verification Checklist

- [ ] Trace every promoted control to Sandbox 005 evidence.
- [ ] Identify controls rejected or simplified after pilots.
- [ ] Check for duplicate truth and conflicting IDs.
- [ ] Check that generated status remains disposable.
- [ ] Check that SDLC agents are not confused with product agents.
- [ ] Review licensing and version pinning for adopted tools.
- [ ] Review the plan against current production-aligned boundaries.
- [ ] Obtain human approval for every proposed durable architecture choice.

## Completion Checklist

- [ ] Concept of operations is complete and human-reviewed.
- [ ] Initial SDLC requirements and traceability model are documented.
- [ ] Verification evidence and agent governance models are documented.
- [ ] Required ADRs are accepted, rejected, or explicitly deferred.
- [ ] Phase A entry remains a separate owner decision.
- [ ] Sandbox 005 is closed or given a narrow carry-forward scope.
- [ ] README, stage plan, documentation map, handoff, lesson, journal, and
      `AGENT_CONTEXT.json` reflect the final state.

## Closure Gate

Sandbox 005 closes only when every useful control has one of four outcomes:

- promote to Phase A;
- retain as optional practice;
- defer with a stated trigger;
- or reject with evidence.

Unresolved framework enthusiasm is not a closure outcome.
