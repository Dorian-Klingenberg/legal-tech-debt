# Insurance Process Maturity Models: A Landscape Assessment for the Legal Tech Debt Platform

## Executive Summary

No single CMMI equivalent exists for the insurance industry. Instead, the sector has accumulated a patchwork of domain-specific maturity models — each covering a narrow slice of insurer operations — with significant structural gaps in the areas most relevant to legal tech debt: policy form quality, regulatory mapping integrity, and claims adjudication governance. The five models with the most substance are examined below, along with an honest accounting of what each covers, what each misses, and where the opportunity lies for a process-quality framework derived from RAII defect taxonomy and CMMI discipline.

***

## The Five Models That Actually Exist

### 1. ACORD Insurance Digital Maturity Study

**What it is:** The closest thing the industry has to an industry-wide benchmark. Published annually by ACORD (the global insurance standards body), the study assesses the largest insurers worldwide — 210 carriers in its 2026 edition — and segments them across five levels of digital maturity.[^1][^2]

**The five levels:**
- **Digital Competitors** — Fully integrated digital capability used to influence customers and partners, improve performance, and support strategic positioning. Only 7% of carriers reached this level as of 2026.[^2][^1]
- **Digitalised Firms** — Broad digitalization completed across the value chain; roughly one quarter of carriers.[^3]
- **Digital Aspirants** — Digitalization underway but not yet integrated end-to-end.
- **Localised Digitalisation** — Digital activity siloed in specific functions or geographies.
- **Digital Laggards** — Digital activity limited, fragmented, or not prioritized; more than 10% of carriers.[^3]

**What it measures:** Digital capability adoption, technology integration, and strategic digital positioning. Covers the full P&C, life, and reinsurance value chain but measures *how digital* operations are, not *how well-governed* they are. The 2025/2026 editions added an AI & Digital Maturity addendum examining AI leverage potential — ACORD estimates robust AI integration could reduce P&C insurer expenses by as much as 14.6%, representing over $480 billion in annual industry savings.[^4][^3]

**Correlation with ACORD Data Standards:** A notable structural finding is that higher maturity correlates strongly with enterprise-wide adoption of ACORD Data Standards, while less mature insurers apply those standards only in isolated compliance or integration contexts. This matters for a legal tech debt platform because ACORD data standards address interoperability, not wording quality or regulatory traceability.[^1]

**What it misses for legal tech debt purposes:** The model entirely ignores policy form quality, rating rule governance, regulatory mapping integrity, and claims adjudication process discipline. A carrier could be a Digital Competitor while simultaneously operating with Circular Definitions, Orphan Denial Reason Codes, and Zombie Policies throughout its policy and claims infrastructure. Digital maturity and governance quality are orthogonal.[^5][^6]

***

### 2. RIMS Risk Maturity Model (RMM)

**What it is:** The most structurally CMMI-like model in the insurance ecosystem. The Risk and Insurance Management Society (RIMS) launched the RMM in 2006 and has since updated it. Critically, it is explicitly based on the Capability Maturity Model developed by Carnegie Mellon's SEI. It applies a five-level progression across seven core attributes of enterprise risk management.[^7][^8]

**The five levels:**
- **Nonexistent / Ad hoc** — Risk management undocumented, largely dependent on individual heroics.
- **Initial** — Basic processes emerging but inconsistently applied across silos.
- **Repeatable** — Common risk assessment and response frameworks in place; top risks reported to board.
- **Managed** — Risk management coordinated across business areas; tools and enterprise-wide monitoring in use.
- **Leadership** — Risk management is a proactive strategic tool using sophisticated modeling, real-time monitoring, and scenario planning.[^9][^10]

**The seven attributes assessed:**
1. Adoption of an ERM-based approach (culture, executive buy-in)
2. ERM process management (degree of embedding across the organization)
3. Risk appetite management (risk/reward awareness, tolerance, gaps)
4. Root cause discipline (causal analysis, risk source identification)
5. Uncovering risks (discovery, identification processes)
6. Performance management
7. Business resiliency and sustainability[^9][^7]

