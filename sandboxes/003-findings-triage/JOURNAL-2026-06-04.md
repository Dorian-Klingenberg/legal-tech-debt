# Journal: Sandbox 003 — All Three Stages Built and Run

Date: 2026-06-04
Session: Third session of the day (Sandbox 003 build)
Author: Dorian Klingenberg + Claude Code (claude-sonnet-4-6)

---

## Session Summary

Built all three Sandbox 003 stages from scratch in a single session. Started from the stage plan scaffolded at end of the previous session. By end of session: 35 findings enriched, human-reviewed, cross-carrier analysis complete, and a prospect-facing executive summary report produced and approved.

---

## What We Did

### Stage 001: Hybrid LLM Triage

Built `stages/001-llm-triage/src/` — models, prompts, triage runner.

- Chose gpt-4o-mini (Tier 1 mechanical: plain-language explanation, false positive risk, next step) + gpt-4o (Tier 2 judgment: business severity, remediation direction, `triage_verdict`)
- Added `triage_verdict` after observing that LOW confidence + HIGH severity read as contradictory without a synthesizing sentence. Verdict field gives the reviewer one sentence combining both signals.
- `response_format={"type": "json_object"}` enforced — eliminates markdown code-fence parse failures
- `_safe()` helper added — escapes `{` and `}` in finding field values before `str.format()` to prevent KeyError from evidence text containing literal curly braces
- Switched from Anthropic SDK to OpenAI (practical constraint: only OpenAI credits available). Not an architectural decision.
- Full 35-finding run: 35/35 enriched, 0 errors

**Human review of all 35 findings:**

25 confirmed, 10 excluded:
- All 4 Smell 3 findings: false positives — detectors firing on KRS/KAR statutory nodes (reference layer only, not carrier filings)
- 3 Smell 5 findings: false positives — section headers, filing instructions, not carrier provisions
- 2 duplicates (SMELL5-H004, consolidated into patterns)
- 1 downgraded (s2-0002: "Reasonable" in KFBM → MEDIUM, not HIGH)

Root cause of nearly all false positives: detectors running on wrong node types. BACKLOG-006 (node language context annotation) would resolve this systemically.

### Stage 002: Cross-Carrier Pattern Analysis

Built `stages/002-cross-carrier/src/carrier_analysis.py`.

- Encoded human review decisions into `stages/002-cross-carrier/data/review_verdicts.json` — canonical record for downstream stages
- Grouped 25 confirmed findings by smell/heuristic across carriers
- Labeled each pattern: industry-wide (both KNIC and KFBM independently) vs. carrier-specific

Key results:
- **SMELL2-H003** (ACV / Replacement Cost): industry-wide, 5+5 = strongest signal
- **SMELL5-H004** (rate nodes, no regulatory edge): industry-wide, 1+4
- **SMELL5-H005** (mandatory coverage claims, no regulatory edge): industry-wide, 1+1
- **SMELL2-H001** ("reasonable time"): KFBM-specific, 6 findings
- **SMELL4-H001** (unversioned manual reference): KNIC-specific, 1 finding

### Stage 003: Executive Summary Report

Built `stages/003-executive-report/src/report_builder.py`.

- **Dollar anchors decision**: Stage 003 required public cost examples before it could function as a sales document. Material existed in `002-ROI-CASES-FIVE-SMELLS.md` (named cases, dollar figures, per-smell). Created `data/dollar_anchors.json` and wired into LLM narrative prompts per smell plus deterministic Risk Context section.
- **Findings table collapsed**: 25 individual rows → 6 pattern-level rows (one per confirmed heuristic). Individual findings are in the JSONL; CEO audience needs pattern-level summary.
- **H004 narrative corrected**: original prompt described "rate increases / undefined valuation terms." Corrected to "rate-setting filings with no traceable citation to KRS/KAR/DOI authority."
- **Markdown rendering fix**: `**Label ($2.575M):**` caused math-delimiter rendering corruption (spaces dropped, apostrophes replaced with prime symbol) in user's renderer. Root cause: `$` inside `**bold**` triggers math mode in some markdown renderers. Fixed by moving dollar amounts out of label fields into description plain text; format `**Label** — description (figures embedded in prose)`.

Report structure: Executive Summary → Industry-Wide Patterns → Carrier-Specific Patterns → Risk Context → Confirmed Findings → What Forward-Looking Carriers Are Doing → Methodology Note.

Human-reviewed and approved.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| `triage_verdict` field added to Tier 2 schema | LOW confidence + HIGH severity read as contradictory without synthesis — one sentence resolves confusion for reviewers |
| OpenAI SDK (not Anthropic) | Practical: only OpenAI API credits available. Swap back when Anthropic credits available. |
| Dollar anchors required for Stage 003 | Report cannot function as a sales document without cost context; material already existed |
| Findings table collapsed to 6 rows | 25 rows is a developer log, not a CEO report |
| H004 prompt rewritten | Original was factually wrong — describing the wrong smell |
| Dollar amounts removed from bold label strings | Rendering correctness across markdown renderers |

No ADRs warranted — no architectural choices between named alternatives.

---

## New Backlog Items

| ID | Priority | Description |
|---|---|---|
| BACKLOG-006 | MEDIUM | Node language context annotation — LLM pass during ingestion to classify obligation/coverage/structure nodes. Resolves 006/010/011/012 together. ADR candidate when designed. |
| BACKLOG-007 | LOW | KRS/KAR definitional cross-reference check |
| BACKLOG-008 | LOW | Smell 2/4 miscategorization — RC/ACV may be unversioned external reference = Smell 4 |
| BACKLOG-009 | LOW | Candidate new smell: Non-Deterministic Underwriting/Eligibility Criteria ("favorable impact on market value" in KNIC guidelines) |
| BACKLOG-010 | HIGH | Source ID prefix guard — skip KY-KRS-*, KY-KAR-*, KY-DOI-* in Stage 006 detectors. Quick fix. |
| BACKLOG-011 | MEDIUM | Section headers/structure nodes → minimum text length filter before detection |
| BACKLOG-012 | MEDIUM | H005 fires on filing requirements (instructions to agents), not just provisions — needs language context guard |
| BACKLOG-013 | MEDIUM | `--anonymize` flag in report_builder.py for prospect-facing versions |
| BACKLOG-014 | MEDIUM | Human editorial pass on LLM prose before any prospect use |

---

## Validation Performed

- Stage 001: 35/35 enriched findings reviewed by human — confirmed/rejected/downgraded verdicts documented in `validation/human-review-notes.md`
- Stage 002: carrier comparison output reviewed and approved
- Stage 003: full report output reviewed; markdown rendering confirmed clean with PowerShell Select-String on anchor lines

---

## Current State

All three stages complete. `003-STAGE-PLAN.md` updated with all checklists checked off through Stage 003. Handoff written at `HANDOFF-2026-06-04.md`.

Key outputs:
- `stages/001-llm-triage/output/enriched_findings.jsonl`
- `stages/002-cross-carrier/output/carrier_comparison.md`
- `stages/003-executive-report/output/executive_summary.md`

---

## What Comes Next

- [ ] BACKLOG-010 (HIGH): apply source ID prefix guard to Stage 006 detectors — quick, high-value, eliminates all Smell 3 false positives
- [ ] BACKLOG-013: `--anonymize` flag before prospect use
- [ ] BACKLOG-014: editorial pass on LLM prose
- [ ] Next lane decision: BACKLOG-010 fix + Sandbox 002 re-run, vs. Stage 003 prospect prep, vs. Sandbox 004 (UI/data view design), vs. BACKLOG-006 node annotation design
