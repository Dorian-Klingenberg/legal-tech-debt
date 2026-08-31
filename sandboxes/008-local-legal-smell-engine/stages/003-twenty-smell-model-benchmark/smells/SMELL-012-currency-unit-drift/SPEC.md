# SMELL-012 — Currency / Unit Drift

- **ID:** `SMELL-012`
- **Name:** Currency / Unit Drift
- **Taxonomy source:** `insurance_claims_smells.md`, Section 2: Valuation & Payment Smells, Claims §2
- **Complexity:** Medium

## Definition

The policy or filed coverage contract states a monetary limit, deductible, or payment basis using one unit of application, while the claims calculation or payment system applies the amount using a different unit for the same coverage context. Examples include `per occurrence` versus `per item`, `per structure` versus `per occurrence`, or a policy amount in one currency versus a payment field interpreted in another. The smell requires a semantic unit mismatch, not a formatting difference.

## Positive signal

A policy unit and a calculation/payment-system unit are both supplied, linked to the same coverage context, and differ in a way that can change the amount or scope applied. A currency mismatch is positive only when the evidence shows the currency interpretation differs, not merely when symbols are omitted.

## Negative signal

The policy and system use the same unit and currency semantics, or the system explicitly aggregates/splits amounts in a way the policy defines. Different display formats, line-item detail, or multiple payment rows do not establish drift when the governing unit remains aligned.

## Insufficiency / abstention rule

Return `insufficient` when either the policy unit or system unit is missing, the coverage context cannot be matched, or the evidence gives only an amount without its unit/currency. Do not infer `per item`, `per occurrence`, or currency from a field name alone.

## Evidence contract

The smallest useful evidence set contains:

1. `coverage_context` — the shared coverage, limit, deductible, or payment subject;
2. `policy_unit` — the policy wording and currency/unit basis;
3. `system_unit` — the calculation or payment configuration and its currency/unit basis;
4. `unit_comparison` — the typed mapping showing alignment or drift and, for positives, its possible effect on the amount applied.

## Provenance requirements

Each node must carry synthetic `source_id`, `document_id`, `section`, `version`, and `fixture_scope` metadata. Cross-artifact mappings must use local stable IDs and explicit `maps_to`, `calculates`, or `applies_to` edges. Fixtures must not use real policy numbers, claimants, carriers, or payment records.

## Known limitations

The benchmark does not calculate a final claim amount, resolve currency conversion dates, or determine whether a system's aggregation is legally authorized. Real systems may apply a documented hierarchy or conversion service outside the supplied excerpt. A detected mismatch is a review lead requiring reconciliation with the full policy, declarations, endorsements, and configuration history.

