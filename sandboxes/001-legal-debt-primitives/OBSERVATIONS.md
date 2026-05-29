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
