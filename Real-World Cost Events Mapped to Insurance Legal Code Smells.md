# Real-World Cost Events Mapped to Insurance Legal Code Smells

## Overview

The 83 smells identified across the two companion documents — 41 in Claims and 42 in Policy — are not theoretical. For each major category, real insurers have absorbed measurable financial losses in the form of class-action settlements, regulatory fines, market conduct penalties, and adverse court judgments. The examples below are organized by smell section and annotated with the financial consequence, the smell it instantiates, and what the underlying technical failure was.

***

## Claims Smells — Real-World Examples

### Section 1: Coverage Determination Smells

#### Undefined Concurrent Causation → *Hurricane Ian / Harvey Wind-vs-Water Disputes*
When Hurricane Harvey devastated Houston in 2017 and Hurricane Ian hit Florida in 2022, the absence of explicit apportionment rules for concurrent wind-flood losses triggered thousands of coverage disputes and extensive litigation. Florida applies the concurrent causation doctrine, under which any contribution by a covered peril can trigger full coverage — unless the policy has an explicit Anti-Concurrent Causation (ACC) clause. Policies that were *silent* on how to apportion left carriers exposed to paying wind-and-flood losses on policies written only for wind. Policies with ACC clauses faced the opposite problem: courts and regulators scrutinized whether the clause was being applied beyond its legitimate scope. The financial cost was enormous — CoreLogic estimated that 52% of Houston residential and commercial properties lacked flood insurance, concentrating disputes on ambiguously worded windstorm policies.[^1][^2][^3]

**Smell instantiated:** *Undefined Concurrent Causation* — the policy was silent on how to apportion a multi-peril loss.

***

#### Overbroad Exclusion Applied → *UK FCA Business Interruption Test Case (2020–2021)*
The FCA brought a landmark test case on behalf of roughly 370,000 policyholders after insurers applied "governmental action" and "disease" exclusions to deny virtually all COVID-19 business interruption claims. The UK Supreme Court ruled in January 2021 substantially in the policyholders' favor, finding that broad "disease clauses" and "prevention of access" clauses — when not precisely bounded — did trigger coverage. By September 2021, total reported BI payments had exceeded £1 billion, with interim payments on top of that. Carriers including Hiscox, RSA, QBE, and MS Amlin were required to pay claims they had denied by broadly applying exclusions that courts found were not drafted with sufficient precision to eliminate coverage.[^4][^5][^6]

**Smell instantiated:** *Overbroad Exclusion Applied* — carriers applied broad exclusion language beyond its intended scope, lost in court, and paid over £1 billion.[^4]

***

#### Non-deterministic Exclusion → *"Arising Out Of" Scope Disputes*
"Arising out of" and "related to" are among the most litigated phrases in coverage law because they create a scope boundary that courts interpret inconsistently. In *Aviva v 8262900 Canada* (2023), the Ontario Superior Court found that a data exclusion endorsement worded with "arising out of" excluded liability for personal injury claims from a data breach but did NOT exclude bodily injury claims — a split outcome driven entirely by the non-deterministic scope of the exclusion language. The carrier had to defend and indemnify the insured on half the claims from an 80,000-person class action, a result that was directly traceable to ambiguous exclusion drafting.[^7]

**Smell instantiated:** *Non-deterministic Exclusion* — the phrase "arising out of" produced an adjudicator-dependent outcome that cost the insurer coverage it thought it had excluded.

***

#### Magic Number Ambiguity → *Pedicini v. Life Insurance Company of Alabama*
The 6th Circuit Court of Appeals held that the insurer's use of the undefined term "actual charges" — without specifying whether it meant amount billed or amount accepted as full payment — created an ambiguity that the insurer was already on notice about from prior circuit court rulings. Because the insurer *knew* the term was ambiguous under Kentucky law and knew it must be construed in favor of the insured, yet still denied the claim under its own preferred interpretation, the court allowed a bad-faith claim to survive. The cost: litigation exposure on both the contract and bad-faith claims, plus potential extracontractual damages.[^8]

**Smell instantiated:** *Magic Number Ambiguity* — "actual charges" had no defined threshold, leading directly to bad-faith exposure.

***

