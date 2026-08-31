# SMELL-011 — Overlapping Exclusion Conflict

- **ID:** `SMELL-011`
- **Name:** Overlapping Exclusion Conflict
- **Taxonomy source:** `insurance_claims_smells.md`, Section 1: Coverage Determination Smells, Claims §1
- **Complexity:** Medium

## Definition

Two or more exclusions apply to the same loss, peril, or damage scenario, yet their supplied wording or linked endorsements imply materially different coverage outcomes, such as total denial versus covered ensuing damage or limited coverage. The smell is the unresolved conflict in application, not merely duplicate exclusions.

## Positive signal

The evidence links at least two exclusions to the same loss and supplies outcome language for each that conflicts. No supplied priority, anti-conflict, ensuing-loss, or endorsement-order rule resolves the difference.

## Negative signal

Overlapping exclusions produce the same outcome, or exclusions apply to distinct loss components. A clear priority or exception rule that resolves otherwise competing wording is also negative.

## Insufficiency / abstention rule

Return `insufficient` when fewer than two applicable exclusions are supplied, the common loss is not identified, or the evidence does not include outcome language. Do not infer conflict merely because two exclusions mention the same general peril.

## Evidence contract

The smallest useful evidence set contains:

1. `common_loss` — the loss or damage scenario shared by the exclusions;
2. `applicable_exclusions` — two exclusions linked to that loss or peril;
3. `conflicting_outcomes` — the different implied results (for example, denied and covered/limited);
4. `conflict_resolution_check` — a supplied priority or exception rule, or a bounded statement that none is present.

## Provenance requirements

All nodes must include synthetic `source_id`, `document_id`, `section`, `version`, and `fixture_scope` metadata. Applicability and outcome edges must be explicit (`applies_to`, `implies_outcome`, `resolves`) and node IDs must be stable within each case. Examples must be purpose-built and legally cautious.

## Known limitations

The benchmark does not decide which clause would prevail under contra proferentem, anti-concurrent-causation doctrine, endorsement hierarchy, or other jurisdiction-specific interpretation. “Different outcome” is a fixture-level signal requiring human review against the complete form and claim facts.