**The mechanics:** The RMM consists of 68 key readiness indicators describing 25 competency drivers across those seven attributes. Organizations complete a self-assessment and receive a scored report benchmarking against the model. The model is available to both RIMS members and non-members.[^7]

**What it covers well:** Root cause discipline (Attribute 4) is directly relevant — it focuses on searching for root causes of risks, classifying risks, and improving internal controls. This maps to CMMI's Causal Analysis and Resolution (CAR) process area and would, in principle, drive upstream fixes to policy wording when claims patterns reveal defects. The formal ERM-based approach also addresses governance culture and executive accountability in ways that overlap with CMMI's Organizational Process Focus.[^9]

**What it misses for legal tech debt purposes:** The RMM is scoped to enterprise risk management as a discipline — not to insurance product governance, policy form quality, or operational claims workflow. It would assess how well a carrier manages its risk portfolio, not how well it drafts coverage terms, versions its rate manuals, or traces adjuster decisions back to specific policy provisions. None of the 83 insurance-specific smells in the policy and claims taxonomy would be directly detected or prevented by RIMS RMM scoring.[^6][^5]

***

### 3. Aite-Novarica iDAMM (Insurance Data & Analytics Maturity Model)

**What it is:** Published by Aite-Novarica Group (now Datos Insights), the iDAMM provides a framework for insurers to evaluate their data organization and capabilities across seven dimensions and 21 subdimensions.[^11][^12]

**The three stages:**
- **Traditional** — Conventional data management; siloed systems; limited analytics capability.
- **Evolving** — Data governance developing; analytics capabilities expanding; integration underway.
- **Transforming** — Advanced analytics, AI/ML, data-driven decision-making embedded across the organization.[^12][^11]

**The seven dimensions:** Leadership and organization, data governance, architecture and technology management, and four additional subdimension clusters covering data quality, analytics capability, data operations, and integration. The model explicitly notes that insurers will have different maturity levels across different dimensions — a carrier can be Transforming in analytics while remaining Traditional in governance.[^11]

**What it covers well:** Data governance dimension overlaps with several Spec-to-Configurator Traceability Smells — specifically *No Regulatory Trace in Code*, *Manual Sync Between Systems*, and *Spec-Code Divergence*, all of which are fundamentally data quality and governance failures. An insurer at the Transforming stage would have strong data lineage practices that would naturally surface some of these.[^5]

**What it misses:** The iDAMM is entirely oriented toward data and analytics capability. It says nothing about policy wording quality, the legal validity of cross-references, regulatory mapping completeness, or the process by which claims decisions are documented and audited. The *Blob Adjuster*, *Non-deterministic Denial*, and *Circular Coverage Definition* smells are invisible to this model.[^6]

***

### 4. Send Technology Underwriting Maturity Framework

**What it is:** A vendor-published five-stage framework from Send Technology (a commercial underwriting workflow platform), focused on the evolution from manual to data-driven underwriting in commercial and specialty lines. Send has joined the International Underwriting Association to promote the framework across that membership.[^13][^14][^15]

**The five stages:** The framework maps a progression from fully manual, document-centric underwriting through increasing levels of data integration, workflow automation, and AI-assisted risk selection and pricing. Each stage characterizes how data is accessed, how underwriting insights are generated, and how exposure analysis and pricing decisions are made.[^14][^13]

**What it covers well:** The most operationally specific of the five models for underwriting. It directly addresses the transition away from isolated rule sets and paper-based processes that produce *Hardcoded Jurisdiction Logic*, *Duplicate Rating Logic*, and *Order-Sensitive Rating* smells. A carrier at Stage 4 or 5 would have unified data flows that make *Manual Sync Between Systems* structurally difficult to sustain.[^5]

