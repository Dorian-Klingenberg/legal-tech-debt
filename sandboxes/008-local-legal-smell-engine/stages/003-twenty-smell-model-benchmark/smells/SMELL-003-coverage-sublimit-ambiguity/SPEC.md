# SMELL-003 — Coverage Sublimit Ambiguity

- **ID:** `SMELL-003`
- **Name:** Coverage Sublimit Ambiguity
- **Taxonomy source:** `insurance_claims_smells.md`, Section 2 — Valuation & Payment Smells
- **Complexity:** Low

## Definition

Two active policy or claims artifacts impose different sublimits on the same item or coverage bucket, while the supplied evidence does not state which limit controls or how the limits interact. The smell flags an unresolved competing-limit relationship; it does not decide the insured's entitlement.

## Positive signal

Two distinct limit nodes both apply to the same identified item/bucket, carry different amounts or scopes, and are linked to that same item. The supplied metadata explicitly states that both are active and that precedence/interaction is undefined.

## Negative signal

Only one applicable sublimit exists, the limits apply to distinct items/buckets, or a clear priority/supersession rule resolves the apparent overlap.

## Insufficiency / abstention rule

Return `insufficient` when fewer than two applicable limit statements are supplied, the item/bucket identity cannot be joined, or the evidence does not establish whether both provisions are active. Do not infer overlap from similar labels alone.

## Evidence contract

Required roles for a positive finding:

1. `first_sublimit` — first active limit and its coverage/item scope.
2. `second_sublimit` — competing active limit and its coverage/item scope.
3. `same_item_join` — shared item key, coverage bucket, or explicit applicability edge.
4. `precedence_gap` — explicit evidence that priority, aggregation, or supersession is undefined.

The smallest positive set is two sublimit nodes plus the shared item node or typed applicability edges.

## Provenance requirements

Each limit and item node must retain stable local IDs and metadata for `source_id`, `source_type`, `document_version`, `section_path`, and active status. The shared item identity is synthetic fixture data and must not be mistaken for a real claim identifier.

## Known limitations

This low-complexity packet does not calculate aggregation, anti-stacking, scheduled-property, or excess-layer outcomes. A complete endorsement hierarchy or declarations-page schedule could resolve an apparent conflict even when the text excerpts look similar.
