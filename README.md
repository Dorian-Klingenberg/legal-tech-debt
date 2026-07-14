# Legal Tech Debt

Status: Sandbox research, production-aligned portfolio development, and market validation
Current as of: 2026-07-13

Legal Tech Debt explores whether insurance policy, filing, and regulatory documents can be turned into source-traceable evidence, named defect patterns, reviewer findings, and useful expert work products.

The repository is not a production service and its findings are not legal advice. It contains completed proofs of concept, two bounded current experiments with explicit start/review gates, productization planning, and unresolved commercial validation questions.

## Start Here

Use these files in this order when orienting:

1. `BOOTSTRAP.md` - cross-agent startup contract.
2. `README.md` - human-readable current state and pivot history.
3. `AGENT_CONTEXT.json` - compact machine-readable current state.
4. `AGENT_OPERATING_MODEL.md` - truth hierarchy and cross-agent rules.
5. The README, stage plan, and latest handoff for the sandbox being touched.

Historical journals, handoffs, generated reports, external reports, and archived conversations explain how the project arrived here. They do not override the current documents above.

## Current Lanes

| Lane | State | Next gate |
|---|---|---|
| [Sandbox 005](sandboxes/005-agentic-sdlc-project-manager/README.md) | Primary technical lane; Stage 001 complete and Stage 002 ready but not started | Owner explicitly starts `S005-PILOT-001`; isolate the dirty worktree before any agent pilot |
| [Sandbox 006](sandboxes/006-interactive-drilldown-report/README.md) | Secondary UX review lane; static workbench implemented | Human visual/responsive review before design-tool comparison |
| [Productization](productization/README.md) | Planning only | Choose a synthetic public demo and first product unit before production code |
| [Feasibility studies](feasibility-studies/README.md) | Provider-facing commercial hypothesis, not validated demand | Put a sanitized or synthetic example in front of trusted domain and provider-side reviewers |
| [BACKLOG-003](BACKLOG.md) | Owner/access lane | Recheck Kentucky Growers in SERFF when practical; close as unavailable if a second search is also empty |

No production infrastructure, customer data handling, authentication, billing integration, or deployment work is authorized merely because it appears in a planning checklist.

## Completed Evidence

| Scope | Verified state |
|---|---|
| **Complete legal code smell inventory** | 159 documented smells across three taxonomies: `legal_code_smell_taxonomy.md` (74 patterns), `insurance_policy_smells.md` (43 patterns), `insurance_claims_smells.md` (41 patterns) |
| **Operationalized detectors** | Five Kentucky homeowners policy-layer smells (Sandbox 002) with detection specs and Gherkin scenarios |
| Canonical Kentucky corpus inventory | 32 unique files in `corpus/kentucky-homeowners-policy-smells/sources/` |
| Preserved Sandbox 002 ingestion run | 28 ingested sources, 353 nodes, 121 candidate-evidence records, 41 Stage 002 discovery bundles |
| Stage 003 retrieval baseline | 39 retrieval bundles |
| Current Stage 006 detector output | 31 findings: Smell 1 = 1, Smell 2 = 17, Smell 3 = 0, Smell 4 = 1, Smell 5 = 12; confidence HIGH = 1, MEDIUM = 24, LOW = 6 |
| Sandbox 003 historical analysis input | 35-finding June 4 snapshot; later filtering removed four regulatory-layer Smell 3 false positives |
| Sandbox 004 product-content proof | 3 expert entries rendered into 5 combined, carrier, and sanitized HTML variants |
| Case library | 4 public cases/actions plus 6 explicit gap sentinels |

The source inventory, preserved ingestion run, current detector output, and historical downstream snapshot are different scopes. Do not collapse them into one count.

## Pivot Ledger

1. **Broad legal-tech debt to measurable primitives.** Sandbox 001 tested extraction, graph, matrix, and structural-defect ideas in plain Python.
2. **Broad insurance and claims scope to five Kentucky homeowners policy-layer smells.** Sandbox 002 deliberately narrowed the domain and produced the evidence substrate.
3. **Technical findings to business-readable triage.** Sandbox 003 added LLM-assisted annotation, human review, cross-carrier analysis, and an executive report.
4. **Sales memo to expert work product.** Sandbox 004 separated the executive summary from the finding-level drill-down deliverable.
5. **Direct-carrier SaaS to provider-facing evidence capability.** The feasibility study found a crowded market and a more credible path through trusted compliance, filing, legal, actuarial, or insurtech providers.
6. **Static report to interactive review workbench.** Sandbox 006 reframed the report as a local evidence, interpretation, and action surface.
7. **Ad hoc multi-agent work to a repo-native SDLC hybrid.** Sandbox 005 selected existing repository artifacts as the control plane, with selected Agile V concepts and Codex as the first execution engine.
8. **Production-ready aspiration to production-aligned portfolio work.** The current goal is to make bounded demos and artifacts look and behave like credible software while keeping production infrastructure behind explicit validation and stage gates.

## Honest Boundaries

- Two carriers and five issue classes demonstrate a method, not a market.
- The provider-facing buyer model and USD 60,000 to USD 90,000 annual income range are hypotheses, not forecasts or committed revenue.
- A skilled professional using a general LLM may reproduce part of the report value. The remaining hypothesis is that source acquisition, stable provenance, repeatable detectors, graph relationships, review workflow, and auditability create additional value.
- Missing, redacted, copyrighted, or unparsed documents limit what the system can establish.
- KFBM's actual base policy jacket is not in the corpus and its form number is unknown. ISO HO 04 93 is a roof-surfacing ACV endorsement, not that base jacket.
- Human expert review remains part of the product concept.

## Open Decisions

- [ ] Decide when to start Sandbox 005 Stage 002.
- [ ] Complete Sandbox 006 visual and responsive review.
- [ ] Validate the provider-facing workflow with at least one trusted domain contact and one provider-side contact.
- [ ] Choose the synthetic public demo corpus and first production-aligned surface.
- [ ] Decide the first paid unit only after validation: package, pilot, workspace, internal provider tool, or research engagement.
- [ ] Recheck Kentucky Growers SERFF availability when the owner chooses to spend time on the access lane.

## Repository Map

- `sandboxes/` - bounded experiments and preserved proofs.
- `corpus/` - primary analysis inputs and acquisition records.
- `feasibility-studies/` - external market reports and validation notes.
- `productization/` - portfolio and future production gates.
- `skills/` - repo-visible workflows shared across agents.
- `journal/` - chronological point-in-time history.
- `lessons/` - reusable project learning.
- `previous-chats/` - historical conversation archive.
