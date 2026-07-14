# Journal: Repository Documentation Audit

Date: 2026-07-13
Scope: Entire repository documentation, agent instructions, project memory, and generated reviewer-report status

## Session Summary

This session audited the repository as a future human or agent would encounter it. The problem was not missing effort; it was that several generations of valid point-in-time notes had accumulated beside newer decisions. Counts from different pipeline stages were being compared as if they described one thing, historical handoffs still sounded current, and a few corrected assumptions remained searchable inside old records.

The result is a layered documentation model: the root `README.md` and `AGENT_CONTEXT.json` state what is current; ADRs and sandbox closure/stage documents control their domains; handoffs and journals preserve chronology; generated and external reports are evidence, not project-control surfaces.

## Inventory And Review

The review covered root instructions and research, backlog and roadmaps, Sandboxes 001-006, corpus records, project skills, feasibility studies, productization plans, journals, lessons, prior-chat indexes, and Markdown link targets. Machine-readable context, skill registry rows, corpus files, run artifacts, detector findings, and case-library counts were checked directly rather than copied from prose.

## Decisions And Corrections

### Current lanes

- Sandbox 005 is primary but owner-gated at Stage 002.
- Sandbox 006 is secondary and paused for human visual/responsive review.
- Sandboxes 001-004 are complete and preserved.
- Productization remains planning, and provider-facing demand remains unvalidated.
- BACKLOG-003 is the only open cross-sandbox backlog item.

### Scoped counts

The documentation now distinguishes 32 canonical corpus files, 28 ingested sources, 353 nodes, 121 candidate-evidence records, 41 Stage 002 bundles, 39 Stage 003 bundles, and 31 current detector findings. Sandbox 003's 35 findings are a historical pre-filter snapshot, not the current detector count.

### Source-role correction

ISO HO 04 93 is a roof-surfacing actual-cash-value endorsement. It is not KFBM's proprietary base policy. The KFBM base-jacket form number and text remain unknown, so package-completeness and definition-domain conclusions must state that limitation.

### Backlog and Phase A correction

The closed BACKLOG-005 still imposed SE coursework, a standards RAG corpus, and universal Gherkin as prerequisites. Sandbox 005 Stage 001 superseded that premise. Current repo artifacts remain the SDLC control plane; selected Agile V concepts are provisional inputs; Codex is the first engine to test; formal Phase A work has not started.

Resolved backlog items also lost stale “next action” language. Deferred designs now require an explicit future stage rather than silently remaining open.

### Commercial and production correction

The family report had transformed the USD 60,000 to USD 90,000 personal annual-income aspiration into a per-client report price and extrapolated much larger revenue. That was removed. The current argument distinguishes gross compensation, business revenue, costs, and personal income and labels all example arithmetic as unvalidated.

The production-readiness checklist now has separate gates for a production-aligned demo or controlled pilot and for live production. Local auth waivers and test/manual invoices can support a demo; they cannot support a claim that the system is ready for ordinary live customer use.

### Historical records

Old roadmaps, handoffs, journals, research reports, and external analyses were retained but labeled with their snapshot boundaries. The audit did not erase historical mistakes; it made corrections explicit at likely entry points so text search cannot safely mistake them for current truth.

## Documentation Changed And Why

- Root `README.md` and `path.md`: establish current state, pivot history, scoped counts, honest boundaries, and visible gates.
- `BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `CLAUDE_CONSTRAINTS.md`, `AGENT_OPERATING_MODEL.md`, and `AGENT_CONTEXT.json`: synchronize startup order, truth hierarchy, and current scope.
- `BACKLOG.md` and historical implementation plan: separate the one open item from resolved history and eliminate hidden queues.
- Sandbox 001-004 control and history docs: freeze completed work and label snapshot counts/assumptions.
- Sandbox 005/006 docs: complete stage maps, plans, handoffs, and lessons; make owner/review gates explicit.
- Corpus and taxonomy docs: correct source roles and count boundaries.
- Feasibility and productization docs: downgrade unverified claims, correct the personal money argument, and separate portfolio/pilot from production.
- `skills/`: repair links, mark the nine repo-visible skills active, and keep workflows cross-agent.
- `journal/` and `lessons/`: add discovery rules and the reusable documentation-drift lesson.
- Stage 007 report builder/output: replace the obsolete Smell 5 zero-findings gap note and regenerate the current report.

These are plan/status corrections and their reasons; no ADR was needed because the work reconciled existing decisions rather than selecting a new architecture between named alternatives.

## Validation Performed

- Parsed `AGENT_CONTEXT.json` successfully.
- Parsed `skills/registry.csv`: 9 rows, all active.
- Counted 32 canonical corpus files.
- Verified preserved run counts: 28 sources, 353 nodes, 121 candidate-evidence records, 55 references, 797 edges, 100 citations, and 6 preserved parse warnings.
- Verified 41 Stage 002 and 39 Stage 003 retrieval bundles.
- Verified current findings: 31 total; S1 1, S2 17, S3 0, S4 1, S5 12; HIGH 1, MEDIUM 24, LOW 6.
- Verified case library: 4 cases/actions and 6 gap sentinels.
- Ran a repository-wide Markdown local-link check with zero broken links.
- Checked plan/phase/roadmap/stage files for checkbox status sections.
- Regenerated Stage 007 Markdown/HTML from the current findings and candidate evidence.
- Checked 17 new/current control files directly for CRLF and trailing whitespace; none was found.

## Intentionally Not Done

- Dated external market, legal, grant, salary, pricing, and competitor claims were labeled for revalidation rather than silently presented as current. No web research was performed in this documentation pass.
- The Sandbox 006 visual review remains a human gate.
- Sandbox 005 Stage 002 remains unstarted because the owner has not authorized it.
- The preserved Stage 002 ingestion run and detector artifacts were not rewritten.
- No unrelated dirty-worktree changes were reverted, staged, or committed.
- A repository-wide `git diff --check` was attempted, but the pre-existing dirty worktree contains broad CRLF conversions and captured HTML whitespace that produce thousands of unrelated warnings. The audit did not normalize those files.

## Current Open Gates

- [ ] Owner authorizes Sandbox 005 Stage 002 when ready.
- [ ] Human completes Sandbox 006 visual/responsive review.
- [ ] Qualified reviewers test provider-facing usefulness and generic-LLM substitutability.
- [ ] Owner chooses a synthetic public demo and first product unit.
- [ ] BACKLOG-003 receives an optional second SERFF search.

These are conscious decisions or validation needs. They are not documentation omissions.
