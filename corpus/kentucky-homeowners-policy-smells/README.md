# Kentucky Homeowners Policy Smells Corpus

Status: Active shared corpus
Related sandbox: `sandboxes/002-claims-regulatory-automation`

This corpus contains real Kentucky homeowners-related insurance source material mapped to the five preserved Sandbox 002 policy-layer smells. Sandbox 002 is closed; the corpus remains an active shared data area.

## Contents

- `_download_manifest.csv` - downloaded source records and smell mappings
- `_download_errors.csv` - download errors
- `_manual_or_skipped_sources.csv` - manual or skipped source records
- `CORPUS-SOURCES.md` - canonical inventory and source-role notes
- `KNOWN-GAPS.md` - known unknowns and when to chase them
- `sources/` - authoritative location for every unique source file
- `Sandbox 002  Kentucky Homeowners Policy-Layer Smell Experiments — Real-Document Corpus Research Report.md` - source research report
- `01-*/` through `05-*/` - historical smell-oriented duplicate views; never use these paths as pipeline source truth

## Relationship To Sandbox 002

Sandbox 002 consumes this corpus. The corpus does not belong to the sandbox.

Stage-specific fixtures, excerpts, and generated outputs should live under the relevant Sandbox 002 stage. Raw downloaded source files and corpus-level manifests should stay here.

## Relationship To Skills

The `legal-rag-builder` skill should read and reference this corpus, but the corpus files do not belong inside the skill.
