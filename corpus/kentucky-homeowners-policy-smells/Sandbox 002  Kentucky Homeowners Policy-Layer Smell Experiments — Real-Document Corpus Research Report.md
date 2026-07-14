# Sandbox 002: Kentucky Homeowners Policy-Layer Smell Experiments
## Real-Document Corpus Research Report

**Prepared for:** Legal-Tech Research Sandbox  
**Scope:** Kentucky Homeowners Insurance — Real Public-Source Documents Only  
**Access Date:** June 1, 2026  
**Coverage:** KRS Statutes · KAR Regulations · Kentucky DOI Guidance · SERFF Filings

> **Quality Notice:** Every source listed in this report has a real, traceable URL or clear manual-access path. No documents have been invented. Secondary discovery sources are labeled `secondary_discovery_only`. Restrictions are noted inline.

***

## SECTION 1: Must-Have Official Legal Sources (KRS & KAR)

### 1.1 KRS Chapter 304 — The Kentucky Insurance Code

Kentucky Revised Statutes Chapter 304 is the primary statutory framework for all insurance regulation in the Commonwealth. The full chapter is maintained by the Kentucky Legislative Research Commission (LRC) and is freely accessible online.[^1]

***

#### KY-KRS-304-14 — KRS Chapter 304, Subtitle 14: The Insurance Contract

| Field | Value |
|---|---|
| **source_id** | KY-KRS-304-14 |
| **Title** | KRS Chapter 304, Subtitle 14 — The Insurance Contract |
| **source_type** | krs_statute |
| **official_source** | Yes |
| **URL** | https://law.justia.com/codes/kentucky/chapter-304/subtitle-304-14/ (Justia mirror, current 2024 version) |
| **LRC Canonical URL** | https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38671 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current through 2025 Regular Session (KRS 304.14-120 effective January 1, 2025 as amended) |
| **Status** | In force |
| **Line of Business** | All insurance including homeowners/property |

**Key Sections for Corpus:**

- **KRS 304.14-120** — Filing and approval of forms. Governs the prior-approval system for all P&C policy forms. No homeowners form may be delivered in Kentucky unless filed with and approved by the Commissioner. **Smell 5 (Regulatory Mapping)** — the statutory anchor for whether a form is legally in use.[^2]
- **KRS 304.14-130** — Grounds for disapproval: forms containing "inconsistent, ambiguous or misleading clauses, or exceptions and conditions which deceptively affect the risk purported to be assumed in the general coverage." **Smell 1 (Overbroad Exclusions), Smell 3 (Coverage Inversion).** Directly prohibits misleading coverage-grant/exclusion structures.[^3]
- **KRS 304.14-150** — Required policy contents. Every policy shall specify risks insured against, conditions, and benefits payable. **Smell 2 (Magic Valuation Terms)** — absence of required specificity could fail this section.
- **KRS 304.14-370** — No conditions may limit suits to less than one year. **Smell 5 (Regulatory Mapping).**
- **KRS 304.14-420 through 450 / 806 KAR 14:121** — Readability/Flesch score requirements. **Smell 1, 3 (Overbroad/Contradictory language).**[^3]

***

#### KY-KRS-304-13 — KRS Chapter 304, Subtitle 13: Rates and Rating

| Field | Value |
|---|---|
| **source_id** | KY-KRS-304-13 |
| **Title** | KRS Chapter 304, Subtitle 13 — Rates and Rating |
| **source_type** | krs_statute |
| **official_source** | Yes |
| **URL** | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17055 (KRS 304.13-051 direct) |
| **LRC Full Chapter URL** | https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38669 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current; KRS 304.13-051 last amended July 15, 2010 |
| **Line of Business** | P&C including homeowners |

**Key Sections for Corpus:**

- **KRS 304.13-051** — Rate/rule filing requirements. Every insurer shall file rates and supplementary rating information. All rating manuals and underwriting rules must be filed within 15 days of effective date. **Use-and-file for <25% changes; prior approval for >25%.** **Smell 4 (Calculation Rule Drift)** — establishes the legal framework under which unversioned rate manuals become a regulatory violation. The statute says "Manuals, rules, and guidelines must be adhered to until amended," creating the legal hook for identifying drift between filed and applied rules.[^4]
- **KRS 304.13-051(4)** — Manuals and underwriting rules must be filed within 15 days of becoming effective. **Smell 4.**
- **KRS 304.13-057** — Rates based on Kentucky experience. Insurers must demonstrate the extent to which rates are based on Kentucky loss experience. **Smell 4, Smell 5.**[^5]

***

#### KY-KRS-304-20 — KRS Chapter 304, Subtitle 20: Casualty Insurance Contracts

| Field | Value |
|---|---|
| **source_id** | KY-KRS-304-20 |
| **Title** | KRS Chapter 304, Subtitle 20 — Casualty Insurance Contracts (Property & Casualty Provisions) |
| **source_type** | krs_statute |
| **official_source** | Yes |
| **URL** | https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38730 |
| **Key Sections URL** | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=29502 (304.20-310) |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current through 2025 Regular Session |
| **Line of Business** | Property and casualty including homeowners |

**Key Sections for Corpus:**

- **KRS 304.20-300 to 304.20-350** — Declination, cancellation, and nonrenewal framework for P&C policies.[^6]
- **KRS 304.20-310** — Definitions; policy period rules; termination scope.[^7]
- **KRS 304.20-320** — Cancellation and nonrenewal: requires 14-day notice for nonpayment/new policies; **75-day notice** for all other mid-term cancellations and all nonrenewals; must state specific reasons. Premium increase >25% also requires 75-day notice. **Smell 5 (Regulatory Mapping)** — forms referencing generic "as required by law" notice language without these specific numbers are a pattern target.[^8][^3]
- **KRS 304.20-340** — Declination/termination prohibited grounds; subsection (7): insurer may NOT terminate solely because insured had natural-cause losses "that could not have been prevented by the exercise of prudence, diligence, and care." **Smell 5; Smell 1** — underwriting exclusions that effectively replicate prohibited declination grounds.[^9]
- **KRS 304.20-260** — Maximum coverage for structure loss: **100% of replacement cost.** **Smell 2 (Magic Valuation)** — statutory cap on loss settlement obligation.
- **KRS 304.20-035** — 30-day renewal notice requirement; 7 days for sub-30-day policies. **Smell 5.**

***

#### KY-KRS-304-44 — KRS Chapter 304, Subtitle 44: Mine Subsidence Insurance

| Field | Value |
|---|---|
| **source_id** | KY-KRS-304-44 |
| **Title** | KRS Chapter 304, Subtitle 44 — Mine Subsidence Insurance |
| **source_type** | krs_statute |
| **official_source** | Yes |
| **URL** | https://law.justia.com/codes/kentucky/chapter-304/subtitle-304-44/ |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current; KRS 304.44-030 and 304.44-050 effective January 1, 2025 as amended |
| **Line of Business** | Homeowners/property (mandatory in eligible counties) |

**Why This Matters:** Kentucky mandates mine subsidence coverage on homeowners policies in qualifying counties (approximately 37 counties with underground coal-bearing strata). A homeowners form that lacks the required mine subsidence inclusion, or that excludes "earth movement" without a separate mine subsidence provision, is a textbook **Smell 5 (Regulatory Mapping)** and potential **Smell 3 (Coverage Inversion)** target.[^10][^11]

- **KRS 304.44-020** — Mine subsidence fund established. Coverage mandatory unless insured waives in writing.[^11]
- **KRS 304.44-060** — Exempt counties. Creates a split-state applicability map.

***

#### KY-KRS-304-12-230 — KRS 304.12-230: Unfair Claims Settlement Practices Act

| Field | Value |
|---|---|
| **source_id** | KY-KRS-304-12-230 |
| **Title** | KRS 304.12-230 — Unfair Claims Settlement Practices Act |
| **source_type** | krs_statute |
| **official_source** | Yes |
| **URL** | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17009 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current |
| **Line of Business** | All P&C including homeowners |

The statute identifies 17 specific prohibited claims practices, including refusing to pay claims without reasonable investigation, failing to affirm or deny coverage within a "reasonable time," and failing to effectuate "prompt, fair and equitable settlements." **Smell 2 (Magic Number/Valuation Terms)** — the statute itself contains the undefined terms "reasonable," "prompt," and "equitable" that 806 KAR 12:095 then attempts to operationalize. This statutory/regulatory gap is a canonical smell target.[^12][^13]

***

### 1.2 Kentucky Administrative Regulations (Title 806 KAR)

#### KY-KAR-806-14-006 — 806 KAR 14:006: P&C Form Filings

| Field | Value |
|---|---|
| **source_id** | KY-KAR-806-14-006 |
| **Title** | 806 KAR 14:006 — Property and Casualty Insurance Form Filings |
| **source_type** | kar_regulation |
| **official_source** | Yes |
| **URL (LRC canonical)** | https://apps.legislature.ky.gov/law/kar/titles/806/014/006/ |
| **URL (Law.Cornell mirror)** | https://www.law.cornell.edu/regulations/kentucky/806-KAR-14-006 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current through Register Vol. 51, No. 12, June 1, 2025 |
| **Line of Business** | All P&C including homeowners |

**Key Provisions for Corpus:**

