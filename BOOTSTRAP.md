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

## Project Skill Workbench

- Project skills are tracked under `skills/`.
- Skills are reusable agent workflows, similar to how sandboxes are reusable experiment containers.
- The repository remains the source of truth. Codex-installed skills should point back to repo docs rather than becoming the only place where project knowledge lives.
- For skill creation or updates, read:
  - `skills/README.md`
  - `skills/SKILL-DEVELOPMENT.md`
  - `skills/registry.csv`
- Keep skills applicable across Codex, GitHub Copilot, and Claude Code by updating shared repo documentation whenever a skill captures durable project knowledge.
- Do not use skill creation as a reason to add production infrastructure. Skill work should follow the same quick, clean, readable proof-of-concept discipline as sandbox work.
- Current draft project skills:
  - `legal-rag-builder` for Sandbox 002 legal document ingestion and retrieval.
  - `project-memory-artifacts` for shared handoffs, journals, lessons, and agent context updates.

## Documentation Map

Start with these documents when orienting:

1. `path.md` - current project path and north star.
2. `legal_tech_debt_report.md` - research synthesis and strategic frame.
3. `legal_code_smell_taxonomy.md` - core smell taxonomy and RAII defect classes.
4. `insurance_policy_smells.md` and `insurance_claims_smells.md` - insurance-specific smells.
5. `Real-World Cost Events Mapped to Insurance Legal Code Smells.md` - evidence and cost examples.
6. `Insurance Process Maturity Models  A Landscape Assessment for the Legal Tech Debt Platform.md` - maturity model landscape and gap.
7. `sandboxes/README.md` - sandbox rules and index.
8. `corpus/README.md` - shared primary-document corpus rules.
9. `previous-chats/README.md` and `previous-chats/Legal Tech Debt & Legal Code Smells — ChatGPT Conversation Index.md` when historical context is needed.

For Sandbox 001, read:

1. `sandboxes/001-legal-debt-primitives/README.md`
2. `sandboxes/001-legal-debt-primitives/CLOSURE.md`
3. `sandboxes/001-legal-debt-primitives/STAGING.md`
4. `sandboxes/001-legal-debt-primitives/NEXT_STAGES.md`
5. `sandboxes/001-legal-debt-primitives/stages/004-typed-edge-study/STAGE_004_STATUS.md`
6. `sandboxes/001-legal-debt-primitives/stages/004-typed-edge-study/DOCUMENTATION_MAP.md`

For Sandbox 002, read:

1. `sandboxes/002-claims-regulatory-automation/002-claims-regulatory-automation-README.md`
2. `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`
3. `sandboxes/002-claims-regulatory-automation/002-ROI-CASES-FIVE-SMELLS.md`
4. `sandboxes/002-claims-regulatory-automation/002-ROADMAP-revised.md`
5. `sandboxes/002-claims-regulatory-automation/002-CARRY-FORWARD-FROM-001.md`
6. `sandboxes/002-claims-regulatory-automation/002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md`
7. `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md` when doing RAG, ingestion, retrieval, chunking, citation extraction, or legal corpus indexing work.
8. `sandboxes/002-claims-regulatory-automation/002-RAG-SUBSYSTEM-PLAN.md` and `sandboxes/002-claims-regulatory-automation/002-RAG-PHASE-PLAN.md` when doing RAG implementation planning.
9. `skills/legal-rag-builder/adr/` when doing Legal RAG Builder skill architecture work.
10. `sandboxes/002-claims-regulatory-automation/002-PAIN-POINTS-TAXONOMY.md`
11. `sandboxes/002-claims-regulatory-automation/001-vs-002-REUSE-ANALYSIS.md`
12. `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`
13. `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`

Current Sandbox 002 scope:

- Focus on Kentucky homeowners insurance.
- Align all active Sandbox 002 work to the five policy-layer smells in `002-five-policy-layer-phish.md`:
  - Overbroad / Non-deterministic Exclusions
  - Magic Number / Magic Valuation Terms
  - Coverage Inversion / Contradictory Conditions
  - Calculation Rule Drift / Unversioned Rate Reference
  - Regulatory Mapping Smells
- Do not start auto, personal auto, motor vehicle, no-fault, or PIP work unless the user explicitly reopens that scope.
- If homeowners sources cross-reference auto or other P&C lines, record the reference as context only and keep the active fixture/detectors homeowners-centered.
- Treat broad claims-platform, regulatory-feed, PAS, productization, and infrastructure references as background or parked unless a specific stage explicitly reopens them.
- Attach smell-specific ROI notes from `002-ROI-CASES-FIVE-SMELLS.md` to fixture examples and findings when useful.
- Use the corpus at `corpus/kentucky-homeowners-policy-smells/` as the current real-document evidence base.
- Treat `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` as the record of sources already downloaded and mapped by smell.
- Treat `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` and `corpus/kentucky-homeowners-policy-smells/_manual_or_skipped_sources.csv` as the record of known unknowns. Do not chase manual SERFF gaps unless an active experiment actually needs that evidence.
- Keep primary source corpora under top-level `corpus/`, not inside `sandboxes/` or `skills/`.
- Use `sources/` for background research, papers, web captures, and how-to/reference material.

## Cross-Agent Startup Automation

Every future agent working in this repository should do the following before making changes:

1. Read this file first.
2. Read the relevant agent entry file for the tool in use:
   - `AGENTS.md` for Codex and general coding agents.
   - `CLAUDE.md` for Claude Code.
   - `.github/copilot-instructions.md` for GitHub Copilot.
3. Read the current sandbox README, controlling scope document, active roadmap, and latest handoff.
4. For Sandbox 002 work, inspect the corpus manifest and known gaps before deciding that more source procurement is needed.
5. Preserve decisions in shared files that Codex, Copilot, Claude Code, and future agents can all read. Do not store durable project knowledge in one assistant's private memory only.
6. Add or update journal, handoff, lesson, and context records at major pause points, scope changes, corpus changes, or stage transitions. Use `skills/project-memory-artifacts/SKILL.md` when creating these shared memory artifacts.
7. For skill work, inspect `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv` before drafting or installing a skill.

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

