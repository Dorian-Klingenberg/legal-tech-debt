# AI Reality-Check Prompt

Date: 2026-06-06
Purpose: Weekend-friendly prompt for asking an external AI system whether Legal Tech Debt is a real product opportunity or a nothing burger.

---

## Recommended Tool Order

1. **ChatGPT Deep Research**, if available.
   - Best fit for a sourced, structured market/competitive/buyer analysis.
   - Use if you want citations and a report you can inspect.

2. **Perplexity Deep Research / Research**, if available.
   - Best fit for fast source discovery and finding market, association, vendor, regulator, and competitor links.
   - Good fallback if ChatGPT Deep Research is unavailable.

3. **Claude**, preferably with Research enabled if available.
   - Best fit for skeptical critique, weak-point analysis, and turning the research into clear questions.
   - Use after one sourced research pass, or use immediately if you want a cold strategic critique without spending the whole day.

Do not use a normal no-search chat as the only reality check. It can critique logic, but it cannot reliably tell whether the market already exists, who buys, or whether the premise has been contradicted by current sources.

---

## Configuration

Use the most research-capable mode available:

- Enable web/research/deep research.
- Ask for citations.
- Ask it to distinguish facts, inferences, and assumptions.
- Ask it to be adversarial.
- Ask it not to flatter the idea.
- Do not upload private code, detector logic, or the full repository.
- Provide only the project summary, current prototype facts, and target-market question.

---

## Pasteable Prompt

You are acting as a skeptical market due-diligence analyst and red-team evaluator. Your job is to decide whether my product idea is a real opportunity, a small consulting/report niche, a research project, or probably a nothing burger.

Do not encourage me by default. Do not flatter the work. Do not assume that "AI + insurance compliance" is a market. I want grounded, source-backed reality, including the case against the idea.

If you cannot verify a claim with sources, label it as an inference or assumption. If the best answer is "unclear until you talk to buyers," say that, but still tell me exactly which buyers to talk to and what evidence would change the verdict.

### Product Being Evaluated

Name: Legal Tech Debt

One-sentence concept:

> A source-traceable review workflow for finding insurance policy and regulatory document risks before they become filing, broker, claims, litigation, or remediation problems.

More detail:

Legal Tech Debt examines insurance policy documents and related legal/regulatory sources, identifies policy-layer "code smells" or risk patterns, retrieves supporting evidence, and produces human-reviewed findings. The current prototype is focused on homeowners/property insurance policy review. It is not legal advice. It is not an exhaustive national scanner. It is not yet validated with buyers.

Current prototype status:

- Only two insurance carriers have been examined.
- The proof of concept is in Kentucky homeowners/property insurance.
- Only five policy-layer smells have been tested so far.
- The current output is closer to a specialized report/evidence workflow than a finished SaaS product.
- No paying buyer has validated the need yet.

Personal commercial hypothesis:

- I am testing whether this could eventually support roughly USD 60,000 to USD 90,000 per year in income through specialized reports, pilots, advisory work, or tooling.
- Treat that number as a hypothesis, not proof.
- Test whether that income level is reasonable, too optimistic, or aimed at the wrong buyer.

Founder/business-model constraint:

- I do not want a high-volume direct-sales business.
- I do not want 2,000 small customers.
- I do not want to spend my life chasing sales, running repetitive reports, or doing busy work.
- I may be willing to work for those customers' existing providers, platforms, law firms, consultants, filing vendors, regulatory intelligence vendors, or technology vendors.
- Reframe the client if appropriate: the best customer may be a provider that already serves insurers, not the insurer directly.
- Evaluate whether this is better as a capability, expert workflow, report engine, diligence method, or partner/vendor feature inside someone else's existing customer relationship.

### What We Have Dug Up So Far

Buyer/workflow hypotheses:

- Possible buyer/workflow owners: insurance compliance, product/forms, claims coverage, legal, regulatory affairs, policy administration, market-conduct/remediation, or vendor management.
- Possible non-buyer validators: former regulators, market-conduct examiners, insurance regulatory lawyers, brokers, mutual insurers, and insurtech operators.
- The first safe artifact for outside discussion should be a sanitized sample report, not source code, detector internals, prompts, repository contents, or full corpus strategy.

Warm contacts:

