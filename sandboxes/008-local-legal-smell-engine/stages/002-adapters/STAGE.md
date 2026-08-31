# Stage 002: Integration Adapters

**Status**: Implemented as local adapter stubs; deployment validation not run  
**Depends on**: Stage 001 local engine

## Checklist

- [x] Add a repo-visible Codex skill over the local engine.
- [x] Add an optional MCP server adapter.
- [x] Add an optional Azure Functions HTTP adapter.
- [x] Add an Azure Functions Python v2 `function_app.py` scaffold.
- [x] Document Microsoft Foundry integration through MCP or HTTP.
- [x] Keep all optional dependencies outside the core runtime.
- [ ] Install and exercise the MCP SDK locally.
- [ ] Run the Azure Functions adapter under Azure Functions Core Tools.
- [ ] Connect a real Foundry agent or deployment endpoint.
- [ ] Add authentication, authorization, rate limiting, and deployment policy.

## Boundary

These adapters are callable surfaces around the tested local engine. They are
not production infrastructure, and no cloud resource or endpoint was created
by this stage.
