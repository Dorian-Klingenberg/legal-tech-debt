# Sandbox 002: Kentucky Homeowners Policy-Layer Phish Prototypes

## Project Overview

Sandbox 002 is the active work lane. It is currently focused on **Kentucky homeowners insurance policy-layer smells** and the **five policy-layer phish** plan in [002-five-policy-layer-phish.md](002-five-policy-layer-phish.md).

The immediate goal is to produce small, explainable, fixture-first detector prototypes that make policy defects visible early, before they become costly disputes, rework, or compliance fire drills.

**Current scope**: Kentucky homeowners insurance only. Do not start personal auto, motor vehicle, no-fault, or PIP work unless the user explicitly reopens that scope.

---

## Current Priority: Five Policy-Layer Phish

Primary near-term workstream:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells (generic "state law", null references)

The canonical detection blueprints and Gherkin-style checks live in [002-five-policy-layer-phish.md](002-five-policy-layer-phish.md).

---

## Implementation Style (Sandbox Contract)

- Keep prototypes lightweight, readable, and deterministic.
- Start with small KY fixtures first; expand only after detector behavior is clear.
- Prefer regex/rule heuristics plus simple clause/reference graphs over heavy NLP infrastructure.
- Produce explainable outputs (`findings.json`, concise markdown summaries, fixture notes).
- Keep human review in the loop; detector findings are not legal advice.

---

## Relationship to Sandbox 001

Sandbox 001 remains reusable foundation work. Bring forward only the primitives that help the current policy-layer phish detectors:

- section/reference extraction
- dangling/null reference checks
- circular reference checks
- simple matrix/graph outputs
- JSON/CSV/Markdown evidence generation

See [002-CARRY-FORWARD-FROM-001.md](002-CARRY-FORWARD-FROM-001.md) for reuse guidance.

---

## Near-Term Implementation Targets

The first detector implementations should stay close to the five-phish plan and KY homeowners data reality:

1. **Regulatory Mapping + Broken/Null Reference pass**
   - Detect "as required by law"/"applicable law" clauses without concrete KY citations.
   - Detect missing internal targets and stale external references where possible.
2. **Calculation Rule Drift / Unversioned Reference pass**
   - Flag "current manual/current guideline" references without edition/date/version.
   - Compare filed/expected formula snippets vs. implemented formula snippets in a narrow fixture.
3. **Magic Terms + Overbroad Exclusion pass**
   - Flag undefined temporal/valuation terms and broad exclusion trigger language.
4. **Coverage Inversion pass**
   - Build small grant→exclusion→exception chains and flag contradictory/hollowed grants.

---

## Staged Next Steps

1. **Stage A: Fixture Curation**
   - Build a small KY homeowners fixture set (forms, endorsements, rate/rule snippets, KY legal references).
2. **Stage B: Detector Prototypes**
   - Implement the first two high-traction passes above with explainable outputs.
3. **Stage C: Expand to Full Five-Phish Coverage**
   - Add remaining phish detectors incrementally.
4. **Stage D: Calibration**
   - Review false positives/negatives on fixtures and tighten heuristics before any broader expansion.

The detailed sequencing and success gates are in [002-ROADMAP-revised.md](002-ROADMAP-revised.md).

---

## Planning and Reference Documents

- [002-ROADMAP-revised.md](002-ROADMAP-revised.md) — active roadmap aligned to five policy-layer phish
- [002-five-policy-layer-phish.md](002-five-policy-layer-phish.md) — detector blueprints + Gherkin scenarios
- [002-PAIN-POINTS-TAXONOMY.md](002-PAIN-POINTS-TAXONOMY.md) — smell taxonomy, impact framing, and phish mapping
- [002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md](002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md) — KY fixture source strategy

*Last updated: June 2026*
