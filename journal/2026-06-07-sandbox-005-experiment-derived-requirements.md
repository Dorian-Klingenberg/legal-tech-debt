# 2026-06-07 Sandbox 005 Experiment-Derived Requirements

## Session Summary

Updated Sandbox 005 so the agentic SDLC project-manager stack treats experimentation as a first-class source of requirements and as a first-class validation/verification method, not merely conversation.

The user clarified that their work style derives requirements through experiments as well as through human/agent discussion. Legal-tech-debt sandboxes and Grannies House Trials both show this pattern: prototypes, failed probes, surprising outputs, playtests, and generated reports reveal durable requirements, risks, and design constraints.

## What Changed

- Updated `sandboxes/005-agentic-sdlc-project-manager/README.md`.
- Updated `sandboxes/005-agentic-sdlc-project-manager/STAGE-PLAN.md`.
- Updated `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/STAGE.md`.
- Updated `AGENT_CONTEXT.json` so future agents see experiment-to-requirement promotion as part of the active Sandbox 005 lane.
- Added Stage 001 example artifact sketches under `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/examples/`:
  - `task-contract.md`
  - `experiment-requirement-candidate.md`
  - `evidence-bundle.md`
  - `experiment-vv-evidence.md`
  - `risk-register.md`
  - `dashboard-read-model.md`

## Decisions Made

- Requirements may originate from conversation, experiments, backlog items, ADRs, external constraints, or mixed sources.
- Sandbox 005 now includes an experiment-to-requirement gate alongside conversation-to-contract.
- Sandbox 005 now treats experiment-backed V&V as part of the Agile V / V-model approach.
- Experiment observations should be captured as evidence first, then deliberately promoted into requirements, risks, backlog items, ADR candidates, lessons, or task contracts.
- Not every interesting surprise becomes a requirement. Some remain journal notes, lessons, risk records, or follow-up experiments.
- Experiments can also confirm, falsify, or refine whether implemented behavior satisfies the domain need after deterministic tests pass.

## Validation Performed

- Read the active Sandbox 005 documents before editing:
  - `sandboxes/005-agentic-sdlc-project-manager/README.md`
  - `sandboxes/005-agentic-sdlc-project-manager/STAGE-PLAN.md`
  - `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/STAGE.md`
- Added concrete example sketches and marked only the corresponding checklist items complete.
- Checked `git status --short` before and after the update.

## Current State

Sandbox 005 now models both:

- conversation-to-contract, and
- experiment-to-requirement.
- experiment-backed validation and verification.

This makes the sandbox more clearly an emerging digital twin of an AI-assisted software engineering team/process: it models how the team learns from probes, promotes discoveries, creates contracts, verifies work, and exposes state.

For portfolio positioning, the stronger public framing is not "digital twin of an SE team." The stronger public framing is:

> Agentic SDLC Control System

or:

> Repo-Native AI Software Engineering Manager

That framing keeps the focus on the company pain: AI-assisted development work needs traceability, artifact contracts, experiment-derived requirements, V&V evidence, risk records, and human approval gates.

## What Comes Next

- [ ] Define the first agent role set.
- [ ] Decide whether Stage 002 should pilot a real backlog item.
- [ ] During Stage 002, pilot at least one task whose origin is experiment evidence.
- [ ] If developed for portfolio use, build a small demo from messy conversation/experiment note through task contract, evidence bundle, V&V record, and generated status surface.

## Checklist Follow-Up

Completed on 2026-06-07:

- [x] Sketch experiment-to-requirement candidate fields.
- [x] Sketch experiment-backed V&V evidence fields.
- [x] Update the planned `task-contract.md` example to include `origin` and `source evidence path`.
- [x] Update the planned dashboard read model to show traces from experiment or conversation to requirement to task to verification evidence.

Still open:

- [ ] Define the first agent role set.
- [ ] Decide whether Stage 002 should pilot a real backlog item.
- [ ] During Stage 002, pilot at least one task whose origin is experiment evidence.
- [ ] If developed for portfolio use, build a small demo from messy conversation/experiment note through task contract, evidence bundle, V&V record, and generated status surface.
