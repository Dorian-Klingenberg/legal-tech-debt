# Legal Code Smell Taxonomy
*Derived from original research — Insurance & Legal Domain*
*Total: ~87 named patterns across 10 categories + 7 RAII defect classes*

> The academic "Law Smells" paper (Coupette et al., 2022) covers only 5 basic smells.
> The Rules as Code movement covers 0. Everything below is original work.

---

## Category 1: Structural Smells
*Patterns that make a policy hard to reason about or modify.*

| Smell | Description | Software Analog |
|---|---|---|
| **Shotgun Clause Surgery** | One change (e.g., deductible definition) requires editing 12 scattered sections | Shotgun Surgery |
| **God Clause** | Master clause attempts to govern dozens of exceptions — "Notwithstanding any other provision herein…" | God Object |
| **Circular Reference** | Clause A refers to Clause B which refers back to Clause A | Recursive Loop |
| **Dead Clause** | Clause references an obsolete law or repealed regulation | Dead Code |
| **Orphan Definition** | Defined term never actually used anywhere in the document | Unused Variable |
| **Ambiguous Override** | Clause says "except as otherwise provided" but multiple "otherwise" sections exist | Shadowed Variable |
| **Nested Exception Hell** | "Except as provided in subsection (ii)(b)(3)…" nested deeply | Deeply Nested Conditionals |
| **Rule Duplication** | Identical or near-identical clauses repeated across product lines or riders | Copy-Paste Code |
| **Ambiguous Inheritance** | Nested exclusions and exceptions with unclear precedence order | Multiple Inheritance Ambiguity |

---

## Category 2: Semantic Smells
*Ambiguities or inconsistencies in meaning or logic.*

| Smell | Description | Software Analog |
|---|---|---|
| **Magic Number Term** | Arbitrary thresholds like "30 days" or "reasonable time" without context or rationale | Magic Number |
| **Undefined Behavior Clause** | Policy doesn't specify what happens under a plausible event (e.g., concurrent perils) | Missing Else / Null Dereference |
| **Non-deterministic Language** | Phrases like "customary," "reasonable," or "as deemed appropriate" | Non-deterministic Function |
| **Contradictory Conditions** | Two clauses contradict each other when applied together | Conflicting Conditional |
| **Scope Creep Clause** | Clause intended for one coverage area leaks into others via cross-reference | Global Variable |
| **Implicit Default** | Behavior changes based on silence or omission rather than explicit text | Hidden Side Effect |
| **Semantic Drift** | Term meaning shifts across endorsements — "occurrence," "event," "incident" used interchangeably | Variable Type Drift |
| **Coverage Inversion** | Policy structure hides that exclusions dominate inclusions | Inverted Logic |

---

## Category 3: Dependency Smells
*Problems with how the policy connects to laws, bylaws, and other documents.*

| Smell | Description | Software Analog |
|---|---|---|
| **External Hardcoding** | Clause relies on an external statute number that changes frequently | Hardcoded External Dependency |
| **Unversioned Reference** | "Pursuant to state law" — which one? No version, year, or jurisdiction tagged | Missing Dependency Version |
| **Broken Link / Null Reference Clause** | References a repealed act, retired regulation, or withdrawn bureau form | Null Pointer / Broken Import |
| **Cyclic Dependency** | Policy references endorsement which references the policy back | Cyclic Import |
| **Unbounded Exception** | "Except as otherwise provided by law" — no citation boundary given | Wildcard Import |
| **Orphaned Cross-Reference** | Cross-reference to a section that was deleted in a prior amendment | Dangling Pointer |

---

## Category 4: Legislative Drift / Bureau Change Smells
*Unique to regulated industries — when external sources change but internals don't update.*

