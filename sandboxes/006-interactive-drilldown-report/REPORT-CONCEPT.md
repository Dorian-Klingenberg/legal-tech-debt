# Interactive Drill-Down Report Concept

Status: Draft concept note
Date: 2026-06-05
Inputs: Latest Sandbox 004 drill-down reports and `drill_down_entries.json`

## Short Version

The drill-down report is not really a report.

It is a local, interactive expert review workbench for moving from:

> "The detector found something suspicious"

to:

> "A human expert understands the gap, trusts the source trail, sees the business impact, and knows the next action."

Sandbox 004 currently renders this as stacked expert cards. Sandbox 006 should explore the same content as a navigable, filterable, role-aware work surface.

## What The Current Reports Are

The latest Sandbox 004 outputs are static HTML variants:

- `drilldown.html` — combined current generated report.
- `drilldown_KFBM.html` — KFBM internal view.
- `drilldown_KNIC.html` — KNIC internal view.
- `drilldown_KFBM_sanitized.html` — KFBM copyright-safe view.
- `drilldown_KNIC_sanitized.html` — KNIC copyright-safe view.

Each current report is built from `drill_down_entries.json`.

The current conceptual unit is a **finding card**. Each card contains:

- finding identity,
- carrier/source context,
- severity and confidence,
- evidence,
- gap statement,
- compliance/counsel analysis,
- claims analysis,
- policy designer / filing specialist fix guidance,
- disclaimers and limitations.

This is already close to a product. It just presents the product as a scrollable document rather than an interactive workspace.

## What The Interactive Version Should Become

The interactive version should be a **review console** around the finding cards.

It should let a reviewer:

- see the portfolio of findings,
- choose a carrier or combined view,
- filter by smell, severity, confidence, role, and status,
- open one finding without losing orientation,
- toggle internal vs sanitized evidence,
- inspect source trace and limitation notes,
- compare role-specific implications,
- mark review status,
- and decide what action is needed.

The experience should feel like working with an expert dossier, not reading a static memo.

## Core Objects

### Finding

The primary work object.

Current fields already support:

- `entry_id`,
- `heuristic_id`,
- `smell_name`,
- `finding_id` or `finding_ids`,
- `carrier` or `carriers`,
- `source_id`,
- `source_description`,
- `section_path`,
- `confidence`,
- `severity`,
- `scope`,
- evidence/context,
- `gap_statement`,
- role sections.

Interactive additions to consider:

- review status,
- assigned reviewer role,
- accepted/rejected/needs-source decision,
- action priority,
- limitation tags,
- related cases/dollar anchors,
- source availability state.

### Evidence

Evidence has two modes:

- **Internal evidence:** may include verbatim carrier/source text for internal analysis.
- **Sanitized evidence:** paraphrased/copyright-safe, suitable for commercial-facing report output.

The UI should make the mode visible. It should not let users confuse paraphrased evidence with the raw source trail.

### Role Analysis

The current three-panel structure is good content architecture:

- Compliance & Coverage Counsel
- Claims Professional
- Policy Designer / Filing Specialist

In the interactive version, these may become tabs, columns, or role filters depending on layout.

### Source Trace

The current reports include source ID and section path, but the source trace is not yet a first-class interaction.

The interactive version should make source trace more visible:

- source ID,
- source description,
- section path,
- supporting instances,
- citation/regulatory anchors,
- limitation/procurement note,
- internal/sanitized mode state.

## Screen Concept

### 1. Portfolio Overview

Purpose:

Give the reviewer immediate orientation.

Should show:

- finding count,
- carriers represented,
- severity/confidence distribution,
- top categories/smells,
- current mode: internal or sanitized,
- review status summary,
- filters/search.

This screen answers:

> What am I looking at, and where should I start?

### 2. Finding List

Purpose:

Let the reviewer scan and select findings.

Each row/card should show:

- finding headline,
- carrier,
- smell/heuristic,
- severity/confidence,
- one-line gap summary,
- status,
- limitation badge if any.

This screen answers:

> Which issue do I want to inspect?

### 3. Finding Detail

Purpose:

Let the reviewer understand one finding deeply.

Should show:

- headline and badges,
- gap statement,
- evidence summary,
- role analysis,
- suggested fix,
- source trace,
- limitation notes,
- related cases/dollar anchors,
- reviewer status/action controls.

This screen answers:

> Do I trust this, what does it mean, and what should happen next?

### 4. Trace / Evidence Panel

Purpose:

Separate the source trail from the narrative.

Should show:

- internal vs sanitized evidence,
- source ID,
- section path,
- supporting instances,
- regulatory citations,
- case/dollar anchors,
- missing source limitations.

This screen answers:

> Where did this come from, and what uncertainty remains?

## Interaction Ideas

- Carrier filter: all, KFBM, KNIC.
- Mode toggle: internal vs sanitized.
- Role tabs: compliance, claims, policy/forms.
- Severity/confidence filters.
- Status filter: unreviewed, accepted, rejected, needs source, needs counsel.
- Finding detail drawer or split pane.
- Expandable evidence/source trace.
- "Why this matters" collapsed by default for dense mode.
- "Suggested fix" pinned near the action/status controls.

## Design Cautions

- Do not make it a marketing landing page.
- Do not hide source limitations.
- Do not make sanitized mode look like raw evidence.
- Do not turn every finding into a giant card on the overview screen.
- Do not use a dashboard style that implies false precision.
- Do not let Figma/Canva become the source of truth.

## Current Data Readiness Notes

`drill_down_entries.json` is the best starting data source. It is valid JSON and already contains the key content atoms.

`case_library.json` has been repaired to parse as strict JSON. It currently contains 4 cases and 6 gap sentinels. Treat it as a secondary input for case and dollar-anchor panels; the first prototype can still ignore it unless those anchors are needed.

## First Prototype Recommendation

Start with a static HTML prototype using `drill_down_entries.json`.

Do not start with Canva or Figma alone. First decide the information architecture:

- left finding list,
- right finding detail,
- top filter/mode bar,
- role tabs inside the detail,
- collapsible source trace.

Then use Figma to try alternative layouts and Canva to explore visual polish or executive-facing framing.

Client-side Blazor becomes attractive if the prototype grows into:

- reusable finding components,
- richer filter state,
- review status state,
- typed models,
- or multi-view navigation.

For the first interactive proof, static HTML with local JavaScript is enough unless the owner wants to explicitly test Blazor ergonomics.
