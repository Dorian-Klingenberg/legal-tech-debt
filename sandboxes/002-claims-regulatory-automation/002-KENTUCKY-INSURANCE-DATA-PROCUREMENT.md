# How To Procure Kentucky Insurance Information

Created: 2026-05-29
Scope: Sandbox 002 Kentucky homeowners insurance research and proof-of-concept fixtures

## Purpose

This guide explains how to collect Kentucky homeowners insurance source material for Sandbox 002 without turning the project into an infrastructure project.

The goal is to gather enough public, reviewable homeowners material to build synthetic-but-realistic fixtures for policy and claims legal tech debt detectors:

- Broken Link / Null Reference Clause
- Calculation Rule Drift
- Coverage Inversion
- Magic Number Term
- Non-deterministic Language
- Regulatory Drift in Claim Handling

This is a research procurement guide, not legal advice.

## Current Scope

Focus on Kentucky homeowners insurance.

Do not procure personal auto, motor vehicle, no-fault, or PIP material for the active fixture. Those sources may appear nearby on Kentucky DOI pages, but they are out of scope unless the user explicitly reopens auto work.

If a homeowners source cross-references another line, record the reference in the manifest as context and keep the fixture homeowners-centered.

## Source Priority

Use official sources first.

1. Kentucky Legislative Research Commission for statutes and regulations.
2. Kentucky Department of Insurance for P&C documents, filing instructions, bulletins, consumer/insurer guidance, and open records.
3. SERFF Filing Access for public rate, rule, and form filings.
4. NAIC or advisory-organization material only when it is publicly available and terms allow research use.

Avoid secondary sources unless they are only being used to discover an official citation.

## Official Source Map

