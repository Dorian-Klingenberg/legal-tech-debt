# KRS/KAR Definitional Audit — Smell 2 Flagged Terms

Date: 2026-06-05
Scope: BACKLOG-007
Reviewer: Claude Code (automated search) + human review pending
Source: Regulatory corpus nodes from run `18b0dec5` (73 nodes, sources KY-KRS-*, KY-KAR-*, KY-DOI-*)
Node: `6715f59035644bcc` (KY-KAR-806-12-095, single parsed node)

---

## Purpose

Check whether any of the terms flagged by Smell 2 detectors are **formally defined** in the
Kentucky regulatory corpus. If a statutory or regulatory definition exists, carriers can rely
on it without restating the definition in the filing — which would reduce the severity of the
corresponding Smell 2 findings.

---

## Search Method

For each flagged term, searched all 73 regulatory corpus nodes (KY-KRS-*, KY-KAR-*, KY-DOI-*)
for the term within a 300-character window that also contains a definitional marker
("means", "is defined", "shall mean", "defined as", "as defined", "is construed", "refers to").

---

## Results

### Term: "reasonable time"

| | |
|---|---|
| **Hits** | 1 |
| **Definitional hits** | 0 |
| **Source** | KY-KAR-806-12-095 |
| **Context** | Used in fraud-investigation context: "a reasonable basis, which shall be supported by specific information available for review by the commissioner, that a claimant has fraudulently caused..." |
| **Verdict** | **NOT DEFINED** in Kentucky statutes or regulations for loss settlement timing. |

**Severity implication for SMELL2-H001:** Severity remains HIGH. No statutory definition
insulates carriers from the ambiguity. A claimant cannot determine when "reasonable time"
expires to trigger the ACV-vs-replacement-cost switch in a roof loss settlement.

---

### Term: "actual cash value"

| | |
|---|---|
| **Hits** | 6 |
| **Definitional hits** | 0 (no "means" / "is defined" within window) |
| **Source** | KY-KAR-806-12-095 |
| **Key regulatory text** | Section 9(2)(a): *"If the insurance policy provides for the adjustment and settlement of losses on an actual cash value basis on residential fire and extended coverage, the insurer **shall determine actual cash value as follows: replacement cost of property at the time of the loss less depreciation, if any.** If provided for in the policy, depreciation **may include** the costs of goods, materials, labor, equipment, overhead and profit, taxes, fees, and services necessary to replace, repair, or rebuild the damaged property. If requested by the insured, the insurer shall provide a copy of the claim file worksheets showing any and all deductions for depreciation."* |
| **Node ID** | `6715f59035644bcc` |
| **Section path** | KY-KAR-806-12-095 > Unfair claims settlement practices |
| **Verdict** | **NOT formally defined** (no "means" formulation), but **Section 9(2)(a) establishes a mandatory calculation standard** for residential fire and extended coverage policies. |

**Critical finding — STRENGTHENS H003, not weakens it:**

806 KAR 12:095 Section 9(2)(a) establishes two mandatory rules:

1. **ACV must be calculated as replacement cost minus depreciation.** This is a regulatory
   floor, not carrier discretion.

2. **Labor depreciation requires explicit policy authorization.** The phrase "if provided for
   in the policy, depreciation **may include**... labor" means labor may only be depreciated
   when the policy text expressly authorizes it. A carrier applying labor depreciation without
   a clear policy provision permitting it may be violating this regulation.

This directly bears on the KFBM H003 finding: KFBM's 7-year ACV roof rule applies ACV
settlement without disclosing (a) whether labor is included in depreciation, and (b) what
calculation method or schedule is used. Under 806 KAR 12:095 Section 9(2)(a), if KFBM is
depreciating labor, the policy must say so explicitly. If the policy does not say so, the
practice may not be permissible regardless of the ACV settlement designation.

**Recommended enhancement to H003 reviewer question:** Add reference to 806 KAR 12:095
Section 9(2)(a) — ask whether the filing explicitly authorizes labor depreciation as required
by that section.

---

### Term: "replacement cost"

| | |
|---|---|
| **Hits** | 4 |
| **Definitional hits** | 0 |
| **Source** | KY-KAR-806-12-095 |
| **Context** | Used in Section 9(1) — replacement cost coverage standards (matching rule, betterment prohibition) — and in Section 9(2)(a) as the basis for the ACV calculation. Not independently defined. |
| **Verdict** | **NOT DEFINED** in Kentucky statutes or regulations. Used as a term of art without definition. |

**Severity implication for SMELL2-H003 (replacement cost variant):** Severity remains
HIGH/MEDIUM. No statutory definition provides a safe harbor for carriers. The ACV calculation
standard in Section 9(2)(a) implies replacement cost is determinable but does not define the
methodology for determining it.

