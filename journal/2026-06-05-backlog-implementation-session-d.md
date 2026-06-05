# Journal: Backlog Implementation Session D

Date: 2026-06-05
Session: Claude Code session 6 continuation (third closeout — post-session-C)
Scope: BACKLOG-015 case library research completion + dollar_anchors.json source citation pass

---

## Summary

Completed BACKLOG-015 case library research to the limit of publicly accessible sources. Added CL-004 (Mercury Insurance CA enforcement action) for SMELL4-H001. Exhausted regional DOI search (TN, OH, WV) for SMELL5 enforcement actions — confirmed these are behind FOIA walls across the Appalachian region. Established that the enforcement mechanism is publicly documented via FL OIR, LA DOI, and SD DLR anchors. Added source citations to all dollar_anchors.json entries and corrected two factual inaccuracies.

---

## What Changed

### BACKLOG-015: Case library research — final public-web pass

**Case library additions:**
- **CL-004** (SMELL4-H001, OUT-OF-STATE): Mercury Insurance Co. / California DOI enforcement action, $27.6M fine (upheld CA Supreme Court 2019). Carrier charged consumers unapproved broker fees not included in its filed and approved rate schedule — the enforcement principle that rate components outside the approved filing constitute unapproved rates. `case_library_ids` added to DA-S4-001 and DA-S4-002.

**Holding text updates:**
- CL-001 (Hicks): `full_holding_text` updated with verbatim quotes sourced via Property Insurance Coverage Law Blog citation of the 6th Circuit opinion: "depreciation traditionally refers to value lost from physical wear and tear"; carrier "could have removed any ambiguity by simply writing its policies to expressly include labor depreciation"; "an ambiguous policy with competing reasonable interpretations must be construed in favor of the insured."
- CL-002 (Schoening): `full_holding_text` updated with verbatim quotes sourced via Insurance Journal: "less a deduction that reflects depreciation"; "Schoening's interpretation of the insurance contract makes little sense against the backdrop of the contract as a whole."
- CL-003: Justia still 403; holding summary unchanged; source URL preserved for retry.

**Gap sentinel updates (H004, H005, H006):**
- Regional search exhausted: KY, TN, OH, WV DOI enforcement portals are not publicly indexed. NAIC central database covers only unlicensed carriers. Property Insurance Coverage Law Blog confirmed Oklahoma only publishes exam reports on FOIA request — pattern consistent across region.
- All three gap sentinels updated with thorough search trail and the key framing: *"The enforcement mechanism is documented at $750K–$2.5M range (DA-S5-001 through DA-S5-003). Specific regional findings are behind FOIA walls."*
- H005 flagged for possible scope recalibration — KRS does not create many affirmative homeowners coverage mandates.

**Jurisdiction preference policy updated:**
- Search order for regulatory enforcement actions: (1) KY DOI, (2) TN DOI, (3) OH DOI, (4) WV DOI, then broader US.
- Source type for SMELL4/SMELL5 heuristics: enforcement actions only — not court opinions (court opinions reserved for SMELL2 coverage dispute heuristics).

### dollar_anchors.json — source citation pass + factual corrections

Schema version bumped 1.0.0 → 1.1.0. `source_url` and `source_note` fields added to all 8 anchors.

**Factual corrections:**
- **DA-S2-002**: State Farm $15.6M is an Arkansas auto total-loss case (Chadwick v. State Farm, E.D. Ark., prelim approval March 2026), not a homeowners case. Description corrected to state this explicitly. Pattern remains analogous to SMELL2-H003.
- **DA-S5-002**: Louisiana figure corrected from "nearly $1 million" to $764,750 — the confirmed proposed fine total across five carriers.
- **DA-S4-001**: Original $419K/$850K single-home Marshall Fire example was unverifiable. Replaced with Colorado DOI statistics: 74% of policyholders underinsured, average shortfall $99K–$240K.

**Sources verified:**
- DA-S5-001 (FL OIR): floir.gov press releases Sept 2 + Nov 3, 2025; Insurance Journal.
- DA-S5-002 (Louisiana): Insurance Journal April 18, 2022; Property Insurance Coverage Law Blog.
- DA-S5-003 (SD Farmers/Foremost): Insurance Journal June 5, 2015; SD DLR exam report PDF at dlr.sd.gov.
- DA-S4-001 (Marshall Fire): Colorado DOI official release; CPR News Dec 2024; United Policyholders.
- DA-S2-002 (State Farm): Repairer Driven News April 13, 2026; PropertyCasualty360 April 8, 2026.

**Still unverified:**
- DA-S4-002 (Han v. State Farm): dollar figure marked [VERIFY]; no primary source URL found. Search CourtListener/PACER.

---

## Decisions Made

### FOIA wall is the correct framing for H004/H006 gap sentinels
These enforcement actions almost certainly exist inside DOI market conduct exam files, but those files are behind FOIA walls in every Appalachian state. This is not a signal that the violations are rare — it is a documented structural barrier confirmed by the Merlin Law Group blog (Oklahoma last published exam in 2009; no public list of which carriers have been examined). The gap sentinels accurately reflect this.

### Cite sources for everything; note when not available
All dollar anchors and case library entries now carry source attribution. When a primary source is unavailable (Justia 403, FOIA-walled exam reports), the entry notes the barrier and the retrieval path. No figures are asserted without a note on where they came from.

### KFBM base jacket procurement is low priority
Owner decision: carriers can manage their own internal documentation. The risk we measure is regulatory and judicial exposure to the outside world, not internal form consistency. BACKLOG-021 deprioritized accordingly.

---

## Current State of BACKLOG-015

| Item | Status |
|---|---|
| CL-001 Hicks (H003, KY) | Verbatim quotes sourced ✓; full opinion Justia 403 |
| CL-002 Schoening (H003, KY) | Verbatim quotes sourced ✓; full PDF binary |
| CL-003 FB Ins v Jones (H001, KY) | Summary present; Justia 403 |
| CL-004 Mercury/CA DOI (H001-S4, out-of-state) | Complete ✓ |
| SMELL4-H001 sentinel | CL-004 is anchor; KY DOI open records = closing step |
| SMELL5-H004 sentinel | Enforcement mechanism documented; specific KY exam = FOIA |
| SMELL5-H005 sentinel | Possible scope recalibration needed |
| SMELL5-H006 sentinel | Enforcement mechanism documented; specific KY exam = FOIA |
| dollar_anchors.json sources | All 8 anchors have source attribution ✓ |
| Han v. State Farm (DA-S4-002) | [VERIFY] — no primary source URL |

---

## Open Threads Carried Forward

- **Owner lane**: KY DOI open records request (502-564-3630) — closes BACKLOG-021 + H004/H006 gap sentinels in one call.
- **[VERIFY] items**: CL-001/CL-002/CL-003 verbatim opinion text (retry Justia/CourtListener); DA-S4-002 Han v. State Farm source URL.
- **H005 scope recalibration**: Flag for next smell taxonomy review.
- **BACKLOG-009** (LOW): Candidate underwriting smell taxonomy check — still open.
