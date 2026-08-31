# Model Task Contract

Use this prompt shape for each benchmark run. Replace the bracketed smell fields from the manifest and provide only the smell packet's evidence.

```text
You are reviewing structured legal-policy and claims evidence for one named code smell.

Target smell: [smell_name]
Target ID: [smell_id]
Complexity: [complexity]
Definition: [definition]

Review the supplied nodes and edges. Return JSON with exactly these top-level fields:
{
  "smell_id": "...",
  "label": "positive|negative|insufficient",
  "confidence": 0.0,
  "summary": "one concise explanation",
  "evidence": [
    {"node_id": "...", "quote": "short supporting excerpt", "role": "why it matters"}
  ],
  "missing_evidence": ["..."],
  "questions_for_reviewer": ["..."]
}

Rules:
1. Do not infer a positive smell from absent evidence unless the packet explicitly defines that absence as testable.
2. Use only supplied node IDs and quote only supplied text.
3. Use `insufficient` when the evidence needed by the smell contract is not present.
4. Confidence is a calibrated estimate, not a legal conclusion.
5. Identify the smallest evidence set that supports the label.
```

Each smell packet adds its own definition, evidence contract, and abstention rule. The benchmark is designed to compare model reasoning and provenance discipline, not to produce legal advice.
