# Lesson 5: Spec-Code Divergence Requires Versioned Paired Evidence

Date: 2026-07-14

Status: Boundary lesson; current corpus cannot establish this smell

Scope: Sandbox 007 — Spec-Code Divergence

Related: [strategy matrix](../DETECTION_STRATEGY_MATRIX.md),
[policy-smell taxonomy](../../../insurance_policy_smells.md),
[corpus inventory](../../../corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md),
[ADR-004 artifact identity](../../002-claims-regulatory-automation/adr/ADR-004-schema-run-identity-and-id-stability.md),
[ADR-010 expected-edge reasoning](../../002-claims-regulatory-automation/adr/ADR-010-smell5-retrieval-architecture-gap-detection.md)

## Problem or Question

Spec-Code Divergence is a comparison smell: a written requirement and the
system rule intended to implement it behave differently. Policy text alone can
show an ambiguous requirement or a missing trace, but it cannot establish what
a policy administration system, configurator, rating engine, or claims system
actually implements.

The Kentucky corpus contains policy, form, rate-manual, filing, and regulatory
artifacts. It does not contain a paired PAS export, configuration ruleset,
deployed build, execution trace, or claims-outcome dataset. No real Spec-Code
Divergence instance can therefore be established from the current corpus.

## Why It Mattered

Calling a policy-side traceability gap "divergence" turns a missing comparator
into a finding. It also hides version skew: comparing a historical filing with
current configuration may show two legitimate points in time rather than a
defect.

The detector needs to distinguish three evidence levels:

1. a static requirement-to-rule mismatch;
2. an executed mismatch in a controlled scenario; and
3. an observed production or claims impact.

Evidence at one level does not prove the next.

## Pattern or Solution

Pair before comparing:

1. Identify the authoritative specification unit with a stable clause ID,
   content hash, edition, jurisdiction, product, and effective interval.
2. Identify the implementation unit with a stable rule ID, configuration or
   build hash, environment or deployment identity, normalized condition and
   action, and effective interval.
3. Add an explicit, versioned `implements` relationship that pins both endpoint
   hashes and the comparison run ID.
4. Compare only artifacts whose product, jurisdiction, and effective intervals
   overlap.
5. Audit both directions: spec to code finds missing implementations; code to
   spec finds orphan or unsourced behaviors.
6. Replay boundary and golden-path scenarios when executable access exists.
7. Emit distinct candidate types: `missing_implementation`, `orphan_rule`,
   `semantic_mismatch`, `version_window_mismatch`, and `unresolved_mapping`.

Sandbox 002's stable-ID and provenance rules are reusable principles. Its
closed source and edge schemas do not already model system rules. A future
Sandbox 007 stage should define a versioned extension or new contract rather
than silently changing preserved artifacts.

## Concrete Example — Synthetic

Assume these invented, versioned artifacts:

```text
Spec SYN-HO-KY-2026.1, clause SYN-C17:
Attach endorsement SYN-E9 when roof age is greater than 12 years.

PAS ruleset SYN-PAS-KY-2026.1, rule SYN-R441:
if roof_age_years >= 12: attach("SYN-E9")
```

A trace row links `SYN-C17` to `SYN-R441` and pins both content hashes. A replay
at exactly 12 years produces different results because `>` and `>=` have
different boundaries. That supports a static `semantic_mismatch` candidate.

Without the PAS rule, the specification alone establishes no divergence.
Without execution or deployment evidence, the static diff does not prove that
production issued a policy incorrectly. Without outcome evidence, it does not
establish customer or financial impact.

## Evidence or Validation

| Evidence status | What the repository supports |
|---|---|
| Observed | The canonical corpus inventory contains no PAS, configurator, rule-engine, deployment, execution, or claims-outcome artifact type. |
| Observed | Sandbox 002 schemas provide stable identity, hashes, run identity, and policy-side edges, but they contain no system-rule endpoint or spec-to-code implementation relationship. |
| Inherited | ADR-004 supplies the versioned provenance contract. ADR-010 supplies the general rule that an absence finding requires an explicit expected relationship across both sides of the graph. |
| Proposed | The matrix's trace-back matrix, version-sync comparison, scenario replay, and outcome mining are future designs. They are not detector results or evidence that the smell exists in the Kentucky corpus. |

## Limitations

- A missing trace link can reflect incomplete mapping rather than divergent
  behavior.
- A static configuration diff does not prove executed or deployed behavior.
- Claim clusters do not prove causation without rule, version, and deployment
  linkage.
- Current artifacts can support policy-side requirement extraction and
  synthetic paired fixtures only.
- Real PAS, claims, customer, or production data requires an explicitly
  authorized future stage and appropriate governance.
- Human product, engineering, actuarial, filing, and legal review remains
  required.

## What To Reuse Next Time

- [ ] Confirm both specification and implementation artifact classes exist.
- [ ] Pin exact versions, hashes, product, jurisdiction, and effective windows.
- [ ] Require stable clause and rule IDs plus a versioned comparison run.
- [ ] Check both spec-to-code and code-to-spec coverage.
- [ ] Preserve the mapping edge and logic witness with every candidate.
- [ ] Boundary-test operators, units, defaults, precedence, and missing branches.
- [ ] Separate static mismatch, executed mismatch, and observed outcome impact.
- [ ] Use synthetic fixtures until real system-data access is explicitly
      authorized.