- Karen: a highly trusted Saskatchewan insurance professional with CAIB/CIP credentials and Germania Mutual/Saskatchewan context. Likely best for insurance-domain sanity checking: "does this sound real or overblown?"
- Roger: an insurance technology/CIO-type contact from Finesse. Likely best for carrier-systems and go-to-market mapping: "who inside a carrier would own this?"

Saskatchewan/SGI context:

- Saskatchewan may be useful for warm validation, especially property/casualty, mutual-insurer, broker, home/farm/business policy questions.
- Saskatchewan is probably not a clean first market for anything centered on compulsory auto insurance because SGI's Saskatchewan Auto Fund is structurally central there.
- SGI has two relevant sides: the Saskatchewan Auto Fund for compulsory auto, and SGI CANADA for property/casualty products sold through independent brokers.
- The Insurance Brokers Association of Saskatchewan appears to represent a large share of Saskatchewan property/casualty brokerages, so brokers may be useful validators even if they are not direct buyers.

U.S. context:

- The strongest possible U.S. market would likely involve property/casualty carriers, carrier compliance teams, legal/regulatory teams, claims coverage teams, forms/product teams, outside counsel, filing support vendors, or insurtech vendors.
- A major risk is that this work is already handled well enough by existing counsel, ISO/Verisk-type services, regulatory filing tools, internal compliance teams, or general-purpose LLMs.

### Primary Question

Is this a real market opportunity, a narrow consulting/report opportunity, a research project, or probably a nothing burger?

### Required Research Behavior

Use current web research if available. Prioritize primary or high-quality sources:

- insurance regulator pages,
- SGI / Saskatchewan official pages,
- insurance broker/professional associations,
- carrier product/forms/compliance sources,
- incumbent vendor pages,
- regulatory filing/product compliance vendors,
- legal/regulatory commentary from credible firms,
- market reports only when claims are specific and attributable.

Avoid relying on generic AI hype articles. If using them, label them as weak evidence.

For each market or competitor claim, cite sources. Separate:

- **Verified fact**
- **Reasonable inference**
- **Speculation**
- **Unknown / needs buyer interview**

### Major Tests To Run

1. **Buyer Test**
   - Who, specifically, would own this workflow?
   - Who has budget?
   - Who feels pain before a claim, filing problem, broker issue, or regulatory problem occurs?
   - Who would care but not pay?

2. **Substitute Test**
   - What do carriers, brokers, mutuals, and compliance/legal teams use today?
   - Include outside counsel, internal review, ISO/Verisk-type services, SERFF/filing tools, compliance management tools, document review vendors, insurtech tools, and manual workflows.

3. **Generic LLM Substitution Test**
   - Could a highly skilled insurance/compliance/legal professional simply ask ChatGPT, Claude, or Perplexity to do this directly using public sources?
   - If a skilled professional with a good prompt could get 80% of the value from a general LLM, say so clearly.
   - Identify what remains valuable, if anything, beyond generic LLM use.
   - Evaluate whether the defensible value is source acquisition, evidence graphing, stable citations, repeatable detectors, jurisdiction comparison, human review workflow, audit trail, domain taxonomy, speed, liability controls, buyer trust, or report packaging.

4. **Incumbent / Competition Test**
   - Identify at least five substitutes or competitors to investigate.
   - For each, explain whether it competes directly, partially substitutes, or defines buyer expectations.
   - Include existing vendor categories even if you cannot find a perfect direct competitor.
   - Address the incumbent paradox: if this industry already has ISO/Verisk-type forms/content, SERFF filing workflows, regulatory-change tools, filing-intelligence tools, outside counsel, internal compliance teams, and policy-admin systems, why would the issues found by this prototype still exist?
   - If incumbents are probably catching these issues, explain why clients might not care or act: low severity, low frequency, accepted risk, remediation cost, no clear owner, state approval comfort, lack of claims signal, or buried legal/compliance knowledge.
   - If incumbents are probably not catching them, explain which job they actually perform instead and what gap remains.

5. **Market Wedge Test**
   - What is the strongest first wedge?
   - What is the weakest wedge?
   - Is "Kentucky homeowners/property policy review" a reasonable proof point or too narrow?
   - Is Saskatchewan meaningful as a first market, or mainly useful for trusted validation?

