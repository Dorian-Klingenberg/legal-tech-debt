# Observations

## Smoke Test: Initial Synthetic Corpus

Command:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Result:

- 10 sections found
- 7 section references found
- 8 findings generated

Detected seeded issues:

- dangling reference: Section 300 references missing Section 900
- circular reference: Section 400 and Section 410 reference each other
- orphan definitions: Covered vehicle, Legacy endorsement, Policy year
- unversioned external authorities: NAIC and ISO references without version/date anchors

## What Existing Technology Already Gives Us

- Plain regex parsing can catch basic structural debt surprisingly quickly.
- A lightweight in-memory graph is enough for the first dependency checks.
- Markdown and JSON are sufficient for early human-review artifacts.
- Deterministic detectors are explainable, which matters for legal/compliance review.

## What Looks Like Custom Build Work

- A robust legal citation parser that handles jurisdiction, title, chapter, section, subsection, and form identifiers.
- A normalized obligation schema with authority references, scope, triggers, actions, evidence, owner, and lifecycle status.
- A review workflow where legal/compliance SMEs accept, reject, or annotate findings.
- Drift detection that compares versions of external statutes, forms, circulars, and internal artifacts.
- Severity scoring that reflects legal/compliance risk, not only text structure.

## First Surprise

The first implementation accidentally treated section headings as self-references. That false-positive class was easy to fix in the toy corpus, but it is a useful warning: real legal text will need source-aware parsing, not only global text scanning.

## Next Best Experiment

Compare graph traversal with matrix closure on the same extracted references. The first matrix version now emits direct adjacency, two-hop dependencies, transitive closure, terminal dependency roots, and cycle nodes without committing to Neo4j or a numerical stack too early.

## Stage 002 Dashboard Mockup

The static dashboard showed that the current output is already rich enough to support a small review experience. The most useful pattern is the combination of:

- graph view for direct dependencies
- matrix view for reachability
- findings view for triage
- drill-down panel for source text and local context

The matrix view is especially promising as a teaching and analysis surface. It lets us show direct adjacency, two-hop relationships, and transitive closure using the same node ordering, which makes the difference between "points to" and "can reach" concrete.

The second dashboard pass made the matrix interactive. A selected cell now behaves like a question about one source/target pair. When the relationship exists, the dashboard shows the witness path and highlights the involved nodes and edges in the graph. This is a useful bridge between matrix math and legal explainability.

The selected-node dependency-order panel is also promising. It shows the exact powers of the adjacency matrix that matter for the currently selected node, then summarizes the highest order that adds new information.

The next visual problem is typed reachability. A plain edge is too simple for legal work; references may mean definition, exception, authority, evidence, duty, or background context. A future stage should test whether edge-type matrices can answer "reachable through what kind of legal relationship?" without becoming opaque.

## Stage 003 Kentucky Insurance Sample

The larger Kentucky-style corpus produced 60 sections, 197 references, 65 matrix nodes, and 48 findings.

The dashboard needed a data-driven graph layout immediately. Fixed coordinates were acceptable for the tiny Stage 002 fixture, but they would have made this stage fragile. Document lanes are a first simple compromise: they preserve source-document context while allowing the graph to grow.

The result also shows that circularity alone is not enough. Many cycles are structural artifacts of authority/procedure relationships. The next detector should know whether an edge means citation, implementation, evidence, exception, definition, record retention, or workflow delegation.

## Stage 004 Typed Edge Study

The typed-edge study begins with a semantic reframing:

A reference is not yet a relationship.

The plan is to hand-label a representative subset of edges before adding automation. This should prevent the implementation from freezing bad assumptions into code too early.

The initial seed queue has examples of authority implementation, validation, workflow handoff, proof requirements, reporting requirements, evidence packets, retention duties, review loops, and stale references. The next useful evidence will be a comparison between plain reachability and typed reachability on the same source/target pairs.
