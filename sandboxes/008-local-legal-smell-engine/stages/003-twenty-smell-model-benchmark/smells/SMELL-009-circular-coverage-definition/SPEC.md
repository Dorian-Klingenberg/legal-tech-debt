# SMELL-009 — Circular Coverage Definition

- **ID:** `SMELL-009`
- **Name:** Circular Coverage Definition
- **Taxonomy source:** `insurance_claims_smells.md`, Section 1: Coverage Determination Smells, Claims §1
- **Complexity:** Medium

## Definition

A claims coverage rule is circular when the rule's operative coverage meaning depends directly or indirectly on the same coverage concept, without an independent peril, property, loss, trigger, or other adjudication criterion. This packet is claims-specific: it tests cycles in the definition/reference graph used to decide whether a loss is covered. It is not the policy-layer `Circular Definition` smell, which concerns generic glossary terms such as `occurrence` and `event` even when the coverage rule itself has an independent test.

## Positive signal

At least one supplied coverage-definition path returns to its starting coverage concept through `defines` or `references` edges, and the supplied text does not provide an independent operative criterion. A direct statement such as “covered loss means a loss that is covered” and an indirect cycle such as `Coverage A -> covered property -> Coverage A` are both positive signals.

## Negative signal

The coverage rule has an independent operative criterion and no cycle in the coverage-definition subgraph, even if an unrelated glossary term has a generic definitional loop. Overlapping references alone are not enough; the loop must support the coverage decision itself.

## Insufficiency / abstention rule

Return `insufficient` when the supplied evidence contains only a coverage conclusion or an isolated phrase such as “covered under applicable terms,” without the linked definition/reference edges needed to establish a cycle or an independent criterion. Do not infer circularity from absent nodes.

## Evidence contract

The smallest useful evidence set contains:

1. `coverage_definition` — the operative coverage clause or defined coverage concept;
2. `circular_reference_path` — the relevant nodes and typed edges showing a direct or indirect return to that concept;
3. `independent_criterion_check` — text showing either the missing independent criterion (positive) or a real peril/property/trigger test (negative).

The graph must be inspected within the coverage-determination context; a generic glossary cycle is not sufficient by itself.

## Provenance requirements

Every node must identify synthetic provenance in metadata, including `source_id`, `document_id`, `section`, `version`, and `fixture_scope`. Edges must use local stable node IDs and explicit `defines` or `references` types. Fixtures must not reproduce real policy text or identify a real carrier, insured, or claim.

## Known limitations

The fixtures do not resolve drafting intent, severability, incorporation by reference, or jurisdiction-specific interpretive doctrines. A graph cycle may be an intentional shorthand in a complete policy; a real review would need the full form, endorsements, definitions, and applicable law. The packet tests evidence selection and abstention, not a legal conclusion.

