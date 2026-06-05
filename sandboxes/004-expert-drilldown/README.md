# Sandbox 004 — Expert Drill-Down Report (BACKLOG-017)

**Status:** Proof-of-concept complete  
**Started:** 2026-06-04  
**Completed:** 2026-06-04

---

## Purpose

Build the expert drill-down report — the paid product. Three reader panels per finding: compliance/counsel, claims professional, policy designer. Static HTML proof-of-concept with hand-crafted entries grounded in Sandbox 002 detector findings.

This is not the executive summary (Sandbox 003). That is the sales instrument. This is the product a carrier expert reads to understand exactly what the gap is, why it matters to their role, and what to do about it.

## Entries Built

| Entry ID | Heuristic | Carrier(s) | Finding |
|---|---|---|---|
| S4-H001-KNIC-001 | SMELL4-H001 | KNIC | Unversioned manual reference — Section 602 "refer to the Manual for that state" |
| S5-H004-KFBM-KNIC-001 | SMELL5-H004 | KFBM + KNIC | Rate methodology without regulatory citation — Homeowner Risk Factor / Property Insurance Score |
| S4-H003-KFBM-001 | SMELL2-H003 (reclassified Smell 4, ADR-011) | KFBM + KNIC | Undisclosed ACV calculation methodology — roof surfacing ACV loss settlement, 7-year rule |

## Outputs

- `data/drill_down_entries.json` — hand-crafted entry data (schema version 1.0)
- `output/drilldown_report.html` — static three-panel HTML report, three finding cards

## Product Principles Established This Sandbox

- **Ground truth is internal disclosure, not ISO comparison.** Every finding is grounded in what the carrier's own filed documents fail to disclose. No external standard required.
- **ISO as implicit gold standard.** ISO HO 00 03/05 content is established fact; we do not need a copy to make findings. See ADR-011.
- **Target carriers are ISO divergers.** Pure ISO adopters are low-value targets. Legal tech debt lives in proprietary base forms, heavy endorsement stacks, and proprietary rate/underwriting methodologies. See SESSION-NOTES product principle entry.
- **Two distinct products.** Phase 1: gaps in your own filed documents. Phase 2 (future): how you diverged from ISO and the risk profile of each change.
- **Four structural gap types** (Jem framework, 2026-06-04): Phantom Form, Broken Definitions Loop, Undisclosed Rating Rules vs. Policy Constraints, Missing State Amendatory. See BACKLOG-019 and BACKLOG-020.

## Source Evidence

All findings sourced from Sandbox 002 run `20260604_130606_18b0dec5`. Detector findings in:
`sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl`

## Next Steps

- BACKLOG-019: Missing State Amendatory detector (new high-value gap type)
- BACKLOG-015: Heuristic-specific case library (one public case per heuristic)
- Phase 2 product planning: Internal Reference Map visualization (post-Phase A)