---

### Term: "market value"

| | |
|---|---|
| **Hits** | 4 |
| **Definitional hits** | 0 |
| **Source** | KY-KAR-806-12-095 |
| **Context** | Used in motor vehicle total-loss context (fair market value of vehicle). Not used in homeowners property loss context. |
| **Verdict** | **NOT DEFINED** for homeowners property. All regulatory uses are in the auto/motor vehicle context. |

**Severity implication for SMELL2-H003 (market value variant):** Severity remains
MEDIUM. Context of regulatory use is auto — does not provide a definition applicable to
homeowners property valuations.

---

### Term: "depreciation"

| | |
|---|---|
| **Hits** | 5 |
| **Definitional hits** | 0 |
| **Source** | KY-KAR-806-12-095 |
| **Context** | Used in Section 9(2)(a) — ACV calculation requires deducting depreciation; insurer must provide claim file worksheets showing "any and all deductions for depreciation." Also Section 9(2)(a) permits labor depreciation "if provided for in the policy." |
| **Verdict** | **NOT DEFINED** (no formula or enumeration). Regulatory text establishes that: (a) depreciation is deducted from replacement cost to get ACV; (b) labor may be included in depreciation only if the policy provides for it; (c) the insurer must document all depreciation deductions on request. |

**Severity implication:** Depreciation methodology is a regulatory compliance matter under
806 KAR 12:095 Section 9(2)(a). Undisclosed or unauthorized depreciation practices (especially
labor depreciation without explicit policy authorization) are not merely an undefined-term
smell — they may constitute a regulatory violation.

---

## Summary Table

| Term | Formally Defined? | Regulatory Standard Exists? | Effect on Finding Severity |
|---|---|---|---|
| reasonable time | No | No | H001 severity unchanged — HIGH |
| actual cash value | No (no "means" formulation) | Yes — 806 KAR 12:095 § 9(2)(a): RC minus depreciation | H003 STRENGTHENED — labor depreciation requires explicit policy authorization |
| replacement cost | No | Referenced but not defined | H003 severity unchanged — HIGH/MEDIUM |
| market value | No | Auto context only | H003 severity unchanged — MEDIUM |
| depreciation | No | Yes — insurer must document; labor requires policy authorization | H003 STRENGTHENED — same basis as ACV |

---

## Recommended Actions

### 1. Update H003 reviewer question and rationale (smell2.py)

Add explicit citation to 806 KAR 12:095 Section 9(2)(a) in the H003 rationale and reviewer
question. The question should now ask:

- Does the filing explicitly authorize labor depreciation as required by 806 KAR 12:095
  Section 9(2)(a)?
- If ACV settlement applies to roof losses, does the filing document the calculation method
  consistent with the regulatory standard (replacement cost minus depreciation)?

### 2. Note in drill-down entry S4-H003-KFBM-001

The 806 KAR 12:095 Section 9(2)(a) finding materially strengthens the H003 drill-down entry.
It transforms the finding from "methodology not disclosed" to "methodology not disclosed AND
labor depreciation may lack the required policy authorization under Kentucky regulation."
This should be added to the regulatory citations and rationale section of that entry.

### 3. No severity downgrade warranted

No finding in the current corpus should be downgraded based on this audit. No term is
formally defined in a way that would insulate a carrier from ambiguity. The 806 KAR
Section 9(2)(a) standard strengthens existing findings rather than reducing them.

### 4. Deferred: graph-lookup enrichment

The longer-term implementation from BACKLOG-007 — wiring this as a graph-lookup enrichment
that automatically cross-references Smell 2 findings against regulatory corpus nodes — remains
open. The audit establishes that such enrichment would RAISE rather than lower confidence
on ACV/depreciation findings, and would ADD a citation to 806 KAR 12:095 Section 9(2)(a).
Design a Stage 007 enrichment pass when ready.

---

## Regulatory Text (verbatim)

**806 KAR 12:095, Section 9(2)(a)** — Standards for Prompt, Fair, and Equitable Settlements
Applicable to Fire-and-Extended-Coverage-Type Policies with Replacement Cost Coverage:

> "If the insurance policy provides for the adjustment and settlement of losses on an actual
> cash value basis on residential fire and extended coverage, the insurer shall determine
> actual cash value as follows: replacement cost of property at the time of the loss less
> depreciation, if any. If provided for in the policy, depreciation may include the costs of
> goods, materials, labor, equipment, overhead and profit, taxes, fees, and services necessary
> to replace, repair, or rebuild the damaged property. If requested by the insured, the insurer
> shall provide a copy of the claim file worksheets showing any and all deductions for
> depreciation."

Node ID: `6715f59035644bcc` | Source: `KY-KAR-806-12-095` | Run: `18b0dec5`
