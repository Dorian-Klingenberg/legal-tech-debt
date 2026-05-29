# Stage 004: Typed Edge Study

This stage asks whether the Kentucky insurance dependency graph can become semantically meaningful by classifying edges.

The inherited dashboard still shows plain references. The study artifacts define the next layer: typed edges and typed reachability.

## Run

From this stage folder:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

From the sandbox root, refresh the static dashboard after regeneration:

```powershell
python .\tools\embed_dashboard_data.py .\stages\004-typed-edge-study
```

## Study Files

- [PLAN.md](PLAN.md): staged plan for the typed-edge investigation
- [study/EDGE_TYPE_FRAMEWORK.md](study/EDGE_TYPE_FRAMEWORK.md): taxonomy, rules, and matrix interpretation
- [study/EDGE_LABELING_GUIDE.md](study/EDGE_LABELING_GUIDE.md): how to label edges consistently
- [study/edge_labeling_seed.csv](study/edge_labeling_seed.csv): first labeling queue
- [journal/2026-05-13-work-session.md](journal/2026-05-13-work-session.md): detailed journal entry for the work session

## Starting Principle

A reference says that one text points to another text.

A relationship says why that pointer matters.

This stage is about discovering the second thing.
