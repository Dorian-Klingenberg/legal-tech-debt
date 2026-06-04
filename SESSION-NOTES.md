# Session Notes

This file is a running scratch-pad of items to capture in the end-of-session journal and handoff. It is not a journal — it is a prompt for writing one. Clear it after the journal is written.

Current session: 2026-06-04

---

## Items To Journal

- [ ] Sandbox 003 stage plan updated based on review of `business_owner_prospects_report.md` and `KNIC_real_world_examples_and_costs_report.md`. Changes: Stage 001 now includes business severity signal and remediation direction as annotation outputs; Stage 002 now explicitly labels patterns as industry-wide vs. carrier-specific; Stage 003 reframed around decisions and actions with dollar anchors; workflow integration added to "Does Not Do"; external feedback prerequisite checked off.

- [ ] `BACKLOG.md` created at repo root with four seeded items: Smell 5 calibration (BACKLOG-001), file extension mismatches (BACKLOG-002), Kentucky Growers SERFF search (BACKLOG-003), Stage 005 re-open conditions (BACKLOG-004).

- [ ] `KNOWN-GAPS.md` updated: KGIC entry now reflects actual 2026-06-03 search result (no entry found in SFA) and 2026-06-04 recheck blocked by site downtime.

- [ ] All four agent config files (`BOOTSTRAP.md`, `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) updated with new rule: plan/spec changes must be captured in end-of-session journal; ADRs reserved for architectural decisions only.

- [ ] `SESSION-NOTES.md` created as a running session scratch-pad.

---

## Decisions Made This Session

- Backlog tracking home: `BACKLOG.md` at repo root, visible to all agents.
- Kentucky Growers (KGIC): treated as likely not present in SFA, not "manual retrieval pending." Recheck when site is back up.
- Decision tracking policy: journals and handoffs are end-of-session artifacts; ADRs are not the vehicle for routine plan updates.

---

## Open Before Next Session

- [ ] SERFF site back up — rerun Kentucky Growers search and close or update BACKLOG-003.
- [ ] Model choice for Sandbox 003 Stage 001 (Sonnet vs. Opus).
- [ ] Prompt design review for Stage 001 LLM triage before running at scale.