#### Zombie Coverage / Missing Endorsement → *Ironshore v. RPG Hospitality (Hurricane Florence, 2018)*
Ironshore's underwriter failed to include a wind-driven rain sublimit endorsement when renewing a hotel policy. A senior employee audited the policy three months *before* Hurricane Florence made landfall and discovered that the endorsement — which limited wind-driven rain coverage to $250,000 — had been omitted from the policy delivered to the policyholder. The company did not immediately disclose this to the insured. When Florence caused catastrophic damage, RPG claimed the full $26 million policy limit. The Court of Appeals of Georgia held there were genuine issues of material fact as to whether the full limit applied, remanding the case to trial — leaving Ironshore exposed to up to $26 million vs. the $250,000 sublimit they intended.[^9]

**Smell instantiated:** *Zombie Coverage* — a sublimit endorsement that should have been in the policy was missing due to a form delivery error, creating massive unintended coverage exposure.

***

### Section 2: Valuation & Payment Smells

#### Calculation Rule Drift / Magic Valuation Term → *State Farm ACV Class Action (Arkansas, 2024–2026)*
A civil jury found that State Farm breached its contract by failing to properly calculate actual cash value on totaled vehicles. State Farm reached a $15.6 million settlement with affected Arkansas policyholders in 2026, receiving preliminary court approval in March of that year. The core issue: State Farm's ACV calculation methodology — which used "Projected Sold Adjustments" to reduce comparable-vehicle list prices — had drifted from what policyholders understood their policies to promise. A parallel class action in North Carolina (*Brewer v. State Farm*, filed October 2025) alleged that State Farm's "condition adjustment" via CCC Intelligent Solutions similarly reduced total-loss payouts through an undisclosed methodology.[^10][^11][^12]

**Smell instantiated:** *Calculation Rule Drift* and *Magic Valuation Term* — "actual cash value" was used without a defined calculation methodology, and the claims system's formula had drifted from what the policy promised.

***

#### Undefined Depreciation Logic → *Labor Depreciation Class Action Wave (2015–Present)*
When insurers depreciate *labor* in addition to materials when calculating ACV, and their policies do not explicitly authorize labor depreciation, class actions follow. The Arkansas Supreme Court ruled in 2013 that labor is not "logically depreciable" and may not be reduced when policies do not expressly state otherwise. This triggered a wave of class actions in at least 15 states. The Hartford subsidiary Trumbull Insurance faced a class action by Betty and Daniel Grawe alleging that hundreds of thousands of claimants in 15 states were underpaid by more than $5 million due to improper labor depreciation. Cincinnati Insurance settled a class action for improper depreciation of labor and general contractor costs — the Cincinnati settlement was notable enough to generate its own dedicated settlement-claims-filing infrastructure. These cases collectively cost the industry "hundreds of millions of dollars in settlement payments" over the last decade, per the *Property Insurance Coverage Law Blog*.[^13][^14][^15][^16][^17]

**Smell instantiated:** *Undefined Depreciation Logic* — policies that did not specify the depreciation methodology left carriers legally exposed to class-action liability whenever the claimed method was inconsistent with state law.

***

#### Stale Pricing Reference → *Marshall Fire Underinsurance Litigation (Colorado, 2022–Present)*
After the 2021 Marshall Fire devastated Louisville, Colorado, homeowners discovered that insurer-recommended coverage amounts — generated by software tools at the time of policy issuance — were wildly insufficient to cover actual rebuild costs. A Louisville couple insured for $419,000 found their actual rebuild cost was $850,000. Colorado Insurance Commissioner Michael Conway confirmed publicly that the software insurers use to *recommend* coverage levels and the software they use to *price* post-loss rebuilds are different systems, consistently producing a gap. Lawsuits named agents, carriers, and the software vendors. The core technical failure: pricing reference tools were not version-locked or synchronized to current construction cost reality.[^18]

**Smell instantiated:** *Stale Pricing Reference* — the estimation tool used at policy inception was disconnected from the cost database used at claims time, producing systematic underinsurance.

***

#### Non-Executable Payment Condition → *COVID-Era Payment Processing Delays*
Florida's Office of Insurance Regulation fined eight insurers a total of $2,575,000 in 2025 for misconduct during Hurricanes Ian and Idalia, with findings including failures to pay or deny claims within the state-mandated 90-day window and failures to pay interest when owed. Among the specific findings: American Coastal Insurance Company ($400,000 fine), American Mobile Insurance Exchange ($400,000), and Clear Blue Insurance Company ($400,000), among others. These violations reflect a systemic pattern of payment conditions existing on paper with no system-enforced trigger — the procedural equivalent of the *Non-Executable Payment Condition* smell.[^19][^20]

