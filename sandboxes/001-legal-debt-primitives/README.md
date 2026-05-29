# Sandbox 001: Legal Debt Primitives

Status: Complete as foundational research. See [CLOSURE.md](CLOSURE.md).

This sandbox explores the smallest useful building blocks for a legal tech debt tool:

- extract section anchors from statutes, policies, and internal manuals
- extract references between sections
- detect dangling references
- detect simple circular references
- detect orphan definitions
- flag external authorities that are named without a version, date, or source anchor

The first prototype is intentionally plain Python with no third-party dependencies. That keeps the early experiment focused on the problem shape before choosing NLP frameworks, graph databases, LLM workflows, or legal markup standards.

## Stage Workflow

This sandbox is now staged. The current stable baseline is [stages/001-baseline](stages/001-baseline/STAGE.md).

Use [STAGING.md](STAGING.md) for the workflow and [NEXT_STAGES.md](NEXT_STAGES.md) for candidate follow-on experiments.
Each stage should include a `LESSON.md`; the baseline example is [stages/001-baseline/LESSON.md](stages/001-baseline/LESSON.md).

To start a new stage from the current study:

```powershell
python .\tools\new_stage.py --from 004-typed-edge-study --to 005-typed-matrix-prototype --title "Typed Matrix Prototype" --include-output
```

## Run

From this sandbox folder, the root working copy still runs:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

From a stage folder, use the same command inside that stage:

```powershell
cd .\stages\001-baseline
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Expected outputs:

- `output/findings.json`
- `output/report.md`
- `output/section_index.csv`
- `output/adjacency_matrix.csv`
- `output/two_hop_matrix.csv`
- `output/transitive_closure.csv`
- `output/dependency_roots.json`

The first smoke-test observations are recorded in [OBSERVATIONS.md](OBSERVATIONS.md).
Matrix interpretation notes are recorded in [MATRIX_NOTES.md](MATRIX_NOTES.md).

Stage 003 adds a larger synthetic Kentucky insurance fixture at [stages/003-kentucky-insurance-sample](stages/003-kentucky-insurance-sample/STAGE.md).
Stage 004 sets up typed-edge study materials at [stages/004-typed-edge-study](stages/004-typed-edge-study/STAGE.md).

## Final Question

How far can lightweight parsing plus graph/matrix checks get before we need heavier tools such as Akoma Ntoso, LegalRuleML, spaCy, embeddings, a graph database, or LLM-assisted extraction?

## Final Answer

Lightweight parsing plus graph/matrix checks get far enough to support useful proof-of-concept legal debt detection:

- section/reference extraction
- dangling/null references
- simple circular references
- orphan definitions
- unversioned external authorities
- matrix and dashboard evidence

They also expose the next bottleneck: legal references need semantic relationship types before reachability can be treated as legal or compliance meaning.

That lesson now carries forward into [../002-claims-regulatory-automation](../002-claims-regulatory-automation/002-claims-regulatory-automation-README.md), where the active focus is insurance policy and claims smells.

## Success Criteria

- Complete: The probe finds intentional defects in the sample corpus.
- Complete: The output is understandable enough for a compliance or legal SME to review.
- Complete: The experiment produces a clear next question instead of pretending to be a full solution.

## Non-Goals

- legal interpretation
- jurisdiction-complete compliance analysis
- production-grade citation parsing
- automated legal advice
- semantic equivalence checking
