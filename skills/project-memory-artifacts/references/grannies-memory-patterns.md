# Grannies Memory Artifact Patterns

This reference captures patterns observed in `grannies-house-trials` for project memory artifacts. Use it when the user wants this project's memory style to resemble that system.

## Core Pattern

- Human-readable canonical docs explain the project.
- A compact machine-readable context file gives agents a fast ingest target.
- Handoffs are point-in-time snapshots, not the canonical source of truth.
- Journals describe what happened in a session or day.
- Lessons preserve reusable understanding and may be surfaced by tooling.
- Agent instruction files force the startup reading ritual.

## Startup Memory

The agent entry file tells agents to read the key docs before acting. A machine-readable context file can include:

- schema
- project
- mission
- north star
- current focus
- do-not-build-yet list
- scenario or active scope
- implementation notes
- canonical docs
- startup order

## Handoff Shape

Use for context transfer, resume points, stage transitions, or major framing changes.

Recommended sections:

- Purpose or Scope
- Current State
- User-Requested Behavior
- Implemented Changes
- Validation Performed
- Known State
- Known Gaps or Drift
- Suggested Next Steps
- Primary Files To Read First

Keep the handoff factual and dated. Include what was not validated.

## Journal Shape

Use for session/day records.

Recommended sections:

- Session Summary
- What We Did
- Why This Matters
- Validation Performed
- Current State
- What Comes Next

Journals can be warmer and more narrative than handoffs, but they should still include concrete changes and validation.

## Lesson Shape

Use when a result should teach future collaborators or agents.

Recommended sections:

- Problem
- Why It Matters
- Implementation or Pattern
- Runtime Sequence or Workflow
- Evidence / Validation
- Current Limitations
- What We Learned
- What To Reuse Next Time

Sequence diagrams are useful when a lesson explains flow, lifecycle, or component interaction.

## Discovery Surfaces

When adding artifacts, update the places future agents will actually read:

- handoff index or README
- lesson catalog or plan
- sandbox README or roadmap
- skill registry
- agent bootstrap/context files

