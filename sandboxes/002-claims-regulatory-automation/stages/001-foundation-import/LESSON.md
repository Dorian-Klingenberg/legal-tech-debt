# Lesson: Import the Useful Primitive, Not the Whole Sandbox

Sandbox 001 proved that a small plain-Python probe can make legal debt visible. It did not prove that the generic probe is already an insurance product.

That distinction matters.

The useful move is to import the working primitive into Sandbox 002, then let homeowners insurance policy and claims smells reshape it. A dangling reference in 001 becomes the foundation for Broken Link / Null Reference Clause detection in 002. A matrix output in 001 becomes useful only when it explains which homeowners policy, claims workflow, rating spec, or compliance artifact is affected.

## What We Learned From 001

Lightweight parsing is enough for a first pass.

The probe can:

- find section anchors
- find references
- report missing targets
- show simple cycles
- identify unused definitions
- emit reviewable artifacts

That is enough to start insurance experiments without infrastructure.

## What Changes in 002

The evaluation target changes.

In 001, success meant proving the primitive worked.

In 002, success means finding high-value Kentucky homeowners insurance smells in a way a policy, claims, compliance, or product reviewer can understand.

The first useful insurance adaptation should therefore focus on:

- Broken Link / Null Reference Clause
- Calculation Rule Drift

## Boundary

This stage is a bridge, not a destination. It should stay small and readable.

Do not add databases, services, schedulers, or external NLP stacks here. The next stage should earn every new concept by tying it to a concrete insurance smell.
