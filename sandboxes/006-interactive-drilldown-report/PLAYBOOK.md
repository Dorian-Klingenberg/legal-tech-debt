# Sandbox 006 Playbook

Status: Current working agreement; execution remains subject to the Stage 002 review gate
Date: 2026-06-05
Scope: How to explore the interactive drill-down report UX

## Purpose

This playbook defines how the owner and agents should work inside Sandbox 006.

The goal is to iterate visually and functionally without turning the sandbox into hosted product development or letting design tools become a second source of truth.

## Working Loop

### 1. Discuss Functionality With Codex

Start in conversation.

Define:

- target user,
- workflow,
- screens,
- interactions,
- data needed,
- uncertainty/limitation display,
- and what question the next artifact should answer.

Prefer real Sandbox 004 data when possible, especially `drill_down_entries.json` and `case_library.json`.

### 2. Build A Local Behavior Prototype When Useful

Use a local prototype when the question is interaction, state, or data behavior.

Allowed prototype options:

- static HTML/CSS with minimal JavaScript,
- client-side Blazor if interaction/state becomes meaningfully JavaScript-heavy,
- generated static output from a local script.

Default decision rule:

- Use static HTML/plain JavaScript for simple filtering, expand/collapse, tabs, and mode toggles.
- Use client-side Blazor when the prototype needs reusable components, typed data models, richer state, status controls, or enough interaction that plain JavaScript would become messy.

Do not add:

- hosted services,
- backend APIs,
- databases,
- authentication,
- deployment scaffolding,
- or production infrastructure.

### 3. Feed A Tight Brief To Figma Or Canva

Use design tools after the workflow and required content are clear enough.

Codex should provide a copyable design brief that includes:

- audience,
- purpose,
- required screens,
- required controls,
- content to use,
- visual tone,
- interaction states,
- and forbidden inventions.

Figma is preferred for:

- workbench layout,
- screen hierarchy,
- interaction states,
- component structure,
- responsive frame exploration.

Canva is preferred for:

- executive-facing polish,
- visual direction,
- report cover/overview concepts,
- stakeholder-friendly presentation language.

### 4. Bring Design Learning Back To The Repo

After using Figma or Canva, summarize the useful learning in repo-visible Markdown.

Record:

- what felt useful,
- what felt annoying,
- what changed the design,
- what should carry into static HTML or Blazor,
- what should be rejected,
- and links/exports if available.

Do not rely on private design-tool memory as project memory.

### 5. Implement Or Revise The Review Artifact

Codex can then implement or revise the local artifact.

The output should remain:

- local,
- static or client-side only,
- reviewable,
- source-traceable,
- and driven by repo-visible data or fixtures.

## Design Brief Template

Use this when sending work to Figma, Canva, or another design assistant:

```markdown
Design an interactive legal-tech-debt drill-down report workbench.

Audience:
Insurance compliance, product/forms, claims, and executive reviewers.

Goal:
Help a reviewer inspect findings, understand evidence and limitations, and decide what action to take next.

Do not create:
- a marketing landing page,
- a generic SaaS dashboard,
- a hosted product concept,
- or invented findings/data.

Required screens:
1. Portfolio overview
2. Finding detail
3. Evidence/source trace panel

Required controls:
- carrier filter
- smell/category filter
- severity/confidence filter
- internal/sanitized mode toggle
- role tabs
- reviewer status control

Required content concepts:
- finding headline
- carrier/source context
- severity and confidence
- paraphrased evidence summary
- source trace
- limitation/procurement/copyright note
- suggested fix
- related cases or dollar anchors when available

Visual tone:
Quiet, expert, source-traceable, professional, serious, readable. Avoid flashy marketing visuals.

Use sanitized/paraphrased evidence only. Do not paste long carrier or ISO policy text.

Question to answer:
[Insert the exact design question for this pass.]
```

## Sandbox 006 Rules

- Sandbox 004 remains the source for current drill-down content and report-generation logic.
- Sandbox 006 explores interaction and presentation.
- Static HTML is the preferred review artifact.
- Client-side Blazor is acceptable when interaction complexity justifies it.
- Figma and Canva are accelerators, not authorities.
- Repo-visible notes are mandatory for design learning worth keeping.
- No hosted implementation unless a future sandbox explicitly evaluates hosting.