**Smell instantiated:** *InvariantViolation — Payment Deadline* and *Non-Executable Payment Condition* — no system enforcement of payment deadlines resulted in regulatory violations and $2.575 million in fines.[^20]

***

### Section 3: Notice & Procedure Smells

#### InvariantViolation — Payment Deadline → *Florida OIR Hurricane Ian Market Conduct Examinations (2025)*
The Florida OIR's market conduct examination found that in one carrier, the error rate for not including required disclosure statements exceeded 60% for Hurricane Ian claims and 80% for Hurricane Idalia claims. These errors — missing legally required notices in payment letters, failing to acknowledge communications within statutory timeframes, and failing to pay interest on delayed payments — are textbook *InvariantViolation* smells: statutory obligations with no system-enforced tracking or trigger. Ten carriers were examined; all ten were fined, with penalties totaling $2.575 million.[^19][^20]

***

#### Sunset Obligation Smell → *COVID-Era Waiver Persistence*
A direct instantiation of this smell: during COVID, insurance regulators across many states issued emergency bulletins extending notice deadlines, waiving late-reporting defenses, and modifying claims procedures. Where carriers' claims workflow systems absorbed these rules without a sunset trigger, claims filed *after* the emergency period were still processed under emergency-era rules — either inadvertently granting waivers that carriers had no obligation to extend, or applying obsolete documentation requirements. No single case has been publicly adjudicated as "caused by a COVID waiver that wasn't turned off," but the OIR examinations noted the operational complexity of having two layers of procedural rules (pre-COVID and COVID-modified) running simultaneously in claims systems.[^19]

***

### Section 4: Adjuster Workflow & Decision Smells

#### Blob Adjuster / No Coverage Decision Log → *Farmers "Bring Back a Billion" Program (North Dakota, 2007)*
The North Dakota Insurance Department fined Farmers Insurance $750,000 — the largest fine in state history at the time — after investigators uncovered that Farmers had implemented incentive pay programs ("Bring Back a Billion," "Quest for Gold") that created quotas for claim denials and capped settlement ranges regardless of individual claim merit. Adjusters who deviated from prescribed low-settlement targets faced pay cuts. This is a precise real-world instantiation of the *Blob Adjuster* and *Implicit Escalation Default* smells: one adjuster handled coverage determination, valuation, and payment approval under a hidden incentive structure, with no documented decision authority matrix and no auditable decision log. The $750,000 fine was explicitly described as punitive; actual customer harm was believed to be widespread but not individually quantified.[^21][^22]

**Smell instantiated:** *Blob Adjuster*, *Hidden State in Adjuster Notes*, *No Coverage Decision Log* — the claims system produced non-reproducible, incentive-distorted outcomes with no audit trail.

***

#### Jurisdictional Inheritance in SIU → *State Farm Algorithm Bias Lawsuit (Huskey v. State Farm, 2022–Present)*
In December 2022, Black homeowners filed a class-action lawsuit under the Fair Housing Act alleging that State Farm's machine-learning algorithms for predicting fraudulent claims produced racially discriminatory outcomes — with Black claimants 39% more likely to be asked for additional documentation and white claimants nearly one-third more likely to have claims processed in under a month. The case survived a motion to dismiss in 2023 and remains in active litigation, with one of the named plaintiffs alleging her claim took three months longer to process than her white neighbor's claim for identical storm damage to an attached townhome. This is the *Jurisdictional Inheritance in SIU* smell generalized to a demographic dimension: a single fraud-prediction model was applied uniformly regardless of whether its indicator variables were valid proxies for fraud risk across all demographic groups.[^23][^24][^25][^26]

**Smell instantiated:** *Jurisdictional Inheritance in SIU* — a uniform fraud model produced demographically inconsistent outcomes, generating active Fair Housing Act litigation and reputational cost.

***

### Section 5: Subrogation & Recovery Smells

#### Missing Statute of Limitations Trigger → *Systemic Subrogation Deadline Failures*
Subrogation deadlines vary dramatically by state and by claim type — from two years (Florida tort claims) to six years (New York contract claims) — and are triggered from the date of loss, not from the date of claim resolution. Insurers that lack jurisdiction-aware, system-enforced subrogation deadline tracking silently lose recovery rights when those deadlines lapse. While no single insurer has publicly disclosed a material financial loss attributed specifically to missed subrogation SOL deadlines, the problem is well-documented in insurance recovery law literature: "The difference between a recoverable subrogation claim and a closed file often comes down to one simple question: When did the clock start ticking?". Given that private health insurers recovered an estimated $1.7–$2.5 billion annually through subrogation as far back as 2010, the opportunity cost of untracked deadline lapses is measurable.[^27][^28][^29][^30]

