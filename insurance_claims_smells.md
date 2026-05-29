# Insurance Claims Smells
*Legal Code Smells specific to the Claims Handling, Adjudication, and Resolution lifecycle*
*Derived from original research — P&C domain*

---

## Overview

These smells occur **after a loss event** — in how coverage is determined, how claims are
investigated, how payments are calculated, and how disputes are resolved. Many originate
upstream (in policy wording or regulatory mapping) but only **surface at claims time**,
making them expensive and sometimes legally dangerous by the time they are discovered.

Claims smells fall into two broad types:
- **Inherited smells** — originated in policy/spec, exposed by the claims event
- **Native smells** — introduced by claims processes, workflows, and systems themselves

---

## Section 1: Coverage Determination Smells
*Problems that arise when an adjuster tries to determine whether a loss is covered.*

| Smell | Description | Risk |
|---|---|---|
| **Coverage Inversion (Inherited)** | Adjuster reads the policy as broad; exclusions actually eliminate the claim | Bad faith exposure, E&O |
| **Circular Coverage Definition** | "Covered loss means a loss that is covered" — adjuster cannot make a deterministic decision | Escalation, litigation |
| **Undefined Concurrent Causation** | Two perils contribute to a loss (e.g., wind + flood); policy is silent on how to apportion | Coverage dispute, litigation |
| **Magic Number Ambiguity** | "Prompt notice," "reasonable time," "substantial damage" — no defined threshold | Insured claims late; carrier disputes; bad faith risk |
| **Non-deterministic Exclusion** | Exclusion uses "arising out of" or "related to" without a defined scope boundary | Adjuster discretion = inconsistent outcomes |
| **Overlapping Exclusion Conflict** | Two exclusions apply to the same loss but imply different outcomes | Coverage dispute, litigation |
| **Silent Coverage Gap** | A plausible loss scenario is simply not addressed anywhere in the policy | Denied claim, customer complaint, regulatory complaint |
| **Zombie Coverage** | A coverage that was meant to be removed via endorsement but still exists due to form error | Unintended payout or unintended denial |
| **Overbroad Exclusion Applied** | Carrier applies a broad exclusion ("governmental action") beyond its original scope | Bad faith, regulatory action |

---

## Section 2: Valuation & Payment Smells
*Problems in calculating what is owed once coverage is confirmed.*

| Smell | Description | Risk |
|---|---|---|
| **Calculation Rule Drift (Inherited)** | Policy says ACV; the calculation method in claims system uses a formula that has drifted from the filed definition | Systematic underpayment, class action |
| **Magic Valuation Term** | "Actual Cash Value," "Replacement Cost," "Fair Market Value" used without a defined calculation methodology | Inconsistent payouts, dispute |
| **Undefined Depreciation Logic** | Policy allows depreciation but doesn't specify method (straight-line, age-condition, etc.) | Insured disputes every claim |
| **Stale Pricing Reference** | Claims system references a cost database (e.g., Marshall & Swift) with no version lock | Payouts based on outdated rebuild costs |
| **Coverage Sublimit Ambiguity** | Multiple sublimits apply to the same item (e.g., jewelry under personal property AND a scheduled items rider) | Double-counting or gap |
| **Currency / Unit Drift** | Policy wording says "per occurrence" but claims system calculates "per item" or "per structure" | Systematic exposure miscalculation |
| **Non-Executable Payment Condition** | Payment conditioned on something practically impossible (e.g., approval by an agency that no longer exists) | Payment delayed indefinitely |
| **Missing Escalation Path** | No defined process when valuation is disputed — policy is silent | Informal resolutions, inconsistency, litigation |

---

## Section 3: Notice & Procedure Smells
*Problems with the procedural obligations in the claims process.*

| Smell | Description | Risk |
|---|---|---|
| **InvariantViolation — Notice** | Policy requires written notice within N days; claims system doesn't track or enforce this | Carrier waives a defense inadvertently |
| **InvariantViolation — Payment Deadline** | State law requires payment within X days of proof of loss; no system-enforced trigger | Regulatory violation, interest penalties |
| **Sunset Obligation Smell** | A COVID-era or emergency notice waiver is still active in the claims workflow | Wrong procedure being applied to current claims |
| **Procedural Dependency (Inherited)** | Policy requires mediation before a board or panel that no longer exists | Claims stuck with no path to resolution |
| **Unversioned Proof-of-Loss Form** | Claims system still uses a version of the proof-of-loss form that has been superseded by DOI | Filing invalid, claim restarted |
| **Jurisdictional Inheritance in SIU** | Special Investigations Unit uses a single fraud indicator model regardless of state; some indicators are only valid in certain jurisdictions | False positives, discriminatory denial risk |

