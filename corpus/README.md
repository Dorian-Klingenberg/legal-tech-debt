# Project Corpus

Status: Active shared data area

This folder holds primary documents and evidence corpora used by sandbox experiments and project skills.

## Folder Roles

- `corpus/` is for primary source material used as analysis input: statutes, regulations, bulletins, filings, policy forms, manuals, endorsements, and source manifests.
- `sources/` is for background research, papers, web captures, market research, how-to documents, and supporting literature.
- `sandboxes/` is for experiments that consume corpus material and produce stage-specific fixtures, outputs, and lessons.
- `skills/` is for reusable agent workflows. Skills should reference corpus files, not contain them.

## Current Corpora

| Corpus | Purpose |
|---|---|
| [kentucky-homeowners-policy-smells](kentucky-homeowners-policy-smells/) | Real-document Kentucky homeowners insurance corpus mapped to the five Sandbox 002 policy-layer smells. |

## Rules

- Keep raw downloaded corpus files stable.
- Track downloaded sources in a manifest.
- Track known gaps separately from downloaded evidence.
- Let sandboxes copy or excerpt only what they need for a stage.
- Do not put large primary document sets inside installable skills.

