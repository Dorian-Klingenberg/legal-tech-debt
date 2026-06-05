# Project Backlog

Status: Active
Scope: Cross-sandbox items with no current sandbox home
Last updated: 2026-06-04 (session 2)

This file tracks open questions, deferred tasks, and homeless backlog items — things that are real enough to record but not yet assigned to a sandbox or stage. Items are checked off when resolved, not deleted, so the search history stays visible.

Implementation brief: see `BACKLOG-IMPLEMENTATION-PLAN.md` for Claude-ready instructions, file allowlists, validation commands, and item-by-item acceptance criteria for currently unblocked backlog work.

---

## Open Items

### [x] BACKLOG-001: Smell 5 Detector Calibration — RESOLVED 2026-06-04

**Status:** Open — no sandbox assigned  
**Affects:** Sandbox 002 Stage 006; Sandbox 003 five-smell completeness claim  
**Priority:** Must resolve before claiming five-smell completeness

The Regulatory Mapping smell detector (Smell 5) produces zero findings on the expanded 28-source corpus (run `18b0dec5`). This is almost certainly under-recall from uncalibrated heuristics, not a clean negative result.

**What we know:**
- The most promising targets are the KFBM DOI objection response and rate manual filings, which should contain KRS/KAR citation gaps the current heuristics are not firing on.
- ADR-009 formally records this as a known limitation and a non-blocker to starting Sandbox 003.
- Sandbox 003 must not claim five-smell completeness until this is resolved.

**Diagnosis (2026-06-04):** Zero raw pattern matches across all 353 nodes — not a filtering bug. Carrier policy forms don't use "as required by state law" language; the smell requires semantic retrieval to surface. This is the documented BM25 failure that earns Stage 005 re-evaluation. Stage 005 formally reopened.

**Architecture decision (ADR-010, 2026-06-04):** Vector similarity cannot detect absence. Smell 5 requires graph-based gap detection — identify carrier nodes making regulatory-sounding claims, then check for missing outbound edges to KRS/KAR/DOI/SERFF nodes. See `adr/ADR-010-smell5-retrieval-architecture-gap-detection.md`.

**Resolution:** Detector rebuilt as two-tier (H001-H003 lexical + H004-H006 graph gap). H004-H006 emit one consolidated finding per source with supporting_nodes. Detectors rerun: 12 Smell 5 findings (7 MEDIUM, 5 LOW) across KNIC and KFBM. Stage 007 report regenerated: 35 total findings. Five-smell coverage is now complete for the current corpus.

---

### [x] BACKLOG-002: Corpus File Extension Mismatches — RESOLVED 2026-06-05

**Status:** Open — low priority  
**Affects:** Corpus parsing warnings; no stage is currently blocked

Two corpus files are named `.html` but contain PDF content:
- `KY-KRS-304-12-230`
- `KY-KRS-304-14`

A third file with the same issue (`KY-KRS-304-13`) was already renamed. The pipeline parses these with warnings and does produce nodes, so nothing is blocked.

**Resolution (2026-06-05):** Both files renamed to `.pdf` in `corpus/kentucky-homeowners-policy-smells/sources/`. All manifest rows updated (replace_all — files appear under multiple smell directories). Stage 002 rerun to confirm warnings clear is deferred to next pipeline run.

---

### [ ] BACKLOG-003: Kentucky Growers Insurance Company (KGIC) SERFF Search

**Status:** Open — no filings found in SFA  
**Affects:** `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` (Gap ID: KY-SERFF-KGIC-POST2018)

**Search history:**
- 2026-06-03: User searched SERFF Filing Access for Kentucky Growers Insurance Company homeowners/dwelling filings (KY, TOI 04.0/04.1). No entry found — carrier may not file homeowners in SERFF or may file under a different name.
- 2026-06-04: Attempted recheck to confirm — SERFF Filing Access site was down.

**What we know:**
- This is not "manual retrieval required" — it is "searched and came up empty."
- Until the site is back up and a confirmed second search is run, treat as likely not present in SFA.
- Low urgency: the current KNIC and KFBM corpus is sufficient for Sandbox 003.

**Next action:** When SFA is back up, rerun the search: State = Kentucky, TOI = 04.0 then 04.1, Company = "Growers" / "Kentucky Growers". If still no results, close this gap as not available in SFA and update `KNOWN-GAPS.md`.

---

### [x] BACKLOG-004: Stage 005 Semantic Retrieval Re-open Conditions — RESOLVED 2026-06-04

**Status:** Open — one of three gates met  
**Affects:** Sandbox 002 Stage 005; ADR-002; vector store selection (ADR-005)

Re-opening semantic retrieval requires all three conditions:
- [x] Second carrier homeowners corpus present (KFBM added 2026-06-03)
- [ ] At least one gold set item written as a plain-English reviewer paraphrase query (not document vocabulary)
- [ ] At least one documented BM25 failure that a concept-level query would fix

**What we know:**
- BM25 currently hits 21/21 (100%) on the existing gold set, but the gold set queries are written in document vocabulary, making it an unfairly easy test for BM25.
- Semantic retrieval scored 76% on the same queries — not because embeddings are weak, but because the queries are phrase-matchable.
- A fair evaluation needs reviewer-style paraphrase queries and a real BM25 miss.

**Resolution:** All three conditions met 2026-06-04. Five Smell 5 paraphrase queries approved. Stage 005 formally reopened. See BACKLOG-001 for next steps.

---

### [ ] BACKLOG-006: Node Provision-Type Classification in Stage 002 Ingestion

**Status:** Open — no sandbox assigned  
**Affects:** Sandbox 002 Stage 006 detectors (Smell 1 specifically); any future smell whose heuristics depend on distinguishing exclusions from conditions/duties/definitions  
**Priority:** Medium — do not attempt until a validation approach is designed

**What we know:**
The Stage 002 ingestion pipeline assigns every parsed section a `node_type` (document, section, subsection) but not a **provision type** — whether the section is a coverage grant, exclusion, condition, duty of the insured, definition, rate rule, etc. Smell 1 detectors compensate by checking for exclusion keywords in proximity to the broad-subject pattern, but this is fragile: a "Duties After Loss" condition that ends with "this policy shall provide no coverage for such claims" passes the proximity check and fires as an overbroad exclusion even though it is a notice provision, not a coverage exclusion.

