# ADR-013: Node-Level Language Context Annotation

Date: 2026-06-05
Status: Accepted — design recorded; implementation deferred
Scope: Sandbox 002 Stage 002 ingestion; Stage 006 detectors (Smell 1, Smell 5 H005)
Resolves: BACKLOG-006, BACKLOG-012

---

## Context

Two open detector quality problems share the same root cause:

**BACKLOG-012 (H005 false positives):** `SMELL5-H005` fires on "mandatory coverage" and "mandatory endorsement" language, but two structurally different contexts produce that pattern:

1. **Statement of provision** — a policy clause asserting a coverage is required under regulatory authority. A finding here is real if no regulatory citation is present.
2. **Filing instruction** — a rate manual or underwriting guideline telling agents how to structure a policy (e.g., "Section II Coverage is not mandatory for the secondary residence policy," "use this endorsement with all new-business policies"). A finding here is not actionable — it is a workflow instruction, not a coverage provision.

The H005 heuristic cannot distinguish these contexts from text alone. Targeted fixes (removing the "is not mandatory" negation branch) reduce obvious false positives but do not eliminate the ambiguity for positive-form filing instructions.

**BACKLOG-006 (Smell 1 context):** `SMELL1` overbroad-exclusion detectors fire identically whether broad language appears in a coverage grant, an exclusion, or a condition with a coverage consequence. These three contexts carry different risk profiles and require different reviewer questions. The detector correctly identifies broad language but cannot communicate which context the finding is in.

In both cases the root problem is the same: the node schema carries `node_type` (document / section / subsection) but not **provision type** — what the node is doing in the policy, not just where it sits in the hierarchy.

---

## Decision

Add a `language_context` field to carrier nodes, populated by a lightweight LLM annotation pass during Stage 002 ingestion (or as a separate post-ingestion enrichment step).

### Field schema

```json
"language_context": "<category>"
```

**Categories (enum):**

| Value | Meaning | Examples |
|---|---|---|
| `coverage_grant` | Affirmatively extends coverage | "We cover...", "This policy provides..." |
| `exclusion` | Removes or limits coverage | "We do not cover...", "This policy does not apply to..." |
| `condition` | Establishes a duty, obligation, or procedural rule that affects coverage | "You must notify us within...", "Loss settlement shall be..." |
| `filing_instruction` | Rate manual or underwriting guideline directive — not a policy provision | "Use this endorsement with all...", "Section II is not mandatory for..." |
| `definition` | Defines a term used elsewhere in the policy | "Occurrence means...", "'We', 'us', 'our' refer to..." |
| `ambiguous` | Cannot be reliably classified from text alone | Mixed-context sections, tables of contents, preambles |

### How detectors use it

Once `language_context` is populated:

- **H005**: Skip nodes where `language_context == "filing_instruction"`. Fire only on `coverage_grant`, `condition`, or `ambiguous` nodes where the mandatory-coverage claim appears.
- **Smell 1**: Differentiate reviewer questions by context. A broad phrase in an `exclusion` node gets a different reviewer question than the same phrase in a `coverage_grant` node.
- **All detectors**: `language_context == "definition"` nodes should generally be excluded from smell detection — definitions are not operational provisions.

### Annotation approach

Lightweight LLM pass: for each carrier node, prompt a small model with the node text (up to ~500 tokens) and ask it to classify into the six categories above. The prompt should include 2–3 few-shot examples per category.

The pass runs once per corpus refresh and writes results back to the node records. `language_context` is treated as a soft annotation, not a hard schema field — detectors check for its presence and fall back to `ambiguous` behavior if missing.

Validate on a hand-labeled sample of 20–30 nodes before using `language_context` to gate or weight detector output.

---

## Alternatives Considered

### Deterministic rules
Deterministic classification rules (e.g., "if the section path contains 'exclusion' then tag as exclusion") work for well-structured forms with consistent section naming but fail silently on mixed-context sections, carrier-specific naming conventions, and endorsements that blend coverage grants with conditions. The false-positive rate on KFBM's filing format was unacceptably high in manual testing.

### Full semantic retrieval per node
Embedding-based context detection — similar to the approach evaluated in ADR-010 — measures what is present in a node, not what role it plays. A node containing "we do not cover" scores similarly to one containing "we cover" in many embedding spaces. Provision-type classification requires understanding the illocutionary force of the clause, which is better served by a generative model prompt than by cosine similarity.

### No annotation (current state)
Acceptable as a short-term mitigation when combined with:
- Targeted pattern removal (H005 "is not mandatory" branch — done in this session)
- Strengthened `false_positive_risk` text naming the filing-instruction context
- Reviewer guidance to verify node context before escalating

This is the current state. It produces actionable findings with acceptable false-positive rates given human review. The annotation pass becomes valuable at scale — when finding counts are high enough that per-finding human context verification becomes expensive.

---

## Implementation Plan (deferred)

When a Stage 002 annotation pass is designed:

1. Add `language_context` to the node schema in `sandboxes/002-claims-regulatory-automation/stages/002-ingestion/schema/`.
2. Write a post-ingestion enrichment script: `annotate_language_context.py`. Reads the Stage 002 nodes JSONL, calls LLM for each carrier node, writes `language_context` back.
3. Validate: hand-label 20–30 nodes, compute agreement rate. Target >85% agreement on `coverage_grant`, `exclusion`, and `filing_instruction` categories before using to gate H005.
4. Update `smell5.py` H005 to skip `filing_instruction` nodes.
5. Update `smell1.py` to branch reviewer questions by `language_context`.
6. Rerun Stage 006 detectors on annotated corpus; compare finding counts.

Implementation is not required before any current milestone. The annotation pass is a quality improvement, not a correctness fix — existing findings are valid; this reduces noise and improves reviewer guidance.

---

## Consequences

- H005 false-positive rate is improved immediately by the "is not mandatory" pattern removal (done) and strengthened `false_positive_risk` documentation (done). Residual false positives on filing-instruction nodes remain until the annotation pass is implemented.
- Smell 1 findings remain context-undifferentiated until the annotation pass. Reviewer questions are generic rather than provision-type-specific.
- The `language_context` field design is recorded here and will not need to be re-derived when implementation begins.
- BACKLOG-006 and BACKLOG-012 are closed as design records. Implementation is tracked in the Stage 002 ingestion backlog when that work is ready to begin.
