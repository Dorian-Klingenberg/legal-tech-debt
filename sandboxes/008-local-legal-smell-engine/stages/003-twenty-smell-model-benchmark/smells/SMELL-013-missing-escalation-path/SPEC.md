# SMELL-013 — Missing Escalation Path

- **ID:** `SMELL-013`
- **Name:** Missing Escalation Path
- **Taxonomy source:** `insurance_claims_smells.md` §2, Valuation & Payment Smells
- **Complexity:** Medium

## Definition

A valuation-dispute trigger exists, but the supplied policy and claims workflow do not define a complete escalation actor, route, and deadline for handling the dispute.

## Positive signal

The evidence package establishes that the valuation-dispute procedure is in scope and complete enough to inspect, then shows a dispute trigger without a named decision owner, destination or mechanism, and response deadline. A structured absence check may count as evidence only when the package explicitly enumerates the inspected workflow components.

## Negative signal

The valuation-dispute path names an accountable actor, a route or handoff mechanism, and a deadline or service-level trigger. A shared resolution path is not a smell when it is expressly applicable to the covered dispute.

## Insufficiency / abstention rule

Return `insufficient` when the evidence contains only a dispute phrase, an isolated policy clause, or an incomplete workflow extract. Do not infer a missing path from an absent edge unless a workflow-scope or component-inventory node establishes that the relevant procedure was fully supplied.

## Evidence contract

Required roles:

- `valuation_dispute_trigger`: the condition that starts escalation consideration.
- `workflow_scope`: evidence that the supplied policy/workflow is the complete procedure or an explicit component inventory.
- `escalation_component_check`: actor, route, and deadline fields/edges inspected, including an explicit missing-state when applicable.
- `applicability_context`: claim, product, or version context tying the trigger to the inspected procedure.

The smallest positive set normally contains the trigger, workflow scope, and component check. A complete actor/route/deadline path is sufficient for a negative label.

## Provenance requirements

Every node must retain synthetic `source_id`, `source_type`, `document_version`, `section`, `jurisdiction`, and `provenance_status` metadata. Evidence selections must cite supplied node IDs and distinguish policy text from workflow metadata. Missing components must be represented by an explicit scope/check node or a typed absent relationship, not by an unsupported assumption.

## Known limitations

The smell does not decide whether appraisal, mediation, or supervisory review is legally required. It detects an evidence-level workflow gap only; external claims manuals, jurisdictional overlays, or operational runbooks not supplied in the packet may complete the path.

