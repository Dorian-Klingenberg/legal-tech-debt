# Carry Forward from Sandbox 001

Created: 2026-05-29
Status: Active guidance for Sandbox 002

## Decision

Sandbox 001 is complete as foundational research. Sandbox 002 is now the active lane for Kentucky homeowners insurance policy-layer legal tech debt experiments.

The goal is not to copy 001 wholesale. The goal is to carry forward only the proven primitives that help validate the five active homeowners policy-layer smells quickly.

Current scope note: avoid personal auto, motor vehicle, no-fault, and PIP work unless the user explicitly reopens that scope.

## Why 002 Takes Over

Recent research shifted the project from general legal debt primitives to a sharper Kentucky homeowners policy-layer smell focus:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

That means the next experiments should be judged by insurance usefulness, not by whether they complete every interesting primitive from 001.

## Import First

These 001 patterns should be reused early in 002.

| 001 Artifact | Why It Carries Forward | 002 Use |
|---|---|---|
| Plain-Python probe shape | Fast, readable, dependency-light | Start detectors without infrastructure |
| Markdown corpus layout | Easy source slices and reviewable text | Homeowners policy, statute, regulation, bulletin, and filing samples |
| Section extraction | Needed for clause-level analysis | Policy/claim manual section indexing |
| Reference extraction | Foundation for regulatory mapping and unversioned reference smells | Internal and external citation detection |
| Dangling reference detector | Supports Regulatory Mapping Smells | Null or missing Kentucky references |
| Circular reference detector | Useful for circular definitions and coverage logic loops | Support for Coverage Inversion / Contradictory Conditions |
| Orphan definition detector | Useful for dead terms and stale definitions | Support for Magic Number / Magic Valuation Terms |
| JSON findings | Machine-readable evidence | `findings.json` for 002 reports |
| Markdown report | Human-readable evidence | Compliance/SME review report |
| Matrix outputs | Useful for impact and reachability when small | Show affected downstream sections |
| Static dashboard pattern | Proven review surface | Optional 002 visual drill-down |
| Stage workflow | Keeps experiments disciplined | Numbered 002 proof-of-concept stages |
| Lesson files | Preserves what each experiment taught | Every material 002 stage should explain itself |

## Adapt Before Reuse

These should be adapted rather than copied directly.

| 001 Concept | Adaptation Needed for 002 |
|---|---|
| Finding types | Rename around the five active smells from `002-five-policy-layer-phish.md` |
| Severity | Tie to review urgency and business/legal exposure, not only structural graph severity |
| Edge types | Keep the idea, but use only types needed for the detector under test |
| Dashboard labels | Use insurance policy/claims language, not generic graph language |
| Corpus | Use real Kentucky homeowners source slices first; use synthetic seeds only when clearly marked and traceable to real source context |
| Reports | Include "why it matters" and reviewer questions, not legal advice |

## Do Not Import Yet

These are parked until a concrete 002 stage earns them.

- graph database
- live regulatory feed ingestion
- PAS integration
- containerized services
- background jobs
- full typed-matrix implementation
- LLM extraction pipeline
- production citation parser
- automated legal interpretation

## First 002 Implementation Target

The first practical 002 implementation should be a small homeowners-focused discovery-and-instrumentation pipeline:

Question:

> Can selected Kentucky homeowners corpus files become source-traceable legal nodes, citations, broader references, conservative graph edges, parser diagnostics, retrieval bundles, and candidate evidence for the five active smells?

Use the 001 probe style:

- plain Python
- local source slices
- no services
- JSON/Markdown/CSV outputs
- readable discovery and instrumentation logic
- explicit limitations

Candidate evidence should align to the five active smells:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

## Suggested Stage Shape

The initial import stage has been created at `stages/001-foundation-import`.

Future implementation stages should follow the same shape:

```text
stages/
  002-homeowners-discovery-instrumentation/
    STAGE.md
    LESSON.md
    data/
    src/
    output/
```

The fixture should be curated from discovery outputs, not built as a fully manual first pass.

## Success Criteria

The first 002 stage is successful if:

- it runs locally without infrastructure
- it reuses or mirrors the useful 001 probe structure
- it emits parser diagnostics and candidate evidence a compliance/product/claims reviewer could understand
- it demonstrates at least one candidate evidence item or seeded example for each active smell, or documents why the selected corpus slice did not support one
- it separates citations from broader references
- it keeps graph edges conservative and auditable
- it documents what still requires human review

## Carry-Forward Rule

If a 001 feature does not directly help a high-value insurance smell, leave it parked.

002 should stay narrow, readable, and evidence-driven.
