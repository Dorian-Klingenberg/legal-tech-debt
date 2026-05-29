# Carry Forward from Sandbox 001

Created: 2026-05-29
Status: Active guidance for Sandbox 002

## Decision

Sandbox 001 is complete as foundational research. Sandbox 002 is now the active lane for Kentucky homeowners insurance policy and claims legal tech debt experiments.

The goal is not to copy 001 wholesale. The goal is to carry forward the proven primitives that help validate high-value homeowners insurance smells quickly.

Current scope note: avoid personal auto, motor vehicle, no-fault, and PIP work unless the user explicitly reopens that scope.

## Why 002 Takes Over

Recent research shifted the project from general legal debt primitives to a sharper insurance focus:

- insurance policy smells
- insurance claims smells
- real-world cost events
- process maturity gaps
- high-value defect classes with economic consequences

That means the next experiments should be judged by insurance usefulness, not by whether they complete every interesting primitive from 001.

## Import First

These 001 patterns should be reused early in 002.

| 001 Artifact | Why It Carries Forward | 002 Use |
|---|---|---|
| Plain-Python probe shape | Fast, readable, dependency-light | Start detectors without infrastructure |
| Markdown corpus layout | Easy fixtures and reviewable source text | Homeowners policy, claims, statute, regulation, bulletin, and filing samples |
| Section extraction | Needed for clause-level analysis | Policy/claim manual section indexing |
| Reference extraction | Foundation for null references and drift | Internal and external citation detection |
| Dangling reference detector | Directly maps to Broken Link / Null Reference smells | First high-value detector |
| Circular reference detector | Useful for circular definitions and coverage logic loops | Secondary structural detector |
| Orphan definition detector | Useful for dead terms and stale definitions | Policy wording hygiene detector |
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
| Finding types | Rename around insurance smells: Broken Link, Calculation Rule Drift, Coverage Inversion, Magic Number Term, Regulatory Drift |
| Severity | Tie to review urgency and business/legal exposure, not only structural graph severity |
| Edge types | Keep the idea, but use only types needed for the detector under test |
| Dashboard labels | Use insurance policy/claims language, not generic graph language |
| Corpus | Use synthetic but homeowners-insurance-realistic policy, claims, statute, bulletin, and rating-spec fixtures |
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

The first practical 002 implementation should be a small homeowners-focused dual-detector probe:

1. Broken Link / Null Reference Clause
2. Calculation Rule Drift

Use the 001 probe style:

- plain Python
- local synthetic fixture
- no services
- JSON/Markdown/CSV outputs
- readable detector logic
- explicit limitations

## Suggested Stage Shape

The initial import stage has been created at `stages/001-foundation-import`.

Future implementation stages should follow the same shape:

```text
stages/
  002-dual-detector-probe/
    STAGE.md
    LESSON.md
    data/
    src/
    output/
```

Suggested question:

> Can the 001 legal debt primitives be adapted into a Kentucky homeowners insurance probe that detects broken/null references and one narrow calculation drift in a synthetic homeowners policy/claims fixture?

## Success Criteria

The first 002 stage is successful if:

- it runs locally without infrastructure
- it reuses or mirrors the useful 001 probe structure
- it emits findings a compliance/product/claims reviewer could understand
- it demonstrates at least one Broken Link / Null Reference finding
- it demonstrates at least one Calculation Rule Drift finding
- it documents what still requires human review

## Carry-Forward Rule

If a 001 feature does not directly help a high-value insurance smell, leave it parked.

002 should stay narrow, readable, and evidence-driven.
