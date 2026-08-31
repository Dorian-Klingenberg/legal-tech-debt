# SMELL-002 — Stale Pricing Reference

- **ID:** `SMELL-002`
- **Name:** Stale Pricing Reference
- **Taxonomy source:** `insurance_claims_smells.md`, Section 2 — Valuation & Payment Smells
- **Complexity:** Low

## Definition

A claims valuation rule relies on an external cost database, manual, or pricing service without a pinned edition, effective date, or equivalent immutable version identifier. The smell is about loss of reproducibility and possible staleness; it does not establish that the referenced prices are inaccurate.

**Benchmark boundary:** this packet is limited to claims settlement and
valuation inputs. It excludes filed rating manuals, underwriting factors,
policy ACV wording, and the Stage 006 rate-reference family.

## Positive signal

The supplied calculation/configuration evidence identifies an external pricing source and explicitly records that its version/date is not locked. A claim or policy node may demonstrate that the reference participates in payment calculation.

## Negative signal

The pricing source is pinned to a specific edition/effective date or immutable release identifier, or the evidence uses an internally versioned schedule rather than an unpinned external reference.

## Insufficiency / abstention rule

Return `insufficient` when a pricing database or manual is named but the supplied evidence does not establish whether the reference is version-locked, or when the calculation context is only a fragment. Do not infer staleness merely because a source name appears.

## Evidence contract

Required roles for a positive finding:

1. `external_pricing_reference` — a node naming the external database/manual/service and its use in valuation.
2. `unlocked_version_assertion` — explicit metadata or configuration evidence that no edition/date/release is pinned.
3. `pricing_context` — the rule or claim context showing the reference can affect a payment amount.

The smallest positive set is usually one complete configuration node carrying all three roles; a linked calculation node is preferred when available.

## Provenance requirements

Retain stable local node IDs plus `source_id`, `source_type`, `document_version`, and `section_path` in metadata. Distinguish an external pricing source from a synthetic fixture's own document version. The fixture's `version_locked: false` is an explicit test assertion, not proof about a real vendor's current release.

## Known limitations

The packet does not compare prices across dates and cannot prove that a source is actually stale. It also does not resolve licensing, vendor naming variants, geographic tables, or whether an external source is incorporated by a separate filed rule.
