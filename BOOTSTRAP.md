# Project Bootstrap for All Agents

This file is the shared memory and startup contract for every AI assistant working in this repository, including Codex, GitHub Copilot, Claude Code, and any future agent.

## Required Startup

Before beginning any conversation or work:

0. If the active agent is Claude Code, read `CLAUDE_CONSTRAINTS.md` first and treat it as a mandatory runtime policy. If it cannot be read, stop and request human instruction.
1. Read the project documentation listed in the Documentation Map and establish a full understanding of where the project currently stands.
2. Read the sandbox documentation for the sandbox being touched.
3. If the work touches Sandbox 001, read `sandboxes/001-legal-debt-primitives/README.md`, `STAGING.md`, `NEXT_STAGES.md`, and the active stage status docs before changing files.
4. Summarize the current state internally before acting; do not start from assumptions or from one tool's prior memory alone.

## Shared Agent Memory

- The user works with multiple agents: Codex, GitHub Copilot, and Claude Code.
- Project memory must be written where all agents can read it, not only into Claude-specific, Codex-specific, or current-session memory.
- `AGENT_CONTEXT.json` is the compact current-state context for constrained agents and fast startup. Read it after this file when present, then use canonical Markdown docs for details.
- `AGENT_OPERATING_MODEL.md` explains the shared role split across Codex, Claude Code, and GitHub Copilot. Read it with the startup docs when you need the operating rules in one place.
- Chronological journal entries belong in the top-level `journal/` folder. Do not create new `JOURNAL-*.md` files inside sandbox folders; use sandbox-local handoffs for resume instructions and top-level journal entries for session history.
- When adding durable instructions, update the shared bootstrap/config files as appropriate:
  - `BOOTSTRAP.md` for cross-agent project memory
  - `AGENTS.md` for Codex and general agent entry
  - `CLAUDE.md` for Claude Code entry
  - `.github/copilot-instructions.md` for GitHub Copilot entry

## Current Operating Mode

- This repository is currently a sandbox research environment transitioning toward Phase A (formal SE lifecycle entry).
- Phase A requires the owner to complete SE coursework (MIT) and configure an SE expert RAG corpus (NASA, INCOSE, IEEE — see open threads in AGENT_CONTEXT.json). Phase A has not started. Do not treat it as active or imminent.
- **Sandboxes remain open and active during Phase A preparation.** Discovery work, proof-of-concept experiments, and evidence capture in sandboxes directly inform the product decisions that Phase A will formalize. Do not shut down or defer sandbox work on the grounds that formal development has not started.
- The product direction is not yet fixed. Sandbox outputs are the primary input to the product decision. Keep building evidence.
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
  - `project-coding-preferences` for shared implementation defaults, validation habits, and constrained-agent handoff behavior.
  - Granular portable skills: `apply-implementation-defaults`, `write-adr`, `write-journal-entry`, `write-lesson`, `write-handoff`, and `maintain-agent-context`.

## Documentation Map

Start with these documents when orienting:

