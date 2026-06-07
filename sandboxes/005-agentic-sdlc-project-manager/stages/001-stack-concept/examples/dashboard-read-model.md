# Dashboard Read Model Sketch

Status: Sketch

Purpose: define what a future generated status surface may read from repo truth and what it must not own.

## Allowed Inputs

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

## Must Show

- active lane and active sandbox
- open task contracts
- latest validation evidence
- experiment-derived requirement candidates
- experiment-backed V&V records
- open risks and accepted risks
- stale handoffs or stale context pointers
- missing evidence explicitly
- trace from conversation/experiment to requirement to task to verification evidence when available

## Forbidden To Own

- canonical project scope
- backlog truth
- ADR decisions
- human approval decisions
- source corpus truth
- product runtime memory
- private assistant memory

## Duplicate-Truth Risks

- A dashboard status field could drift from `AGENT_CONTEXT.json`.
- Generated summaries could look more authoritative than ADRs or handoffs.
- Task state could be split between backlog, task contract, evidence bundle, and dashboard.
- Experiment observations could become requirements without human promotion.

## Guardrail

The dashboard must be disposable. If deleting generated dashboard output loses project truth, the design is wrong.