**Smell instantiated:** *Missing Statute of Limitations Trigger* — no system-enforced deadline tracking silently erodes recovery rights.

***

### Section 6: Regulatory & Bad Faith Exposure Smells

#### Non-deterministic Denial / Time-Based Logic Leak in Bad Faith → *Louisiana Hurricane Market Conduct Examinations (2022)*
Following Hurricanes Laura, Delta, and Zeta, the Louisiana Insurance Commissioner proposed nearly $1 million in fines against multiple carriers based on market conduct examinations that found 44 instances of improper activities, including boilerplate denial letters that did not cite specific policy provisions and failures to respond to claimants within statutory time limits. This is a direct instantiation of *Non-deterministic Denial* (denial letters using boilerplate without citing the specific policy provision) and *Time-Based Logic Leak in Bad Faith* ("We will respond promptly" with no defined SLA and no system enforcement).[^31][^32]

***

## Policy Smells — Real-World Examples

### Section 1: Form & Wording Smells

#### Coverage Inversion → *Business Interruption — COVID-19 (US, 2020–2023)*
In the US, the coverage inversion played out in reverse: carriers drafted BI policies that *read* as if virus and governmental action would be covered (broad property-loss insuring agreements), but exclusions — particularly virus exclusions and governmental action exclusions — eliminated most of the coverage when actually tested. By the end of June 2021, 1,937 business interruption lawsuits had been filed. The total legal cost was enormous, even though carriers ultimately prevailed in most US federal appellate courts. The cost was not the claims paid — it was the litigation cost, regulatory scrutiny, and reputational damage from denying claims that policyholders genuinely believed they had purchased.[^33][^34]

**Smell instantiated:** *Coverage Inversion* — policies read as providing broad property coverage but exclusions substantially narrowed the scope, creating massive dispute volume even where carriers legally prevailed.

***

#### Circular Definition → *ISO "Bodily Injury" and "Permanently Attached Equipment" Disputes*
Courts have explicitly called out circular definitions in coverage disputes. The Louisiana Supreme Court in *Hebert v. Webre* (2008) found that the ISO definition "bodily injury means bodily injury, sickness or disease" was circular and should not be used to restrict coverage. In a 2025 property claim, an adjuster denied coverage for a stolen generator based on the definition "permanently attached equipment means equipment that is permanently attached" — a circular self-reference that left the adjuster unable to make a deterministic coverage decision. These cases illustrate exactly the *Circular Definition* smell: the adjuster cannot make a rule-based coverage determination because the definition references itself.[^35]

**Smell instantiated:** *Circular Definition* — the Louisiana Supreme Court refused to enforce circular ISO language; adjusters in current claims are still encountering the same pattern.

***

#### Magic Number Term → *Multiple State Bad-Faith Rulings on Undefined Deadlines*
All states except South Carolina have "prompt pay" laws requiring insurers to process claims within defined timeframes (typically 30, 45, or 60 days). These laws were enacted precisely *because* policy language like "respond promptly" or "within a reasonable time" produced no actionable obligation and allowed indefinite delay. Insurers that still embed undefined temporal terms in their claims procedures — rather than coding them to statutory SLAs — risk the interest penalties (up to 18% in some states) and regulatory fines that these laws impose.[^36]

**Smell instantiated:** *Magic Number Term* — "reasonable time" without a defined threshold is unenforceable and has prompted legislative mandates with real financial teeth.

***

#### Contradictory Conditions → *Wind-Driven Rain Endorsement — Ironshore v. RPG Hospitality*
As described above, the failure to include a sublimit endorsement in the policy delivered to the insured created a direct contradiction between the binder (which limited wind-driven rain coverage to $250,000) and the policy-as-delivered (which carried a $26 million full-limit grant). The court found that this generated genuine factual issues requiring trial, leaving the insurer potentially exposed to over 100x the intended sublimit.[^9]

***

### Section 2: Rating & Underwriting Rule Smells

#### Calculation Rule Drift → *Xactimate "New Construction vs. Reconstruction" — Han v. State Farm (2021)*
A proposed class action alleged that State Farm pivoted at some point from using Xactimate's reconstruction pricing (higher) to new construction pricing (lower) for all property damage claims — regardless of which Xactimate category correctly applied — generating systematically underpaid claims. The policy promised to cover the cost of reconstruction; the claims system formula had drifted to use a cheaper calculation that did not match the filed definition. This is a textbook *Calculation Rule Drift* smell: the exposure base definition in the filed coverage promise diverged from the calculation method in the claims system.[^37]

