# Handoff: Repository Documentation Audit

Date: 2026-07-13
Audience: Dorian, Codex, Claude Code, GitHub Copilot, and future agents
Status: Current repository-level resume point

## Purpose

This handoff closes a repository-wide documentation and instruction audit. The audit reconciled pivots, stage status, evidence counts, historical records, planning gates, and cross-agent startup rules so a future reader can resume from current truth without reconstructing the project from dated handoffs or generated output.

## Current State

The root `README.md` is the human-readable current-status surface. `AGENT_CONTEXT.json` is its compact machine-readable mirror.

| Lane | Current state | Gate |
|---|---|---|
| Sandbox 005 | Primary technical lane; Stage 001 complete | Stage 002 starts only after explicit owner authorization |
| Sandbox 006 | Secondary UX lane; Stage 002 prototype implemented | Human visual/responsive review before Stage 003 |
| Productization | Planning only | Choose a synthetic demo and first product unit before production code |
| Commercial feasibility | Provider-facing hypothesis, not validated demand | Show sanitized/synthetic evidence to qualified domain and provider-side reviewers |
| BACKLOG-003 | Only open cross-sandbox backlog item | Optional owner-led SERFF recheck |

Sandboxes 001-004 are complete and preserved. Formal Phase A lifecycle work has not started. No production infrastructure, customer-data path, authentication, billing integration, or deployment is authorized by the planning documents alone.

## Evidence Count Boundaries

Do not merge these scopes:

| Scope | Verified count |
|---|---|
| Canonical Kentucky source files | 32 |
| Preserved Stage 002 ingestion run | 28 sources, 353 nodes, 121 candidate-evidence records |
| Stage 002 discovery bundles | 41 |
| Stage 003 retrieval bundles | 39 |
| Current Stage 006 output | 31 findings: S1 1, S2 17, S3 0, S4 1, S5 12 |
| Historical Sandbox 003 input | 35 findings before four regulatory-layer Smell 3 false positives were removed |
| Sandbox 004 | 3 entries rendered into 5 variants |
| Case library | 4 cases/actions and 6 gap sentinels |

The preserved ingestion run is `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/`.

## What The Audit Reconciled

- Created a root status surface and current roadmap with a scoped count table, pivot ledger, honest boundaries, and owner/review gates.
- Aligned `BOOTSTRAP.md`, all three agent entry files, `AGENT_OPERATING_MODEL.md`, `CLAUDE_CONSTRAINTS.md`, and `AGENT_CONTEXT.json` on startup order and current scope.
- Marked superseded plans, handoffs, journals, research notes, and external reports as historical or time-sensitive without deleting useful chronology.
- Documented every Sandbox 005 and 006 stage and added their missing documentation maps, handoffs, and lessons.
- Reconciled closed Sandbox 001-004 stage records and added checkbox disposition summaries to planning/stage documents.
- Reduced `BACKLOG.md` to one live next action. Closed items no longer contain hidden implementation instructions.
- Corrected ISO HO 04 93 to a roof-surfacing ACV endorsement; KFBM's base-jacket form number and text remain unknown.
- Corrected taxonomy totals to 41 claims, 43 policy, 84 combined, and 74 entries in the broader legal taxonomy.
- Reframed the USD 60,000 to USD 90,000 figure as a personal gross-income aspiration, not a per-client price or revenue forecast.
- Split production-aligned demo/pilot gates from live-production cutover gates.
- Regenerated the Stage 007 reviewer report from the current 31 findings after removing its obsolete Smell 5 zero-findings warning.

## Completed Work Not To Redo

- [x] Repository documentation inventory and classification.
- [x] Cross-agent startup and current-state reconciliation.
- [x] Sandbox 001-006 status and stage-documentation reconciliation.
- [x] Corpus, source-role, evidence-count, taxonomy-count, feasibility, and productization review.
- [x] Historical/current snapshot labeling for the 35-to-31 finding change.
- [x] Markdown planning/stage checklist audit.
- [x] Repository-wide local-link audit.
- [x] JSON/CSV parsing and evidence-artifact count validation.
- [x] Stage 007 report-builder syntax check and current report regeneration.

## Open Work

These are explicit gates, not accidental documentation loose ends:

- [ ] Owner decides when to authorize Sandbox 005 Stage 002 and `S005-PILOT-001`.
- [ ] Human completes Sandbox 006 desktop and narrow/mobile review.
- [ ] Qualified reviewers test provider-facing usefulness and ordinary-LLM substitution risk.
- [ ] Owner chooses a synthetic public demo corpus and first production-aligned surface.
- [ ] A first paid unit and live-production architecture are defined only after validation.
- [ ] Owner optionally rechecks Kentucky Growers in SERFF (`BACKLOG-003`).

## Validation

Completed during this audit:

- `AGENT_CONTEXT.json` parsed as JSON.
- `skills/registry.csv` parsed with 9 active skill rows.
- All repository Markdown local links resolved.
- All plan, phase, roadmap, and stage documents have checkbox status/disposition sections; dated journals and handoffs are not treated as plans.
- Canonical source, run artifact, retrieval bundle, finding, and case-library counts matched the current status table.
- `report_builder.py` regenerated Markdown and HTML for run `20260604_130606_18b0dec5` from 31 findings and 121 candidate-evidence records.
- Seventeen new/current control files were checked directly for CRLF and trailing whitespace; none was found.

Not performed:

- No web revalidation of dated laws, grants, competitors, program windows, salaries, prices, or market claims.
- No Sandbox 006 visual/responsive review.
- No Sandbox 005 pilot, production implementation, customer-data work, or live billing work.
- No new Stage 002 ingestion or detector run; preserved evidence artifacts remain intact.
- Repository-wide `git diff --check` was attempted but is not a usable clean signal in this already-dirty worktree: pre-existing broad CRLF conversions and captured HTML whitespace produce thousands of unrelated warnings. Those files were not normalized during this documentation task.

The worktree was already broadly dirty and contains user/generated changes outside this audit. Nothing was reverted, staged, or committed.

## Next Resume Step

Choose one gate rather than reopening completed discovery:

1. Authorize Sandbox 005 Stage 002 and follow its preflight, or
2. Perform the Sandbox 006 human review and record the result, or
3. Run one bounded provider-facing validation conversation using sanitized/synthetic evidence.

## Startup Reading List

1. `BOOTSTRAP.md`
2. `README.md`
3. `AGENT_CONTEXT.json`
4. `AGENT_OPERATING_MODEL.md`
5. This handoff
6. `BACKLOG.md`
7. The selected sandbox README, documentation map, stage plan, and latest sandbox handoff
