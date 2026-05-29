# Stage 004-typed-edge-study: Typed Edge Study

Created: 2026-05-13
Cloned from: `003-kentucky-insurance-sample`

## Purpose

Study whether plain dependency references can be classified into relationship types that make reachability legally meaningful.

Stage 003 proved that the Kentucky-style sample is large enough to expose a real modeling problem: a reference is not yet a relationship. Some edges cite authority, some implement authority, some hand work to another internal procedure, some preserve evidence, some define a term, and some are stale references that should not count as valid access paths.

## Command

Regenerate the inherited Kentucky sample output:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Refresh the embedded dashboard data from the sandbox root:

```powershell
python .\tools\embed_dashboard_data.py .\stages\004-typed-edge-study
```

## Result

Framework setup complete.

Inherited baseline evidence:

- 60 sections
- 197 references
- 65 matrix nodes
- 48 findings

New study artifacts:

- [PLAN.md](PLAN.md)
- [study/EDGE_TYPE_FRAMEWORK.md](study/EDGE_TYPE_FRAMEWORK.md)
- [study/EDGE_LABELING_GUIDE.md](study/EDGE_LABELING_GUIDE.md)
- [study/edge_labeling_seed.csv](study/edge_labeling_seed.csv), with 46 seed edges
- [journal/2026-05-13-work-session.md](journal/2026-05-13-work-session.md)

## Observations

The stage begins as a semantic study rather than an optimization study. Matrix speed matters later, but the Kentucky sample showed that plain closure can answer the wrong question very efficiently.

The first task is to label a controlled subset of edges and decide which relationship types should participate in which reachability rules.

## Stage Status

Framework established. Ready for hand-labeling and typed-matrix implementation.
