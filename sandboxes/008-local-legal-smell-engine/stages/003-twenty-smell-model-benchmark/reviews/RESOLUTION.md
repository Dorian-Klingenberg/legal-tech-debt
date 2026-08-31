# Stage 003 Review Resolution

The independent contract review and taxonomy review were completed before
model runs.

## Contract findings addressed

- [x] SMELL-017 negative cases now contain distinct reserve and payment nodes with typed integration edges.
- [x] SMELL-011-N02 now models separate roof and foundation components rather than attaching both exclusions to one shared loss node.
- [x] SMELL-018's negative-role vocabulary is documented, and its specification now requires a dated trigger or explicitly exercised trigger field.
- [x] The validator enforces unique case IDs, node kind/text shape, non-empty edge types, and unique `(source, target, type)` edge identity per case.

## Taxonomy boundaries accepted

- [x] SMELL-002 is claims settlement/valuation pricing only.
- [x] SMELL-008 is claimant-communication or bad-faith response timing only.
- [x] SMELL-009 requires a coverage-decision witness path; a generic glossary cycle is insufficient.
- [x] SMELL-015 requires SIU fraud detection/routing/consent/notice behavior.
- [x] SMELL-019 requires a dated authority-to-deployed-claims-workflow propagation failure.

These boundaries preserve stable taxonomy names while making the benchmark's
semantic distance from Stage 006 and Sandbox 007 explicit.
