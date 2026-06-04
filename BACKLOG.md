# Project Backlog

Status: Active
Scope: Cross-sandbox items with no current sandbox home
Last updated: 2026-06-04 (session 2)

This file tracks open questions, deferred tasks, and homeless backlog items — things that are real enough to record but not yet assigned to a sandbox or stage. Items are checked off when resolved, not deleted, so the search history stays visible.

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

### [ ] BACKLOG-002: Corpus File Extension Mismatches

**Status:** Open — low priority  
**Affects:** Corpus parsing warnings; no stage is currently blocked

Two corpus files are named `.html` but contain PDF content:
- `KY-KRS-304-12-230`
- `KY-KRS-304-14`

A third file with the same issue (`KY-KRS-304-13`) was already renamed. The pipeline parses these with warnings and does produce nodes, so nothing is blocked.

**Next action:** Rename both files to `.pdf`, update `_download_manifest.csv`, rerun Stage 002 to confirm warnings clear.

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

### [ ] BACKLOG-010: Smell Detectors Must Not Fire On Statutory/Regulatory Corpus Nodes

**Status:** Open — Sandbox 002 fix required  
**Affects:** All smell detectors in Stage 006; Sandbox 003 Stage 001 output  
**Priority:** High — directly produces false positives that would appear in a client report

**What we know:**
All four Smell 3 findings in the current run are on KRS/KAR statutory and regulatory nodes. The smell detectors have no guard against firing on reference-layer sources. The statutory/regulatory corpus (KY-KRS-*, KY-KAR-*, KY-DOI-*) exists to check carrier filings *against*, not to be analyzed for smells itself. Suggesting a carrier "clarify the exceptions" in a Kentucky statute is not actionable and would undermine a client report.

The immediate cause is that `source_type` is blank for all statutory/regulatory nodes — it was never populated during ingestion — so detectors cannot guard on it.

**Short-term fix (Sandbox 002 Stage 006):** Add a source ID prefix guard to all detectors: skip any node whose `source_id` starts with `KY-KRS-`, `KY-KAR-`, or `KY-DOI-`. Fast and reliable without a schema change.

**Long-term fix (Stage 002 ingestion):** Populate `source_type` correctly for all sources during ingestion. The corpus manifest (`CORPUS-SOURCES.md`) already classifies each source — that classification should flow through to every node as a first-class field. Detectors then guard on `source_type not in {ky_statute, ky_regulation, doi_bulletin, doi_guidance}`.

**Next action:** Apply the short-term source ID prefix guard to Stage 006 detectors. Re-run Stage 006 and Stage 007. Add the long-term schema fix to the Stage 002 ingestion backlog.

---

### [ ] BACKLOG-007: KRS/KAR Definitional Cross-Reference Check

**Status:** Open — no sandbox assigned  
**Affects:** Sandbox 002 Stage 006 detectors (Smell 2 specifically); Stage 003 severity ratings  
**Priority:** Medium — affects severity of multiple findings before they reach a client report

**What we know:**
During Sandbox 003 Stage 001 human review, "reasonable time" was flagged in six Smell 2 findings (all in roof surfacing / windstorm-or-hail loss settlement conditions across KNIC and KFBM). The LLM rated these HIGH severity, but "reasonable time" may be defined in Kentucky statute or regulation — KRS or KAR. If a statutory definition exists, carriers can rely on it without restating it in the filing, and the finding drops significantly in severity.

The same issue applies to other common insurance terms flagged by Smell 2 heuristics: if KRS/KAR provides a definition, the absence of an in-filing definition is not a smell.

**What the fix is:** Build a reference lookup during Stage 006 detection (or as a post-detection enrichment step) that checks whether a flagged term appears in the Kentucky statutory/regulatory corpus already in the graph. If a definitional edge exists in the corpus from a statutory node, the finding confidence and severity should be downweighted accordingly.

**Next action:** Audit the existing corpus for KRS/KAR definitional sections. Check whether "reasonable time," "actual cash value," and "replacement cost" are defined anywhere in the statutory nodes. If so, wire that as a graph-lookup enrichment on Smell 2 findings. Assign to a new Sandbox 002 or 003 stage when ready.

---

### [ ] BACKLOG-008: Smell 2 / Smell 4 Miscategorization — External Valuation References

