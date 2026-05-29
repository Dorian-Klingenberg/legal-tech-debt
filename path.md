# PATH.md — Legal Tech Debt Sandbox

A working draft roadmap for the "Sandbox 001: Legal Debt Primitives" project.

---

## 1. Where You Are Now

- You have a plain-Python probe (`legal_debt_probe.py`) that:
  - extracts section anchors from statutes, policies, and manuals
  - extracts references between sections
  - detects dangling references, simple circular references, orphan definitions
  - flags external authorities that are named without a version/date/source anchor
- The sandbox is staged (001-baseline, 003-kentucky-insurance-sample, 004-typed-edge-study), with each stage having its own STAGE.md and LESSON.md.
- The current question is: **How far can lightweight parsing + graph/matrix checks get before heavier tools are needed?**

This is the "legal smell detector core" in miniature.

---

## 2. Short-Term Path (Next 2–4 Stages)

### 2.1 Finish Typed-Edge Study (Stage 004 ➜ 005)

Goal: move from "raw adjacency" to **typed edges** and **named smells**.

- Define a small, explicit edge type vocabulary (e.g., DEFINES, REFERS_TO, OVERRIDES, CITES_EXTERNAL).
- Update the probe to emit typed edges instead of just a generic adjacency.
- Implement smell detectors on top of typed edges:
  - DanglingReference (no target for REFERS_TO)
  - OrphanDefinition (DEFINES with no inbound uses)
  - SimpleCircularReference (2–3 node REFERS_TO cycles)
  - UnversionedReference (CITES_EXTERNAL without version/date/source anchor)
- Record limitations and false positives/negatives in LESSON.md.

### 2.2 Kentucky Insurance Fixture Deep Dive (Stage 003 ➜ 006)

Goal: prove this is useful **on real-ish insurance text**, not just synthetic toy examples.

- Expand the KY Home/Farmowners fixture with:
  - base form
  - 1–2 endorsements
  - 2–3 synthetic regulatory circulars / bulletins
- Run the typed-edge detectors on this corpus.
- Classify findings by your insurance-specific smells:
  - Coverage Inversion
  - Magic Number Term
  - Sunset Clause Smell
  - Filing Dependency
- Capture 3–5 "this would matter to a SME" examples in OBSERVATIONS.md.

### 2.3 Human-Readable Report Shape (Stage 006 ➜ 007)

Goal: make the output something a **compliance/legal SME can actually read**.

- Take `output/findings.json` and generate:
  - a concise `report.md` grouping findings by smell
  - per-smell sections with:
    - where it was found
    - why it matters (1–2 sentences)
    - suggested remediation questions (not advice)
- Test this with at least one "cold reader" (future you counts).

### 2.4 Minimal API Layer (Stage 007 ➜ 008)

Goal: wrap the probe in a callable interface.

- Extract a `probe_corpus(corpus_path) -> Findings` function.
- Define a minimal `Finding` schema:
  - `id, smell_type, location, message, supporting_edges`
- Keep it plain Python for now (no web, no DB).

---

## 3. Medium-Term Path (After Core Probe Works)

### 3.1 Compare to OpenFisca / PolicyEngine

Goal: learn from existing "rules as code" engines once you have your own data model pressure-tested.

- Read OpenFisca docs and tutorial notebooks.
- Map their `Variable` + `formula` + `Parameter` concepts onto your `Obligation` schema.
- Decide what you want to borrow:
  - versioned parameters
  - test-driven rule definitions
  - separation of input vs output variables

Outcome: a refined `Obligation`/`Rule` data model that can coexist with your smell detector.

### 3.2 Draft Obligation Schema and Lifecycle

Goal: define the canonical object the product will operate on.

- Draft `Obligation`:

  ```
  Obligation {
    id
    jurisdiction
    authority_refs   # statutes, bulletins, forms, versions
    scope            # products, channels, time window
    formula          # rule logic (placeholder for now)
    effective_date
    expiry_date
    owner
    status           # active / superseded / zombie
  }
  ```

- Define RAII defect checks over this schema:
  - DanglingReference, ZombiePolicy, ScopeLeak, DoubleOwnership,
    ShadowDefinition, MissingDestructor, InvariantViolation.

### 3.3 Hook into Policy Spec Workflow (Prototype)

Goal: prove this can plug into the **policy specification process**, where you actually worked.

- Take a KY Home/Farmowners spec (or a simplified version) and:
  - run the probe on the spec document
  - generate a "spec smell report" grouped by policy smells
  - manually map a few findings to real rating/spec issues you know from experience

Outcome: an end-to-end demo: spec in ➜ smells out ➜ human-readable report.

---

## 4. Long-Term Path (Product Direction)

Once the probe and obligation model feel solid:

1. **Add richer extraction** where it clearly pays off:
   - spaCy or an LLM for better section/definition extraction.
   - Akoma Ntoso / LegalRuleML only if you commit to a structured corpus.
2. **Persist the graph** in a real store (Neo4j or equivalent) when you need scale.
3. **Attach cost signals** using your policy smell cost estimates:
   - Prioritize smells by estimated $ impact over 10 years.
4. **Embed in a UI** for compliance/legal SMEs:
   - Upload corpus ➜ see smells and dependency graph ➜ export report.

At every step, keep the sandbox discipline:
- one question per stage
- explicit success criteria
- a short LESSON.md documenting what you learned and what the next question is.

---

## 5. North Star

The end state this PATH is walking toward:

> A plain-Python legal tech debt probe that can be dropped into an
> insurance policy/spec workflow to automatically find structural
> defects (smells), show their dependency context, and hand a
> human-readable report to a compliance or legal SME — with a clear
> path to a full product layered on top.

