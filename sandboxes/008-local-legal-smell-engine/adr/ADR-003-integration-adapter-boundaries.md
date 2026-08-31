# ADR-003: Integration Adapter Boundaries

**Date**: 2026-08-06  
**Status**: Accepted for Stage 002 review  
**Scope**: Sandbox 008 Stage 002 integration adapters

## Context

The user wants the local engine to be usable directly from Codex and deployable
through Python-oriented agent and Azure surfaces. Stage 001 established a
tested local API and CLI. Stage 002 adds thin integration surfaces without
creating cloud resources or moving detector logic into prompts.

## Decisions and rationale

### 1. Make the Codex skill repo-visible and thin

**Decision:** Add `skills/local-legal-smell-review/SKILL.md` and register it as
an active repo-visible skill.

**Why:** The repository is the shared source of truth for Codex, Copilot, and
Claude. The skill should teach agents how to run and interpret the engine, not
fork its detector code or hide project knowledge in a private installation.

### 2. Keep MCP optional and expose one tool over the Python API

**Decision:** Add an optional FastMCP adapter with a `review_legal_smells` tool;
keep `mcp` out of core dependencies and constrain the optional extra to
`mcp>=1.27,<2`.

**Why:** MCP is a natural shared tool surface for Codex and Foundry, but it is
an integration dependency. The upper bound follows the official SDK's current
v1-to-v2 transition guidance. The tool accepts the same nodes, edges, run ID,
and smell IDs as the local engine.

Reference: [official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

### 3. Use the Azure Functions Python v2 HTTP model as the Azure wrapper

**Decision:** Add an optional `azure-function` adapter plus a Python v2
`function_app.py` scaffold that translates a JSON request into the local engine
response and depends on `azure-functions` only when deployed or explicitly
installed.

**Why:** The current Python v2 model is decorator-based and uses
`function_app.py`, `FunctionApp`, `HttpRequest`, and `HttpResponse`. This is the
closest Azure analogue to a small Lambda-style callable while keeping the core
engine independent of the runtime.

Reference: [Microsoft Python developer reference for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python)

### 4. Treat Foundry as an orchestration/hosting consumer

**Decision:** Provide Foundry guidance for consuming the MCP server or HTTP
adapter; do not add a Foundry SDK dependency or duplicate detectors in an
agent prompt.

**Why:** The local engine must remain testable and source-traceable outside
Foundry. MCP or HTTP allows a Foundry agent to orchestrate review while the
detector result contract remains stable and independently testable.

### 5. Do not create deployment infrastructure in this stage

**Decision:** Add adapter code and deployment guidance only. Do not create an
Azure resource, publish an endpoint, add auth, or claim production readiness.

**Why:** The repository is still sandbox research. Authentication, network
exposure, rate limits, tenancy, logging, and data retention require a separate
deployment decision and must not be inferred from an adapter stub.

## Validation evidence

- Codex skill validator: passed.
- Skill forward-test: completed against `fixtures/positive.jsonl`; no files
  changed by the validation agent.
- Local engine and adapter suite: 7 tests passed.
- Azure `function_app.py` scaffold: syntax parsed locally; Azure runtime not installed.
- MCP SDK installation and live transport: not run.
- Azure Functions Core Tools execution: not run.
- Real Foundry connection or hosted endpoint: not created or run.

## Follow-up checklist

- [ ] Install and smoke-test the MCP optional extra in an isolated environment.
- [ ] Exercise stdio and/or streamable HTTP transport.
- [ ] Run the Azure wrapper under Azure Functions Core Tools.
- [ ] Decide authentication and authorization before any hosted endpoint.
- [ ] Connect a synthetic Foundry agent/tool call after the transport is validated.
- [ ] Keep detector calibration and source-layer policy ahead of production hosting.
