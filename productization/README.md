# Legal Tech Debt Productization Notes

Status: planning layer
Created: 2026-07-13
Purpose: Keep the production-aligned portfolio and commercial-skeleton direction visible without turning the sandbox into premature infrastructure.

---

## Current Read

Legal Tech Debt is still a research and proof-of-concept repository. The useful next shape is not "launch a SaaS tomorrow." The useful next shape is:

> A deployable, evidence-backed portfolio demo that shows how the existing legal tech debt pipeline could become a provider-facing commercial workflow after validation.

This folder defines that production-aligned shape. It does not authorize production services, customer data handling, legal-advice claims, billing integration, or deployment scaffolding by itself.

## Truth Boundary

- [x] The repo has real proof-of-concept evidence across Kentucky homeowners policy-layer smells.
- [x] Sandbox 002/003/004 show ingestion, candidate evidence, detector findings, triage, and expert-style report generation.
- [x] Sandbox 006 explores a static HTML workbench shape.
- [x] Feasibility studies preserve the uncomfortable market reality: incumbents exist, and direct carrier SaaS is not yet proven.
- [ ] The repo does not yet prove repeatable buyer demand.
- [ ] The repo does not yet contain a public synthetic demo corpus suitable for open portfolio use.
- [ ] The repo does not yet contain a production app with auth, tenancy, billing, observability, and cutover controls.
- [ ] The repo does not yet establish that the findings are legal conclusions, or that they should be used without expert review.

## Production-Aligned Target

The target is a portfolio-grade commercial skeleton:

- A synthetic or sanitized demo dataset that protects real entities and proprietary source material.
- A local or deployable demo workbench that can ingest a small document set, show evidence, display findings, support reviewer notes, and export a report.
- Clear account/workspace boundaries so the app can later accept a real username, password, and customer workspace without rethinking the model.
- A manual or test-mode invoice path that shows how a small number of provider relationships could be supported without high-volume sales work.
- Evidence lineage, run metadata, reviewer state, and audit logs treated as first-class product behavior.
- Human review gates and disclaimers that keep the output in decision-support territory, not automated legal advice.

## Commercial Hypothesis

The strongest current hypothesis is provider-facing:

> Existing insurance compliance, legal, filing, regulatory intelligence, or insurtech providers may be able to use Legal Tech Debt as a source-traceable evidence workflow for work they already sell.

That is more grounded than claiming carriers will immediately buy a standalone AI tool. It also fits the founder constraint: avoid thousands of small customers, avoid repetitive report labor, and seek leverage through people who already have trust and distribution.

## Folder Map

- [commercial-skeleton-brief.md](commercial-skeleton-brief.md) - product, buyer, and portfolio framing.
- [production-readiness-checklist.md](production-readiness-checklist.md) - cutover-style checklist for what must exist before the repo can honestly be called production-ready.

## Near-Term Documentation Checklist

- [x] Preserve the production-aligned portfolio direction in a repo-visible folder.
- [x] Connect the direction to the feasibility studies and sandbox evidence.
- [x] Keep production infrastructure out of scope until an explicit future stage exists.
- [ ] Build a synthetic public demo dataset plan that can be implemented without exposing real carrier or proprietary material.
- [ ] Choose the first deployable demo surface: static workbench, lightweight local app, or hosted demo with synthetic data only.
- [ ] Define the minimum auth/workspace/billing model before writing production code.
- [x] Consolidate the four available external feasibility reports and provider-facing synthesis.
- [ ] Revisit market validation after qualified human/provider feedback or materially new external evidence is added.
