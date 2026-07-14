# Sandbox 005 SDLC System Selection Study

Status: Provisional Stage 001 decision; requires Stage 002 pilot evidence
Date: 2026-07-13
Scope: Development SDLC tooling for this repository only

## Executive Decision

Do not adopt Agile V, SwarmForge, or Codex CLI as the whole SDLC system.

Use a layered hybrid:

1. Keep the existing repository artifacts as the canonical control plane.
2. Borrow selected Agile V concepts for task contracts, risk-adaptive gates,
   traceability, evidence bundles, and independent verification.
3. Use Codex CLI as the first execution engine because it can run custom agents,
   subagents, reviews, sandboxed commands, and structured non-interactive output.
4. Use manual Git worktrees and a single-writer rule for the first pilot.
5. Borrow SwarmForge's role, worktree, and handoff concepts, but defer running or
   copying SwarmForge until Stage 004 evaluates it in isolation.

This is a hybrid by responsibility, not a blend of three installed frameworks.
No candidate becomes a second source of project truth.

## Why The Candidates Are Not Direct Substitutes

The three candidates solve different parts of the problem:

| Question | Best current owner |
|---|---|
| What work is authorized, why, and against which evidence? | Repo-native task contract with selected Agile V concepts |
| What must be proven before the work is accepted? | Repo-native risk and evidence contract with deterministic gates |
| Which model edits or reviews the repository? | Codex CLI initially; other agents may verify independently |
| How are concurrent roles isolated and handed work? | Manual Git worktrees first; SwarmForge-style orchestration later |
| Where does durable project truth live? | Existing repository Markdown, JSON, ADRs, journals, handoffs, and generated evidence |

Agile V is mainly a lifecycle and assurance model. SwarmForge is mainly a local
orchestrator. Codex CLI is mainly an agent runtime and automation interface.
Asking one of them to replace the other two would leave a major gap.

## Candidate Fit

`Strong`, `Partial`, and `Weak` describe fit for this repository, not overall
product quality.

| Need | Agile V | SwarmForge | Codex CLI | Sandbox 005 consequence |
|---|---|---|---|---|
| Requirement and artifact traceability | Strong | Weak | Weak by default | Borrow the trace links, keep local IDs and files |
| Risk-adaptive gates and evidence | Strong | Partial quality roles, no evidence contract | Partial through prompts and output schemas | Make the contract repo-native and enforce only proven gates |
| Experiment-derived requirements and experiment-backed V&V | Weak or unstated | Weak | Weak by default | Preserve the existing Sandbox 005 model; it is a differentiator |
| Human approval boundaries | Strong | Strong at specification handoff | Configurable approvals, but not lifecycle approval | Keep explicit human product/scope/release gates |
| Agent execution | Skills are portable; scaffold centers OpenHands | Strong multi-backend launcher | Strong Codex execution and review runtime | Start with Codex CLI without adopting another runtime |
| Role isolation and handoffs | Partial | Strong | Partial; subagents do not provide Git worktree isolation | Use one writer and manual worktrees first |
| Repo-native source of truth | Partial; scaffold adds its own task/state tree | Partial; runtime state is local but project truth is undefined | Partial; sessions are not project truth | Existing repo artifacts remain canonical |
| Model/provider portability | Strong at the skills layer | Strong backend-per-role concept | OpenAI execution engine | Keep role and artifact contracts provider-neutral |
| Current local readiness | Partial | Not ready in current WSL setup | Windows CLI works; native WSL CLI is absent | Install and verify native WSL Codex before the pilot |
| Adoption overhead | High if installed whole | Medium to high for a solo/small project | Low to medium | Adopt capabilities one at a time |

## Agile V Assessment

The Agile V organization currently exposes two materially different projects:

- `agile_v_skills`: a skills and method library for requirement architecture,
  build roles, test design, red-team verification, control matrices, and related
  disciplines.