6. **Trust / Liability Test**
   - What would make an insurer, lawyer, compliance officer, or regulator trust this report?
   - What wording would make them reject it?
   - What legal-advice, E&O, confidentiality, or procurement concerns would appear?

7. **Business Model Test**
   - Is this more likely to sell as:
     - one-off expert reports,
     - a recurring monitoring/report service,
     - a narrow consulting service,
     - a pilot with a carrier,
     - a tool licensed to counsel/compliance teams,
     - a vendor feature inside someone else's platform,
     - or not commercially attractive?
   - Assess whether USD 60,000 to USD 90,000 per year in income is plausible, too low, too high, or pointed at the wrong buyer.
   - Specifically assess low-sales-burden paths: working for existing providers, licensing/reporting to vendors, subcontracting to law/compliance firms, selling to a small number of platform partners, or packaging the workflow as expert augmentation.

8. **Kill Criteria Test**
   - What evidence would make this idea not worth pursuing?
   - What interview answer would be a serious warning?
   - What market fact would make this a nothing burger?

### Scoring Rubric

Score each category from 0 to 5 and explain the score:

- Buyer pain clarity
- Budget owner clarity
- Urgency
- Repeatability across carriers/states
- Differentiation from generic LLMs
- Differentiation from incumbents
- Trust/compliance feasibility
- Ease of first validation
- Suitability of Kentucky proof point
- Suitability of Saskatchewan validation path
- Plausibility of USD 60,000 to USD 90,000/year personal income

Then give:

- total score out of 55,
- confidence level,
- whether the score suggests continue, pause, narrow, or stop.

### Required Output

Use this exact structure:

1. **Executive Verdict**
   - Verdict: real opportunity / possible niche / consulting-only / research project / probably nothing burger / unclear.
   - Confidence level.
   - One-paragraph reason.

2. **Fact / Inference / Unknown Table**
   - Table with three columns: claim, status, evidence/source or reason.

3. **Buyer Map**
   - Top three likely buyers/workflow owners.
   - Top three people who care but probably do not pay.
   - For each: why they care, what they already use, what question to ask them.

4. **Substitutes And Competitors**
   - At least five categories or named vendors/processes.
   - Include direct, partial, and internal/manual substitutes.
   - Cite sources.
   - Explain whether each substitute would likely catch the prototype's class of issues, and if not, why not.
   - Explain why a client might still ignore the issue even if the substitute or consultant catches it.

5. **Generic LLM Substitution Risk**
   - Could an expert do this with ChatGPT/Claude/Perplexity alone?
   - What percentage of value could a skilled expert plausibly get without this product?
   - What remains defensible, if anything?

6. **Saskatchewan / SGI Assessment**
   - Is Saskatchewan a real first market, a validation market, or a distraction?
   - How does SGI change the analysis?
   - What should I ask Karen?

7. **U.S. Market Assessment**
   - Best U.S. buyer wedge.
   - Biggest U.S. blocker.
   - Whether Kentucky homeowners/property is a good first proof point.

8. **Business Model Assessment**
   - Rank possible models: report service, consulting, SaaS/tooling, pilot, partner/vendor feature.
   - Assess USD 60,000 to USD 90,000/year plausibility.
   - Identify which models best match the founder constraint: low direct sales, few relationships, low busy work, high leverage through existing providers.

9. **Red-Team Critique**
   - Brutal reasons this may fail.
   - Nothing-burger scenario.
   - Signs I am overbuilding.

10. **Validation Questions**
   - Questions for Karen.
   - Questions for Roger.
   - Questions for first cold/warm insurance compliance contact.

11. **30-Day No-Build Validation Plan**
   - Week 1, Week 2, Week 3, Week 4.
   - No major software build work.
   - Include pass/fail thresholds.

12. **Final Decision Memo**
   - "If I were advising you this weekend, I would..."
   - Give one clear recommendation: continue, narrow, pause, or stop.

### Style Rules

- Be concise but not shallow.
- Be skeptical but not performatively negative.
- Do not tell me to build more software unless buyer/workflow evidence supports it.
- Do not use vague language like "huge opportunity" unless sources and buyer evidence justify it.
- If the best next step is five conversations rather than more research, say so.
- If this is likely a service business rather than a software product, say so.
- If this is likely useful but not fundable or venture-scale, say so.
- If the strongest product is actually "trusted expert report plus evidence trail" rather than "AI tool," say so.
