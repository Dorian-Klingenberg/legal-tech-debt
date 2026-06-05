# CLAUDE_CONSTRAINTS.md

## PURPOSE
This profile defines hard execution constraints for Claude Code in this repository.
These constraints are mandatory, non-negotiable, and always in force unless explicitly overridden by a human in the current session.

## OPERATING MODE
- Mode: `Constrained Execution`
- Priority Order:
  1. Human direct instruction in current prompt
  2. This constraints profile
  3. Existing repository instructions
- Default Action: `Do Not Act` unless explicitly authorized

## 0) REPOSITORY STARTUP AND MEMORY-TASK EXCEPTIONS

These exceptions exist so Claude Code can obey the repository startup contract without uncontrolled exploration.

### 0.1 Pre-Authorized Broad Read-Only Startup Access
When operating in this repository, Claude Code has broad read-only access during startup and context alignment for repo-visible planning, instruction, source-code, schema, and memory files.

This includes:

- root startup and agent files (`BOOTSTRAP.md`, `AGENT_CONTEXT.json`, `AGENT_OPERATING_MODEL.md`, `AGENTS.md`, `CLAUDE.md`, `CLAUDE_CONSTRAINTS.md`, `.github/copilot-instructions.md`)
- root planning and memory files (`BACKLOG.md`, `BACKLOG-IMPLEMENTATION-PLAN.md`, root `HANDOFF-*.md`, top-level `journal/*.md`)
- project skills and skill registries under `skills/`
- sandbox README, ADR, handoff, closure, stage-plan, lesson, and source-code files
- corpus indexes and manifests under `corpus/`
- schemas, deterministic pipeline code, and focused test/validation files relevant to the active task

This read access does not authorize broad write access. Edits remain limited to the active task's explicit file allowlist, user-named paths, or paths named by the current handoff/backlog plan for the item being implemented.

Avoid bulk-reading large generated outputs, `sources/`, PDFs, binary files, or full corpus content during startup unless a current handoff, backlog item, or user prompt explicitly names them.

### 0.2 Bootstrap-Named Task Context
After reading the startup context, Claude Code must read the current `latest_handoff` and `latest_backlog_plan` named in `AGENT_CONTEXT.json` when those fields are present and relevant to the active task. These files are part of startup alignment, not optional background reading.

After that startup alignment, Claude Code may read additional files only when they are both:

- named by `BOOTSTRAP.md`, `AGENT_CONTEXT.json`, an active skill, or the user; and
- relevant to the user's current task.

If relevance is unclear, stop and ask for the exact file list.

### 0.3 Explicit Memory Review Tasks
If the user explicitly asks to review or update agent instructions, shared memory, skills, handoffs, journals, or context records, Claude Code may enumerate repo-visible Markdown, CSV, and JSON documentation outside `sources/` and `output/` to identify relevant files.

Edits remain limited to the user-requested memory/instruction/skill artifacts or exact paths approved after the scan.

### 0.4 Tool Budget For Startup And Memory Tasks
The 3-tool and 60-second kill-switch applies to ordinary implementation tasks. Startup alignment and explicit memory-review tasks may exceed it only while following the scoped rules above and while making concise progress. If the task expands beyond the requested memory/context scope, stop and ask for human instruction.

## 1) CRITICAL BEHAVIOR BOUNDARIES

### 1.1 Autonomous Tool Loops: PROHIBITED
- The agent must not run repetitive or self-directed tool loops.
- The agent must not retry tools beyond one controlled retry without human approval.
- The agent must not continue tool execution chains after uncertainty is detected.

### 1.2 Directory Scanning: LIMITED
- Broad recursive exploration is forbidden during implementation unless explicitly requested in the active prompt.
- During startup/context alignment, bounded repository searches and file enumeration are allowed when limited to repo-visible planning, instruction, source-code, schema, memory, and task-relevant files.
- Avoid bulk enumeration of `sources/`, generated `output/`, binary assets, PDFs, vendored files, and archived captures unless explicitly named by the user, current handoff, or current backlog plan.
- Passive exploration behavior is disallowed after startup alignment. Implementation should follow the active task's exact file allowlist.
- Exception: Section 0.3 allows bounded documentation enumeration for explicit memory-review tasks.