- `agentic_agile_v`: a Python scaffold/runtime with task state, schemas, policies,
  CI gates, evidence bundles, graph traceability, and OpenHands integration.

### What Is Useful Here

- Stable IDs linking requirements, changed artifacts, tests, and evidence.
- A risk tier that changes required evidence and approval depth.
- A separate verifier role instead of relying entirely on self-review.
- Machine-readable task and evidence schemas.
- Explicit gate results, waivers, reviewer state, and approval state.
- A control matrix for tools, permissions, data, owners, and rollback.

These are close to Sandbox 005's existing task-contract and evidence-bundle
sketches. The local model is already better aligned to this project in one
important way: it records conversation and experiments as requirement origins
and treats experiments as V&V evidence.

### What Should Not Be Adopted Yet

- The complete `.agentic-agile-v` state tree. It would duplicate `BACKLOG.md`,
  `AGENT_CONTEXT.json`, journals, handoffs, and sandbox stage state.
- The fixed `AAV-####` namespace. Existing project and sandbox IDs should remain
  valid rather than being translated into a parallel numbering system.
- Compliance-readiness claims as evidence of actual certification. Alignment
  matrices and generated artifacts are not an audit or certification.
- Every role, gate, business skill, or hardware path. Most are outside this
  repository's immediate need.
- Upstream files copied verbatim before the licensing discrepancy is resolved.

### Maturity Evidence

Research snapshot at `2026-07-13`:

- The skills repository was at tag `v3.6.0`, commit
  `a7ae1994ee03f2ff3a7a5986e7c9e5fc71e743f1`.
- The scaffold main branch was at commit
  `54eaa5451fcbfe9fa1c59355584deddbf7cef342`; its latest GitHub release was
  `v2.2.0`, while `pyproject.toml` identified the Python package as `0.1.0` and
  Alpha.
- The scaffold README described the OpenHands path as an MVP with phases 0-4 of
  12 complete. Other files used stronger "production-ready" language. Treat the
  narrower MVP statement as the safer status.
- A clean temporary clone produced `366 passed` with 7 pytest warnings. Ruff,
  Ruff format checking, and mypy passed. Whole-package test coverage was 44%,
  with several runtime and integration modules lightly covered or uncovered.
- The current risk policy names five gate scripts that are absent from the
  `scripts/` directory: security, rollback, traceability, independent
  verification, and compliance validators. The current CI uses other inline or
  partial checks and passed its main quality-gate workflow.
- Daily OpenWiki update runs on the scaffold were failing on July 9-13, although
  the main Agentic Agile-V quality-gate workflow passed on July 8.

Conclusion: Agile V contains useful, working material, but the broad scaffold is
not yet evidence that this project should replace its own control model.

## SwarmForge Assessment

SwarmForge is a tmux-based local coordinator. Its runnable branches define
two-, four-, and six-role packs; `main` provides shared scripts, constitution
articles, terminal adapters, and a file-based handoff daemon.

### What Is Useful Here

- One explicit role per responsibility.
- Dedicated Git worktrees for writing roles.
- Project-local role prompts and topology configuration.
- A small, durable commit handoff protocol instead of transcript copying.
- Different model backends per role.
- Visible local sessions and restartable handoff queues.
- A two-pack/four-pack/six-pack idea that makes ceremony proportional to task
  size.

### What Should Be Borrowed Carefully

- Use only one implementation writer at a time for the initial pilot.
- Keep planner/specifier and verifier roles read-only when possible.
- Treat architecture and refactoring as review concerns for ordinary tasks,
  not permanent extra agents.
- Add more roles only when risk or parallelism earns them.
- Keep handoffs linked to commits and task IDs, but let the evidence bundle carry
  richer validation details.

### Current Fit Problems

- SwarmForge does not define the requirement, risk, evidence, or project-status
  model that Sandbox 005 needs.
- Its four-pack defaults depend on the Acceptance Pipeline Specification and
  Gherkin mutation whether or not those tools fit the task.
