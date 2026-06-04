# Sandbox 003: Findings Triage And Intelligence

Status: **Active — Stage 003 complete; pending next lane decision**
Scope: Take structured findings from Sandbox 002 and make them business-actionable
Created: 2026-06-03
Depends on: Sandbox 002 repaired run `output/002/20260604_130606_18b0dec5/`, Stage 006 findings JSONL, and Stage 007 reviewer report

---

## The Problem This Sandbox Solves

Sandbox 002 produces structured `Finding` records — each one has a node, evidence text, confidence level, rationale, and a reviewer question. That output is technically correct but not yet useful to a non-technical audience. A claims officer, coverage counsel, or CEO cannot directly act on a JSONL file.

This sandbox turns findings into decisions.

---

## Guiding Question

> Can we take the structured findings from Sandbox 002 and produce output that a claims professional or executive can act on without understanding the pipeline that generated it?

---

## Stages

### Stage 001: LLM-Assisted Finding Triage ✓ Complete

**Question:** Can an LLM reliably explain each finding in plain English, assess its false positive risk, assign business severity, suggest a remediation direction, and propose a concrete next step — without inventing legal conclusions?

**Checklist:**
- [x] Hybrid model design decided: gpt-4o-mini (Tier 1 mechanical) + gpt-4o (Tier 2 judgment)
- [x] Dispute scenario audience confirmed: claims professional
- [x] `triage_verdict` field added — synthesizes detector confidence and business severity into one-sentence action signal
- [x] `response_format={"type": "json_object"}` enforced — eliminates markdown code-fence parse failures
- [x] 5-finding sample run and reviewed — output quality validated
- [x] Full 35-finding run complete: 35/35 enriched, 0 errors — `stages/001-llm-triage/output/enriched_findings.jsonl`
- [x] Human review of all 35 findings complete — confirmed finding set documented in `stages/001-llm-triage/validation/human-review-notes.md`

**Key outputs:**
- `stages/001-llm-triage/output/enriched_findings.jsonl` — 35 enriched findings
- `stages/001-llm-triage/validation/human-review-notes.md` — confirmed/rejected/downgraded findings with reasoning
- `stages/001-llm-triage/output/run_manifest.json` — run metadata

**Key findings from human review:**
- ~20 of 35 confirmed; false positives concentrated in Smell 3 (all 4 — wrong source layer), thin H006 entries, and one Smell 1 notice provision
- Statutory/regulatory corpus is reference layer only — detectors must not fire on KRS/KAR/DOI nodes (BACKLOG-010)
- Most false positives trace to a shared root: detectors running on wrong node types — section headers, statutory text, filing instructions. Node-level context annotation (BACKLOG-006) would resolve this systematically
- Seven new backlog items (BACKLOG-006 through BACKLOG-012) identified, all grounded in real corpus examples

**Key constraint:** LLM output is annotation only — never overwrites the original finding. Original provenance and evidence text stay intact.

---

### Stage 002: Cross-Carrier Pattern Analysis ✓ Complete

**Question:** Do the same smells appear in both KNIC and KFBM policy language? Where do they diverge?

**Checklist:**
- [x] Stage 001 enriched findings available as input
- [x] Confirmed finding set from human review available (`human-review-notes.md`)
- [x] Human review verdicts encoded as `stages/002-cross-carrier/data/review_verdicts.json` — canonical record for downstream stages
- [x] Group confirmed findings by smell and heuristic across carriers
- [x] Label each pattern as **industry-wide** (both KNIC and KFBM) or **carrier-specific** (one carrier only)
- [x] Flag cross-carrier term matches (ACV and replacement cost in both carriers)
- [x] Produce carrier comparison table per smell
- [x] Human review of cross-carrier output — approved