**Smell instantiated:** *Calculation Rule Drift* — the pricing methodology used in the claims system drifted from the methodology that the policy language implied, generating class-action exposure.

***

#### Missing Else / Undefined Behavior → *ReSource Pro Policy Error Data (2018)*
ReSource Pro, which processes thousands of insurance policies monthly on behalf of carriers, reported an average of nine errors per policy and logged more than 4.5 million discrepancies in 2018. The most common: incorrect location/address, incorrect per-occurrence and aggregate limits, and exposure mismatches between ACORD forms and issued policies (e.g., a policy issued for 7 vehicles when 10 were requested). These represent missing-else and undefined-behavior smells in the configurator: no branch for the case where the quoting engine received an input combination that produced a coverage gap. The financial cost is dispersed across E&O claims and coverage disputes, but the data suggests this is an industry-wide structural problem.[^38]

***

### Section 3: Regulatory Mapping Smells

#### Jurisdictional Inheritance → *South Dakota Farmers/Foremost Fine ($750,000, 2015)*
South Dakota's Division of Insurance found "various deficiencies" across five Farmers and Foremost companies in a market conduct examination and levied a combined $750,000 penalty. The deficiencies encompassed claims handling, cancellation/non-renewal practices, and other compliance failures that regulators attributed to practices not being tailored to South Dakota's specific requirements. This is the *Jurisdictional Inheritance* smell at scale: processes and rules designed for a multi-state carrier's dominant markets were applied uniformly in a state with different requirements.[^39]

***

#### Regulatory Drift in Claim Handling → *Florida OIR Disclosure Requirement Violations (Hurricanes Ian/Idalia, 2025)*
Florida updated its claims handling disclosure requirements (including the Homeowners Claims Bill of Rights), but carriers' claims workflows were not updated to match. The result: in one carrier, more than 80% of Hurricane Idalia claims were processed without the required disclosure statements. The OIR classified this as a violation of Florida's Insurance Code and fined the carrier accordingly. This is a near-perfect instantiation of *Regulatory Drift in Claim Handling*: the DOI updated its standards; the claims workflow was not updated to match.[^19]

**Smell instantiated:** *Regulatory Drift in Claim Handling* — the statutory requirement changed, the claims system did not, and the error rate exceeded 80%.[^19]

***

### Section 4: Spec-to-Configurator Traceability Smells

#### Spec-Code Divergence → *Missing Wind-Driven Rain Endorsement (Ironshore, 2018)*
The binder and policy specification said one thing (sublimit applies); the policy-as-configured and delivered to the policyholder said another (full limit, no sublimit). An internal audit discovered the divergence three months before the hurricane — but the carrier did not disclose it, creating both a coverage exposure and potential bad-faith exposure for non-disclosure. This is the *Spec-Code Divergence* smell: the written spec said "sublimit"; the configurator produced a policy without that sublimit.[^9]

***

#### Manual Sync Between Systems → *Farmers "Bring Back a Billion" Quota Violations*
The North Dakota investigation found that Farmers' claims handling incentive structure — which involved manual quota targets communicated through management directives that were separate from the formal claims system — created a parallel, undocumented decision layer. This is a *Manual Sync Between Systems* smell: the actual decision logic lived in a separate management reporting system (or informal meeting culture) that was never synchronized with the documented claims procedures.[^22][^21]

***

## Cross-Cutting Financial Impact Summary

| Smell Category | Representative Incident | Approximate Cost |
|---|---|---|
| Undefined Concurrent Causation | Hurricane Ian/Harvey wind-flood disputes | Hundreds of millions across industry[^1][^3] |
| Overbroad Exclusion Applied | UK FCA BI Test Case (COVID) | £1+ billion paid[^4] |
| Calculation Rule Drift / Magic Valuation Term | State Farm ACV class action (Arkansas) | $15.6 million settlement[^11] |
| Undefined Depreciation Logic | Industry-wide labor depreciation class actions | "Hundreds of millions" since 2015[^15] |
| Stale Pricing Reference | Marshall Fire underinsurance (Colorado) | Individual gaps of $400K+ per home[^18] |
| InvariantViolation — Payment Deadline | Florida OIR Hurricane Ian/Idalia fines | $2.575 million in regulatory fines[^20] |
| Blob Adjuster / Hidden State | Farmers "Bring Back a Billion" (ND) | $750,000 regulatory fine[^21] |
| Jurisdictional Inheritance in SIU | Huskey v. State Farm (algorithm bias) | Active FHA litigation, reputational cost[^25] |
| Non-deterministic Denial | Louisiana hurricane market conduct exams | ~$1 million proposed fines[^32] |
| Zombie Coverage / Missing Endorsement | Ironshore v. RPG Hospitality | Up to $26M exposure vs. $250K sublimit[^9] |
| Jurisdictional Inheritance (Policy) | SD Farmers/Foremost market conduct exam | $750,000 regulatory fine[^39] |
| Regulatory Drift in Claim Handling | Florida OIR Ian/Idalia error rate >80% | Included in $2.575M fines[^19] |

