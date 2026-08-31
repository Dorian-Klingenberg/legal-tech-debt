# ADR-002: Local Engine Implementation Decisions

**Date**: 2026-08-06  
**Status**: Accepted for Stage 001 review  
**Scope**: Sandbox 008 local legal smell engine

## Context

Stage 001 extracted the five preserved Sandbox 002 Stage 006 detector families
into a standalone local Python package. The user asked for direct Python and
CLI use first, parallel porting of the remaining four detectors, and an ADR
that makes the implementation choices reviewable.

The implementation was validated with six focused `unittest` tests, synthetic
fixtures, CLI probes, and an adapter over the preserved Stage 006 nodes and
edges.

## Decisions and rationale

### 1. Use a standard-library-only runtime core

**Decision:** The package has no runtime dependencies and uses a minimal
`pyproject.toml` for optional installation.

**Why:** The first goal is a generic, open-source-friendly local tool that can
run without Azure, Foundry, an LLM, vector infrastructure, or proprietary
services. This keeps the evidence behavior inspectable and makes later hosting
adapters optional.

### 2. Make generic nodes and typed edges the input boundary

**Decision:** The engine accepts `Node`, `Edge`, and `EvidenceCorpus` contracts
instead of importing Sandbox 002's `RunIndex`.

**Why:** Stage 006's `RunIndex` is valuable but binds the detector to one
evidence substrate. A generic node/edge contract lets Python callers, a CLI,
Codex, MCP, Azure Functions, and Foundry adapters provide evidence in their own
way while preserving source IDs, node IDs, source types, and graph relations.

### 3. Use one run-scoped detector interface and registry

**Decision:** Detectors expose `detect(run: DetectionRun)` and are selected by
stable `SMELL1`–`SMELL5` registry identifiers.

**Why:** The shared run object centralizes timestamps, run identity, finding
IDs, and graph access. The registry keeps the engine extensible without making
the CLI know detector internals. It also made the four remaining ports safe to
implement in parallel with disjoint files.

### 4. Preserve Stage 006 finding fields and add explicit missing evidence

**Decision:** `Finding` retains Stage 006's evidence, provenance, confidence,
rationale, reviewer question, and false-positive fields, with optional
`missing_evidence` and `supporting_nodes` fields.

**Why:** The existing contract already supports human review. Explicit missing
evidence is necessary for graph gaps, incomplete packages, and unresolved
authority references; absence of evidence must not be serialized as a
confirmed legal defect.

### 5. Keep regulatory mapping graph-aware

**Decision:** Smell 5 uses typed edges and a bounded two-hop search for
regulatory relationships, while retaining lexical H001–H003 and package-level
H007 checks.

**Why:** A missing relationship cannot be established by text similarity alone.
The preserved Stage 006 architecture and ADR-010 already established this
boundary, so the generic port carries it forward through `EvidenceCorpus`.

### 6. Provide both JSONL and Markdown outputs

**Decision:** The CLI writes structured JSONL findings and can write a Markdown
review report; the Python API returns `Finding` objects directly.

**Why:** JSONL is easy to pipe into other tools and adapters. Markdown keeps
early output human-readable and diffable. The Python API supports direct use
without forcing callers through a subprocess.

### 7. Preserve the Stage 006 baseline instead of forcing parity immediately

**Decision:** Stage 006 remains untouched. Baseline comparison is recorded as a
calibration test, not an exact-count acceptance gate.

**Why:** The historical runner applies Kentucky-specific corpus filters and
context assumptions that are not part of the first generic contract. The
preserved baseline has 31 findings (S1=1, S2=17, S3=0, S4=1, S5=12); the
generic adapter produced 54 leads (S1=2, S2=39, S3=0, S4=1, S5=12). The delta
is visible evidence that source/package filtering still needs deliberate
design, not a reason to rewrite the historical experiment.

### 8. Use synthetic fixtures and built-in `unittest` first

**Decision:** Stage 001 uses positive, negative, and insufficient-evidence
JSONL fixtures plus the Python standard library's `unittest`.

**Why:** The project is still evaluating the right contract. Synthetic fixtures
are safe to publish and isolate detector behavior; `unittest` avoids making a
test framework a runtime or development prerequisite before the package shape
is settled.

### 9. Defer deployment adapters

**Decision:** Codex skills, MCP, Azure Functions, and Foundry adapters are
follow-on work, not Stage 001 dependencies.

**Why:** Adapters are only useful after the local evidence and result contracts
are stable. Building them first would add hosting decisions before the engine's
false-positive and provenance behavior has been calibrated.

### 10. Use one umbrella review skill over five detector modules

**Decision:** Keep the five smell families as separately addressable engine
modules and stable `SMELL1`–`SMELL5` tools, but expose them through one
repo-visible `local-legal-smell-review` skill.

**Why:** The reusable agent behavior is the review workflow—scope evidence,
run the right detector, preserve provenance, and communicate uncertainty. The
detector-specific logic belongs in Python modules and the registry. Five
duplicate skills would increase maintenance and make cross-smell runs harder
to keep consistent. Separate per-smell skills remain a possible later surface
if real usage shows that trigger precision requires them.

## Validation evidence

- `python -B -m unittest discover -s tests -v` — 6 tests passed.
- CLI registered `SMELL1` through `SMELL5` and produced JSONL findings for all
  five on `fixtures/positive.jsonl`.
- CLI report and JSONL output were exercised through the test harness.
- Preserved Stage 006 baseline was verified as 31 findings with its historical
  per-smell counts.
- Generic engine ran against the preserved nodes/edges through a source-type
  adapter and produced 54 leads.
- Sandbox 002 Stage 006 source and output were not modified.

## Follow-up checklist

- [ ] Make source-layer filtering an explicit generic-engine policy.
- [ ] Investigate and calibrate the S1 and S2 count deltas against Stage 006.
- [ ] Add more labeled negative and insufficient-evidence fixtures from the
      observed false-positive patterns.
- [ ] Validate package installation from a clean checkout.
- [ ] Design the Codex skill and MCP adapter over the stable local API.
- [ ] Evaluate Azure Functions and Foundry hosting only after the local gate.
