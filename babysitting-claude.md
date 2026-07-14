# Context Freeze Prompt Template

Status: Reusable historical template, not a current agent directive. Use `skills/write-adr/SKILL.md` and current project memory rules before applying it.

Generate a "Context Freeze" ADR for this session. Use this exact structure. Keep it entirely mechanical, dense, and objective. No conversational filler.

# [ADR-XXX]: Context Freeze & Handoff

## 1. System State
* **Core Objective:** [1-sentence absolute goal]
* **Architecture Constraints:** [Tech stack, strict boundaries, patterns to follow]
* **Files Affected:** [Explicit list of file paths]

## 2. Completed Work (Do Not Re-do)
* [Component/Feature A] -> Completed in [File Path]
* [Component/Feature B] -> Completed in [File Path]

## 3. Immediate Next Mechanical Step
* **Task:** [The exact next function, file, or line to write]
* **Input Context Needed:** [Variables, APIs, or schemas to check]
* **Expected Output:** [What the next code block must do]

## 4. Forbidden Actions
* [List what the next agent must NOT refactor, change, or look at]