- Section 2: All P&C form filings must be submitted via SERFF.[^14]
- Section 3(1): No form used in Kentucky until approved, unless exempted by DOI order per KRS 304.14-120(4). Disapproval grounds include: does not meet KY law requirements; contains unfair, deceptive, ambiguous, misleading, or unfairly discriminatory provisions; or advertising is deceptive. **Smell 1, Smell 3, Smell 5 — the regulatory disapproval standard is the smell test codified.**[^14]
- Relates to: KRS 304.14-120; KRS 304.2-110.[^15][^14]

***

#### KY-KAR-806-13-150 — 806 KAR 13:150: P&C Rate and Rule Filings

| Field | Value |
|---|---|
| **source_id** | KY-KAR-806-13-150 |
| **Title** | 806 KAR 13:150 — Property and Casualty Rate and Rule Filings |
| **source_type** | kar_regulation |
| **official_source** | Yes |
| **URL (LRC canonical)** | https://apps.legislature.ky.gov/law/kar/titles/806/013/150/ |
| **URL (Law.Cornell mirror)** | https://www.law.cornell.edu/regulations/kentucky/title-806/chapter-13 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current |
| **Line of Business** | All P&C including homeowners |

This regulation establishes rate and rule filing procedures and references the SERFF filing platform as the required submission channel. It mandates the LC-1 Loss Cost Multiplier form and rate/rule schedule attachments. **Smell 4 (Calculation Rule Drift)** — this regulation defines what must be versioned and filed; any rate reference in a policy manual that lacks a traceable filing number maps to a potential violation here.[^16][^3]

***

#### KY-KAR-806-13-110 — 806 KAR 13:110: Rate Standards for P&C Flex Rating

| Field | Value |
|---|---|
| **source_id** | KY-KAR-806-13-110 |
| **Title** | 806 KAR 13:110 — Rate Standards for Property and Casualty Insurance "Flex Rating" |
| **source_type** | kar_regulation |
| **official_source** | Yes |
| **URL (LRC canonical)** | https://apps.legislature.ky.gov/law/kar/titles/806/013/110/ |
| **URL (kyrules.elaws.us)** | https://kyrules.elaws.us/rule/806kar13:110 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current |
| **Line of Business** | All P&C including homeowners |

This regulation codifies the rate standards for flex-rated P&C insurance: rates shall not be excessive, inadequate, or unfairly discriminatory; due consideration shall be given to "past and prospective loss experience" and "all other relevant factors." **Smell 4 (Calculation Rule Drift)** — the phrase "all other relevant factors" is itself an undefined valuation term.[^17][^18]

***

#### KY-KAR-806-20-010 — 806 KAR 20:010: Declination, Cancellation, and Nonrenewal

| Field | Value |
|---|---|
| **source_id** | KY-KAR-806-20-010 |
| **Title** | 806 KAR 20:010 — Declination, Cancellation, and Nonrenewal of P&C and Automobile Liability Insurance |
| **source_type** | kar_regulation |
| **official_source** | Yes |
| **URL (LRC canonical)** | https://apps.legislature.ky.gov/law/kar/titles/806/020/010/ |
| **URL (Law.Cornell)** | https://www.law.cornell.edu/regulations/kentucky/806-KAR-20-010 |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current through Register Vol. 51, No. 12, June 1, 2025 |
| **Line of Business** | P&C including homeowners |

Section 1: All cancellation/nonrenewal notices must give **specific grounds**, not general underwriting reasons. **Smell 5 (Regulatory Mapping)** — homeowners policies that cross-reference "as required by law" for notice reasons, without embedding the specific grounds, are direct targets. Cross-reference restriction: Section also applies to auto liability, but the auto provisions (KRS 304.20-040) are **out of scope** for this corpus.[^19][^20]

***

#### KY-KAR-806-12-095 — 806 KAR 12:095: Unfair Claims Settlement Practices for P&C

| Field | Value |
|---|---|
| **source_id** | KY-KAR-806-12-095 |
| **Title** | 806 KAR 12:095 — Unfair Claims Settlement Practices for Property and Casualty Insurance |
| **source_type** | kar_regulation |
| **official_source** | Yes |
| **URL (LRC PDF)** | https://apps.legislature.ky.gov/services/karmaservice/documents/7539/ToPDF?markup=false |
| **URL (LRC canonical)** | https://apps.legislature.ky.gov/law/kar/titles/806/012/095/ |
| **Accessed** | June 1, 2026 |
| **Effective Date** | Current |
| **Line of Business** | All P&C including homeowners |

**Key Provisions:**

- Section 5(1): Insurer must acknowledge receipt of claim notification within **15 days.**[^12]
- Section 6(1)(a): Insurer must affirm or deny liability and offer payment within **30 calendar days** of due proof of loss.[^12]
- Section 6(2)(a): If more time needed, insurer must notify claimant within 30 days of proof of loss, then every **45 days** thereafter.[^12]
- Section 9(1)(b): If loss requires replacement and replaced items don't reasonably match in quality, color, and size, insurer shall replace **all items in the area** for uniform appearance. See also DOI Advisory Opinion 2023-08 for Department interpretation (area = entire roof, entire contiguous floor, etc.).[^21]
- **Smell 2 (Magic Number Terms)**: Section 6 operationalizes the "reasonable time" and "promptly" terms from KRS 304.12-230. Section 9 creates a de facto matching rule without defining depreciation methodology. **Smell 4**: No formula or version reference for how claim amounts are calculated.

***

## SECTION 2: Kentucky DOI / Filing Process Sources

#### KY-DOI-HO-CHECKLIST — Personal Dwelling, Homeowners, Mobile Homeowners & Farmowners Review Requirements Checklist

| Field | Value |
|---|---|
| **source_id** | KY-DOI-HO-CHECKLIST |
| **Title** | Review Requirements Checklist: Personal Dwelling, Homeowners, Mobile Homeowners, and Farmowners Including Primary Residence (3rd Edition) |
| **source_type** | doi_checklist |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/Documents/PersDwellingHomeowners050211.pdf |
| **Accessed** | June 1, 2026 |
| **Edition/Revision Date** | 02/2009 (3rd Edition) — note: this is the currently posted version; check DOI P&C Documents page for updates |
| **Line of Business** | Homeowners, dwelling, mobile homeowners, farmowners with primary residence |

**This is a 7-page comprehensive form and rate filing checklist.** It is the most important single DOI document for this corpus because it explicitly cross-references the statutory and regulatory requirements that reviewers apply to every homeowners form and rate/rule filing.[^3]

**Key Sections for Corpus Smells:**

- **Cancellation & Nonrenewal** (pp. 1-2): Cross-references KRS 304.20-310, 320, 330, 340, and 806 KAR 20:010. Lists all 7 permitted cancellation reasons verbatim. Lists prohibited declination bases. Notice timing: 14 days / 75 days. **Smell 5 (Regulatory Mapping).**[^3]
- **Ambiguous/Inconsistent/Misleading Language Prohibited** (p. 2): Direct citation to KRS 304.14-130(1)(b)(c). Forms shall not "contain any inconsistent, ambiguous or misleading clauses, or exceptions and conditions which deceptively affect the risk." **Smell 1, Smell 3.**[^3]
- **Loss Settlement** (p. 4): References KRS 304.12-235 (30-day payment rule), KRS 304.14-270 (proof of loss forms). **Smell 2.**[^3]
- **Maximum Coverage for Loss to Structure** (p. 4): KRS 304.20-260 — 100% of replacement cost. **Smell 2.**[^3]
- **Rate/Rule Manual Section** (pp. 4-6): Filing standards for advisory organization (AO) adoption, loss cost multiplier LC-1/LC-2, flex-rating, and use-and-file requirements. **Smell 4 (Calculation Rule Drift)** — the checklist specifies that "manuals, rules, and guidelines must be adhered to until amended" and that ratings manuals must be filed within 15 days of effective date.[^3]
- **Mine Subsidence** (pp. 5-6): "Subsidence damage coverage must be included for structures, unless waived in writing by the insured, on policies issued or renewed in counties not exempted." References Bulletin 2006-2 for rates. **Smell 5.**[^3]
- **Earthquake Coverage** (p. 3): References Bulletin 98-2 and Adv Op 99-12; coverage and deductibles must be made available on habitational risks. **Smell 5.**[^3]

***

#### KY-DOI-PC-DOCS-PAGE — Kentucky DOI P&C Documents and Checklists Index Page

| Field | Value |
|---|---|
| **source_id** | KY-DOI-PC-DOCS-PAGE |
| **Title** | Kentucky Department of Insurance — P&C and Documents (Checklists, Rate/Form Filing, Open Records) |
| **source_type** | doi_guidance |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/new_docs.aspx?cat=198 |
| **Accessed** | June 1, 2026 |
| **Line of Business** | All P&C including homeowners |

This page hosts the full array of Kentucky DOI P&C documents including all filing checklists by line, the LC-1/LC-2 loss cost multiplier forms, the NAIC Transmittal Document, Open Records forms, and the Consumer Information System instructions. Key sub-documents:[^22]