| Smell | Description | Software Analog |
|---|---|---|
| **Schema Drift** | A government form or filing changes structure but your policy still assumes the old version | Broken API Contract |
| **Procedural Dependency** | Policy clause depends on an administrative process that no longer exists (e.g., defunct arbitration board) | Broken Workflow / Dangling Callback |
| **Referential Drift** | Referenced laws or codes change numbering or structure; internal references now stale | Outdated Import Path |
| **Implicit Dependence** | Policy assumes an external authority's definition of a term but doesn't cite it; authority changes silently | Shadowed Variable |
| **Null Reference Clause** | Cites an external document or table that no longer exists (e.g., "per Bureau Table C-17" — retired) | Null Pointer Exception |
| **Calculation Rule Drift** | Rate calculation or exposure base definitions change at regulatory level but policy references the old formula | Mismatched Function Signature |
| **Filing Dependency** | Internal policy language depends on rate filings or circulars that have been superseded | Outdated Dependency Version |
| **Jurisdictional Inheritance** | Policy assumes all jurisdictions follow the same regulatory template | Cross-Platform Assumption |
| **External Schema Migration** | A new bureau API or XML schema changes field types or enumerations, breaking internal mappings | Schema Migration Bug |
| **Sunset Clause Smell** | References a temporary or emergency regulation that was time-limited but never cleaned up after expiration | Expired Feature Flag Left On |

---

## Category 5: Logic and Flow Smells
*When policy behavior is unpredictable or order-dependent.*

| Smell | Description | Software Analog |
|---|---|---|
| **Order Sensitivity** | Coverage interpretation changes depending on reading order | Execution Order Bug |
| **Short-Circuiting Ambiguity** | Multiple exclusions apply but precedence is undefined | Undefined Evaluation Order |
| **Duplicate Condition Check** | "No coverage for flood. No coverage for rising water." — redundant conditions that may conflict | Redundant Condition |
| **Catch-All Clause** | "Under no circumstances shall…" used as last-resort blanket denial | Overbroad Exception Catch |
| **Overbroad Exclusion** | Denies coverage well beyond original intent (e.g., "acts of government") | Overfitting |
| **Inconsistent Jurisdictional Logic** | Different interpretations of same wording across regions without explicit branching | Platform-Dependent Behavior |
| **Non-Executable Clause** | Clause can't practically be applied — requires official notice from a nonexistent agency | Unreachable Code |

---

## Category 6: Maintainability Smells
*Practical issues in keeping the policy up to date or auditable.*

| Smell | Description | Software Analog |
|---|---|---|
| **Lack of Traceability** | No reference to the underlying regulatory or actuarial basis for a rule | Missing Unit Test / Comment |
| **Manual Synchronization** | Same clause retyped in multiple jurisdictions instead of parameterized | Manual Configuration Drift |
| **Legal Debt Clause** | Temporary workaround clause becomes permanent (e.g., emergency endorsement never sunset) | Technical Debt |
| **Implicit Dependencies** | Clause assumes another clause is read first to make sense; no explicit ordering declared | Hidden Dependency |
| **Lack of Coverage Tests** | No scenario analysis for combined perils or edge-case interactions | Missing Integration Test |
| **Version Drift** | Multiple policy versions across states reference different years of the same statute | Multi-Branch Version Skew |
| **Semantic Entropy** | Same clause evolves inconsistently across product lines | Code Fork Divergence |
| **Regulatory Fork Bomb** | Different regulators issue overlapping circulars with conflicting guidance | Infinite Recursion in Governance |
| **Retired Entity Reference** | Policy mentions a defunct agency, program, or classification code | Broken External Pointer |
| **Time-Based Logic Leak** | "Effective until further notice" with no expiration date | Memory Leak |

---

## Category 7: Risk and Fraud Smells
*Patterns that expose vulnerabilities to exploitation or coverage failure.*

| Smell | Description | Software Analog |
|---|---|---|
| **Loophole Leakage** | Ambiguous language exploitable for coverage or denial depending on who reads it first | Security Vulnerability |
| **Overbroad Exclusion** | Denies coverage beyond original intent | Overfitting |
| **Inconsistent Jurisdictional Logic** | Same wording interpreted differently across regions without explicit branching | Platform-Dependent Behavior |
| **Non-Executable Clause** | Clause that can't practically be applied | Unreachable Code |

