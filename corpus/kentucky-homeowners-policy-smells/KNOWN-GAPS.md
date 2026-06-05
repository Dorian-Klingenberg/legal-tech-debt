# Corpus Known Gaps

Status: Active corpus record
Scope: Sandbox 002 Kentucky homeowners five-smell corpus
Last updated: 2026-06-04

This file records what the corpus does not yet contain, so future agents do not confuse missing manually accessed material with an accidental download failure.

The current corpus is intentionally enough to begin proof-of-concept work. These gaps are not blockers by default. Treat them as targeted follow-up only when a detector, fixture, reviewer question, or ROI case needs current carrier-specific evidence that is not already represented by the downloaded sources.

Project-level procurement strategy lives in `../PROCUREMENT-STRATEGY.md`. If Kentucky-specific acquisition risk becomes the main blocker, shift the next acquisition experiment to the owner's home state rather than stalling product discovery. Kentucky gaps matter only when the active Kentucky experiment needs that exact source. The target is current new-business policy repairability, not historical filing reconstruction; pre-November 1, 2018 filings should be chased only if they are needed to identify or obtain a current package document.

## Operating Rule

- Do not treat these gaps as urgent collection work unless an active experiment runs into them.
- Prefer currently approved/currently issued policy packages over foundational approval history.
- Do not treat pre-November 1, 2018 material as required unless it is the only practical route to a current new-policy source.
- Do not automate or scrape SERFF Filing Access.
- If one of these sources becomes necessary, collect it manually through SERFF Filing Access, then place the downloaded filing or attachment in the relevant smell directories and update `_download_manifest.csv`.
- Keep a note of the filing search path, carrier, TOI, status, tracking number, filing date, and attachment names.
- If the source cannot be previewed or downloaded, record that limitation here instead of silently dropping it.

## Known Gaps

| Gap ID | Source | Why It Is Missing | Smells Affected | When To Chase It |
|---|---|---|---|---|
| ~~KY-SERFF-KFBM-POST2018~~ | ~~Kentucky Farm Bureau Mutual Insurance Company homeowners filings~~ | **RESOLVED 2026-06-03** — 11 files extracted from 5 SERFF filings (KNFB-133738601, 134503212, 134827992, 134870230, 134870729); added to corpus sources and manifest | — | — |
| KY-SERFF-KGIC-POST2018 | Kentucky Growers Insurance Company homeowners or dwelling filings in SERFF Filing Access | Searched SFA 2026-06-03 (KY, TOI 04.0/04.1, Company = "Growers"/"Kentucky Growers") — no entry found. Recheck attempted 2026-06-04 but SFA was down. Carrier may not file homeowners in SERFF or files under a different name. See BACKLOG-003. | 1, 2, 3, 4, 5 | Rerun SFA search when site is back up. If still no results, close as not available in SFA. Low urgency — current KNIC/KFBM corpus is sufficient for Sandbox 003. |
| KY-SERFF-KNIC-POST2018 | Kentucky National Insurance Company post-2018 homeowners filings in SERFF Filing Access | Manual SFA search required; no direct static download URL in the manifest | 2, 4 | Chase if the older KNIC-127064322 filing is not current enough for a rate/rule drift or valuation-term example. |
| KY-DOI-OPEN-RECORDS-PAGE | Kentucky DOI open-records process | Not a smell-mapped source; it is a retrieval path for older filings | N/A | Use only if we need pre-November 2018 filings that are not available through SFA or another public pipeline. |

| ISO-HO-BASE-FORMS | ISO HO 00 03 (Special Form), HO 00 05 (Comprehensive Form) base homeowners policy forms | **Searched 2026-06-04.** KNIC adoption filings reference ISO by SERFF tracking number only — no form text attached (confirmed 2026-06-05 via Perplexity research). ISO files in SERFF as "Insurance Services Office, Inc." with ISOF- tracking prefix. ISO form text is routinely redacted in SFA public view. **Workarounds if Phase 2 ever needs ISO text:** (1) Nevada DOI public portal — has published full HO 00 03 05 11 text publicly; (2) III (Insurance Information Institute) sample HO 3 form; (3) KY DOI open records request. ISO Definitions section is stable across editions (10-00 and 05-11). | 2 (H003) | LOW — not needed for Phase 1. ISO is implicit gold standard; ACV methodology gap is established litigation fact regardless. Needed only for Phase 2 (ISO divergence diff product). |
| KY-KFBM-BASE-FORM-UNREDACTED | KFBM base policy jacket — unredacted full text with Definitions Section | **Updated 2026-06-05:** ISO HO 04 93 confirmed as an endorsement form (Actual Cash Value Loss Settlement — Windstorm/Hail Roof Surfacing), NOT a policy jacket. `KY-SERFF-KFBM-134503212-HO-FORM` is therefore KFBM's version of this endorsement, not their base jacket. KFBM's actual base policy jacket form number is unknown. A redacted base jacket or redacted filing schedule may be enough to document that definition-domain review cannot be completed from public text, but it is not enough to confirm missing definitions. See BACKLOG-021. | 2 (H004) | LOW — optional confidence limitation for now. Do not block higher-value cross-document/package-level work on unredacted proprietary base-form procurement. |

## Current Interpretation

The downloaded corpus gives us enough material to start Stage 002 fixture and detector work. The known gaps mainly affect confidence about current-state carrier practice. They should become active work only if a future experiment needs to prove that a pattern still appears in recent Kentucky homeowners filings.


