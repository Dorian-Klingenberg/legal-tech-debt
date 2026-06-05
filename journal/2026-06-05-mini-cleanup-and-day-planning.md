# 2026-06-05 - MINI cleanup and day planning

## What Changed

- Reviewed MINI's agent-configuration cleanup as a documentation review.
- Kept the useful operating-model and journal-location changes.
- Fixed the remaining bad repo-relative Sandbox 002 run paths in root startup files.
- Unified the cross-agent startup order so Claude constraints are first for Claude Code, followed by the shared startup/context/operating-model docs.
- Clarified that `BACKLOG.md` is active work tracking and top-level `journal/` entries are point-in-time history.

## Why

MINI had not received a tight enough handoff, so the review was not a fair test of its capability. The cleanup focused on converting the useful work into durable shared instructions and removing the few things that could trip a fresh agent.

## Current State

- Sandbox 002, 003, and 004 remain complete/preserved.
- Current forward lane remains a choice between BACKLOG-019 and BACKLOG-015.
- Root startup docs now point to the real preserved run path: `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/`.

## Day-Planning Note

Recommended next decision: choose whether today is a code/detector day (BACKLOG-019) or research/product-evidence day (BACKLOG-015).
