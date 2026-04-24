# CLAUDE.md — session conventions for Ash to Altar

Load this after [`README.md`](README.md). Reading order and stage/research tables live in [`CASCADE.md`](CASCADE.md); don't duplicate them here.

## Bootstrap (every fresh session)

1. [`README.md`](README.md) → this file → [`CASCADE.md`](CASCADE.md) → [`HANDOFF.md`](HANDOFF.md) → [`PROGRESS.md`](PROGRESS.md) → [`CONCEPT.md`](CONCEPT.md).
2. Follow the "Current work pointer" in `CASCADE.md` for what's in flight.
3. State aloud before producing anything:
   - Phase status + drift vs. last `HANDOFF.md` snapshot.
   - Open blockers (see [`CONCEPT.md §7.1`](CONCEPT.md) + any newer debt in `PROGRESS.md`).
   - The specific next-step proposal (from `PROGRESS.md` first unchecked row, or `HANDOFF.md` directive if queue is paused).
4. **Wait for PM "go" before producing any deliverable.**

## Working cadence (guided, one step at a time)

- **Propose → PM "go" → produce → verify → tick.** No batching. If a request implies batching, split it first.
- One step per turn. Each step persists an artifact (file, decision, status bump).
- Every doc that progresses updates its Status + Last-reviewed line + the matching `CASCADE.md` row.

## Handoff trigger

When the PM types **"prepare for handoff"** (or "handoff time", "wrap session", "checkpoint"):
1. Re-read `PROGRESS.md`, `CASCADE.md`, `admin/concept.json` head, `prototype/index.html` BALANCE region, `decisions/` listing.
2. Rewrite `HANDOFF.md` TL;DR + state snapshot + carried debts/blockers.
3. Bump `CASCADE.md` pointer if doc statuses changed. **Trim live docs** (see Doc hygiene below): archive old session log entries from `PROGRESS.md` and old pointer blocks from `CASCADE.md`.
4. Emit a single fenced copy-pasteable prompt for the next session after `/clear`.
5. Stop. Do not start the next step.

## Doc hygiene

Keep bootstrap files small — they load every session and burn context fast.

- **`PROGRESS.md` session log:** keep only the **3 most recent** entries. On each handoff, move older entries to `PROGRESS-archive.md` under the existing section there.
- **`CASCADE.md` current work pointer:** keep only the **most recent pointer block**. On each CASCADE bump, move older blocks to `CASCADE-history.md` under the existing section there.
- **`CASCADE.md` document version footer:** keep only the **2 most recent** version-bump sentences. Move older history to `CASCADE-history.md` under the "Archived version history" section.

Archive files are on-demand references — they are never part of the bootstrap chain.

## Cascade discipline

CONCEPT.md is a 7-phase waterfall. No decision in Phase N may violate a Phase N-1 constraint without a written override in [`decisions/`](decisions/). If a downstream decision requires a change upstream, **reopen the upstream phase properly** — do not silently edit.

Every concept-constraint change gets a dated `decisions/<YYYY-MM-DD>-<slug>.md` entry per [`decisions/TEMPLATE.md`](decisions/TEMPLATE.md).

## 3x debug loop

All major design / technical decisions:
1. **Loop 1 — aggressive critique.** Attack the proposal on every plausible failure mode.
2. **Loop 2 — steelman.** Read Loop 1 back; identify what it got wrong or overweighted.
3. **Loop 3 — synthesis.** Combine. Propose actionable direction with stop-gaps.

This is the ACCORD-pattern discipline applied to design. Do it without being asked on any CONCEPT-constraint-touching call.

## Placeholder flagging

Every name is placeholder unless explicitly `[LOCKED]`. Naming conventions in [`CONCEPT.md §5.4`](CONCEPT.md) are the only locked decisions about names. When generating new names, run them through the §5.4 convention check and flag any that break pattern.

## Commander = user

Across every doc, "Commander" is the player's persistent identity. When working on commander / unit / UI flows, adopt first-person player perspective. The Commander is not an NPC.

## No code yet

Concept-only until Phase 5 opens. Do not generate game code, engine configuration, shader pseudocode, or asset pipelines until Phase 4 exits and engine is locked. Exceptions:
- Structural docs, decision entries, design-artifact markup (tables, diagrams).
- Tooling for doc management (lint scripts, prototype editors).
- Throwaway HTML/JS in `prototype/` per [`decisions/2026-04-19-design-prototype-scope.md`](decisions/2026-04-19-design-prototype-scope.md). **Port findings, not code.**

## What Claude should do

- Refine concept docs when asked.
- Propose names following §5.4 convention.
- Flag cascade violations on sight.
- Generate design exploration / system specs when prompted.
- Run 3x debug loops on major proposals unprompted.
- Populate hybrid tables, commander rosters, age-gate UX, etc., when explicitly in scope.
- Propose engine architecture + data model as Phase 4 nears exit.

## What Claude should NOT do

- Lock any name without explicit sign-off.
- Generate game code before engine is locked and Phase 5 begins (prototype exception stands).
- Expand scope beyond `CONCEPT.md` without a written scope decision.
- Treat any placeholder as final.
- Propose monetization changes that move toward pay-to-win.
- Suggest features that violate the solo-first principle.

## Style

- Prose over bullets for analysis and design exploration.
- Tables for structured data (hybrid tables, commander rosters, mode comparisons).
- Markdown throughout.
- One document per major system when systems get large.

## Escalation

If a request requires violating any non-negotiable in `README.md` or any principle here, **stop and flag it before proceeding.** The discipline is the product.

## Help + feedback

- `/help` in Claude Code for CLI help.
- Feedback / issues: https://github.com/anthropics/claude-code/issues