- **LC-1 P&C Calculation of Loss Cost Multiplier (10/2007)** — https://insurance.ky.gov/ppc/Documents/[LC1]. **Smell 4 (Calculation Rule Drift)** — the official form used to document the relationship between advisory organization loss costs and filed rates. Any manual that references "current ISO loss costs" without a filed LC-1 is a drift candidate.
- **Consumer Information System for Personal Automobile and Homeowner Premium Information** — Instructions for the DOI-mandated premium comparison shopper guide that accompanies every rate filing. **Smell 4, Smell 5.**
- **Open Records Request Form ORR-1 P&C** — needed for pre-2018 filings. See Section 6.

***

#### KY-DOI-SERFF-ACCESS — Public Access Insurance Filings for Rate, Rule, and Form Filing Search

| Field | Value |
|---|---|
| **source_id** | KY-DOI-SERFF-ACCESS |
| **Title** | Public Access Insurance Filings for Property/Casualty Rate, Rule, and Form Filing Search (DOI Instruction Sheet) |
| **source_type** | doi_guidance |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf |
| **URL (instructions page)** | https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=6 |
| **SFA Access URL** | https://filingaccess.serff.com/sfa/home/KY |
| **Accessed** | June 1, 2026 |
| **Scope** | Filings submitted after November 1, 2018 (SFA searchable); pre-2018 requires open records request |

**Important Access Note:** SFA only covers filings submitted after November 1, 2018. Filings predating November 1, 2018, including KNIC-127064322 (filed 2011), are not on SFA but the KNIC-127064322 pipeline PDF is publicly available via AM Best's completefilings archive (see Section 3).[^23][^24]

***

#### KY-DOI-BULLETIN-2026-01 — Kentucky DOI Bulletin 2026-01: Satellite/Aerial Imagery for Cancellations

| Field | Value |
|---|---|
| **source_id** | KY-DOI-BULLETIN-2026-01 |
| **Title** | Kentucky Department of Insurance Bulletin 2026-01 — Use of Satellite and Aerial Imagery as Basis for Cancellations, Nonrenewals, and Claim Denials |
| **source_type** | doi_bulletin |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/Documents/Bulletin%202026-01.pdf |
| **Issued** | March 11, 2026 |
| **Line of Business** | All P&C including homeowners |

This bulletin addresses a live regulatory mapping issue: satellite imagery **alone** does not constitute a "reasonable investigation" under KRS 304.12-230 and KRS 304.20-320, and cannot justify cancellation, nonrenewal, or claim denial. Aerial imagery (drone/aircraft) may support adverse action only if: (1) sufficiently clear to show specific noncompliant conditions; (2) accompanied by a written summary identifying specific violations; and (3) date-stamped within last 12 months. Roof streaking or discoloration from satellite/aerial images alone is insufficient. Insureds are entitled to review all images relied upon.[^25][^26][^27]

**Smell Map:** **Smell 5 (Regulatory Mapping)** — any homeowners cancellation/nonrenewal form referencing "insurer's underwriting guidelines" without the Bulletin 2026-01 constraints is a non-compliant or under-specified regulatory reference. **Smell 1** — effectively creates a new standard for what constitutes a valid peril-assessment basis for adverse action.

***

#### KY-DOI-AO-2023-08 — Advisory Opinion 2023-08: Matching in Property Loss Settlement

| Field | Value |
|---|---|
| **source_id** | KY-DOI-AO-2023-08 |
| **Title** | Advisory Opinion 2023-08 — Interpretation of 806 KAR 12:095 Section 9(1)(b): Matching Requirement in Property Loss Settlement |
| **source_type** | doi_bulletin |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/Documents/Advisory%20Opinion%202023-08%20RE%20Matching%20Final.pdf |
| **Issued** | October 17, 2023 |
| **Compliance Deadline** | Filings in violation must be amended by September 1, 2024 |
| **Line of Business** | Homeowners/property |

The Department held that "area" under the matching rule means the **entirety** of a part used for a specific purpose (entire roof, entire contiguous interior carpet, entire contiguous tile floor). The "line of sight" rule for partial roof replacement was explicitly rejected. Endorsements placing **sublimits on matching undamaged areas** must be amended or removed.[^21]

**Smell Map:** **Smell 3 (Coverage Inversion)** — endorsements that cap matching coverage (e.g., "we will pay no more than $X to match undamaged areas") directly invert the 806 KAR 12:095 Section 9 obligation. **Smell 2 (Magic Valuation)** — "reasonably match in quality, color, and size" is an undefined standard. **Smell 5** — compliance deadline creates a temporal regulatory mapping issue for policies filed before September 1, 2024, that were not amended.

***

#### KY-DOI-AO-2024-01 — Advisory Opinion 2024-01: Non-Renewal Notice and Natural Causes

| Field | Value |
|---|---|
| **source_id** | KY-DOI-AO-2024-01 |
| **Title** | Advisory Opinion 2024-01 — Interpretation of KRS 304.20-340(7): Non-Renewal Notice and Natural Cause Losses |
| **source_type** | doi_bulletin |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/Documents/AdvisoryOpinionNonRenewalNotice.pdf |
| **Issued** | May 22, 2024 |
| **Line of Business** | P&C including homeowners |

This Advisory Opinion clarifies that under KRS 304.20-340(7), insurers may **not** decline to insure or terminate coverage for losses immediately resulting from natural causes that arose "without intervention of any person and that could not have been prevented by the exercise of prudence, diligence, and care."[^28][^29]

**Smell Map:** **Smell 5 (Regulatory Mapping)** — homeowners nonrenewal provisions citing "prior losses" or "loss history" as grounds for nonrenewal, without excepting KRS 304.20-340(7)-protected natural-cause losses, are directly implicated. Also directly relevant to the KNIC-127064322 manual's language on prior losses for the Vantage program (Note 2 on prior loss thresholds for natural/catastrophe losses vs. other losses).[^30]

***

#### KY-DOI-OPEN-RECORDS-PAGE — Kentucky DOI Open Records Request Process

| Field | Value |
|---|---|
| **source_id** | KY-DOI-OPEN-RECORDS-PAGE |
| **Title** | Kentucky Department of Insurance Open Records Request Process |
| **source_type** | open_records_target |
| **official_source** | Yes |
| **URL** | https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=6 |
| **ORR-1 Form URL** | https://insurance.ky.gov/ppc/Documents/openrecordsrequest092415.pdf (ORR-1 form) |
| **Contact** | DOI.PropertyCasualty@ky.gov; Phone: 502-564-6046 |

Pre-2018 SERFF filings are not on SFA and must be obtained via open records request to the Kentucky DOI. The ORR-1 P&C form is available at the link above. See Section 6 for a draft targeted open records request.[^23]

***

## SECTION 3: SERFF Homeowners Filings to Download

### Important Access Framework

Kentucky DOI began making P&C filings publicly searchable via the SERFF Filing Access (SFA) system for filings submitted after **November 1, 2018.** Pre-2018 filings require an open records request. The main SFA search URL for Kentucky is: **https://filingaccess.serff.com/sfa/home/KY**[^23]

**SFA Search Instructions for Kentucky Homeowners Filings:**
1. Go to https://filingaccess.serff.com/sfa/home/KY
2. Click "Begin Search" and accept the User Agreement
3. Business Type: Property & Casualty
4. Type of Insurance: select "04.0 Homeowners" and/or "04.0000 Homeowners Sub-TOI Combinations"
5. State: Kentucky
6. Filing Type: Rate/Rule, Form, or Rate/Rule/Form
7. Status: Closed-Approved (preferred) or Closed-Acknowledged
8. Date range: 2019–2026 for SFA-accessible filings
9. Company name: enter "Kentucky National," "Kentucky Farm Bureau," "Kentucky Growers," or leave blank to browse

***

### Filing 1: KNIC-127064322 — Kentucky National Insurance Company Homeowners Program Manual

| Field | Value |
|---|---|
| **source_id** | KY-SERFF-KNIC-127064322 |
| **Carrier** | Kentucky National Insurance Company |
| **NAIC CoCode** | 29149 |
| **SERFF Tracking Number** | KNIC-127064322 |
| **Filing Type** | Rate/Rule |
| **SERFF Status** | Closed-Acknowledged |
| **State Status** | Filing Closed |
| **Date Submitted** | March 8, 2011 |
| **Disposition Date** | March 9, 2011 |
| **Effective Date (New)** | May 1, 2011 |
| **Effective Date (Renewal)** | June 1, 2011 |
| **Line of Business** | TOI 04.0 Homeowners / Sub-TOI 04.0000 Homeowners Combinations |
| **Product Name** | KNIC Homeowners |
| **Project Name** | 3/2010 Rate Changes / KNIC HO 3/2010 |
| **Filing Method** | Use & File |
| **Rate Change** | +8.841% (indicated: 12.67%) |
| **Reviewer** | Diane Traylor |

**Publicly Available URL:** https://www3.ambest.com/completefilings/KY_05_2011_601300_584481.pdf

**Note on Access:** This filing predates November 1, 2018 and is NOT on SFA. However, AM Best's completefilings pipeline PDF is publicly accessible at the URL above and contains the **full filing PDF pipeline** including the Revised Manual Pages attachment (KYHO0211).[^30]

