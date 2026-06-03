# Kentucky Homeowners Corpus — Canonical Source Index

All unique source files live in `sources/`. The smell subdirectories (`01-*/` through `05-*/`) contain duplicates organized by smell relevance — use `sources/` as the authoritative path for any pipeline or script.

## Canonical Paths

| source_id | type | size | smells | notes |
|---|---|---:|---|---|
| KY-SERFF-KNIC-127064322 | serff_rate_rule_filing | 965 KB | 1,2,3,4,5 | Kentucky National Insurance Company homeowners policy program manual rate/rule filing. **Primary carrier form source.** |
| KY-DOI-BULLETIN-2026-01 | doi_bulletin | 124 KB | 1,5 | DOI Bulletin 2026-01 — property insurance claims handling requirements |
| KY-DOI-AO-2023-08 | doi_bulletin | 437 KB | 2,3,5 | DOI Advisory Opinion 2023-08 — aerial imagery and property inspection |
| KY-DOI-AO-2024-01 | doi_bulletin | 177 KB | 5 | DOI Advisory Opinion 2024-01 |
| KY-DOI-HO-CHECKLIST | doi_guidance | 176 KB | 1,2,3,4,5 | DOI homeowners policy form filing checklist |
| KY-DOI-PC-DOCS-PAGE | doi_guidance | 125 KB | 4,5 | DOI P&C documents page |
| KY-DOI-SERFF-ACCESS | doi_guidance | 354 KB | 5 | DOI public access insurance filings instruction sheet |
| KY-KAR-806-12-095 | kar_regulation | 96 KB | 2,3,5 | 806 KAR 12:095 — homeowners insurance |
| KY-KAR-806-13-110 | kar_regulation | 45 KB | 4 | 806 KAR 13:110 — rate filing requirements |
| KY-KAR-806-13-150 | kar_regulation | 87 KB | 4,5 | 806 KAR 13:150 — rate/loss cost filing procedures |
| KY-KAR-806-14-006 | kar_regulation | 55 KB | 1,3,5 | 806 KAR 14:006 — form filing requirements |
| KY-KAR-806-20-010 | kar_regulation | 38 KB | 5 | 806 KAR 20:010 — unfair claims settlement practices |
| KY-KRS-304-12-230 | krs_statute | 4 KB | 2 | KRS 304.12-230 — unfair competition and deceptive practices |
| KY-KRS-304-13 | krs_statute | 9 KB | 4,5 | KRS 304.13 — rates |
| KY-KRS-304-14 | krs_statute | 16 KB | 1,2,3,5 | KRS 304.14 — insurance contracts |
| KY-KRS-304-20 | krs_statute | 27 KB | 1,2,5 | KRS 304.20 — claims practices |
| KY-KRS-304-44 | krs_statute | 21 KB | 3,5 | KRS 304.44 — property insurance |
| KY-SERFF-KFBM-134503212-HO-FORM | serff_form_filing | 25 KB | 1,2,3,5 | KFBM HO 04-93 homeowners form May 2025 (redacted). **Second carrier form source.** |
| KY-SERFF-KFBM-134503212-HO-FORM-MARKUP | serff_form_filing | 210 KB | 1,2,3,5 | KFBM 2025 form with markups showing changes from prior version |
| KY-SERFF-KFBM-133738601-HO-FORM-MARKUP | serff_form_filing | 216 KB | 1,2,3,5 | KFBM original 2012 HO form with markups; baseline for cross-version comparison |
| KY-SERFF-KFBM-134827992-ENDORSEMENT | serff_form_filing | 20 KB | 1,3,5 | KFBM KY amendatory endorsement HO FB 01 07 26 (2026) |
| KY-SERFF-KFBM-134870230-UW-MANUAL | serff_rate_rule_filing | 331 KB | 4,5 | KFBM underwriting manual pages HO-4.1; rating factors and underwriting guidelines |
| KY-SERFF-KFBM-134870230-UW-MANUAL-CHANGES | serff_rate_rule_filing | 354 KB | 4 | KFBM underwriting manual change form; documents rule amendments |
| KY-SERFF-KFBM-134870230-DOI-OBJECTION | serff_correspondence | 252 KB | 5 | DOI objection and KFBM carrier response; regulatory dialogue evidence |
| KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP1 | serff_rate_rule_filing | 137 KB | 4 | KFBM homeowner rate manual HOP-1; base rates and rating rules |
| KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP2 | serff_rate_rule_filing | 177 KB | 4 | KFBM homeowner rate manual HOP-2; rating factors and calculation rules |
| KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP2-1 | serff_rate_rule_filing | 133 KB | 4 | KFBM homeowner rate manual HOP-2.1; supplemental rating rules |
| KY-SERFF-KFBM-134870729-RATE-MANUAL-HOP8 | serff_rate_rule_filing | 119 KB | 4 | KFBM homeowner rate manual HOP-8; endorsement rating factors |

## Pipeline Coverage

All 28 sources are now included in `source_manifest_subset.csv` and will be parsed by Stage 002.

**File note:** `KY-KRS-304-13` was originally saved as `.html` but is PDF content. Renamed to `KY-KRS-304-13.pdf` on 2026-06-03; manifest updated to match.

## Organization Note

The `01-*/` through `05-*/` smell subdirectories are the original research-phase organization and contain duplicates of shared files. They are preserved for reference but should not be used as canonical paths in pipeline code.
