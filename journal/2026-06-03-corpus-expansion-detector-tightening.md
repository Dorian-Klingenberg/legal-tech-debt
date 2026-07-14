# 2026-06-03 Corpus Expansion, KFBM SERFF Procurement, And Detector Tightening

## Summary

This session completed the Sandbox 002 pipeline end-to-end on an expanded 28-source corpus. A second Kentucky homeowners carrier (Kentucky Farm Bureau Mutual) was procured via SERFF Filing Access. The Smell 2 detector was tightened to suppress false positives on regulatory source types. Sandbox 003 was scoped and a plan document placed. Five ADRs were written or updated.

---

## What Happened

### Part 1: Corpus Audit And Expansion

Discovered that 10 of 17 downloaded corpus sources were in `corpus/kentucky-homeowners-policy-smells/sources/` but absent from `source_manifest_subset.csv`. The pipeline had been ignoring them entirely. Added all 10 to the manifest.

Also found that `KY-KRS-304-13.html` was PDF content with a wrong file extension. Renamed to `.pdf`. (Two others — KY-KRS-304-12-230 and KY-KRS-304-14 — have the same issue but parse with warnings; left for a future cleanup pass.)

ADR-005 written: always audit local sources against the manifest before doing any SERFF procurement.

### Part 2: SERFF Filing Access — Kentucky Farm Bureau Mutual

Navigated to `filingaccess.serff.com/sfa/home/KY`. Accepted terms (user clicked Accept). Selected Business Type: Property & Casualty, Type of Insurance: 04.0 Homeowners, Company: Kentucky Farm Bureau Mutual Insurance Company.

38 filings returned. Identified 5 priority filings based on Closed-Approved status and document type:

| Tracking # | Name | Type | Status |
|---|---|---|---|
| KNFB-133738601 | Homeowner | Form | Closed-Approved |
| KNFB-134503212 | Home HO 04 93 2025 Form | Form | Closed-Approved |
| KNFB-134827992 | Home Amendatory Endorsement (FORM) | Form | Closed-Approved |
| KNFB-134870729 | Homeowner Rate Change | Rate | Closed-Approved |
| KNFB-134870230 | Homeowner Underwriting Manual / Risk Factor Rules | Rule | Closed-Acknowledged |

User downloaded all 5 as zip files and placed them in `corpus/`. Extracted 11 relevant PDFs using Python `zipfile` module (shell `unzip` failed because SERFF zips use Windows backslash paths internally).

Files extracted:
- `KY-SERFF-KFBM-134503212-HO-FORM.pdf` — 2025 HO 04-93 policy form (redacted)
- `KY-SERFF-KFBM-134503212-HO-FORM-MARKUP.pdf` — 2025 form showing changes from prior version
- `KY-SERFF-KFBM-133738601-HO-FORM-MARKUP.pdf` — 2012 base HO form with markups
- `KY-SERFF-KFBM-134827992-ENDORSEMENT.pdf` — KY amendatory endorsement HO FB 01 07 26 (2026)
- `KY-SERFF-KFBM-134870230-UW-MANUAL.pdf` — Underwriting manual pages HO-4.1
- `KY-SERFF-KFBM-134870230-UW-MANUAL-CHANGES.pdf` — UW manual change form
- `KY-SERFF-KFBM-134870230-DOI-OBJECTION.pdf` — DOI objection + carrier response
- `KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP1.pdf` — Rate manual part HOP-1
- `KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP2.pdf` — Rate manual part HOP-2
- `KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP2-1.pdf` — Rate manual part HOP-2.1
- `KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP8.pdf` — Rate manual part HOP-8

CORPUS-SOURCES.md updated to 28 sources. KNOWN-GAPS.md KFBM gap marked resolved.

### Part 3: Stage 002 Re-Run

```
run_id: 87283951-fd71-44aa-bf0b-ba18aa23b12d
output: output/002/20260603_210315_87283951/
```

| Metric | Old (7 sources) | New (28 sources) |
|---|---|---|
| Sources | 7 | 28 |
| Nodes | 251 | 353 |
| Blocks | ~800 | 2,103 |
| Citations | ~20 | 100 |
| References | ~30 | 55 |
| Edges | ~400 | 797 |
| Table failures | 0 | 0 |
| Parse warnings | 2 | 6 |
| Candidate evidence | — | 121 |

### Part 4: Detector Run — First Pass (50 Findings, Too Noisy)

Stage 006 on run 87283951 produced 50 findings: Smell 2 had 44. On review, 27 of the 44 were false positives — the H001 heuristic ("reasonable" near valuation context) was firing on `kar_regulation`, `krs_statute`, `doi_bulletin`, and `doi_guidance` sources where "reasonable" is legal standard language, not a claim dispute gate.

Root cause: nodes in `nodes.jsonl` do not carry `source_type` — it lives in `sources.jsonl`. The detector had no way to know what kind of document a node came from.

Fix:
1. `detector_runner.py`: build `source_type_by_id` dict from `idx.source_by_id`; enrich each node dict with `source_type` before passing to detectors
2. `detectors/smell2.py`: define `_CARRIER_SOURCE_TYPES = {"serff_form_filing", "serff_rate_rule_filing", "serff_correspondence"}`; skip H001 and H003 unless `source_type` is in that set

ADR-006 written: smell heuristics must be suppressed on regulatory source types; carrier-only firing is the default design principle for qualitative language heuristics.

### Part 5: Detector Run — Second Pass (23 Findings, Clean)

After fix:

