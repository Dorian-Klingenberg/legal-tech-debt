# SMELL-006 — Dead Recovery Path

- **ID:** `SMELL-006`
- **Name:** Dead Recovery Path
- **Taxonomy source:** `insurance_claims_smells.md`, Claims §5 — Subrogation & Recovery Smells
- **Complexity:** Low
- **Definition:** A policy, claims procedure, or recovery workflow directs staff to a salvage/subrogation process that the organization has explicitly discontinued.
- **Positive signal:** A recovery instruction points to a named process, queue, desk, portal, or vendor and an authoritative current-status record says that target is retired, closed, or unavailable.
- **Negative signal:** The referenced recovery target is active for the same jurisdiction and effective period, with an operational owner or intake route.
- **Insufficiency / abstention rule:** Abstain when the recovery reference is not identified precisely or the status record is stale, unofficial, jurisdictionally mismatched, or absent. “Not found” is not equivalent to discontinued.
- **Evidence contract:** Require `recovery_instruction`, `process_status`, and `policy_context`; connect the instruction to the named process with a `routes_to` edge. A positive requires an explicit discontinued/retired status and compatible effective dates.
- **Provenance requirements:** Every node must carry stable `source_id`, `source_type`, `locator`, jurisdiction, and effective/review date. Status evidence must identify its owner or authoritative system and status timestamp.
- **Known limitations:** A synthetic status registry cannot establish whether an undocumented replacement route exists. Real organizations may retire a route operationally before updating policy text.