**Attachments in the Filing:**
1. `Cover Letter.pdf` — Filing description
2. `Actuarial Memorandum.pdf` — Supporting actuarial basis
3. `LC-1 P&C (8/00) Calculation of Loss Cost Multiplier.pdf` — **KEY: loss-cost multiplier calculation**
4. `LC-2 P&C (8/00) Expense Constant Supplement.pdf`
5. `SG-2 Synopsis For Homeowners-Rate Comparisons.pdf`
6. `Supporting Documentation.pdf`
7. **`KYHO0211 - Revised Manual Pages(2).pdf`** — **THE PRIMARY CORPUS DOCUMENT: Full KNIC Kentucky Homeowners Policy Program Manual (02/11)**

**Manual Contents Confirmed (from pipeline PDF):**

The Revised Manual Pages attachment contains the complete Kentucky National Insurance Company Homeowners Policy Program Manual, including:[^30]

- **Underwriting selection and agent binding rules** (Blue Ribbon, Medalist, Vantage programs)
- **Rule 210: Special State Requirements** — lists mandatory endorsements for all Kentucky policies:
  - Special Provisions Endorsement PCH-2106 ("use with all Homeowners policies")
  - Personal Property Replacement Cost HO 04 90 ("use with all Homeowners policies")
  - No Coverage For Home Day Care Business HO 04 96 ("use with all Homeowners policies")
  - **Lead Liability Exclusion PCH-2135 ("use with all Homeowners policies")**
- **Rule 204: Manual Premium Revision** — "The effective date of such revision shall be **as announced.**" **This is a canonical Smell 4 (Calculation Rule Drift) instance.** The revision effective date is "as announced" without a versioned reference or filing number.
- **Rule 301: Base Premium Computation** — County/territory classification codes, construction type factors (Masonry vs. Frame), protection class factors (Class 1–10), key premium tables by territory/protection class/construction for all programs and forms
- **Rule 901: Insurance to Value Coverage** — policies are automatically adjusted for inflation using "a national appraisal company's statistics" — **Smell 4: "national appraisal company" is unversioned and not identified by name or filing citation**
- **Rule 405: Deductibles** — credit factors without explicit versioning
- **Rule 907: Risk Level** — credit score factor table (range 0.70 to 2.75 based on score bands 801+ to 0–499)
- **Rule 520: Limited Fungi, Wet or Dry Rot, or Bacteria Coverage** — limited coverage endorsement available as optional buyback, **Smell 3 (Coverage Inversion)**: base exclusion + optional endorsement to restore
- **Rule 303: Ordinance or Law Coverage** — available as optional coverage, **Smell 1 (Overbroad Exclusion)**: base form excludes ordinance-or-law costs; endorsement required to include
- Loss settlement language cross-referencing ISO forms HO 00 03, HO 00 08, HO 00 15

**Smell Coverage from KNIC-127064322:**

| Smell | Location in Manual | Pattern |
|---|---|---|
| 1 — Overbroad Exclusions | Rule 520, Lead Exclusion PCH-2135 | Fungi/bacteria sublimit; broad lead exclusion |
| 2 — Magic Valuation | Rule 901 ("national appraisal company"), Rule 204 ("as announced") | Unidentified/unversioned valuation reference |
| 3 — Coverage Inversion | Rule 520 + Rule 302 (Special Loss Settlement) | Exclusion in base + optional endorsement to restore |
| 4 — Calculation Rule Drift | Rule 204 ("as announced"), Rule 301 territory tables, Rule 907 risk level table | Rate manual with stated date 02/11 but annual revision mechanism "as announced" without filing citation |
| 5 — Regulatory Mapping | Rule 210 mandatory endorsements, KRS 304.20-340 cross-ref in underwriting loss rules | Kentucky-specific mandatory endorsements listed; KRS 304.20-340(8) cited in program requirements |

***

### Filing 2: Kentucky National Insurance — SFA Post-2018 Filings (Manual Search Required)

| Field | Value |
|---|---|
| **source_id** | KY-SERFF-KNIC-POST2018 |
| **Carrier** | Kentucky National Insurance Company |
| **NAIC CoCode** | 29149 |
| **SERFF Tracking Number** | Unknown — manual search required via SFA |
| **Filing Type** | Rate/Rule and/or Form |
| **Status** | Closed-Approved (target) |
| **Search URL** | https://filingaccess.serff.com/sfa/home/KY |
| **Line of Business** | TOI 04.0 Homeowners |

**Search Instructions:**
- SFA → State: Kentucky → Business Type: P&C → TOI: 04.0 Homeowners → Company: "Kentucky National" → Status: Closed-Approved → Date: 2019–2026
- Look for filings with attachments named: "Revised Manual Pages," "Program Manual," "Rate Manual," "Rule Manual," "State Amendatory Endorsement," or "Homeowners Manual"
- The most recent homeowners program manual update will supersede KNIC-127064322 and is the corpus priority for current-state analysis

**Why This Matters:** KNIC-127064322 dates from 2011. Kentucky National has certainly filed rate/rule revisions since then. The SFA search will surface any post-2018 filings. The "as announced" language in Rule 204 means each rate revision should have a filed revision — the SFA record will show whether revised manual pages were filed with each change or whether the reference was simply carried forward without update.

***

### Filing 3: Kentucky Growers Insurance Company — SFA Manual Search

| Field | Value |
|---|---|
| **source_id** | KY-SERFF-KGIC-POST2018 |
| **Carrier** | Kentucky Growers Insurance Company, Inc. |
| **NAIC CoCode** | (search SFA or AM Best; Demotech FSR notification confirms company exists)[^31] |
| **SERFF Tracking Number** | Unknown — manual search required via SFA |
| **Filing Type** | Rate/Rule, Form, or Rate/Rule/Form |
| **Status** | Closed-Approved (target) |
| **Search URL** | https://filingaccess.serff.com/sfa/home/KY |
| **Line of Business** | TOI 04.0 Homeowners or TOI 04.1 Dwelling |

Kentucky Growers is a property and casualty insurance company that insures homes and farms in rural and suburban Kentucky. As a specialized rural Kentucky homeowner writer, their filing package is likely to contain: (a) farmowners/homeowners combination forms with Kentucky-specific exclusions; (b) protection class and construction factor tables for rural properties; (c) state amendatory endorsements; and (d) Kentucky-specific loss settlement language.[^32]

**Search Instructions:**
- SFA → State: Kentucky → Business Type: P&C → TOI: 04.0 Homeowners → Company: "Kentucky Growers" → Status: Closed-Approved
- Also search TOI: 04.1 Dwelling (farmowners/dwellings may be filed under dwelling or homeowners)
- Look for: base forms, rate manual pages, rule manual, state specific endorsements, loss settlement endorsements

***

### Filing 4: Kentucky Farm Bureau Mutual Insurance Company — SFA Manual Search

| Field | Value |
|---|---|
| **source_id** | KY-SERFF-KFBM-POST2018 |
| **Carrier** | Kentucky Farm Bureau Mutual Insurance Company |
| **NAIC CoCode** | (search SFA; KFB is the dominant homeowners carrier in Kentucky) |
| **SERFF Tracking Number** | Unknown — manual search required via SFA |
| **Filing Type** | Rate/Rule, Form, and/or Rate/Rule/Form |
| **Status** | Closed-Approved (target) |
| **Search URL** | https://filingaccess.serff.com/sfa/home/KY |
| **Line of Business** | TOI 04.0 Homeowners |

Kentucky Farm Bureau Mutual is the dominant homeowners insurer in rural and suburban Kentucky. Their filing package is the highest-value SFA target for this corpus because: (a) they are Kentucky-domiciled and Kentucky-only, meaning their forms will be Kentucky-specific rather than multi-state generic; (b) their scale means the forms have been through repeated DOI review cycles; (c) as a mutual insurer, their loss settlement and valuation language is likely to reflect the full range of Smell 2 and Smell 4 patterns.[^33]

**Search Instructions:**
- SFA → State: Kentucky → Business Type: P&C → TOI: 04.0 Homeowners → Company: "Kentucky Farm Bureau" → Status: Closed-Approved
- Also check: "KFB" or "Farm Bureau Mutual" variants
- Priority attachments: base policy form, state amendatory endorsements, rate manual, loss settlement language, mold/water/fungi exclusion endorsements, ACV vs. replacement cost election endorsements

***

## SECTION 4: Candidate Source-to-Smell Map

### Smell 1 — Overbroad / Non-Deterministic Exclusions

| Best Source Document | Clause / Section | Phrase Patterns to Find | Why Relevant |
|---|---|---|---|
| **KNIC-127064322 Manual, Rule 520** | "Limited Fungi, Wet or Dry Rot, or Bacteria Coverage" | "fungi," "bacteria," "wet or dry rot" | Fungi/bacteria is the canonical non-deterministic exclusion in homeowners; limited endorsement makes base exclusion broad |
| **KNIC-127064322 Manual, Rule 303** | "Ordinance or Law Coverage" | "ordinance or law," "governmental action" | Base exclusion for law-compliance costs; endorsement required to include |
| **KNIC-127064322 Manual, Lead Exclusion PCH-2135** | Mandatory endorsement for all KY policies | "lead," "pollutant," "arising out of" | Broad mandatory exclusion; "arising out of" is the primary non-determinism signal |
| **806 KAR 14:006, Section 3(1)(b)** | DOI disapproval standard | "unfair, deceptive, ambiguous, misleading" | Regulatory standard for what constitutes an overbroad exclusion |
| **KRS 304.14-130(1)(b)** | Form disapproval grounds | "inconsistent, ambiguous or misleading clauses… exceptions and conditions which deceptively affect the risk" | Statutory prohibition that overbroad exclusions violate |
| **KY-SERFF-KFBM or KGIC (SFA search)** | Water damage exclusion, anti-concurrent causation | "resulting from," "directly or indirectly," "in any sequence," "concurrent causation" | Anti-concurrent causation clauses are the highest-value overbroad exclusion pattern |

