# Project Bootstrap for All Agents

This file is the shared memory and startup contract for every AI assistant working in this repository, including Codex, GitHub Copilot, Claude Code, and any future agent.

## Required Startup

Before beginning any conversation or work:

1. Read the project documentation listed in the Documentation Map and establish a full understanding of where the project currently stands.
2. Read the sandbox documentation for the sandbox being touched.
3. If the work touches Sandbox 001, read `sandboxes/001-legal-debt-primitives/README.md`, `STAGING.md`, `NEXT_STAGES.md`, and the active stage status docs before changing files.
4. Summarize the current state internally before acting; do not start from assumptions or from one tool's prior memory alone.

## Shared Agent Memory

- The user works with multiple agents: Codex, GitHub Copilot, and Claude Code.
- Project memory must be written where all agents can read it, not only into Claude-specific, Codex-specific, or current-session memory.
- When adding durable instructions, update the shared bootstrap/config files as appropriate:
  - `BOOTSTRAP.md` for cross-agent project memory
  - `AGENTS.md` for Codex and general agent entry
  - `CLAUDE.md` for Claude Code entry
  - `.github/copilot-instructions.md` for GitHub Copilot entry

## Current Operating Mode

- This repository is currently a sandbox research environment.
- The work is proof-of-concept development, experiments, and evidence capture.
- Do not introduce infrastructure, services, deployment layers, databases, queues, containers, or production scaffolding unless a specific stage explicitly exists to evaluate that choice.
- Keep implementations quick, clean, readable, and easy to explain.
- Prefer plain files, plain Python, static HTML, JSON/CSV/Markdown outputs, and small deterministic probes while the project is still learning what the right model is.

## Documentation Map

Start with these documents when orienting:

1. `path.md` - current project path and north star.
2. `legal_tech_debt_report.md` - research synthesis and strategic frame.
3. `legal_code_smell_taxonomy.md` - core smell taxonomy and RAII defect classes.
4. `insurance_policy_smells.md` and `insurance_claims_smells.md` - insurance-specific smells.
5. `Real-World Cost Events Mapped to Insurance Legal Code Smells.md` - evidence and cost examples.
6. `Insurance Process Maturity Models  A Landscape Assessment for the Legal Tech Debt Platform.md` - maturity model landscape and gap.
7. `sandboxes/README.md` - sandbox rules and index.
8. `previous-chats/README.md` and `previous-chats/Legal Tech Debt & Legal Code Smells — ChatGPT Conversation Index.md` when historical context is needed.

For Sandbox 001, read:

1. `sandboxes/001-legal-debt-primitives/README.md`
2. `sandboxes/001-legal-debt-primitives/CLOSURE.md`
3. `sandboxes/001-legal-debt-primitives/STAGING.md`
4. `sandboxes/001-legal-debt-primitives/NEXT_STAGES.md`
5. `sandboxes/001-legal-debt-primitives/stages/004-typed-edge-study/STAGE_004_STATUS.md`
6. `sandboxes/001-legal-debt-primitives/stages/004-typed-edge-study/DOCUMENTATION_MAP.md`

For Sandbox 002, read:

1. `sandboxes/002-claims-regulatory-automation/002-claims-regulatory-automation-README.md`
2. `sandboxes/002-claims-regulatory-automation/002-ROADMAP-revised.md`
3. `sandboxes/002-claims-regulatory-automation/001-vs-002-REUSE-ANALYSIS.md`
4. `sandboxes/002-claims-regulatory-automation/002-CARRY-FORWARD-FROM-001.md`
5. `sandboxes/002-claims-regulatory-automation/002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md`
6. `sandboxes/002-claims-regulatory-automation/002-PAIN-POINTS-TAXONOMY.md`

Current Sandbox 002 scope:

- Focus on Kentucky homeowners insurance.
- Do not start auto, personal auto, motor vehicle, no-fault, or PIP work unless the user explicitly reopens that scope.
- If homeowners sources cross-reference auto or other P&C lines, record the reference as context only and keep the active fixture/detectors homeowners-centered.

## Current Sandbox 001 State

Sandbox 001 is complete as foundational research. It proved the basic legal debt probe idea with plain Python:

- section extraction
- reference extraction
- dangling references
- orphan definitions
- circular references
- unversioned external authorities
- dependency matrices and transitive closure
- static dashboard exploration

The conceptual bottleneck it discovered is semantic edge typing. Stage 004 completed the 46-edge seed labeling pass and paused in Phase 2: refine the edge taxonomy before implementing typed matrices or dashboard edge filtering.

Do not use 001 as the default active work lane. Use it as preserved evidence and reusable foundation. The active lane is now Sandbox 002: Kentucky homeowners insurance policy and claims legal tech debt.

Sandbox 001 work should resume only when a specific 002 experiment needs one of its primitives or when the user explicitly asks to revisit 001.

## Working Style

- Preserve existing sandbox stage discipline.
- Do not mutate frozen stages for new ideas; clone to a new numbered stage.
- Record assumptions, surprises, failure modes, and lessons.
- Treat generated outputs as evidence when they explain an experiment.
- Favor readable experiments over clever abstractions.
- Human review is part of the product concept; do not frame automated findings as legal advice.
