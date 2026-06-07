# 2026-06-06 Feasibility Study Consolidation

## Summary

Consolidated the current Legal Tech Debt feasibility and market-validation materials into a dedicated `feasibility-studies/` folder.

This was prompted by the user moving four external reports into the repository root and asking that they be collected with the working notes generated during the feasibility discussion.

## What Changed

- Created `feasibility-studies/README.md` as the discovery surface for the research bundle.
- Created `feasibility-studies/external-reports/` for outside research and counter-report artifacts.
- Created `feasibility-studies/working-notes/` for current prompt and validation planning notes.
- Moved and renamed the four imported reports:
  - `compass_artifact_wf-60f3d885-d033-4399-9296-aff060ef9f7d_text_markdown.md` to `feasibility-studies/external-reports/counter-report-contrarian-review.md`
  - `compass_artifact_wf-ec17d09f-0125-4af8-b10f-7cb0443e2082_text_markdown.md` to `feasibility-studies/external-reports/bull-case-due-diligence-graph-policy-smell-detector.md`
  - `deep-research-report-gpr.md` to `feasibility-studies/external-reports/market-due-diligence-consulting-only.md`
  - `Legal Tech Debt — Market Due-Diligence & Red-Team Evaluation.md` to `feasibility-studies/external-reports/market-due-diligence-red-team-evaluation.md`
- Moved today's working notes:
  - `ai-reality-check-prompt.md` to `feasibility-studies/working-notes/ai-reality-check-prompt.md`
  - `product-validation-targets.md` to `feasibility-studies/working-notes/product-validation-targets.md`
- Moved adjacent feasibility notes from the broader direction-finding thread:
  - `canadian-ai-grant-feasibility.md` to `feasibility-studies/working-notes/canadian-ai-grant-feasibility.md`
  - `mom-executive-summary-draft.md` to `feasibility-studies/working-notes/family-executive-summary-draft.md`

## Current Strategic Framing

The strongest current reframing is:

> Legal Tech Debt may be more valuable as a specialized evidence/review capability for existing insurance compliance, legal, filing, regulatory intelligence, or insurtech providers than as a direct-to-carrier product.

The user explicitly wants to avoid a high-volume direct-sales business, thousands of small customers, repetitive report work, and busy-work-heavy customer chasing.

## Open Questions

- Do incumbents catch the prototype's issue class, and if so, why do clients not care or act?
- If incumbents do not catch the issue class, what exact gap remains?
- Is the defensible value source acquisition, evidence graphing, stable citations, repeatable detectors, human review, audit trail, domain taxonomy, or report packaging?
- Can a skilled professional reproduce most of the value with a general LLM?
- Which provider-side customer could use this capability without requiring the user to build a large sales machine?

## Validation

- Confirmed the moved files exist under `feasibility-studies/`.
- Created a folder-level README with active questions and next-step checklists.

## Next Useful Work

- Load any additional Claude counter-reports into `feasibility-studies/external-reports/`.
- Compare incumbent tools against the exact issue class found by the prototype.
- Prepare a sanitized sample report for Karen and Roger.
- Use the provider-facing business-model constraint when evaluating future market feedback.

## Later Update

Added `feasibility-studies/client-pivot-synthesis-2026-06-06.md` after reviewing all four external reports through the client-base pivot question. The synthesis reframes the strongest current hypothesis as a provider-facing evidence/review capability for existing insurance compliance, filing, legal, regulatory intelligence, actuarial, or insurtech providers rather than a high-volume direct-to-carrier product.
