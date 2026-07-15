# 2026-07-14 Sandbox 007 Five-Smell Lessons

## Session Summary

Created one reusable detector-design lesson for each smell in Sandbox 007's
Detection Strategy Matrix:

- Circular Definition;
- Rule Duplication;
- Hardcoded Jurisdiction Logic;
- Null Reference Clause; and
- Spec-Code Divergence.

The work used `skills/write-lesson/SKILL.md` and the shared
`project-memory-artifacts` workflow. It was isolated on
`codex/policy-smell-lessons` because the original `main` checkout was two
commits behind and contained many unrelated local modifications. The clean
worktree was based on merged upstream `main`, where Sandbox 007 already exists.

## What Changed

- Added the [Sandbox 007 lesson catalog](../sandboxes/007-policy-smell-detector-strategies/lessons/README.md).
- Added five smell-specific lesson files beneath that catalog.
- Updated the [Sandbox 007 README](../sandboxes/007-policy-smell-detector-strategies/README.md) to make the lessons discoverable and preserve the Sandbox 002 closure boundary.
- Updated the [Detection Strategy Matrix](../sandboxes/007-policy-smell-detector-strategies/DETECTION_STRATEGY_MATRIX.md) to label candidate evidence, future targets, and unavailable comparators accurately.
- Updated the [Stage 001 completion record](../sandboxes/007-policy-smell-detector-strategies/STAGE-001-COMPLETION.md) with a post-research evidence-boundary clarification and lesson links.
- Added the Sandbox 007 catalog to the [top-level lesson index](../lessons/README.md).

No detector code, corpus source, preserved Sandbox 002 output, project count,
active lane, or owner gate changed.

## Decisions Made

- Keep the five lessons sandbox-local because they teach Sandbox 007 detector
  design and have not yet been validated as cross-project detector results.
- Use only synthetic teaching examples. Real corpus evidence is identified by
  source ID and paraphrased.
- Treat Stage 001's counts and precision values as Stage 002 targets, not
  achieved measurements.
- Separate the evidence boundary for each smell:
  - Circular Definition has one literal term-echo candidate.
  - Rule Duplication has lineage, delta, and fan-out candidates, but no
    validated independent duplicate cluster.
  - Hardcoded Jurisdiction Logic has state-scoped rule candidates, but
    package-level authority resolution remains open.
  - Null Reference Clause has no validated instance and requires authoritative
    identity, supersession, and temporal metadata.
  - Spec-Code Divergence cannot be established without a version-aligned
    system-side comparator.
- Reuse Sandbox 002's stable identity and provenance principles without
  silently extending its closed schemas or adding findings to preserved output.

## Validation Performed

- [x] Inspected the canonical policy-smell definitions and all Sandbox 007
      Stage 001 documents.
- [x] Used direct PDF text extraction to verify the narrow candidate signals
      described for Circular Definition, Rule Duplication, and Hardcoded
      Jurisdiction Logic. The roof-form comparison used the KFBM markup and ISO
      endorsement, not the redacted KFBM public-view artifact.
- [x] Inspected Sandbox 002's graph builder and confirmed that current
      `defines_term` edges are node-to-self extraction markers, not semantic
      term-dependency edges.
- [x] Inspected the reference extractor and source schema and confirmed that
      they do not establish live-authority identity, supersession, or effective
      intervals.
- [x] Confirmed the corpus has no PAS/configuration comparator for Spec-Code
      Divergence.
- [x] Verified that exactly five lesson files exist and each contains the
      lesson skill's required sections.
- [x] Checked 49 local Markdown links across all eleven lesson, discovery, and
      journal files; all resolved.
- [x] Checked touched files for trailing whitespace and final newlines.
- [x] Ran focused `git diff --check`; it passed with only expected Git line-ending
      notices.
- [x] Completed an independent evidence review and corrected four issues: a
      leftover self-loop instruction, an ambiguous redacted source ID, the Null
      Reference archive dependency, and wording that implied mutation of
      preserved Sandboxes 003–004.

## Current State

Sandbox 007 Stage 001 remains complete and Stage 002 remains ready but not
started. The lesson set is complete as detector-design guidance. No precision,
recall, or finding-count target is validated, and the lessons state those limits
explicitly.

`AGENT_CONTEXT.json` was intentionally not changed because this work did not
change the current lane, evidence counts, open gates, or startup contract. No
handoff was needed because there is no partially completed implementation to
resume.

## What Comes Next

- [ ] Review the five lessons for preferred teaching tone and depth.
- [ ] If Sandbox 007 Stage 002 starts, create labeled synthetic positive and
      negative cases before reporting detector accuracy.
- [ ] Add authoritative current and archival lookup data before validating a
      Null Reference Clause finding.
- [ ] Design a synthetic, versioned spec-to-configuration contract before
      seeking access to real system artifacts.