**What it misses:** The framework is vendor-motivated and commercially scoped to underwriting workflow automation — not to policy form governance, regulatory compliance quality, or claims operations. It has no mechanism for detecting wording-level smells, no regulatory mapping assessment, and no claims lifecycle coverage. Its maturity levels are also process-automation stages, not governance quality levels — a carrier can automate bad rules efficiently without ever improving their legal quality.

***

### 5. NAIC Model Laws and Regulatory Frameworks

**What it is:** The National Association of Insurance Commissioners (NAIC) produces Model Laws, Regulations, and Guidelines that serve as template legislation adopted (with variations) by state insurance departments. The NAIC also produces standards such as the Insurance Data Security Model Law, which establishes cybersecurity program requirements for licensed insurers.[^16][^17]

**What it is not:** A maturity model. NAIC frameworks are compliance floors — binary pass/fail checklists of what carriers must do — with no concept of maturity levels, no improvement pathway from Level 1 to Level 5, and no process-quality assessment. They establish regulatory minimums, not operational excellence standards.[^17][^16]

**What it covers:** Compliance requirements for specific domains (cybersecurity, data security, market conduct, solvency). Relevant to the Regulatory Mapping Smells in the policy taxonomy — specifically *Unmapped Obligation* and *Jurisdictional Inheritance*, which represent failures to implement NAIC-derived requirements correctly. A market conduct examination by a state DOI would surface several smells in the Regulatory & Bad Faith Exposure section of the claims taxonomy.[^6][^5]

**What it misses:** Everything process-quality related. NAIC frameworks do not assess how a carrier drafts its forms, governs its rate manuals, manages cross-references to superseded bulletins, or documents adjuster decisions. Compliance with NAIC Model Laws is necessary but not sufficient for any of the RAII-derived defect classes.

***

## Structural Comparison

| Model | Publisher | Scope | Levels/Stages | CMMI-Derived? | Policy Smells Coverage | Claims Smells Coverage |
|---|---|---|---|---|---|---|
| ACORD Digital Maturity Study | ACORD | Digital capability, technology adoption | 5 levels | No | Minimal (Spec-Code Divergence indirectly) | Minimal |
| RIMS Risk Maturity Model | RIMS | Enterprise risk management | 5 levels | Yes (explicitly CMM-based)[^7] | None directly | Root cause loop only |
| iDAMM | Datos Insights (Aite-Novarica) | Data & analytics capability | 3 stages | No | Data governance overlap | None directly |
| Underwriting Maturity Framework | Send Technology | Underwriting workflow automation | 5 stages | No | Rating rule smells partially | None |
| NAIC Model Laws | NAIC | Regulatory compliance minimums | Binary (compliant/non-compliant) | No | Regulatory mapping only | Bad faith exposure floor |

***

## The Gap

Taken together, these five models cover digital capability, enterprise risk governance, data analytics maturity, underwriting automation, and regulatory compliance. None of them covers the **policy-to-claims quality lifecycle as a process engineering problem**.[^5][^6]

Specifically, no existing model addresses:

- **Form and wording quality** — the 14 Form & Wording Smells (God Clause, Circular Definition, Semantic Drift, etc.) are invisible to every framework above.
- **Rating rule governance** — *Magic Rating Factor*, *Calculation Rule Drift*, and *Dead Rating Rule* are not assessed by any current model.
- **Regulatory mapping traceability** — the 10 Regulatory Mapping Smells (Null Reference Clause, Referential Drift, Unversioned Statutory Reference, etc.) fall through every framework.
- **Spec-to-configurator fidelity** — no model measures whether the written policy spec and the system implementation agree.
- **Claims adjudication process quality** — *Hidden State in Adjuster Notes*, *No Coverage Decision Log*, *Blob Adjuster*, and the entirety of the adjuster workflow smells are outside every existing framework's scope.
- **The upstream-to-downstream feedback loop** — no model tracks how upstream policy smells generate downstream claims failures and requires a remediation cycle.