**Status:** Open — no sandbox assigned  
**Affects:** Sandbox 002 Stage 006 Smell 2 findings; Stage 003 report framing  
**Priority:** Low — findings are real, but the category affects the remediation advice

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

### [ ] BACKLOG-011: Filter Section Headers and Document Structure Nodes Before Smell Detection

**Status:** Open — Sandbox 002 Stage 006 fix  
**Affects:** All smell detectors; produces noise findings with no actionable content  
**Priority:** Medium — straightforward fix, directly reduces false positive count

**What we know:**
Several findings have evidence text that is purely structural — a section header ("Roof Surface Loss Settlement"), a table-of-contents entry, or a document title. These nodes contain no substantive policy language. Running smell detectors on them produces findings with no meaningful evidence text and no actionable remediation.

**Fix:** Before running any detector, filter out nodes where the substantive text content (excluding the section title/path) falls below a minimum meaningful length — approximately 50–75 characters of non-title text. This eliminates header-only nodes without suppressing legitimate short provisions.

**Next action:** Add a minimum text length pre-filter to the Stage 006 detector runner. Re-run and measure false positive reduction.

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

### [ ] BACKLOG-013: Stage 003 Report — Carrier Name Anonymization

**Status:** Open — design decision required before prospect use  
**Affects:** `stages/003-executive-report/src/report_builder.py`; Stage 003 output  
**Priority:** Medium — required before this report goes in front of a prospect who doesn't know the carriers

**What we know:**
The carrier-specific patterns section names KNIC and KFBM explicitly. For internal analysis this is correct. For a prospect pitch to a carrier that doesn't know those names, it is a distraction and may raise questions about data sourcing. The report should have a mode that replaces carrier names with generic labels ("Carrier A", "Carrier B") or "one of the carriers analyzed."

**Decision needed:** Should anonymization be a build-time flag (always anonymize for external output) or a post-processing step? Also: should the methodology note disclose whether carrier names are available on request?

**Next action:** Add an `--anonymize` flag to `report_builder.py` that substitutes KNIC → "Carrier A" and KFBM → "Carrier B" throughout the output. The internal version retains real names; the prospect version uses labels.

---

### [ ] BACKLOG-014: Stage 003 Report — LLM Prose Quality Improvement

**Status:** Open — iterative prompt work  
**Affects:** `stages/003-executive-report/src/report_builder.py` narrative prompts  
**Priority:** Low — current prose is serviceable but generic; a human editorial pass would significantly improve it

**What we know:**
The current executive intro and closing use generic phrases ("crucial insights," "evolving landscape," "strategic priority") that read like competent but unedited LLM output. The pattern narratives are more grounded but still slightly formal.

**Two approaches:**
1. Tighter prompts — add explicit constraints against filler phrases, require concrete specifics, provide sentence-level examples of the desired register
2. Human editorial pass — treat LLM output as a first draft, edit in place before distribution

Both are needed. Option 2 is essential for any client-facing version regardless of prompt quality.

**Next action:** Before any prospect use, have a human editor review and tighten the narrative sections. In parallel, iterate on prompts to reduce generic language — add an explicit list of prohibited phrases and a short example of the target register to the system prompt.

---

### [ ] BACKLOG-005: Project Graduation And Agile V Framework Integration

**Status:** Open — not yet time; placeholder for future discussion  
**Priority:** Low — revisit after Sandbox 003 produces a client-ready output

At some point the sandbox research phase ends and this becomes a real project with a real delivery framework. Two questions to answer when that time comes:

1. **Project graduation** — what criteria signal that the sandbox phase is over and a proper project structure (scope, milestones, resourcing, client commitments) is warranted?
2. **Agile V integration** — how and when does the Agile V framework get layered onto this project's workflow?

**Next action:** Revisit after Sandbox 003 Stage 003 (executive summary report) is complete and there is a client-facing artifact to evaluate. That output will be the clearest signal of whether the concept is ready to graduate.

---

## Resolved Items

| ID | Item | Resolution | Date |
|---|---|---|---|
| — | KFBM SERFF filings (KY-SERFF-KFBM-POST2018) | 11 files from 5 filings extracted and added to corpus | 2026-06-03 |
