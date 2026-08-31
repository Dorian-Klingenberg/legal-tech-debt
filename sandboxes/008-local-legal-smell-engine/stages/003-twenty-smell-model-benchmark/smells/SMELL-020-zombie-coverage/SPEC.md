# SMELL-020 — Zombie Coverage

- **ID:** SMELL-020
- **Name:** Zombie Coverage
- **Taxonomy source:** `insurance_claims_smells.md`, Section 1 (Coverage Determination Smells), “Zombie Coverage”
- **Complexity:** High

## Definition

A coverage intended to be removed or overridden by an endorsement, renewal,
or form change remains active in the applicable policy or claims system after
the removal's effective date. The benchmark requires temporal and artifact
joins; a historical coverage before the effective date is not a zombie.

## Positive signal

The packet supplies a base form or prior declaration that establishes the
coverage, a dated removal/override endorsement, and post-effective-date
renewal/declarations or system/claim evidence showing the coverage still
active. The same policy, jurisdiction, product, and term must be aligned.

## Negative signal

The smell is negative when the current term omits or disables the removed
coverage, or when the coverage is active only in a term that predates the
removal. A coverage retained by an explicit replacement endorsement is not a
zombie even if the base form text remains in a historical artifact.

## Insufficiency / abstention rule

Abstain if the packet lacks either the removal instruction, its effective
date, or post-effective evidence of active coverage. Do not infer active
coverage from a stale base form alone, and do not infer a zombie from a claim
without policy-term and endorsement applicability evidence.

## Evidence contract

Required positive roles:

1. `base_coverage` — named coverage and the form/declaration version that grants it;
2. `removal_or_override` — endorsement/form change, scope, and effective date;
3. `applicable_policy_term` — policy, jurisdiction, product, and term after the removal date;
4. `active_coverage_evidence` — current declaration, configurator state, claim decision, or issued form showing the coverage remains active;
5. `temporal_join` — explicit relationship proving the active evidence is after the effective removal and within scope.

Negative cases should provide the same artifacts with a disabled/omitted
current state or a pre-effective term. Insufficient cases should omit the
term/date/state needed to establish that join.

## Provenance requirements

Every form, endorsement, declaration, and configuration node must carry a
synthetic source ID, document/version ID, product, jurisdiction, policy ID or
term key, and effective/issued date. Edges must distinguish `grants`,
`removes`, `applies_to`, and `active_in`. Claims may support active coverage
only when tied to the policy term and coverage configuration; a claim text
alone is not enough.

## Known limitations

This packet cannot resolve legal priority rules, notice/consent requirements,
midterm endorsement validity, or whether a filing is enforceable. It tests
whether supplied artifacts expose a likely stale active state. Real systems
may intentionally retain base-form language while applying an endorsement
overlay, which requires explicit precedence evidence.
