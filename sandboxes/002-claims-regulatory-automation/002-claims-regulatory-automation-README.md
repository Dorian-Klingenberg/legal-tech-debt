# Sandbox 002: Kentucky Homeowners Policy-Layer Smell Experiments

Status: Active sandbox
Current controlling scope: `002-five-policy-layer-phish.md`
Created: May 2026

## Purpose

Sandbox 002 is the active proof-of-concept lane for Kentucky homeowners insurance legal tech debt experiments.

The work is intentionally narrow: build quick, clean, readable discovery, instrumentation, detectors, and reviewer evidence around the five policy-layer smells in the five-smell report. Sandbox 001 is complete and should be treated as a source of reusable primitives, not as a source of new scope.

## Active Scope

Current focus:

- Kentucky homeowners insurance.
- Policy-layer and claim-adjacent policy interpretation defects.
- Small public source slices, discovery outputs, and clearly marked synthetic seeds only where needed.
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
| `002-RAG-INGESTION-RETRIEVAL-SPEC.md` | Draft engineering spec for local-first discovery-and-instrumentation, structure-aware chunking, citation/reference extraction, graph-linked nodes, parser diagnostics, candidate evidence, and retrieval bundles. |
| `002-RAG-SUBSYSTEM-PLAN.md` | Component plan for the discovery/RAG evidence substrate, including parser instrumentation, reuse from Sandbox 001, and layer boundaries. |
| `002-RAG-STAGE-PLAN.md` | Stage-by-stage build plan for discovery-and-instrumentation, retrieval baselines, semantic retrieval evaluation, detectors, and reviewer report. |
| `adr/ADR-001-rag-substrate-reuses-001-structure.md` | Skill architecture decision to reuse Sandbox 001 graph/data structures and keep findings downstream of RAG storage. |
| `adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md` | Skill architecture decision that semantic vector retrieval is expected but vector store selection is deferred until evaluation. |
| `adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md` | Path decision: discovery-and-instrumentation comes before fixture detectors; parser/reference uncertainty is evidence. |
| `adr/ADR-004-schema-run-identity-and-id-stability.md` | Artifact contract decision: schema versions, run identity, run manifest, and stable IDs are required for Stage 002 outputs. |
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

The next implementation stage should build a narrow Kentucky homeowners discovery-and-instrumentation slice:

```text
stages/
  002-homeowners-discovery-instrumentation/
    STAGE.md
    LESSON.md
    data/
      source_manifest_subset.csv
    src/
    output/
```

That stage should answer:

> Can a small local pipeline turn selected Kentucky homeowners corpus files into source-traceable legal nodes, citations, broader references, conservative graph edges, parser diagnostics, retrieval bundles, and candidate evidence for the five active smells?

The ingestion layer should not make final legal findings. It should emit candidate evidence and machinery confidence: source text, provenance, parser quality, legal structure, citations, broader references, conservative edges, and parser/reference uncertainty. Downstream detector and reporting layers convert those candidates into reviewable findings.

Core outputs should include:

- `schema/` JSON Schemas for every JSON/JSONL artifact type
- `data/heuristics.md`
- `run_manifest.json`
- `sources.jsonl`
- `parser_runs.jsonl`
- `blocks.jsonl`
- `block_stats.jsonl`
- `nodes.jsonl`
- `citations.jsonl`
- `references.jsonl`
- `edges.jsonl`
- `table_failures.jsonl`
- `parse_warnings.jsonl`
- `candidate_evidence.jsonl`
- `retrieval_bundles.json`
- `discovery_report.md`

Each candidate evidence item should also carry a lightweight ROI note using `002-ROI-CASES-FIVE-SMELLS.md`: cost pool, why it matters, reviewer question, and possible fix.

Each JSON/JSONL record should carry `schema_version`, `run_id`, and `created_at`. Source and node IDs should be stable under a fixed parsing strategy; parser or segmentation changes that break ID stability need a version bump and migration note.

Before procuring more sources, inspect `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` and `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`. The current corpus is sufficient to start discovery-and-instrumentation; known SERFF gaps should be chased only when candidate evidence, fixture curation, detector work, or reviewer questions actually need them.

## Working Rule

Keep the sandbox small. A good result here is clear source-traceable evidence, visible parser/reference uncertainty, candidate five-smell examples, and a straightforward path to detectors. Do not build infrastructure until a specific evidence or retrieval failure has earned it.

