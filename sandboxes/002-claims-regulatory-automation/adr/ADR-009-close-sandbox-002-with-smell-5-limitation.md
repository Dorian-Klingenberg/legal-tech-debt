# ADR-009: Close Sandbox 002 With Smell 5 As A Carried Limitation

Date: 2026-06-04
Status: Accepted
Scope: Sandbox 002 closure and Sandbox 003 start conditions

## Context

Sandbox 002 now has a validated file-backed pipeline over the expanded Kentucky homeowners corpus. Stages 002-007 produce source-traceable nodes, parser diagnostics, citations, broader references, graph edges, candidate evidence, retrieval bundles, deterministic findings, and reviewer reports.

The repaired active run is:

- Stage 002 run: `output/002/20260604_130606_18b0dec5/`
- Sources: 28
- Nodes: 353
- Candidate evidence items: 121
- Stage 003 retrieval bundles: 39
- Detector findings: 23
- Gold-set evaluation: BM25 21/21

One loose thread remains: Smell 5 regulatory-mapping detector calibration. The current detector emits 0 findings on the expanded corpus. That is probably detector under-recall, not proof that the corpus lacks regulatory-mapping risk.

ADR-007 originally listed Smell 5 calibration as a prerequisite before Sandbox 003. After the Stage 002 contract repair and revalidation, keeping Sandbox 002 open only to calibrate one detector would blur the boundary between the evidence substrate and the next product-facing layer.

## Decision

Close Sandbox 002 as complete for its current purpose.

Carry Smell 5 detector calibration forward as a known limitation, not as a blocker to starting Sandbox 003.

Sandbox 003 may begin from run `output/002/20260604_130606_18b0dec5/`, provided it treats Smell 5 honestly:

- do not claim five-smell detector completeness;
- do not treat 0 Smell 5 findings as evidence of no regulatory-mapping risk;
- include Smell 5 as a detector-calibration gap in any executive or triage output;
- if Sandbox 003 needs all five smells represented, pause and calibrate Smell 5 first.

## Consequences

- Sandbox 002 can be documented as complete and preserved.
- Sandbox 003 can start on findings triage and intelligence without reopening ingestion/retrieval architecture.
- Smell 5 remains visible as a limitation for downstream reporting.
- Future work should not mutate Sandbox 002 architecture unless the user explicitly reopens it.

## Rejected Alternatives

- Keep Sandbox 002 open until Smell 5 produces findings.
  - Rejected because the discovery/retrieval/detector/reporting pipeline question has been answered, and Smell 5 calibration is a detector-quality improvement rather than a substrate blocker.
- Drop Smell 5 from the project.
  - Rejected because regulatory mapping remains one of the five active policy-layer smells.
- Treat Smell 5 zero findings as a valid negative result.
  - Rejected because the current evidence points to heuristic under-recall.

## Follow-Up Checklist

- [x] Create Sandbox 002 closure document.
- [x] Update Sandbox 002 handoff and startup docs to point to the repaired run.
- [x] Mark gold-set re-evaluation complete.
- [x] Update Sandbox 003 plan so Smell 5 is a known limitation, not a hard start blocker.
- [ ] Calibrate Smell 5 if Sandbox 003 needs all five smells represented in triage or executive output.
