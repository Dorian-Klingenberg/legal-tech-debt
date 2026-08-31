# Stage 003 — Twenty-Smell Model Benchmark

**Status:** Ready for model runs; no model-accuracy result has been claimed.

## Objective

Create a self-contained, repeatable benchmark package for twenty legal code smells that are new to the current local engine and Sandbox 007 strategy work. The package should let multiple models or agents receive the same smell-specific task, inspect the same evidence contract, and produce comparable findings without contaminating existing detector calibration.

## Scope decisions

- **In scope:** smell specifications, evidence contracts, synthetic fixtures, expected labels, model task prompts, a manifest, and structural validation.
- **Out of scope:** changing the five Stage 006 detectors, changing Sandbox 007 strategy documents, live cloud deployment, production legal conclusions, and claiming model accuracy before an actual run.
- **Default fixture unit:** JSONL evidence nodes and edges, compatible in shape with the local engine but stored only in this stage.
- **Result policy:** model outputs belong under `results/<run-id>/`; checked-in examples belong under `results/examples/`. No benchmark output is written to the parent engine's `fixtures/` or `tests/` directories.

## Complexity distribution

| Level | Count | Expected evidence shape |
|---|---:|---|
| Low | 8 | One document or a small set of typed nodes; deterministic lexical or presence/absence signal |
| Medium | 8 | Multiple clauses, references, versions, jurisdictions, or competing outcomes; needs contextual reasoning |
| High | 4 | Cross-artifact, temporal, workflow, or structured-system evidence; requires explicit joins and reviewer adjudication |

## Checklist

- [x] Confirm the 20 candidates are outside Stage 006 and Sandbox 007's five strategy smells.
- [x] Establish a separate, easy-to-find Stage 003 directory.
- [x] Define low/medium/high complexity criteria and an 8/8/4 distribution.
- [x] Create four-file smell packets for all twenty smells: specification, positive fixture, negative fixture, and insufficiency fixture.
- [x] Add model-facing prompts with a stable output contract.
- [x] Add a machine-readable manifest with stable IDs and expected labels.
- [x] Validate every smell packet has the required fields and no duplicate IDs.
- [x] Run a local structural benchmark check; keep its output in this stage's `results/` directory.
- [x] Record the benchmark design decisions in ADR-004.
- [x] Update the shared journal and compact agent context at the pause point.

## Work split

The twenty smell packets are divided into five disjoint groups of four. Each group can be designed and fixture-built independently. Integration owns only the shared manifest, validation, and durable memory files.

## Exit criteria

Stage 003 is ready for model runs when every selected smell has a complete packet, the manifest validates, fixtures contain positive/negative/insufficient examples, and a structural check confirms that the benchmark is isolated from the parent engine fixtures and outputs.
