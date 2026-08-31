# SMELL-015 — Jurisdictional Inheritance in SIU

- **ID:** `SMELL-015`
- **Name:** Jurisdictional Inheritance in SIU
- **Taxonomy source:** `insurance_claims_smells.md` §3, Notice & Procedure Smells
- **Complexity:** Medium

## Definition

An SIU fraud-indicator or fraud-routing rule is declared universal across multiple jurisdictions even though the supplied jurisdictional authority or requirements matrix identifies different applicability, notice, proof, or escalation conditions, and no jurisdiction-specific branch or override exists.

**Benchmark boundary:** the required scope is claims Special Investigations
Unit detection, routing, consent, notice, or escalation behavior. A generic
multi-state rating or underwriting rule belongs to the separate jurisdiction
logic smell and is not sufficient here.

## Positive signal

The evidence joins one shared SIU indicator/routing rule to at least two jurisdictions, supplies a material jurisdictional variance, and shows that the rule has no branch, override, or applicability gate for that variance.

## Negative signal

Jurisdiction-specific branches or overrides govern the differing requirements, or the supplied authority comparison expressly establishes that the same rule is applicable in every covered jurisdiction. A common model is not a smell by itself.

## Insufficiency / abstention rule

Return `insufficient` when the packet has only one jurisdiction, lacks a jurisdictional variance/ equivalence record, or does not establish the rule's scope. Do not infer cross-jurisdiction inheritance from a generic SIU label.

## Evidence contract

Required roles:

- `shared_siu_rule`: the indicator, score, or routing rule and its claimed scope.
- `jurisdiction_set`: at least two named jurisdictions tied to the rule.
- `jurisdictional_variance`: authoritative or synthetic comparison showing different applicability or required handling.
- `branch_or_override_check`: explicit branch/override inventory showing missing or valid jurisdiction handling.

The smallest positive set contains all four roles. A negative set must show either a valid branch/override or an explicit equivalence finding for the named jurisdictions.

## Provenance requirements

Every node must include synthetic `source_id`, `source_type`, `document_version`, `section`, `jurisdiction` or jurisdiction set, `as_of`, and `provenance_status`. Jurisdictional differences must be represented as supplied evidence, not as the model's legal assumption. Cite the rule and the specific comparison node supporting the label.

## Known limitations

The packet cannot establish the real legal validity of a fraud indicator or predict disparate impact. It only identifies a missing jurisdictional decision branch when the supplied comparison says the requirements differ. A shared analytical score may still be acceptable if downstream legal gates are separately implemented.
