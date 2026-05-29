# Backlog

## Now

- Run the sample corpus through the lightweight probe.
- Review whether each finding is understandable without reading the code.
- Add line numbers and source snippets to findings.
- Inspect dependency matrix outputs and decide whether matrix closure is worth developing further.

## Next

- Add an obligation schema draft: authority refs, scope, triggers, required actions, evidence, owner.
- Export a dependency graph as Graphviz DOT or Mermaid.
- Add detector IDs aligned to the RAII/legal debt taxonomy.
- Add fixture cases for false positives.

## Later

- Compare regex extraction with spaCy or LexNLP.
- Test a Neo4j import path.
- Test LLM-assisted extraction on the same sample corpus.
- Try modeling one rule in OpenFisca or Catala.
- Add SME review states: accepted, rejected, needs clarification.
