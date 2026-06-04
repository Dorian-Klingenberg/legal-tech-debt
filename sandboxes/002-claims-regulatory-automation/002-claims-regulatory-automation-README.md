# Sandbox 002: Kentucky Homeowners Policy-Layer Smell Experiments

Status: Complete; preserved as evidence substrate
Current controlling scope: `002-five-policy-layer-phish.md`
Created: May 2026

> Current resume point: read `CLOSURE.md`, `HANDOFF-2026-06-04.md`, `adr/ADR-008-stage-002-artifact-contract-repair.md`, and `adr/ADR-009-close-sandbox-002-with-smell-5-limitation.md`. The active repaired run is `output/002/20260604_130606_18b0dec5/`. New forward work should start in `sandboxes/003-findings-triage/` unless the user explicitly reopens Sandbox 002.

## Purpose

Sandbox 002 was the proof-of-concept lane for Kentucky homeowners insurance legal tech debt experiments.

The work is intentionally narrow: build quick, clean, readable discovery, instrumentation, detectors, and reviewer evidence around the five policy-layer smells in the five-smell report. Sandbox 001 is complete and should be treated as a source of reusable primitives, not as a source of new scope.

## Active Scope

Preserved focus:

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
| `adr/ADR-008-stage-002-artifact-contract-repair.md` | Repair decision: Stage 002 implementation drift was restored to the artifact contract. |
| `adr/ADR-009-close-sandbox-002-with-smell-5-limitation.md` | Closure decision: Sandbox 002 closes with Smell 5 as a carried limitation, not a Sandbox 003 blocker. |
| `CLOSURE.md` | Closure record and final validated state for Sandbox 002. |
| `002-CARRY-FORWARD-FROM-001.md` | What to reuse from Sandbox 001 and what to leave parked. |
| `002-ROADMAP-revised.md` | Active implementation roadmap for Sandbox 002. |
| `HANDOFF-2026-06-04.md` | Current handoff for future agents, including repaired run state and next step. |
| `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv` | Real-document source manifest, downloaded paths, and smell mappings. |
| `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` | Known source gaps and rules for when to chase manual SERFF material. |
| `002-PAIN-POINTS-TAXONOMY.md` | Background rationale only; do not use it to expand active scope. |
| `001-vs-002-REUSE-ANALYSIS.md` | Background reuse analysis only; superseded by current carry-forward guidance. |
| `002-ROADMAP.md` | Historical roadmap only; superseded by the revised roadmap. |

## Final Stage State

Stages 001-007 are complete. The final repaired run is:

`output/002/20260604_130606_18b0dec5/`

Final validated outputs include:

- source-traceable parser artifacts, nodes, citations, references, and graph edges
- parser diagnostics and parse warnings
- candidate evidence for policy-layer smells
- retrieval bundles shaped for future hybrid retrieval
- gold-set evaluation with BM25 21/21
- deterministic detector findings
- reviewer HTML and Markdown reports

## Next Lane

New forward work should move to `sandboxes/003-findings-triage/`.

Sandbox 003 should consume Sandbox 002 outputs rather than mutate the evidence substrate. Smell 5 detector calibration remains a known limitation; downstream work must not claim five-smell completeness unless that detector is calibrated first.

## Working Rule

Treat this sandbox as closed unless the user explicitly reopens it. Do not add infrastructure, broaden corpus scope, or rewrite the Stage 002 artifact contract without a new decision record.

