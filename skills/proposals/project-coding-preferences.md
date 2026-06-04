# Project Coding Preferences Skill Proposal

Status: draft implemented

## Recurring Workflow

Agents repeatedly need to infer how this repository wants code, schemas, runs, validation, and handoffs handled.

This skill captures the implementation defaults that were previously implicit in Codex context so Codex, Claude Code, GitHub Copilot, and future agents can apply them from repo-visible memory.

## Why This Should Be A Skill

The repository already has domain and memory-artifact skills, but neither one fully captures day-to-day coding taste:

- small deterministic probes before architecture
- plain local Python and file-backed artifacts
- schema/run/provenance discipline
- source-type-aware detector heuristics
- focused validation with run IDs and counts
- constrained-agent handoff instructions

Without a shared skill, a new agent can read the domain documents and still choose the wrong implementation shape.

## Source Of Truth

- `BOOTSTRAP.md`
- `AGENT_CONTEXT.json`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `CLAUDE_CONSTRAINTS.md`
- `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-03d.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-004-schema-run-identity-and-id-stability.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-006-detector-source-type-filtering.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-007-sandbox-003-scope-findings-triage.md`

## Trigger Examples

- "Make this detector change in Sandbox 002."
- "Review this stage output and tell me what is missing."
- "Prepare a handoff so Claude can continue safely."
- "Add a schema field to the discovery pipeline."
- "Should we add vector infrastructure now?"

## Guardrails

- Do not turn preferences into production architecture.
- Do not override active sandbox scope.
- Do not use private Codex memory as source of truth.
- Do not loosen Claude constraints for ordinary coding work; only make startup and explicit memory-review tasks feasible.
- Do not mark the skill active until it has been validated on a real implementation, review, or constrained-agent handoff task.

## Implementation Checklist

- [x] Draft repo-visible `skills/project-coding-preferences/SKILL.md`
- [x] Add compact cross-agent context in `AGENT_CONTEXT.json`
- [x] Register the skill in `skills/registry.csv`
- [x] Link the skill from `skills/README.md`
- [x] Update `BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md`
- [x] Add bounded Claude startup/memory-task exceptions in `CLAUDE_CONSTRAINTS.md`
- [ ] Validate the skill on a real implementation, review, or constrained-agent handoff task
- [ ] Mark the skill `active` after validation
- [ ] Install or mirror into `$CODEX_HOME/skills` only if the user wants Codex auto-discovery

## First Validation Task

Use the skill on one focused follow-up task, preferably one of:

- calibrate the Smell 5 detector on run `87283951`
- re-evaluate the gold set on run `87283951`
- prepare a Claude-readable context freeze for Sandbox 003 startup

The validation should show that the agent chooses small, file-backed, provenance-preserving work and avoids infrastructure or broad refactors.
