# Corpus Known Gaps

Status: Active corpus record
Scope: Sandbox 002 Kentucky homeowners five-smell corpus
Last updated: 2026-06-04

This file records what the corpus does not yet contain, so future agents do not confuse missing manually accessed material with an accidental download failure.

The current corpus is intentionally enough to begin proof-of-concept work. These gaps are not blockers by default. Treat them as targeted follow-up only when a detector, fixture, reviewer question, or ROI case needs current carrier-specific evidence that is not already represented by the downloaded sources.

## Operating Rule

- Do not treat these gaps as urgent collection work unless an active experiment runs into them.
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

| ISO-HO-BASE-FORMS | ISO HO 00 03 (Special Form), HO 00 05 (Comprehensive Form) base homeowners policy forms | **Searched 2026-06-04.** KNIC SERFF form filings KNIC-132500003 and KNIC-133829383 inspected — neither contains HO 00 03 or HO 00 05. KNIC-132500003 is an endorsement filing (HO 04 95 water backup); KNIC-133829383 is a non-renewal notice filing. KNIC almost certainly licensed ISO base forms rather than filing them independently. ISO forms are copyrighted; carriers adopt them by reference without re-filing the full text. **Gap remains.** Next procurement paths: (1) KFBM SERFF form filings — search for any filing with "base form" or "HO 00" attachments; (2) Kentucky DOI public portal (insurance.ky.gov) — some states maintain a public form index; (3) ISO directly (subscription service). | 2 (H003), 4 | LOW — no longer blocks H003 drill-down. The finding is undisclosed methodology, not undefined term; ISO HO 00 03 defining ACV is established litigation fact. KFBM base form (HO 04 93) already in corpus. Remaining path: ISO direct subscription if verbatim corpus comparison ever needed. |

## Current Interpretation

The downloaded corpus gives us enough material to start Stage 002 fixture and detector work. The known gaps mainly affect confidence about current-state carrier practice. They should become active work only if a future experiment needs to prove that a pattern still appears in recent Kentucky homeowners filings.


