# Journal - May 29, 2026

## Focus

Today was about turning the project from broad legal tech debt exploration into a cleaner active path:

- close Sandbox 001 as completed foundational research
- move the useful primitives into Sandbox 002
- make Sandbox 002 the active lane
- narrow the current domain to Kentucky homeowners insurance
- prevent future agents from drifting into auto/no-fault/PIP work by accident

## What Changed

### 1. Closed Sandbox 001

Sandbox 001 is now marked complete as foundational research.

The reason for closing it is that it answered its original question: lightweight parsing plus graph/matrix checks are enough to prove useful legal debt primitives, but richer insurance work now needs domain-specific fixtures and detectors.

001 proved:

- section extraction
- reference extraction
- dangling/null reference detection
- circular reference detection
- orphan definition detection
- unversioned external authority detection
- matrix and graph-style evidence
- JSON, Markdown, and CSV outputs
- static dashboard exploration
- staged experiment discipline

It also taught the most important modeling lesson so far: a reference is not yet a relationship. Typed edges are useful, but they should not block the insurance work unless a concrete homeowners detector needs them.

### 2. Made Sandbox 002 the Active Lane

Sandbox 002 is now the active sandbox for insurance policy and claims legal tech debt experiments.

The carry-forward record explains what comes from 001 and what stays parked. The key decision is to reuse the small, readable proof-of-concept style, not to import infrastructure or turn 002 into a premature platform.

Carried forward:

- plain-Python probe shape
- Markdown fixture pattern
- section and reference extraction
- dangling reference detector concept
- simple circular/orphan checks
- JSON/Markdown/CSV evidence outputs
- staged lessons
- human-review framing

Parked for later:

- graph databases
- live regulatory feeds
- PAS integration
- containers and services
- LLM extraction pipelines
- full typed-matrix implementation

### 3. Added Cross-Agent Bootstrap Memory

The repo now has shared agent instructions so Codex, Copilot, Claude Code, and future agents all get the same context.

The key memory is:

- read the documentation before starting
- update shared project memory, not only one assistant's private memory
- this is sandbox proof-of-concept work
- keep work quick, clean, readable, and explainable
- do not add infrastructure unless a stage explicitly evaluates it

### 4. Added Kentucky Data Procurement Guidance

Sandbox 002 now includes a Kentucky insurance data procurement guide.

It documents official sources:

- Kentucky Revised Statutes Chapter 304
- Title 806 Kentucky Administrative Regulations
- Kentucky DOI P&C documents
- SERFF Filing Access
- DOI open records

It also documents how to keep source collection small and auditable:

- use official sources first
- manually collect only a few representative filings
- do not scrape SERFF
- keep raw and processed files separate
- maintain a source manifest
- convert only short excerpts into Markdown fixtures

### 5. Narrowed Scope to Kentucky Homeowners Insurance

This was the most important clarification.

Although earlier notes and the inherited 001 fixture had a lot of auto/no-fault/PIP language, the active work is now Kentucky homeowners insurance.

The docs now say not to start:

- personal auto
- motor vehicle insurance
- no-fault
- PIP

unless that scope is explicitly reopened.

If a homeowners source cross-references another P&C line, that can be recorded as context, but it should not become the active fixture or detector target.

### 6. Updated the Active 002 Foundation Stage

The first 002 stage now imports the 001 probe but uses a tiny homeowners-oriented synthetic fixture instead of the old auto-flavored one.

The stage was run successfully and generated:

```text
Wrote 8 findings, 7 references, and 10 sections to output
```

The report now references homeowners files and terms such as:

- `homeowners_claims_manual.md`
- `homeowners_property_reference.md`
- covered dwelling
- ISO homeowners form language

## Current State

The project state is now:

> Sandbox 001 is complete and preserved as foundational evidence.
> Sandbox 002 is active.
> The current Sandbox 002 scope is Kentucky homeowners insurance.
> The next meaningful implementation stage should adapt the imported probe into homeowners-specific detectors.

## Next Good Step

Create the next 002 stage, probably:

```text
stages/002-homeowners-dual-detector/
```

Working question:

> Can the imported 001 probe detect Broken Link / Null Reference Clause and one narrow Calculation Rule Drift smell in a Kentucky homeowners fixture?

Keep it local, plain Python, and small.