| Smell | Findings | Confidence |
|---|---|---|
| 1 — Overbroad Exclusions | 1 | LOW |
| 2 — Magic Valuation Terms | 17 | MEDIUM |
| 3 — Coverage Inversion | 4 | LOW |
| 4 — Calculation Rule Drift | 1 | HIGH |
| 5 — Regulatory Mapping | 0 | — |

**Notable findings:**

**Smell 4 HIGH — KNIC Section 602:**
> "If the insured location is in another state, refer to the Manual for that state."

No version, edition, or filing number. For a multi-state claim, the applicable rate manual is unidentified and unauditable at time of loss. Reviewer question: which manual, which version, is it filed with the Kentucky DOI?

**Smell 2 MEDIUM — KFBM endorsement HO FB 01 07 26:**
> "general contractor fees will only be included in the estimated reasonable replacement costs if it is reasonably likely that the services of a general contractor will be required"

"Reasonably likely" is undefined. This is the GC overhead-and-profit dispute — one of the most litigated homeowners claims issues in Kentucky. DOI Bulletin 2026-01 and AO 2023-08 are both regulatory responses to exactly this practice. The 2026 KFBM endorsement is actively perpetuating the undefined threshold those bulletins were trying to address. Two carriers using the same undefined gate = industry pattern.

**Smell 2 MEDIUM — KFBM SECTION I CONDITIONS (roof settlement):**
> "If the damage is repaired or replaced within a reasonable time, at the actual cost to repair or replace; If the damage is not repaired or replaced within a reasonable time, at actual cash value"

The settlement method — and therefore the payout amount — switches based on an undefined time threshold. The carrier decides whether the claimant met "reasonable time." ACV can be substantially less than replacement cost on a depreciated roof.

Stage 007 reviewer report regenerated: `output/007/20260603_210315_87283951/reviewer_report.html`.

### Part 6: Sandbox 003 Scoped

Three proposed stages:
1. LLM-assisted finding triage — plain-English explanations, dispute scenarios, false positive assessment
2. Cross-carrier pattern analysis — which smells appear in both KNIC and KFBM vs. one carrier only
3. Executive summary report — one-page output for a CEO or Chief Claims Officer

Plan at `sandboxes/003-findings-triage/003-STAGE-PLAN.md`. Work not started. ADR-007 written.

---

## Decisions Made

| Decision | ADR |
|---|---|
| Always audit local sources before SERFF procurement | ADR-005 |
| Suppress smell heuristics on regulatory source types; carrier-only firing | ADR-006 |
| Sandbox 003 is findings triage and intelligence, not infrastructure | ADR-007 |
| ADR-002 updated: KFBM in corpus (condition 1 partial), Stage 005 re-eval still deferred | ADR-002 |

---

## What We Learned

**Source type matters more than source count for detector precision.** Adding 10 regulatory sources inflated findings 3x with false positives. The fix was one conditional in the detector, not more data.

**SERFF Filing Access is viable for corpus procurement.** Kentucky is public access, no credentials required. One search session yields a carrier's full filing history. Filter by Closed-Approved for policy forms; Closed-Acknowledged filings still contain useful attached documents (rate manuals, underwriting manuals, DOI objection correspondence).

**SERFF zips use Windows backslash paths.** Shell `unzip -j` with forward-slash paths fails silently. Use Python `zipfile.ZipFile` with `namelist()` inspection and path normalization.

**Two carriers using the same undefined term is an industry pattern.** The KFBM 2026 endorsement's "reasonably likely" gate on GC O&P is the same undefined threshold that DOI Bulletin 2026-01 and AO 2023-08 are responding to. That's live regulatory tension visible in the corpus.

**The GC overhead-and-profit dispute is already in this corpus.** The DOI bulletins, the advisory opinion on matching, and the new KFBM endorsement are all touching the same active dispute area. The pipeline found it without being told to look for it.

---

## Loose Threads Carried Forward

- Smell 5 detector produces 0 findings on 28-source corpus — implausible; needs calibration
- Gold set not re-evaluated on run 87283951; BM25 100% not confirmed on expanded corpus
- KY-KRS-304-12-230 and KY-KRS-304-14 still have EXT MISMATCH (PDF content, .html extension)
- Stage 005 re-open conditions: condition 1 partially met (KFBM in corpus); conditions 2 and 3 unmet

---

## Files Changed This Session

**New:**
- `corpus/kentucky-homeowners-policy-smells/sources/KY-SERFF-KFBM-*.pdf` (11 files)
- `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-03d.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-005-corpus-expansion-local-before-serff.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-006-detector-source-type-filtering.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-007-sandbox-003-scope-findings-triage.md`
- `sandboxes/003-findings-triage/003-STAGE-PLAN.md`
- `output/002/20260603_210315_87283951/` (full Stage 002 run artifacts)
- `output/006/20260603_210315_87283951/detector_findings.jsonl` + `detector_report.md`
- `output/007/20260603_210315_87283951/reviewer_report.html` + `reviewer_report.md`

**Modified:**
- `stages/002-.../data/source_manifest_subset.csv` — 7 → 28 sources
- `stages/006-.../src/detector_runner.py` — source_type enrichment
- `stages/006-.../src/detectors/smell2.py` — carrier-only H001/H003
- `corpus/.../CORPUS-SOURCES.md` — 28 sources, KFBM entries, pipeline coverage updated
- `corpus/.../KNOWN-GAPS.md` — KFBM gap resolved
- `corpus/.../sources/KY-KRS-304-13.html` → `KY-KRS-304-13.pdf`
- `sandboxes/002-.../002-RAG-STAGE-PLAN.md` — run 87283951 results, loose threads section
- `sandboxes/002-.../stages/002-.../LESSON.md` — corpus expansion lessons appended
- `sandboxes/002-.../adr/ADR-002` — second status update
- `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` — status line updated
