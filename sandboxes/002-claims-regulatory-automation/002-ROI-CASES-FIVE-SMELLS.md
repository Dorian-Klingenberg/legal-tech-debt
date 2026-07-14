# ROI Cases For The Five Active Policy-Layer Smells

Status: Preserved directional ROI support document; not a validated sales forecast
Scope: Kentucky homeowners policy-layer smell experiments
Controlling scope: `002-five-policy-layer-phish.md`

## Purpose

This document keeps ROI reasoning aligned to the five active Sandbox 002 smells. It replaces the older broad platform ROI framing with smaller, smell-specific cases that are useful for proof-of-concept prioritization.

These are not legal conclusions or audited savings estimates. They are directional ROI cases: each one explains why detecting the smell early could plausibly avoid claim leakage, litigation expense, regulatory rework, form refiling, or reviewer time.

## Sales Use Case

This document is meant to support a buyer-facing case for a focused homeowners policy-layer smell review service. It should not sound like a generic RegTech platform pitch. The sale is narrower:

> We can review your homeowners forms, endorsements, rate/rule excerpts, and state-specific schedules for five defect patterns that have already produced public losses, settlements, fines, litigation exposure, and remediation costs across the insurance industry.

The service is valuable even before any software product exists because the first deliverable is a source-traceable review report with detected smells, dollar-risk rationale, reviewer questions, and recommended cleanup priorities.

## ROI Logic For This Sandbox

Sandbox 002 is not trying to prove a full product business case yet. The near-term ROI question is narrower:

> Can a small homeowners policy-layer probe find defects early enough that a reviewer would recognize avoidable cost or risk?

For each smell, the useful ROI evidence is:

- a realistic loss path
- the cost pool it touches
- what the detector would flag before the expensive event
- the reviewer question that could lead to a fix

## Summary Table

| Active Smell | Primary Cost Pool | ROI Case | What The Probe Should Surface |
|---|---|---|---|
| Overbroad / Non-deterministic Exclusions | Coverage litigation, bad-faith exposure, inconsistent denials | Broad exclusion wording can produce court-dependent outcomes or force carriers to pay claims they believed were excluded. | Sweeping phrases such as "arising out of," "directly or indirectly," "governmental action," "virus," "data," and missing carve-outs. |
| Magic Number / Magic Valuation Terms | Claim disputes, bad-faith exposure, manual rework | Undefined terms such as "actual cash value," "reasonable time," or "prompt notice" turn ordinary claims into interpretive disputes. | Vague timing or valuation language with no number, formula, schedule, or versioned source. |
| Coverage Inversion / Contradictory Conditions | Unintended coverage, unintended denial, E&O exposure | Broad grants plus endorsement stacks can leave reviewers unsure whether coverage exists at all. | Broad coverage grants that are hollowed out by exclusions, exceptions, sublimits, or conflicting priority language. |
| Calculation Rule Drift / Unversioned Rate Reference | Systematic underpayment, overpayment, premium leakage, audit findings | A valuation or rating method can drift from what the policy, filing, or reviewer expects. | References to "current" manuals, company guidelines, ACV methods, loss-cost sources, or rating factors without versioning. |
| Regulatory Mapping Smells | Market conduct findings, remediation, refiling, interest/penalties | Generic "as required by law" language can hide missing Kentucky-specific duties, deadlines, or disclosures. | Missing KRS/KAR citations, missing state schedules, generic multi-state language, and unversioned bulletin references. |

## Cost-Benefit Analysis

The first Sandbox 002 cost-benefit question is not "Which detector can become a full product?" It is "Which smell is cheap enough to surface as source-traceable candidate evidence and valuable enough that a reviewer would care?"

Use this as a relative planning guide for the next stage.

