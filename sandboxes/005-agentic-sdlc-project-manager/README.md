# Sandbox 005: Agentic SDLC Project Manager

Status: Active concept sandbox
Started: 2026-06-05
Scope: Development SDLC stack, agent coordination, Agile V control surface

## Purpose

This sandbox explores the development-side project manager for Legal Tech Debt: a repo-native SDLC control system that turns human/agent conversation and experiment evidence into requirements, implementation slices, verification evidence, risk records, and human-approved progress.

This is the SDLC stack, not the agentic product runtime stack. See `../../ADR-012-separate-sdlc-stack-from-agentic-product-stack.md` and `../../SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md`.

Working thesis:

> Build a project manager that treats the repository as the source of truth. The project manager reads and writes disciplined artifacts, coordinates agents, tracks verification evidence, and makes project state visible without becoming a second competing planning universe.

## Why This Exists

The project is moving from exploratory sandbox work toward a more disciplined Phase A posture. The owner wants to combine:

- Agile iteration,
- V-model verification and validation,
- Gherkin/BDD acceptance specifications where useful,
- SwarmForge-style multi-agent coordination,
- Uncle Bob / Clean AI engineering discipline,
- risk-adaptive testing,
- and LLM-as-judge for semantic review only where deterministic checks are insufficient.

The goal is not to adopt a generic dashboard template. The goal is to design a stack that can become a practical project-manager layer for this repo and, later, for the product engineering lifecycle.

## Scope

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

## Design Principles

- Repo truth first. Dashboards summarize canonical files; they do not become canonical.
- Conversation and experimentation before contract. Exploration is allowed, and requirements may be discovered through sandbox runs, prototypes, playtests, corpus probes, or failed experiments. Implementation starts only after the discovered work has a clear artifact contract.
- Verification is risk-adaptive. Unit tests and fixtures are common; mutation testing and LLM judges are used when the risk justifies them.
- Experimentation supports both sides of the V. Experiments can discover requirements before implementation and can validate/verify whether built behavior matches real domain expectations after implementation.
- Agents leave evidence. Every substantive agent run should leave a readable trail: what changed, why, what was validated, and what remains uncertain.
- Experiments leave requirements candidates. A surprising sandbox result should be captured as evidence first, then promoted deliberately into a requirement, risk, backlog item, ADR, or lesson when it proves durable.
- Gherkin is for behavior. Use it when acceptance behavior benefits from executable specification, not as universal paperwork.
- Swarm discipline can be adopted incrementally. Start with roles, work isolation, and prompts before depending on any one orchestration tool.

## Candidate Stack

| Layer | Candidate Tools / Artifacts | Notes |
|---|---|---|
| Source of truth | Git, Markdown, JSON/JSONL, ADRs, backlog, journals, handoffs | Existing repo pattern; preserve it. |
| Experiment evidence | Sandbox outputs, playtest notes, probe results, failed runs, screenshots, generated reports | Requirements can be discovered by experiment, not only written before implementation. |
| Requirements | `requirements/`, `features/`, traceability records | Design in this sandbox before creating globally. |
| BDD | Gherkin, `pytest-bdd` or `behave` for Python slices | Use for product behavior and acceptance tests. |
| Tests | `pytest`, golden fixtures, schema validation, regression snapshots | Default hard gate. |
| Static checks | `ruff`, optional `mypy`, future `eslint`/`tsc` if TypeScript appears | Match actual implementation languages. |
| Mutation | `mutmut` for Python, later equivalents if needed | Risk-adaptive, not default ceremony. |
| Agent orchestration | Existing Codex/Claude/Copilot docs; SwarmForge-style worktrees and role prompts | Evaluate before adopting. |
| Semantic review | LLM-as-judge rubrics for report quality, semantic completeness, reviewer usefulness | Sensor only; not final authority. |
| Dashboard | Generated Markdown/HTML/JSON status view over repo artifacts | No separate planning database at first. |

## Starting Questions

- What is the minimum artifact contract for a disciplined implementation slice?
- How should experiment observations become requirement candidates without turning every surprise into scope creep?
- What work requires Gherkin, and what work should stay in Markdown task/ADR/risk form?
- What is the smallest useful traceability model from requirement to test to evidence?
- What agent roles are actually useful for this repo, and which create coordination overhead?
- What should count as an evidence bundle?
- What gates should be hard, advisory, or human-only?
- What should the project-manager dashboard read, and what should it be forbidden to edit?

## Future Sibling Sandbox

A likely future sandbox should explore the agentic product runtime stack: product agents, legal evidence processing, customer-data boundaries, runtime audit logs, and product-agent permissions. That is deliberately not started here.

## References

- SwarmForge: `https://github.com/unclebob/swarm-forge`
- Cucumber/Gherkin reference: `https://cucumber.io/docs/gherkin/reference`
- IEEE 1012 V&V overview: `https://standards.ieee.org/ieee/1012/7324/`
- CMU SEI V-model testing discussion: `https://www.sei.cmu.edu/blog/using-v-models-for-testing/`
- Clean AI course overview: `https://www.oreilly.com/videos/clean-ai-agentic/9780135968819/`
