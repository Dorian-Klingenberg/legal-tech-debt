# Corpus Known Gaps

Status: Active corpus record
Scope: Sandbox 002 Kentucky homeowners five-smell corpus
Last updated: 2026-07-13

This file records what the corpus does not yet contain, so future agents do not confuse missing manually accessed material with an accidental download failure.

The current corpus was sufficient to complete the Sandbox 002 proof of concept. These gaps are not blockers by default. Treat them as targeted follow-up only when an explicitly reopened detector, validation question, or report claim needs evidence not represented by the preserved run.

Project-level procurement strategy lives in `../PROCUREMENT-STRATEGY.md`. If Kentucky-specific acquisition risk becomes the main blocker, shift the next acquisition experiment to the owner's home state rather than stalling product discovery. Kentucky gaps matter only when the active Kentucky experiment needs that exact source. The target is current new-business policy repairability, not historical filing reconstruction; pre-November 1, 2018 filings should be chased only if they are needed to identify or obtain a current package document.

## Operating Rule

- Do not treat these gaps as urgent collection work unless an active experiment runs into them.
- Prefer currently approved/currently issued policy packages over foundational approval history.
- Do not treat pre-November 1, 2018 material as required unless it is the only practical route to a current new-policy source.
- Do not automate or scrape SERFF Filing Access.
- If one of these sources becomes necessary, collect it manually through SERFF Filing Access, place the unique file in canonical `sources/`, and update the appropriate inventory/manifest records. Do not add a new pipeline dependency on smell-duplicate directories.
- Keep a note of the filing search path, carrier, TOI, status, tracking number, filing date, and attachment names.
- If the source cannot be previewed or downloaded, record that limitation here instead of silently dropping it.

## Known Gaps

| Gap ID | Source | Why It Is Missing | Smells Affected | When To Chase It |
|---|---|---|---|---|
| ~~KY-SERFF-KFBM-POST2018~~ | ~~Kentucky Farm Bureau Mutual Insurance Company homeowners filings~~ | **RESOLVED 2026-06-03** — 11 files extracted from 5 SERFF filings (KNFB-133738601, 134503212, 134827992, 134870230, 134870729); added to corpus sources and manifest | — | — |
| KY-SERFF-KGIC-POST2018 | Kentucky Growers Insurance Company homeowners or dwelling filings in SERFF Filing Access | Searched SFA 2026-06-03 (KY, TOI 04.0/04.1, Company = "Growers"/"Kentucky Growers") — no entry found. Recheck attempted 2026-06-04 but SFA was down. Carrier may not file homeowners in SERFF or files under a different name. See BACKLOG-003. | 1, 2, 3, 4, 5 | Rerun SFA search when site is back up. If still no results, close as not available in SFA. Low urgency — current KNIC/KFBM corpus is sufficient for Sandbox 003. |
| KY-SERFF-KNIC-POST2018 | Kentucky National Insurance Company post-2018 homeowners filings in SERFF Filing Access | Manual SFA search required; no direct static download URL in the manifest | 2, 4 | Chase if the older KNIC-127064322 filing is not current enough for a rate/rule drift or valuation-term example. |
| KY-DOI-OPEN-RECORDS-PAGE | Kentucky DOI open-records process | Not a smell-mapped source; it is a retrieval path for older filings | N/A | Use only if we need pre-November 2018 filings that are not available through SFA or another public pipeline. |

| ISO-HO-BASE-FORMS | ISO HO 00 03 (Special Form), HO 00 05 (Comprehensive Form) base homeowners policy forms | **Searched 2026-06-04.** KNIC adoption filings reference ISO by SERFF tracking number only; no base-form text is attached. Public copies may remain copyrighted or edition-specific. A future ISO-comparison experiment must identify and verify the exact licensed or public edition it uses rather than relying on assumed content. | 2 (H003) | LOW — not needed for the completed proof of concept. Activate only for an explicit ISO-divergence or definition-domain experiment. |
| KY-KFBM-BASE-FORM-UNREDACTED | KFBM base policy jacket — unredacted full text with Definitions Section | **Updated 2026-06-05:** ISO HO 04 93 is an endorsement (Actual Cash Value Loss Settlement — Windstorm/Hail Roof Surfacing), not a policy jacket. `KY-SERFF-KFBM-134503212-HO-FORM` is KFBM's version of that endorsement. KFBM's actual base-jacket form number remains unknown. A redacted schedule can establish that a form exists but cannot prove a missing definition. BACKLOG-021 is closed; this row preserves the limitation. | 2 (H004) | LOW — optional future source. No current work is blocked. |

## Current Interpretation

The downloaded corpus was enough to complete the preserved Stage 002-007 proof. Known gaps limit claims about complete carrier packages and current market prevalence. They become active only when a named future experiment needs the exact missing source.


