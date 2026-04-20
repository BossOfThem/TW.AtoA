# Decision — Prototype pivots from throwaway to playable concept-demo

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md) (partial supersession), [`prototype/`](../prototype/) (scope expansion), [`PROGRESS.md`](../PROGRESS.md) (new Step 10 block), [`CASCADE.md`](../CASCADE.md) (pointer + decisions table).

---

## Decision

The `prototype/` single-file HTML/JS artifact is re-scoped from "throwaway design slice" to **playable concept-demo with a second life**: a PM-testable, friend-shareable browser build that runs the full 11-age arc, 5 lineages, Commander identity-floor visuals, Options/Pause/Save meta-UI, first-run/returning flow, Co-op Horde multiplayer over PeerJS, and a localStorage login/logout. It remains vanilla JS + JSON data; no build step, no engine code, no asset pipeline. The "port findings, not code" discipline for the Godot target is preserved — the prototype is not a code-reuse candidate for the engine, but it is no longer strictly discardable.

## Context

Playtest on 2026-04-20 (post-PROGRESS-Step-9 sweep) surfaced a painful mismatch: the PM saw concept docs, research, stage drafts, and a cascade-lint tool land — but the *playable* artifact was materially unchanged (one chip chooser on the Pick scene). The PM's reaction: *"nothing seems to have improved or gotten better... I thought we built this — what did we do?"* Followed by the corrective directive: *"CREATE the FULL game technically using this simple UI version so we test full functionality — login, logout, invite friend... draft the MOST complete version you can with the current context and information."* Plus the standing cadence override: *"bypass permissions aggressively."*

The project is in concept phase; `decisions/2026-04-19-design-prototype-scope.md` established the prototype as throwaway. That was correct for Phase 3 exploration — but we now need a *playable artifact the PM can share with a collaborator friend* to unblock playtest-driven findings (PROGRESS Step 5, which has been blocked on "PM has not played enough to have findings"). A richer concept-demo is the cheapest path to unblocking Step 5.

## Alternatives considered

- **Option A — Keep the throwaway-only scope; build a separate engine-spec document instead.** Rejected: the PM explicitly asked for a playable artifact they can share with a friend. A spec doc is not shareable-as-play; it's another artifact the PM has to read before doing the thing they want to do.
- **Option B — Start a minimal Godot project now.** Rejected: hard-violates the "no engine code until Phase 5" non-negotiable in [CLAUDE.md](../CLAUDE.md). Phase 5 is months away. Also: engine setup is one-person-locked (only the PM installs Godot); a browser build is zero-install for the friend.
- **Option C — Pivot the existing prototype into a playable concept-demo.** (Chosen.) Single-file HTML + JSON data + PeerJS CDN. Zero install for the friend (paste a URL). No engine code. Preserves cascade discipline: concept canon (11 ages, 5 lineages, identity floor, save model, meta-UI envelope, accessibility floor) is *implemented* rather than *described*, validating the design by exercise.

## Reason chosen

### Loop 1 — aggressive critique

- **Sunk cost.** We're about to pour N sessions of Edit/Write into a codebase we explicitly labeled throwaway. The Godot port will rewrite every line of it. N sessions spent now is N sessions NOT spent on §7.1 open blockers, research/01/02/04/05, stages 02–08, or real Phase 4 specification work.
- **Maintenance trap.** Once the PM and a friend are playing it, bugs become pressure. Bug pressure on a throwaway is a category error that absorbs cascade-editing time.
- **Balance fiction.** 55 tower rows across 11 ages × 5 lineages is 55 [PROPOSAL] numbers that nobody has playtested. Shipping them in a playable demo makes them feel authoritative; they are not.
- **Feature creep vector.** PM satisfaction with the demo will *increase* pressure to add features (matchmaking, ELO, Campaign content, audio). Each addition further entrenches a codebase we're supposed to discard.
- **Multiplayer is hard.** State-sync-over-WebRTC correctness is non-trivial. The first cross-NAT playtest will likely surface PeerJS broker flakiness, NAT-traversal failures, and reconnection edge cases. Debugging those in a throwaway is particularly thankless.
- **Security/privacy vectors.** localStorage login means usernames leak between tabs; PeerJS invite links are shareable tokens. Minor — but real.

