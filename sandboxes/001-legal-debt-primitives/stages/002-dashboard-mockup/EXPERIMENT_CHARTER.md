# Experiment Charter

## Mission Need

Legal and compliance corpora accumulate references, definitions, obligations, exceptions, and external authority dependencies. The first mission need is not to automate legal judgment. It is to make structural debt visible enough that humans can review it faster and with better traceability.

## Pre-Phase A Framing

This sandbox is a concept exploration artifact. It should answer:

- What can simple deterministic tooling detect?
- Which defects need legal-domain parsing rather than generic text search?
- Which defects need semantic analysis, SME review, or formal modeling?
- What data model is implied by useful findings?

## Hypotheses

1. A useful first-pass legal debt report can be generated from plain text or Markdown without a full legal ontology.
2. The highest-value early defects are structural: dangling references, circular references, orphan definitions, missing owners, missing effective dates, and unversioned external authorities.
3. Graph-shaped output will become necessary quickly, but a graph database is not needed for the first learning loop.
4. Human review should be designed into the workflow from the beginning.

## Evidence To Capture

- detector precision on sample documents
- false positives caused by formatting variation
- data fields required to make findings actionable
- where existing standards or libraries appear to help
- where a custom obligation schema is needed

## First Review Gate

After the first probe can run on a small sample corpus, decide whether Sandbox 002 should focus on:

- graph database modeling
- Akoma Ntoso or LegalRuleML representation
- LLM-assisted obligation extraction
- insurance-specific legislative drift
- SME review workflow and evidence capture
