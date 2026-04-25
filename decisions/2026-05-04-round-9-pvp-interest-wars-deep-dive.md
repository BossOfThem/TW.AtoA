# Decision — Round 9: PvP Interest Wars Lane deep-dive + frame-#12 lives extension (Accepted)

**Date:** 2026-05-04 (Round 9, later same day)
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (item #12 lives amended), [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md), [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md), CONCEPT.md §-new "Game modes: PvP Interest Wars".

---

## Ratified

| # | Axis | Ratified value |
|---|------|----------------|
| 1 | Round cadence | **Fixed 20s rounds, simultaneous send + defend** — every 20s a wave fires; players send creeps + place towers in real-time. Squadron TD baseline. ~10 min match length at R30. |
| 2 | Elimination | **30-leak knockout, last alive wins, R30 tie-break escalation** — each player tolerates up to 30 lane-leaks before knockout. If R30 ends with multiple alive, R30 fuses with R29 send-pressure escalating incrementally until tie breaks. "Both lose simultaneously" = **co-victory tie** (both ratified as final winners). |
| 3 | Send-targets | **Send to any opposing lane (free choice)** — maximum tactical depth. Dogpile-leader mitigation deferred to Patch-1 (leader-tax / dogpile-bonus mechanic TBD). |
| 4 | Aux slots | **All Universal + Send-for-Interest** — Targeting / Build-queue / Tower-count / Lifecycle / Damage Bonus / Economy Bonus + Send-for-Interest signature mechanic (spend Tribute → dispatch creep to opponent → sender accrues permanent recurring Income, Squadron TD pattern). Maze Stone NOT enabled. Call-for-Help NOT enabled. |

## Frame-#12 amendment — per-mode lives

Original locked value (balance-pass-#1 frame item #12): **"Lives 10 fixed across all (k)."**

**Amended:** Lives are **per-mode declarable**; default 10. PvP Interest Wars overrides to 30. Mode-table:

| Mode | Lives |
|------|-------|
| Solo Campaign | 10 |
| Horde-A Lane Defense | 10 (per-player) |
| Horde-B Shared Front | 10 (shared) |
| PvE Multiplayer | 10 (per-player) |
| PvP Interest Wars | **30** (per-player, leak-budget) |
| PvP Maze Lane | 10 (per-player; pending Round 11 confirmation) |

Per-mode (k) tuning still applies to HP-curve only (single-axis compounding rule preserved). Lives-per-mode is a static declaration, not a (k)-coupled variable.

## Tie-break escalation rule (R30 multi-alive)

When R30 completes and ≥2 players remain alive:

1. **R30+1 fusion round** — R30's wave is replayed, augmented by R29-magnitude send-pressure from each alive player onto each other alive player. All alive players fire simultaneously.
2. **R30+2** — same shape, R28-magnitude send-pressure layered.
3. **R30+N** continues, each round adding magnitude from one earlier round's send-baseline.
4. **Termination conditions:**
   - One player remaining alive → that player wins.
   - All-but-one knocked out simultaneously in same R30+N → that player wins.
   - **All remaining alive players knocked out simultaneously** → **co-victory tie** (all surviving-into-tiebreak players ratified as final winners).
5. No hard cap on R30+N rounds at concept stage; numbers-phase will tune escalation curve to ensure termination within ≈5 escalation rounds in 95th-percentile cases.

## Cascade implications

- **Send-Creeps cross-mode classification update.** After Rounds 7-9: Solo NO, Horde-A NO, Horde-B NO, PvP-IW YES (Send-for-Interest). Pending Rounds 10-11. Likely final: Send-Creeps is a 3-mode mechanic (PvE-MP / PvP-IW / PvP-Maze), not universal. Round 6's 5-mode-variants table will be superseded after Round 11.
- **Frame item #12 supersession.** This decision supersedes the universal-lives portion of `2026-05-04-balance-pass-1-conceptual-frame.md` item #12. The frame document remains Accepted; this decision is the explicit per-mode amendment. No silent edit.
- **Numbers-phase Follow-up #13 scope grows.** Send-for-Interest income-yield curve, leak-budget tuning per mode, tie-break escalation curve, and 20s-round wave-magnitude curve all enter the numbers-phase scope.
- **Engine architecture (Phase 4 exit) gains a real-time-PvP requirement.** 20s-round simultaneous-send scheduling, server-authoritative tick rate, anti-desync model. Most demanding mode for netcode. Likely the hardest engine-architectural concern of the project.
- **PvP balance is harder than PvE balance** — locked frame is PvE-tuned. PvP-IW will need its own follow-up balance-pass after numbers-phase Follow-up #13 closes.

## Open follow-ups for Round 10+

- Dogpile-leader mitigation mechanic (Patch-1+).
- Tie-break escalation curve numbers.
- Send-for-Interest income-yield curve.
- Real-time netcode architectural concern (Phase 4 entry).

## Reason chosen

PM Recommended on 3 of 4 Round 9 axes + custom expansion on elimination (30-leak knockout + tie-break escalation + co-victory tie) + explicit re-confirmation of Send-for-Interest (the mode's defining mechanic). 20s simultaneous rounds match Squadron TD's battle-tested cadence. Free-choice send-targets preserves deep tactical surface; the dogpile risk is a tractable Patch-1 problem, not a launch-blocker. Per-mode lives extension cleanly resolves the frame conflict without breaking single-mode locked values.