### 1.3 Unprompted File Reads: LIMITED
- During startup/context alignment, Claude Code may read repo-visible planning, instruction, source-code, schema, and memory files needed to understand the active task.
- During implementation, the agent must not open unrelated files that are outside the active task's file allowlist unless the user, current handoff, current backlog plan, or relevant startup docs name them.
- If required context is missing and not covered by startup access or the task plan, ask for exact file authorization before reading.
- Exception: Sections 0.1 and 0.2 define pre-authorized startup and bootstrap-named context reads.

## 2) FILE-SYSTEM DISCIPLINE

### 2.1 Explicit Path Allowlist: REQUIRED
- The agent may only edit files whose paths are explicitly declared by the user in the current task.
- Any file path not explicitly listed is out of scope.
- Assumed or inferred target paths are forbidden.

### 2.2 File Creation: DENY BY DEFAULT
- Creating new files is prohibited unless the user explicitly requests file creation and path.
- If path or filename is ambiguous, the agent must stop and request clarification.
- Temporary files, scratch files, and convenience artifacts are prohibited unless requested.

### 2.3 File Relocation and Renames: PROHIBITED
- The agent must not move, rename, or duplicate files unless explicitly authorized.

### 2.4 Directory Integrity: ENFORCED
- The agent must not place outputs in "best guess" directories.
- The agent must not create new directories unless explicitly requested.
- The agent must preserve existing project structure exactly.

## 3) CONTEXT ALIGNMENT

### 3.1 ADR/Config Compliance: REQUIRED
- Before proposing architecture-level changes, the agent must read only the ADRs/config files explicitly named by the user.
- The agent must align recommendations to existing ADR decisions unless user requests divergence.

### 3.2 Rewrite Restriction: ENFORCED
- The agent must not rewrite ADRs, policy docs, or config baselines unless explicitly asked.
- The agent must not "improve" foundational documents without direct instruction.

### 3.3 Cross-Reference Restriction: ENFORCED
- The agent must not perform broad cross-repo reference expansion unless requested.
- The agent must not introduce unrelated standards, examples, or external frameworks.
- The agent must stay within the user-declared context boundary.

### 3.4 Context Gap Protocol
- If required source-of-truth files are unknown, the agent must ask for exact file paths.
- The agent must not guess and proceed.

## 4) KILL-SWITCH TRIGGER

### 4.1 Hard Stop Conditions
The agent must immediately stop execution and request human intervention if either condition is met:
- Elapsed active task time exceeds 60 seconds.
- Tool execution count exceeds 3 for a single task.
- Exception: Section 0.4 defines the only allowed overage for startup alignment and explicit memory-review tasks.

### 4.2 Mandatory Kill-Switch Message
When triggered, output exactly:

`KILL-SWITCH: Execution halted. Task exceeded constraint threshold (time/tool limit). Human guidance required before continuing.`

### 4.3 No Autonomous Recovery
- After kill-switch activation, the agent must not continue analysis, retries, or edits.
- Resume is allowed only after explicit human instruction.

## 5) EXECUTION CHECKLIST (MANDATORY)
Before any action, the agent must verify all checks pass:
- [ ] Target file paths explicitly provided by user
- [ ] Required reads explicitly authorized
- [ ] No unauthorized file creation
- [ ] Estimated tool calls <= 3
- [ ] Estimated completion <= 60 seconds
- [ ] ADR/config alignment scope explicitly defined

If any check fails, stop and ask for human clarification.

## 6) RESPONSE FORMAT CONTRACT
- Use concise, deterministic output.
- No conversational filler.
- No speculative alternatives unless requested.
- State assumptions as a strict bullet list when unavoidable.

## 7) NON-COMPLIANCE POLICY
Any violation of this profile is a critical execution fault.
On fault detection, the agent must:
1. Stop immediately.
2. Report the exact violated rule section.
3. Request human instruction before any further action.

## 8) PINNED SESSION DIRECTIVE
Treat this document as an active runtime constraint profile when pinned in chat.
If conflicting instructions appear, ask the human to resolve priority explicitly before proceeding.
