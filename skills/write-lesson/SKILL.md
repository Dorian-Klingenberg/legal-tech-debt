---
name: write-lesson
description: Capture reusable lessons from experiments, bugs, validation results, design decisions, or agent behavior. Use when work produced a repeatable pattern, warning, teaching artifact, failure mode, implementation insight, or project convention that should outlive the session and help future agents or humans.
---

# Write Lesson

## Startup

1. Read the repository startup instructions and current context.
2. Gather the specific evidence: changed files, outputs, failed attempts, validation, user decision, or reviewer feedback.
3. Decide whether the lesson is local to a stage or reusable across the project.

## Lesson Shape

Prefer:

- Problem or Question
- Why It Mattered
- Pattern or Solution
- Concrete Example
- Evidence or Validation
- Limitations
- What To Reuse Next Time
- Follow-up checklist with checkboxes when useful

## Rules

- Teach the transferable pattern, not just the event timeline.
- Anchor the lesson in evidence, not vibes.
- Include limits so future agents do not overgeneralize.
- Link to the stage, ADR, journal, or artifact that produced the lesson.
- Update a catalog, README, roadmap, or discovery surface if the repo has one.

## Do Not

- Do not create a lesson for ordinary progress unless it changes future behavior.
- Do not hide canonical decisions in a lesson; update the canonical doc too.
- Do not present hypotheses as proven lessons.

## Output

Report the lesson path, what evidence supports it, what canonical docs were updated, and what remains tentative.
