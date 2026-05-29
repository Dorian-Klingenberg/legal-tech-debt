# Edge Type Framework

## Principle

A section reference is evidence of a possible relationship. It is not the relationship itself.

This framework separates the text-level reference from the legal/compliance meaning of that reference.

## Proposed Edge Types

`cites_authority`

The source points to an authority as background or governing law, but does not itself implement an operational step.

`implements_authority`

The source is an internal policy, procedure, control, form, or workflow that operationalizes an authority.

`validates_against`

The source uses the target as a check, condition, or rule before making a decision.

`workflow_handoff`

The source sends work to another internal workflow step.

`requires_evidence`

The source requires the target as evidence, a packet, a record, or a proof source.

`records_retention`

The source preserves records because the target creates or describes the recordkeeping duty.

`notice_requirement`

The source depends on the target for notice content, timing, cancellation, nonrenewal, adverse action, or privacy content.

`proof_requirement`

The source depends on the target for proof of insurance, proof-card, or electronic proof requirements.

`reporting_requirement`

The source depends on the target for vehicle, termination, VIN, electronic coverage, or regulator reporting.

`exception_process`

The source invokes the target because ordinary processing failed or because an exception is required.

`definition_dependency`

The source uses or defines a term whose meaning depends on the target.

`coordinates_with`

The source must be considered together with the target, but the direction of control is weak or mutual.

`review_loop`

The source sends a matter back for review, reopening, audit, or supervisory evaluation.

`stale_reference`

The source points to a missing, obsolete, retired, or explicitly stale target. This edge should be visible but excluded from valid legal reachability.

## Matrix Interpretation

Plain adjacency:

`A[i,j] = 1` means node `i` references node `j`.

Typed adjacency:

`A_type[i,j] = 1` means node `i` has a relationship of `type` to node `j`.

Typed closure should not mean "reachable by any edge." It should mean "reachable by an allowed sequence of edge types."

## Initial Reachability Rules

Valid authority path:

- `implements_authority -> cites_authority`
- `validates_against -> cites_authority`
- `proof_requirement -> cites_authority`
- `notice_requirement -> cites_authority`

Valid workflow path:

- `workflow_handoff -> workflow_handoff`
- `exception_process -> workflow_handoff`
- `review_loop -> workflow_handoff`

Valid evidence path:

- `requires_evidence -> records_retention`
- `notice_requirement -> requires_evidence`
- `proof_requirement -> requires_evidence`

Invalid or non-live path:

- Any path containing `stale_reference` is not valid legal reachability.
- `coordinates_with` should not automatically produce transitive closure until a reviewer decides the relationship has direction.
- `review_loop` should be visible as a loop but should not automatically imply substantive legal authority.

## What This Should Let Us See

Typed edges should let the dashboard distinguish:

- a real authority chain
- an internal workflow loop
- an evidence-retention path
- an exception path
- a stale citation
- a benign reciprocal implementation/citation pattern

That is the point where the graph starts to become a legal debt model.
