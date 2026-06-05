# Design Tool Evaluation: Figma And Canva

Status: Active trial brief
Date: 2026-06-05
Scope: Sandbox 006 interactive drill-down report UX

## Purpose

Evaluate whether Figma and Canva are worth keeping in the workflow for the interactive drill-down report.

This is a practical trial, not a tool adoption decision. The question is:

> Do these tools help the owner understand, shape, and judge the report/workbench experience faster than working directly in static HTML and Markdown?

## Trial Rule

Use the same design problem in both tools:

> Design the first screen and one finding-detail view for an interactive expert drill-down report. The report helps an insurance carrier inspect policy/legal tech debt findings, understand evidence and limitations, and decide what action to take next.

The final review artifact for this sandbox remains static HTML. Figma and Canva are design aids only.

## Time Box

Recommended first pass:

- Figma: 45 minutes
- Canva: 45 minutes
- Notes: 15 minutes

Stop when each tool has produced one useful artifact or clearly failed to help.

## What To Make In Figma

Create one small file with:

- one desktop frame for the portfolio/overview screen,
- one desktop frame for a finding-detail screen,
- basic component ideas for filters, severity/confidence badges, role tabs, evidence panels, and status controls,
- brief annotations if the layout idea is not obvious.

Figma success means:

- the layout is easier to reason about than a prose description,
- interaction/state questions become clearer,
- and the design can inform static HTML without becoming a second source of truth.

## What To Make In Canva

Create one small design with:

- a polished overview/cover or executive-summary screen,
- one visual treatment for a finding card or finding-detail section,
- possible typography/color/spacing direction,
- optional stakeholder-facing language for why the report matters.

Canva success means:

- the artifact helps explore polish, brand, and stakeholder presentation,
- the result feels more professional than the default HTML,
- and the useful visual choices can be summarized back into repo notes.

## Shared Content To Use

Use representative Sandbox 004 content:

- Carrier: KFBM or KNIC
- Finding type: calculation methodology, regulatory mapping, or unversioned manual reference
- Required concepts:
  - severity/confidence,
  - evidence summary,
  - source trace,
  - limitation note,
  - suggested fix,
  - reviewer status.

Do not paste long carrier/ISO verbatim policy text into Canva or Figma. Use paraphrased/sanitized evidence language unless the file is clearly private/internal and not intended for sharing.

## Evaluation Rubric

Score each tool from 1 to 5:

| Criterion | Figma | Canva | Notes |
|---|---:|---:|---|
| Speed from blank page to useful artifact |  |  |  |
| Helps clarify interaction/workflow |  |  |  |
| Helps visual polish |  |  |  |
| Easy to translate into static HTML |  |  |  |
| Avoids duplicate-truth risk |  |  |  |
| Pleasant enough to keep using |  |  |  |

## Decision Options

After the trial, choose one:

- **Keep Figma:** use for interaction/wireframe work before larger UI prototypes.
- **Keep Canva:** use for presentation polish, executive mockups, and visual direction.
- **Keep both:** Figma for product interaction; Canva for stakeholder-facing polish.
- **Keep neither:** build directly in static HTML and use screenshots/Markdown notes.
- **Occasional only:** keep accounts only if a specific design/review need appears.

## Notes Template

```markdown
## Figma Notes

- What felt useful:
- What felt annoying:
- What changed my thinking:
- What should carry into static HTML:

## Canva Notes

- What felt useful:
- What felt annoying:
- What changed my thinking:
- What should carry into static HTML:

## Decision

- Keep / cancel / defer:
- Why:
- Next action:
```

