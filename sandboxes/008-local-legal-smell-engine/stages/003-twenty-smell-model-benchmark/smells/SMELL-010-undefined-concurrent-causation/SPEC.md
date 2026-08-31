# SMELL-010 — Undefined Concurrent Causation

- **ID:** `SMELL-010`
- **Name:** Undefined Concurrent Causation
- **Taxonomy source:** `insurance_claims_smells.md`, Section 1: Coverage Determination Smells, Claims §1
- **Complexity:** Medium

## Definition

Two or more independently described perils or causal conditions materially contribute to the same insured loss, but the supplied policy and claims evidence contains no rule for allocating, prioritizing, excluding, or otherwise deciding the concurrent causes. The smell concerns the missing adjudication rule, not merely the existence of multiple facts in a claim.

## Positive signal

The evidence links at least two contributing perils to one loss and explicitly scopes the supplied materials as lacking an anti-concurrent-causation, dominant-cause, efficient-proximate-cause, or allocation rule. The competing causes must be material to the same coverage decision.

## Negative signal

Multiple causes are present but a supplied rule resolves their interaction, such as a dominant-cause rule, anti-concurrent-causation clause, or stated allocation method. A single-cause loss is also negative because there is no concurrent-causation question.

## Insufficiency / abstention rule

Return `insufficient` when the evidence names only one peril, describes damage without causal links, or omits the relevant policy/rule scope. Do not infer that a rule is absent from a partial excerpt unless the fixture's evidence-scope node expressly bounds the supplied materials.

## Evidence contract

The smallest useful evidence set contains:

1. `loss_event` — the common loss or damage being adjudicated;
2. `contributing_perils` — two or more material causes linked to that loss;
3. `concurrent_causation_rule_check` — an explicit rule resolving the causes (negative) or a bounded statement that no such rule is supplied (positive).

The reviewer should preserve the distinction between “two things happened” and “two causes materially contributed to the same loss.”

## Provenance requirements

Each node must carry synthetic `source_id`, `document_id`, `section`, `version`, and `fixture_scope` metadata. Causal and rule edges must be typed (`contributes_to`, `applies_to`, or `resolves`) and use case-local stable IDs. No fixture may imply a real insured, carrier, or legal outcome.

## Known limitations

The benchmark does not determine factual causation, burden of proof, efficient proximate cause under a particular jurisdiction, or whether damage can be physically apportioned. A short policy excerpt may omit a rule that exists elsewhere; positive cases therefore include an explicit evidence-scope boundary. Human review remains necessary.

