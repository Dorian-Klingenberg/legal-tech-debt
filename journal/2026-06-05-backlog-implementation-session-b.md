# Journal: Backlog Implementation Session B

Date: 2026-06-05
Session: Claude Code session 6 continuation (compacted mid-session)
Scope: Backlog implementation, case library research, product architecture decisions

---

## Summary

Full-day implementation session completing five backlog items, establishing the case and bad-faith closure library, making two significant product architecture decisions, and closing out minor corpus cleanup. Detector count unchanged at 31 findings; two new detectors added (H007, H004) that fire zero times on current corpus as expected. Three confirmed Kentucky/Sixth Circuit cases entered into the case library. Two new backlog items added to capture discovered constraints (copyright, per-carrier reporting).

---

## What Changed

### Detectors

**BACKLOG-019: SMELL5-H007 — Missing State Amendatory** (`smell5.py`)
- Source-level scan: collects multi-state cue hits per source, checks for KY amendatory presence
- Emits one consolidated MEDIUM finding per source where multi-state cues present but no KY text found
- Run result: 0 findings (expected — current corpus has no multi-state jacket language)
- H007 will fire when a multi-state master jacket is added to corpus

**BACKLOG-020: SMELL2-H004 — Broken Definitions Loop** (`smell2.py`)
- Source-level pre-pass: identifies Definitions Section nodes, extracts quoted defined terms, cross-references body quoted terms
- Emits one LOW finding per (source, term) missing from same-source Definitions Section
- Guards against sources with no Definitions Section and sources where no terms extracted
- Run result: 0 findings (expected — base policy forms with Definitions Sections not in corpus yet)

**BACKLOG-011: Structure node pre-filter** (`detector_runner.py`)
- `_has_substantive_text()` + `_MIN_SUBSTANTIVE_CHARS = 50` constant
- 109 structure/header nodes skipped (252 → 143 carrier nodes passed to detectors)
- Total findings: 31 (unchanged); 0 short-evidence findings (was 2)

**BACKLOG-007: KRS/KAR Definitional Audit** (`KRS-KAR-DEFINITIONAL-AUDIT.md` — new)
- Searched 73 regulatory nodes for definitional context on 5 flagged terms
- Result: ZERO terms formally defined in KRS/KAR
- Critical finding: 806 KAR 12:095 § 9(2)(a) establishes mandatory ACV = RC minus depreciation AND requires explicit policy authorization for labor depreciation
- Strengthens H003 (not weakens) — carrier applying labor depreciation without explicit policy provision may violate regulation
- No severity downgrades warranted on any current finding

**806 KAR 12:095 § 9(2)(a) citation propagated:**
- `smell2.py` H003 rationale, reviewer_question, false_positive_risk updated
- `drill_down_entries.json` S4-H003-KFBM-001 updated: regulatory citation, compliance_question, remediation_note all strengthened
- Finding upgraded from disclosure gap to potential regulatory violation

### Corpus

- **ISO HO 04 93 confirmed as endorsement** (user downloaded 2-page form). HO 04 XX = ISO endorsements by convention. KFBM's corpus entry labeled "HO 04 93" is their endorsement, not their base jacket. Base jacket form number unknown.
- **ISO-HO-04-93-1000-ROOF-ACV-ENDORSEMENT.pdf** added to corpus (29 sources total)
- **BACKLOG-002**: `KY-KRS-304-12-230.html` and `KY-KRS-304-14.html` renamed to `.pdf` in `sources/`; all manifest rows updated

### Case Library

**BACKLOG-015: `sandboxes/004-expert-drilldown/data/case_library.json`** (new file)
- Schema v1.0, flat array, `is_local` flag, `dollar_anchor_id` cross-reference, `jurisdiction_preference` policy
- Source types: court_opinion, doi_enforcement_order, market_conduct_exam, class_action_filing, regulatory_settlement, naic_exam — no secondary sources
- Three cases entered (all Kentucky/Sixth Circuit — local):
  - **CL-001**: *Hicks v. State Farm Fire & Casualty Co.*, 965 F.3d 452 (6th Cir. 2020) — H003 — labor depreciation impermissible without explicit policy authorization; 65,575 KY policyholders; class certified
  - **CL-002**: *Schoening Investment LP v. Cincinnati Casualty Co.*, No. 25-3273 (6th Cir. 2026) — H003 — insurer prevailed because policy explicitly defined ACV = RC minus depreciation; validates H003 from defense side
  - **CL-003**: *FB Ins. Co. v. Jones*, 864 S.W.2d 926 (Ky. Ct. App. 1993) — H001 — undefined "reasonable time" for rebuild forced litigation; insurer lost
