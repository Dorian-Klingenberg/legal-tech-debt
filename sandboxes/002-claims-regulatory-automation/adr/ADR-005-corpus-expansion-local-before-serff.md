# ADR-005: Expand With All Available Local Sources Before New SERFF Procurement

Date: 2026-06-03
Status: Accepted
Scope: Sandbox 002 corpus management; applies to any future sandbox using SERFF-sourced documents

## Context

After completing Stages 002–007 on a 7-source corpus, the pipeline produced a thin finding set. The question arose: should we procure new sources from SERFF Filing Access, or are there sources already on disk that haven't been added to the manifest?

Inspection revealed that 10 of the 17 downloaded corpus sources were present in `corpus/kentucky-homeowners-policy-smells/sources/` but absent from `source_manifest_subset.csv`. The Stage 002 pipeline had been ignoring them entirely.

Additionally, one file (`KY-KRS-304-13.html`) had been downloaded with the wrong extension — it was PDF content saved as `.html`, causing the pipeline to route it incorrectly.

## Decision

Before procuring any new sources from SERFF Filing Access or other external systems, always:

1. Audit `corpus/.../sources/` against `source_manifest_subset.csv` to identify any downloaded-but-unparsed files
2. Add all available local sources to the manifest first
3. Fix any file extension mismatches (PDF content named .html, etc.) before running the pipeline
4. Only then identify remaining gaps and chase them via SERFF or other procurement

SERFF procurement follows this order of priority:
1. Second carrier homeowners policy forms (cross-carrier comparison is higher value than more regulatory sources)
2. Rate manuals for carriers already in corpus (fills smell 4 gaps)
3. Amendatory endorsements (KY-specific form modifications)
4. Additional regulatory sources only if a specific detector or gold set item needs them

## Consequences

Positive:
- Avoids wasted procurement effort when data is already on disk
- Surfaces file quality issues (extension mismatches, corrupt downloads) early
- Keeps CORPUS-SOURCES.md and KNOWN-GAPS.md as the authoritative state of what exists and what doesn't
- Second carrier data (KFBM) proved to yield the most valuable new findings — cross-carrier comparison confirmed

Tradeoffs:
- Requires an audit step before each procurement session
- Extension mismatch detection requires reading file magic bytes, not just checking filenames

## Rejected Alternatives

- Jump directly to SERFF procurement without auditing local files — risks duplicating work and missing available data
- Automate SERFF scraping — explicitly prohibited by KNOWN-GAPS.md operating rules and SERFF terms
- Treat CORPUS-SOURCES.md as the authoritative list of what's parsed — it documented what was *downloaded*, not what was *manifested*

## Follow-Up

- CORPUS-SOURCES.md now documents all 28 sources and their parsed status
- KNOWN-GAPS.md updated: KFBM gap resolved; remaining gaps are KY-SERFF-KGIC and newer KNIC filings
- Future procurement sessions should start with an audit of sources/ vs manifest before opening a browser
