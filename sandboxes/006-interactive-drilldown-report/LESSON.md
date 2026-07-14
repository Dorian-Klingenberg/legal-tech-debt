# Lesson: A Report Becomes A Workbench When Evidence, Interpretation, And Action Stay Distinct

Status: Provisional lesson from the Stage 001/002 implementation; human visual review pending
Date: 2026-07-13

## What Happened

Sandbox 004 proved that a finding could be rendered as an expert report card. Sandbox 006 reorganized the same content into a persistent finding list, selected-finding detail, role views, evidence mode, source trace, and reviewer status controls.

## Lesson

Interactivity is useful here when it preserves three different jobs:

1. **Evidence:** what source material and limitations support the finding.
2. **Interpretation:** why different professional roles may care.
3. **Action:** what review state or next step a human chooses.

Combining those jobs into one long narrative makes uncertainty and provenance hard to scan. Treating them as separate panels or states lets a reviewer move from detection to judgment without mistaking a detector signal for a legal conclusion.

## What Is Proven

- [x] Real Sandbox 004 entry data can drive a local static workbench.
- [x] Plain HTML, CSS, and JavaScript can support the first interaction model.
- [x] Internal and sanitized evidence can switch without changing finding identity.
- [x] Reviewer workflow state can be explored without persistence or a backend.

## What Is Not Proven

- [ ] The current layout works well at desktop and mobile sizes.
- [ ] The status vocabulary matches a real provider workflow.
- [ ] Figma or Canva would improve the experience.
- [ ] Users want this workbench or would pay for it.
- [ ] The prototype data model is sufficient for production.

## Reuse Rule

Future report or product work should keep evidence, interpretation, and human action distinguishable. It should not copy the current layout until the human review gate is complete.

