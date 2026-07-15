# Lesson 1: Detect Definition Dependencies, Not Generic Graph Cycles

Date: 2026-07-14

Status: Design lesson; one lexical candidate observed, detector unimplemented

Scope: Sandbox 007 — Circular Definition

Related: [strategy matrix](../DETECTION_STRATEGY_MATRIX.md),
[policy-smell taxonomy](../../../insurance_policy_smells.md),
[Sandbox 001 typed-edge lesson](../../001-legal-debt-primitives/stages/004-typed-edge-study/LESSON.md)

## Problem or Question

A circular definition fails to add independent meaning. The simplest form
repeats the term being defined; a harder form sends the reader through two or
more definitions and eventually returns to the starting term.

A text echo can find the first shape. A generic document-reference cycle cannot
reliably find the second. Legal documents contain many legitimate cycles, and
the current Sandbox 002 `defines_term` edges are node-to-self markers recording
that a node contains a definition. Treating those markers as definition
dependencies would falsely make every recorded definition look circular.

## Why It Mattered

An untyped cycle detector answers only, "Can this node reach itself?" The review
question is narrower: "Does the meaning of term A depend on term B, whose
meaning ultimately depends on term A?"

Without that distinction, the detector mixes three different review cases:

- a literal term echo;
- a genuine multi-term dependency loop; and
- a missing definition caused by an incomplete filing package or parser miss.

Those cases need different evidence, confidence, and remediation.

## Pattern or Solution

Use a layered detector:

1. Extract a definition record with stable source, node, package, term, and
   definition-body identifiers.
2. Normalize the defined term and look for a meaningful reuse of that term in
   its own definition body. Keep the full sentence as a witness.
3. Represent terms as term nodes, or emit explicit
   `definition_depends_on(term_a, term_b)` relationships. Do not infer semantic
   cycles from generic document-reference edges or from the current
   node-to-self `defines_term` markers.
4. Run strongly connected component or cycle detection only over those typed
   definition-dependency relationships.
5. Reconcile the complete policy or filing package before labeling an
   unresolved term as circular. A definition may live in an omitted base form,
   endorsement, schedule, or manual.
6. Emit separate candidate classes: `literal_self_reference`,
   `definition_cycle`, and `unresolved_definition_dependency`.

Every graph finding should carry a witness path. A reviewer should be able to
see the exact sequence `term A -> term B -> term A`, not merely a cycle flag.

## Concrete Example — Synthetic

Assume this invented definitions section:

```text
"Protected event" means an event that qualifies as a protected event under
this section.

"Eligible occurrence" means a protected event.

"Protected event" also means an eligible occurrence.
```

The first sentence is a literal self-reference candidate. The latter two
sentences create a two-term loop only if the parser emits term-level dependency
edges. A generic section graph cannot establish that semantic relationship.

A useful finding would show:

```text
candidate_type: definition_cycle
witness_path: Protected event -> Eligible occurrence -> Protected event
package_status: complete
review_question: What independent condition terminates this definition chain?
```

## Evidence or Validation

| Evidence status | What the repository supports |
|---|---|
| Observed | Direct text extraction from source `KY-SERFF-KFBM-134870230-UW-MANUAL` confirmed a sentence that repeats the term being defined before adding thresholds and exceptions. That supports a literal term-echo candidate, not a confirmed defect. |
| Observed | Sandbox 002's graph builder emits `defines_term` edges from a node back to the same node. Those edges record extraction provenance; they are not term-to-term semantic dependencies. |
| Inherited | Sandbox 001 established that cycles are review questions, not automatic defects, and that edge meaning plus witness paths matter. |
| Proposed | The matrix's Phase 1 detector, package reconciliation, term-node model, and precision target have not been implemented or measured. |

The existing Sandbox 002 `SMELL2-H004` definition extraction can inform term
parsing, but its output does not validate the new Circular Definition detector.

## Limitations

- Repeating a term can be stylistically redundant while later language still
  supplies an operational threshold.
- Pronouns, synonyms, and incorporated definitions can hide a semantic loop
  from literal matching.
- OCR and layout errors can split a defined term from its definition body.
- A missing package component can resemble an unresolved or circular
  definition.
- Semantic similarity can suggest equivalent definitions, but it does not by
  itself prove a meaning dependency.
- A candidate requires human policy and legal review; it is not a legal
  conclusion.

## What To Reuse Next Time

- [ ] Separate literal self-reference, multi-term cycles, and unresolved
      definitions.
- [ ] Create term-level dependency relationships before running cycle logic.
- [ ] Never treat the current node-to-self `defines_term` marker as proof of a
      circular definition.
- [ ] Attach a typed witness path to every cycle candidate.
- [ ] Check package completeness and parser warnings before assigning
      confidence.
- [ ] Preserve source ID, node ID, term normalization, detector version, and
      run identity.
- [ ] Report validation targets as targets until a labeled evaluation run
      measures them.