***

### Smell 2 — Magic Number / Magic Valuation Terms

| Best Source Document | Clause / Section | Phrase Patterns to Find | Why Relevant |
|---|---|---|---|
| **KNIC-127064322 Manual, Rule 901** | Insurance to Value Coverage | "a national appraisal company's statistics" (un-named company) | Classic magic valuation term: undefined third-party reference without version |
| **806 KAR 12:095, Section 6** | Claims settlement timeline | "reasonable time," "affirm or deny… within a reasonable period" | Undefined time standard — operationalizes KRS 304.12-230 |
| **806 KAR 12:095, Section 9(1)(b)** | Matching standard | "reasonably match in quality, color, and size" | "Reasonably match" is undefined without depreciation schedule or formula |
| **KRS 304.20-260** | Maximum coverage | "100% of replacement cost" | Statutory upper bound — forms that use "ACV" or "fair market value" instead are below statutory floor |
| **KY-DOI-AO-2023-08** | Advisory Opinion interpretation | "area" = entire roof/floor | Regulatory interpretation revealing that "area" was itself a magic/undefined term until this opinion |
| **KRS 304.12-230 (Items 3, 4, 5, 6)** | UCSPA standard | "reasonable standards," "reasonable investigation," "reasonable time," "prompt, fair and equitable" | All undefined; these are the "magic standard terms" in the claims-handling context |

***

### Smell 3 — Coverage Inversion / Contradictory Conditions

| Best Source Document | Clause / Section | Phrase Patterns to Find | Why Relevant |
|---|---|---|---|
| **KNIC-127064322 Manual, Rules 302+520** | Special Loss Settlement + Fungi Limited | Base exclusion + optional restore endorsement | Prototypical inversion: base form excludes mold, optional endorsement restores sublimited coverage |
| **KNIC-127064322 Manual, Rule 210 mandatory endorsements** | HO 04 96 (No Home Day Care) | "notwithstanding any other provision," "excludes… home day care" | Mandatory exclusion endorsement contradicts broad "all-risks" grant |
| **KY-DOI-AO-2023-08** | Matching sublimit endorsements | Endorsement "places sublimit on matching undamaged areas" | DOI found this creates a contradiction with the base 806 KAR 12:095 Section 9 obligation |
| **KRS 304.14-130 / KY-DOI-HO-CHECKLIST p.2** | Ambiguous clauses prohibition | "inconsistent… clauses… exceptions and conditions which deceptively affect the risk" | Legal standard for Coverage Inversion; checklist is the operational form of this standard |
| **SFA search: KFBM or KGIC, state amendatory endorsement** | Kentucky-specific coverage grant vs. base form exclusion | "except as provided in," "notwithstanding" | State amendatory endorsements that narrow the base form coverage grant |

***

### Smell 4 — Calculation Rule Drift / Unversioned Rate Reference

| Best Source Document | Clause / Section | Phrase Patterns to Find | Why Relevant |
|---|---|---|---|
| **KNIC-127064322 Manual, Rule 204** | Manual Premium Revision | "The effective date of such revision shall be as announced" | Canonical drift pattern: rate revision with no traceable filing reference |
| **KNIC-127064322 Manual, Rule 301** | Territory/protection class/construction tables | Key premium tables dated 02/11 (February 2011) with no update mechanism visible | Static manual tables used as "current" without version control |
| **KNIC-127064322 Manual, Rule 901** | Insurance-to-Value | "a national appraisal company's statistics" | Unidentified third-party; no version or filing citation |
| **KNIC-127064322 Manual, Rule 907** | Risk Level (credit-based) | Score bands with multipliers 0.70–2.75, "No Score: 1.00" | Rating table with no actuarial manual citation or version date |
| **KRS 304.13-051(4) + KY-DOI-HO-CHECKLIST p.5** | Rate filing requirement | "filed within 15 days of the effective date" | Legal standard: manuals must be filed to be used; any "as announced" or undated table is a potential statutory violation |
| **806 KAR 13:150 + LC-1 P&C form** | Loss cost multiplier | LC-1 form documents the multiplier calculation | Any rate filing that references AO loss costs without an accompanying filed LC-1 is a drift instance |
| **SFA search: most recent KNIC or KFBM rate filing** | Most recent rate manual pages | Roof age factors, protection class factors, construction type factors | Search for tables without edition dates or with "current rating plan" language |

***

### Smell 5 — Regulatory Mapping Smells

| Best Source Document | Clause / Section | Phrase Patterns to Find | Why Relevant |
|---|---|---|---|
| **KRS 304.20-320 + 806 KAR 20:010** | Cancellation/nonrenewal notice | "as required by state law," "75 days," "14 days," "specific reason" | Forms that say "notice as required by law" without the specific day-counts fail the regulatory mapping test |
| **KY-DOI-BULLETIN-2026-01** | Satellite/aerial imagery cancellation | "cancellation or nonrenewal based on property condition" | Any form permitting adverse action on "property condition" without the Bulletin 2026-01 constraints is non-compliant |
| **KY-DOI-AO-2024-01** | Natural-cause loss nonrenewal | KRS 304.20-340(7); "natural cause," "without intervention" | Prior-loss underwriting language that doesn't carve out natural-cause losses violates this statute/AO |
| **KRS 304.44-020 + KY-DOI-HO-CHECKLIST p.5** | Mine subsidence mandatory | "mine subsidence," county-specific | Kentucky-only mandatory coverage that multi-state forms often omit without a KY-specific endorsement |
| **KNIC-127064322 Manual, Rule 210** | Special State Requirements | PCH-2106, PCH-2135 listed as mandatory "use with all Homeowners policies" | Shows how Kentucky-specific mandatory endorsement requirements are embedded in the manual — look for this pattern in other carriers' manuals |
| **KRS 304.14-420–450 / 806 KAR 14:121** | Readability requirement | Flesch score certification required | Multi-state forms without Kentucky Flesch-score certification are non-compliant |
| **SFA search: any state amendatory endorsement** | Kentucky state-specific page | "where permitted by law," "in accordance with applicable law" | Generic multi-state forms with catch-all conformity clauses rather than Kentucky-specific schedules |

***

## SECTION 5: Download Package Recommendations

### Minimum Viable Stage 002 Corpus

The following represents the smallest real-document corpus that will support at least one verified real-source example for each of the five smells:

#### Tier 1: Must-Have (Direct Download, All Publicly Available)

| Priority | source_id | Document | Format | URL | Smells Covered |
|---|---|---|---|---|---|
| 1 | KY-SERFF-KNIC-127064322 | KNIC Kentucky Homeowners Policy Program Manual (KYHO0211 attachment, full pipeline PDF) | PDF | https://www3.ambest.com/completefilings/KY_05_2011_601300_584481.pdf | 1, 2, 3, 4, 5 |
| 2 | KY-DOI-HO-CHECKLIST | DOI Personal Dwelling/Homeowners Review Requirements Checklist (3rd ed., 02/2009) | PDF | https://insurance.ky.gov/ppc/Documents/PersDwellingHomeowners050211.pdf | 1, 2, 3, 4, 5 |
| 3 | KY-DOI-AO-2023-08 | Advisory Opinion 2023-08: Matching Requirement | PDF | https://insurance.ky.gov/ppc/Documents/Advisory%20Opinion%202023-08%20RE%20Matching%20Final.pdf | 2, 3, 5 |
| 4 | KY-DOI-BULLETIN-2026-01 | Bulletin 2026-01: Satellite/Aerial Imagery | PDF | https://insurance.ky.gov/ppc/Documents/Bulletin%202026-01.pdf | 1, 5 |
| 5 | KY-KRS-304-14 | KRS 304.14-120 (Form approval) and 304.14-130 (Disapproval grounds) | HTML/text | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=55765 | 1, 2, 3, 5 |
| 6 | KY-KRS-304-20-320 | KRS 304.20-320 (Cancellation/nonrenewal notice requirements) | HTML/text | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=29503 | 5 |
| 7 | KY-KRS-304-13-051 | KRS 304.13-051 (Rate filing, manual filing requirements) | HTML/text | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17055 | 4, 5 |
| 8 | KY-KAR-806-12-095 | 806 KAR 12:095 (Unfair claims settlement practices; claims timeline; matching rule) | PDF | https://apps.legislature.ky.gov/services/karmaservice/documents/7539/ToPDF?markup=false | 2, 3, 5 |

#### Tier 2: High Value (Direct Download)