**Key findings:**
- 25 of 35 confirmed after human review (10 excluded: 7 false positives, 2 duplicates, 1 downgraded to LOW)
- **Smell 2 H003 (ACV / Replacement Cost)** — industry-wide: 5 KNIC + 5 KFBM findings. Strongest signal in confirmed set.
- **Smell 2 H001 ("reasonable time")** — KFBM-specific: 6 findings. KNIC does not use this drafting pattern.
- **Smell 5 H004 (rate nodes, no regulatory edge)** — industry-wide: KFBM carries heavier unanchored rate methodology (4 findings vs 1 KNIC)
- **Smell 5 H005 (mandatory coverage claims)** — industry-wide: 1 KNIC + 1 KFBM
- **Smell 4 H001 (unversioned manual reference)** — KNIC-specific: 1 clean finding

**Output:** `stages/002-cross-carrier/output/carrier_comparison.json` + `carrier_comparison.md`

---

### Stage 003: Executive Summary Report ✓ Complete

**Question:** Can we produce a one-page summary that a CEO or Chief Claims Officer can read in five minutes and understand what risk the findings represent?

**Checklist:**
- [x] Stage 001 and Stage 002 outputs available
- [x] Draft report structure reviewed against reference prototypes
- [x] Report written — framed around decisions and actions, not a findings list
- [x] Dollar anchors included — `dollar_anchors.json` extracted from `002-ROI-CASES-FIVE-SMELLS.md`; wired into narrative prompts and Risk Context section
- [x] Industry-wide vs. carrier-specific distinction surfaced prominently
- [x] Findings table collapsed to 6 pattern-level rows (one per heuristic) — appropriate for CEO audience
- [x] H004 narrative prompt corrected — now describes "rate-setting filings with no traceable citation to KRS/KAR/DOI authority"
- [x] Markdown rendering fix — dollar signs removed from bold labels; format is `**Label** — description with figures in plain text`
- [x] Human review of report output — approved
- [x] Output: `stages/003-executive-report/output/executive_summary.md`

**Key outputs:**
- `stages/003-executive-report/output/executive_summary.md` — 125-line prospect-facing report
- `stages/003-executive-report/data/dollar_anchors.json` — named cost anchors mapped per smell
- `stages/003-executive-report/src/report_builder.py` — gpt-4o driven; deterministic Risk Context + findings table sections

**Known gaps before prospect use (see BACKLOG):**
- BACKLOG-013: Carrier name anonymization (`--anonymize` flag not yet built)
- BACKLOG-014: Human editorial pass on LLM-generated prose required before external distribution

**Tone:** Written for a CEO or Chief Claims Officer who will hand it to a team, not read it themselves.

**Reference prototypes:** `sandboxes/002-claims-regulatory-automation/business_owner_prospects_report.md` and `KNIC_real_world_examples_and_costs_report.md`

**Output target:** Something you'd put in front of a potential client to demonstrate value before a sales conversation.

---

## What This Sandbox Does NOT Do

- Does not make legal conclusions — findings are patterns for human judgment
- Does not build a production API or deployment infrastructure
- Does not automate regulatory filings
- Does not expand the corpus (that stays in Sandbox 002)
- Does not design workflow integration (dashboards, issue tracking, sign-off flows, document management hooks) — that is a product-design question for a later lane
- Does not design UI or data views — different display formats (e.g., confidence vs. severity as separate axes, verdict-first layouts) will help communicate the distinction between detector confidence and business severity; that is a future lane after Stage 003 produces the report

---

## Prerequisites Before Starting ✓ All Complete

- [x] Sandbox 002 artifact contract repaired and revalidated on run `18b0dec5`
- [x] Gold set re-evaluated on repaired expanded run — BM25 remains 21/21
- [x] Sandbox 002 closure decision recorded in ADR-009
- [x] Smell 5 calibrated — graph-based gap detector (H004-H006) produces 12 findings (7 MEDIUM, 5 LOW) across KNIC and KFBM. ADR-010 records the architectural decision.
- [x] External business-prospect feedback reviewed and incorporated into Stage 003 design
- [x] Hybrid LLM model design decided and built — gpt-4o-mini (Tier 1) + gpt-4o (Tier 2)
- [x] Human review of Stage 001 output complete — confirmed finding set documented