The RIMS RMM is the only existing model with structural CMMI heritage, but its seven attributes are scoped to enterprise risk management culture and governance rather than product manufacturing quality. The closest analogue in healthcare — HIMSS's Digital Maturity Models, which use an eight-stage system to evaluate digital health transformation including clinical processes — suggests that insurance could support a comparable domain-specific operational quality framework.[^8][^18][^7]

***

## Implications for a Legal Tech Debt Platform

The absence of a comprehensive operational quality maturity model in insurance is both the competitive gap and the design requirement. A platform that scores carriers against a CMMI-structured progression — using the RAII-derived defect taxonomy as the detection mechanism and the 83-smell policy/claims catalog as the evidence base — would occupy territory that no existing framework covers.

The closest structural template is the RIMS RMM (CMM-based, seven attributes, five levels, readiness indicators), but applied to **product governance quality** rather than enterprise risk management. The iDAMM's three-stage model is too coarse; the ACORD study is annual and retrospective rather than diagnostic; the underwriting framework is vendor-scoped and automation-focused; NAIC is a compliance floor with no improvement pathway.

A maturity scoring function that maps smell density by category to CMMI level equivalents would produce output that none of these models currently generate: a quantified, actionable assessment of how far an insurer's policy and claims operations are from governed, process-mature, defect-preventable practice.

---

## References

