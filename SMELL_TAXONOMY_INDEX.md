# Complete Legal Code Smell Taxonomy Index

**Status**: Master index of 159 documented legal code smells across three specialized taxonomies.

This file is a reference landing page. For detailed specifications, see the individual taxonomy documents.

---

## Quick Links to All Taxonomies

| Document | Scope | Smell Count |
|---|---|---|
| [legal_code_smell_taxonomy.md](legal_code_smell_taxonomy.md) | Cross-domain legal/regulatory patterns | **74** |
| [insurance_policy_smells.md](insurance_policy_smells.md) | Policy specification, drafting, rating, underwriting | **43** |
| [insurance_claims_smells.md](insurance_claims_smells.md) | Claims handling, adjudication, resolution, bad faith exposure | **41** |
| **TOTAL** | **All legal code smells in the system** | **159** |

---

## Operationalization Status

| Status | Count | Details |
|---|---|---|
| **Operationalized (Detectors Exist)** | **5** | Five Kentucky homeowners policy-layer smells from Sandbox 002 have detection specs and Gherkin scenarios |
| **Specification Ready** | **~110+** | Additional smells documented and ready for detector development |
| **Total Smells** | **159** | All smells across the three taxonomies |

**Currently Detected Findings (Sandbox 002)**: 31 findings from the five operationalized smells.

---

## Taxonomy 1: Legal Code Smell Taxonomy (74 patterns)

**Source**: [legal_code_smell_taxonomy.md](legal_code_smell_taxonomy.md)

**Categories:**

| Category | Count | Examples |
|---|---|---|
| 1. Structural Smells | 9 | Shotgun Clause Surgery, God Clause, Circular Reference, Dead Clause, Orphan Definition |
| 2. Semantic Smells | 9 | Magic Number Term, Undefined Behavior Clause, Non-deterministic Language, Contradictory Conditions, Coverage Inversion |
| 3. Dependency Smells | 6 | External Hardcoding, Unversioned Reference, Broken Link / Null Reference, Cyclic Dependency |
| 4. Legislative Drift / Bureau Change Smells | 10 | Schema Drift, Referential Drift, Calculation Rule Drift, Filing Dependency, Sunset Clause Smell |
| 5. Logic and Flow Smells | 7 | Order Sensitivity, Short-Circuiting Ambiguity, Overbroad Exclusion, Inconsistent Jurisdictional Logic |
| 6. Maintainability Smells | 6 | Lack of Traceability, Manual Synchronization, Legal Debt Clause, Version Drift |
| RAII Defect Classes | 7 | Structural/systemic defect patterns |
| **Subtotal** | **74** | |

---

## Taxonomy 2: Insurance Policy Smells (43 patterns)

**Source**: [insurance_policy_smells.md](insurance_policy_smells.md)

**Sections:**

| Section | Count | Scope |
|---|---|---|
| 1. Form & Wording Smells | 14 | Policy document language, coverage terms, clause structure |
| 2. Rating & Underwriting Rule Smells | 11 | Rating tables, rule engines, underwriting guidelines |
| 3. Regulatory Mapping Smells | 10 | Connections to statutes, bulletins, and regulatory filings |
| 4. Spec-to-Configurator Traceability Smells | 8 | Handoff from spec to policy admin system / configurator code |
| **Subtotal** | **43** | |

**Five Operationalized Smells** (with Sandbox 002 detectors):
- Overbroad / Non-Deterministic Exclusions (Phish 1)
- Magic Number / Magic Valuation Terms (Phish 2)
- Coverage Inversion / Contradictory Conditions (Phish 3)
- Calculation Rule Drift / Unversioned Rate Reference (Phish 4)
- Regulatory Mapping Smells (Phish 5)

---

## Taxonomy 3: Insurance Claims Smells (41 patterns)

**Source**: [insurance_claims_smells.md](insurance_claims_smells.md)

**Sections:**

| Section | Count | Scope |
|---|---|---|
| 1. Coverage Determination Smells | 9 | How an adjuster determines if a loss is covered |
| 2. Valuation & Payment Smells | 8 | Calculating what is owed; payment logic |
| 3. Notice & Procedure Smells | 6 | Procedural obligations in claims process |
| 4. Adjuster Workflow & Decision Smells | 8 | Claims handling processes independent of policy wording |
| 5. Subrogation & Recovery Smells | 4 | Recovery lifecycle after a claim is paid |
| 6. Regulatory & Bad Faith Exposure Smells | 6 | Regulatory and litigation risk in claims handling |
| **Subtotal** | **41** | |

---

## Why Three Taxonomies?

**Legal Code Smell Taxonomy (74)**
- Cross-domain patterns applicable to any legal or regulatory document
- Foundational language for discussing defects
- Analogies to software code smells where relevant

**Insurance Policy Smells (43)**
- Specialized to policy specification, drafting, rating, underwriting
- Organized by lifecycle stage (spec → configurator → deployment)
- Detectable at requirements, filing, and audit time

**Insurance Claims Smells (41)**
- Specialized to claims handling and adjudication
- Organized by decision point (coverage → valuation → procedure → adjuster workflow → recovery)
- Detectable after a loss event
- Many are **inherited** from upstream policy smells

---

## Claims ↔ Policy Feedback Loop

Many claims smells originate as upstream policy smells:

| Policy Smell | Claims Symptom |
|---|---|
| Circular Definition | Coverage Determination paralysis |
| Magic Number Term | Notice / valuation dispute |
| Overbroad Exclusion | Bad faith denial |
| Calculation Rule Drift | Systematic underpayment |
| Non-deterministic Language | Inconsistent adjuster decisions |

A **recurring claims smell** is a signal to scan the policy layer upstream for the corresponding policy smell.

---

## Next Steps: Detector Development

**Current focus (Sandbox 002)**: Five policy-layer smells have operationalized detectors.

**Available for future work (~110+ smells)**:
- All claims-layer smells (41 patterns)
- Additional structural, dependency, and maintainability smells (20+ patterns)
- All regulatory/legislative drift smells (10 patterns)
- Cross-category analysis (ranking ROI, detectability, frequency)

To start detecting additional smells:

1. Select a smell or category from this index
2. Review the specification in the source document
3. Write detection logic (heuristics, regex, or graph traversal)
4. Test against the Kentucky homeowners corpus or applicable source set
5. Document findings and false-positive handling

---

## Reference

For complete documentation, see:
- [BOOTSTRAP.md](BOOTSTRAP.md) - Startup documentation with smell inventory references
- [README.md](README.md) - Current project state and evidence inventory
- [AGENT_CONTEXT.json](AGENT_CONTEXT.json) - Compact current state for agents
