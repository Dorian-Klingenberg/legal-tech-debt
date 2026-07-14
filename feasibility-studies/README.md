# Legal Tech Debt Feasibility Studies

Date created: 2026-06-06
Status: Active research bundle
Purpose: Keep external feasibility reports, counter-reports, and current validation working notes together.

---

## Current Read

Current disposition, 2026-07-13:

- The provider-facing evidence-workflow hypothesis remains the leading commercial frame.
- The owner has chosen to continue bounded portfolio, SDLC, and UX experiments while buyer validation remains open.
- This does not authorize a commercial SaaS build, production infrastructure, or revenue claims.
- The four external reports are unedited point-in-time inputs. They may contain stale counts, vendor claims, links, or assumptions; this README and the synthesis control the current interpretation.

These reports do **not** yet settle whether Legal Tech Debt is a product, service, provider-facing capability, or research artifact.

The current useful framing is:

> Legal Tech Debt may be more valuable as a specialized evidence/review capability for existing insurance compliance, legal, filing, regulatory intelligence, or insurtech providers than as a direct-to-carrier product.

The central unresolved question is no longer "does competition exist?" It does. The sharper question is:

> If incumbents exist, why did the prototype's issue class survive existing workflows, and does that survival indicate a valuable gap or a low-priority issue that buyers already tolerate?

Current synthesis:

- [client-pivot-synthesis-2026-06-06.md](client-pivot-synthesis-2026-06-06.md) — strategic review of all four reports through the provider/client-base pivot lens.

---

## External Reports

| File | Role | Notes |
|---|---|---|
| [market-due-diligence-consulting-only.md](external-reports/market-due-diligence-consulting-only.md) | Bearish / conservative due diligence | Frames the current opportunity as consulting-only, with no SaaS proof yet. |
| [market-due-diligence-red-team-evaluation.md](external-reports/market-due-diligence-red-team-evaluation.md) | Red-team market evaluation | Finds possible niche, leaning report service/consulting rather than scalable product. |
| [counter-report-contrarian-review.md](external-reports/counter-report-contrarian-review.md) | Counter-report against bearish view | Argues the bearish report overstates incumbents and underweights filing-delay pain. |
| [bull-case-due-diligence-graph-policy-smell-detector.md](external-reports/bull-case-due-diligence-graph-policy-smell-detector.md) | Bull-case technical and market thesis | Argues graph-based legal/policy smell detection may be a defensible niche/data wedge. |

Original root filenames were renamed for clarity when moved into this folder.

---

## Working Notes

| File | Role | Notes |
|---|---|---|
| [ai-reality-check-prompt.md](working-notes/ai-reality-check-prompt.md) | Prompt harness | Due-diligence prompt for ChatGPT, Claude, or Perplexity reality checks. |
| [product-validation-targets.md](working-notes/product-validation-targets.md) | Product validation map | Named contacts, outreach order, Saskatchewan/SGI notes, and founder business-model constraint. |
| [canadian-ai-grant-feasibility.md](working-notes/canadian-ai-grant-feasibility.md) | Canadian funding/entity feasibility | Canadian grant paths, U.S. grant comparison, corporation ownership and dissolution considerations. |
| [family-executive-summary-draft.md](working-notes/family-executive-summary-draft.md) | Family-facing project summary | Plain-language explanation of the project, personal money hypothesis, and risk-grounded framing. |

---

## Known Strategic Constraints

- Avoid a high-volume direct-sales business.
- Avoid repetitive report production for thousands of small customers.
- Prefer low-sales-burden paths through existing providers, platforms, law firms, consultants, filing vendors, regulatory intelligence vendors, or technology vendors.
- Do not treat "AI + insurance compliance" as proof of a market.
- Do not build a commercial product or production infrastructure until buyer/workflow evidence improves. Bounded portfolio, SDLC, synthetic-demo, and UX experiments may continue under explicit sandbox stages.
- Use sanitized samples for validation; do not share source code, detector internals, prompts, or full corpus strategy.

---

## Active Questions

- [ ] Who owns this pain inside an insurer: compliance, product/forms, legal, claims, filing, or someone else?
- [ ] Which provider category would benefit most from this as an internal capability?
- [ ] Do incumbents already catch the issue class, and if so, why do clients not act?
- [ ] If incumbents do not catch the issue class, what job are they actually doing instead?
- [ ] Can a skilled insurance/compliance/legal professional reproduce 80% of the value with ChatGPT, Claude, or Perplexity?
- [ ] Does the defensible value lie in source acquisition, evidence graphing, stable citations, repeatable detectors, human review, audit trail, domain taxonomy, or report packaging?
- [ ] Is Saskatchewan useful only for warm validation, or also for a real property/casualty wedge?
- [ ] Is Kentucky homeowners/property a credible proof point or too narrow to matter commercially?
- [ ] Is USD 60,000 to USD 90,000/year plausible through a small number of provider relationships?

---

## Next Validation Steps

- [x] Collect bearish, red-team, counter, and bull-case reports into one folder.
- [x] Preserve the current AI reality-check prompt.
- [x] Preserve the product validation target map.
- [x] Preserve the Canadian grant/entity feasibility note.
- [x] Preserve the family-facing executive summary draft.
- [x] Collect the four available bearish, red-team, counter, and bull-case reports under `external-reports/`.
- [ ] Add future external analysis only when it materially changes a validation question.
- [ ] Ask Karen whether a sanitized finding sounds like a real insurance workflow problem or over-reading.
- [ ] Ask Roger who inside a carrier or provider would own this workflow.
- [ ] Identify 5-10 provider-side targets rather than only end-carrier targets.
- [ ] Compare incumbent tools against the exact issue class found by the prototype.
- [ ] Decide whether the next move is validation conversations, a provider-facing sample, or stopping/narrowing.
