# Journal: Sandbox 003 — Post-Completion Hardening and Product Strategy

Date: 2026-06-04
Session: Fourth session of the day (post-completion hardening)
Author: Dorian Klingenberg + Claude Code (claude-sonnet-4-6)

---

## Session Summary

Sandbox 003 pipeline was complete entering this session. Work focused on three queued backlog items (BACKLOG-010, -013, -014), two emergent bug fixes (dollar-sign rendering), and two new backlog items surfaced during review (BACKLOG-015, -016, -017). The most significant output was a strategic clarification: the drill-down expert report (BACKLOG-017) is not a supporting artifact — it is the product being sold.

---

## What We Did

### BACKLOG-010: Source ID Prefix Guard in Stage 006 Detectors

**File changed:** `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detector_runner.py`

Added `_REGULATORY_PREFIXES = ("KY-KRS-", "KY-KAR-", "KY-DOI-")` constant and `_is_carrier_node()` predicate. In `run_detectors()`, nodes are filtered through the predicate before being passed to any detector. The runner logs the pre-filter count, skip count, and post-filter count at each run.

**Why the runner, not individual detectors:** A single guard in the runner covers all five detectors now and any future ones without repetition. Each detector was previously responsible for its own filtering; this was fragile and incomplete.

**Impact:** Eliminates all four Smell 3 false positives (s3-0019 through s3-0022) — all were on KRS/KAR statutory nodes using standard legislative drafting ("except as otherwise provided"). Suggesting a carrier amend a Kentucky statute was never actionable.

**Not done:** Long-term fix — populating `source_type` correctly in Stage 002 ingestion so the guard is semantic rather than ID-prefix-based — remains open (part of BACKLOG-006 scope).

**Smoke-tested:** Import check + predicate unit assertions ran clean. Full pipeline re-run not performed — existing run `20260604_130606_18b0dec5` preserved.

---

### BACKLOG-013: Carrier Name Anonymization Flag in report_builder.py

**File changed:** `sandboxes/003-findings-triage/stages/003-executive-report/src/report_builder.py`

Added:
- `CARRIER_LABELS_INTERNAL = {"KNIC": "KNIC", "KFBM": "KFBM"}` — identity map, default
- `CARRIER_LABELS_ANON = {"KNIC": "Carrier A", "KFBM": "Carrier B"}` — external mode
- `--anonymize` CLI flag — selects the anon map and writes to `executive_summary_anon.md`
- `OUTPUT_MD_ANON` path constant

Labels threaded through three functions: `apply_verdicts()`, `build_findings_table()`, `build_report()`. The carrier-specific patterns section and the findings table both use the label map for all carrier name output. LLM narrative sections already said "the carriers analyzed" — no change needed there.

**Design decision:** Build-time flag (not post-processing). Two output files coexist — `executive_summary.md` (internal, real names) and `executive_summary_anon.md` (external, generic labels). Both are always producible from the same input data.

**Usage:**
```bash
python report_builder.py            # internal — KNIC, KFBM visible
python report_builder.py --anonymize  # external — Carrier A, Carrier B
```

**Smoke-tested:** Import check, label map verification, and `apply_verdicts()` substitution test ran clean.

---

### BACKLOG-014: Editorial Pass on Executive Summary LLM Prose

**File changed:** `sandboxes/003-findings-triage/stages/003-executive-report/output/executive_summary.md`

12 targeted replacements applied directly to the output file (not via prompt re-run). Prompt re-run was explicitly rejected — it would be non-deterministic, cost money, and risk corrupting the stable dollar-anchor content that took calibration to produce.

**What was replaced:**