---

## Category 8: Observability Smells
*When humans can't easily tell what's covered or why.*

| Smell | Description | Software Analog |
|---|---|---|
| **Opaque Definitions** | Requires multiple lookups to resolve the meaning of one term | Over-Encapsulation |
| **Lack of Logging** | No record of the interpretive decision pathway for a claim or audit | Missing Logging / Debug Info |
| **Coverage Inversion** | Exclusions dominate inclusions but the structure hides this until deep reading | Inverted Logic |

---

## Category 9: AI-Specific Smells
*Detectable only when using AI/NLP models on a corpus of policies.*

| Smell | Description | Software Analog |
|---|---|---|
| **Vector Ambiguity Cluster** | Semantically similar clauses with different intent — high embedding similarity but divergent meaning | Code Clone Divergence |
| **Semantic Dead Zone** | Area of low embedding density — under-defined or ambiguous region of text | Untested Branch |
| **Clause Entropy Spike** | Excessive variance in AI certainty across a section — contradictory or confusing drafting | High Cyclomatic Complexity |
| **Prompt-Buried Policy** | Regulatory intent is hidden in implementation detail — meaning only emerges after deep context injection | God Function with Hidden State |
| **Parse-and-Pray Clause** | Rule written assuming inputs that may never actually arrive in that form | Optimistic Parsing / No Error Handling |

---

## Category 10: Automation / Agent Smells
*When AI agents or automated systems interact with legal text.*

| Smell | Description | Software Analog |
|---|---|---|
| **Blob Agent** | A single agent or rule that attempts to handle too much legal territory at once | Blob Anti-Pattern |
| **Fuzzy Boundary** | Unclear jurisdiction or scope — agent can't determine where one rule ends and another begins | Unclear Interface |
| **Hidden State** | Non-transparent decision logic — outputs change without any visible rule triggering | Hidden State Bug |
| **Contradictory Rules** | Directly conflicting statutes or clauses that both fire on the same input | Race Condition |

---

## RAII Defect Classes (Structural Governance Layer)
*Original framework — not present in any academic taxonomy.*
*Based on Resource Acquisition Is Initialization (RAII) applied to legal obligation lifecycle.*

| Defect Class | Description |
|---|---|
| **DanglingReference** | Clause points to authority, form, or section that no longer exists |
| **ZombiePolicy** | Rule or obligation still active but its authorizing statute was repealed |
| **ScopeLeak** | Obligation's applicability predicate (jurisdiction, product, channel) is undefined or unbounded |
| **DoubleOwnership** | Same obligation claimed by two different teams or systems — nobody actually owns it |
| **ShadowDefinition** | Term redefined in an endorsement in a way that silently overrides the base policy definition |
| **MissingDestructor** | No decommissioning process — obligations accumulate with no retirement trigger |
| **InvariantViolation** | A provable compliance invariant ("notice must be sent within T days") is not satisfied by any current rule |

---

## Summary Count

| Category | Smell Count |
|---|---|
| 1. Structural | 9 |
| 2. Semantic | 8 |
| 3. Dependency | 6 |
| 4. Legislative Drift / Bureau Change | 10 |
| 5. Logic and Flow | 7 |
| 6. Maintainability | 10 |
| 7. Risk and Fraud | 4 |
| 8. Observability | 3 |
| 9. AI-Specific | 5 |
| 10. Automation / Agent | 4 |
| **RAII Defect Classes** | **7** |
| **Total** | **73** |

---

*For comparison: Coupette et al. (2022) "Law Smells" academic paper covers 5 smells.*
*Rules as Code movement (OECD, NZ, AU, etc.) covers 0 smells.*
*This taxonomy is original work at the intersection of software engineering, insurance, and computational law.*

