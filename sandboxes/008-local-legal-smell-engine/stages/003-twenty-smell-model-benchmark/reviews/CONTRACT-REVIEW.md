# Stage 003 contract review

## Scope and validation

Reviewed the stage contract, manifest, all 20 `SPEC.md` files, and all 60 JSONL fixture files (100 cases total). The existing structural harness passes:

- 20 unique smell IDs and the expected 8 low / 8 medium / 4 high distribution.
- Valid JSONL syntax, required case keys, matching top-level/expected labels, unique case-local node IDs, and case-local edge endpoints.
- No duplicate `(source, target, type)` edge triples were found in the current fixtures.

The low and medium packets generally distinguish positive, negative, and insufficient evidence substantively through explicit scope/completeness, presence/absence assertions, typed joins, and abstention examples. The high packets are cross-artifact in general, but the issues below should be repaired before model runs.

## Findings

### P1 — SMELL-017 negative cases do not supply the required reserve/payment join

`SMELL-017/SPEC.md` requires negative support to include the same reserve and payment records as the positive case plus an integration or controlled-reconciliation record. `017-neg-001` has one `reserve_system_record` whose text mentions both systems, but no distinct payment node or payment edge. `017-neg-002` similarly collapses both views into one `system_record`. Both expected contracts nevertheless list `payment_record` and `reconciliation_process`.

This makes the negative label depend on prose inside a single conflated artifact rather than demonstrating the high-complexity cross-system join. It also makes positive and negative cases structurally incomparable.

Recommended fix: split each negative fixture into distinct reserve and payment nodes carrying the same claim key, add typed integration/reconciliation edges to both, and retain the automated/controlled exception evidence. Keep `expected.required_evidence_roles` aligned with the actual nodes and edges.

### P1 — SMELL-011-N02 graph contradicts its intended negative distinction

`SMELL-011/SPEC.md` says separate loss components are negative when exclusions do not overlap. In `SMELL-011-N02`, both the earthquake exclusion and the wear exclusion point to the same `n02-loss` node, even though its text describes separate foundation and garage-roof damage. The graph therefore presents both exclusions as applying to one common loss, which is the positive-path shape; only the node prose preserves the intended separation.

Recommended fix: represent the foundation and garage-roof damage as separate local loss/component nodes, connect each exclusion and outcome to its matching component, and retain an explicit `separate_loss_components` or equivalent relation. This prevents a graph-based reviewer from treating the negative case as overlapping applicability.

### P2 — SMELL-018-N02 has an undocumented negative-role drift

The SMELL-018 specification describes the negative path as showing the applicable rule, trigger event, due date, workflow branch, and enforcement/audit evidence. `018-neg-002` has no explicit claim-event/trigger node; it relies on workflow text, schema fields, and a simulated control test. Its expected roles replace `proof_of_loss_trigger` with `enforcement_control`, a role not named in the packet's formal role list.

Recommended fix: either add a dated proof-of-loss completion event and connect it to the workflow/system, or explicitly document a control-only negative variant in `SPEC.md`. Standardize the expected role vocabulary (for example, use one defined enforcement/audit role) across positive and negative cases.

### P2 — Edge identity and edge-schema guarantees are incomplete

All current edge endpoints are valid, but the harness only checks `source`/`target` membership. The 237 edges have no explicit local `edge_id`, and the validator does not require `type`, reject duplicate semantic edges, or validate an allowed edge-type vocabulary. Stable edge references are therefore implicit rather than part of the enforced contract.

Recommended fix: define edge identity as either a required case-local `edge_id` or the tuple `(source, target, type)`, then extend the structural check to require the chosen identity, a non-empty edge type, and uniqueness. Add a required `kind`/text node-shape check as well so future packets cannot pass with unreferable evidence nodes.

## High-complexity coverage conclusion

SMELL-018, SMELL-019, and SMELL-020 include useful temporal, authority/workflow, deployment, or policy/configuration joins in their positive and insufficient cases. SMELL-017 has strong positive cross-system fixtures, but its negative cases need the repair above. After those repairs, rerun the structural check and perform a graph-oriented spot review of every high-complexity case.

