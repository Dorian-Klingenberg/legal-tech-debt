# Journal - June 1, 2026

## Focus

Today was about turning Sandbox 002 from aligned planning into an evidence-backed Kentucky homeowners corpus, then pausing to make sure future agents inherit the working memory.

The main shift:

> Sandbox 002 now has a real-document corpus and a written record of both what we know and what we know we do not know yet.

## What Changed

### 1. Reconfirmed The Active Scope

Sandbox 002 remains focused on Kentucky homeowners insurance and the five policy-layer smells:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

Auto, motor vehicle, no-fault, PIP, broad claims-platform work, live feeds, PAS integration, and production infrastructure remain out of scope unless explicitly reopened.

### 2. Built The Real-Document Corpus

The new corpus report in `sandboxes/002-claims-regulatory-automation/corpus/` contained a manifest of directly downloadable Kentucky homeowners-related sources.

Downloaded sources were organized into one directory per active smell:

```text
corpus/
  01-overbroad-nondeterministic-exclusions/
  02-magic-number-magic-valuation-terms/
  03-coverage-inversion-contradictory-conditions/
  04-calculation-rule-drift-unversioned-rate-reference/
  05-regulatory-mapping-smells/
```

Final corpus counts:

| Directory | File Count |
|---|---:|
| `01-overbroad-nondeterministic-exclusions` | 6 |
| `02-magic-number-magic-valuation-terms` | 7 |
| `03-coverage-inversion-contradictory-conditions` | 7 |
| `04-calculation-rule-drift-unversioned-rate-reference` | 6 |
| `05-regulatory-mapping-smells` | 16 |

The corpus now includes 42 smell-specific source copies representing 17 unique public sources.

### 3. Added Corpus Tracking Files

The corpus now has explicit tracking records:

- `corpus/_download_manifest.csv` records downloaded sources and their smell mappings.
- `corpus/_download_errors.csv` records download failures. It is currently clear except for the header.
- `corpus/_manual_or_skipped_sources.csv` records sources that were not directly downloaded.
- `corpus/KNOWN-GAPS.md` records known missing evidence and when to chase it.

The KRS 304.44 mine-subsidence source originally pointed to a Justia URL that returned 403. It was replaced with the official Kentucky Legislative Research Commission chapter page:

```text
https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38764
```

### 4. Converted Manual SERFF Work Into Known Gaps

Manual SERFF sources are no longer treated as urgent chores or blockers. They are now recorded as known gaps.

Known gaps:

- `KY-SERFF-KFBM-POST2018`
- `KY-SERFF-KGIC-POST2018`
- `KY-SERFF-KNIC-POST2018`
- `KY-DOI-OPEN-RECORDS-PAGE`

Working rule:

> Do not chase these unless an active fixture, detector, reviewer question, or ROI case needs the missing evidence.

This keeps the project honest without stopping the experiment.

### 5. Updated Cross-Agent Startup Memory

The shared agent entry points were updated so Codex, GitHub Copilot, Claude Code, and future agents all receive the same instructions.

Updated:

- `BOOTSTRAP.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`

The new shared startup expectation is:

- read the bootstrap first
- read the relevant agent entry file
- read Sandbox 002 docs before changing Sandbox 002
- inspect the current handoff
- inspect the corpus manifest and known gaps before procuring more source material
- write durable memory into shared files, not assistant-private memory only
- add journal and handoff records at major pause points

## Current State

Sandbox 002 is ready to move from corpus procurement into fixture construction and detector work.

The project does not need more data collection before starting Stage 002 unless the first fixture runs into a specific missing source need.

The next work should stay small:

> Extract a handful of source-traceable excerpts from the corpus and build the first homeowners five-smell fixture.

## Next Good Step

Create the next stage:

```text
sandboxes/002-claims-regulatory-automation/stages/002-homeowners-policy-layer-smells/
```

The stage should use the downloaded corpus to create a small fixture with at least one source-traceable example for each of the five smells. It should not chase SERFF gaps unless the downloaded corpus cannot support one of the five examples.