- Shared engineering prompts tell roles to procure the latest upstream CRAP,
  DRY, and mutation tools at startup. That is not reproducible enough for this
  project's production-aligned posture; tools must be selected and pinned.
- Its shared language-tool table currently covers Go, Clojure, and Java, while
  this repository is primarily Python and static artifacts.
- The first configured role runs in the main checkout. That is unsafe for the
  repository's currently dirty working tree unless the topology is adapted.
- The current WSL environment has Git and tmux, but lacks `zsh` and Babashka.
  It also does not have an executable native WSL `codex` command.
- The main branch contains 24 Clojure `deftest` declarations but no GitHub
  Actions workflow. The tests were not run locally because Babashka is absent.

Conclusion: SwarmForge is a good Stage 004 orchestration experiment, not the
Stage 002 starting point.

## Codex CLI Assessment

Codex CLI can currently supply the execution layer without introducing another
project-state model.

### Useful Current Capabilities

- Project instructions through `AGENTS.md`.
- Project-scoped custom agents with role instructions and per-agent settings.
- Built-in subagent orchestration and a default maximum nesting depth of one.
- Sandboxed interactive work and non-interactive `codex exec` runs.
- Read-only review through `codex review` or a verifier configuration.
- JSONL execution events and schema-constrained final output.
- Explicit approval and sandbox policies.
- A machine-readable route that can later feed evidence collection without
  making the Codex session itself canonical truth.

### Boundaries

- Codex CLI is not a requirements method or V-model implementation.
- A structured model response is not proof that a test ran; commands, exit
  codes, artifacts, and reviewer evidence still need independent capture.
- Subagents share the parent permission boundary. They do not automatically get
  separate branches or worktrees.
- Parallel writing agents can conflict. Read-heavy parallelism is the safer
  initial use.
- A second Codex thread is context-independent review, but not organizational
  or vendor independence. Higher-risk work may still benefit from a human or a
  different model/provider reviewing the deterministic evidence.

### Local Readiness

- Windows resolves `codex.exe` and reports `codex-cli 0.130.0-alpha.5`.
- WSL resolves an inaccessible Windows application path rather than a native
  executable.
- Before Stage 002, install the official standalone Codex CLI inside WSL, record
  the version, verify authentication, and run a read-only smoke test.