| Priority | source_id | Document | URL | Smells Covered |
|---|---|---|---|---|
| 9 | KY-KAR-806-14-006 | 806 KAR 14:006 (Form filing procedures, disapproval standards) | https://apps.legislature.ky.gov/law/kar/titles/806/014/006/ | 1, 3, 5 |
| 10 | KY-KAR-806-20-010 | 806 KAR 20:010 (Declination, cancellation, nonrenewal; specific-grounds requirement) | https://apps.legislature.ky.gov/law/kar/titles/806/020/010/ | 5 |
| 11 | KY-KRS-304-20-340 | KRS 304.20-340 (Prohibited declination grounds incl. natural-cause losses) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=29505 | 5, 1 |
| 12 | KY-DOI-AO-2024-01 | Advisory Opinion 2024-01: Non-Renewal Notice (natural causes) | https://insurance.ky.gov/ppc/Documents/AdvisoryOpinionNonRenewalNotice.pdf | 5 |

#### Tier 3: SERFF SFA Manual Download Required (Post-2018)

| Priority | source_id | Carrier | Search Steps | Smells Targeted |
|---|---|---|---|---|
| 13 | KY-SERFF-KNIC-POST2018 | Kentucky National Insurance | SFA → KY → P&C → TOI 04.0 → "Kentucky National" → Closed-Approved | 2, 4 |
| 14 | KY-SERFF-KFBM-POST2018 | Kentucky Farm Bureau Mutual | SFA → KY → P&C → TOI 04.0 → "Kentucky Farm Bureau" → Closed-Approved | 1, 2, 3, 4, 5 |
| 15 | KY-SERFF-KGIC-POST2018 | Kentucky Growers Insurance | SFA → KY → P&C → TOI 04.0 → "Kentucky Growers" → Closed-Approved | 1, 2, 3, 4, 5 |

#### Specific Attachments to Convert to Markdown (10 Priority Items)

1. **KNIC-127064322: Rule 204 (Manual Premium Revision)** — extract verbatim "as announced" language → Smell 4 canonical example
2. **KNIC-127064322: Rule 901 (Insurance to Value)** — extract "national appraisal company" language → Smell 4, Smell 2
3. **KNIC-127064322: Rule 210 (Special State Requirements)** — extract mandatory endorsement list → Smell 5
4. **KNIC-127064322: Rule 520 (Limited Fungi/Bacteria Coverage)** — extract sublimit and restore-by-endorsement structure → Smell 3, Smell 1
5. **KNIC-127064322: Rule 301 (Base Premium Computation, Territory Table)** — extract territory/protection class/construction tables → Smell 4
6. **DOI Homeowners Checklist pp. 1–2** — cancellation notice and ambiguous-clauses sections → Smell 5, Smell 1
7. **DOI AO 2023-08** — full text (2 pages) → Smell 3, Smell 2
8. **KRS 304.14-130** — full text of form disapproval grounds → Smell 1, Smell 3 statutory anchor
9. **KRS 304.20-320** — cancellation/nonrenewal notice requirements → Smell 5 statutory anchor
10. **806 KAR 12:095 Sections 5, 6, 9** — claim acknowledgment, payment timelines, matching rule → Smell 2, Smell 3

***

## SECTION 6: Open Records Fallback

The following is a draft narrow open records request for pre-2018 SERFF filings not accessible via SFA.

***

### Draft Kentucky DOI Open Records Request — Homeowners Rate/Rule/Form Filings