0. `AGENT_CONTEXT.json` - compact current-state context, active scope, open threads, and implementation preferences.
1. `AGENT_OPERATING_MODEL.md` - shared role split, truth hierarchy, and drift prevention rules for Codex, Claude Code, and Copilot.
2. `path.md` - current project path and north star.
3. `legal_tech_debt_report.md` - research synthesis and strategic frame.
4. `legal_code_smell_taxonomy.md` - core smell taxonomy and RAII defect classes.
5. `insurance_policy_smells.md` and `insurance_claims_smells.md` - insurance-specific smells.
6. `Real-World Cost Events Mapped to Insurance Legal Code Smells.md` - evidence and cost examples.
7. `Insurance Process Maturity Models  A Landscape Assessment for the Legal Tech Debt Platform.md` - maturity model landscape and gap.
8. `sandboxes/README.md` - sandbox rules and index.
9. `corpus/README.md` - shared primary-document corpus rules.
10. `previous-chats/README.md` and `previous-chats/Legal Tech Debt & Legal Code Smells — ChatGPT Conversation Index.md` when historical context is needed.

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
7. `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md` when doing discovery, instrumentation, RAG, ingestion, retrieval, chunking, citation/reference extraction, or legal corpus indexing work.
8. `sandboxes/002-claims-regulatory-automation/002-RAG-SUBSYSTEM-PLAN.md` and `sandboxes/002-claims-regulatory-automation/002-RAG-STAGE-PLAN.md` when doing discovery/RAG implementation planning.
9. `sandboxes/002-claims-regulatory-automation/adr/` when doing Legal RAG Builder skill architecture work.
10. `sandboxes/002-claims-regulatory-automation/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md` for the current Sandbox 002 path decision.
11. `sandboxes/002-claims-regulatory-automation/adr/ADR-004-schema-run-identity-and-id-stability.md` for Stage 002 schema, run identity, and stable-ID requirements.
12. `sandboxes/002-claims-regulatory-automation/adr/ADR-008-stage-002-artifact-contract-repair.md` for the 2026-06-04 repair of Stage 002 implementation drift back to the artifact contract.
13. `sandboxes/002-claims-regulatory-automation/adr/ADR-009-close-sandbox-002-with-smell-5-limitation.md` for the Sandbox 002 closure decision and Smell 5 limitation.
14. `sandboxes/002-claims-regulatory-automation/CLOSURE.md`
15. `sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md` when doing Docling, local parsing model, VLM enrichment, embedding, or retrieval-store work.
16. `sandboxes/002-claims-regulatory-automation/002-PAIN-POINTS-TAXONOMY.md`
17. `sandboxes/002-claims-regulatory-automation/001-vs-002-REUSE-ANALYSIS.md`
18. `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-04b.md`
19. `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
20. `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`

Current Sandbox 002 scope:

- Focus on Kentucky homeowners insurance.
- Align all active Sandbox 002 work to the five policy-layer smells in `002-five-policy-layer-phish.md`:
  - Overbroad / Non-deterministic Exclusions
  - Magic Number / Magic Valuation Terms
  - Coverage Inversion / Contradictory Conditions
  - Calculation Rule Drift / Unversioned Rate Reference
  - Regulatory Mapping Smells
- Do not start auto, personal auto, motor vehicle, no-fault, or PIP work unless the user explicitly reopens that scope.
- If homeowners sources cross-reference auto or other P&C lines, record the reference as context only and keep active discovery, fixtures, and detectors homeowners-centered.
- Treat broad claims-platform, regulatory-feed, PAS, productization, and infrastructure references as background or parked unless a specific stage explicitly reopens them.
- Sandbox 002 is closed as a discovery/retrieval/detector/reviewer-report proof of concept. Preserved repaired run: `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/` (28 sources, 353 nodes, 121 candidate evidence items, 39 Stage 003 retrieval bundles, 35 findings across all five smells). Smell 5 resolved via graph-based gap detection (ADR-010). Latest handoff: `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-04b.md`.
- Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist.
- Treat parser/reference uncertainty as part of the evidence layer, not as an implementation detail.
- Stage 002 JSON/JSONL artifacts should carry schema version, run identity, creation timestamp, and stable source/node IDs under a fixed parsing strategy.
- Attach smell-specific ROI notes from `002-ROI-CASES-FIVE-SMELLS.md` to candidate evidence, fixture examples, and findings when useful.
- Use the corpus at `corpus/kentucky-homeowners-policy-smells/` as the current real-document evidence base.
- Treat `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` as the record of sources already downloaded and mapped by smell.
- Treat `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` and `corpus/kentucky-homeowners-policy-smells/_manual_or_skipped_sources.csv` as the record of known unknowns. Do not chase manual SERFF gaps unless an active experiment actually needs that evidence.
- For RAG parser work, Docling is a parser/enrichment adapter only. It may use local cached document models, but it is not the legal RAG store, a vector database, parser truth, or a verified general local LLM runtime. See `sandboxes/002-claims-regulatory-automation/references/docling-local-stack-boundary.md`.
- Keep primary source corpora under top-level `corpus/`, not inside `sandboxes/` or `skills/`.
- Use `sources/` for background research, papers, web captures, and how-to/reference material.

## Cross-Agent Startup Automation

Every future agent working in this repository should do the following before making changes:

0. If the active agent is Claude Code, read `CLAUDE_CONSTRAINTS.md` before any exploration, file reads, planning, or tool use.
1. Read this file.
2. Read `AGENT_CONTEXT.json`.
3. Read `AGENT_OPERATING_MODEL.md`.
4. Read the relevant agent entry file for the tool in use:
   - `AGENTS.md` for Codex and general coding agents.
   - `CLAUDE.md` for Claude Code.
   - `.github/copilot-instructions.md` for GitHub Copilot.
5. Read the current sandbox README, controlling scope document, active roadmap, and latest handoff.
6. For Sandbox 002 work, inspect the corpus manifest and known gaps before deciding that more source procurement is needed.
7. Preserve decisions in shared files that Codex, Copilot, Claude Code, and future agents can all read. Do not store durable project knowledge in one assistant's private memory only.
8. Add or update journal, handoff, lesson, and context records at major pause points, scope changes, corpus changes, or stage transitions. Write chronological journals under top-level `journal/`; keep handoffs near the sandbox or component they resume. Use `skills/project-memory-artifacts/SKILL.md` when creating these shared memory artifacts.
9. For substantive code changes or code review, read `skills/project-coding-preferences/SKILL.md` so implementation defaults are shared across agents.
10. For skill work, inspect `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv` before drafting or installing a skill.

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

Do not use 001 as the default active work lane. Use it as preserved evidence and reusable foundation. Sandbox 002 is preserved as the Kentucky homeowners evidence substrate. Sandbox 003 is complete — findings triage, cross-carrier analysis, and executive summary report all built and hardened. Sandbox 004 is complete as the expert drill-down report proof of concept.

The active lane is choosing between BACKLOG-019 (Missing State Amendatory detector) and BACKLOG-015 (heuristic-specific case library). See `sandboxes/004-expert-drilldown/HANDOFF-2026-06-04.md` and `BACKLOG.md` for full context.

Sandbox 001 work should resume only when a specific experiment needs one of its primitives or when the user explicitly asks to revisit it.

## Working Style

- Preserve existing sandbox stage discipline.
- Do not mutate frozen stages for new ideas; clone to a new numbered stage.
- Record assumptions, surprises, failure modes, and lessons.
- Treat generated outputs as evidence when they explain an experiment.
- Favor readable experiments over clever abstractions.
- Prefer small deterministic probes, explicit local files, schema-aware artifacts, and focused validation before new abstractions or tools.
- Human review is part of the product concept; do not frame automated findings as legal advice.
- When you update a specification, stage plan, roadmap, or architecture document, capture what changed and why in the end-of-session journal entry. Decision tracking — knowing when, why, and what changed — is the goal. ADRs are reserved for architectural choices between named alternatives, not routine plan updates. Silent plan edits with no session record are not acceptable.

