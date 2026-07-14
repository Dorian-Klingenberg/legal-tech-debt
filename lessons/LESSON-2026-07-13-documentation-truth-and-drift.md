# Lesson: Current State Needs One Home And Every Count Needs A Scope

Date: 2026-07-13
Status: Active reusable lesson

## What Happened

The repository preserved its decisions well, but volatile state was copied into startup files, sandbox READMEs, handoffs, plans, and generated reports. Later work completed backlog items and changed detector counts without updating every copy.

The result was not missing history. It was too many documents claiming to be current.

Examples included:

- agent entry files still directing work to two completed backlog items;
- a 35-finding historical snapshot presented beside the current 31-finding output without naming the difference;
- a 29-source shorthand mixed with 28 ingested sources and 32 canonical corpus files;
- historical handoffs using present-tense resume instructions;
- a copied assumption that HO 04 93 was KFBM's base form after it had been identified as an endorsement;
- a generated reviewer report retaining an obsolete zero-Smell-5 warning.

## Lesson

Use one human-readable current-status surface and one compact machine-readable mirror:

- `README.md` owns the human-readable current lane, pivot ledger, scoped counts, and open gates.
- `AGENT_CONTEXT.json` mirrors that state for fast agent startup.

Other documents own narrower truth:

- startup files own rules;
- ADRs own accepted decisions and explicit corrections;
- sandbox closure/stage records own experiment state;
- `BACKLOG.md` owns unresolved cross-sandbox work;
- journals, older handoffs, external reports, generated outputs, and conversations own history.

## Count Rule

Never write a bare project count when the scope matters. Name at least:

- artifact type;
- run or snapshot;
- filter stage;
- date when it is not immutable.

For this repository, these are all valid and different:

- 32 canonical corpus files;
- 28 sources in the preserved ingestion run;
- 353 total nodes in that run;
- 143 carrier nodes after detector filters;
- 31 current detector findings;
- 35 findings in the historical Sandbox 003 input snapshot.

## Historical Record Rule

Do not rewrite a historical result merely because the present changed. Add a visible historical/superseded label and a concise current pointer. Correct factual errors that could be reused as facts, while preserving the record of why the earlier decision happened.

## Generated Artifact Rule

If documentation is generated from code, fix the generator and regenerate the artifact. Editing only the output leaves the contradiction ready to return.

## Reuse Checklist

- [ ] Is there exactly one obvious current-status page?
- [ ] Does compact agent context mirror it?
- [ ] Are old handoffs labeled historical or superseded?
- [ ] Does every important count name its scope?
- [ ] Do accepted ADRs include later corrections or supersession notes?
- [ ] Are parked non-goals distinguishable from unfinished work?
- [ ] Did a generator create the stale statement, and if so, was it fixed too?
- [ ] Do local links and machine-readable files validate?

