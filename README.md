# Ash to Altar (working title) — TW-Commanders

Tower wars game with persistent Commander identity, age-based tower evolution within each match, and cross-lineage hybrid units. Two-dev project, AI-assisted workflow, concept phase.

**Repo:** https://github.com/BossOfThem/TW.AtoA

## Fresh Claude Code session bootstrap

```
Read in order, then state-aloud status + blockers + proposed next step before producing anything:
1. README.md (this file)
2. CLAUDE.md           — session conventions + 3x debug loop
3. CASCADE.md          — navigation spine, decisions table, current work pointer
4. HANDOFF.md          — most recent session checkpoint + copy-paste next-session prompt
5. PROGRESS.md         — step tracker (first unchecked box = next step unless paused)
6. CONCEPT.md          — vision hub (phase content in concept/phase-1..7.md)

Then wait for PM "go". One step per turn; no batching.
```

Current gate: **Step 5 — PM + friend two-browser Co-op Horde playtest**. See [`HANDOFF.md`](HANDOFF.md) for full state snapshot.

## Start here

**Every session:** [`CASCADE.md`](CASCADE.md) is the navigation spine. Open it first. Current work pointer + reading order + stage/research/decision tables all live there.

Other root docs at a glance:
- [`CLAUDE.md`](CLAUDE.md) — session conventions (cascade discipline, 3x debug loop, naming rules, what Claude should/shouldn't do).
- [`CONCEPT.md`](CONCEPT.md) — the vision anchor. 7-phase cascade. Don't silently edit.
- [`CONCEPT-GAPS.md`](CONCEPT-GAPS.md) — proposal layer cataloging intro-game baseline gaps against industry references. Ephemeral; rows migrate into CONCEPT via ratified decisions.
- [`HANDOFF.md`](HANDOFF.md) — most recent session checkpoint + copy-pasteable next-session prompt.
- [`PROGRESS.md`](PROGRESS.md) — step tracker. Fresh session reads this to know what's ticked.
- [`PLAYER-JOURNEY.md`](PLAYER-JOURNEY.md) — legacy source material feeding stage-doc drafts.
- [`stages/`](stages/) — 9 player-journey stage docs (stubs until Phase C).
- [`research/`](research/) — 6 market-research docs (stubs until Phase B).
- [`decisions/`](decisions/) — dated decision log. Every major change goes here first.
- [`admin/`](admin/) — node-graph concept-map editor (`admin/concept.json` is the structured mirror of `CONCEPT.md`).
- [`prototype/`](prototype/) — clickable design prototype (data-driven over `start.bat`).

## Critical context (read before any other doc)

**1. The Commander is the user.** "Commander" = the player's persistent identity, not an NPC. First-person player perspective everywhere.

**2. Names are placeholder.** Nothing is final unless marked `[LOCKED]`. Only the *naming conventions* in `CONCEPT.md §5.4` are locked, not specific names.

**3. Structural counts are a lean-launch floor.** **3 lineages** (Ash / Nature / Prayer), **3 tiers** (Dust / Form / Apotheosis) under an **Ash→Altar dungeon-cosmology arc**, **3 launch commanders**, **2 hybrid families** (Ash×Nature, Ash×Prayer — Nature×Prayer does NOT hybridize). Ratified 2026-04-21 (Reversibility Hard) — see [concept tightening decision](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md). The 3/3/3 shape is a lean-launch *floor*, not an expansion ceiling. Lineage + tier names are prose placeholders pending a deferred naming pass — `concept/phase-5.md §5.4 [LOCKED]` is untouched.

## Non-negotiables (hard inputs to every decision)

- **Solo must be fully great.** Multiplayer is additive, never required.
- **No pay-to-win. Ever.** Cosmetic-only monetization.
- **Two-dev team.** Content is data-driven, not hand-sculpted.
- **Cascade discipline.** Phase N+1 does not silently edit Phase N. Reopen upstream phases properly.
- **3x debug loop** on every major decision: aggressive critique → steelman → synthesis.
- **No engine / production code** before Phase 4 exits. Prototype HTML/JS exception per [`decisions/2026-04-19-design-prototype-scope.md`](decisions/2026-04-19-design-prototype-scope.md).

## Status

**Concept phase.** Cascade restructured 2026-04-19. Workflow upgrade Steps 0, 1, 1.5a shipped. `CONCEPT-GAPS.md` landed 2026-04-20 from PM playtest feedback. Workflow queue paused pending PM ratification of gap resolutions. See [`CASCADE.md`](CASCADE.md) current work pointer for what's in flight.

## Engine

Leading: **Godot 4**, 3D scene with angled orthographic camera (StarCraft/WC3 style). Not locked. Locks at Phase 4 exit.

## What is NOT in this repo

Code, art, audio, final names, final art direction, engine lock, final monetization model.

## Decisions already made (repo-level)

Cascade-waterfall concept structure · Tower Wars genre (not roguelike) · Commander as persistent identity · Solo-primary, multiplayer-additive · Premium + cosmetic monetization · PC-first, mobile deferred · Prototype HTML/JS allowed as design artifact only.
