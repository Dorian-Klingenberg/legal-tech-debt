# 2026-06-04: Sandbox 003 Planning, Smell 5 Resolution, Stage 005 Architectural Finding

> Historical snapshot boundary: the 35-finding result below predates the regulatory-layer source filter. The current Stage 006 artifact contains 31 findings after four Smell 3 false positives were removed; Sandbox 003 intentionally preserves its original input snapshot.

## Session Summary

Two major threads completed in this session: (1) Sandbox 003 stage plan was sharpened using external business-prospect feedback, and (2) the long-standing Smell 5 zero-findings problem was diagnosed and resolved through a combination of semantic retrieval investigation and a redesigned graph-based gap detector.

---

## What Changed

### Sandbox 003 Stage Plan

- Reviewed `business_owner_prospects_report.md` and `KNIC_real_world_examples_and_costs_report.md` (external Perplexity/LLM feedback on the Stage 007 reviewer report).
- Stage 001 (LLM triage) upgraded: now requires **business severity signal** (claim frequency, litigation sensitivity, regulatory exposure) and **remediation direction** (concrete fix suggestion) in addition to plain-English explanation and false positive assessment.
- Stage 001 LLM approach clarified: **hybrid model design** — smaller/faster model for mechanical annotation fields; larger model for high-judgment fields (business severity, remediation direction). Prompt constraint quality is the gate, not model selection.
- Stage 002 (cross-carrier analysis) now explicitly labels patterns as **industry-wide** vs. **carrier-specific**.
- Stage 003 (executive report) reframed around **decisions and actions** with dollar anchors; reference prototypes identified.
- External feedback prerequisite checked off. Workflow integration added to "Does Not Do."

### Cross-Agent Policy Update

- All four agent config files (`BOOTSTRAP.md`, `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) updated with rule: plan/spec changes must be captured in end-of-session journal; ADRs reserved for architectural decisions only.
- `SESSION-NOTES.md` created at repo root as running scratch-pad for journal items.
- `BACKLOG.md` created at repo root with five seeded items (BACKLOG-001 through BACKLOG-005).

### Smell 5 Detector: Zero Findings Diagnosed and Resolved

**Diagnosis:** H001/H002/H003 regex patterns produce zero raw matches across all 353 nodes. Carrier policy forms do not use "as required by state law" language. The smell is real but not expressed in language the heuristics can match.

**Stage 005 reopened:** All three re-open conditions met:
- Second carrier corpus (KFBM) present since 2026-06-03
- Five Smell 5 paraphrase gold set items approved and added to `goldset-002.2.json` (eval-022 through eval-026)
- Documented BM25 failure: lexical cannot surface regulatory-mapping smell in carrier policy language

**Semantic retrieval evaluation (run `18b0dec5`, 26-item gold set):**
- Overall: 14/26 hits (54% recall) → Decision: PURSUE
- Smell 5 paraphrase items: 0/5 hits with both `text-embedding-3-small` and `text-embedding-3-large`
- Model diagnostic confirmed: the miss is **architectural**, not model capability. Both models correctly retrieve regulatory source nodes (KAR/KRS) but cannot retrieve carrier nodes based on what they *lack*. Vector similarity cannot detect absence.

**ADR-010 written:** Smell 5 requires graph-based gap detection, not vector similarity. See `adr/ADR-010-smell5-retrieval-architecture-gap-detection.md`.

**Smell 5 detector redesigned:** Two-tier approach:
- H001-H003: lexical (retained for corpora where that language appears)
- H004: carrier rate-setting claim with no regulatory edge (MEDIUM)
- H005: carrier mandatory-coverage/endorsement claim with no regulatory edge (MEDIUM)
- H006: carrier loss-settlement methodology with no regulatory edge (LOW)
- H004-H006 emit **one consolidated finding per source** with `supporting_nodes` list preserving all triggering nodes — avoids 29-finding noise from repetitive rate manual sections.

**Finding model updated:** `supporting_nodes: list[dict]` added as optional field to `Finding` and `make_finding()`.

**Stage 006 rerun results:**

| Smell | Findings | H | M | L |
|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 1 |
| 2 | 17 | 0 | 17 | 0 |
| 3 | 4 | 0 | 0 | 4 |
| 4 | 1 | 1 | 0 | 0 |
| 5 | 12 | 0 | 7 | 5 |
| **Total** | **35** | **1** | **24** | **10** |

**Stage 007 reviewer report regenerated:** 35 findings, 121 candidate evidence items.

### Other Backlog Items

- **BACKLOG-003 (Kentucky Growers SERFF):** Searched 2026-06-03 — no entry found. Recheck blocked by SFA downtime 2026-06-04. `KNOWN-GAPS.md` updated to reflect actual search result.
- **BACKLOG-005 added:** Project graduation and Agile V framework integration — revisit after Sandbox 003 Stage 003.

---

## Decisions Made

- Sandbox 003 Stage 001 uses a hybrid LLM model design (smaller for mechanical, larger for high-judgment fields). Prompt constraint quality is the design gate, not model selection.
- Smell 5 is a gap smell, not a similarity smell. Vector retrieval is the wrong tool for absence detection. Graph-based gap detection using the existing Stage 002 edge substrate is the correct architecture.
- H004-H006 deduplicate to one finding per source (not per node) with supporting_nodes for reviewer drill-down.
- Vector store selection (ADR-005) remains deferred. The Stage 005 finding is that vector retrieval earns a role in cross-carrier paraphrase matching (a future use case), not in gap detection.
- Journal entries and handoffs are end-of-session artifacts. ADRs are for architectural decisions only. Plan/spec changes go in the journal.

---

## Validation Performed

- `python -m compileall src` not run this session; individual scripts executed successfully.
- Stage 006 detector runner completed without error: 35 findings, all five smells represented.
- Stage 007 report builder completed without error: 35 findings, 121 candidate evidence items.
- goldset-002.2.json validated as valid JSON with 26 items before semantic evaluator run.
- Semantic evaluator completed: 14/26 hits, both models tested on Smell 5 paraphrase items.

---

## Current State

- Sandbox 002 evidence substrate: fully calibrated. 35 findings across five smells, both KNIC and KFBM represented.
- Sandbox 003 stage plan: ready to implement. All prerequisites checked off except prompt design review (human gate before Stage 001 runs at scale).
- Stage 005: complete with architectural finding. ADR-010 records the conclusion.
- BACKLOG.md: active, 3 open items (BACKLOG-002 file extension mismatches, BACKLOG-003 Kentucky Growers recheck, BACKLOG-005 project graduation).

## What Comes Next

- [ ] Write the Sandbox 002 updated handoff reflecting today's Smell 5 resolution and new finding counts.
- [ ] Begin Sandbox 003 Stage 001: design hybrid LLM prompt schema, human review of prompt before running at scale.
- [ ] When SERFF site is back up: recheck Kentucky Growers (BACKLOG-003).
- [ ] Low priority: rename KY-KRS-304-12-230 and KY-KRS-304-14 from .html to .pdf (BACKLOG-002).
