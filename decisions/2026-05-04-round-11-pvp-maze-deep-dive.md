# Decision — Round 11: PvP Maze Lane deep-dive (Accepted)

**Date:** 2026-05-04 (Round 11, later same day)
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md) (closes axis #6 hex-vs-maze conflict), [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md), CONCEPT.md §-new "Game modes: PvP Maze".

---

## Ratified (4 PM Recommended picks)

| # | Axis | Ratified value |
|---|------|----------------|
| 1 | Maze × hex reconciliation | **Hex grid preserved; towers + maze stones occupy hexes; creeps A*-path around.** Player's lane = rectangular hex region; creeps spawn one edge, exit opposite edge. **Validation rule: build cannot fully wall off the path** (server rejects placements that produce no valid path). |
| 2 | Stone economy | **Cheap stones, upgradable to T1 tower in-place.** Stones ≈ 10-20% of T1 cost (numbers-phase tunes). Upgrade-to-T1 cost = (T1 cost − stone cost). Creates "plant cheap, mature later" econ rhythm. Mirrors Line Tower Wars. |
| 3 | Send mechanic | **Send-Through-Maze.** Spend Tribute → dispatch creep through opponent's maze; reaching the end = sender accrues recurring Income. Maze-quality directly determines opponent's vulnerability. |
| 4 | Elimination | **Lives = 10, last alive wins, R30 highest-lives tiebreak** (then Tribute+Divinity). Frame-default lives count; mirrors PvE-MP. |

## Cascade implications

- **Hex grid invariant preserved across all 6 modes.** Closes open axis #6 from `2026-05-04-auxiliary-economy-and-modes-scope.md`. No separate placement physics required for Maze. Single hex placement system in engine.
- **A* path-finding becomes a load-bearing engine primitive.** Required for: PvP Maze creep routing, "build cannot wall off path" placement-validation, Send-Through-Maze creep traversal. Implementation cost amortized across these uses. Phase 4 architecture must include hex-graph A* + dynamic-edge-update on placement events.
- **Send-Creeps cross-mode classification finalized.** After Rounds 7-11: Solo NO, Horde-A NO, Horde-B NO, PvE-MP YES (Lane-Trade), PvP-IW YES (Send-for-Interest), PvP-Maze YES (Send-Through-Maze). **Send-Creeps is a 3-mode mechanic** (PvE-MP / PvP-IW / PvP-Maze). Round 6's "universal-with-variants" classification supersedes to 3-mode-with-variants.
- **Stone-upgrade-in-place** introduces a new lifecycle primitive. Frame item #5 (lifecycle Tier × Level) extends: stones become a pre-T1 lifecycle node — `Stone → T1 (in-place upgrade)` is a Maze-mode-only transition. Frame extension follow-up needed.
- **Maze-validity placement rule** is a UX concern: when does the system reject a placement? Pre-placement (gray hover hex if it would wall off) vs post-placement (place + auto-undo with feedback) — needs Round 12+ UX ratification.
- **Send-Through-Maze recurring Income** balance is delicate: if mazes are too easy to solve, senders dominate; if too hard, defenders dominate. Numbers-phase Follow-up #13 must tune the income-per-successful-traverse curve carefully.

## Per-mode summary (all 6 modes ratified)

| Mode | Lanes | Lives | Send-Creeps | Aux slots beyond Universal | Win |
|------|-------|-------|-------------|----------------------------|-----|
| Solo Campaign | 1 (authored) | 10 | — | — | R30 alive |
| Horde-A Lane Defense | N adjacent (bleed) | 10/player | — | — | R30 alive (any) |
| Horde-B Shared Front | 1 shared (N-scaled map) | 10 shared | — | — | R30 alive |
| PvE Multiplayer | N parallel | 10/player | Lane-Trade | Call-for-Help | Last alive |
| PvP Interest Wars | N (per-player, send anywhere) | 30/player | Send-for-Interest | — | Last alive (tie-escalation) |
| PvP Maze | N (per-player, send anywhere) | 10/player | Send-Through-Maze | Maze Stone | Last alive |

## Reason chosen

PM Recommended on all 4. Hex-preservation choice resolves the largest open architectural conflict in the project — single placement physics across all modes is a major engine-cost saver and a major design-coherence win. Stone-upgrade-in-place gives Maze its own econ rhythm without adding new currency. Send-Through-Maze couples maze-design quality directly to opponent vulnerability — pure design-skill expression. Lives=10 keeps Maze's stakes high and matches PvE-MP cadence; PvP-IW's lives=30 is the outlier specific to that mode's leak-tolerance feel.

## Open follow-ups for Round 12+

- Maze-validity placement UX (pre-hover gray-out vs post-placement undo).
- Stone → T1 lifecycle node frame-#5 extension.
- All-mode aux-structure UX (open axis #8): separate scene? in-match panel? right-click? between-rounds phase?
- Frame-extension variable (s) auxiliary-state (open axis #9): how do auxiliary upgrades cross-cut (a)/(c)/(e)/(f) curves in the master damage equation?
- Per-mode (k) (open axis #7): does Easy/Hard/Hardcore apply to PvP-IW + PvP-Maze, or are PvP modes player-driven-only?
- Real-time netcode architecture (Phase 4 entry concern, deferred).
- Numbers-phase Follow-up #13 (downstream of all the above).