***

## Smells With No Confirmed Public Cost Event

Several smells did not yield a publicly attributable, named case with a confirmed dollar amount within the last 10 years. These are not necessarily rare — they may simply resolve quietly in settlements, internal audits, or reinsurance disputes that are not publicly disclosed:

- **Dead Workflow Step / Dead Recovery Path / Dead Rating Rule** — these tend to produce quiet process inefficiency rather than dramatic litigation, unless a specific claim falls into the dead path and the failure is discovered in discovery.
- **Orphan Definition / Orphan Denial Reason Code** — typically resolved at the claims adjuster level before reaching litigation.
- **Non-Executable Payment Condition** (e.g., approval by a defunct agency) — these are extremely fact-specific and rarely litigated publicly.
- **Order-Sensitive Rating** — this produces non-reproducible quotes, which surface as premium disputes that are typically resolved informally.
- **Unversioned Subrogation Clause** — rights either lapse silently (financial cost invisible) or produce recovery attempts in novel states that fail; no named cases found with confirmed dollar amounts in the last decade.

The absence of a named public case does not mean these smells are harmless. Industry-wide claims leakage is estimated at $30 billion to $67 billion annually in the US alone, with 5–10% of all claims paid estimated to represent leakage attributable to exactly these kinds of systemic process and drafting failures.[^40]

***

*Research note: Dollar figures represent settlements, regulatory fines, and court judgments as publicly reported. Litigation costs, defense fees, and reputational losses are additional but not quantified here. The majority of coverage disputes settle confidentially; the cases cited represent the publicly visible fraction of a larger pattern.*

---

## References