| Rank | Smell | Prototype Cost | Expected Benefit | Main Cost Drivers | Main Benefit Drivers | Net Read |
|---|---|---|---|---|---|---|
| 1 | Magic Number / Magic Valuation Terms | Low | High | Phrase list, nearby-definition scan, reviewer validation of false positives. | ACV, replacement cost, depreciation, notice, and timing terms are common and directly tied to disputes. | Best first detector: cheap, visible, easy to explain. |
| 2 | Regulatory Mapping Smells | Low-Medium | High | Citation extraction, Kentucky source manifest, checking nearby schedules or KRS/KAR references. | Missing state-specific parameters can create filing, audit, and market-conduct remediation cost. | Strong second detector: direct compliance value with manageable logic. |
| 3 | Overbroad / Non-deterministic Exclusions | Medium | High | Needs phrase detection plus simple context checks to avoid noisy results. | Broad exclusions can become portfolio-wide litigation or bad-faith risk when applied to repeated facts. | High-value detector, but needs careful reviewer questions. |
| 4 | Calculation Rule Drift / Unversioned Rate Reference | Medium | Very High | Requires rate/rule source excerpts, version metadata, and sometimes a comparison target. | Drift can create systematic underpayment, overpayment, premium leakage, or audit findings. | Potentially highest dollar value, but source procurement is harder. |
| 5 | Coverage Inversion / Contradictory Conditions | Medium-High | High | Needs complete form package, endorsement relationships, and a small clause graph. | Can expose unintended coverage, unintended denials, and inconsistent claim decisions. | Important, but should follow fixture assembly and simpler detectors. |

## Benefit Categories

### Direct benefits

- Finds reviewable defects before a claim population is affected.
- Reduces repeated manual review of the same vague wording.
- Creates source-traceable evidence for policy, claims, compliance, and product review.
- Helps distinguish "text risk" from legal conclusion, keeping human review in the loop.

### Avoided-cost benefits

- Avoided coverage litigation or earlier settlement posture.
- Avoided class-pattern underpayment or overpayment.
- Avoided market conduct findings and remediation.
- Avoided form refiling or endorsement cleanup after launch.
- Avoided premium leakage from stale or unversioned rating references.

### Learning benefits

- Clarifies which public Kentucky homeowners sources are enough for meaningful detection.
- Shows which smells can be detected with plain text and which require relationship graphs.
- Produces reusable candidate-evidence and fixture patterns for future stages.
- Prevents the project from drifting back into broad infrastructure or platform work.

## Cost Categories

### Build costs

- Procurement time for Kentucky homeowners forms, endorsements, and rate/rule filings.
- Markdown conversion and source manifest upkeep.
- Detector implementation time.
- Report formatting and finding schema updates.

### Review costs

- SME or reviewer time to separate true concerns from harmless drafting conventions.
- False-positive triage, especially for broad exclusions and coverage inversion.
- Updating candidate evidence and fixture examples as better source material is procured.

### Complexity costs

- Simple phrase-based smells are cheap but risk shallow findings.
- Relationship-based smells require more structure but produce richer insight.
- Rate/rule drift has high ROI potential but depends on getting the right source material.

## Recommended Build Order

1. **Magic Number / Magic Valuation Terms**
   - Lowest prototype cost.
   - Strong homeowners relevance.
   - Easy to surface as candidate evidence and explain in a reviewer report.

2. **Regulatory Mapping Smells**
   - Natural extension of citation/reference extraction from Sandbox 001.
   - Gives compliance-oriented value without infrastructure.
   - Helps validate the Kentucky source manifest discipline.

3. **Overbroad / Non-deterministic Exclusions**
   - High business value, especially for catastrophe-style repeated facts.
   - Requires slightly better context handling than a pure phrase list.
   - Good candidate once the first two detectors establish the report format.

4. **Calculation Rule Drift / Unversioned Rate Reference**
   - Potentially the strongest economic case.
   - Best started once at least one rate/rule filing or synthetic rating excerpt is ready.
   - Should stay narrow: one or two version-reference checks before formula comparison.

