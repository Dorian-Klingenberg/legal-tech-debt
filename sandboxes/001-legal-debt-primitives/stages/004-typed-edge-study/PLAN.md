# Typed Edge Study Plan

## Purpose

Turn the Stage 003 Kentucky insurance sample into a semantic dependency study.

The central hypothesis is that legal dependency analysis needs typed edges before matrix reachability becomes trustworthy.

## Working Question

Can a matrix-based dependency system distinguish valid legal/compliance access from plain graph reachability by using relationship types?

## Phase 1: Label a Controlled Edge Set

Inputs:

- `output/findings.json`
- `output/dependency_roots.json`
- `study/edge_labeling_seed.csv`

Work:

- Review the seed CSV row by row.
- Confirm or revise the proposed edge type.
- Mark confidence as `high`, `medium`, or `low`.
- Record ambiguous cases in the `notes` column.

Done when:

- at least 40 representative edges are labeled
- every label has a short rationale
- stale and missing-target references are explicitly identified

## Phase 2: Define Typed Matrix Semantics

Work:

- Decide whether each edge type participates in legal reachability.
- Decide which edge types are informational only.
- Draft path-composition rules.
- Identify paths that plain closure includes but typed closure should exclude.

Done when:

- `A_type` matrix layers are named
- invalid path examples are documented
- at least five witness paths have expected typed outcomes

## Phase 3: Build the First Typed Matrix Prototype

Work:

- Add a typed edge label loader.
- Emit one adjacency matrix per edge type.
- Emit a typed reachability report.
- Compare typed reachability to plain transitive closure.

Done when:

- the probe emits typed matrix artifacts
- the report lists paths that changed meaning after typing
- the output can still be explained from source snippets

## Phase 4: Update the Dashboard

Work:

- Add edge-type filtering.
- Show the type of each edge in witness paths.
- Let the matrix switch between plain closure and typed closure.
- Highlight invalid/stale path segments differently.

Done when:

- clicking a matrix cell explains the edge-type path
- stale references are visible but excluded from valid reachability
- at least one formerly noisy cycle is explained as benign or meaningful

## Phase 5: Decide What To Automate

Work:

- Identify edge types that can be detected deterministically from phrasing.
- Identify edge types requiring SME review.
- Identify edge types that may require NLP or LLM assistance.

Done when:

- the next implementation stage has a clear extraction strategy
- false-positive risk is documented
- the role of human review is explicit

## Current Priority

Start with hand labeling. Do not automate before the labels teach us what distinctions are real.