- Six gap sentinels with search notes recorded (H001 partial, H004/H005/H006 open)
- Full holding text fields marked [VERIFY] — Justia/CourtListener returned 403 during session

**Dollar anchor cross-references:**
- `dollar_anchors.json`: `anchor_id` fields added (DA-S2-001 through DA-S5-003); `case_library_ids` back-references added
- `case_library.json`: `dollar_anchor_id` wired on all three cases

### Report Output

- **`executive_summary_anon.md`** generated (124 lines, KNIC→Carrier A, KFBM→Carrier B). Pitch report artifact now exists.

### New Backlog Items

- **BACKLOG-022**: Commercial report copyright sanitization — carrier/ISO forms are copyrighted; verbatim text cannot appear in commercial output. `paraphrased_evidence` field + `--sanitize` flag on renderer. Prerequisite for product reports.
- **BACKLOG-023**: Per-carrier report pipeline — one pitch report (combined anonymized benchmark) + two product reports (per-carrier, named). `--carrier` filter on detector runner + report builder. Product model finalized.

---

## Decisions Made

### Product model: pitch report + two product reports (BACKLOG-023)
The combined corpus run is the benchmark/pitch artifact. Per-carrier filtered runs are the commercial deliverables. Three output modes: `--anonymize` (pitch), `--carrier KFBM` (product), `--carrier KNIC` (product). The `_is_carrier_node()` source_id prefix pattern already exists — wiring is straightforward.

### Copyright two-layer architecture (BACKLOG-022)
Carrier/ISO policy forms are copyrighted — verbatim text cannot appear in commercial output. Internal research layer retains full `evidence_text`. Commercial output uses `paraphrased_evidence` (our language, safe to reproduce). Court opinions (US) are public domain — case library full text is safe at all layers.

### ISO adopters vs. proprietary-form carriers for H004
ISO-adopting carriers (KNIC) have missing definitions covered by ISO HO 00 03 by reference — H004 is low-value for them. Proprietary-base-form carriers (KFBM) own their definition domain — H004 is highest value. Captured in H004 false_positive_risk language and BACKLOG-021.

### Case library: static pre-built, no LLM needed for retrieval
Query construction is template-driven from finding fields; CourtListener API handles case retrieval; jurisdiction filter is string matching. LLM useful only for condensing holdings — deferred. Dynamic retrieval is BACKLOG-level, not PoC-level. Full text from public domain court opinions is safe for all uses.

---

## Validation Performed

- Detector rerun after each code change: 31 findings, counts unchanged, HIGH finding intact
- H007 and H004 zero findings confirmed correct via diagnostic node content queries
- `executive_summary_anon.md` generated cleanly (124 lines)
- Corpus file renames verified via Glob

---

## Current State

| Item | Status |
|---|---|
| Detector findings | 31 (HIGH:1, MEDIUM:24, LOW:6) |
| Carrier nodes to detectors | 143 (after regulatory + structure filters) |
| H007 (State Amendatory) | 0 findings — corpus gap, correct |
| H004 (Definitions Loop) | 0 findings — corpus gap, correct |
| Case library | 3 cases (CL-001, CL-002, CL-003), 3 H001/H003 gap sentinels, 3 H004/H005/H006 open |
| Pitch report | `executive_summary_anon.md` — complete |
| Product reports | Not yet wired (BACKLOG-023) |
| Corpus sources | 29 total |

---

## Open Threads Carried Forward

- **BACKLOG-021** (owner lane): KFBM base jacket procurement — two-step (identify form number, open records request to KY DOI 502-564-3630)
- **BACKLOG-022**: Copyright sanitization — `paraphrased_evidence` schema + `--sanitize` renderer flag
- **BACKLOG-023**: Per-carrier report pipeline — `--carrier` filter on detector runner + report builder
- **BACKLOG-015 continued**: H004/H005/H006 case research — KY DOI enforcement orders, NAIC exam database
- **Case library [VERIFY] items**: Pull verbatim holding text for CL-001, CL-002, CL-003 from Justia/CourtListener
- **dollar_anchor_id cross-references**: DA-S4/S5 anchors have empty `case_library_ids` pending future H004/H005/H006 cases
- **Owner lane**: Document accessibility research project — deep research on KY DOI open records process, ISO form access, one-batch procurement strategy
- **BACKLOG-009**: Candidate underwriting smell taxonomy check — still open
- **BACKLOG-003**: Kentucky Growers SERFF recheck — still open (SFA was down)