5. **Coverage Inversion / Contradictory Conditions**
   - Most structurally interesting and probably the hardest to make clean.
   - Needs package-level context: base form plus endorsements plus priority language.
   - Best treated as the first graph-shaped detector after simpler text smells are working.

## Cost-Benefit Conclusion

The best near-term return is not to chase the highest-dollar smell first. It is to build a cheap detection/reporting loop around Magic Number / Magic Valuation Terms and Regulatory Mapping Smells, then use that loop to support the higher-complexity smells.

The strongest economic upside likely sits in Calculation Rule Drift and Coverage Inversion, but those need better source packages. The strongest proof-of-concept upside sits in Magic Number, Regulatory Mapping, and Overbroad Exclusion detection because they can produce credible findings quickly from small homeowners excerpts.

## Dollar-Value Cost-Benefit Case

The project's 84-entry claims-and-policy taxonomy is accompanied by research mapping selected patterns to public settlements, regulatory fines, market-conduct penalties, adverse coverage outcomes, and class-action allegations. Those analogies do not prove causation or avoided cost. The five Sandbox 002 smells sit in coverage determination, valuation, rating, and regulatory mapping, where the project found useful public risk context.

### Public Cost Anchors From Project Research

| Active Sandbox 002 Smell | Public Cost Evidence In Project Docs | Buyer-Facing Lesson |
|---|---|---|
| Overbroad / Non-deterministic Exclusions | UK FCA business interruption test case: more than GBP 1 billion in reported payments after broad disease/prevention-of-access wording failed under stress. Aviva data-exclusion dispute: ambiguous "arising out of" wording forced defense/indemnity on part of an 80,000-person class action. | Broad exclusions are cheap to draft and expensive to test in court. A small wording review can prevent one phrase from becoming a portfolio-wide dispute. |
| Magic Number / Magic Valuation Terms | Pedicini Kentucky ambiguity example: undefined payment term allowed bad-faith exposure to survive. Labor depreciation class-action wave: more than $5 million alleged underpayment in one Trumbull/Hartford suit and "hundreds of millions" across the industry since 2015. | Undefined valuation and timing terms are repeatable dispute generators. These are some of the easiest high-value smells to detect early. |
| Coverage Inversion / Contradictory Conditions | Ironshore wind-driven-rain endorsement dispute: carrier faced up to $26 million exposure versus intended $250,000 sublimit. US COVID BI litigation: 1,937 lawsuits by June 2021 even where carriers often prevailed. | Even a legally defensible position can be expensive if the policy reads broader than the exclusion stack actually allows. |
| Calculation Rule Drift / Unversioned Rate Reference | State Farm ACV settlement: $15.6 million. Marshall Fire underinsurance example: one home insured for $419,000 against an $850,000 rebuild estimate, a $431,000 gap. Han v. State Farm alleged systematic property underpayment from using lower new-construction pricing rather than reconstruction pricing. | Drift between filed/policy promises and pricing or valuation references can create systematic leakage, not one-off error. |
| Regulatory Mapping Smells | Florida OIR hurricane market conduct exams: $2.575 million in fines across ten carriers. Louisiana hurricane exams: nearly $1 million in proposed fines. South Dakota Farmers/Foremost market conduct exam: $750,000 penalty. | "As required by law" is not a control. Missing state-specific mapping creates audit, remediation, and penalty exposure. |

### 10-Year Exposure Framing

The broader Sandbox 002 taxonomy estimated annual impact for a typical P&C insurer with $1B+ in written premium:

| Defect Category | Relevant Active Smells | Estimated Annual Impact | 10-Year Exposure Range |
|---|---|---:|---:|
| Semantic defects | Overbroad / Non-deterministic Exclusions; Magic Number / Magic Valuation Terms | $20M-$200M | $200M-$2.0B |
| Structural defects | Coverage Inversion / Contradictory Conditions | $5M-$50M | $50M-$500M |
| Dependency defects | Regulatory Mapping Smells where references are missing, stale, or null | $5M-$25M | $50M-$250M |
| Legislative/regulatory drift | Regulatory Mapping Smells; Calculation Rule Drift / Unversioned Rate Reference | $10M-$100M | $100M-$1.0B |

