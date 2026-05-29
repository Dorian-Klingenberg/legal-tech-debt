# Stage 003-kentucky-insurance-sample: Kentucky Insurance Sample

Created: 2026-05-13
Cloned from: `002-dashboard-mockup`

## Purpose

Replace the tiny teaching corpus with a substantially richer synthetic Kentucky auto-insurance sample.

The goal is not legal accuracy. The goal is to stress the extractor, matrix outputs, and static dashboard with data that looks more like a real compliance dependency surface: statutes, administrative regulation fragments, internal claims procedures, product-compliance controls, missing references, cross-document cycles, orphan definitions, and external authority mentions.

## Command

Regenerate the probe output from this stage folder:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Re-embed regenerated output into the static dashboard from the sandbox root:

```powershell
python .\tools\embed_dashboard_data.py .\stages\003-kentucky-insurance-sample
```

Open [dashboard.html](dashboard.html) in a browser.

## Result

The probe produced:

- 60 sections
- 197 references
- 65 matrix nodes, including 5 missing targets
- 48 findings
- 46 cycle nodes in the transitive closure

Finding mix:

- 5 high dangling-reference findings
- 34 medium circular-reference findings
- 3 low orphan-definition findings
- 6 medium unversioned external-authority findings

## Observations

This stage immediately changed the feel of the dashboard. The graph is no longer a hand-sized diagram; it is a navigation surface. The matrix is no longer a cute table; it is the more stable representation for asking source/target reachability questions.

The dashboard had to move from fixed node coordinates to document-based graph lanes. That is the first concrete UI scaling pressure we have seen.

The larger sample also shows why typed edges are not optional for serious legal work. Many circular references are structurally true but not equally suspicious. A statute and an internal procedure can legitimately point to each other if one provides authority and the other implements a control. A plain graph cannot tell that difference.

## Stage Status

Working sample complete. This stage is ready to use as the larger fixture for matrix-performance and typed-edge experiments.
