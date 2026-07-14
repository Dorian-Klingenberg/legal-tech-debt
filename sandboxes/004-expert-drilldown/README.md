# Sandbox 004 — Expert Drill-Down Report (BACKLOG-017)

**Status:** Proof-of-concept complete  
**Started:** 2026-06-04  
**Completed:** 2026-06-04

---

## Purpose

Build an expert drill-down report proof of concept. It tests three reader panels per finding: compliance/counsel, claims professional, and policy designer. The entries are hand-crafted and grounded in Sandbox 002 detector findings.

This is not the executive summary (Sandbox 003). It explores the deeper work product a qualified reviewer might use. It does not prove that carriers or providers will buy it.

## Entries Built

| Entry ID | Heuristic | Carrier(s) | Finding |
|---|---|---|---|
| S4-H001-KNIC-001 | SMELL4-H001 | KNIC | Unversioned manual reference — Section 602 "refer to the Manual for that state" |
| S5-H004-KFBM-KNIC-001 | SMELL5-H004 | KFBM + KNIC | Rate methodology without regulatory citation — Homeowner Risk Factor / Property Insurance Score |
| S4-H003-KFBM-001 | SMELL2-H003 (reclassified Smell 4, ADR-011) | KFBM + KNIC | Undisclosed ACV calculation methodology — roof surfacing ACV loss settlement, 7-year rule |

## Outputs

- `data/drill_down_entries.json` — hand-crafted entry data (schema version 1.0)
- `generate_drilldown.py` — generator with carrier and sanitization filters
- `output/drilldown.html` — combined internal report
- `output/drilldown_KFBM.html` and `output/drilldown_KNIC.html` — carrier-scoped internal reports
- `output/drilldown_KFBM_sanitized.html` and `output/drilldown_KNIC_sanitized.html` — carrier-scoped paraphrased reports

## Product Principles Established This Sandbox

- **Ground findings in available internal disclosure and state the package boundary.** A missing item in an incomplete corpus is a limitation, not automatically a defect.
- **Use ISO comparison only when its role and source are verified.** ISO HO 04 93 is a roof-surfacing ACV endorsement, not KFBM's base jacket. See the ADR-011 corrective addendum.
- **Treat divergence and package complexity as hypotheses to inspect.** Modified forms, endorsement stacks, and proprietary methodologies may create review value, but carrier targeting requires verified form roles and buyer evidence.
- **Two distinct products.** Phase 1: gaps in your own filed documents. Phase 2 (future): how you diverged from ISO and the risk profile of each change.
- **Four structural gap types** (Jem framework, 2026-06-04): Phantom Form, Broken Definitions Loop, Undisclosed Rating Rules vs. Policy Constraints, Missing State Amendatory. See BACKLOG-019 and BACKLOG-020.

## Source Evidence

All findings sourced from Sandbox 002 run `20260604_130606_18b0dec5`. Detector findings in:
`sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl`

## Current Disposition

- [x] BACKLOG-019 missing-state-amendatory detector implemented.
- [x] BACKLOG-015 case library completed to the public-web limit.
- [x] Carrier filtering and sanitization generation implemented.
- [ ] Treat buyer value, pricing, and paid-deliverable language as validation questions.
- [ ] Use Sandbox 006 for interaction/UX review rather than modifying this completed content proof by default.
