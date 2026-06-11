# Demo Dataset Strategy — Synthetic Dirty Laundry

Date: 2026-06-11

## The Problem

The legal-tech-debt pipeline is a portfolio project with an inherent demo problem: it works by
finding compliance defects in real codebases. Demoing it on real data airs someone's dirty laundry.
That's not acceptable as a public artifact.

## The Solution

Build a synthetic demo dataset — a fictional company with fabricated documents and a fabricated
codebase — but seeded with **real defect patterns** drawn from actual analysis work.

The identifying information (company, documents, proprietary logic) is synthetic. The patterns,
defect types, severity distributions, and triage logic are real — drawn from real codebases. This
is standard practice in security research and consulting case studies: the finding is real, the
client is protected.

## Why This Is Stronger Than Pure Fiction

A technical audience scrutinizing the demo can be told honestly: "the patterns are drawn from
real-world analysis, the company is synthetic." That's more credible than "I made everything up."
The shape of the problems is authentic even though the identity of the source is not.

## Construction Notes

**Strip carefully.** If a defect pattern is distinctive enough to fingerprint the source company,
change it. Pattern matters; fingerprint doesn't.

**Document the synthesis.** A short note in the repo: "defect patterns derived from real-world
analysis, company and documents are fictional." Protects against misrepresentation and makes
methodology transparent.

**Pick a boring fictional company.** Generic enough that no resemblance can be claimed.
Something like "Meridian Casualty & Surety" or "Lakeview General Insurance."

**Plant deliberately.** Unlike a real codebase (which produces whatever it produces), the
synthetic dataset can be designed to showcase specific pipeline behaviors:
- At least one absence detection case (graph finding a missing compliance element)
- At least one triage escalation (GPT-4o overriding the mechanical annotation)
- A clean human-readable report at the end
- Defects across three or four severity levels

## The Synthetic Dataset as a Public Artifact

Once built, the dataset goes on GitHub alongside the pipeline. Other people can run the pipeline
against it. That removes all liability and turns the demo into something the community can
actually use and reference.

## Next Steps

- [ ] Define the fictional company (name, domain, size, regulatory context)
- [ ] Draft the defect taxonomy (pattern types, severity levels, sources from real analysis)
- [ ] Build the synthetic documents (policy docs, requirements, contracts)
- [ ] Build the synthetic codebase with planted defects
- [ ] Write the "how I built a synthetic compliance dataset" companion article/session
