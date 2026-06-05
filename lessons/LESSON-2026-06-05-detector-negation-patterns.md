# Lesson: Negation-Form Phrases in Detector Patterns Fire Backwards

Date: 2026-06-05
Session: Backlog implementation session E
Source: BACKLOG-012, smell5.py H005 fix
Related: `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detectors/smell5.py`, ADR-013

---

## Problem or Question

`SMELL5-H005` was designed to detect mandatory-coverage claims with no regulatory citation. Its pattern included `"is not mandatory"` — intended to catch negation-form regulatory assertions. In practice it fired on rate manual filing instructions like "Section II Coverage is not mandatory for the secondary residence policy." These are not regulatory claims; they are underwriting instructions telling agents how to structure a policy.

---

## Why It Mattered

H005 findings on filing-instruction nodes are not actionable. A reviewer who follows up will find that the "mandatory coverage claim" is actually an agent workflow note, not a provision. It erodes trust in H005 findings as a group.

---

## Pattern: Negation-Form Phrases Usually Match the Opposite Context

When a smell is defined as "provision that does X without a regulatory citation," the negation of X is almost never the smell context — it is the counter-example context:

| Pattern form | What it fires on | Is that the smell? |
|---|---|---|
| "mandatory coverage" | A provision asserting coverage is required | ✓ Usually yes |
| "is not mandatory" | A note asserting coverage is optional | ✗ Almost always no — filing instruction |
| "required endorsement" | A provision requiring an endorsement | ✓ Usually yes |
| "endorsement is not required" | A note saying the endorsement is optional | ✗ Filing instruction |

**Rule:** Before adding a negation phrase to a smell pattern, verify that the negation context reliably represents the smell, not its absence. If the phrase describes "not having the problem," it should not be in the smell pattern.

---

## Pattern: Filing Instructions Are a Distinct Node Type

Rate manuals and underwriting guidelines contain two structurally different types of content:

1. **Policy provisions** — the actual text of the insurance contract. These are the target for smell detectors.
2. **Filing instructions** — directions to agents, underwriters, or configurators about how to build or apply the policy. These look like policy language but are not part of the contract.

Filing instruction context markers:
- "Use this endorsement with all..." — tells the agent to always attach
- "Section [X] is not mandatory for..." — tells the agent this is optional
- "Must be endorsed when..." — tells the agent the condition for attachment
- "Special state requirements" — filing-level header, not a policy clause

These phrases appear in the H005 pattern and produce false positives. The correct fix at scale is the `language_context` annotation (ADR-013). The immediate fix is removing the negation phrase and strengthening the `false_positive_risk` documentation.

---

## Concrete Example

Before (in `smell5.py`):
```python
_H005_PATTERN = re.compile(
    r"\b(mandatory\s+coverage|mandatory\s+endorsement|"
    r"...
    r"is\s+not\s+mandatory)\b",
    re.IGNORECASE,
)
```

Firing on: "Section II Coverage **is not mandatory** for the secondary residence policy" — a rate manual instruction.

After:
- `"is not mandatory"` removed from pattern
- `_H005_FP` updated to name "special state requirements," "use this endorsement with all," and "must be endorsed" as filing-instruction risk terms

---

## Evidence / Validation

- Syntax check passed after edit
- Pattern removal was safe: no H005 findings in run `18b0dec5` fire on "is not mandatory" text; the zero-finding run on the current corpus means no count change

---

## What To Reuse Next Time

- [ ] When adding a new phrase to a smell pattern, ask: does the negation of this phrase represent the smell or its absence?
- [ ] If the negation matches the opposite context (filing instruction, optional coverage, carrier choice), exclude it from the pattern.
- [ ] Filing instructions frequently use negation to describe optional coverages or optional endorsements. This is the most common negation false-positive source.
- [ ] Until `language_context` annotation is implemented (ADR-013), strengthen `false_positive_risk` text to name the specific filing-instruction phrases that are high-FP risks.

---

## Limitations

- This lesson applies to deterministic regex patterns. Semantic/LLM-based detection handles negation context differently.
- Some negation-form phrases are genuine smell signals (e.g., "coverage is not provided" in an exclusion context). The rule is not "never use negation" — it is "verify the negation context before including it."
