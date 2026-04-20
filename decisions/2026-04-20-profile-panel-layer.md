# Decision — Profile panel + availability layer

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (scene-profile 384–401, profile CSS, `renderProfileScene()` + `confirmLogout()` JS, `Profile.writeMatchSave` mode guard)

---

## Decision

Add a dedicated Profile scene accessible from the main menu that surfaces the always-persistent profile layer separately from per-match save state. Shows username + join-date + last-mode, a 5-cell commander-progression roster (level, XP bar, cosmetic count, highlighted last-played), and a settings summary. Also: audit `Profile.writeMatchSave()` so Skirmish / Co-op / Lane Wars never write mid-match save state (only Campaign honors `matchSave` per [save-model.md](2026-04-20-save-model.md)).

## Context

Strand 1 added Profile-aware menu branching, but the profile itself was invisible to the player — they had no way to inspect XP, settings, or saves without opening Options. The save-model rails also said non-Campaign modes must never persist mid-match; `writeMatchSave` previously wrote unconditionally.

## Alternatives considered

- **Option A — Inline profile panel on the menu.** Why not: crowds the 7-button menu list and violates the click-budget floor (the menu already has 7 primary buttons).
- **Option B — Modal over the menu.** Why not: no other modals exist at this shell level, would create UX inconsistency.
- **Option C — Dedicated `scene-profile` accessed via menu button.** (Chosen.) Matches Steam/console-game patterns; scoped to its own scene so it can grow.

## Reason chosen

**Loop 1 — aggressive critique.** Grid of 5 commanders takes vertical space; a "returning" player mostly cares about their active commander's level. The settings summary duplicates what Options already shows. The `writeMatchSave` mode guard assumes `mode === "campaign"` literally — brittle if future modes like "endless" want autosave.

**Loop 2 — steelman.** The 5-commander grid gives at-a-glance progress parity (HoMM campaign-select vibe) — it's *the* visualization of "I've been playing all 5 tilts". Settings summary is read-only; Options is the edit surface. `writeMatchSave` guard is a strict allowlist; new modes deliberately opt in.

**Loop 3 — synthesis.** Ship as-coded. Follow-up: when we add mode 6 (Endless, etc.) extend the allowlist explicitly in that mode's decision entry. No CONCEPT change needed — this is instantiation of `save-model.md` + `commander-identity-floor.md`.

## Reversibility note

Easy. Profile scene + `renderProfileScene()` removable; `writeMatchSave` guard revert is one line.

## Follow-ups

- Strand 3: Options tabs real.
- Port note: Godot `ConfigFile` for profile, dedicated `ProfileScene.tscn`, `save_match_state(mode)` RPC-safe with allowlist.
