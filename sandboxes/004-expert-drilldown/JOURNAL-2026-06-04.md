# Journal: Sandbox 004 Session — 2026-06-04

Date: 2026-06-04 (session 5 — continuation after compaction)
Author: Dorian Klingenberg + Claude Code
Sandbox: 004 — Expert Drill-Down Report

---

## What Was Accomplished

### SERFF Search — BACKLOG-018 (ISO Base Forms)

Conducted SERFF Filing Access searches for both KNIC and KFBM in the Kentucky partition.

- **KNIC:** Form filings KNIC-132500003 (endorsement: HO 04 95 Water Backup) and KNIC-133829383 (non-renewal notice). Neither contains ISO HO 00 03 or HO 00 05. KNIC licenses ISO base forms by reference — standard industry practice.
- **KFBM:** Full form filing history inspected. KFBM uses proprietary base form HO 04 93, not ISO. Already in corpus. No independently filed ISO base forms.

**Decision:** BACKLOG-018 closed. ISO HO 00 03/05 content is established fact in insurance regulation and litigation — we do not need a copy to make findings. ADR-011 updated with this principle. KNOWN-GAPS.md ISO-HO-BASE-FORMS downgraded to LOW and noted as no longer an active collection target.

Three low-relevance corpus files added during search:
- `KY-SERFF-KNIC-132500003-HO-04-95.pdf` (endorsement)
- `KY-SERFF-KNIC-132500003-EXPLANATION.pdf` (supporting doc)
- `KY-SERFF-KNIC-133829383-NONRENEWAL-NOTICE.pdf`

SERFF Kentucky direct URL logged in CORPUS-SOURCES.md: `https://filingaccess.serff.com/sfa/home/KY` (SERFF defaults to last-used state — always use this direct link).

---

### H003 Drill-Down Entry Built

Third and final Sandbox 004 PoC entry: `S4-H003-KFBM-001`.

**Finding:** Undisclosed ACV calculation methodology — KFBM's 7-year roof rule imposes ACV loss settlement on roof surfacing without disclosing the depreciation methodology anywhere in the filed policy package. 11 SMELL2-H003 detector findings across KNIC and KFBM. KFBM primary (proprietary HO 04 93 base form; endorsed separately as "Actual Cash Value Loss Settlement — Windstorm or Hail Losses to Roof Surfacing").

**Why this is the strongest entry:** Kentucky is in a high-frequency hail/wind corridor. The 7-year rule affects the majority of the active book. The labor depreciation class-action wave (2015+) established this exact gap — ACV applied without methodology disclosure — as a material bad-faith trigger.

Entry includes full three-panel structure: compliance (KRS 304.12-230, KRS 304.20-040, 806 KAR 12:095, 806 KAR 20:010), claims (dispute scenario referencing *Henn v. American Family* and *Wilcox v. State Farm*), policy designer (redline with ACV definition, depreciation schedule citation, labor depreciation disclosure).

HTML updated with third finding card.

---

### Strategic Input — Internal Referential Integrity Framework (Jem)

Significant product strategy input received and captured. Core reframe:

**The product's ground truth is complete internal disclosure within the carrier's own filed document package — not an external standard.**

Jem identified four structural gap types that the parser should target:

1. **Phantom Form (Referential Integrity Bug):** Form referenced in schedule/booklet but PDF payload missing from SERFF attachments. → Already implemented as Smell 5 graph-gap detection (ADR-010).
2. **Broken Definitions Loop:** Defined term used in bold/quotes in policy text but absent from Definitions Section; or amendment deletes definition without replacement. → Partial implementation in Smell 2 H003.
3. **Undisclosed Rating Rules vs. Policy Constraints:** Rule Manual describes endorsement/coverage option; no corresponding form in attached schedule. → Partial implementation in Smell 4/5.
4. **Missing State Amendatory:** Multi-state master jacket filed in specific state without required state amendatory endorsement. → Not yet implemented. HIGH value, binary finding, near-zero false positives.

Engineering approach: treat each SERFF filing package as an isolated graph database. Extract manifest → cross-reference payload → flag vacuums.

