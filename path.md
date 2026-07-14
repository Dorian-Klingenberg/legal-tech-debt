# Legal Tech Debt Path

Status: Current roadmap
Updated: 2026-07-13

This roadmap describes the current direction. The earlier Sandbox 001 roadmap is preserved in that sandbox's historical stage documents.

## North Star

Build inspectable legal tech debt probes that turn insurance legal and regulatory text into source-traceable evidence, candidate smells, findings, and human-reviewable work products.

The portfolio version of that north star is:

> Demonstrate a production-aligned evidence workbench that a trusted insurance compliance, legal, filing, or technology provider could evaluate without pretending the repository is already a production service or a proven business.

## Where The Project Is

- [x] Sandbox 001 proved lightweight structural and graph primitives.
- [x] Sandbox 002 produced a file-backed evidence, retrieval, detector, and reviewer-report pipeline for five Kentucky homeowners smells.
- [x] Sandbox 003 converted a 35-finding point-in-time snapshot into triage, cross-carrier analysis, and an executive report.
- [x] Sandbox 004 produced three expert drill-down entries and five generated report variants.
- [x] Feasibility work reframed the likely buyer from direct-carrier SaaS to a provider-facing evidence capability.
- [x] Sandbox 005 Stage 001 selected a repo-native SDLC hybrid.
- [x] Sandbox 006 Stage 002 generated a local interactive workbench.
- [x] Productization documents define the difference between proof of concept, portfolio demo, pilot, and production.

## Current Work Order

### 1. Sandbox 005 Manual Pilot

Status: Ready, not started; owner-gated.

- [ ] Explicitly start Stage 002.
- [ ] Isolate the current dirty worktree.
- [ ] Run the read-only Codex/worktree preflight.
- [ ] Approve the `S005-PILOT-001` task contract.
- [ ] Implement and independently verify the bounded manifest validator.
- [ ] Record measured overhead, failure modes, and whether the hybrid is worth keeping.

### 2. Sandbox 006 Review Gate

Status: Prototype implemented; visual review pending.

- [ ] Open the generated workbench through an approved local review path.
- [ ] Check desktop and narrow/mobile layouts.
- [ ] Record accepted and rejected interaction patterns.
- [ ] Decide whether Figma or Canva comparison would answer a remaining question.
- [ ] Carry accepted data-model or generation changes back only through an explicit decision.

### 3. Production-Aligned Portfolio Demo

Status: Planning only.

- [ ] Define a fictional carrier/provider corpus that preserves real defect patterns without exposing real entities or proprietary text.
- [ ] Choose the first demo surface.
- [ ] Define the minimum workspace, reviewer-state, export, audit, and test-invoice model before implementation.
- [ ] Make the demo runnable end to end from a clean checkout.
- [ ] Keep real auth, payments, customer uploads, and deployment behind later gates.

### 4. Commercial Validation

Status: Hypothesis testing.

- [ ] Ask a trusted insurance-domain reviewer whether one sanitized finding represents a real workflow problem.
- [ ] Ask a provider-side reviewer whether the evidence pack reduces work or merely adds review burden.
- [ ] Compare the exact issue class with incumbent tools and ordinary LLM use.
- [ ] Identify the smallest repeatable paid unit, if one exists.
- [ ] Stop or narrow if qualified reviewers do not recognize actionable value.

## Parked Until Earned

- [ ] Vector or retrieval-store infrastructure for a demonstrated semantic-retrieval workload.
- [ ] Graph database or production API.
- [ ] Hosted multi-tenant application.
- [ ] Live regulatory feeds or automated SERFF acquisition.
- [ ] Customer authentication, billing, and deployment.
- [ ] Broad state or product-line expansion.
- [ ] Automated legal conclusions.

These are not overdue tasks. They are explicit non-goals until a new stage or validation result earns them.

## Owner And Access Lanes

- [ ] Recheck Kentucky Growers in SERFF when practical (`BACKLOG-003`).
- [ ] Consider Kentucky DOI market-conduct records only if a validation or case-library question needs them.
- [ ] Revalidate grants, laws, program eligibility, and time-sensitive market facts before acting on dated feasibility notes.

## Decision Rule

Prefer the next experiment that reduces uncertainty about usefulness, trust, repeatability, or buyer workflow. Do not use production architecture as a substitute for that evidence.