These are broad-category estimates, not a promise that every homeowners book carries that much risk. For sales purposes, use them to show scale, then make a conservative point: even finding and fixing a tiny fraction of this exposure can justify a focused review.

### Conservative Buyer Savings Scenarios

| Scenario | What The Review Prevents Or Reduces | Conservative Savings Case |
|---|---|---:|
| One avoided coverage dispute | Early cleanup of one overbroad exclusion, contradictory condition, or undefined valuation term before it reaches litigation. | $50k-$500k avoided defense/escalation cost, using the taxonomy's structural and semantic incident ranges. |
| One avoided serious valuation class pattern | ACV/depreciation/rate-reference issue found before repeated claim payments accumulate. | $1M-$10M avoided remediation reserve, far below public examples such as $15.6M State Farm ACV and industry-wide labor depreciation settlements. |
| One avoided regulatory remediation cycle | Missing Kentucky-specific mapping or notice/cancellation parameter caught before audit or filing challenge. | $500k-$2.5M avoided penalty/remediation exposure, anchored by $750k, nearly $1M, and $2.575M public market-conduct examples. |
| One avoided endorsement/sublimit contradiction | Delivered policy and intended coverage hierarchy reconciled before a catastrophic loss. | $1M-$25M avoided coverage exposure, anchored by the Ironshore $26M vs. $250k sublimit example. |
| Ongoing reviewer time reduction | Repeatable smell report reduces manual form/rule review for common defects. | 10%-25% reduction in targeted review time for the reviewed corpus; quantify with the buyer's hourly legal/compliance/product rates. |

### Proposed Service Pricing

These prices are for a focused advisory/proof-of-concept service, not a production platform.

| Offer | Scope | Buyer Profile | Suggested Price |
|---|---|---|---:|
| Five-Smell Snapshot | Review one homeowners program or 10-25 forms/endorsements/rate-rule excerpts. Deliver smell report, ROI notes, and cleanup priority list. | Carrier product/compliance team exploring the concept. | $25k-$40k |
| Kentucky Homeowners Deep Dive | Review one Kentucky homeowners program package, including base form, common endorsements, rate/rule excerpts, and state-specific mappings. Include source manifest and executive ROI memo. | Regional carrier, MGA, or compliance/legal team with Kentucky exposure. | $60k-$90k |
| Multi-State Homeowners Smell Audit | Review the same homeowners product across Kentucky plus 2-4 comparison states for jurisdictional inheritance and mapping drift. | Carrier with multi-state homeowners filings. | $125k-$250k |
| Litigation/Remediation Rapid Review | Targeted review after a dispute, market-conduct concern, filing objection, or suspected valuation/rate drift. | Legal/compliance team facing immediate exposure. | $40k-$75k per rapid review |
| Retainer / Quarterly Smell Scan | Quarterly scan of new filings, endorsements, and rule changes for the five active smells. | Product/compliance organization that wants ongoing hygiene. | $8k-$20k per month |

### Payback Logic

| Offer | Price | Break-Even Avoided Cost | Payback Story |
|---|---:|---:|---|
| Five-Smell Snapshot | $25k-$40k | One small coverage/legal escalation avoided. | Pays back if it prevents or shortens a single $50k-$100k dispute. |
| Kentucky Homeowners Deep Dive | $60k-$90k | One moderate claim dispute, refiling cycle, or compliance remediation avoided. | Pays back if it avoids one $100k-$250k issue or identifies one high-priority form cleanup. |
| Multi-State Homeowners Smell Audit | $125k-$250k | One state-specific compliance defect or repeated valuation issue avoided. | Pays back if it prevents a six-figure remediation project or catches a pattern before it spreads across states. |
| Litigation/Remediation Rapid Review | $40k-$75k | Better early settlement posture or narrowed discovery/remediation scope. | Pays back if it reduces outside counsel/remediation spend by even a small percentage. |
| Retainer / Quarterly Smell Scan | $96k-$240k annually | One regulatory mapping miss, rating drift, or repeated wording defect avoided each year. | Pays back against public fine/remediation examples in the $750k-$2.575M range. |

