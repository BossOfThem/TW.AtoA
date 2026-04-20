# Decision — Age-as-history flavor banner + map modifier data + auto-age-up + age-gate autosave

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Medium
**Affects:** `prototype/index.html` (#age-banner DOM + CSS, `showAgeBanner`, `ageUp` autosave hook, `AGES_DATA` read), `prototype/data/mapmods.json` **(new)**, `profile.settings.gp.autoAgeUp`

---

## Decision

Every age-gate transition fires a 2.5s cinematic banner (top-of-board) showing the age's `eraDescriptor`, lore, and signature motif from `ages.json`. Reduce-motion users get a 400ms fade instead of the animation. For Campaign mode, `Profile.writeMatchSave()` fires on age-gate crossing per [save-model.md:28](2026-04-20-save-model.md) — max 2-4 min loss window. `mapmods.json` (6 biomes: neutral/volcanic/frostfall/verdant/coastal/ruins [PROPOSAL]) defines passive match-level modifiers; Skirmish will surface biome chips in mode-select (wiring in Step 5 playtest window). Gameplay option `gp.autoAgeUp` (off by default) auto-advances age on wave-start when sufficient Knowledge is banked — "flow-first" toggle that preserves AoE ceremony by default.

## Context

Phase 10.1 concept-demo pivot specified AoE DNA for the age system — each age should *feel* like a civilizational shift, not a stat bump. `ages.json` already carried `eraDescriptor`, `color`, `motif`, `lore` fields; they were data-only and never surfaced. [save-model.md](2026-04-20-save-model.md) called for age-gate autosave as the Campaign persistence hook. PM asked for "build-vs-combat rhythm" + "spontaneity" — this strand is the *combat* half of that (spontaneity is strand 9).

## Alternatives considered

- **Option A — Age transition is a silent stat tick.** (Prior state.) Why not: the `eraDescriptor` / lore / motif were never surfaced; AoE DNA was invisible.
- **Option B — Full-screen transition cinematic.** Why not: interrupts flow; contradicts "flow-first" gameplay toggle sentiment.
- **Option C — Non-blocking top-of-board banner, 2.5s, respects reduce-motion; autosave bound to age-gate for Campaign; mapmods as data-only file now + wiring in playtest.** (Chosen.)

## Reason chosen

**Loop 1 — aggressive critique.** 2.5s banner at every age transition is 11×2.5=27.5s of banner time across a full Campaign — too much? Autosave on age-gate means a player who age-ups rapidly writes the save frequently; localStorage write churn. mapmods.json currently loaded but Skirmish mode-select chip UI deferred — half-finished.

**Loop 2 — steelman.** Age gates are not frequent (user advances when they earn Knowledge; ~1–2 per minute in a paced match). Autosave churn is negligible for localStorage (< 50KB per write, debounced implicitly by the user's pace). mapmods.json *is* loaded and exposed on `MAPMODS` — playtest Step 5 can surface them without schema churn.

**Loop 3 — synthesis.** Ship as-coded. Mapmods mode-select chip UI lives as a follow-up in the Step 5 post-playtest decision entry, not this one. Reduce-motion path is tested (400ms fade). Campaign autosave is mode-gated — Skirmish/Horde/LaneWars never trigger it per the `writeMatchSave` guard from Strand 2.

## Reversibility note

Medium. Removing the age banner CSS + JS is trivial; removing the mapmods data file is additive (MAPMODS goes null, code falls through). Autosave hook revert is one line.

## Follow-ups

- Strand 9 (this pass): spontaneity events.
- Post-Step-5: wire mapmods chip UI into Skirmish mode-select based on playtest feedback.
- Port note: Godot → `AnimationPlayer` for banner, `ConfigFile.save()` on age-gate signal for Campaign.