**What the fix is NOT:** Restricting Smell 1 detectors to "exclusion nodes only" would suppress real findings. Coverage forms frequently mix coverages and exclusions in the same section, and broad language in a coverage grant can indirectly create the same ambiguity as an overbroad exclusion. The detector should run on all coverage-document nodes.

**What the fix IS:** The detector fires identically whether broad language appears in (a) a coverage grant, (b) an exclusion, or (c) a condition with a coverage consequence — but these three contexts carry different risk profiles and warrant different reviewer questions. The output needs to communicate which context the finding is in so a reviewer knows what to do with it.

This likely requires LLM-assisted context classification at the node level during ingestion — not a provision-type enum, but a short characterization of how the broad language is functioning in context. A deterministic rule cannot reliably make this distinction across varied carrier form formats.

**Next action:** Design a node-level context annotation approach — likely a lightweight LLM pass during Stage 002 ingestion that adds a `language_context` field (e.g., "coverage grant", "exclusion", "condition with coverage consequence", "ambiguous") to each node. Validate on a hand-labeled sample before using it to gate or weight detector output. Assign to a new sandbox stage when ready.

---

### [x] BACKLOG-010: Smell Detectors Must Not Fire On Statutory/Regulatory Corpus Nodes — RESOLVED 2026-06-04

**Status:** Resolved — short-term fix applied  
**Affects:** All smell detectors in Stage 006; Sandbox 003 Stage 001 output  
**Priority:** High — directly produces false positives that would appear in a client report

**What we know:**
All four Smell 3 findings in the current run are on KRS/KAR statutory and regulatory nodes. The smell detectors have no guard against firing on reference-layer sources. The statutory/regulatory corpus (KY-KRS-*, KY-KAR-*, KY-DOI-*) exists to check carrier filings *against*, not to be analyzed for smells itself. Suggesting a carrier "clarify the exceptions" in a Kentucky statute is not actionable and would undermine a client report.

The immediate cause is that `source_type` is blank for all statutory/regulatory nodes — it was never populated during ingestion — so detectors cannot guard on it.

**Short-term fix (Sandbox 002 Stage 006):** Add a source ID prefix guard to all detectors: skip any node whose `source_id` starts with `KY-KRS-`, `KY-KAR-`, or `KY-DOI-`. Fast and reliable without a schema change.

**Long-term fix (Stage 002 ingestion):** Populate `source_type` correctly for all sources during ingestion. The corpus manifest (`CORPUS-SOURCES.md`) already classifies each source — that classification should flow through to every node as a first-class field. Detectors then guard on `source_type not in {ky_statute, ky_regulation, doi_bulletin, doi_guidance}`.

**Resolution (2026-06-04):** Short-term source ID prefix guard applied in `detector_runner.py`. `_REGULATORY_PREFIXES = ("KY-KRS-", "KY-KAR-", "KY-DOI-")` tuple and `_is_carrier_node()` predicate added. Runner now filters regulatory nodes before passing to detectors, logs skip count. Eliminates all four Smell 3 false positives. Long-term `source_type` ingestion fix remains open in the Stage 002 ingestion backlog.

---

### [x] BACKLOG-007: KRS/KAR Definitional Cross-Reference Check — RESOLVED 2026-06-05 (audit phase)

**Status:** Open — no sandbox assigned  
**Affects:** Sandbox 002 Stage 006 detectors (Smell 2 specifically); Stage 003 severity ratings  
**Priority:** Medium — affects severity of multiple findings before they reach a client report

**What we know:**
During Sandbox 003 Stage 001 human review, "reasonable time" was flagged in six Smell 2 findings (all in roof surfacing / windstorm-or-hail loss settlement conditions across KNIC and KFBM). The LLM rated these HIGH severity, but "reasonable time" may be defined in Kentucky statute or regulation — KRS or KAR. If a statutory definition exists, carriers can rely on it without restating it in the filing, and the finding drops significantly in severity.

The same issue applies to other common insurance terms flagged by Smell 2 heuristics: if KRS/KAR provides a definition, the absence of an in-filing definition is not a smell.

**What the fix is:** Build a reference lookup during Stage 006 detection (or as a post-detection enrichment step) that checks whether a flagged term appears in the Kentucky statutory/regulatory corpus already in the graph. If a definitional edge exists in the corpus from a statutory node, the finding confidence and severity should be downweighted accordingly.

**Audit result (2026-06-05):** Zero terms formally defined in KRS/KAR corpus. Key finding: 806 KAR 12:095 Section 9(2)(a) establishes a mandatory ACV calculation standard ("replacement cost minus depreciation") and requires explicit policy authorization for labor depreciation. This STRENGTHENS H003 findings — not weakens them. Full audit: `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/KRS-KAR-DEFINITIONAL-AUDIT.md`. No severity downgrades warranted. Graph-lookup enrichment (Stage 007) deferred — design when ready.

---

### [x] BACKLOG-008: Smell 2 / Smell 4 Miscategorization — External Valuation References — RESOLVED 2026-06-04 (ADR-011)

**Status:** Resolved — see ADR-011  
**Affects:** Sandbox 002 Stage 006 H003 findings; Sandbox 004 drill-down report framing  
**Resolution:** H003 findings reclassified to Smell 4. The finding is not "ACV is undefined" — it is "the ACV calculation methodology (whether labor is depreciated, which tool or index is used) is not disclosed in the filing." This framing survives professional scrutiny; the "undefined term" framing does not. See ADR-011 for full decision record.

**What we know:**
During Sandbox 003 Stage 001 human review, "replacement cost" findings were assessed as real but potentially miscategorized. Replacement cost is often calculated using an external tool (e.g., Xactimate, CoreLogic, Marshall & Swift) at time of policy issuance. If the carrier uses such a tool but does not cite it in the filing, the term is not undefined — it is externally defined but untraceable from the filing. That is a Smell 4 pattern (Calculation Rule Drift / Unversioned Rate Reference), not a Smell 2 pattern (undefined magic term).

**What the fix is:** Add a cross-check in Smell 2 detection: if a flagged valuation term appears near a rate manual computation rule with no citation to an external source or versioned reference, tag the finding as a potential Smell 4 overlap and adjust the reviewer question accordingly.