### Simple ROI Formula For A Prospect

```text
Expected annual value =
  (probability of avoided event x estimated event cost)
  + reviewer time savings
  + avoided remediation/refiling cost
  - service fee
```

Example conservative pitch:

```text
If the review has only a 10% chance of preventing a $1M remediation or litigation event,
expected value is $100k.

If the service costs $60k-$90k, the buyer has a plausible positive expected ROI before
counting reviewer time savings, reduced outside counsel spend, or reputational risk.
```

For a larger carrier, the same logic scales:

```text
If a $150k multi-state audit has a 10% chance of catching a $5M repeated valuation,
coverage, or regulatory mapping defect, expected value is $500k.

That is a 3.3x expected-value case before soft benefits.
```

### Sales Positioning

Lead with the real public-cost examples, then narrow quickly:

- "We are not asking you to buy a platform."
- "We are offering a focused smell audit of homeowners policy-layer defects."
- "The five smells were selected because public events show these patterns can create seven- and eight-figure exposure."
- "The first engagement is small enough to approve as legal/compliance/product risk review, not enterprise transformation."
- "The deliverable is a source-traceable report your policy, claims, compliance, and legal teams can actually review."

## Case 1: Overbroad / Non-deterministic Exclusions

### Property proxy: COVID business interruption exclusion disputes

The project research notes that broad disease, governmental action, and prevention-of-access wording became extremely expensive when applied at scale. The useful lesson for Sandbox 002 is not the commercial BI product itself; it is the drafting pattern: broad exclusion subjects plus sweeping causal language can become non-deterministic when a large event stresses the policy.

Sandbox 002 detector value:

- Flag broad exclusion subjects before they are applied to a catastrophe-scale fact pattern.
- Ask whether the exclusion has a narrow trigger, explicit carve-outs, and a priority rule against the coverage grant.
- Create an early reviewer queue for exclusions likely to be reinterpreted by courts or regulators.

Potential ROI path:

- Fewer escalated denials.
- Reduced coverage counsel review on repeated fact patterns.
- Lower chance that one ambiguous phrase becomes a portfolio-wide dispute.

### Homeowners relevance

For homeowners, the same pattern can appear in ordinance-or-law, governmental action, virus/bacteria, mold, water, data/electronic systems, and anti-concurrent-causation language.

## Case 2: Magic Number / Magic Valuation Terms

### Property case family: labor depreciation and ACV disputes

The project research identifies labor depreciation class actions and ACV disputes as examples where undefined valuation methodology created large claim-payment exposure. The homeowners relevance is direct: property claims often turn on actual cash value, replacement cost, depreciation, condition, age, useful life, and comparable pricing.

Sandbox 002 detector value:

- Flag "actual cash value," "fair market value," "reasonable cost," "customary charge," "prompt notice," and similar terms when no formula or deadline is nearby.
- Ask whether depreciation applies to labor, materials, overhead, profit, taxes, or code upgrades.
- Ask whether a timing term maps to a Kentucky statutory or regulatory deadline.

Potential ROI path:

- Fewer valuation disputes.
- Fewer repeated manual escalations over the same undefined term.
- Earlier correction of policy forms or claim guidance before a class pattern forms.

### Kentucky proxy: ambiguous policy terms and bad-faith exposure

The broader research includes a Kentucky ambiguity example involving undefined payment terminology. The lesson for this sandbox is that Kentucky-facing wording should be treated carefully when a term is known to support multiple interpretations.

## Case 3: Coverage Inversion / Contradictory Conditions