**To:** Kentucky Department of Insurance  
Property & Casualty Division, Open Records Custodian  
500 Mero Street, 2SE11, Frankfort, KY 40601  
**Email:** DOI.PropertyCasualty@ky.gov  
**Phone:** 502-564-6046  
**Form:** Use ORR-1 P&C (available at https://insurance.ky.gov/ppc/Documents/openrecordsrequest092415.pdf)

***

**Pursuant to KRS 61.870 to 61.884, I respectfully request the following public records:**

**Request 1 — Kentucky National Insurance Company Homeowners Filings (2011–2018)**

All approved rate, rule, and form filings submitted by Kentucky National Insurance Company (NAIC CoCode 29149) for Line of Business TOI 04.0 Homeowners or 04.0000 Homeowners Sub-TOI Combinations, with a filing date between January 1, 2011, and October 31, 2018. I specifically request:

(a) SERFF Tracking Number KNIC-127064322 (Rate/Rule, filed March 8, 2011) if not available through the AM Best pipeline noted above; and  
(b) Any subsequent homeowners rate/rule/form filings made by Kentucky National Insurance Company for Kentucky between January 1, 2011 and October 31, 2018, including revised manual pages, state amendatory endorsements, or program manual updates.

**Request 2 — Kentucky Farm Bureau Mutual Insurance Company Homeowners Filings (Pre-2018)**

All approved rate, rule, and form filings submitted by Kentucky Farm Bureau Mutual Insurance Company for Line of Business TOI 04.0 Homeowners in Kentucky with a filing date between January 1, 2010, and October 31, 2018, specifically including:

(a) Base homeowners policy forms and endorsements;  
(b) Rate manuals and program manuals;  
(c) State amendatory endorsements specific to Kentucky;  
(d) Loss settlement or valuation endorsements (ACV vs. replacement cost elections, depreciation schedules, matching provisions).

**Request 3 — Kentucky Growers Insurance Company Homeowners Filings (Pre-2018)**

All approved rate, rule, and form filings submitted by Kentucky Growers Insurance Company, Inc. for Line of Business TOI 04.0 Homeowners or TOI 04.1 Dwelling in Kentucky with a filing date between January 1, 2010, and October 31, 2018, specifically including base policy forms, rate manuals, and state endorsements.

**Format Requested:** Electronic copies preferred (PDF). If paper only, please advise on cost and turnaround.

**Purpose:** This request is for academic and legal-technology research purposes related to analysis of publicly filed insurance policy language. It is not for commercial solicitation purposes.

***

### Alternative: Targeted DOI Contact for Bulletin Index

Contact the Kentucky DOI Property & Casualty Division directly for a complete index of all P&C bulletins and advisory opinions issued between 2010 and 2026 that reference homeowners, dwelling, or farmowners coverage:

- **Phone:** 502-564-6046  
- **Email:** DOI.PropertyCasualty@ky.gov  
- **DOI Bulletins Page:** https://insurance.ky.gov/ppc/new_bulletin.aspx?bullid=1

In particular, request:
- Bulletin 98-2 (Earthquake coverage availability requirement for habitational risks) — referenced in checklist but not directly linked
- Bulletin 2006-2 (Mine subsidence rates) — referenced in checklist
- Advisory Opinion 2024-01 (May 22, 2024) — already has a URL but confirm it is the current version

***

## SECTION 7: CSV-Style Manifest Table

```
source_id,title,source_type,official_source,url_or_request_id,accessed_date,effective_date,status,line_of_business,company_name,serff_tracking_number,attachments,smells_supported,notes
KY-KRS-304-14,KRS Chapter 304 Subtitle 14 — The Insurance Contract,krs_statute,yes,https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=55765,2026-06-01,current through 2025 Regular Session,in force,All insurance including homeowners,N/A,N/A,"KRS 304.14-120 (form approval); KRS 304.14-130 (disapproval grounds); KRS 304.14-150 (required policy contents); KRS 304.14-370 (jurisdiction)",1|2|3|5,"See also KRS 304.14-420-450 for readability requirements"
KY-KRS-304-13,KRS Chapter 304 Subtitle 13 — Rates and Rating,krs_statute,yes,https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17055,2026-06-01,current through 2025 Regular Session,in force,All P&C including homeowners,N/A,N/A,"KRS 304.13-051 (rate/rule/manual filing); KRS 304.13-057 (KY experience basis)",4|5,"Use-and-file for <25% change; prior approval for >25%"
KY-KRS-304-20,KRS Chapter 304 Subtitle 20 — Casualty Insurance Contracts,krs_statute,yes,https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38730,2026-06-01,current through 2025 Regular Session,in force,P&C including homeowners,N/A,N/A,"KRS 304.20-310 (definitions); KRS 304.20-320 (cancellation/nonrenewal 75-day notice); KRS 304.20-340 (prohibited declination grounds); KRS 304.20-260 (100% replacement cost max)",5|1|2,"Auto sections (304.20-040) out of scope"
KY-KRS-304-44,KRS Chapter 304 Subtitle 44 — Mine Subsidence Insurance,krs_statute,yes,https://law.justia.com/codes/kentucky/chapter-304/subtitle-304-44/,2026-06-01,current (304.44-030 eff. Jan 1 2025),in force,Homeowners/property in eligible KY counties,N/A,N/A,"KRS 304.44-020 (mandatory coverage); KRS 304.44-060 (exempt counties)",5|3,"Mandatory in ~37 KY counties with underground coal mines; waiver must be in writing"
KY-KRS-304-12-230,KRS 304.12-230 — Unfair Claims Settlement Practices Act,krs_statute,yes,https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17009,2026-06-01,current,in force,All P&C including homeowners,N/A,N/A,17 enumerated prohibited practices including items (3)(4)(5)(6) — undefined 'reasonable' and 'prompt' standards,2|5,"Statutory source of magic standard terms operationalized by 806 KAR 12:095"
KY-KAR-806-14-006,806 KAR 14:006 — P&C Insurance Form Filings,kar_regulation,yes,https://apps.legislature.ky.gov/law/kar/titles/806/014/006/,2026-06-01,current through Register Vol. 51 No. 12 (June 2025),in force,All P&C including homeowners,N/A,N/A,"Section 2 (SERFF required); Section 3 (disapproval grounds: unfair/deceptive/ambiguous/misleading)",1|3|5,"Prior approval required; disapproval for ambiguous or misleading provisions"
KY-KAR-806-13-150,806 KAR 13:150 — P&C Rate and Rule Filings,kar_regulation,yes,https://apps.legislature.ky.gov/law/kar/titles/806/013/150/,2026-06-01,current,in force,All P&C including homeowners,N/A,N/A,"SERFF required; LC-1 LCM form; rate/rule schedule",4|5,N/A
KY-KAR-806-13-110,806 KAR 13:110 — Rate Standards for P&C Flex Rating,kar_regulation,yes,https://kyrules.elaws.us/rule/806kar13:110,2026-06-01,current (last updated August 2016 in this mirror),in force,All P&C including homeowners,N/A,N/A,"Rate standards: not excessive/inadequate/discriminatory; 'all other relevant factors'",4,"'All other relevant factors' is itself an undefined standard"
KY-KAR-806-20-010,806 KAR 20:010 — Declination Cancellation and Nonrenewal of P&C Insurance,kar_regulation,yes,https://apps.legislature.ky.gov/law/kar/titles/806/020/010/,2026-06-01,current through Register Vol. 51 No. 12 (June 2025),in force,P&C including homeowners,N/A,N/A,"Section 1: specific grounds required; not general underwriting reasons",5,"Auto liability (KRS 304.20-040) cross-referenced but out of scope; extract only P&C sections"
KY-KAR-806-12-095,806 KAR 12:095 — Unfair Claims Settlement Practices for P&C,kar_regulation,yes,https://apps.legislature.ky.gov/services/karmaservice/documents/7539/ToPDF?markup=false,2026-06-01,current,in force,All P&C including homeowners,N/A,N/A,"Section 5 (15-day ack); Section 6(1)(a) (30-day pay/deny); Section 6(2) (45-day update); Section 9(1)(b) (matching rule)",2|3|5,"Section 9 matching rule is subject of AO 2023-08"
KY-DOI-HO-CHECKLIST,Review Requirements Checklist: Personal Dwelling Homeowners Mobile Homeowners and Farmowners (3rd Edition 02/2009),doi_checklist,yes,https://insurance.ky.gov/ppc/Documents/PersDwellingHomeowners050211.pdf,2026-06-01,02/2009 (3rd edition — check DOI for updates),posted/in use,Homeowners/dwelling/mobile homeowners/farmowners with primary residence,N/A,N/A,7-page checklist covering forms/rates/cancellation/loss settlement/mine subsidence/earthquake,1|2|3|4|5,"Best single cross-reference document for all 5 smells; check DOI P&C docs page for any updated version"
KY-DOI-PC-DOCS-PAGE,Kentucky DOI P&C and Documents Index Page,doi_guidance,yes,https://insurance.ky.gov/ppc/new_docs.aspx?cat=198,2026-06-01,current,live,All P&C,N/A,N/A,"LC-1 LCM form; ORR-1 open records form; SFA public access instructions; NAIC transmittal documents",4|5,"Hub page linking all P&C filing forms and checklists"
KY-DOI-SERFF-ACCESS,Public Access Insurance Filings for P&C Rate Rule and Form Filing Search (DOI Instruction Sheet),doi_guidance,yes,https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf,2026-06-01,current,live,All P&C,N/A,N/A,SFA search instructions; cutoff date November 1 2018,5,"SFA URL: https://filingaccess.serff.com/sfa/home/KY"
KY-DOI-BULLETIN-2026-01,DOI Bulletin 2026-01 — Use of Satellite and Aerial Imagery for Cancellations and Claim Denials,doi_bulletin,yes,https://insurance.ky.gov/ppc/Documents/Bulletin%202026-01.pdf,2026-06-01,2026-03-11,active,All P&C including homeowners,N/A,N/A,Full bulletin text,1|5,"References Bulletin 2024-02 on AI in insurance for cross-reference"
KY-DOI-AO-2023-08,Advisory Opinion 2023-08 — Matching in Property Loss Settlement (806 KAR 12:095 Section 9),doi_bulletin,yes,https://insurance.ky.gov/ppc/Documents/Advisory%20Opinion%202023-08%20RE%20Matching%20Final.pdf,2026-06-01,2023-10-17,active (compliance deadline was September 1 2024),Homeowners/property,N/A,N/A,Full advisory opinion text,2|3|5,"Any sublimit endorsement on matching undamaged areas must have been amended by September 1 2024"
KY-DOI-AO-2024-01,Advisory Opinion 2024-01 — Non-Renewal Notice and Natural Cause Losses (KRS 304.20-340),doi_bulletin,yes,https://insurance.ky.gov/ppc/Documents/AdvisoryOpinionNonRenewalNotice.pdf,2026-06-01,2024-05-22,active,P&C including homeowners,N/A,N/A,Full advisory opinion text,5,"Clarifies KRS 304.20-340(7) prohibition on termination for natural-cause losses"
KY-DOI-OPEN-RECORDS-PAGE,Kentucky DOI Open Records Request Process,open_records_target,yes,https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=6,2026-06-01,current,live,All P&C,N/A,N/A,"ORR-1 form; SFA cutoff explanation; DOI Property Casualty contact info",N/A,"Required for pre-November 2018 SERFF filings not on SFA"
KY-SERFF-KNIC-127064322,Kentucky National Insurance Company Homeowners Policy Program Manual Rate/Rule Filing (KNIC-127064322) — Full Pipeline PDF via AM Best,serff_rate_rule_filing,yes,https://www3.ambest.com/completefilings/KY_05_2011_601300_584481.pdf,2026-06-01,2011-05-01 (new) / 2011-06-01 (renewal),Closed-Acknowledged,TOI 04.0 Homeowners,Kentucky National Insurance Company,KNIC-127064322,"Cover Letter; Actuarial Memorandum; LC-1 LCM; LC-2; SG-2 Synopsis; Supporting Documentation; KYHO0211 Revised Manual Pages (PRIMARY CORPUS DOCUMENT)",1|2|3|4|5,"Pre-2018 filing; publicly available via AM Best pipeline PDF (not on SFA); Rule 204 'as announced' is canonical Smell 4 example; Rule 901 'national appraisal company' is Smell 2/4"
KY-SERFF-KNIC-POST2018,Kentucky National Insurance Company Post-2018 Homeowners Filings (manual SFA search required),serff_rate_rule_filing,yes,https://filingaccess.serff.com/sfa/home/KY,2026-06-01,varies,target: Closed-Approved,TOI 04.0 Homeowners,Kentucky National Insurance Company,TBD via SFA search,"Rate manual pages; state amendatory endorsements; program manual updates",2|4,"Search: SFA → KY → P&C → TOI 04.0 → 'Kentucky National' → Closed-Approved; supersedes KNIC-127064322 for current-state analysis"
KY-SERFF-KFBM-POST2018,Kentucky Farm Bureau Mutual Insurance Company Homeowners Filings (manual SFA search required),serff_form_filing,yes,https://filingaccess.serff.com/sfa/home/KY,2026-06-01,varies,target: Closed-Approved,TOI 04.0 Homeowners,Kentucky Farm Bureau Mutual Insurance Company,TBD via SFA search,"Base policy form; state amendatory endorsements; rate manual; loss settlement endorsements; water/mold exclusion endorsements",1|2|3|4|5,"Highest-priority SFA search; KY-only carrier with KY-specific forms; search for anti-concurrent causation and matching sublimit endorsements"
KY-SERFF-KGIC-POST2018,Kentucky Growers Insurance Company Homeowners Filings (manual SFA search required),serff_form_filing,yes,https://filingaccess.serff.com/sfa/home/KY,2026-06-01,varies,target: Closed-Approved,TOI 04.0 Homeowners / 04.1 Dwelling,Kentucky Growers Insurance Company Inc.,TBD via SFA search,"Base policy form; rate manual; state endorsements; farmowners/homeowners combination forms",1|2|3|4|5,"Rural/suburban Kentucky specialist; farmowners/homeowners combination forms likely; search TOI 04.0 and 04.1"
```

***

## Appendix: Quick-Reference URL Table

| source_id | Short URL / Access Path |
|---|---|
| KY-KRS-304-14 | apps.legislature.ky.gov → Law → KRS → Chapter 304 → Subtitle 14 |
| KY-KRS-304-13 | apps.legislature.ky.gov/law/statutes/statute.aspx?id=17055 (KRS 304.13-051) |
| KY-KRS-304-20 | apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38730 |
| KY-KRS-304-44 | law.justia.com/codes/kentucky/chapter-304/subtitle-304-44/ |
| KY-KRS-304-12-230 | apps.legislature.ky.gov/law/statutes/statute.aspx?id=17009 |
| KY-KAR-806-14-006 | apps.legislature.ky.gov/law/kar/titles/806/014/006/ |
| KY-KAR-806-13-150 | apps.legislature.ky.gov/law/kar/titles/806/013/150/ |
| KY-KAR-806-13-110 | kyrules.elaws.us/rule/806kar13:110 |
| KY-KAR-806-20-010 | apps.legislature.ky.gov/law/kar/titles/806/020/010/ |
| KY-KAR-806-12-095 | apps.legislature.ky.gov/services/karmaservice/documents/7539/ToPDF?markup=false |
| KY-DOI-HO-CHECKLIST | insurance.ky.gov/ppc/Documents/PersDwellingHomeowners050211.pdf |
| KY-DOI-PC-DOCS-PAGE | insurance.ky.gov/ppc/new_docs.aspx?cat=198 |
| KY-DOI-SERFF-ACCESS | insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf |
| KY-DOI-BULLETIN-2026-01 | insurance.ky.gov/ppc/Documents/Bulletin%202026-01.pdf |
| KY-DOI-AO-2023-08 | insurance.ky.gov/ppc/Documents/Advisory%20Opinion%202023-08%20RE%20Matching%20Final.pdf |
| KY-DOI-AO-2024-01 | insurance.ky.gov/ppc/Documents/AdvisoryOpinionNonRenewalNotice.pdf |
| KY-DOI-OPEN-RECORDS-PAGE | insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=6 |
| KY-SERFF-KNIC-127064322 | www3.ambest.com/completefilings/KY_05_2011_601300_584481.pdf |
| KY-SERFF-KNIC-POST2018 | filingaccess.serff.com/sfa/home/KY (manual search) |
| KY-SERFF-KFBM-POST2018 | filingaccess.serff.com/sfa/home/KY (manual search) |
| KY-SERFF-KGIC-POST2018 | filingaccess.serff.com/sfa/home/KY (manual search) |

---

## References

1. [2024 Kentucky Revised Statutes :: Chapter 304 - Insurance code ...](https://law.justia.com/codes/kentucky/chapter-304/subtitle-304-14/) - Justia Free Databases of U.S. Laws, Codes & Statutes

2. [304.14-120   Filing and approval of forms.](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=55765)

3. [[PDF] REVIEW REQUIREMENTS - DEPARTMENT OF INSURANCE](https://insurance.ky.gov/ppc/Documents/PersDwellingHomeowners050211.pdf) - Kentucky Department of Insurance. 02/2009. Review Requirements Checklist. Personal Dwelling, Homeown...

4. [[PDF] 304.13-051 Filing rates and rate information](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17055) - (6) Rates and supplemental rating information for a residual market mechanism shall not become effec...

5. [[PDF] 304.13-057 Rates based on Kentucky experience.](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17058) - (1) Every insurer shall provide to the commissioner information to demonstrate to what extent the in...

6. [Kentucky Revised Statutes - Legislative Research Commission](https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38730) - 20-035 Notice of renewal premiums of property or casualty policy. .20-037 ... 20-300 Purpose and app...

7. [[PDF] 304.20-310 Definitions for KRS 304.20-320 to 304.20-350.](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=29502) - (3) "Termination" means either a cancellation or nonrenewal of property or casualty ... -- Amended. ...

8. [[PDF] 304.20-320 Declinations -- Cancellations -- Nonrenewals](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=29503) - (a) No insurer shall refuse to renew a property or casualty insurance policy subject to KRS 304.20-3...

9. [[PDF] 304.20-340 Declination or termination prohibited, when.](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=29505) - (7) Based solely upon the fact that the applicant or named insured has sustained one (1) or more los...

10. [Mine Subsidence Coverage: Do you have it?](https://govaughn.com/mine-subsidence-coverage-do-you-have-it/) - The reinsurance limits for damages to structures due to mine subsidence increased from $100,000 to $...

11. [mine subsidence coverage - IRMI](https://www.irmi.com/term/insurance-definitions/mine-subsidence-coverage) - As of this writing, mine subsidence coverage is mandated for both commercial and residential propert...

12. [Kentucky Unfair Claims Settlement Practices Act](https://www.propertyinsurancecoveragelaw.com/blog/kentucky-unfair-claims-settlement-practices-act/) - Kentucky's UCSPA outlines various conduct which constitutes unfair claims settlement practice, inclu...

13. [Insurance bad faith , kentucky unfair claims settlement practices](https://aguiarinjurylawyers.com/kentucky-bad-faith-cases/) - Under 806 KAR 12:095, the DOI has established administrative regulations governing unfair property a...

14. [Title 806 Chapter 14 Regulation 006 • Kentucky Administrative ...](https://apps.legislature.ky.gov/law/kar/titles/806/014/006/) - This administrative regulation provides form filing procedures for property, casualty, surety, title...

15. [806 KAR 14:006. Property and casualty insurance form filings ...](https://kyrules.elaws.us/rule/806kar14:006) - Section 6. (1) A policy or form shall not be used in Kentucky until it has been approved. (2) If the...

16. [Title 806 Chapter 13 Regulation 150 • Kentucky Administrative ...](https://apps.legislature.ky.gov/law/kar/titles/806/013/150/) - This administrative regulation establishes rate and rule filing procedures for property, casualty, s...

17. [[PDF] KRS 304.13-051 STATUTORY AUTHORI](https://apps.legislature.ky.gov/law/kar/downloads/docs/7571/document.engrossed.pdf) - This administrative regulation prescribes the rate standards which must be met by property and casua...

18. [806 KAR 13:110. Rate standards for property and casualty ...](https://kyrules.elaws.us/rule/806kar13:110) - This administrative regulation prescribes the rate standards which must be met by property and casua...

19. [Kentucky Administrative Regulations, Chapter 20, Section 806 KAR ...](https://regulations.justia.com/states/kentucky/title-806/chapter-20/010/) - This administrative regulation establishes guidelines for the declination, cancellation, and nonrene...

20. [[PDF] 806 KAR 20:010. Declination, cancellation, and nonrenewal of ...](https://apps.legislature.ky.gov/services/karmaservice/documents/7695/ToPDF?markup=false) - This administrative regulation establishes guidelines for the declination, cancellation, and nonrene...

21. [[PDF] advisory opinion 2023-08 - DEPARTMENT OF INSURANCE](https://insurance.ky.gov/ppc/Documents/Advisory%20Opinion%202023-08%20RE%20Matching%20Final.pdf) - The following Advisory Opinion is to advise the reader of the current position of the Kentucky. Depa...

22. [DEPARTMENT OF INSURANCE](https://insurance.ky.gov/ppc/new_docs.aspx?cat=198) - DEPARTMENT OF INSURANCE · Charitable Health Care · Checklists- Rate and Form Filing for P&C Companie...

23. [DEPARTMENT OF INSURANCE](https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=6) - To file an open records request, go here. More information on filing a request is available here. Pu...

24. [[PDF] Public Access Insurance Filings for Rate, Rule, and Form Filing Search](https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf) - If you need assistance finding a filing or have public access questions, please contact the Kentucky...

25. [Kentucky Issues Bulletin Regarding the Use of Satellite and Aerial ...](https://aaisviews.aaisonline.com/compliance-alerts/kentucky-issues-bulletin-regarding-the-use-of-satellite-and-aerial-imagery) - An insured is entitled to review all satellite and aerial images relied upon to support a cancellati...

26. [Kentucky Bars Use of Satellite Imagery Alone for Policy ...](https://www.resourcepro.com/bulletin/kentucky-bars-use-of-satellite-imagery-alone-for-policy-cancellations-and-claim-denials/) - KY| Kentucky Department of Insurance Bulletin 2026-01 advises that property and casualty insurers ma...

27. [Kentucky - Bulletin Regarding Satellite and Aerial Imagery for ...](https://www.propertycasualty360.com/fcs/2026/03/16/kentucky---bulletin-regarding-satellite-and-aerial-imagery-for-nonrenewal-cancellation-and-denials/) - Insurers may not rely on satellite imagery as the sole basis for cancellation, nonrenewal, or claim ...

28. [Kentucky Issues Interpretation of KRS 304.20-040(4)(c) & KRS ...](https://www.ilsainc.com/bulletin/kentucky-issues-interpretation-of-krs-304-20-0404c-krs-304-20-3407-regarding-non-renewal-notice/) - KY | The Kentucky Department of Insurance has issued Advisory Opinion 2024-01 to clarify its interpr...

29. [[PDF] commonwealth of kentucky - DEPARTMENT OF INSURANCE](https://insurance.ky.gov/ppc/Documents/AdvisoryOpinionNonRenewalNotice.pdf) - REGARDING NON-RENEWAL NOTICE. DATE: May 22, 2024. The Department of Insurance is issuing this Adviso...

30. [[PDF] Filing KNIC-127064322 - AM Best](https://www3.ambest.com/completefilings/KY_05_2011_601300_584481.pdf) - Use this endorsement with all Homeowners policies. Page 16. KENTUCKY NATIONAL INSURANCE COMPANY. HOM...

31. [About Kentucky Growers Insurance Company, Inc. - Demotech](https://www.demotech.com/fsr_notifications/fsr_notification_14658/) - Kentucky Growers is a property and casualty insurance company that insures homes and farms located i...

32. [Kentucky Growers Insurance](https://kentuckygrowers.com) - Helping Kentucky Families Grow. Kentucky Growers is a property and casualty insurance provider for h...

33. [Kentucky Farm Bureau Customer Ratings - Clearsurance](https://clearsurance.com/insurance-company/kentucky-farm-bureau-5835ece073b103329e91abdc) - The average Kentucky Farm Bureau homeowners insurance rates for both the $200K home and $400K home a...