| Location | Problem | Fix |
|---|---|---|
| Executive intro ¶1 | "Rapidly evolving landscape / crucial for strategic leadership" boilerplate | Direct statement of what the briefing is and what we found |
| Executive intro ¶2 | Four-sentence meander with "could potentially lead to" hedging | Two sentences stating the convergence finding plainly |
| Executive intro ¶3 | "Challenge and opportunity / strategic foresight fortifies the carrier's market position" | One concrete sentence on why acting early matters |
| SMELL2-H003 ¶1 | "In the insurance industry, clarity is crucial" filler opener | Leads directly with the specific gap: no cited methodology in either carrier |
| SMELL2-H003 ¶2 | Filler opener + dangling relative clause | Trimmed opener; fixed dangling clause in labor depreciation class-action sentence |
| SMELL5-H004 ¶1 | "The SMELL5-H004 pattern refers to a notable absence" technical identifier | Leads with what both carriers do (or don't do) |
| SMELL5-H004 ¶2 | Typo "undocumentated"; "reflecting broader challenges seen in other states" generic closer | Fixed typo; replaced generic closer with one concrete sentence |
| SMELL5-H005 ¶1 | "The SMELL5-H005 pattern identifies policy provisions" technical opener | Leads with what both carriers assert |
| SMELL5-H005 ¶2 | "Without precise citations, carriers face reputational damage" vague closer | Replaced with the specific South Dakota dollar figure |
| Closing ¶1 | Full LLM boilerplate — "enhance clarity and predictability... operational excellence" | Specific actionable steps: valuation definitions, tool citations, KRS anchors |
| Closing ¶2 | "Cannot be understated / showcasing a proactive stance / evolving regulatory landscapes" | Direct statement of why structured review finds conventional-looking gaps |

**Human review still required** before any external distribution — this was a mechanical pass, not a final editorial judgment.

---

### Dollar-Sign Rendering Bug (Two Instances)

**Files changed:**
- `sandboxes/003-findings-triage/stages/003-executive-report/output/executive_summary.md`
- `sandboxes/003-findings-triage/stages/003-executive-report/data/dollar_anchors.json`

**Root cause:** Markdown renderers that support LaTeX math treat paired `$...$` as math delimiters. Any two `$` signs in close proximity — even in prose or blockquotes — can trigger this. Two separate instances were found:

1. **Blockquote ROI pitch:** `$1M ... $100K ... $60K–$90K` — three dollar signs in one sentence, causing the text between the first and second to render as math expression
2. **Portfolio framing bullet ranges:** `$20M–$200M`, `$5M–$25M`, `$10M–$100M` — paired dollar signs in every range value

**Fix applied:** Removed dollar signs from the affected strings. Blockquote reworded to "1M-dollar" / "100K" / "60K–90K". Ranges reformatted as "20M–200M USD" etc. Fix applied to both the rendered output file and the source `dollar_anchors.json` so future report builds generate clean output.

**Defensive fix pending:** BACKLOG-016 — add a `_safe_dollar()` sanitizer in `report_builder.py` to prevent re-introduction through future data edits.

---

### New Backlog Items Logged

| ID | Priority | Description |
|---|---|---|
| BACKLOG-015 | HIGH (sales) | Heuristic-specific case and bad-faith closure library — one public case per heuristic (H001, H003, H004, H005, H006) matched to the exact language gap, not the broad smell category. Output slots into `dollar_anchors.json` and the Risk Context section. |
| BACKLOG-016 | LOW (defensive) | Dollar-sign rendering guard in `report_builder.py` — `_safe_dollar()` helper to sanitize bare `$` signs before they enter markdown output strings. |
| BACKLOG-017 | CRITICAL (product) | Expert drill-down report — finding-level technical brief with verbatim evidence, regulatory grounding, and suggested fixes. See strategic framing below. |

---

## Strategic Clarification: Product Model

The most significant output of this session is a product model decision, not a code change.

**Executive summary = sales instrument.** Gets a CEO or CCO to the table. Pattern-level, no filing detail, no suggested fixes. Generated once per carrier cohort and reused as a prospect hook.

**Drill-down expert report = the paid service.** Carrier-specific, finding-specific, actionable. The deliverable a carrier pays for. Structured to serve three distinct reader roles in one document:

- **Compliance officer / coverage attorney** — regulatory grounding, exact filing citations, defensible suggested language
- **Claims professional** — claim dispute exposure per finding, bad-faith risk framing, how current language lets a claimant challenge a settlement
- **Policy designer / filing specialist** — proposed redlines or remediation templates; whether a DOI refiling is required

Each finding entry in the drill-down report will contain: verbatim evidence text, section path, gap statement, applicable KRS/KAR/DOI citation, suggested fix (redline or template depending on smell type), and a disclaimer that fixes are editorial suggestions, not legal advice.

**BACKLOG-015 and BACKLOG-017 are linked:** the heuristic-specific case library (BACKLOG-015) provides the claims exposure evidence that populates the claims professional section of the drill-down report (BACKLOG-017). Both should be scoped into the same sandbox.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Guard in runner, not in each detector | One authoritative filter; trivially extended for new prefixes; no per-detector repetition |
| Anonymization as build-time flag | Two output files coexist; both always producible; no post-processing step required |
| Editorial pass as direct file edit | Non-deterministic LLM re-run would cost money and risk corrupting stable dollar-anchor content |
| Dollar-sign fix in source data, not just output | Prevents re-introduction on next `python report_builder.py` run |
| Drill-down report classified as CRITICAL | It is the product being sold, not a supporting artifact — priority must reflect that |
| Suggested fix strategy: redline vs. template by smell type | Smell 4/5 → redline (mechanical add of citation/version); Smell 2 → template (methodology is carrier-specific) |

No ADRs warranted this session. All decisions were implementation choices within established architecture, not decisions between named alternatives with long-term architectural consequences.

---

## Validation Performed

- BACKLOG-010: smoke-tested via Python import + predicate unit assertions
- BACKLOG-013: smoke-tested via label map verification and `apply_verdicts()` substitution test
- BACKLOG-014: full report re-read after edits; all 12 replacements visually confirmed clean
- Dollar-sign fix: final scan for remaining bare `$` pairs confirmed clean (single `$` in prose sentences confirmed safe)

---

## Current State

Six files changed this session:

| File | Change |
|---|---|
| `stages/006-deterministic-detectors/src/detector_runner.py` | BACKLOG-010: regulatory node filter |
| `stages/003-executive-report/src/report_builder.py` | BACKLOG-013: `--anonymize` flag |
| `stages/003-executive-report/output/executive_summary.md` | BACKLOG-014: editorial pass + dollar-sign fix |
| `stages/003-executive-report/data/dollar_anchors.json` | Dollar-sign fix in source data |
| `BACKLOG.md` | BACKLOG-010/013/014 resolved; BACKLOG-015/016/017 added |
| `SESSION-NOTES.md` | Running notes throughout session |

Report is prospect-ready pending one final human read. The anonymized version (`executive_summary_anon.md`) has not yet been generated — requires one `python report_builder.py --anonymize` run.

---

## What Comes Next

1. **Final human read** of `executive_summary.md` before any prospect use
2. **Generate anonymized version:** `python report_builder.py --anonymize`
3. **Sandbox 004 / BACKLOG-017 scoping:** start the expert drill-down report as the primary product lane. Proof-of-concept scope: hand-build one example entry per priority finding type (SMELL2-H003, SMELL4-H001, SMELL5-H004), validate format with human expert read, then decide pipeline architecture.
4. **BACKLOG-015 research:** heuristic-specific case library — research lane that feeds directly into the drill-down report's claims exposure section.
5. **BACKLOG-016** (low priority): dollar-sign sanitizer in `report_builder.py`.
