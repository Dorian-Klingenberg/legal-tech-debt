# 2026-08-07 — Sandbox 008 Stage 003 Twenty-Smell Benchmark

## Session Summary

Created a separate, model-facing benchmark lane inside Sandbox 008 for twenty
new legal code smells. The benchmark is intentionally separate from the
five-detector local engine and the frozen Sandbox 002 Stage 006 output.

## What Changed

- Added `sandboxes/008-local-legal-smell-engine/stages/003-twenty-smell-model-benchmark/`.
- Selected 20 claims-layer smells outside the Stage 006 and Sandbox 007 named
  smell sets: 8 low complexity, 8 medium complexity, and 4 high complexity.
- Parallelized authoring into five disjoint groups of four smell packets.
- Added 20 `SPEC.md` files and 60 JSONL fixture files: two positive, two
  negative, and one insufficient case per smell, for 100 cases total.
- Added a stable model task/output contract, machine-readable manifest,
  dependency-free validator, and separate `results/` area.
- Added independent contract and taxonomy reviews, then addressed their P1/P2
  fixture and boundary findings.
- Added ADR-004 documenting the isolated benchmark architecture and rejected
  alternatives.

## Validation

- Stage 003 validator: passed 20 packets, 100 cases, and the 8/8/4 split.
- Validator checks JSONL syntax, labels, unique case IDs, node shape, local
  edge endpoints, non-empty edge types, and unique semantic edge triples.
- Existing Sandbox 008 engine suite: 7 tests passed.
- Structural result recorded at
  `sandboxes/008-local-legal-smell-engine/stages/003-twenty-smell-model-benchmark/results/examples/structural-validation-2026-08-07.json`.
- No model accuracy, calibration, legal conclusion, or cloud deployment result
  is claimed.

## Decisions

- Keep exploratory smell packets out of the runtime engine until a later stage
  proves their detector contracts and model usefulness.
- Keep each smell packet self-contained so parallel authoring and per-smell
  error attribution remain possible.
- Make insufficient evidence a first-class label so models are tested on
  abstention and provenance discipline, not only positive detection.
- Preserve taxonomy names while adding explicit benchmark-only boundaries for
  near-duplicates such as claims pricing, SIU routing, and regulatory workflow
  propagation.

## Open Gates

- [ ] Run one or more actual model/agent benchmark runs and store immutable
  predictions under `results/<run-id>/`.
- [ ] Define scoring and human adjudication before interpreting model output.
- [ ] Decide whether any smell earns a production detector implementation.
- [ ] Keep the existing Stage 006 calibration and live adapter validation
  follow-ups separate from this benchmark.
