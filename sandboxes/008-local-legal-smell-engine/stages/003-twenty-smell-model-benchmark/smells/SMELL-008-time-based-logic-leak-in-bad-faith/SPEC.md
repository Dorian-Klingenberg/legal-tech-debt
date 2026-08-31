# SMELL-008 — Time-Based Logic Leak in Bad Faith

- **ID:** `SMELL-008`
- **Name:** Time-Based Logic Leak in Bad Faith
- **Taxonomy source:** `insurance_claims_smells.md`, Claims §6 — Regulatory & Bad Faith Exposure Smells
- **Complexity:** Low
- **Definition:** A claims communication or workflow promises a time-based response but supplies no measurable deadline, trigger event, or auditable enforcement field. This packet is limited to claimant-communication or bad-faith response promises.
- **Positive signal:** A complete promise record uses vague timing such as “promptly” or “as soon as practicable,” while the associated workflow metadata explicitly has no SLA, trigger, or audit field.
- **Negative signal:** The promise has a measurable duration or date, a defined trigger event, and a recorded/auditable field or monitor that can test compliance.
- **Insufficiency / abstention rule:** Abstain when the communication or workflow is partial, the promise is not time-based, or SLA/trigger/audit metadata is unavailable. Do not infer a leak from a phrase alone when the implementation evidence is absent.
- **Evidence contract:** Require `time_promise`, `workflow_timing_metadata`, and `claim_context`. A positive requires complete evidence plus explicit `sla_status`, `trigger_status`, and `audit_field_status` values showing the controls are absent; a negative requires all three controls to be present.
- **Provenance requirements:** Preserve stable `source_id`, `source_type`, `locator`, jurisdiction, policy/workflow version, completeness, and timing metadata review date. Keep the exact promise text for reviewer quotation.
- **Boundary from adjacent smells:** Do not label policy-only vague timing terms, statutory notice/payment deadlines, or proof-of-loss enforcement gaps here; those belong to separate semantic or invariant checks such as SMELL-018.
- **Known limitations:** A local audit-field declaration does not establish that a production monitor works. Statutory or regulatory timing requirements may exist outside the supplied packet and require separate authority review.
