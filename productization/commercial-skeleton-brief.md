# Commercial Skeleton Brief

Status: planning brief
Created: 2026-07-13
Scope: productization direction for portfolio and future commercial validation

---

## Executive Take

Legal Tech Debt should be framed as a source-traceable evidence and review workflow, not as a generic AI compliance chatbot and not as a finished SaaS company.

The portfolio goal is to show that the project can become real software:

- ingest a bounded document set,
- preserve source evidence,
- detect named issue classes,
- show reviewer-friendly reasoning,
- produce an exportable report,
- and sit behind a plausible account, workspace, and invoice model.

The commercial claim must stay modest:

> The prototype suggests a skilled engineer, using modern AI and deterministic evidence tooling, can compress part of the research and source-assembly work that trusted insurance compliance providers perform. It does not prove replacement of counsel, filing vendors, actuarial consultants, or carrier compliance teams.

## Best Current Buyer Frame

The first likely client is not "every insurer." The better first audience is one of:

- insurance regulatory or compliance consulting firms,
- insurance regulatory or coverage law firms,
- filing-support or SERFF-intelligence vendors,
- regulatory intelligence platforms,
- P&C product/forms teams through a trusted provider,
- actuarial or filing advisory firms with existing DOI workflow pain.

These groups already understand forms, filings, objections, state variation, and review cost. They also supply trust that a solo technical vendor does not yet have.

## Weak First Buyer Frame

- Individual brokers are useful validators, but weak buyers.
- Regulators are useful validators, but unlikely customers.
- Direct carrier procurement is too heavy for the current proof level.
- Generic "AI compliance" buyers will invite comparison against broader incumbents before this project has narrow proof.

## Existing Evidence In This Repo

- [../sandboxes/002-claims-regulatory-automation/002-claims-regulatory-automation-README.md](../sandboxes/002-claims-regulatory-automation/002-claims-regulatory-automation-README.md) shows the source-evidence substrate and detector proof of concept.
- [../sandboxes/003-findings-triage/003-STAGE-PLAN.md](../sandboxes/003-findings-triage/003-STAGE-PLAN.md) shows business-facing triage and executive report work.
- [../sandboxes/004-expert-drilldown/README.md](../sandboxes/004-expert-drilldown/README.md) shows expert drill-down report shape and paid-service-style packaging.
- [../sandboxes/006-interactive-drilldown-report/README.md](../sandboxes/006-interactive-drilldown-report/README.md) explores the interactive workbench shape.
- [../feasibility-studies/README.md](../feasibility-studies/README.md) preserves the market counterweight and client-pivot research.
- [../journal/2026-06-11-demo-dataset-strategy.md](../journal/2026-06-11-demo-dataset-strategy.md) records the synthetic dirty-laundry strategy for portfolio-safe demos.

## Production-Aligned Demo Shape

The demo should feel like a system that could be switched from synthetic data to a real account after proper validation:

1. A user signs in or enters a demo workspace.
2. A synthetic carrier/file set is selected or uploaded.
3. The pipeline creates a run with stable IDs, timestamps, source metadata, and parser notes.
4. Findings appear in a reviewer workbench with evidence snippets, graph context, severity, uncertainty, and reviewer questions.
5. A human reviewer marks each finding as accepted, rejected, needs more evidence, or out of scope.
6. The system exports a sanitized report.
7. A test/manual invoice record can be associated with the workspace or report package.

This can begin as a local demo or static workbench, but the data model should not ignore eventual users, workspaces, billing events, and audit trails.

## What Must Not Be Overclaimed

- Do not claim the tool replaces counsel or established compliance providers.
- Do not claim USD 60,000 to USD 90,000 per year is proven revenue.
- Do not claim two Kentucky carriers and five issue classes prove a market.
- Do not claim a generic LLM cannot reproduce any value.
- Do not claim the findings are legal advice.
- Do not claim production readiness until auth, tenancy, secrets, logging, security review, data retention, error handling, and billing boundaries exist.

## Grounded Money Argument

USD 60,000 to USD 90,000 per year is a personal gross-income aspiration, not a per-client price or forecast. It may be worth testing through provider employment, contract work, retainers, or a small number of engagements if the workflow measurably helps qualified experts. The repository does not yet show that it does, what buyers would pay, or how business revenue would translate into personal income after costs.

The grounded version:

- [x] The current prototype shows enough depth to support serious validation conversations.
- [x] The arithmetic does not require thousands of retail customers; employment, one provider contract, or a handful of engagements are possible models to test.
- [x] Dated market research identifies existing filing, compliance, legal, actuarial, and regulatory providers, but their services and prices do not establish demand for this project.
- [ ] No provider has yet committed budget.
- [ ] No repeatable pricing unit has been validated.
- [ ] Delivery time, operating costs, gross margin, and owner compensation have not been measured.
- [ ] No evidence yet shows whether this is software, a report service, subcontracted research, or internal tooling for a provider.

Possible service/software units to validate:

- Per sanitized review package.
- Per provider pilot.
- Per state/product-line evidence buildout.
- Per internal provider seat/workspace after a successful pilot.
- Retainer-style support for recurring filing or policy refresh cycles.

## Next Validation Checklist

- [ ] Put one sanitized or synthetic finding in front of a trusted insurance-domain contact and ask whether the workflow problem is real.
- [ ] Ask a provider-side person who would own this: compliance, filing, product/forms, legal, claims, or another role.
- [ ] Compare the exact issue class against incumbent tools, not against broad "insurance compliance" categories.
- [ ] Ask whether a skilled professional with Claude, ChatGPT, or Perplexity can reproduce the useful part.
- [ ] Identify what remains valuable after generic LLM substitution: source acquisition, graph relationships, stable citations, detector repeatability, reviewer workflow, audit trail, or report packaging.
- [ ] Decide whether the next build is a synthetic public demo, a private validation packet, or a narrower stop/go report.
