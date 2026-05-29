# Technology Evaluation Matrix

| Capability | Existing Candidate | What To Test | Build/Buy Bias |
|---|---|---|---|
| Citation extraction | regex, spaCy, LexNLP, custom parser | Can it reliably identify section references across statutes, policies, and manuals? | Start simple, build domain-specific parser if needed |
| Dependency graph | NetworkX, Neo4j, RDF stores | Can reviewers understand upstream/downstream impact quickly? | Prototype in memory, graduate to graph DB later |
| Dependency matrix | dense CSV, bitsets, sparse matrices, NumPy/SciPy | Can matrix products and closure answer whole-corpus reachability faster or more clearly than traversal? | Prototype dense; move to sparse/bitset only after scale pressure |
| Legal document format | Markdown, Akoma Ntoso, LegalDocML | Does structured markup improve extraction enough to justify conversion cost? | Avoid conversion early unless source data already has structure |
| Rule execution | OpenFisca, Drools, Camunda, Catala | Which obligations are executable rules vs review findings? | Use existing engines for executable rules; build debt layer separately |
| Semantic similarity | embeddings, sentence transformers, LLMs | Can it detect duplicated obligations or drift without too many false positives? | Use as assistive ranking, not authoritative proof |
| Obligation extraction | LLMs, information extraction pipelines | Can humans validate extracted obligations efficiently? | Likely custom workflow around existing models |
| Audit evidence | JSON findings, markdown reports, review records | What evidence is needed to defend a finding? | Build lightweight schema early |

## Evaluation Notes

- A tool is useful only if it produces reviewable evidence.
- A detector with moderate recall can still be valuable if false positives are explainable.
- Formal tools matter most where obligations become executable decisions.
- The product gap is likely not parsing alone; it is lifecycle, ownership, validation, and impact analysis.
