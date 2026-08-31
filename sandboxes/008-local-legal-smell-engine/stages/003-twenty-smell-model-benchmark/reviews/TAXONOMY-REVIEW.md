# Taxonomy and Non-Overlap Review

## Result

The twenty selections are aligned to named entries in `insurance_claims_smells.md`. `SMELL-018` is correctly cross-referenced to the claims-layer `InvariantViolation — Payment Deadline` entry and the RAII `InvariantViolation` defect class. No packet introduces a new taxonomy name or a clearly misclassified complexity level.

The structural validator also confirms 20 packets and the intended 8 low / 8 medium / 4 high distribution, with positive, negative, and insufficient cases for every packet. The main risk is semantic overlap with the frozen Stage 006 families and Sandbox 007 strategy smells.

## Packet-by-packet assessment

| IDs | Taxonomy / level | Review finding |
|---|---|---|
| SMELL-001 | Claims §2 / low | Aligned. Keep the boundary at a missing depreciation method and inputs; a generic undefined ACV term belongs to Stage 006 S2. |
| SMELL-002 | Claims §2 / low | Aligned but high overlap with Stage 006 S4 (`Calculation Rule Drift / Unversioned Rate Reference`). The current definition is effectively the claims-system variant of an unversioned external reference. |
| SMELL-003 | Claims §2 / low | Aligned. Same-item/bucket join plus missing precedence distinguishes it from Stage 006 coverage inversion. |
| SMELL-004 | Claims §3 / low | Aligned and low is defensible: the supersession check is a small deterministic join. Keep it limited to proof-of-loss form identity/supersession, not generic unversioned legal references. |
| SMELL-005 | Claims §4 / low | Aligned. It is a claims code-to-current-form absence check, but is structurally close to Sandbox 007 `Null Reference Clause`; the complete current-form inventory and denial-code relationship are essential boundaries. |
| SMELL-006 | Claims §5 / low | Aligned. Retired process/status evidence keeps it distinct from a generic null citation; do not broaden it to any missing external reference. |
| SMELL-007 | Claims §6 / low | Aligned. The positive signal is missing denial citation, not broad or ambiguous exclusion language. |
| SMELL-008 | Claims §6 / low | Aligned but high overlap with Stage 006 S2 temporal “magic number” signals and with SMELL-018. It needs an explicit communication/workflow-promise boundary. |
| SMELL-009 | Claims §1 / medium | Claims entry is correct, but the name and graph-cycle mechanism are very close to Sandbox 007 `Circular Definition`. The packet’s generic glossary cycle negative case helps, but the distinction remains easy for models to collapse. |
| SMELL-010 | Claims §1 / medium | Aligned. Two material causes plus a missing allocation/prioritization rule is distinct from exclusion conflict and coverage inversion. |
| SMELL-011 | Claims §1 / medium | Aligned, with controlled overlap with Stage 006 S1/S3. Require two applicable exclusions, two different outcome edges, and no resolution rule; duplicate exclusions alone are correctly negative. |
| SMELL-012 | Claims §2 / medium | Aligned. Semantic unit/currency mapping is distinct from Stage 006 S4’s unversioned or opaque rate reference. |
| SMELL-013 | Claims §2 / medium | Aligned. The missing actor/route/deadline component check is a workflow smell, not a general regulatory-mapping gap. |
| SMELL-014 | Claims §3 / medium | Aligned. Temporary authority plus current executable workflow and absent retirement control matches the claims taxonomy; retained historical text alone is correctly negative. |
| SMELL-015 | Claims §3 / medium | Aligned but high overlap with Sandbox 007 `Hardcoded Jurisdiction Logic`: universal rule + jurisdictional variance + no branch is the same core shape. The SIU fraud-indicator/routing scope must remain explicit. |
| SMELL-016 | Claims §6 / medium | Aligned. It tests missing structured coverage-test identity/input/outcome logging, not merely an uncited denial; this is a useful boundary from SMELL-007. |
| SMELL-017 | Claims §4 / high | Aligned. Same-claim reserve/payment records plus recurring manual reconciliation justify high complexity. |
| SMELL-018 | Claims §3 + RAII / high | Aligned. Versioned authority, proof trigger, deployed workflow, and enforcement gap justify high complexity. Keep statutory payment deadlines distinct from vague communication timing in SMELL-008. |
| SMELL-019 | Claims §6 / high | Aligned but high overlap with Sandbox 007 `Spec-Code Divergence` and Stage 006 S5. The authority-to-deployed-claims-workflow propagation mismatch must be the required scope, not generic policy/system divergence. |
| SMELL-020 | Claims §1 / high | Aligned. The effective removal date, applicable policy term, and active post-removal coverage state justify high complexity. Require this temporal removal join so it does not become generic Spec-Code Divergence or RAII `ZombiePolicy`. |

