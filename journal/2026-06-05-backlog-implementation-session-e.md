# Journal: Backlog Implementation Session E

Date: 2026-06-05
Session: Claude Code session 6 continuation (fourth and final closeout)
Scope: BACKLOG-021, BACKLOG-005, BACKLOG-009, BACKLOG-012, BACKLOG-006 — all closed

---

## Summary

Final session segment closing all remaining agent-actionable backlog items. Three items involved substantive work (taxonomy entry, detector fix, ADR); two were administrative closures based on owner decisions made during the session. The backlog is now empty of agent-actionable items. Only owner-lane items remain (BACKLOG-003 SERFF recheck, KY DOI open records call).

---

## What Changed

### BACKLOG-021: KFBM Base Jacket Procurement — Closed

Owner confirmed three conditions that close this item:
1. Pre-2018 forms are out of scope — KFBM's base jacket predates SERFF Filing Access (Nov 2018 cutoff); KY DOI open records was the only remaining path.
2. Trust internal document links — H004 corpus limitation is documented; procurement not needed to note it.
3. ISO trust (applies to KNIC, not KFBM directly, but conditions 1+2 close KFBM regardless).

H004 fires zero on current corpus and will continue to. KY DOI open records call survives as an independent owner-lane action for H004/H006 exam findings only.

### BACKLOG-005: Phase A / Agile V Entry — Closed

Superseded by Sandbox 005 (active experiment). Backlog item retired; track in `sandboxes/005-agentic-sdlc-project-manager/`.

### BACKLOG-009: Non-Deterministic Underwriting Criteria — Taxonomy Entry Added

Checked both taxonomy files:
- `legal_code_smell_taxonomy.md` Category 2 had "Non-deterministic Language" (general policy language)
- `insurance_policy_smells.md` Section 2 had "Magic Rating Factor" (actuarial factors without basis)
- Neither covered underwriting *eligibility* criteria specifically

New entry **"Non-Deterministic Underwriting Criteria"** added to both files. Definition: eligibility rule uses vague, unmeasurable language ("stable or improving area," "favorable impact on market value") with no objective measurement standard — accept/decline decisions become non-reproducible across underwriters. Exposes carriers to underwriting inconsistency, adverse selection, discriminatory rating scrutiny, and bad-faith exposure when a declination is challenged.

Source of candidate smell: KNIC rate manual entry flagged as false positive in BACKLOG-009 ("Located in stable or improving area with favorable impact on market value" — underwriting eligibility, not a claims provision).

No detector built. Taxonomy entry added for future review.

### BACKLOG-012: H005 "Is Not Mandatory" Pattern Removal — Fixed

`_H005_PATTERN` in `smell5.py` had an `"is not mandatory"` branch that fired on filing instructions explicitly saying a coverage is *not* required (e.g., "Section II Coverage is not mandatory for the secondary residence policy"). This is a negation context — a filing instruction about optional coverage, not a regulatory mandate claim. A mandatory-coverage smell should only fire when language asserts something IS required.

**Fix applied:**
- Removed `r"is\s+not\s+mandatory"` from `_H005_PATTERN`. No real findings are lost — all regulatory mandate claims use positive-form language.
- Strengthened `_H005_FP` to explicitly name the filing-instruction context and flag the three remaining high-FP terms: "special state requirements," "use this endorsement with all," and "must be endorsed."

Syntax check: OK.

### BACKLOG-006: Language Context Annotation — ADR-013 Written

`ADR-013-language-context-annotation.md` written at `sandboxes/002-claims-regulatory-automation/adr/`. Records the design decision for a `language_context` field on carrier nodes.

**Field schema:** `language_context` with six-value enum:
- `coverage_grant` — affirmatively extends coverage
- `exclusion` — removes or limits coverage
- `condition` — duty, obligation, or procedural rule
- `filing_instruction` — rate manual/underwriting guideline, not a policy provision
- `definition` — defines a term used elsewhere
- `ambiguous` — cannot be classified reliably from text alone

**Annotation approach:** Lightweight LLM pass post-ingestion. Validate on 20–30 hand-labeled nodes (≥85% agreement on `coverage_grant`, `exclusion`, `filing_instruction` before gating detectors).

**How detectors use it once implemented:**
- H005: skip `filing_instruction` nodes
- Smell 1: differentiate reviewer questions by context
- All detectors: skip `definition` nodes

Implementation deferred. Current state (BACKLOG-012 fix + strengthened FP language) is sufficient for current milestone. ADR-013 means the design won't need to be re-derived when implementation begins.

---

## Decisions Made

### Detector negation patterns fire backwards
"Is not mandatory" matches the opposite of what H005 is looking for. Lesson: before adding a negation-form phrase to a detector pattern, verify the context is always the smell context — not a counter-example. Filing instructions frequently use negation to describe optional coverages.

### FOIA wall is the correct framing for missing regional enforcement actions
KY/TN/OH/WV DOI market conduct exam reports are systematically not publicly indexed. This is documented, not speculated. The right framing for the case library gap sentinels: "enforcement mechanism documented at $750K–$2.5M range; specific regional examples behind FOIA walls." The KY DOI open records call is the only path to close H004/H006 with named examples.

### Source citations are required on all dollar anchors
Two factual errors found and corrected during the source citation pass (State Farm $15.6M was auto, not homeowners; Louisiana was $764,750, not ~$1M). Policy: no figure asserted without a source_url or source_note. When a source is inaccessible, note the barrier and the retrieval path.

---

## Current Backlog State

| Status | Items |
|---|---|
| Agent-actionable open | **None** |
| Owner-lane open | BACKLOG-003 (SERFF recheck); KY DOI open records call (standalone) |
| Closed this session | BACKLOG-005, BACKLOG-006, BACKLOG-009, BACKLOG-012, BACKLOG-021 |
| Closed earlier today | BACKLOG-002, BACKLOG-007, BACKLOG-011, BACKLOG-013, BACKLOG-015, BACKLOG-019, BACKLOG-020, BACKLOG-022, BACKLOG-023 |
| Active sandboxes | 002 (source), 003 (triage), 004 (drill-down), 005 (SDLC stack), 006 (interactive UX) |

---

## Files Changed This Session (E)

| File | Change |
|---|---|
| `insurance_policy_smells.md` | New row: Non-Deterministic Underwriting Criteria (Section 2) |
| `legal_code_smell_taxonomy.md` | New row: Non-Deterministic Underwriting Criteria (Category 2) |
| `sandboxes/002.../detectors/smell5.py` | Removed "is not mandatory" from H005 pattern; strengthened _H005_FP |
| `sandboxes/002.../adr/ADR-013-language-context-annotation.md` | New ADR — language_context field design |
| `BACKLOG.md` | BACKLOG-005, 006, 009, 012, 021 all marked [x] with resolution notes |
| `AGENT_CONTEXT.json` | open_threads updated; latest_handoff → session-e |
