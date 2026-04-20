# TW-COMMANDERS (working title)

A tower wars game with deep commander progression, age-based tower evolution within each match, and cross-lineage hybrid units. Two-dev project built with Claude Code.

## Current status

**Concept phase.** No code yet. Documents under active revision.

- `docs/CONCEPT.md` — the main design doc (7-phase cascade structure)
- `docs/PLAYER-JOURNEY.md` — player experience from login to match
- `CLAUDE.md` — Claude Code session conventions
- `README.md` — this file

## Critical context for any reader

Three things to internalize before reading any other doc in this repo:

**1. The Commander is the user.**
Across every design doc, "the Commander" refers to the player's persistent identity in the game. Commander selection at login is identity selection. The Commander carries across matches, levels up, unlocks content, and can be deployed as a Hero Unit on the battle map in supported modes. When in doubt about perspective in the docs, assume first-person player.

**2. Names are placeholder.**
Lineage names (Sinew, Ember, Forge, Crown, Veil), age names (Primal, Mudbrick, Iron, etc.), commander names, tower names, unit names, enemy names, hybrid names, fork names — all placeholder. They will be revised. Do not treat any name as final unless marked `[LOCKED]`. The only locked naming decisions are the *conventions* in `CONCEPT.md §5.4`, not the specific names themselves.

**3. Tier numbers are placeholder.**
The eleven ages are conceptual slots. They may collapse to nine. They may expand to thirteen. The five lineages may become four or six. The four divergence forks may become three. Structure is scaffolding, not spec.

## Working principles (non-negotiable until we decide otherwise)

- **Solo must be fully great.** Multiplayer is additive, not required. Do not design a game that depends on matchmaking queues filling.
- **No pay-to-win.** Ever. Cosmetic-only monetization. One misstep burns audience trust permanently.
- **Two-developer team.** All content must be data-driven, not hand-sculpted per item.
- **Cascade discipline.** Phase decisions have exit conditions. Reopen upstream phases properly when downstream decisions force a change — do not quietly edit Phase 2 constraints because Phase 5 is inconvenient.
- **3x debug loop.** Every major decision: aggressive critique → steelman → synthesis, before commit.

## Engine

Leading choice: **Godot 4**, 3D scene with angled orthographic camera (StarCraft/Warcraft III style). Not locked. Locked at end of Phase 4.

## What is NOT in this repo yet

- Code (any language)
- Art or audio
- Final names for anything
- Final art direction
- Engine lock
- Final monetization model
- Decision log (structure pending, directory to be created when first decision is recorded)

## Next actions when you come back to this repo

1. Read `CLAUDE.md` to load session conventions.
2. Read `docs/CONCEPT.md` current phase status and open blockers.
3. Look at `CONCEPT.md §Phase 7.3 Refinement priority queue`.
4. Work the top unblocked item.

## Repo-level decisions already made

- Cascade waterfall concept structure (inherited from prior TTA draft).
- Tower Wars genre (not roguelike dungeon crawler).
- Commander as persistent player identity.
- Solo-primary, multiplayer-additive scope.
- Premium + cosmetic monetization (no pay-to-win).
- PC-first, mobile deferred.

Everything else is open.
