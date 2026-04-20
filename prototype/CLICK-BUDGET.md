# Click-budget audit — Meta-UI concept-fidelity pass

**Date:** 2026-04-20
**Target:** ≤6 clicks first-time splash→in-match / ≤3 clicks returning splash→in-match
**Source:** [first-run-flow.md](../decisions/2026-04-20-first-run-flow.md)

Instrumentation: `Profile.clickCount` increments on primary nav click; reset on scene splash-entry (`goto('splash')`). Read at `goto('match')` entry.

---

## First-time profile (no `atoA.profile.v1` in localStorage)

Scene path with click count:

| # | Scene                | Action                                               | Clicks so far |
|---|----------------------|------------------------------------------------------|---------------|
| – | splash               | Auto-dismiss after 3s (or any click = 1)             | 0             |
| 1 | login                | Enter name → press **Enter** (Enter ≠ click)         | 0             |
| – | menu (first-time)    | Branch: "New Game" prominent                         | 0             |
| 1 | menu                 | Click **New Game**                                   | 1             |
| 2 | mode-select          | Click **Skirmish** card (or Tutorial)                | 2             |
| 3 | commander-pick       | Click a commander silhouette                         | 3             |
| 4 | commander-pick       | Click **Deploy**                                     | 4             |
| – | match                | In-match                                             | **4**         |

**Result: 4 clicks first-time. ≤6 target met.** Margin = 2.

If splash is click-dismissed (+1 = 5) and login name is entered by clicking a button rather than Enter (+1 = 6), budget is tight but still within the ≤6 ceiling.

---

## Returning profile (`atoA.profile.v1` present)

Scene path:

| # | Scene                | Action                                               | Clicks so far |
|---|----------------------|------------------------------------------------------|---------------|
| – | splash               | Auto-dismiss after 3s (or any click = 1)             | 0             |
| – | login                | Skipped — auto-advance to menu w/ saved name         | 0             |
| 1 | menu (returning)     | Click **Continue** (primary)                         | 1             |
| 2 | commander-pick       | Click **Deploy** (last commander pre-selected)       | 2             |
| – | match                | In-match                                             | **2**         |

**Result: 2 clicks returning. ≤3 target met.** Margin = 1.

If "Continue" launches last mode directly (one click), budget = 1. Current build requires Deploy confirm on commander-pick; that keeps the commander-identity moment even on return, so 2 is the floor we chose.

---

## Audit conclusion

Both budgets pass with margin. No menu-overnest violation. Re-audit if:
- Additional pre-match scenes are inserted (e.g., biome-select chip screen for Skirmish — currently deferred to Step 5 playtest follow-up per [age-history-flavor-mapmods.md](../decisions/2026-04-20-age-history-flavor-mapmods.md)).
- Tutorial-default-on adds a step first-time users must dismiss (currently handled in-match via first-run-toast, not a pre-match scene).

---

## Silhouette-test audit

`?silhouette-test=1` URL param or **Shift+S** on commander-pick toggles grayscale body. All 5 commander SVG silhouettes render distinguishable without lineage color:

| Commander          | Silhouette primitive           | Distinguishing shape cue                       |
|--------------------|--------------------------------|------------------------------------------------|
| Sinew (warmother)  | Hulking pike stance            | Broad shoulders + vertical pike line           |
| Ember (architect)  | Hooded caster with orb         | Tapered hood + circular focus element          |
| Forge (quartermaster)| Anvil-guard crouch           | Low center-of-mass + rectangular anvil base    |
| Crown (conductor)  | Banner-bearer upright          | Vertical banner pole + flared skirt            |
| Veil (archivist)   | Masked rogue in half-cloak     | Asymmetric cloak drape + narrow profile        |

**Pass.** Shapes are distinguishable without color — letter-overlay (A/B/C/D/E) additionally present per colorblind toggle.

---

## Co-op snapshot additive-only verification

Diff of `buildSnapshot` → `applyGuestSnapshot` this pass:

- Added field: `commander: {x, y, lineage, cd, sigActiveTtl, auraCells}` — guarded by `if (snap.commander && game.commander)` on guest; absence is safely tolerated.
- Added messages: `{type:'event-roll', id}`, `{type:'pause-vote', by, paused}`, `{type:'commander-move', x, y}`, `{type:'commander-sig'}` — each has its own `if (msg.type === …)` branch in `Net._onMessage`; unknown types are silently ignored by older peers.
- No existing field removed or retyped. **Schema is additive-only.** Guest profile is never overwritten from host state (profile lives in local storage, match state lives in `game`).

Pass.
