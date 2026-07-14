# Production Readiness Checklist

Status: planning checklist
Created: 2026-07-13
Scope: what must exist before Legal Tech Debt can be called production-ready or customer-ready

---

This checklist has two distinct gates. Completing the first supports a production-aligned portfolio demo or tightly controlled pilot. Only the second supports a live production claim. A local-demo waiver or test invoice is not production readiness.

## Product Boundary

- [x] Current repo purpose is proof-of-concept research and portfolio development.
- [x] Current outputs are evidence, findings, reviewer questions, and reports.
- [x] Current output boundary is decision support, not legal advice.
- [ ] Define the first paid product unit: report package, pilot, workspace subscription, internal provider tool, or research retainer.
- [ ] Define target user roles and permissions: founder/admin, provider reviewer, client viewer, auditor.
- [ ] Define what the system refuses to do without human review.

## Demo And Data Boundary

- [x] Recognize that real carrier/policy defects cannot be used as public dirty laundry.
- [x] Preserve the synthetic dataset strategy in [../journal/2026-06-11-demo-dataset-strategy.md](../journal/2026-06-11-demo-dataset-strategy.md).
- [ ] Create a fictional carrier or provider demo corpus.
- [ ] Seed the corpus with real defect patterns while removing identifying fingerprints.
- [ ] Document what is synthetic, what pattern source is real, and what has been transformed.
- [ ] Confirm public demo assets contain no proprietary carrier, ISO, SERFF, or private-client material.

## Application Shape

- [x] Static HTML workbench exploration exists in Sandbox 006.
- [ ] Decide first production-aligned surface: static generated workbench, local app, or hosted app.
- [ ] Define a workspace model before storing user data.
- [ ] Define a run model with stable run IDs, schema versions, source IDs, created_at, parser strategy, and source provenance.
- [ ] Define reviewer state: accepted, rejected, needs evidence, out of scope, escalated.
- [ ] Define export formats: HTML, Markdown, PDF, JSON, or CSV.

## Auth, Access, And Tenant Boundary

- [ ] Choose auth strategy for any hosted demo or customer environment.
- [ ] Define password, session, token, and account recovery boundaries.
- [ ] Define tenant/workspace isolation rules.
- [ ] Define role-based access controls.
- [ ] Define audit events for login, upload, run creation, review decisions, export, invoice, and deletion.

## Billing And Invoice Path

- [ ] Decide whether billing is manual, Stripe-style checkout, invoice-only, or provider contract.
- [ ] Define billable objects: workspace, report, run, pilot, month, or package.
- [ ] Define test-mode invoice generation for demo use.
- [ ] Keep real payment credentials and live billing out of the repo.
- [ ] Document cancellation, refund, and data-retention behavior before live billing.

## AI And Model Boundary

- [x] Current defensibility is not "LLM magic"; it is evidence structure, detectors, citations, and review workflow.
- [ ] Record which steps are deterministic and which use AI.
- [ ] Preserve prompts, model versions, run metadata, and reviewer overrides when AI is used.
- [ ] Define failure behavior for missing sources, parser uncertainty, hallucinated claims, and conflicting evidence.
- [ ] Add evaluation cases that test generic LLM substitution risk.

## Evidence, Audit, And Observability

- [x] Existing pipeline emphasizes source provenance and stable IDs.
- [ ] Define immutable run records for production-like demos.
- [ ] Define audit log schema.
- [ ] Define error and warning surfaces for parser gaps, source gaps, and detector uncertainty.
- [ ] Define metrics: ingestion success, finding counts, false-positive notes, reviewer disposition, export success.
- [ ] Define retention and deletion policy for uploaded sources and generated reports.

## Security, Legal, And Safety

- [ ] Perform threat modeling before accepting real customer uploads.
- [ ] Define secret management for hosted deployment.
- [ ] Define data classification: public, synthetic, licensed, confidential, privileged, customer-provided.
- [ ] Define copyright and license handling for policy forms, ISO-derived material, SERFF filings, and vendor content.
- [ ] Add visible disclaimers that reports are not legal advice and require qualified review.
- [ ] Decide whether professional liability, contracts, or counsel review are required before paid work.

## Quality Gates

- [ ] Create a small regression corpus for each supported smell.
- [ ] Add golden report snapshots for public demo outputs.
- [ ] Add tests for empty corpus, malformed source, duplicate source, missing metadata, and partial parser failure.
- [ ] Track false positives and false negatives by smell class.
- [ ] Require human review before any exported report is marked client-ready.

## Portfolio Demo Or Controlled Pilot Gates

Do not call the project a production-aligned demo or controlled pilot until these are complete:

- [ ] Synthetic public demo can run end to end from clean checkout.
- [ ] All demo data is safe to publish.
- [ ] A reviewer can inspect evidence, disposition findings, and export a report.
- [ ] Auth and workspace boundaries are implemented or explicitly waived for local-only demo.
- [ ] A test-mode or manual invoice path demonstrates the intended workflow without putting live payment credentials in the repo.
- [ ] Logs and audit events explain what happened without exposing secrets or confidential text.
- [ ] Error states are visible and do not silently produce confident reports.
- [ ] Documentation clearly separates proof-of-concept, portfolio demo, pilot, and production.

## Live Production Cutover Gates

Do not call the project production-ready or accept ordinary live customer use until these are also complete:

- [ ] A qualified buyer and the first paid product unit have been validated.
- [ ] The deployment and customer-data boundary has been explicitly chosen and documented.
- [ ] Authentication, account recovery, role permissions, and tenant isolation are implemented and tested for every hosted customer path.
- [ ] The real invoice or payment path is configured outside the repo with least-privilege credentials, test coverage, reconciliation, and failure handling.
- [ ] Security, privacy, copyright/license, data-retention, contract, and professional-liability reviews are complete for the intended use.
- [ ] Monitoring, backup/restore, incident response, audit retention, support ownership, and deletion/export procedures are operational.
- [ ] A production rehearsal verifies deployment, rollback, billing, access revocation, failure recovery, and customer offboarding.