Suggested pilot baseline, to be created only after the preflight succeeds:

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[agents]
max_threads = 3
max_depth = 1
```

The verifier should override `sandbox_mode` to `read-only`. Model choices should
inherit the user's available default initially rather than being hard-coded into
the repository.

## Recommended Role Set

Start with three roles and one optional role:

| Role | Responsibility | Write policy |
|---|---|---|
| Lead/specifier | Turn approved intent or experiment evidence into a task contract; own scope and acceptance | Task artifacts only; no implementation code |
| Implementer | Make the smallest authorized change and collect deterministic evidence | Single implementation writer in an isolated worktree |
| Verifier | Review requirements, diff, tests, evidence, and unresolved risk from a fresh context | Read-only; returns a structured verification report |
| Researcher, optional | Gather external or repo evidence when the task has a separable research question | Read-only |

Do not start with permanent cleaner, architect, hardener, QA, compliance, or
executive agents. Invoke those concerns as checklists or temporary specialist
reviews when task risk requires them.

## Resulting Hybrid Stack

| Layer | Initial choice |
|---|---|
| Canonical truth | Existing Git, Markdown, JSON/JSONL, ADRs, backlog, journals, handoffs, and sandbox records |
| Task contract | Existing Sandbox 005 template, extended after the pilot only where evidence supports it |
| Assurance method | Agile iteration plus V-shaped traceability, risk-adaptive evidence, and human gates |
| Behavior specification | Gherkin only for stable user-visible or cross-system behavior |
| Agent runtime | Codex CLI first |
| Isolation | Manual Git worktrees and one implementation writer |
| Verification | Deterministic checks, then fresh-context verifier, then human approval where required |
| Status surface | Generated later from repo truth; never canonical |
| Future orchestration | SwarmForge-style topology or clean-room adapter, tested in Stage 004 |

## Stage 002 Pilot Decision

Stage 002 should pilot a real, bounded project task:

> Define and validate a manifest contract for the future synthetic public demo
> corpus described in `journal/2026-06-11-demo-dataset-strategy.md`, including a
> schema, one valid fixture, one invalid fixture, and a small deterministic
> validation command. Do not build the corpus itself in this pilot.

Why this task:

- It advances the production-aligned portfolio direction without adding
  infrastructure or customer data.
- Its origin is explicit project evidence and a human product decision.
- It has deterministic pass/fail behavior and a meaningful negative test.
- It can exercise task traceability, risk classification, evidence capture, and
  independent verification.
- It does not require Gherkin, which also tests the boundary against unnecessary
  ceremony.

The detailed pilot checklist is in
[`../002-manual-pilot/STAGE.md`](../002-manual-pilot/STAGE.md).

## Adoption Gates

After Stage 002:

- Adopt a field or gate only if the pilot used it to prevent ambiguity, detect a
  defect, preserve evidence, or make review materially easier.
- Remove or simplify fields that were filled mechanically and never used.
- Do not add a task database while the repo-native chain remains usable.
- Do not add more writer agents unless a measured task demonstrates safe
  parallelism.

Before running or copying SwarmForge in Stage 004:

- Resolve the absence of a detected upstream license or obtain permission.
- Run its tests in a disposable environment.
- Pin every installed tool and dependency.
- Adapt all roles to Python and this repository's existing instructions.
- Keep the main dirty checkout out of the swarm topology.
- Compare it against Codex built-in subagents plus manual worktrees on a task of
  similar size.

## Licensing Boundary

This section records adoption risk, not legal advice.

- Both Agile V repositories carry a repo-level CC BY-SA 4.0 license. The
  `agentic_agile_v` `pyproject.toml` separately declares MIT, creating an
  inconsistency that should be clarified before copying code or schemas.
- No license file or GitHub-detected license was found for SwarmForge at the
  reviewed main commit. Do not vendor or adapt its code and prompts without a
  license grant or permission.
- This study therefore borrows system concepts and independently specifies the
  local design. It does not copy upstream implementation or prompt text.

## Source Snapshot

Primary sources reviewed on 2026-07-13:

- [Agile V organization](https://github.com/Agile-V)
- [Agile V skills v3.6.0](https://github.com/Agile-V/agile_v_skills/tree/a7ae1994ee03f2ff3a7a5986e7c9e5fc71e743f1)
- [Agentic Agile V scaffold](https://github.com/Agile-V/agentic_agile_v/tree/54eaa5451fcbfe9fa1c59355584deddbf7cef342)
- [Agentic Agile V task schema](https://github.com/Agile-V/agentic_agile_v/blob/54eaa5451fcbfe9fa1c59355584deddbf7cef342/.agentic-agile-v/schemas/task-brief.schema.json)
- [Agentic Agile V evidence schema](https://github.com/Agile-V/agentic_agile_v/blob/54eaa5451fcbfe9fa1c59355584deddbf7cef342/.agentic-agile-v/schemas/evidence-bundle.schema.json)
- [SwarmForge main](https://github.com/unclebob/swarm-forge/tree/9acd54d2239fef7e41ddacd8fd30dfb0e69672fe)
- [SwarmForge four-pack](https://github.com/unclebob/swarm-forge/tree/f17aeec716ff971b1ff9e73742726466410c99fb)
- [Official Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents.md)
- [Official Codex CLI command reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- [Official Codex non-interactive mode documentation](https://learn.chatgpt.com/docs/non-interactive-mode.md)
- [Official Codex `AGENTS.md` documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md)

This is a point-in-time study. All three external projects are moving quickly;
recheck versions, licenses, and current documentation before Stage 004.