**New backlog items:**
- BACKLOG-019: Missing State Amendatory detector (HIGH)
- BACKLOG-020: Tighten Broken Definitions Loop to explicit definition-graph traversal (MEDIUM)

---

### Product Scope Boundary Established

Two distinct products clearly defined:

- **Phase 1 (current):** "Here's what's missing or undisclosed in your own filed documents." Self-contained. Does not require ISO. All three Sandbox 004 entries are grounded in carrier's own SERFF filings.
- **Phase 2 (future):** "Here's exactly how you diverged from the ISO gold standard and the risk profile of each change." Requires ISO base forms. Higher value, higher build cost.

**Target carrier profile:** Carriers who diverge from ISO — at the form level (proprietary base forms like KFBM HO 04 93) or methodology level (undisclosed rating factors like Property Insurance Score). Pure ISO adopters are low-value targets.

**Sales reframe:** Not "do you use ISO forms?" but "where did you diverge from ISO, and do you know what that divergence costs you in claims exposure?"

---

### Sandbox 004 PoC Complete

All three entries built:

| Entry | Heuristic | Carriers | Finding |
|---|---|---|---|
| S4-H001-KNIC-001 | SMELL4-H001 | KNIC | Unversioned manual reference, Section 602 |
| S5-H004-KFBM-KNIC-001 | SMELL5-H004 | KFBM + KNIC | Rate methodology without regulatory citation |
| S4-H003-KFBM-001 | SMELL2-H003 (Smell 4 per ADR-011) | KFBM + KNIC | Undisclosed ACV methodology, roof surfacing 7-year rule |

Static HTML at `sandboxes/004-expert-drilldown/output/drilldown_report.html`. README created. BACKLOG-017 resolved.

---

## Decisions Made

| Decision | Rationale | Where Recorded |
|---|---|---|
| BACKLOG-018 closed — ISO forms not needed for Phase 1 | ISO content is established fact; findings are grounded in carrier's own filings | ADR-011, BACKLOG.md, KNOWN-GAPS.md |
| ISO as implicit gold standard | Carriers adopt ISO by reference; we can assert its content without holding a copy | ADR-011 |
| KFBM is higher-value target than KNIC | Proprietary base form (HO 04 93), DOI objection on file, heavier endorsement stack | SESSION-NOTES, this journal |
| Phase 1 vs Phase 2 product distinction | Phase 1 = internal disclosure gaps; Phase 2 = ISO divergence diff. Different products. | SESSION-NOTES, README |
| Internal referential integrity as core value prop | Jem framework — ground truth is complete internal disclosure, not external standard | SESSION-NOTES, BACKLOG-019/020 |

---

## Files Changed This Session

| File | Change |
|---|---|
| `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md` | Procurement URLs section added (SERFF KY direct URL, DOI portal); three new low-relevance files added |
| `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` | ISO-HO-BASE-FORMS: SERFF search outcome logged, priority downgraded to LOW |
| `corpus/kentucky-homeowners-policy-smells/sources/` | Three new PDFs: KY-SERFF-KNIC-132500003-HO-04-95, KY-SERFF-KNIC-132500003-EXPLANATION, KY-SERFF-KNIC-133829383-NONRENEWAL-NOTICE |
| `sandboxes/002-claims-regulatory-automation/adr/ADR-011-*.md` | ISO gold standard principle added; SERFF search outcome recorded; BACKLOG-018 closure noted |
| `sandboxes/004-expert-drilldown/data/drill_down_entries.json` | Third entry added: S4-H003-KFBM-001 |
| `sandboxes/004-expert-drilldown/output/drilldown_report.html` | Third finding card added (H003 ACV methodology) |
| `sandboxes/004-expert-drilldown/README.md` | Created — PoC summary, entries, product principles, source evidence |
| `BACKLOG.md` | BACKLOG-017 resolved; BACKLOG-018 closed; BACKLOG-019 and BACKLOG-020 added |
| `AGENT_CONTEXT.json` | Active sandbox updated to 004; BACKLOG-017 resolved; -019/-020 added to open threads |
| `CLAUDE.md` | Active lane updated: Sandbox 004 closed, next lane BACKLOG-019 or BACKLOG-015 |
| `SESSION-NOTES.md` | Comprehensive notes added throughout session |