---

## Section 4: Adjuster Workflow & Decision Smells
*Problems introduced by the claims handling process itself, independent of policy wording.*

| Smell | Description | Risk |
|---|---|---|
| **Hidden State in Adjuster Notes** | Coverage decision logic lives in free-text notes, not in a structured decision record | Not auditable, not reproducible |
| **Blob Adjuster** | One adjuster handles coverage determination, valuation, negotiation, AND payment approval with no separation | Control failure, bias risk |
| **No Coverage Decision Log** | Decision to deny (or pay) is not linked to the specific policy language and obligation it implements | Cannot defend in litigation |
| **Implicit Escalation Default** | When a claim exceeds a threshold, it "goes to a supervisor" — but no documented decision authority matrix | Inconsistent outcomes at margin |
| **Manual Sync — Reserves vs. Payments** | Reserve system and payment system are maintained separately; manual reconciliation required | Reserve inadequacy, financial reporting error |
| **Dead Workflow Step** | A required step (e.g., "submit to re-insurance desk") exists in the workflow but the re-insurance treaty was cancelled | Phantom step slowing claims |
| **Orphan Denial Reason Code** | Adjuster selects a denial code that references a policy provision no longer in the current form | Denial legally indefensible |
| **Parse-and-Pray Documentation** | Claim file documentation written assuming a specific format or completeness that field reports never actually achieve | Gaps in file; defense exposure |

---

## Section 5: Subrogation & Recovery Smells
*Problems in the recovery lifecycle after a claim is paid.*

| Smell | Description | Risk |
|---|---|---|
| **Unversioned Subrogation Clause** | Subrogation rights clause references state law with no version; law has changed | Rights inadvertently waived or overclaimed |
| **Missing Statute of Limitations Trigger** | No system-enforced tracking of subrogation filing deadlines per jurisdiction | Rights lapse silently |
| **Jurisdictional Inheritance in Recovery** | Same recovery strategy applied across all states regardless of comparative fault rules | Invalid recovery attempts, legal cost |
| **Dead Recovery Path** | Policy still references a salvage process that the company discontinued | Salvage value left on the table |

---

## Section 6: Regulatory & Bad Faith Exposure Smells
*Patterns that create regulatory or litigation risk in claims handling.*

| Smell | Description | Risk |
|---|---|---|
| **Non-deterministic Denial** | Denial letter uses boilerplate without citing the specific policy provision or obligation | Regulatory complaint trigger, bad faith |
| **Loophole Leakage in Denial** | Ambiguous exclusion language is applied inconsistently across similar claims | Class action, disparate treatment claim |
| **Lack of Coverage Test Logging** | No record of which coverage tests were run and what result each produced | Cannot reconstruct decision in litigation |
| **Regulatory Drift in Claim Handling** | State DOI updated its claim handling standards; claims workflow not updated to match | Systematic regulatory violation |
| **Zombie Denial Reason** | A denial based on a policy provision that was removed in a subsequent endorsement or renewal | Legally invalid denial |
| **Time-Based Logic Leak in Bad Faith** | "We will respond promptly" — no defined SLA, no system enforcement, no audit trail | Statutory bad faith claim |

---

## Summary

| Section | Smell Count |
|---|---|
| 1. Coverage Determination | 9 |
| 2. Valuation & Payment | 8 |
| 3. Notice & Procedure | 6 |
| 4. Adjuster Workflow & Decision | 8 |
| 5. Subrogation & Recovery | 4 |
| 6. Regulatory & Bad Faith Exposure | 6 |
| **Total** | **41** |

---

## Claims ↔ Policy Feedback Loop

Many claims smells are **symptoms of upstream policy smells**. A complete legal tech debt
system would close this loop:

```
Policy Smell (upstream)          → Claims Symptom (downstream)
-------------------------------     --------------------------------
Circular Definition              → Coverage Determination paralysis
Magic Number Term                → Notice / valuation dispute
Overbroad Exclusion              → Bad faith denial
Calculation Rule Drift           → Systematic underpayment
Silent Coverage Gap              → Customer complaint / regulatory action
Non-deterministic Language       → Inconsistent adjuster decisions
InvariantViolation (policy)      → InvariantViolation (claims deadline)
Zombie Coverage                  → Unintended payout or denial
```

A claims smell that keeps recurring is a signal to run a **policy-layer smell scan** upstream.
This is the feedback channel that eventually makes the legal tech debt system self-improving.

---

*See companion document: Insurance Policy Smells.*
*These smells are detectable at: claims audit, SIU review, litigation analysis,*
*regulatory market conduct examination, and AI-assisted claim file review.*