1. [Causation Issues to Consider as You Prepare Your Hurricane Ian ...](https://www.hunton.com/insights/legal/causation-issues-to-consider-as-you-prepare-your-hurricane-ian-insurance-claim) - The Supreme Court of Florida held that the concurrent causation doctrine applied and the loss would ...

2. [Anti-Concurrent Causation Policy - Gulf Coast Insurance Attorneys](https://www.gulfcoastinsuranceattorneys.com/blog/2024/november/what-are-anti-concurrent-causation-policy-provis/) - Many homeowner's insurance policies have an anti-concurrent causation policy clause that can play a ...

3. [HURRICANE HARVEY: ANTI-CONCURRENT CAUSATION ...](https://www.thompsoncoe.com/resources/publications/hurricane-harvey-anti-concurrent-causation-revisited/) - Under the doctrine of concurrent causation, when covered and uncovered perils contribute to a loss, ...

4. [BI test case payouts top £1bn with 64% of policyholders paid: FCA - Reinsurance News](https://www.reinsurancene.ws/bi-test-case-payouts-top-1bn-with-64-of-policyholders-paid-fca/) - New data from the Financial Conduct Authority (FCA) shows that total reported claims payments for po...

5. [Landmark £1.2 billion legal battle opens over pandemic ...](https://www.standard.co.uk/business/pandemic-business-insurance-court-case-legal-hiscox-b71605.html) - Britain’s top judges have begun to hear a landmark £1.2 billion case on insurance payouts for policy...

6. [Supreme Court judgment in FCA's business interruption insurance ...](https://www.fca.org.uk/news/press-releases/supreme-court-judgment-business-interruption-insurance-test-case) - The Supreme Court has today delivered its judgment in the Financial Conduct Authority’s (FCA)’s busi...

7. ["Arising out of" or "liability for"? Choice of words critical in interpretation of exclusion clauses](https://gowlingwlg.com/en-gb/insights-resources/articles/2023/words-critical-in-interpretation-exclusion-clause) - In the recent case of Aviva v 8262900 Canada, Justice Koehnen of the Ontario Superior Court of Justi...

8. [Insurers That Do Not Interpret Ambiguous Policy Language In Favor ...](https://www.propertyinsurancecoveragelaw.com/blog/insurers-that-do-not-interpret-ambiguous-policy-language-in-favor-of-the-policyholder-are-at-risk-for-bad-faith-liability/) - The lower court incorrectly granted summary judgment for LICOA on the bad-faith claims, finding that...

9. [Insurance Coverage Confusion: Unraveling the Impact of " ...](https://andersonkill.com/newsletter/insurance-coverage-confusion-unraveling-the-impact-of-missing-endorsements/) - Recently, the Court of Appeals of Georgia overturned a summary judgment decision that required Irons...

10. [Actual cash value case against Progressive loses class action status](https://www.repairerdrivennews.com/2025/09/05/actual-cash-value-case-against-progressive-loses-class-action-status/) - In another undervalued actual cash value (ACV) case against Progressive, the United States Court of ...

11. [State Farm Settles Suit Over Under-Valuing Total-Loss Cars - CarPro](https://www.carpro.com/blog/state-farm-settles-suit-over-under-valuing-total-loss-cars) - State Farm has reportedly agreed to pay $15.6 million to settle a class-action lawsuit alleging it u...

12. [Class action lawsuit against State Farm for undervaluing ... - YouTube](https://www.youtube.com/watch?v=Qzd1PUpucKo) - ... class action lawsuit against State Farm for undervaluing totaled vehicle claims. The lawsuit is:...

13. [Insurer Faces Class Action for Depreciating Labor in Actual Cash ...](https://www.insurancejournal.com/news/national/2023/02/16/708211.htm) - Two Trumbull Insurance customers who believe they were short-changed on claims payments have filed a...

14. [Labor Depreciation Class Actions Heating Up Across The Country](https://www.jdsupra.com/legalnews/labor-depreciation-class-actions-heating-01326/) - Class action litigation is spreading across the country involving the application of depreciation in...

15. [Depreciation of Labor Issues Are Largely Being Determined in Class ...](https://www.propertyinsurancecoveragelaw.com/blog/depreciation-of-labor-issues-are-largely-being-determined-in-class-action-cases/) - Depreciation of Labor Issues Are Largely Being Determined in Class Action Cases · Decisions focusing...

16. [Cincinnati Insurance class action settlement](https://topclassactions.com/lawsuit-settlements/open-lawsuit-settlements/cincinnati-insurance-class-action-settlement/) - Cincinnati Insurance reached an insurance class action settlement to resolve claims it wrongfully de...

17. [Cincinnati Insurance Class Action Settlement Overview](https://classactiondiscovery.com/cases/cincinnati-insurance-settlement) - The lawsuit alleged that Cincinnati Insurance improperly deducted depreciation on labor and general ...

18. [Why didn't Marshall fire homeowners have enough insurance ...](https://uphelp.org/why-didnt-marshall-fire-homeowners-have-enough-insurance-watchdogs-blame-industry-software-2/?print=print) - And the Mayfields say an estimate for actual costs to rebuild the home they once had now stands at $...

19. [Commissioner Yaworsky Penalizes Companies Over $2 Million Due ...](https://floir.gov/home/2025/09/02/commissioner-yaworsky-penalizes-companies-over--2-million-due-to-misconduct-during-past-hurricanes) - In several of the examinations, OIR found companies failed to pay or deny claims in 90 days. The mar...

20. [Commissioner Yaworsky Penalizes Two More Companies for ...](https://floir.gov/newsroom/archives/item-details/2025/11/03/commissioner-yaworsky-penalizes-two-more-companies-for-misconduct-during-hurricanes-ian---idalia) - This finalizes OIR's market conduct examinations against 10 companies for claims-handling operations...

21. [N.D. Regulator Fines Farmers $750,000 - Insurance Journal](https://www.insurancejournal.com/news/midwest/2007/07/02/81365.htm) - Farmers Insurance Group has been fined $750,000 for allegedly setting up incentives for auto insuran...

22. [Are Market Conduct Examiners Listening to Common Property ...](https://www.propertyinsurancecoveragelaw.com/blog/are-market-conduct-examiners-listening-to-common-property-insurance-claims-complaints/) - The North Dakota Department of Insurance paid attention to the internal claims documents of Farmers ...

23. [State Farm accused of covert racial discrimination in claims processing](https://www.wglt.org/local-news/2022-12-19/state-farm-accused-of-covert-racial-discrimination-in-claims-processing) - Huskey's lawyers said they based their case for systemic racial discrimination on a study of more th...

24. [Lawsuit Against State Farm Alleges Racial Discrimination in Claims ...](https://www.claimsjournal.com/news/national/2022/12/16/314325.htm) - Specifically, more delays are experienced by Black policyholders during the claims process, with the...

25. [State Farm Algorithm Bias Lawsuit - Sanford Heisler Sharp](https://sanfordheisler.com/case/discrimination-harassment/state-farm-algorithm-bias-lawsuit/) - Home › Case › Discrimination and Harassment Cases › State Farm Algorithm Bias Lawsuit ... claims pro...

26. [Case: Huskey v. State Farm Fire & Casualty Company](https://clearinghouse.net/case/44310/) - index,follow

27. [How Long Does An Insurance Company Have to Subrogate](https://lippmanrecupero.com/how-long-does-an-insurance-company-have-to-subrogate/) - The primary constraint on subrogation actions stems from state-specific statutes of limitations. The...

28. [How Long Does an Insurance Company Have to Subrogate?](https://stephenbarkerlaw.com/blog/how-long-does-an-insurance-company-have-to-subrogate/) - Insurance companies don't have forever to make a subrogation claim. While the statutory limitations ...

29. [A Race Against Time: Why Timing is Everything in Subrogation Claims](https://derreverelaw.com/a-race-against-time-why-timing-is-everything-in-subrogation-claims/) - Subrogation claims are bound by strict statutory deadlines, but the clock starts running as soon as ...

30. [ERISA Subrogation: Statute of Limitations & Personal Injury Claim Tips](https://www.peacelawfirm.com/erisa-subrogation/) - ERISA's statute of limitations extends to six years in cases involving fraud or concealment. This to...

31. [Who's Got Money to Burn?/Articles/CLM Magazine](https://www.theclm.org/Magazine/articles/complaints-market-conduct-exams-prove-powerful-in-managing-claims-compliance-risk/617) - Reviewing market conduct exams and any associated fines, fees, and penalties that other companies ha...

32. [The Case of the Missing Market Conduct Exams](https://www.propertyinsurancecoveragelaw.com/blog/the-case-of-the-missing-market-conduct-exams/) - ... claims handling resulted in a $750,000 fine for state law violations. He also explains the Insur...

33. [Illinois Appellate Court Denies Business Interruption Insurance Claim Related to COVID-19](https://www.gouldratner.com/publication/illinois-appellate-court-denies-business-interruption-insurance-claim-related-to-covid-19) - In the wake of the COVID-19 pandemic, many businesses across the country filed claims for business i...

34. [Insurers Remain Undefeated In Federal And State Appellate Tribunals On COVID-19 Business Interruption Claims - Clausen Miller](https://www.clausen.com/insurers-remain-undefeated-in-federal-and-state-appellate-tribunals-on-covid-19-business-interruption-claims/) - By Melinda S. Kollross The body of federal and state appellate precedent keeps growing, with these a...

35. [Circular Definitions | Insurance Commentary with Bill Wilson](https://insurancecommentary.com/circular-definitions/) - In my book, “When Words Collide: Resolving Insurance Coverage and Claim Disputes,” I discuss this is...

36. [A Matter of Law: Prompt Pay Laws - APA Services](https://www.apaservices.org/practice/business/legal/professional/prompt-pay) - All states except South Carolina have rules requiring insurers to pay or deny claims within a certai...

37. [Lawsuit Claims State Farm Uses 'New Construction' Numbers to ...](https://www.classaction.org/news/lawsuit-claims-state-farm-uses-new-construction-numbers-to-generate-lower-cost-estimates-for-property-remodeling-jobs) - A class action claims State Farm Fire and Casualty Company has wrongfully used lower "new constructi...

38. [3 Most Common Insurance Policy Errors - ReSource Pro](https://www.resourcepro.com/blog/common-insurance-policy-errors/) - 1. Location Based on our data, an incorrect location or address is the top error. This is typically ...

39. [North and South Dakota Fine Insurers More than $1 Million](https://www.insurancejournal.com/magazines/mag-features/2015/06/15/371021.htm) - The South Dakota Division of Insurance (DOI) said it reached a settlement with Farmers Insurance Gro...

40. [Eliminating Claims Leakage - Core P&C Insurance Software Solutions](https://www.spear-tech.com/eliminating-claims-leakage/) - Claims leakage is defined as the extent of financial loss due to errors, inefficiencies, or fraudule...

