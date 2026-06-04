# ADR-007: Sandbox 003 Scope Is Findings Triage And Intelligence, Not More Infrastructure

Date: 2026-06-03
Status: Accepted
Scope: Sandbox 003 direction; handoff criteria from Sandbox 002

## Context

Sandbox 002 now produces structured Finding records with confidence levels, rationale, and reviewer questions. The output is technically complete but not business-accessible. The reviewer report (Stage 007) is readable by a technically-oriented legal professional but not by a claims officer, Chief Claims Officer, or CEO.

Three possible directions for Sandbox 003 were considered:

1. **More infrastructure** — vector store, hybrid retrieval, production API, ingestion service
2. **More corpus** — additional carriers, additional states, automated procurement
3. **Findings intelligence** — take the structured findings and make them useful to a non-technical audience

At the same time, external feedback was sought (via Perplexity) on what a CEO or Chief Claims Officer would want to see from this tool. That feedback was expected to inform the design of Sandbox 003's output format.

## Decision

Sandbox 003 scope is **findings triage and intelligence**. The three proposed stages are:

1. **LLM-assisted finding triage** — Claude annotates each Finding with a plain-English explanation, a concrete dispute scenario, a false-positive assessment, and a recommended next step. Output is enriched Finding JSONL alongside original fields; original provenance is never overwritten.

2. **Cross-carrier pattern analysis** — Group findings by smell and heuristic across KNIC and KFBM. Findings that appear in both carriers are industry patterns; findings in one carrier only are carrier-specific. Industry patterns carry the strongest case for regulatory attention.

3. **Executive summary report** — One-page output suitable for a CEO or Chief Claims Officer: top findings by business risk, estimated dispute exposure, recommended actions. No node IDs, no JSONL, no technical vocabulary.

Infrastructure (vector store, API, deployment) remains in "Parked Until Earned" from Sandbox 002.

## Consequences

Positive:
- Addresses the actual gap: the pipeline produces findings no one can act on without technical context
- Cross-carrier analysis was enabled by today's KFBM corpus expansion — timing is right
- Executive output directly supports the business case validation objective
- LLM triage is a natural use of Claude API skills already in the project's toolset
- No new infrastructure required; Sandbox 003 reads Sandbox 002 output files directly

Tradeoffs:
- Sandbox 003 depends on Sandbox 002 loose threads being resolved first (Smell 5, gold set re-eval)
- LLM triage quality depends on prompt design — a bad prompt produces hallucinated legal conclusions, which is worse than no annotation
- The executive report format should be informed by the Perplexity CEO-angle feedback before Stage 003 of Sandbox 003 is designed

## Handoff Criteria From Sandbox 002

Sandbox 003 should not start until:

- [ ] Smell 5 detector calibrated on 28-source corpus (currently 0 findings, which is implausible given the corpus content)
- [ ] Gold set re-evaluated on run 87283951 to confirm BM25 still 100%
- [ ] Perplexity/external LLM feedback on reviewer report reviewed by user
- [ ] Decision made on Claude model for Stage 001 triage (Sonnet vs. Opus; cost vs. quality)

## Rejected Alternatives

- **Start Sandbox 003 with vector store / hybrid retrieval** — premature; ADR-002 re-open conditions partially met (second carrier exists) but not fully (no paraphrase gold set, no documented BM25 failure). The infrastructure question should wait.
- **Expand corpus further before triage** — more data without better output doesn't move the business case forward. What's needed is a demonstration of what the existing findings mean, not more findings.
- **Fold Sandbox 003 work back into Sandbox 002** — the concern is scope creep in the existing sandbox. LLM triage and executive reporting are a different abstraction layer from the pipeline and detectors. Keeping them separate maintains clean boundaries.
- **Skip Sandbox 003 and go directly to a client demo** — the findings are not yet in a form any client could evaluate. The triage and executive output layer is the minimum required before any external audience sees this.

## Follow-Up

- Review Perplexity CEO-angle feedback before finalizing Sandbox 003 Stage 003 design
- Write prompt for LLM triage as a standalone document before running at scale — review it before any API calls
- Define what "false positive dismissed" means in the enriched finding schema before Stage 001 begins
