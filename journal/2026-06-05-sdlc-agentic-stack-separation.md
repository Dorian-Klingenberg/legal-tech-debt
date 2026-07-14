# 2026-06-05 - SDLC and agentic product stack separation

## Summary

Captured a project-level separation-of-concerns rule for the future development SDLC stack and the future agentic product stack.

## What Changed

- Added `SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md`.
- Added `ADR-012-separate-sdlc-stack-from-agentic-product-stack.md`.

## Decision

The project will keep two related but separate technology stacks:

- Development SDLC stack: the engineering and governance system used to plan, build, test, trace, release, and maintain the product.
- Agentic product stack: the product runtime that ingests documents, retrieves evidence, runs detectors, assists reviewers, drafts reports, and logs product actions.

Accepted principle:

> The SDLC stack builds and governs the product. The agentic stack is part of the product being governed.

## Why

The project uses development agents today, and the future product may include product agents. Those agents need different permissions, memory, validation, audit, and safety models. Recording the distinction now prevents Phase A planning from confusing development workflow with product runtime architecture.

## Current State

This is a planning/architecture boundary only. It does not implement an SDLC stack or product agent runtime. Phase A should turn the principle into requirements, concept-of-operations documents, validation gates, and permission models.

## Validation

Documentation-only change. No code or detector validation was run.