| Need | Source | Notes |
|---|---|---|
| Kentucky Insurance Code | [KRS Chapter 304](https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38708) | Main statutory corpus for insurance. Snapshot exact section URLs and access date. |
| Kentucky insurance regulations | [Title 806 KAR](https://apps.legislature.ky.gov/law/kar/titles/806/) | Administrative regulations. Use exact regulation pages where possible. |
| P&C form filing rules | [806 KAR 14:006](https://apps.legislature.ky.gov/law/kar/titles/806/014/006/) | Key source for form filing procedures and approval/disapproval context. |
| Rate, rule, and form filing access | [Kentucky DOI access page](https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=665) | DOI says P&C filings are accepted through SERFF and SFA can be used for public access. |
| Public filing search instructions | [Public Access Insurance Filings PDF](https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf) | Explains SFA coverage and cautions about filing status. |
| P&C checklists and documents | [DOI P&C Documents](https://insurance.ky.gov/ppc/new_docs.aspx?cat=198) | Use the homeowners-related checklist/materials. If Kentucky combines homeowners with dwelling, mobile homeowners, or farmowners in one checklist, extract only the ordinary homeowners portions for the active fixture. |
| Open records | [DOI Open Records page](https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=6) and [PPC Open Records form](https://ppc.ky.gov/NewOpenRecords.aspx) | Use when filings are older, unavailable in SFA, or need confirmation. |

## What To Collect First

For the first useful 002 fixture, collect only enough to support one narrow policy/claims lane.

Recommended first lane:

> Kentucky homeowners property coverage, with a small rate-rule or form-filing component.

Minimum bundle:

1. Statutes
   - KRS Chapter 304 index.
   - KRS 304.13 sections relevant to rates and supplementary rate information.
   - KRS 304.14 sections relevant to policy forms and approval.
   - Any homeowners/property-specific KRS sections discovered through the DOI homeowners checklist, SERFF filings, or official statute cross-references.

2. Regulations
   - 806 KAR 14:006 for P&C form filings.
   - Any linked 806 KAR rate/rule filing regulation referenced by DOI P&C documents.

3. DOI documents
   - Homeowners checklist/material. If the DOI file combines multiple property lines, keep only homeowners-relevant portions.
   - P&C rate/rule/form filing schedules or transmittal instructions.

4. SERFF public filing samples
   - One approved homeowners form filing.
   - One rate/rule filing or loss-cost-multiplier-related filing if publicly available.
   - Prefer filings with clear status, effective date, filing number, company name, line of business, and attached forms/rules.

5. Open records backup
   - If an older filing is needed, submit an open records request rather than scraping or trying to bypass SFA.

## Manual SERFF Workflow

Use SERFF Filing Access manually.

1. Open the Kentucky SERFF Filing Access page from the DOI access page.
2. Accept the SFA terms only if they fit the research task.
3. Search Kentucky filings by:
   - Line of business: Homeowners. Use adjacent dwelling/mobile/farmowner categories only to locate the combined DOI checklist, not as active fixture scope.
   - Filing type: Form, Rate, Rule, or combined Rate/Rule/Form.
   - Status: approved, closed, or final where available.
   - Date range: start with recent filings.
4. Download a small number of representative filings.
5. Record metadata immediately:
   - SERFF tracking number
   - company name
   - NAIC company number if available
   - filing type
   - line of business
   - submitted date
   - disposition/status
   - effective date
   - downloaded attachment names
   - access date
6. Do not bulk scrape or automate SFA downloads. The public-access PDF notes NAIC terms that prohibit circumvention or bypass of the intended workflow.

Important limitation: the DOI public-access guide says SFA provides access to filings made after November 1, 2018. Older filings are handled through open records.

## Open Records Workflow

Use open records when:

- the filing predates November 1, 2018
- SFA does not expose the attachment needed
- the filing status is unclear
- you need confirmation before relying on a form/rate/rule

Request narrowly. Avoid "any and all" requests.

Suggested request shape:

```text
I am requesting public records for Kentucky Department of Insurance property and casualty rate, rule, and/or form filings matching the following description:

Line of insurance:
Company name:
NAIC number, if known:
SERFF tracking number, if known:
Filing type:
Date range:
Specific forms, endorsements, rate/rule pages, or filing memoranda requested:

This request is for research/prototype development. Please provide electronic copies if available.
```

Track:

- request date
- agency selected
- exact request text
- response date
- records received
- fees, if any
- restrictions or notes

## Local Storage Convention

Use a raw/processed split.

```text
stages/
  002-dual-detector-probe/
    data/
      raw/
        kentucky/
          statutes/
          regulations/
          doi-documents/
          serff-filings/
          open-records/
      processed/
        corpus/
        source_manifest.csv
```

Do not edit raw source files after download. Create cleaned Markdown excerpts under `processed/corpus/`.

## Source Manifest Fields

Every procured item should have one row in `source_manifest.csv`.

```csv
source_id,title,source_type,official_source,url_or_request_id,downloaded_path,accessed_date,effective_date,status,line_of_business,notes
```

Example source types:

- `krs_statute`
- `kar_regulation`
- `doi_guidance`
- `doi_checklist`
- `serff_form_filing`
- `serff_rate_rule_filing`
- `open_records_response`

## Conversion To Sandbox Fixtures

For early experiments, do not try to analyze giant PDFs directly.

1. Select small excerpts.
2. Convert relevant sections to Markdown.
3. Preserve source IDs and citations in headings or front matter.
4. Seed intentional defects in synthetic copies, not in raw files.
5. Keep the original source and synthetic fixture clearly separated.

Suggested heading format:

```markdown
# Source: KY-HO-FORM-EXCERPT-001

## Section 100. Dwelling coverage condition
...
```

## Quality Checks

Before using a source in an experiment, confirm:

- It came from an official source or is clearly marked as secondary.
- The URL and access date are recorded.
- The effective date, filing status, or revision date is recorded when available.
- SERFF material is not assumed final unless the status supports that conclusion.
- Any transformed Markdown preserves enough text to explain a finding.
- The fixture does not imply legal advice or legal interpretation.

## What Not To Do Yet

- Do not build scrapers.
- Do not automate SERFF access.
- Do not ingest hundreds of filings.
- Do not create a database.
- Do not treat DOI consumer guidance as a substitute for statute/regulation text.
- Do not rely on unofficial summaries when official KRS/KAR/DOI sources are available.
- Do not collect auto/no-fault/PIP material for the active fixture.

## First Procurement Checklist

- [ ] Download or save links for KRS Chapter 304 and homeowners/property-specific sections discovered through official sources.
- [ ] Download or save links for Title 806 KAR and 806 KAR 14:006.
- [ ] Download the DOI homeowners/personal dwelling checklist or related P&C document.
- [ ] Manually collect 1-2 recent SERFF filings for Kentucky homeowners.
- [ ] Create `source_manifest.csv`.
- [ ] Convert 5-10 short excerpts into Markdown fixtures.
- [ ] Document any source gaps or open records requests.

## Notes For Future Agents

Keep this procurement work small. The project is still proving detector value, not building a Kentucky insurance data warehouse.

When in doubt, collect one better source with excellent metadata instead of ten poorly tracked sources.
