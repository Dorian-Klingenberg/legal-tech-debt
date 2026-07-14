# Corpus Procurement Strategy

Status: Active strategy note
Scope: Cross-sandbox corpus acquisition and state-selection decisions
Last updated: 2026-06-05

This note captures the project-level procurement-risk principle for insurance corpus work.

## Principle

Data procurement risk is not, by itself, a reason to block product discovery. The question is not whether acquisition is annoying; it is whether missing or restricted sources would invalidate a product claim, prevent a detector from running, or make a reviewer-facing output overstate certainty.

If a target state's corpus has high acquisition risk because of open-records eligibility, manual SERFF access, redactions, unknown form numbers, or older filings outside public portals, the project can shift the acquisition experiment to the owner's home state.

The home-state fallback is especially appropriate when the active question is whether the product pattern works, rather than whether a particular state's filing package can be completed.

The active corpus target is current new-business policy repairability. Prefer currently approved, currently issued policy packages, endorsements, manuals, and filing metadata. Do not chase pre-November 1, 2018 history unless it is the only practical way to identify or obtain a document that is still part of the current new-policy package. The project is trying to detect and repair issues carriers can fix now, not reconstruct historical filing lineage for its own sake.

## Current Interpretation

- Kentucky remains the validated prototype corpus for Sandbox 002/003 evidence, detectors, and reports.
- Kentucky procurement gaps should stay targeted: chase them only when an active detector, reviewer question, fixture, ROI example, or report needs the missing source.
- Current new-policy documents matter more than original approval history. Foundational filings are useful only when they are necessary to identify or obtain the current package.
- Missing Kentucky material should be treated as a scoped procurement risk unless a specific experiment requires it and no substitute evidence is adequate.
- If Kentucky procurement risk becomes the main bottleneck, start a home-state corpus acquisition experiment instead of stalling the project.

## Risk Model

Classify corpus gaps by the risk they create:

- **Access risk:** the source may not be available to the owner directly because of residency, portal, open-records, redaction, or licensing constraints.
- **Completeness risk:** the corpus may be missing a current package document needed to prove an attachment map, definition domain, amendatory stack, or rating/manual dependency.
- **Use risk:** the source may be obtainable for inspection but restricted for redistribution, product packaging, or commercial reuse because of copyright, licensing, or confidentiality.
- **Expansion risk:** a state-specific acquisition path may not transfer to another state without local eligibility, counsel, entity setup, carrier cooperation, or licensed data.

Risk should be reflected in outputs. If a source is missing, redacted, or only inferred, downstream artifacts should say so instead of presenting a confirmed defect.

## Redacted Base Jackets

Redacted proprietary base jackets are usually enough to document source limitations, but not enough to confirm definition-domain defects. A redacted jacket may establish that a form exists, belongs to a filing, or was withheld from public view. It cannot prove that a Definitions Section is missing, that a term is undefined, or that an endorsement ambiguity is not cured elsewhere in the policy package.

For the current product lane, proprietary base-form definition review is lower value than cross-document and package-level issues. Treat redacted or unavailable base jackets as a confidence limitation unless a specific high-value detector or report claim depends on the exact base text.

## Expansion Rule

When expanding service coverage to another state, do not assume the home-state procurement posture carries over. Each new state needs a state-specific access plan covering:

- public SERFF or DOI filing access,
- open-records requester eligibility,
- whether a resident, local entity, local counsel, affiliate, or carrier relationship is needed,
- redaction and proprietary-treatment risk,
- copyright and downstream reuse limits,
- available carrier-hosted manuals or forms,
- and whether a licensed forms source is more appropriate than public-record acquisition.

This is not legal advice. It is a project planning rule: keep product discovery moving in the jurisdiction where acquisition risk is lowest, and treat broader state rollout as a separate procurement/compliance problem.

## Practical Use

Use the home-state fallback when:

- a corpus gap blocks a detector or reviewer workflow,
- the blocker is about access rather than product validity,
- the missing source is not essential to preserve continuity with an already validated run,
- and a home-state filing package can answer the same product question with lower acquisition risk.

Do not use the fallback to erase existing evidence. Kentucky remains useful as a worked example, especially for the five Sandbox 002 homeowners smells.
