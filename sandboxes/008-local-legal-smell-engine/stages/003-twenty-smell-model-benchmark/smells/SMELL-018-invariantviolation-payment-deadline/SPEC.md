# SMELL-018 — InvariantViolation — Payment Deadline

- **ID:** SMELL-018
- **Name:** InvariantViolation — Payment Deadline
- **Taxonomy source:** `insurance_claims_smells.md`, Section 3 (Notice & Procedure Smells), “InvariantViolation — Payment Deadline”; cross-reference `legal_code_smell_taxonomy.md`, RAII Defect Classes, “InvariantViolation”
- **Complexity:** High

## Definition

A governing authority creates a payment deadline measured from a defined
proof-of-loss or equivalent trigger, but the current claims workflow and
system state contain no enforceable trigger, due-date calculation, alert,
exception, or audit control that can satisfy the obligation.

## Positive signal

The packet joins a versioned jurisdictional rule to a qualifying claim event
and the deployed workflow/system. The rule supplies both the deadline and
trigger; the current implementation either uses another date or has no
machine-enforced due date and escalation path.

## Negative signal

The smell is negative when the applicable rule, trigger event, due date,
workflow branch, and enforcement/audit evidence agree. A deadline may be
implemented by a service or control outside the claim application if that
control is identified and traceably linked.

## Insufficiency / abstention rule

Abstain when the authority is not versioned or jurisdictionally scoped, when
the triggering proof-of-loss event is absent, or when the packet does not
identify the current deployed workflow/system behavior. Do not infer a
violation merely because a deadline field is not present in one excerpt.

## Evidence contract

Required positive roles:

1. `authority_deadline` — jurisdiction, effective version/date, deadline, and trigger;
2. `proof_of_loss_trigger` — accepted/complete proof event for a claim;
3. `current_workflow` — the procedure that should initiate payment;
4. `deployed_system_state` — fields, jobs, or configuration actually in use;
5. `enforcement_gap` — evidence that no due-date, alert, escalation, or audit control satisfies the rule.

Negative cases should show a calculated due date and at least one durable
enforcement or exception record. A negative case must include either a dated
proof-of-loss completion event or a clearly identified trigger field plus a
control test that exercises that trigger. Required evidence roles may be
distributed across nodes and joined through typed edges. Use the role
`enforcement_control` for durable alerts, escalations, or audit evidence.

## Provenance requirements

Use synthetic authority documents unless a real source is explicitly supplied.
Authority nodes must carry jurisdiction, version/edition, effective date,
and source type. Claim-event nodes must carry claim ID and event timestamp.
Workflow/system nodes must identify deployment version or snapshot date.
Edges must distinguish `requires`, `triggered_by`, `implemented_by`, and
`enforced_by`; absence claims must be supported by an inventory, schema,
control test, or explicit implementation statement.

## Known limitations

This benchmark does not decide whether an authority legally applies to a
particular claim, whether tolling/exceptions exist, or whether a payment was
actually late. It tests traceability of a stated invariant against supplied
implementation evidence. Real systems may enforce deadlines in external
calendar, finance, or compliance tooling not included in the packet.
