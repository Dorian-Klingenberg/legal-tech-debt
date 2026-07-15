# Lesson 3: A Missing Inline Citation Is a Traceability Question

Date: 2026-07-14

Status: Design lesson; state-scoped rule candidates observed, detector unimplemented

Scope: Sandbox 007 — Hardcoded Jurisdiction Logic

Related: [strategy matrix](../DETECTION_STRATEGY_MATRIX.md),
[policy-smell taxonomy](../../../insurance_policy_smells.md),
[ADR-010 gap-detection decision](../../002-claims-regulatory-automation/adr/ADR-010-smell5-retrieval-architecture-gap-detection.md),
[ADR-013 language-context design](../../002-claims-regulatory-automation/adr/ADR-013-language-context-annotation.md)

## Problem or Question

A carrier manual can contain a state-specific imperative, threshold, or required
endorsement without a nearby KRS, KAR, DOI, or filing citation. That establishes
a traceability question in the analyzed text. It does not establish that the
rule is unlawful, that a citation must appear inline, or even that the rule
implements law rather than carrier underwriting or actuarial judgment.

## Why It Mattered

Treating every uncited rule as noncompliance would create noisy findings and
collapse different document roles. Phrases such as "special state
requirements," "use this endorsement," and "must be endorsed" often occur in
filing instructions. They are not necessarily policy provisions directed to an
insured.

Authority can also appear elsewhere in the filing package. "No citation in
this paragraph" and "no traceable authority in the reviewed package" are
different claims.

## Pattern or Solution

Use candidate classification followed by package-level gap detection:

1. Limit candidate generation to carrier materials and require both a
   jurisdiction cue and an operational rule or parameter.
2. Classify the language role as a policy provision, filing instruction,
   actuarial or rating rule, underwriting rule, or ambiguous text.
3. Search the complete filing package and typed graph neighborhood for a
   statute, regulation, bulletin, advisory opinion, or SERFF anchor.
4. Record the search scope, package completeness, parser warnings, authority
   identity, version, and effective dates.
5. Emit separate statuses: `no_inline_citation`, `no_package_trace`,
   `unresolved_authority`, or `resolved_elsewhere`.
6. Phrase the result as an unanchored jurisdiction-rule candidate and ask a
   reviewer whether the rule implements a legal mandate, reflects a permissible
   carrier choice, or conflicts with a verified live authority.

This is an absence problem. Semantic search can retrieve relevant regulatory
documents, but it cannot prove that an expected relationship is missing. The
accepted Sandbox 002 pattern is a typed graph-gap check with inspectable witness
evidence.

## Concrete Example — Synthetic

Assume this invented rate-manual section:

```text
KENTUCKY SPECIAL REQUIREMENTS

For Kentucky risks, attach Endorsement SYN-42 whenever roof age exceeds
15 years.
```

If the paragraph has no citation, the first result is:

```text
status: no_inline_citation
not_established:
  - that an inline citation is legally required
  - that the rule implements a statute
  - that the rule is noncompliant
```

If a filing memorandum in the same complete package maps the rule to a live
authority, the candidate should become `resolved_elsewhere`. If the package is
incomplete, it should remain `unresolved_authority`, not be promoted to a legal
finding.

## Evidence or Validation

| Evidence status | What the repository supports |
|---|---|
| Observed | Direct extraction from KNIC source `127064322` confirms a state-requirements section with endorsement instructions and no inline KRS/KAR citation. The same filing contains a KRS citation elsewhere, proving why paragraph-level and package-level absence must be separated. |
| Observed | Direct extraction from KFBM rate-manual source `134870729-RATE-MANUAL-HOP2-1` confirms a mandatory endorsement instruction without a nearby authority citation. It remains a candidate whose language role and package context require review. |
| Inherited | ADR-010 experimentally established that regulatory traceability gaps require expected-edge analysis rather than vector similarity. ADR-013 records the filing-instruction false-positive class. |
| Proposed | Sandbox 007 has not implemented or evaluated its citation audit, state-header classifier, package reconciliation, or precision target. Current broader Smell 5 findings are not validation of this new smell detector. |

## Limitations

- A citation may exist elsewhere in an incomplete or unparsed filing package.
- Many rating and underwriting rules are carrier or actuarial choices, not
  direct implementations of legal mandates.
- Conservative graph extraction can miss a real authority edge.
- The `language_context` annotation is a deferred design, not a validated field
  in the current artifacts.
- A missing trace is an auditability issue, not proof of substantive
  noncompliance or customer harm.
- Human legal, filing, actuarial, and product review remains required.

## What To Reuse Next Time

- [ ] Confirm the source is carrier material rather than the regulatory
      reference layer.
- [ ] Require both a jurisdiction cue and an operational rule.
- [ ] Distinguish policy provisions, filing instructions, rating logic, and
      underwriting guidance.
- [ ] Search the complete package before calling an authority absent.
- [ ] Separate legal mandates from carrier or actuarial choices.
- [ ] Preserve the graph and package search scope with every candidate.
- [ ] Validate authority identity, version, jurisdiction, and effective dates.
- [ ] Label output as a traceability candidate, not noncompliance.

