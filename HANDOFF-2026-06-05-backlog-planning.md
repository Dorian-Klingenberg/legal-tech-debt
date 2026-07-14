# Handoff: Backlog Planning And Claude Implementation Brief

Date: 2026-06-05
Audience: Claude Code, Codex, GitHub Copilot, and future agents

> Historical snapshot. The implementation priorities in this handoff were later completed, closed, or promoted to Sandbox 005. Use `README.md`, `AGENT_CONTEXT.json`, and the latest handoff named there.

## Purpose

This is the resume point after closing the backlog planning session. The user wants to implement the next backlog items with Claude Code, using detailed repo-visible instructions rather than broad chat context.

## Current State

- Sandbox 002 is complete and preserved as the evidence/detector substrate.
- Sandbox 003 is complete as the executive-summary sales instrument.
- Sandbox 004 is complete as the expert drill-down report proof of concept.
- Current forward lane is backlog work, not a new sandbox by default.
- Root implementation plan: `BACKLOG-IMPLEMENTATION-PLAN.md`.

## Active Scope

Use the unblocked backlog item order in `BACKLOG-IMPLEMENTATION-PLAN.md`:

1. `BACKLOG-019` - Missing State Amendatory detector
2. `BACKLOG-015` - heuristic-specific case and bad-faith closure library
3. `BACKLOG-020` - Tighten Broken Definitions Loop detector
4. `BACKLOG-007` - KRS/KAR definitional cross-reference check
5. `BACKLOG-011` - section-header / structure-node detector pre-filter
6. `BACKLOG-003` - Kentucky Growers SERFF recheck
7. `BACKLOG-002` - corpus file extension mismatches
8. `BACKLOG-009` - candidate underwriting smell taxonomy check

## Exclusions

- Do not start Phase A work until owner prerequisites are ready.
- Do not hand `BACKLOG-006` or `BACKLOG-012` to Claude as implementation tasks until the context-classification validation design exists.
- Do not introduce infrastructure, services, databases, vector stores, or production scaffolding.
- Do not procure new SERFF filings unless the user explicitly asks.
- Do not treat automated outputs as legal conclusions.

## Key Files

| Purpose | Path |
|---|---|
| Claude-ready backlog plan | `BACKLOG-IMPLEMENTATION-PLAN.md` |
| Backlog index | `BACKLOG.md` |
| Compact context | `AGENT_CONTEXT.json` |
| Claude startup instructions | `CLAUDE.md` and `CLAUDE_CONSTRAINTS.md` |
| Current product handoff | `sandboxes/004-expert-drilldown/HANDOFF-2026-06-04.md` |
| Preserved Stage 002 run | `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/` |
| Canonical detector findings | `sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl` |

## Recommended Next Step

Start Claude on `BACKLOG-019`.

Exact instruction to give Claude:

```text
Read CLAUDE_CONSTRAINTS.md first, then BOOTSTRAP.md, AGENT_CONTEXT.json, AGENT_OPERATING_MODEL.md, CLAUDE.md, BACKLOG.md, and BACKLOG-IMPLEMENTATION-PLAN.md. Implement only BACKLOG-019 using the file allowlist, constraints, acceptance criteria, and validation commands in BACKLOG-IMPLEMENTATION-PLAN.md. Do not start other backlog items.
```

## Validation

Planning/documentation-only closeout. No detector or report code was run.

Validation expected before committing:

```powershell
git diff --check
git status --short
```

## ADR And Lesson Notes

No ADR was created for this planning session because no new architectural alternative was selected. The session created an implementation handoff/planning artifact, not a durable architecture decision.

No lesson was created because the reusable insight was already captured in `AGENT_OPERATING_MODEL.md` and the Claude-specific planning pattern is embodied directly in `BACKLOG-IMPLEMENTATION-PLAN.md`.
