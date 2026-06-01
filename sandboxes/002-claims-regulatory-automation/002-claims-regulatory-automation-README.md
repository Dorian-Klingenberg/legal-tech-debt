# Sandbox 002: Kentucky Homeowners Policy-Layer Smell Experiments

Status: Active sandbox
Current controlling scope: `002-five-policy-layer-phish.md`
Created: May 2026

## Purpose

Sandbox 002 is the active proof-of-concept lane for Kentucky homeowners insurance legal tech debt experiments.

The work is intentionally narrow: build quick, clean, readable detectors and fixtures around the five policy-layer smells in the five-smell report. Sandbox 001 is complete and should be treated as a source of reusable primitives, not as a source of new scope.

## Active Scope

Current focus:

- Kentucky homeowners insurance.
- Policy-layer and claim-adjacent policy interpretation defects.
- Small public or synthetic fixtures.
- Plain local scripts and reviewable Markdown/JSON/CSV outputs.
- Human-readable evidence that a policy, claims, compliance, or product reviewer can understand.

Out of scope unless explicitly reopened:

- Personal auto, motor vehicle, no-fault, and PIP.
- Broad claims platform work.
- Live regulatory feeds.
- PAS or carrier system integration.
- Databases, services, schedulers, Docker, or production architecture.
- LLM/NLP pipelines unless a later stage earns them with a concrete need.

## Five Active Smells

All Sandbox 002 documentation, plans, stages, and fixtures should align to these smells:

| Smell | What We Are Looking For |
|---|---|
| Overbroad / Non-deterministic Exclusions | Exclusions with sweeping trigger language, broad subjects, or conflicts with the coverage grant. |
| Magic Number / Magic Valuation Terms | Undefined timing, valuation, or calculation terms where a concrete number, formula, or version is needed. |
| Coverage Inversion / Contradictory Conditions | Broad grants that are hollowed out by exclusions, endorsements, exceptions, or conflicting priority rules. |
| Calculation Rule Drift / Unversioned Rate Reference | Rating or valuation rules that depend on unversioned manuals, current guidelines, or opaque formulas. |
| Regulatory Mapping Smells | "Per state law" and similar null references with no Kentucky citation, schedule, parameter, or versioning. |

See `002-five-policy-layer-phish.md` for the controlling detection specs and Gherkin scenarios.

## Relationship To Sandbox 001

Sandbox 001 proved useful legal debt primitives:

- section extraction
- reference extraction
- dangling/null reference detection
- circular reference detection
- orphan definition detection
- graph/matrix outputs
- JSON, Markdown, CSV, and static dashboard evidence
- staged proof-of-concept workflow

Sandbox 002 should reuse those only where they help the five active homeowners policy-layer smells. The primitive is support equipment, not the mission.

See `002-CARRY-FORWARD-FROM-001.md` for the carry-forward rules.

## Current Documentation Map

| Document | Role |
|---|---|
| `002-five-policy-layer-phish.md` | Source of truth for active detector scope. |
| `002-ROI-CASES-FIVE-SMELLS.md` | Smell-specific ROI cases, public cost anchors, service pricing, and buyer savings logic. |
| `002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md` | How to collect Kentucky homeowners source material for the five smells. |
| `002-RAG-INGESTION-RETRIEVAL-SPEC.md` | Draft engineering spec for local-first legal corpus ingestion, structure-aware chunking, citation extraction, graph-linked nodes, and retrieval bundles. |
| `002-RAG-SUBSYSTEM-PLAN.md` | Component plan for the RAG evidence substrate, including reuse from Sandbox 001 and layer boundaries. |
| `002-RAG-PHASE-PLAN.md` | Phased build plan for file-backed ingestion, retrieval bundles, semantic retrieval evaluation, and store selection. |
| `../../skills/legal-rag-builder/adr/ADR-001-rag-substrate-reuses-001-structure.md` | Skill architecture decision to reuse Sandbox 001 graph/data structures and keep findings downstream of RAG storage. |
| `../../skills/legal-rag-builder/adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md` | Skill architecture decision that semantic vector retrieval is expected but vector store selection is deferred until evaluation. |
| `002-CARRY-FORWARD-FROM-001.md` | What to reuse from Sandbox 001 and what to leave parked. |
| `002-ROADMAP-revised.md` | Active implementation roadmap for Sandbox 002. |
| `HANDOFF-2026-06-01.md` | Current handoff for future agents, including corpus state and next step. |
| `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` | Real-document source manifest, downloaded paths, and smell mappings. |
| `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` | Known source gaps and rules for when to chase manual SERFF material. |
| `002-PAIN-POINTS-TAXONOMY.md` | Background rationale only; do not use it to expand active scope. |
| `001-vs-002-REUSE-ANALYSIS.md` | Background reuse analysis only; superseded by current carry-forward guidance. |
| `002-ROADMAP.md` | Historical roadmap only; superseded by the revised roadmap. |

## Current Stage

`stages/001-foundation-import` imports the small Sandbox 001 probe shape and proves that it still runs against a tiny homeowners-oriented synthetic fixture.

It is a bridge stage. It does not yet implement the five active smells.

## Next Stage

The next implementation stage should build a narrow Kentucky homeowners fixture for all five active smells:

```text
stages/
  002-homeowners-policy-layer-smells/
    STAGE.md
    LESSON.md
    data/
      raw/
      processed/
    src/
    output/
```

That stage should answer:

> Can a small local probe detect the five policy-layer smells in a Kentucky homeowners fixture well enough to produce useful reviewer questions?

Each finding should also carry a lightweight ROI note using `002-ROI-CASES-FIVE-SMELLS.md`: cost pool, why it matters, reviewer question, and possible fix.

Before procuring more sources, inspect `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` and `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`. The current corpus is sufficient to start fixture construction; known SERFF gaps should be chased only when an active experiment runs into them.

## Working Rule

Keep the sandbox small. A good result here is a clear fixture, clear detector logic, and clear evidence. Do not build infrastructure until a specific smell cannot be evaluated without it.

