# Decision — Round 12: Aux UX + frame variable (s) + per-mode (k) + maze validity (Accepted)

**Date:** 2026-05-04 (Round 12, later same day)
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (master equation extends with variable (s)), [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md) (closes axes #6/7/8/9/10), CONCEPT.md §-new "Auxiliary economy structure" + "Game modes".

---

## Ratified (4 PM Recommended picks)

| # | Axis | Ratified value |
|---|------|----------------|
| 1 | Aux structure UX | **In-match side-panel, always visible.** Slot panel pinned to HUD during match; click slot → spend Tribute/Divinity → effect activates. Real-time access; works for PvP-IW 20s cadence + Solo paced play. Universal across all 6 modes. |
| 2 | Frame variable (s) | **First-class auxiliary-state, multiplicative.** Master damage equation extends to: `Σ_T [DPS(T) × t_engaged × matchup × passive_modifiers × status_state × (s)]`. (s) = product of active auxiliary multipliers per tower (or per-archetype scope). Single composable insertion point. |
| 3 | Per-mode (k) | **(k) is PvE-only; PvP modes player-driven-only.** Solo / Horde-A / Horde-B / PvE-MP surface Easy/Hard/Hardcore. PvP-IW + PvP-Maze do NOT — opponent skill is the difficulty axis. |
| 4 | Maze placement validity | **Pre-placement gray-out.** Hex turns invalid-color on hover if placement would wall off the path. Player sees invalid state before clicking. Mirrors existing prototype hover-preview pattern. |

## Master damage equation (frame extension)

Original (frame item #3):
```
Damage_dealt(R) = Σ_T [DPS(T) × t_engaged(T,R) × matchup × passive_modifiers × status_state]
```

**Extended:**
```
Damage_dealt(R) = Σ_T [DPS(T) × t_engaged(T,R) × matchup × passive_modifiers × status_state × s(T,R)]
```

Where `s(T,R)` = product of active auxiliary multipliers applicable to tower T at round R. Default `s = 1` (no aux active). Aux slots that grant Damage Bonus contribute multiplicative factors > 1; Economy Bonus does not affect damage equation but enters Tribute-yield equation analogously.

Aux slots that affect non-damage variables (Tower-count expansion → modifies (j); Lifecycle → modifies (l)) are **structural** and remain curve-modifying, NOT in (s). (s) is reserved for damage / yield multipliers cleanly.

## Cascade implications

- **All 10 open axes from `2026-05-04-auxiliary-economy-and-modes-scope.md` now ratified.** Decision document advances Proposed → Accepted (status update follow-up).
- **Frame extension is a non-silent edit** — this decision explicitly amends frame item #3. Frame document remains Accepted; this decision is the explicit cascade entry. No silent edit per CLAUDE.md cascade discipline.
- **(k) PvE-only** simplifies PvP balance work — PvP modes are tuned at one canonical creep-curve, not three. Rebalance load reduces by ~factor of 3 for PvP-IW + PvP-Maze.
- **In-match side-panel** is now a Phase-4 architecture requirement — HUD must support a persistent slot panel without occluding the play field. Couples to existing prototype HUD layout.
- **Pre-placement gray-out** for maze validity reuses the existing `placement-preview` ghost pattern from `prototype/index.html`. Engine port concern: A* path validity check must run synchronously at hover speed (~60Hz). For 8×N hex regions this is tractable; numbers-phase confirms perf budget.

## All 12 rounds — design state summary

The conceptual design pass for tower-vs-unit math + auxiliary economy + 6-mode ontology is **conceptually complete**. Locked surfaces:

1. **Balance-pass #1 frame** — 17 items (Round 1-5).
2. **Auxiliary economy + modes scope** — 10 axes ratified (Rounds 6 + 12), Round 6 doctrine ("Go big, no scope cuts"), 6 per-mode deep dives (Rounds 7-11), final UX + frame extension + (k) split + Maze UX (Round 12).
3. **Frame extension** — variable (s) multiplicative aux-state; per-mode lives table; per-mode aux-slot enablement; per-mode (k) applicability.

**Numbers-phase Follow-up #13** is now fully unblocked. Consumes the locked frame + extensions to produce ratified values.

## Reason chosen

PM Recommended on all 4. In-match side-panel is the only UX option that survives the PvP-IW 20s-round cadence requirement; between-rounds and separate-scene options would have forced PvP-IW exceptions. Variable (s) multiplicative is the cleanest math composition and matches design intent (most aux upgrades are bonuses, not curve replacements). PvE-only (k) cleanly separates AI-difficulty from opponent-difficulty conceptually. Pre-placement gray-out is the prototype-tested UX pattern; reuses existing ghost-preview infrastructure.

## Follow-ups (post-Round-12)

- Update `2026-05-04-auxiliary-economy-and-modes-scope.md` Status: Proposed → Accepted (all 10 axes resolved).
- CONCEPT.md amendment — §-new "Game modes" (6 modes), §-new "Auxiliary economy structure" (slot inventory + UX + currency split + per-mode enablement table), §-amend master damage equation with (s).
- Numbers-phase Follow-up #13 — fully unblocked; consumes frame + extensions.
- Phase 4 engine architecture — load-bearing concerns now: A* hex-graph + dynamic edges, real-time PvP netcode (PvP-IW/Maze), in-match side-panel HUD, view-only spectate (PvE-MP/PvP-IW), parameterized N-scaling map authoring (Horde-B), per-player-lane-bleed (Horde-A).
- `research/06-tw-subgenres.md` deep-dive (Squadron TD / Legion TD 2 / Bloons TD 6 / Element TD / Line Tower Wars / Mini-TD).
- `admin/concept.json` migration (long-deferred).
