# Stage 002-dashboard-mockup: Dashboard Mockup

Created: 2026-05-13
Cloned from: `001-baseline`

## Purpose

Build a static, self-contained HTML dashboard from the Stage 001 demo output so we can explore ways of seeing the legal dependency system before committing to a real visualization stack.

This stage asks a practical question: when the extractor emits sections, references, dependency roots, cycles, and findings, what kind of interface helps a reviewer understand the system quickly?

## Command

Regenerate the demo output from this stage folder:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Open the mockup directly in a browser:

```powershell
.\dashboard.html
```

## Result

The probe produced:

- 10 sections
- 7 references
- 8 findings
- 1 two-node cycle: Section 400 <-> Section 410
- 1 missing dependency target: Section 900

The stage adds [dashboard.html](dashboard.html), a static dashboard with embedded demo data. It includes:

- a graph view for direct dependencies
- a matrix view for direct adjacency, two-hop reachability, and transitive closure
- a findings view for legal debt issues
- a drill-down panel that keeps section text, outgoing references, incoming references, roots, and nearby findings in one place
- a dark/light theme toggle
- a selected-node dependency-order table under the main matrix
- selectable matrix cells that highlight the source, target, and witness path in the graph

## Observations

The same data becomes easier to understand when the dashboard lets the reader move between three representations:

- the graph answers "what points to what?"
- the matrix answers "what can reach what?"
- the findings table answers "what should someone review?"

The useful idea is not that one representation replaces the others. The graph is a map, the matrix is a calculation surface, and the findings list is a review queue.

The mockup also makes the missing node useful. `missing:900` is not a normal section, but rendering it as a first-class node makes the legal debt visible instead of hiding it in an error message.

The interaction pass made the matrix more than a static table. Selecting a cell now asks a concrete question: "does this source reach this target in the current matrix mode?" If the answer is yes, the dashboard shows a witness path and highlights the matching graph nodes and edges.

## Stage Status

Working mockup complete. This stage is ready to use as a visual reference point for the next experiment.