### Property proxy: wind/flood and concurrent causation disputes

The project research notes that catastrophe property claims can become expensive when policies do not clearly explain how covered and excluded perils interact. This is a close fit for homeowners because wind, water, flood, surface water, sewer backup, mold, ordinance-or-law, and ensuing-loss provisions often sit in different parts of the form and endorsement stack.

Sandbox 002 detector value:

- Build a small clause relationship map for grant, exclusion, exception, endorsement, and sublimit language.
- Flag when a broad grant appears to be fully hollowed out by later provisions.
- Flag same-peril clauses that point to different outcomes without a priority rule.

Potential ROI path:

- Reduced coverage litigation over mixed-cause losses.
- Less adjuster uncertainty and fewer inconsistent claim decisions.
- Earlier form cleanup when endorsement stacks contradict the base form.

### Property proxy: missing or conflicting sublimit endorsement

The research also includes a missing endorsement/sublimit scenario where the intended coverage limit and delivered policy did not match. For Sandbox 002, this supports checking whether endorsements and schedules actually preserve the intended coverage hierarchy.

## Case 4: Calculation Rule Drift / Unversioned Rate Reference

### Homeowners case family: rebuild-cost and stale pricing references

The project research discusses underinsurance after major residential fire losses where replacement-cost estimates and post-loss rebuild cost reality diverged. The technical smell is not just "bad estimate"; it is unversioned or unsynchronized pricing references across underwriting, rating, and claim valuation.

Sandbox 002 detector value:

- Flag references to "current rating guidelines," "current ISO loss costs," "company valuation guide," or unnamed cost databases.
- Ask whether the source has an edition date, effective date, filing identifier, or approved manual version.
- Compare policy wording, rate/rule filing excerpts, and claim valuation references for version drift.

Potential ROI path:

- Earlier detection of systematic underinsurance or mispricing.
- Reduced premium leakage from stale factors.
- Better audit defense because the filed rule, policy promise, and implemented method are traceable.

### Homeowners relevance

This smell fits dwelling limit estimation, roof age factors, protection class factors, construction type, deductible factors, inflation guard, replacement cost, ACV, and ordinance-or-law calculations.

## Case 5: Regulatory Mapping Smells

### Property regulatory case family: hurricane market conduct findings

The project research identifies property market-conduct findings involving required notices, claim handling deadlines, and payment/denial timing after hurricanes. For Sandbox 002, the lesson is that policy and claim-facing language that says "as required by law" is not enough if the Kentucky requirement is not mapped to a concrete deadline, notice, citation, or state-specific schedule.

Sandbox 002 detector value:

- Flag "as required by law," "where permitted by law," and "in accordance with applicable law" when no KRS/KAR citation or Kentucky parameter appears nearby.
- Flag multi-state forms that do not carry Kentucky-specific cancellation, renewal, notice, or mandatory coverage terms.
- Flag bulletin or DOI references without versioning or supersession handling.

Potential ROI path:

- Fewer market conduct exceptions.
- Less manual compliance review during filings and audits.
- Lower remediation cost because missing mappings are found before a claim population is affected.

## What To Measure In The Next Stage

For each candidate evidence item that may become a fixture or finding, capture a lightweight ROI note:

```text
smell:
source_section:
cost_pool:
why_it_matters:
reviewer_question:
possible_fix:
confidence:
machinery_confidence:
```

Example cost pools:

- coverage litigation
- claim leakage
- premium leakage
- regulatory remediation
- form refiling
- reviewer time
- bad-faith exposure
- customer complaint escalation

## Boundary

Keep these ROI cases tied to the five active smells. Do not use this document to reopen broad claims-platform ROI, PAS integration ROI, live regulatory feed ROI, or generic RegTech market sizing.

The discovery-and-instrumentation layer should attach ROI context only as candidate evidence. Final smell findings, severity, cleanup priority, and reviewer decisions belong to downstream detector and reporting layers.
