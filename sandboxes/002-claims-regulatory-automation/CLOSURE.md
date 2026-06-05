# Sandbox 002 Closure

Closed: 2026-06-04
Status: Complete as discovery, retrieval, detector, and reviewer-report proof of concept

## Decision

Sandbox 002 is complete for its current purpose. It should now be treated as a preserved evidence substrate and implementation record, not the active forward-development lane.

The next lanes were completed in Sandbox 003 and Sandbox 004. Current forward work is tracked in `BACKLOG.md`, using the repaired Sandbox 002 run:

`output/002/20260604_130606_18b0dec5/`

## Why We Are Closing 002

Sandbox 002 answered its central question:

> Can a Kentucky homeowners corpus be turned into source-traceable legal evidence, candidate smells, deterministic findings, and reviewer-readable reports without production infrastructure?

The answer is yes.

The pipeline now produces:

- source records with stable identity and content hashes
- parser runs, blocks, block stats, warnings, and table-failure records
- legal nodes with source provenance
- formal citations and broader references as separate artifacts
- conservative graph edges
- candidate evidence for the five policy-layer smells
- retrieval bundles shaped for future hybrid retrieval
- gold-set evaluation reports
- deterministic detector findings
- reviewer-facing HTML and Markdown reports

No database, vector store, service layer, queue, Docker setup, or production API was needed.

## Final Validated State

Active repaired run:

- Stage 002 run directory: `output/002/20260604_130606_18b0dec5/`
- Run ID: `18b0dec5-9a19-4588-a0cd-556db344e8ed`
- Sources: 28
- Blocks: 2,103
- Nodes: 353
- Citations: 100
- References: 55
- Edges: 797
- Candidate evidence: 121
- Stage 002 discovery retrieval bundles: 41
- Stage 003 retrieval bundles: 39
- Stage 006 detector findings: 35

Validation:

- Stage 002 schema validation passed for all contract artifacts.
- Stage 003 retrieval bundles validated against the Stage 002 retrieval-bundle schema.
- Stage 004 gold-set evaluation on run 18b0dec5: phrase 20/21, BM25 21/21.
- Gold-set validator passed all 21 items against run 18b0dec5.
- Stage 006 detectors emitted 35 findings after Smell 5 graph-gap detection was added.
- Stage 007 reviewer report regenerated.

## What 002 Proved

- Docling is useful as a parser/enrichment adapter, not parser truth or a RAG store.
- Parser diagnostics and reference uncertainty belong in the evidence layer.
- JSONL-first artifacts are enough for early discovery, retrieval, detector, and reporting stages.
- Lexical/BM25 retrieval is strong enough for the current document-vocabulary gold set.
- Vector infrastructure should remain deferred for gap-detection smells; ADR-010 established that absence is detected through graph traversal, not vector similarity.
- Deterministic findings are useful but not yet business-accessible enough for an executive audience.

## What Carries Forward To 003

Carry these forward:

- repaired run `output/002/20260604_130606_18b0dec5/`
- Stage 006 findings under `output/006/20260604_130606_18b0dec5/`
- Stage 007 reviewer report under `output/007/20260604_130606_18b0dec5/`
- ADR-008 artifact contract repair
- ADR-010 Smell 5 graph-gap detection decision
- ADR-011 H003 reclassification decision
- human-review framing: findings are not legal conclusions
- source provenance and original evidence text as immutable inputs to triage

## Smell 5 Resolution

ADR-009 originally closed Sandbox 002 with Smell 5 as a carried limitation. Later on 2026-06-04, ADR-010 resolved that limitation by redesigning Smell 5 as graph-based gap detection. The final detector run produced 12 Smell 5 findings and 35 total findings across all five smells.

The important architectural lesson is preserved: regulatory-mapping gaps are absence patterns and should be detected through graph traversal over the evidence substrate, not vector similarity.

## Do Not Reopen By Default

Do not reopen Sandbox 002 for:

- vector database selection
- production APIs
- service layers
- deployment scaffolding
- broad corpus expansion
- live regulatory feeds
- automated legal conclusions

Reopen Sandbox 002 only if the user explicitly asks to improve the evidence substrate, rerun the pipeline with new sources, or calibrate a detector in place.
