---
name: write-journal-entry
description: Write dated project journal entries. Use when capturing what happened in a session, research pass, implementation pass, validation pass, corpus change, stage transition, user decision, or other chronological project memory that future agents should understand without reading the whole conversation.
---

# Write Journal Entry

## Startup

1. Read the repository startup instructions and current context.
2. Inspect focused diffs, logs, outputs, and user decisions needed to reconstruct what happened.
3. Separate point-in-time observations from canonical project truth.

## Journal Shape

Prefer:

- Title with date and scope
- Session Summary
- What Changed or What We Did
- Decisions Made
- Validation Performed
- Current State
- What Comes Next

## Rules

- Write journals as narrative project memory, not canonical specs.
- Write journal files under the top-level `journal/` folder. Do not create new `JOURNAL-*.md` files inside sandbox folders.
- Include concrete paths, run IDs, output counts, and validation commands when available.
- Record surprises, false starts, and what was intentionally left untouched.
- Include checkboxes for next work when the entry creates follow-up.
- Update an index or discovery surface if the repo has one.

## Do Not

- Do not use a journal to silently change canonical scope.
- Do not claim validation happened unless it did.
- Do not omit known gaps just because they are inconvenient.

## Output

Report the journal path, source evidence used, validation captured, and remaining open items.
