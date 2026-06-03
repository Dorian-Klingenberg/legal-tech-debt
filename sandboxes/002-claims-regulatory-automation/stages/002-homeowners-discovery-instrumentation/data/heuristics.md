# Stage 002 Heuristics

Version: 1.0.0
Stage: 002-homeowners-discovery-instrumentation
Updated: 2026-06-03

These are the candidate evidence heuristics used in Stage 002. Each heuristic has a stable ID, a pattern description, the smell it targets, known failure modes, and an expected recall note.

Heuristics are lexical and pattern-based only. They produce candidate evidence, not findings. Paraphrased language, multi-sentence structures, and distributed smells may be missed. Under-recall is expected and is documented per heuristic.

---

## Smell 1 — Overbroad / Non-deterministic Exclusions

### SMELL1-H001: Sweeping Conjunction in Exclusion Context

Pattern: "including but not limited to" within 200 chars of an exclusion keyword (exclud|does not cover|not covered|will not pay)

Rationale: "Including but not limited to" makes exclusion lists non-exhaustive and unpredictable. Reviewers should ask whether the policy's exclusion trigger is bounded.

Failure modes: fires outside exclusion context (in coverage grants); may miss paraphrased open-ended lists.

Expected recall: medium — requires proximity to exclusion keyword.

### SMELL1-H002: Broad Subject in Exclusion

Pattern: "any loss|any damage|any claim|all losses" within 200 chars of an exclusion keyword

Rationale: "Any" or "all" in an exclusion subject without a scoping condition may override a narrow coverage grant.

Failure modes: fires on coverage grants; may miss "loss of any kind."

Expected recall: medium.

### SMELL1-H003: Causation Sweep

Pattern: "arising from or related to|arising out of|directly or indirectly" within 200 chars of an exclusion keyword

Rationale: Open causation language stretches exclusion trigger far beyond proximate cause.

Failure modes: fires in non-exclusion contexts; misses single-direction causation phrases.

Expected recall: low-medium — causation sweeps are common in regulatory text too.

---

## Smell 2 — Magic Number / Magic Valuation Terms

### SMELL2-H001: Undefined Reasonableness

Pattern: "\breasonable\b|\breasonably\b" in sections discussing payment, settlement, valuation, or time limits

Rationale: "Reasonable" without a defined standard or formula is a magic number / magic valuation term — reviewers cannot compute the requirement.

Failure modes: fires on procedural "reasonable" that has an accepted legal meaning; may miss "not unreasonable."

Expected recall: high — very common in claims settlement language.

### SMELL2-H002: Unversioned Current Reference

Pattern: "current manual|current edition|current guidelines|current rate|current standards" without a following version number or date

Rationale: A "current" reference with no version anchor drifts with time and cannot be audited at the time of loss.

Failure modes: misses "latest edition"; may fire on contexts where "current" is anchored by a filing date in a nearby section.

Expected recall: medium.

### SMELL2-H003: Undefined Valuation Term

Pattern: "actual cash value|replacement cost|market value|fair market value" without an adjacent definition or formula reference

Rationale: Valuation terms without a calculation rule or defined methodology are magic valuation terms.

Failure modes: fires when the term is defined elsewhere in the same document; misses novel phrasing.

Expected recall: medium — depends on whether a definition exists in the selected source slice.

---

## Smell 3 — Coverage Inversion / Contradictory Conditions

### SMELL3-H001: Broad Grant With Hollowing Language

Pattern: "all risk|all direct physical loss|all direct loss" within 500 chars followed by "except|unless|subject to|not including|excluding"

Rationale: A broad coverage grant followed by a list of exceptions or conditions may effectively invert coverage if the exceptions are broader than the grant.

Failure modes: fires on legitimate structured policies; requires human review to determine whether inversion exists.

Expected recall: low — most regulatory texts describe the structure without exhibiting the smell.

### SMELL3-H002: Conditioning Without Scope

Pattern: "subject to the terms|subject to all terms|subject to any|except as provided" in coverage-adjacent language

Rationale: Open-ended conditioning phrases can shift coverage scope without specifying limits.

Failure modes: fires broadly; conditioning is normal — the smell is when the conditioning is itself unbounded.

Expected recall: medium — common phrase; most hits require human review.

---

## Smell 4 — Calculation Rule Drift / Unversioned Rate Reference

### SMELL4-H001: Unversioned Manual Reference

Pattern: "the manual|the current manual|the rating manual|the company manual|the bureau manual" without adjacent version or date

Rationale: A reference to "the manual" without a specific version creates a calculation rule that may change without notice.

Failure modes: misses references to "ISO manual" or "AAIS manual" by name; may fire on non-calculation manuals.

Expected recall: medium — depends on whether the source uses "manual" as a technical term.

### SMELL4-H002: As-Amended Calculation Input

Pattern: "as amended|from time to time|as may be amended" in sections describing rates, premiums, fees, or calculation inputs

Rationale: Calculation inputs that can be silently amended create drift between the rate on file and the rate applied.

Failure modes: fires on statutory boilerplate that is expected to reference amendment; not all "as amended" instances are calculation drift.

Expected recall: medium.

### SMELL4-H003: Unanchored Guidelines Reference

Pattern: "guidelines|underwriting guidelines|rating guidelines" without adjacent version, date, or filing reference

Rationale: Unversioned guidelines used as rate or eligibility inputs create invisible dependencies.

Failure modes: fires in contexts where guidelines are expected to be publicly filed; misses "internal guidelines."

Expected recall: low-medium in regulatory text.

---

## Smell 5 — Regulatory Mapping Smells

### SMELL5-H001: Null State Law Reference

Pattern: "as required by state law|as required by applicable law|as required by law|as required by Kentucky law" without adjacent KRS or KAR citation

Rationale: A null reference to "state law" gives reviewers no anchor to verify compliance.

Failure modes: fires on general preambles that do not need a citation; misses "required under applicable regulations."

Expected recall: medium.

### SMELL5-H002: Permitted-By-Law Without Citation

Pattern: "as permitted by law|as allowed by law|to the extent permitted" without adjacent KRS or KAR citation

Rationale: Permissive authority without a citation makes it impossible to verify the scope of the permission.

Failure modes: common boilerplate in regulatory context; many instances are standard without being a smell.

Expected recall: medium-low.

### SMELL5-H003: Vague KRS/KAR Citation

Pattern: KRS reference with only chapter number and no subtitle or section (e.g., "KRS 304" without a section number)

Rationale: A chapter-level KRS citation with no subtitle or section number provides no actionable regulatory anchor.

Failure modes: may flag correct broad citations; chapter-level references are sometimes appropriate in preambles.

Expected recall: low — very specific false-positive risk.

---

## Notes

- All heuristics are version 1.0.0.
- Heuristic IDs are stable across runs within schema_version 1.0.0.
- Adding or changing a heuristic requires a version bump in this file and a corresponding `schema_version` bump in `candidate_evidence.jsonl`.
- These heuristics are intentionally conservative. Under-recall is preferred over flooding reviewers with noise.
- Cross-heuristic evidence (e.g., a single clause that fires SMELL2-H001 and SMELL5-H001) should produce two separate candidate evidence records.
