# SMELL-007 — Non-deterministic Denial

- **ID:** `SMELL-007`
- **Name:** Non-deterministic Denial
- **Taxonomy source:** `insurance_claims_smells.md`, Claims §6 — Regulatory & Bad Faith Exposure Smells
- **Complexity:** Low
- **Definition:** A denial communication uses outcome-determinative boilerplate but does not identify the specific policy provision or claim-handling obligation supporting the denial.
- **Positive signal:** A complete denial letter or approved template has an explicit `citation_status` of `none` and contains only generalized language such as “not covered under the terms of the policy,” with no provision or obligation citation.
- **Negative signal:** The denial identifies a specific provision or obligation, such as a form section, endorsement paragraph, notice requirement, or proof requirement, that can be located in the supplied policy/claims authority.
- **Insufficiency / abstention rule:** Abstain when the denial is an excerpt, citation fields are unavailable, or the supplied policy/claims authority is incomplete. Do not treat a short excerpt as proof that the full communication lacks a citation.
- **Evidence contract:** Require `denial_communication` (complete text and citation status), `policy_or_obligation_reference` (the applicable authority or explicit absence marker), and `claim_context` (the decision context). A positive requires complete communication metadata and explicit absence of a specific citation; a negative requires a resolvable citation.
- **Provenance requirements:** Preserve stable `source_id`, `source_type`, `locator`, jurisdiction, policy/claim identifiers, template version, and completeness status. Quotes must come from supplied denial text.
- **Known limitations:** Boilerplate may be supplemented by attachments or a separate explanation not included in the packet. Whether a citation is legally adequate remains a human-review question.