## Exclusion check

The benchmark does not select the five Stage 006 names: `Overbroad / Non-deterministic Exclusions`, `Magic Number / Magic Valuation Terms`, `Coverage Inversion / Contradictory Conditions`, `Calculation Rule Drift / Unversioned Rate Reference`, or `Regulatory Mapping Smells`. It also does not select the five Sandbox 007 names: `Circular Definition`, `Rule Duplication`, `Hardcoded Jurisdiction Logic`, `Null Reference Clause`, or `Spec-Code Divergence`.

That is true by name and source-taxonomy reference, but not fully by semantic distance. The highest-risk near-duplicates are:

1. **SMELL-002 ↔ Stage 006 S4:** both detect an unversioned external pricing/rate reference.
2. **SMELL-008 ↔ Stage 006 S2 / SMELL-018:** all can be triggered by an unmeasured or unenforced timing obligation.
3. **SMELL-009 ↔ Sandbox 007 Circular Definition:** both detect definition/reference cycles; the claims-coverage criterion is the only discriminator.
4. **SMELL-015 ↔ Sandbox 007 Hardcoded Jurisdiction Logic:** both detect a universal rule applied across jurisdictions without branches.
5. **SMELL-019 ↔ Sandbox 007 Spec-Code Divergence / Stage 006 S5:** all compare an authoritative requirement with an implementation that was not updated.
6. **SMELL-005 ↔ Sandbox 007 Null Reference Clause:** both detect a live-looking reference whose target is absent; the claims denial-code/current-form join must remain mandatory.

## Recommended fixes before model runs

- Rename or narrow **SMELL-002** to an explicitly claims-scoped “Unversioned Claims Pricing Reference,” excluding filed rating manuals, policy ACV definitions, and Stage 006 rate-reference cases.
- Add explicit exclusion text to **SMELL-008** for policy-only vague timing terms and statutory payment/notice deadlines; reserve it for a communication promise whose workflow lacks SLA, trigger, and audit controls.
- Rename **SMELL-009** to a coverage-specific name such as “Coverage-Rule Circularity,” and retain the required coverage-decision witness path plus the generic-glossary negative cases.
- Rename or scope **SMELL-015** to “SIU Fraud-Routing Jurisdiction Inheritance,” requiring a claims SIU rule, jurisdictional variance, and missing routing/consent/notice branch.
- Add a hard boundary to **SMELL-019**: only dated authority-to-deployed-claims-workflow propagation failures qualify; generic policy-to-system mismatch remains Sandbox 007 territory.
- Preserve the current evidence boundaries for **SMELL-001**, **SMELL-005**, **SMELL-011**, **SMELL-018**, and **SMELL-020**; their fixtures already contain the distinctions needed to avoid the nearest Stage 006/Sandbox 007 labels.

## Review basis

- Source taxonomy: `insurance_claims_smells.md` and the RAII section of `legal_code_smell_taxonomy.md`.
- Selection and intended exclusions: `SMELL_SELECTION.md` and `STAGE.md`.
- Frozen Stage 006 scope: `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Sandbox 007 strategy scope: `sandboxes/007-policy-smell-detector-strategies/README.md` and `DETECTION_STRATEGY_MATRIX.md`.
- Packet evidence: all 20 packet `SPEC.md`, `positive.jsonl`, `negative.jsonl`, and `insufficient.jsonl` files.
- Structural check: `harness/validate_packets.py` returned `status: ok` with 20 smells and 8/8/4 complexity counts.