1. [ACORD report highlights profitability gap driven by digital execution ...](https://www.reinsurancene.ws/acord-report-highlights-profitability-gap-driven-by-digital-execution-among-global-insurers/) - ACORD divides insurers into five maturity levels. At the top are Digital Competitors, which ACORD de...

2. [ACORD 2026 Insurance Digital Maturity Study: 7% of World's ...](https://finance.yahoo.com/sectors/healthcare/articles/acord-2026-insurance-digital-maturity-130000994.html) - Each of the insurers studied was segmented into one of five categories based on the level of digital...

3. [ACORD's 2025 Insurance Digital Maturity Study Finds That Only a ...](https://www.prnewswire.com/news-releases/acords-2025-insurance-digital-maturity-study-finds-that-only-a-quarter-of-top-insurers-have-truly-digitalized-302393952.html) - The study found that only one quarter have truly digitalized the value chain, while more than 10% ar...

4. [Revealed – $480 billion could be saved by carriers](https://www.insurancebusinessmag.com/us/news/technology/revealed--480-billion-could-be-saved-by-carriers-527615.aspx) - ACORD's analysis also found that organizations with higher digital maturity levels generate greater ...

5. [insurance_policy_smells-2.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/169632472/73397365-afdf-40d8-815a-4d98bbaff912/insurance_policy_smells-2.md?AWSAccessKeyId=ASIA2F3EMEYEQI323D7Q&Signature=NBzE4T40FfjB1p3wHCG4sjxD7Wc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJHMEUCICGlgDAc2DfX9JpTTPZ09QpdJLOQrQBAYAf3TfE4jq8OAiEAjijfn%2BRYJzw9WO%2B3pUG0Cp3qIDnbf1LaeFFxSSP7cqYq%2FAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDK%2BZgf%2FzSmJOP6nDWirQBJBjfTgwGak04vQX3nRjz%2FpDZq2CNdYa1FFSdVrXsDBz%2BD2KZRF1Ns%2B3o2AyuS4MDvKVb8tdmSPLVeDTbgCCTiWAW834QXObpDxXnRn%2BXxZR%2F%2B5RSAjugOdT0Ri5JuR4%2FIf04GG8D0mmttwwk%2BCtNa3mTYYfEFFXBZVILU0DJMFL0WXn1u3xltapHUQvNwQM7c7XDGliAFVx%2FA39SBIq9tEES4ir%2FQZPZLCFGO3bmTKCIHYHNIkUM50C%2BrACu9%2BrFDcRkyjHbPuD9c%2BPNLgubd0973%2F0igVD07tn9leVWfwFUKGO2dn07wkqqSEKUupACUZLLqGr%2B1w6%2BgLazIPD7P2nkQELGyWecShKxOpDba%2FXLovIzZsoQQ4GPS5dcEsOhFKe04O6EhynmsCwUll66u4TMEWjGpiNIYhr9uVbbEUGV5vc9PPJaUCu3M6ypl73ba642jIA0PoNXCBEF1BiiB8t5ZUDZIJDAy9KWNSPAVRcFoVMcWr6Ba5wMpLOewFNHU09p7vbhrZSpYjCafV6Sb8MDs75fovCz7A02jMK4xVksPhEtyvDS9uYw6jAUnQjequODl9E7hFE6Vizgid%2B7UYLSWhCxBB%2BNQWSK7n8%2FzJnI4vWYye1GGw%2Fuq8Wtz1242gBMScTbhnulir%2B4LiGW4mZvaJsDqUcO%2BmyCL1cmPcMAkDyc9Kq0RXflmKn5afvxg7fjNIHiaETVdvIlIix0UMJgTMhw%2FHmS%2BKTIKn9jYFsXuFyERQJO3AkdWEXrs7XkOwQO71nTu9XpZ6HqNpkPH8w3aXn0AY6mAGVf8H4o6%2F2%2FGpldC5kxWX3FoIft8nJqeN%2Flrq1zf%2FdKod8%2FTYGZrEIrPKky6rKImiRTjsCau5bH1KrFkCtMHgiVpCQmDwmDsA8L57QWgC0V9rNPTnt4WoNlaZ6d7Rtb01In67ZbvJhzxir5Vsep0YoAx8NG7DXYM1a%2F1TYlVHSOmFy1GGFRpIWhbtTPAOAuGZcR09CRUKfaQ%3D%3D&Expires=1780080816) - # Insurance Policy Smells
*Legal Code Smells specific to the Policy Specification, Drafting, Rating,...

6. [insurance_claims_smells.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/169632472/fb298dd6-12a5-42f2-84fa-cb14d9064552/insurance_claims_smells.md?AWSAccessKeyId=ASIA2F3EMEYEQI323D7Q&Signature=8wC3zfTKOy637Of%2FA4Vf6VscCHY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJHMEUCICGlgDAc2DfX9JpTTPZ09QpdJLOQrQBAYAf3TfE4jq8OAiEAjijfn%2BRYJzw9WO%2B3pUG0Cp3qIDnbf1LaeFFxSSP7cqYq%2FAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDK%2BZgf%2FzSmJOP6nDWirQBJBjfTgwGak04vQX3nRjz%2FpDZq2CNdYa1FFSdVrXsDBz%2BD2KZRF1Ns%2B3o2AyuS4MDvKVb8tdmSPLVeDTbgCCTiWAW834QXObpDxXnRn%2BXxZR%2F%2B5RSAjugOdT0Ri5JuR4%2FIf04GG8D0mmttwwk%2BCtNa3mTYYfEFFXBZVILU0DJMFL0WXn1u3xltapHUQvNwQM7c7XDGliAFVx%2FA39SBIq9tEES4ir%2FQZPZLCFGO3bmTKCIHYHNIkUM50C%2BrACu9%2BrFDcRkyjHbPuD9c%2BPNLgubd0973%2F0igVD07tn9leVWfwFUKGO2dn07wkqqSEKUupACUZLLqGr%2B1w6%2BgLazIPD7P2nkQELGyWecShKxOpDba%2FXLovIzZsoQQ4GPS5dcEsOhFKe04O6EhynmsCwUll66u4TMEWjGpiNIYhr9uVbbEUGV5vc9PPJaUCu3M6ypl73ba642jIA0PoNXCBEF1BiiB8t5ZUDZIJDAy9KWNSPAVRcFoVMcWr6Ba5wMpLOewFNHU09p7vbhrZSpYjCafV6Sb8MDs75fovCz7A02jMK4xVksPhEtyvDS9uYw6jAUnQjequODl9E7hFE6Vizgid%2B7UYLSWhCxBB%2BNQWSK7n8%2FzJnI4vWYye1GGw%2Fuq8Wtz1242gBMScTbhnulir%2B4LiGW4mZvaJsDqUcO%2BmyCL1cmPcMAkDyc9Kq0RXflmKn5afvxg7fjNIHiaETVdvIlIix0UMJgTMhw%2FHmS%2BKTIKn9jYFsXuFyERQJO3AkdWEXrs7XkOwQO71nTu9XpZ6HqNpkPH8w3aXn0AY6mAGVf8H4o6%2F2%2FGpldC5kxWX3FoIft8nJqeN%2Flrq1zf%2FdKod8%2FTYGZrEIrPKky6rKImiRTjsCau5bH1KrFkCtMHgiVpCQmDwmDsA8L57QWgC0V9rNPTnt4WoNlaZ6d7Rtb01In67ZbvJhzxir5Vsep0YoAx8NG7DXYM1a%2F1TYlVHSOmFy1GGFRpIWhbtTPAOAuGZcR09CRUKfaQ%3D%3D&Expires=1780080816) - # Insurance Claims Smells
*Legal Code Smells specific to the Claims Handling, Adjudication, and Reso...

7. [Risk Maturity Model FAQ - RIMS](https://www.rims.org/resources/strategic-enterprise-risk-center/risk-maturity-model-faq) - The RIMS RMM model consists of 68 key readiness indicators that describe twenty-five competency driv...

8. [RIMS Risk Maturity Model Launched for ERM | Nov 28, 2006](https://www.logicmanager.com/resources/news/rims-launches-risk-maturity-model-for-enterprise-risk-management/) - The seven drivers for the systematic progression of levels are termed as “Attributes” and include va...

9. [RIMS ERM Maturity Model | Enterprise Risk Management Initiative](https://erm.ncsu.edu/resource-center/rmm-for-erm/) - The RIMS Risk Maturity Model identifies seven key attributes for effective Enterprise Risk Managemen...

10. [Elevate Your Business with a Risk Management Maturity Model](https://bryghtpath.com/risk-management-maturity-model/) - The Five Levels of the Risk Management Maturity Model · Enhanced Decision-Making · Proactive Risk Ma...

11. [Introducing the Insurance Data & Analytics Maturity Model](https://datos-insights.com/blog/introducing-the-insurance-data-analytics-maturity-model/) - Data is an arms race. Competitive pressures, internal demands, and an ever-growing pool of data are ...

12. [The Need to Improve Data Maturity | Insurance Thought Leadership](https://www.insurancethoughtleadership.com/data-analytics/need-improve-data-maturity) - The True Meaning of “Data Maturity”. Aite-Novarica Group has developed the Insurance Data and Analyt...

13. [Introducing the Underwriting Maturity Framework - Send Technology](https://send.technology/resources/blog/introducing-the-underwriting-maturity-framework/) - We've created our Underwriting Maturity Framework to help carriers identify characteristics of each ...

14. [Take The Quiz & Discover Your Organisation's Underwriting Maturity ...](https://innovate.send.technology/send-underwriting-maturity-framework) - This allows for deeper underwriting insights to better inform risk selection, exposure analysis and ...

15. [Send Joins International Underwriting Association to Drive Market ...](https://send.technology/resources/blog/send-joins-international-underwriting-association/) - One of Send's first initiatives will be to explain to IUA members the five stages of the Underwritin...

16. [Understanding the NAIC Insurance Data Security Model Law](https://rsmus.com/insights/services/risk-fraud-cybersecurity/understanding-the-naic-insurance-data-security-model-law.html) - The NAIC's model law establishes a legal framework for requiring insurance organizations to operate ...

17. [Model Laws - NAIC](https://content.naic.org/model-laws) - This comprehensive publication provides quick access to every NAIC Model Law, Regulation, and Guidel...

18. [Explore Digital Maturity Models for Healthcare | HIMSS](https://www.himss.org/maturity-models/) - From analytics to infrastructure, our eight-stage maturity models support every part of your digital...

