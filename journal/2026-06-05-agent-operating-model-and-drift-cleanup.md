# 2026-06-05 - Agent operating model and drift cleanup

## What Changed

- Added `AGENT_OPERATING_MODEL.md` to define the shared role split for Codex, Claude Code, and GitHub Copilot.
- Wired the new operating model into the startup chain so all three agents can read the same role map and drift rules.
- Reaffirmed the top-level `journal/` folder as the only home for chronological journal entries.
- Labeled historical handoffs and carry-forward notes more clearly so they do not read like active guidance.

## Why

We had enough documentation depth that the remaining risk was not missing content, but conflicting current-state signals. The goal here was to make the live startup surface unambiguous:

- one truth hierarchy,
- one journal location,
- one active lane,
- and clear historical markings on older records.

## Notes

- The current active lane remains the backlog choice between BACKLOG-019 and BACKLOG-015.
- Sandbox 002, 003, and 004 remain closed/completed as recorded in the existing handoffs and context docs.
- Historical documents still preserve the work that led to the current state, but they now read as snapshots instead of active guidance.