### Loop 2 — steelman

- **The only playable artifact is the only one the PM and a collaborator can iterate on together.** Concept docs, decision entries, stage drafts — these are author→reader. A playable demo is a *coordination surface*. Two humans pointing at the same wave-11 cursor and saying "that's too slow" is worth more than any decision entry on wave pacing.
- **Implementation-as-validation catches spec bugs.** Building §3.9 Pause, §3.11 First-run, §4.1 Identity floor, §4.9 Save model — in code, playable — will catch contradictions the docs don't. The existing COVERAGE.md already names five such gaps; closing them in the demo *is* Phase 4 specification work, just in a different notation.
- **Playtest findings unblock cadence.** PROGRESS Step 5 is gated on "PM playtest findings → decisions/." Step 5 has blocked queue progression. A richer demo is the fastest path to making Step 5 landable.
- **Port findings scale with realism.** The more of the concept the prototype exercises, the more concrete the PORT-NOTES.md rows become. We're not losing Godot-port productivity; we're *increasing* it by making the idioms we port better-validated.
- **Zero-install collaborator onboarding.** The PM says the friend is a "team helper who will help me build this." If the first thing we ask the friend to do is install Godot, we've set the wrong tone. A URL is the right tone.
- **Cascade is additive, not replacement.** This decision adds Step 10 to PROGRESS; it doesn't delete any upstream step. The Phase 4 spec work still happens, informed by what we learn from the demo.

### Loop 3 — synthesis

Pivot the prototype, but bound it with four guardrails:

1. **Freeze date: 2026-05-15.** Any prototype feature not in the Phase 10.1–10.4 plan is out of scope. Post-freeze, the prototype receives bug fixes only; new concept work goes upstream (CONCEPT.md / decisions / stages).
2. **Engine code discipline preserved.** No Phase 5 engine code. Prototype stays vanilla JS. When Phase 5 opens, the prototype gets archived exactly like `tw-commanders-starter/` (legacy).
3. **All 55 tower-row numbers and every new per-commander number tagged [PROPOSAL].** The demo is a *validation fixture*, not a balance document. Numbers get ratified via per-phase `decisions/` entries if and only if playtest surfaces clear signal.
4. **Multiplayer scope capped at Co-op Horde over PeerJS.** No Lane Wars 1v1, no Campaign content, no matchmaking, no ELO, no audio assets. Login is localStorage-only (no OAuth, no server-side accounts).

This is the smallest pivot that unblocks PM × friend playtest while honoring the solo-first, no-engine-code, cascade-discipline non-negotiables.

## Reversibility note

**Medium.** To undo: delete the added scenes from `prototype/index.html`, delete `ages.json` + `enemies.json`, revert `towers.json` to 2×3, revert `commanders.json` to one playable, delete this decision entry, supersede via a new dated entry. The concept docs (CONCEPT, CONCEPT-GAPS, decisions) are not touched by this pivot, so rollback does not cascade upward. The primary cost of rollback is the PM × friend playtest experience — rolling back mid-playtest would be a trust cost, not a code cost.

## Follow-ups

- `PROGRESS.md` gains a Step 10 block (10.1 scope pivot + data, 10.2 scenes + identity floor, 10.3 Co-op PeerJS, 10.4 polish).
- `CASCADE.md` decisions table gains this row; pointer refreshed.
- `prototype/COVERAGE.md` will be swept at the end of Phase 10.4 to reflect which ⬜→🟡→✅ rows flipped.
- `prototype/PORT-NOTES.md` will gain new Godot-idiom rows for PeerJS, localStorage profile, Settings screen, Pause overlay, identity-floor CSS.
- `prototype/README.md` will gain Co-op invite instructions + Login/Logout note.
- If and when the PeerJS free broker proves flaky, file a follow-up decision entry on a self-hosted PeerServer vs Firebase Realtime DB (plan's known-unknown #7).
- If PM × friend playtest surfaces balance signal on the 55 [PROPOSAL] tower numbers, file per-phase decisions to ratify (or revise) — that is the PROGRESS Step 5 unblocking this pivot enables.
- The 2026-04-19 prototype scope decision is *partially* superseded — its "port findings, not code" clause stands; its "strictly throwaway" framing is now wrong. This entry is the supersession.
