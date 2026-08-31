# SMELL-005 — Orphan Denial Reason Code

- **ID:** `SMELL-005`
- **Name:** Orphan Denial Reason Code
- **Taxonomy source:** `insurance_claims_smells.md`, Claims §4 — Adjuster Workflow & Decision Smells
- **Complexity:** Low
- **Definition:** An adjuster-facing denial reason code cites a policy provision that is absent from the supplied current policy form or endorsement set.
- **Positive signal:** A complete denial-code record names a provision identifier, and the supplied current-form inventory is complete enough to show that identifier is not present.
- **Negative signal:** The same provision identifier is present in the supplied current form, with matching jurisdiction/version context.
- **Insufficiency / abstention rule:** Abstain when the current form set is missing, marked partial, or has unresolved version/jurisdiction identity. Absence in an incomplete or mismatched form set is not evidence of an orphan code.
- **Evidence contract:** Require `denial_reason_code` (code and referenced provision), `current_form_inventory` (complete provision inventory and form identity), and `policy_context` (jurisdiction and effective/version context). A `references` edge should connect the code to the cited provision identifier or form inventory.
- **Provenance requirements:** Every node must identify a stable `source_id`, `source_type`, `locator`, jurisdiction, and effective/version context when applicable. Preserve whether the form inventory is complete or partial.
- **Known limitations:** Synthetic inventories cannot prove that an unlisted provision was never present in an omitted attachment. Similar provision labels or OCR/parser errors require human review.
