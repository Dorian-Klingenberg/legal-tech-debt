# Smell Selection — Twenty New Benchmark Tasks

The selection intentionally favors claims-layer smells that are not already implemented in Sandbox 002. The five Sandbox 007 strategy smells are also excluded: Circular Definition, Rule Duplication, Hardcoded Jurisdiction Logic, Null Reference Clause, and Spec-Code Divergence.

| ID | Smell | Source taxonomy | Level | Evidence challenge |
|---|---|---|---|---|
| SMELL-001 | Undefined Depreciation Logic | Claims §2 | Low | Detect a depreciation allowance without a specified method or inputs |
| SMELL-002 | Stale Pricing Reference | Claims §2 | Low | Detect an external cost database reference with no pinned version/date |
| SMELL-003 | Coverage Sublimit Ambiguity | Claims §2 | Low | Detect competing sublimits for the same item or coverage bucket |
| SMELL-004 | Unversioned Proof-of-Loss Form | Claims §3 | Low | Detect a form reference without an edition/version that conflicts with evidence |
| SMELL-005 | Orphan Denial Reason Code | Claims §4 | Low | Detect a denial code whose referenced provision is absent from the supplied form |
| SMELL-006 | Dead Recovery Path | Claims §5 | Low | Detect a recovery/salvage step pointing to a discontinued process |
| SMELL-007 | Non-deterministic Denial | Claims §6 | Low | Detect denial boilerplate without a specific provision or obligation |
| SMELL-008 | Time-Based Logic Leak in Bad Faith | Claims §6 | Low | Detect a time promise with no measurable SLA, trigger, or audit field |
| SMELL-009 | Circular Coverage Definition | Claims §1 | Medium | Resolve definition/reference edges and detect self-supporting coverage language |
| SMELL-010 | Undefined Concurrent Causation | Claims §1 | Medium | Detect multiple contributing perils with no allocation or dominant-cause rule |
| SMELL-011 | Overlapping Exclusion Conflict | Claims §1 | Medium | Compare exclusions that cover the same peril but imply different outcomes |
| SMELL-012 | Currency / Unit Drift | Claims §2 | Medium | Compare policy units with calculation or payment-system units |
| SMELL-013 | Missing Escalation Path | Claims §2 | Medium | Detect a valuation dispute trigger with no actor, route, or deadline |
| SMELL-014 | Sunset Obligation Smell | Claims §3 | Medium | Join temporary/emergency language to a missing or expired retirement condition |
| SMELL-015 | Jurisdictional Inheritance in SIU | Claims §3 | Medium | Detect a single fraud-indicator rule applied across jurisdictions without branches |
| SMELL-016 | Lack of Coverage Test Logging | Claims §6 | Medium | Detect a decision workflow with no record of test names, inputs, and outcomes |
| SMELL-017 | Manual Sync — Reserves vs. Payments | Claims §4 | High | Join two authoritative-looking systems that require manual reconciliation |
| SMELL-018 | InvariantViolation — Payment Deadline | Claims §3 / RAII | High | Join legal deadline, proof-of-loss trigger, and absence of enforcement |
| SMELL-019 | Regulatory Drift in Claim Handling | Claims §6 | High | Compare authority/workflow versions and identify an unpropagated change |
| SMELL-020 | Zombie Coverage | Claims §1 | High | Compare base form and endorsement/renewal evidence for removed-but-active coverage |

## Why this distribution

- The eight low-level tasks establish a dependable baseline for extraction, provenance, and abstention.
- The eight medium-level tasks exercise context windows, relation following, ambiguity handling, and jurisdiction/version reasoning.
- The four high-level tasks require joins across policy text, claim workflow metadata, system records, or time/version evidence. They are intentionally more likely to require model judgment and human review.

## Non-overlap note

“Circular Coverage Definition” is claims-specific and tests coverage-definition edges; it is not the Sandbox 007 policy-layer “Circular Definition” strategy packet. The benchmark manifest will preserve the taxonomy source and this distinction so later results are not misattributed.

## Benchmark-only boundaries for near-duplicates

- **SMELL-002** is claims settlement/valuation pricing input only; it excludes filed rating manuals, underwriting factors, policy ACV wording, and the Stage 006 rate-reference family.
- **SMELL-008** is claimant-communication or bad-faith response timing only; it excludes policy-only vague timing terms and statutory notice/payment deadline enforcement.
- **SMELL-009** requires a coverage-decision witness path; a generic glossary cycle is not enough.
- **SMELL-015** requires SIU fraud detection/routing/consent/notice behavior; generic multi-state rating or underwriting logic is out of scope.
- **SMELL-019** requires a dated authority-to-deployed-claims-workflow propagation failure; generic policy-to-system divergence is out of scope.