**Next action:** In Stage 003 report, note for replacement cost findings that the carrier may be using an external valuation tool not cited in the filing — recommend verifying the rate manual or endorsement references a specific tool or version. Longer term, refine Smell 2 / Smell 4 heuristic boundary in a future Sandbox 002 stage.

---

### [ ] BACKLOG-009: Potential New Smell — Non-Deterministic Underwriting Criteria

**Status:** Open — candidate smell, not yet validated  
**Affects:** Future sandbox scope; smell taxonomy  
**Priority:** Low — record for taxonomy review, do not act on yet

**What we know:**
During Sandbox 003 Stage 001 human review, finding s2-0002 was assessed as a false positive for Smell 2 but pointed to a potentially distinct smell: vague underwriting eligibility language. The KNIC rate manual describes favorable risk characteristics as "Located in stable or improving area with favorable impact on market value" — "favorable impact" is not defined and "stable or improving area" has no measurement standard attached.

This is not a claims-layer smell (it doesn't affect how a claim is paid). It is an underwriting-layer smell: non-deterministic eligibility criteria that give the carrier discretion to accept or decline risks without an objective, reproducible standard. A claimant who is denied coverage renewal or surcharged for a territory change cannot verify whether the criterion was applied consistently.

This belongs in the smell taxonomy as a candidate new class: **Non-Deterministic Underwriting / Eligibility Criteria** — underwriting rules that use subjective, unanchored language to make coverage eligibility or pricing decisions.

**Next action:** Review the smell taxonomy (`legal_code_smell_taxonomy.md`, `insurance_policy_smells.md`) for whether this class already exists under a different name. If not, draft a candidate smell definition and add to the taxonomy for review. Do not build detectors until the taxonomy entry is approved.

---

### [x] BACKLOG-011: Filter Section Headers and Document Structure Nodes Before Smell Detection — RESOLVED 2026-06-05

**Status:** Open — Sandbox 002 Stage 006 fix  
**Affects:** All smell detectors; produces noise findings with no actionable content  
**Priority:** Medium — straightforward fix, directly reduces false positive count

**What we know:**
Several findings have evidence text that is purely structural — a section header ("Roof Surface Loss Settlement"), a table-of-contents entry, or a document title. These nodes contain no substantive policy language. Running smell detectors on them produces findings with no meaningful evidence text and no actionable remediation.

**Fix applied:** `_has_substantive_text()` helper and `_MIN_SUBSTANTIVE_CHARS = 50` constant added to `detector_runner.py`. Strips section heading from node text, checks remainder >= 50 chars. 109 structure/header nodes now skipped (252 → 143 carrier nodes passed to detectors). Total findings unchanged at 31; 0 short-evidence findings (previously 2). HIGH finding SMELL4-H001 confirmed intact. Two consolidated Smell 5 findings now show substantive evidence text instead of section headers.

---

### [ ] BACKLOG-012: H005 Fires on Statements of Filing Requirement, Not Just Statements of Provision

**Status:** Open — Sandbox 002 Stage 006 detector refinement  
**Affects:** Smell 5 H005 heuristic; affects finding quality in client reports  
**Priority:** Medium — affects how mandatory-coverage findings are interpreted

**What we know:**
H005 fires on "mandatory" language near coverage terms, but two distinct contexts produce that pattern:
1. **Statement of provision** — a policy provision asserting that certain coverage is required under regulatory authority (a real smell if no regulatory citation exists)
2. **Statement of filing requirement** — a rate manual instruction telling agents how to structure a policy (e.g., "Section II Coverage is not mandatory for the secondary residence policy")

The second context is not a regulatory mapping smell. It is a filing instruction. To confirm a real problem in that context, you would need to compare against an actual issued policy. The current heuristic cannot distinguish the two.

**Fix:** Likely the same node-level language context annotation approach as BACKLOG-006 and BACKLOG-012 — a lightweight LLM pass during ingestion that characterizes whether "mandatory" language is a coverage provision or a filing/underwriting instruction. Until then, H005 findings should be flagged in the report as requiring policy-instance verification before escalation.

---

### [x] BACKLOG-013: Stage 003 Report — Carrier Name Anonymization — RESOLVED 2026-06-04

**Status:** Resolved  
**Affects:** `stages/003-executive-report/src/report_builder.py`; Stage 003 output  
**Priority:** Medium — required before this report goes in front of a prospect who doesn't know the carriers

**What we know:**
The carrier-specific patterns section names KNIC and KFBM explicitly. For internal analysis this is correct. For a prospect pitch to a carrier that doesn't know those names, it is a distraction and may raise questions about data sourcing. The report should have a mode that replaces carrier names with generic labels ("Carrier A", "Carrier B") or "one of the carriers analyzed."

**Resolution (2026-06-04):** `--anonymize` flag added to `report_builder.py`. `CARRIER_LABELS_INTERNAL` (identity map) used by default; `CARRIER_LABELS_ANON` (`KNIC→Carrier A`, `KFBM→Carrier B`) used when flag is set. Labels threaded through `apply_verdicts()`, `build_findings_table()`, and `build_report()`. Anonymized run writes to `executive_summary_anon.md`; internal run writes to `executive_summary.md`. LLM narrative sections were already anonymous. Decision: build-time flag (not post-processing) — two output files coexist.

---

### [x] BACKLOG-014: Stage 003 Report — LLM Prose Quality Improvement — RESOLVED 2026-06-04

**Status:** Resolved — direct editorial pass applied  
**Affects:** `stages/003-executive-report/src/report_builder.py` narrative prompts  
**Priority:** Low — current prose is serviceable but generic; a human editorial pass would significantly improve it

**What we know:**
The current executive intro and closing use generic phrases ("crucial insights," "evolving landscape," "strategic priority") that read like competent but unedited LLM output. The pattern narratives are more grounded but still slightly formal.

**Two approaches:**
1. Tighter prompts — add explicit constraints against filler phrases, require concrete specifics, provide sentence-level examples of the desired register
2. Human editorial pass — treat LLM output as a first draft, edit in place before distribution

Both are needed. Option 2 is essential for any client-facing version regardless of prompt quality.

**Resolution (2026-06-04):** Direct editorial pass applied to `executive_summary.md` (12 targeted replacements). Removed all boilerplate openers/closers ("rapidly evolving landscape", "cannot be understated", "showcasing a proactive stance", etc.). Replaced heuristic-ID technical openers in pattern narratives. Fixed typo "undocumentated". Tightened H003/H004/H005 paragraph 2 closers. Fixed dangling clause in H003-p2. Report is now prospect-ready for a final human read. Prompt improvement (Option 1) deferred — not needed before this report ships.

---

### [ ] BACKLOG-015: Heuristic-Specific Case and Bad-Faith Closure Library

**Status:** Open — no sandbox assigned  
**Affects:** Stage 003 executive report; sales materials; dollar_anchors.json  
**Priority:** High for sales readiness — current anchors are real but pattern-general; heuristic-matched cases are materially stronger in a prospect conversation

**What we want:**

The current Risk Context section uses real public events (labor depreciation class actions, State Farm ACV settlement, Florida OIR fines) but they map to broad smell categories, not to the specific gaps we detected. A prospect CCO will ask: "Did this exact problem — undefined 'reasonable time' in a roof settlement condition — actually cause a payout dispute in court?" We should be able to answer that with a case citation, not a general category.

For each active heuristic, find at least one real public case or documented bad-faith closure where the specific language gap drove the dispute outcome:

| Heuristic | Specific gap | Target case type |
|---|---|---|
| SMELL2-H001 | "Reasonable time" undefined in roof/windstorm loss settlement — controls ACV vs. replacement cost cutoff | Court ruling or arbitration where timing ambiguity in a hail/roof claim led to underpayment dispute or bad-faith finding |
| SMELL2-H003 | ACV or replacement cost used without a stated calculation methodology | Case where the carrier's undisclosed depreciation method or valuation tool was the contested issue — not just that ACV was low, but that the method was opaque |
| SMELL4-H001 | Rate manual referenced as "the Manual" with no version, edition, or date | Case or DOI enforcement action where an unversioned external reference was the basis for a disputed rate application or retroactive rate change |
| SMELL5-H004 | Rate-setting nodes with no traceable KRS/KAR/DOI citation | Market conduct exam finding or DOI order where a carrier's rate methodology lacked a regulatory anchor and was ordered revised or refiled |
| SMELL5-H005 | Mandatory coverage assertion with no regulatory citation | Case where a carrier denied a claim on the basis that a coverage was optional, and the dispute turned on whether the regulatory mandate existed |
| SMELL5-H006 | Loss settlement methodology section with no regulatory citation for the settlement approach | Case where the settlement method itself (not just the dollar amount) was contested and the carrier could not cite authority for the approach used |

**Output format:**

For each heuristic, a structured entry suitable for inclusion in `dollar_anchors.json` and the executive report:
- Case name / enforcement action identifier (public record only)
- Jurisdiction and year
- The specific language gap that drove the dispute
- Outcome (settlement amount, fine, order to refile, bad-faith verdict)
- One-sentence connection to the heuristic

**Sources to search:**
- Westlaw / Lexis (if available) — Kentucky homeowners, property insurance, bad faith
- State DOI enforcement orders (Kentucky DOI, Florida OIR, Louisiana DOI, others with public records)
- NAIC market conduct exam results database
- Publicly reported class action filings (PACER, news sources)
- Insurance coverage law blogs and trade press for documented bad-faith closures

**Scope constraint:** Public records only. No confidential claim data. No invented or synthesized cases. If a heuristic has no documented case yet, record that explicitly — a known gap in the case library is still useful signal.

**Progress (2026-06-05, session C):**
- `sandboxes/004-expert-drilldown/data/case_library.json` created — schema v1.0, flat array, dollar_anchor_id cross-reference, `is_local` flag, jurisdiction_preference policy.
- Source types: court_opinion, doi_enforcement_order, market_conduct_exam, class_action_filing, regulatory_settlement, naic_exam — NO secondary sources.
- **CL-001** (H003, LOCAL): Hicks v. State Farm Fire & Casualty Co., 965 F.3d 452 (6th Cir. 2020) — 65,575 KY policyholders, labor depreciation impermissible without explicit policy authorization. full_holding_text updated with verbatim quotes sourced via Property Insurance Coverage Law Blog citation. [VERIFY full opinion text — Justia 403]
- **CL-002** (H003, LOCAL): Schoening Investment LP v. Cincinnati Casualty Co., No. 25-3273 (6th Cir. 2026) — insurer prevailed because policy explicitly defined ACV as RC minus depreciation. full_holding_text updated with verbatim quotes sourced via Insurance Journal. [VERIFY full opinion — CourtListener PDF binary]
- **CL-003** (H001, LOCAL): FB Ins. Co. v. Jones, 864 S.W.2d 926 (Ky. Ct. App. 1993) — undefined "reasonable time" in rebuild condition forced litigation. [VERIFY — Justia 403]
- **CL-004** (SMELL4-H001, OUT-OF-STATE): Mercury Insurance Co. CA DOI enforcement action, $27.6M fine (2019) — carrier charged unapproved rate components not included in filed rate schedule. Out-of-state precedent that rate components outside the approved filing constitute unapproved rates. dollar_anchor_id: null (cross-references DA-S4-001 and DA-S4-002 via case_library_ids added to dollar_anchors.json).
- **Gap sentinels** updated with thorough search notes for H001, H004, H005, H006:
  - SMELL4-H001: CL-004 is best anchor; KY DOI exam reports not publicly indexed
  - SMELL5-H004: No enforcement action found; KY DOI open records request is the next step
  - SMELL5-H005: H005 scope may need recalibration — likely a regulatory-citation gap, not a mandatory-coverage gap
  - SMELL5-H006: Hicks/Schoening are closest but don't hit H006 directly; KY DOI open records is next step

**Blocking gap (all open heuristics):** KY DOI market conduct exam reports are NOT publicly indexed online. The exam results portal (`insurance.ky.gov/mc/default.aspx`) returns 404. Finding exam-based enforcement actions requires an open records request (502-564-3630). This is BACKLOG-021 territory.

**Next actions (remaining):**
- [owner lane] Open records request to KY DOI for market conduct exam reports on KFBM and KNIC — this is the only viable path to SMELL5-H004/H006 enforcement examples.
- [agent] Retry Justia for CL-001 and CL-003 verbatim text when 403 clears.
- [agent] Extract CL-002 verbatim text from CourtListener PDF (downloaded as binary; needs PDF reader pass).

---

### [x] BACKLOG-016: Dollar-Sign Rendering Guard in report_builder.py — RESOLVED 2026-06-04

**Status:** Open — low priority, defensive hardening  
**Affects:** `stages/003-executive-report/src/report_builder.py` — `build_risk_context_section()` and `build_report()`  
**Priority:** Low — source data in `dollar_anchors.json` is already fixed; this prevents the same bug from re-entering via future data edits

**What we know:**
Dollar signs (`$`) inside markdown bold strings and blockquotes are interpreted as math delimiters by renderers that support LaTeX (GitHub, Obsidian, some PDF converters). The pattern `$X ... $Y` renders the content between the two signs as a math expression rather than plain text. This has now surfaced twice:
- First: bold label strings in the findings table (fixed by removing `$` from labels)
- Second: the blockquote ROI pitch and portfolio framing range strings (fixed by rewriting values in `dollar_anchors.json`)

The current fix lives in the data. The right fix is also in the code.

**What the fix is:** Add a `_safe_dollar(text: str) -> str` helper to `report_builder.py` that replaces bare `$` followed by a digit or letter with an escaped or reworded form before writing into markdown output. Apply it in `build_risk_context_section()` wherever `anchor["dollar_figure"]`, `r["annual_estimate"]`, `r["ten_year_range"]`, and `pf["conservative_pitch"]` are interpolated into markdown strings. The simplest safe form: strip `$` from numeric strings and append `USD` where needed (matching what the data now contains).

**Resolution (2026-06-04):** `_safe_dollar()` helper added to `report_builder.py`. Regex `\$(\d[\d,./KMBkmbillion]*)` strips bare `$` signs from all numeric amounts. Applied to the complete report string after `build_report()` and before writing — covers LLM prose and deterministic sections equally. Removed 13 dollar signs from `executive_summary.md` in the same pass. Future builds generate clean output automatically.

---

### [x] BACKLOG-017: Expert Drill-Down Report — Finding-Level Technical Brief with Suggested Fixes — RESOLVED 2026-06-04

**Status:** PoC complete — Sandbox 004  
**Affects:** New output layer on top of Sandbox 002/003 findings  
**Priority:** CRITICAL — resolved

**Strategic framing:**
The executive summary is the sales instrument — it gets a CEO or CCO to the table. The drill-down report is the service itself — the deliverable a carrier pays for. The distinction matters for how we build it: the executive summary can be generated once and reused as a prospect hook; the drill-down must be carrier-specific, finding-specific, and actionable enough that an expert can hand it to a policy revision team and get a concrete result.

**The readers (all three must be served):**
- **Compliance officer / coverage attorney** — needs regulatory grounding, exact filing citations, and defensible suggested language. Their question: "what do I need to change and what authority supports the change?"
- **Claims professional** — needs to understand how each gap affects claim handling and dispute exposure. Their question: "which of these gaps is most likely to generate a bad-faith exposure or a reopened claim, and how does the current language let a claimant challenge a settlement?"
- **Policy designer / filing specialist** — needs proposed redlines or remediation templates they can actually implement. Their question: "what does the corrected language look like, and does it require a new DOI filing?"

Each reader may use a different section of the same report, or the report may eventually support role-based filtering. The proof-of-concept should serve all three with a single document structure before considering role-specific views.

**What the expert reader needs (all three roles):**
- The exact policy language that triggered the finding, verbatim and in context
- The specific section, endorsement, or rate manual page it came from
- A precise statement of what the problem is (not the smell category — the actual gap)
- The regulatory standard the language should be measured against (KRS/KAR/DOI citation where available)
- A suggested fix — either a concrete proposed redline or a description of what compliant language typically includes
- Enough sourcing that they can hand it to outside counsel without re-doing the research

**What "suggested fixes" means (to be validated in proof-of-concept):**
Two possible levels — both worth exploring:
1. **Redline suggestion** — proposed replacement language: "replace 'reasonable time' with 'within 60 days of the carrier's written request for documentation, or as otherwise required by KRS 304.12-230'" — concrete, actionable, auditable
2. **Remediation template** — "this section requires a valuation methodology; compliant language typically includes: (a) the calculation basis (ACV vs. RC), (b) the external tool or index used if any, (c) the effective date of that reference" — gives the expert a checklist rather than a redline

Both may be appropriate for different finding types. Smell 4 (unversioned rate reference) lends itself to a redline. Smell 2 (undefined valuation term) may need a template because the right methodology varies by carrier.

**Relationship to existing outputs:**
- Source data: `enriched_findings.jsonl` (Sandbox 003 Stage 001) — already has plain-English descriptions, dispute scenarios, confidence ratings
- Source data: `detector_findings.jsonl` (Sandbox 002 Stage 006) — has verbatim evidence text, node IDs, source IDs, section paths
- Source data: `carrier_comparison.json` (Sandbox 003 Stage 002) — has confirmed heuristics and carrier scope
- The drill-down report is a new assembly layer over these existing artifacts — it does not require re-running detection

**Likely output format:**
A structured markdown (or HTML) document with one section per confirmed finding or finding group, containing: finding ID, heuristic, source document, section path, verbatim evidence, gap statement, regulatory reference, and suggested fix. Possibly also a machine-readable JSON companion for future UI integration.

**Proof-of-concept scope:**
Start with the three highest-severity confirmed findings (SMELL2-H003, SMELL4-H001, SMELL5-H004) and hand-build one example drill-down entry each. Validate the format with a human expert read before building the pipeline. The suggested-fix language will require LLM assistance plus human review — it must not be presented as legal advice.

**Open design questions (for the proof-of-concept phase):**
- Redline vs. template vs. both — depends on finding type
- How to source suggested fix language — LLM draft + human review, or curated from regulatory text in the corpus?
- Disclaimer language — fixes are editorial suggestions, not legal advice; how prominent?
- Whether carrier names appear (internal version) or are anonymized (external version) — same `--anonymize` flag pattern as the executive summary
- Output format — markdown, HTML, Word doc, or all three

**Next action:** Open a new sandbox (Sandbox 004) or Stage 004 in Sandbox 003. Build one hand-crafted example entry per priority finding type. Review with a human expert. Then decide whether the fix-suggestion pipeline is LLM-driven or template-driven before building at scale.

---

### [x] BACKLOG-018: Procure ISO HO 00 03 and HO 00 05 Base Policy Forms — CLOSED 2026-06-04

**Status:** Closed — ISO base forms treated as implicit gold standard; procurement not required  
**Affects:** Corpus completeness; ADR-011 evidentiary completeness  
**Priority:** Resolved

**What we need:**

The base ISO homeowners policy forms for the carriers in our corpus:
- **ISO HO 00 03** — Homeowners 3 Special Form (the most common; covers all-risk dwelling + named-peril personal property)
- **ISO HO 00 05** — Homeowners 5 Comprehensive Form (all-risk on both dwelling and personal property)

These forms contain the definitions section where ACV is defined, and the base coverage structure that all endorsements amend.

**Why this is no longer a blocker (decided 2026-06-04):** The H003 finding per ADR-011 is "undisclosed ACV calculation methodology," not "undefined ACV term." ISO HO 00 03 defines ACV — that is established industry and litigation fact that does not require us to hold a copy. The finding survives regardless: nowhere in the filed policy package does the carrier disclose *how depreciation is calculated* (specifically, whether labor can be depreciated). For KFBM, HO 04 93 is already in corpus and can be verified directly. For KNIC, we can accurately state that ISO HO 00 03 defines ACV but does not specify depreciation methodology — a gap documented in years of class action litigation — without holding the document. ISO forms are needed only if we want to do a verbatim corpus comparison, which is a nice-to-have, not required for the drill-down report.

**Progress:**

- [x] SERFF/KNIC — searched form filings KNIC-132500003 and KNIC-133829383 (2026-06-04). Neither contains HO 00 03 or HO 00 05. KNIC-132500003 is an endorsement filing (HO 04 95 water backup); KNIC-133829383 is a non-renewal notice. KNIC licenses ISO forms by reference — they are not independently filed. Files added to corpus as low-relevance entries.
- [ ] SERFF/KFBM — search KFBM form filings for any "base form" or "HO 00" attachment
- [ ] Kentucky DOI public portal — `https://insurance.ky.gov` form database
- [ ] ISO directly — subscription service; HO 00 03 (ed. 10 05) and HO 00 05 (ed. 10 05)

**Where to look (remaining, in priority order):**

1. **SERFF/KFBM** — search KFBM form filings, TOI 04.0/04.1, filing type "New" or "Adoption." KFBM may have filed base forms separately.
2. **Kentucky DOI public rate/form portal** — check `https://insurance.ky.gov` for a public forms database.
3. **ISO directly** — ISO forms are copyrighted but available to subscribers.

**What to do when found:**
- Add to `corpus/kentucky-homeowners-policy-smells/sources/` following existing naming conventions
- Update `_download_manifest.csv`
- Update `KNOWN-GAPS.md` — close gap ISO-HO-BASE-FORMS
- Re-inspect the definitions sections for ACV, replacement cost, and actual cash value language
- If methodology is disclosed in the base form, note it in ADR-011 as confirming evidence and update the H003 drill-down entry framing accordingly

---

### [x] BACKLOG-019: Missing State Amendatory Detector — RESOLVED 2026-06-05

**Status:** Resolved — SMELL5-H007 implemented in Stage 006 `smell5.py`
**Priority:** HIGH — binary finding, near-zero false positives, massive regulatory exposure
**Affects:** Sandbox 002 Stage 006 detectors; Sandbox 004 drill-down report

Multi-state master policy jackets filed in a specific state without the required state amendatory endorsement represent one of the highest-value, most-detectable gap types in the filing package. The finding is binary: either the state amendatory is present in the attachment list or it is not. No linguistic ambiguity. No false-positive risk. Massive regulatory exposure for the carrier.

**What was built:**
- `SMELL5-H007` added to `smell5.py` as a source-level check (not per-node).
- Single scan over carrier nodes: collects multi-state cue hits by source (`state amendatory`, `all states`, `amendatory endorsement`, `[state] amendatory`, etc.) and tracks which sources contain Kentucky amendatory/special-provisions text.
- Emits one consolidated MEDIUM finding per source where multi-state cues are present but no Kentucky amendatory text is found.
- No edge graph required — purely text-presence detection. Acceptance criteria all met.

**Run result (18b0dec5, 2026-06-05):** H007 fired **zero times**. Confirmed correct: current corpus (KFBM HO 04 93 proprietary + KNIC ISO-by-reference) contains no multi-state jacket language. H007 will fire if a multi-state master jacket filing is added to the corpus.

**Relationship to existing work:**
Extends the source-level pattern established by H004-H006 graph-gap detection (ADR-010).

---

### [x] BACKLOG-020: Tighten Broken Definitions Loop Detector — RESOLVED 2026-06-05

**Status:** Resolved — SMELL2-H004 implemented in Stage 006 `smell2.py`
**Priority:** MEDIUM — current findings are valid; this improves precision
**Affects:** Sandbox 002 Stage 006 Smell 2 detectors

**What was built:**
- `SMELL2-H004` added to `smell2.py` as a source-level pre-pass.
- Scans carrier nodes once: identifies Definitions Section nodes (by `section_path` keyword or opening text), extracts quoted defined terms per source; collects quoted terms from body nodes.
- Emits one LOW-confidence finding per (source, term) where a quoted term appears in the policy body but has no matching entry in the same source's Definitions Section.
- Guards: only fires when a Definitions Section is found AND at least one term was extracted (avoids empty-Definitions false positives).
- Amendment-deletion detection deferred (requires richer structural metadata).

**Run result (18b0dec5, 2026-06-05):** H004 fired **zero times**. Confirmed correct: current corpus contains only 4 nodes matching "definitions" in section path or opening text — all are rate manual construction/zone definitions, not insurance policy Definitions Sections. Only 7 carrier nodes contain any double-quote characters (rate table entries). Base policy forms with properly formatted Definitions Sections are not in the current corpus. H004 will fire when those forms are added.

---

### [ ] BACKLOG-021: KFBM Base Policy Jacket Confidence Limitation

**Status:** Open — optional corpus confidence limitation identified 2026-06-05
**Priority:** LOW — do not block higher-value package-level or cross-document work
**Affects:** Sandbox 002 Stage 006 SMELL2-H004; future drill-down entries for KFBM

**What this is:**
KFBM's current new-business base policy form would contain the carrier's Definitions Section. That text could help confirm or refute SMELL2-H004 findings about defined terms used in endorsements or amendments. But this is a lower-value product lane than cross-document, package-completeness, regulatory-mapping, and calculation-drift issues.

**Why KFBM only (not ISO):**
ISO-adopting carriers (e.g., KNIC) outsource their definition domain to ISO HO 00 03. Missing definitions in a KNIC endorsement are almost certainly covered by ISO by reference — KNIC is already a lower-value prospect. Proprietary-base-form carriers (KFBM) OWN their definition domain: every term used in an endorsement or amendment must be defined somewhere in their own filing package or it is a genuine gap. No ISO fallback. This is the core value of H004.

**Current corpus status (updated 2026-06-05):**
`KY-SERFF-KFBM-134503212-HO-FORM` is in the corpus but redacted (25 KB). More critically: ISO HO 04 93 has been confirmed as an **endorsement** form — "Actual Cash Value Loss Settlement: Windstorm or Hail Losses to Roof Surfacing" (ISO copyright 1999, 2 pages). HO 04 XX = ISO endorsements by definition. Therefore `KY-SERFF-KFBM-134503212-HO-FORM` is KFBM's version of this endorsement, NOT their base policy jacket. KFBM's actual base policy jacket has an **unknown form number**. The ISO HO 04 93 standard form has been added to the corpus (ISO-HO-04-93-1000) as H003 evidentiary support.

**Current product-value decision:**
Do not treat unredacted proprietary base-form procurement as a required corpus milestone. A redacted base jacket or filing reference is enough to support a limitation note: definition-domain review cannot be completed from public text. It is not enough to confirm that a term is missing from the Definitions Section.

**Optional resolution path if this becomes high value later:**

Step 1 — Identify KFBM's base policy jacket form number:
- In SERFF Filing Access (KY, TOI 04.0), search KFBM form filings
- Look for a JAC-type (Policy Jacket) form in the Form Schedule
- Prefer current/new-business filing evidence. The base jacket may have originated before SFA's November 2018 cutoff, but pre-2018 material is not the target unless needed to identify or obtain the current jacket.
- If not in SFA, the form number may appear in KFBM's markup filings (the 210 KB / 216 KB versions already in corpus show diffs — the form numbers being revised should be visible there)

Step 2 — Procure unredacted text:
- Kentucky is strict prior-approval; the approved form exists at KY DOI
- Open records request: 502-564-3630
- Reference the form number from Step 1 and carrier "Kentucky Farm Bureau Mutual"

**Acceptance criteria:**
- Reports and detector outputs treat missing/redacted KFBM base-jacket text as a limitation, not a confirmed defect
- No high-value work is blocked on unredacted proprietary base-form procurement
- If the current base jacket is later obtained, add it to `corpus/kentucky-homeowners-policy-smells/sources/` and rerun Stage 002/006 only if a specific detector/report needs it
- `CORPUS-SOURCES.md` and `KNOWN-GAPS.md` updated

---

### [x] BACKLOG-022: Commercial Report Output — Copyright-Safe Sanitization Pass — RESOLVED 2026-06-05

**Status:** Open — design constraint identified 2026-06-05
**Priority:** HIGH — blocks commercial distribution of any report containing carrier or ISO policy text
**Affects:** `sandboxes/004-expert-drilldown/output/drilldown_report.html`; any future commercial report pipeline; `stages/003-executive-report/src/report_builder.py`

**What the problem is:**
All carrier policy forms (KFBM, KNIC) and ISO forms (HO 00 03, HO 04 93, etc.) are copyrighted. Verbatim reproduction of their text in a report sold to another party constitutes copyright infringement — regardless of whether the text appears as evidence, quotation, or illustration. The internal research layer (findings JSONL, drill-down entries JSON, KRS-KAR audit markdown) can and must retain verbatim `evidence_text` for analysis. The commercial output layer cannot.

**Copyright exposure map:**

| Content type | Copyrighted? | Commercial report safe? |
|---|---|---|
| Carrier policy forms (KFBM, KNIC) | Yes — carrier | ❌ No verbatim text |
| ISO forms (HO 00 03, HO 04 93, etc.) | Yes — ISO | ❌ No verbatim text |
| KRS / KAR regulatory text | Public domain | ✅ |
| Court opinions / case law (US) | Public domain | ✅ Full text fine |
| Our own findings/analysis language | We own it | ✅ |

**What the fix is:**
A sanitization render pass in the commercial output pipeline that:
1. Replaces verbatim carrier/ISO evidence snippets with **paraphrased descriptions** that describe the problem without quoting the protected text — e.g., "the policy provides for ACV settlement of roof losses after 7 years without disclosing the depreciation calculation methodology" rather than the verbatim clause.
2. Cites **section path and page location** rather than quoting.
3. Can freely include regulatory text (KRS/KAR) and case holdings (public domain).
4. Preserves the internal `evidence_text` field untouched — the sanitization is output-only.

**Design note:**
The two-layer separation already exists: the raw findings JSONL and drill-down JSON hold verbatim evidence for internal analysis. The commercial render pass needs a `paraphrased_evidence` field (or derives it at render time from the existing `rationale` field, which is already our own language and safe to reproduce). The simplest approach: add a `paraphrased_evidence` field to each drill-down entry alongside `verbatim_evidence`, and use `paraphrased_evidence` in the commercial render path.

**Relationship to BACKLOG-015:**
Case law text (CourtListener, court opinions) is US public domain — full case text retrieval is safe. The copyright constraint applies only to carrier/ISO forms.

**Next action:**
Before building the commercial report pipeline, define the `paraphrased_evidence` field in the drill-down entry schema. For current PoC entries (S4-H001, S4-H004, S4-H003), draft paraphrased versions of the evidence text. Add a `--sanitize` flag to the commercial report renderer analogous to the existing `--anonymize` flag.

---

### [ ] BACKLOG-023: Per-Carrier Report Pipeline — Pitch Report vs. Product Report Split

**Status:** Open — architecture decided 2026-06-05
**Priority:** HIGH — required before any commercial delivery
**Affects:** `stages/003-executive-report/src/report_builder.py`; `stages/006-deterministic-detectors/src/detector_runner.py`; `sandboxes/004-expert-drilldown/output/drilldown_report.html`

**The product model (decided 2026-06-05):**

Three distinct report artifacts, one pipeline:

| Artifact | Audience | Carrier scope | Existing status |
|---|---|---|---|
| **Pitch report** | Prospect — any carrier | Anonymized multi-carrier benchmark | Mostly exists: `--anonymize` run of `report_builder.py` |
| **Product report — KFBM** | KFBM (paying client) | KFBM findings only, named | Not yet wired |
| **Product report — KNIC** | KNIC (paying client) | KNIC findings only, named | Not yet wired |

The pitch report is the sales hook: "We scanned the Kentucky homeowners market and found these patterns across Carrier A and Carrier B." The prospect buys to find out which is them and get the full findings with remediation guidance. The product report is the deliverable they pay for.

The current combined corpus run is the **benchmark artifact** (pitch report). A per-carrier filtered run is the **product artifact**.

**What needs to be built:**

1. **`--carrier` filter flag on `detector_runner.py`** (or passed to report_builder):
   - Accept a carrier identifier (e.g., `KFBM`, `KNIC`) and filter corpus nodes to that carrier's source_ids before running detectors.
   - Source_id prefixes: KFBM sources start with `KY-SERFF-KFBM-`; KNIC sources start with `KY-SERFF-KNIC-`.
   - Output: per-carrier `detector_findings_KFBM.jsonl` and `detector_findings_KNIC.jsonl` alongside the combined run.

2. **Per-carrier executive report**:
   - `report_builder.py --carrier KFBM` generates a report scoped to KFBM findings only, with KFBM named explicitly (not anonymized — this is their report).
   - `report_builder.py --carrier KNIC` same for KNIC.
   - `report_builder.py --anonymize` remains the pitch report (combined, anonymized).
   - The carrier comparison section is suppressed or reframed ("your filing package") in per-carrier mode.

3. **Per-carrier drill-down HTML**:
   - `sandboxes/004-expert-drilldown/output/drilldown_report.html` currently shows all entries. A `--carrier` flag on the report generator filters to that carrier's entries.
   - Alternatively: separate output files `drilldown_KFBM.html` and `drilldown_KNIC.html`.

4. **Copyright sanitization** (see BACKLOG-022):
   - Per-carrier product reports are commercial deliverables — must use `paraphrased_evidence` not `verbatim_evidence`.
   - Pitch report (benchmark) uses only our own analysis language — already clean.

**What is already done:**
- [x] Combined corpus run with findings — `detector_findings.jsonl` — exists
- [x] `--anonymize` flag on `report_builder.py` — pitch report mode exists
- [x] Source_id prefixes are stable and carrier-distinguishable
- [ ] `--carrier` filter on detector runner
- [ ] Per-carrier report builder mode
- [ ] Per-carrier drill-down output
- [ ] Copyright sanitization pass (BACKLOG-022)

**Acceptance criteria:**
- `python detector_runner.py --carrier KFBM` produces a findings file containing only KFBM-source findings
- `python report_builder.py --carrier KFBM` produces a named, per-carrier executive report
- `python report_builder.py --anonymize` (no `--carrier`) continues to produce the combined benchmark/pitch report
- Both per-carrier and combined runs are reproducible from the same corpus without re-parsing

---

### [ ] BACKLOG-005: Phase A Entry — Agile V Framework Integration and SE Expert Configuration

**Status:** Open — actively approaching; blocked on two owner-lane prerequisites  
**Priority:** HIGH — this is the next major project milestone, not a distant concern

**What this is:**
The sandbox research phase is substantively complete. The detection pipeline works, findings are calibrated, a sales report exists, and the product direction (expert drill-down report, BACKLOG-017) is identified. The next milestone is entering Phase A of the Agile V lifecycle: formal stakeholder analysis, concept of operations, requirements, and architecture decisions made with real SE rigor.

**Blocked on (owner lane):**
1. **SE coursework** — owner completing MIT SE courses and related material to establish the SE grounding needed for Phase A work.
2. **SE expert RAG corpus** — configure a RAG knowledge base covering:
   - NASA: NPR 7120.5 (Program/Project Management), SE Handbook (SP-2016-6105), potentially GSFC/JPL standards
   - INCOSE: Systems Engineering Handbook
   - IEEE: 15288 (system lifecycle), 12207 (software lifecycle), 29148 (requirements engineering), and related standards
   - Possibly DAU/DoD materials depending on the Agile V framework interpretation in use
   This corpus turns the AI assistant into an SE-grounded collaborator for Phase A work rather than a general-knowledge approximation.
3. **Gherkin / BDD specification language** — owner to learn Gherkin before Phase A begins. Gherkin is the specification language for all code behavior in this project going forward. Given-When-Then syntax produces human-readable acceptance criteria that map cleanly onto Agile V test levels (unit, integration, system, acceptance). Gherkin specs will be the bridge between SE requirements and implementation — requirements trace to scenarios; scenarios drive tests. Tools: Behave (Python), Cucumber (multi-language). The SE RAG corpus should include BDD/Gherkin reference material alongside the NASA/INCOSE/IEEE standards.

**Sandboxes during this period:**
Sandbox work continues in parallel. Discovery, proof-of-concept experiments, and the drill-down report (BACKLOG-017) all feed the product decisions that Phase A will formalize. Do not pause sandbox work to wait for Phase A to start.

**Product direction is not yet fixed:**
Phase A is where the product gets formally defined through stakeholder analysis and concept of operations. The sandbox outputs are the evidence going into that conversation, not the answer.

**Next action:** When SE coursework and RAG corpus are in place, open a dedicated Phase A session. Until then, keep sandbox lanes active.

---

## Resolved Items

| ID | Item | Resolution | Date |
|---|---|---|---|
| — | KFBM SERFF filings (KY-SERFF-KFBM-POST2018) | 11 files from 5 filings extracted and added to corpus | 2026-06-03 |
