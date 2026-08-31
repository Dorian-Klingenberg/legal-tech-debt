# ADR-004 — Isolate the Twenty-Smell Model Benchmark

- **Status:** Accepted
- **Date:** 2026-08-07
- **Context:** Sandbox 008 now has a five-detector local engine and adapter
  scaffolds. The next experiment is intended to exercise new models against
  twenty additional legal code smells without confusing benchmark evidence or
  model outputs with the calibrated Stage 001 engine.

## Decision

Create `stages/003-twenty-smell-model-benchmark/` as a self-contained,
repo-visible benchmark lane with:

- 20 stable smell IDs from the claims and cross-domain taxonomies;
- 8 low-, 8 medium-, and 4 high-complexity tasks;
- one packet per smell containing a specification and positive, negative, and
  insufficient-evidence JSONL fixtures;
- a stable model-facing JSON output contract;
- a manifest and dependency-free structural validator; and
- an immutable-by-convention `results/<run-id>/` area for future model runs.

## Alternatives considered

### A. Add the twenty smells directly to the local engine

Rejected for this experiment. That would mix exploratory detector definitions
with the five-detector calibration surface and make it harder to distinguish a
model benchmark failure from an engine implementation failure.

### B. Keep only prose smell ideas in a planning document

Rejected. Prose alone would not give models stable evidence, abstention, and
provenance tasks to perform. The packet format makes the experiment executable
and reviewable while still avoiding a claim that the smells are production
detectors.

### C. Create one large shared fixture corpus

Rejected for the initial run. Per-smell packets keep positive, negative, and
insufficient evidence local, support parallel authoring, and make it possible
to attribute model errors to one smell contract. A later cross-smell corpus can
be added as a separate benchmark stage if needed.

## Rationale

- **Separation:** benchmark prompts and results cannot silently alter existing
  engine fixtures or Stage 006 reference outputs.
- **Difficulty curve:** the 8/8/4 split starts with deterministic extraction,
  moves through contextual reasoning, and reserves four cases for temporal,
  workflow, and cross-artifact joins.
- **Abstention:** insufficient cases are mandatory so models are evaluated on
  evidence discipline, not only positive recall.
- **Parallel safety:** five workers can author four packets each because their
  write scopes are disjoint; integration owns only the manifest, validator,
  reviews, and memory artifacts.
- **Honest evaluation:** structural validation proves packet integrity, not
  model accuracy. Accuracy, calibration, and legal usefulness remain future
  run-level questions.

## Consequences

- The current benchmark adds 20 experimental smell definitions and 100
  synthetic cases without adding 20 runtime detectors to the local engine.
- Future Python, Codex, Foundry, MCP, or Azure runs can consume the same packet
  and output contract.
- Semantic near-duplicates remain a review risk, so the selection document and
  packet specifications carry explicit boundaries from Stage 006 and Sandbox
  007.
- A future stage must define model adapters, scoring, adjudication, and any
  cross-smell confusion analysis before claiming benchmark performance.
