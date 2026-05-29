# Insurance Policy Smells
*Legal Code Smells specific to the Policy Specification, Drafting, Rating, and Underwriting lifecycle*
*Derived from original research — Kentucky Home/Farmowners & P&C domain*

---

## Overview

These smells occur **before and during the binding of a policy** — in the spec, form wording, rating rules,
underwriting guidelines, and the regulatory mapping that underpins them. They are detectable at
requirements time, spec review, configurator build, and pre-filing audit.

---

## Section 1: Form & Wording Smells
*Problems in the policy document itself — the ISO form, manuscript form, or endorsement language.*

| Smell | Description | Where It Hurts |
|---|---|---|
| **God Clause** | "Notwithstanding any other provision herein…" clause that silently overrides everything else | Claims disputes, coverage litigation |
| **Nested Exception Hell** | Coverage exists except as in (a) except as in (b)(ii) except... | Underwriter confusion, claims misapplication |
| **Circular Definition** | "Occurrence means an event; an event means an occurrence" | Adjuster paralysis, coverage gaps |
| **Orphan Definition** | Term defined in the Definitions section but never used in the body | Dead weight, potential for exploitation |
| **Semantic Drift** | "Occurrence," "event," and "incident" used interchangeably across endorsements | Inconsistent claims outcomes across adjusters |
| **Magic Number Term** | "Within a reasonable time," "customary fee," "appropriate notice" — undefined thresholds | Disputes, bad faith exposure |
| **Coverage Inversion** | Policy reads as broad coverage but exclusions cumulatively eliminate most of it | Customer complaints, E&O exposure |
| **Ambiguous Override** | Multiple "except as otherwise provided" sections with no precedence rule | Coverage litigation |
| **Scope Creep Clause** | A clause written for one peril quietly applies to another via cross-reference | Unintended coverage or denial |
| **Non-deterministic Language** | "As deemed appropriate by the insurer" — outcome depends on who is reading | Regulatory scrutiny, bad faith |
| **Implicit Default** | Silence = coverage (or denial) depending on how a section is read | Inconsistent outcomes, audit failure |
| **Rule Duplication** | Same exclusion retyped across HO-3, HO-5, Farm endorsement with minor variation | One gets updated, others don't — divergence |
| **Contradictory Conditions** | Two clauses apply to the same peril with conflicting outcomes | Claims escalation, litigation |
| **Overbroad Exclusion** | "Acts of government" or similar that unintentionally sweeps in covered scenarios | Coverage gaps, regulatory pushback |

---

## Section 2: Rating & Underwriting Rule Smells
*Problems in how policy logic is encoded into rating tables, rule engines, and underwriting guidelines.*

| Smell | Description | Where It Hurts |
|---|---|---|
| **Hardcoded Jurisdiction Logic** | Rating rule says "IF state = KY THEN…" but the underlying statute it implements is never cited | Rule changes silently when law changes |
| **Magic Rating Factor** | A factor (e.g., 1.15 surcharge for age > 25) with no documented regulatory or actuarial basis | Actuarial audit failure, regulatory challenge |
| **Unversioned Rate Reference** | Rating manual references "current ISO loss costs" with no version pinned | Silent rate drift when ISO updates |
| **Duplicate Rating Logic** | Same rating factor encoded independently in the quoting engine AND the policy admin system | They diverge over time |
| **Dead Rating Rule** | A rule still executing for a discontinued product, territory, or class code | Phantom rate impact, audit finding |
| **Missing Else / Undefined Behavior** | Rating algorithm has no branch for a plausible input combination | Runtime errors, incorrect premium |
| **Calculation Rule Drift** | Payroll, TIV, or other exposure base definition changed in the filed rate manual but not in the system | Systematic misprice |
| **Order-Sensitive Rating** | Premium changes depending on which discount/surcharge fires first — no explicit sequence defined | Non-reproducible quotes |
| **Orphan Underwriting Guideline** | A guideline references a form or class code that no longer exists | Underwriters applying a rule to a ghost |
| **Implicit Underwriting Default** | "If not otherwise specified, standard terms apply" — but "standard" is not defined | Inconsistent decisions across UWs |

---

## Section 3: Regulatory Mapping Smells
*Problems in how the policy and its rules are connected to governing statutes, bulletins, and ISO filings.*

| Smell | Description | Where It Hurts |
|---|---|---|
| **Schema Drift** | State DOI changed a filing form structure; your policy/endorsement still uses the old fields | Filing rejection, compliance finding |
| **Null Reference Clause** | Policy cites "per DOI Bulletin 2019-04" — bulletin superseded, never updated | Audit failure, potential misrepresentation |
| **Referential Drift** | KRS statute renumbered; internal references point to old section numbers | Compliance gap, legal exposure |
| **Unversioned Statutory Reference** | "As required by state law" — no statute cited, no version, no jurisdiction | Unauditable, unenforceable |
| **Filing Dependency** | Policy wording depends on a rate/form filing that has since been superseded | Non-compliant in-force business |
| **Jurisdictional Inheritance** | Multi-state policy assumes all states have same requirements (e.g., same cancellation notice period) | State-specific compliance failures |
| **Sunset Clause Smell** | Emergency COVID-era endorsement or temporary relief provision still in the product | Unintended coverage, regulatory question |
| **Unmapped Obligation** | A state-mandated coverage, condition, or disclosure has no corresponding clause in the filed form | Regulatory violation |
| **Ambiguous Jurisdiction Boundary** | Policy applies "where permitted by law" — no explicit list of states or exclusions | Unknown compliance footprint |
| **Bureau Form Version Lock** | Policy hardcodes ISO HO-3 (04/91) or similar version instead of "current edition" | Must manually update every time ISO revises |

---

## Section 4: Spec-to-Configurator Traceability Smells
*Problems that arise in the handoff from policy spec to policy admin system / configurator code.*

| Smell | Description | Where It Hurts |
|---|---|---|
| **Spec-Code Divergence** | The written policy spec says one thing; the configurator implements something subtly different | Discovered at audit or claims time |
| **Untested Coverage Path** | A combination of coverages, endorsements, and states has never been scenario-tested | Silent gaps found at claims time |
| **No Regulatory Trace in Code** | A rating or eligibility rule has no comment or metadata linking it to the obligation it implements | Cannot audit, cannot update safely |
| **Copy-Paste Configuration** | A state was added by duplicating another state's config and changing a few values | Inherited bugs and stale rules |
| **Manual Sync Between Systems** | The same rule exists in the quoting engine, the PAS, and a spreadsheet — all maintained by hand | They diverge; no one knows which is authoritative |
| **Missing Rollback** | A configuration change was deployed with no ability to revert if it causes issues | Costly hotfix cycles |
| **God Config** | A single configuration object or rule set that governs eligibility, rating, forms, and UW guidelines simultaneously | Impossible to change one thing without breaking others |
| **Implicit Product Dependency** | Endorsement X only works correctly if base product Y is also active — but this is never documented | Silent miscoverage |

---

## Summary

| Section | Smell Count |
|---|---|
| 1. Form & Wording | 14 |
| 2. Rating & Underwriting Rules | 10 |
| 3. Regulatory Mapping | 10 |
| 4. Spec-to-Configurator Traceability | 8 |
| **Total** | **42** |

---

*These smells are detectable at: spec authoring, form filing review, pre-launch configurator audit,*
*regulatory mapping review, and periodic debt-scan of in-force products.*
*See companion document: Insurance Claims Smells.*

