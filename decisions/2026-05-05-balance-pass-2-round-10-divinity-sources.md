# Balance-pass #2 Numbers-phase Round 10/10 — Divinity source escalation hooks

- **Status:** Accepted
- **Date:** 2026-05-05
- **Reversibility:** Medium (numeric source counts; reshape requires re-running aux-build feasibility math)
- **Phase touched:** Numbers (closes Numbers-phase Follow-up #13 arc)

## Context

Confirmed 4-Divinity floor across the match-arc:
- R10 boss = +1 Div
- R15 boss = +1 Div
- R30 final boss = +1 Div
- Match-completion (victory) = +1 Div

Total 4 Div guaranteed on win-path. The 6-Div cap (per Round 7 currency-budget audit: max-aux + 1-Fusion = 5 Div ✓; max-Fusion no-aux = 6 Div ✓) requires headroom above the floor for high-skill expression and PvP-IW Send-for-Interest unlock (+1 Div one-time slot per Round 8).

Round 10 binds the **2 escalation sources** that fill the floor → cap headroom.

## Decision

### Source 5 — Perfect-Wave Bonus (+1 Div per boss-wave with zero leak)

**Trigger:** Clear R10, R15, or R30 boss wave with zero creeps reaching base (zero leak; lives untouched on that wave). Each boss wave evaluated independently.

**Magnitude:** +1 Divinity per perfect boss-wave clear, additive to base boss drop. Maximum +3 Divinity across a full match (perfect R10 + perfect R15 + perfect R30).

**Scope:** All 6 modes. PvP-IW + PvP-Maze: per-side perfect-wave evaluation (each side scores independently).

### Source 6 — First-Hybrid Construction Bonus (+1 Div one-shot)

**Trigger:** Build the first hybrid tower of the match per locked hybrid adjacency topology. "Hybrid" = a tower spawned by the cross-civ adjacency rule that produces a true hybrid type, not merely placing two same-civ towers adjacently.

**Magnitude:** +1 Divinity, one-shot per match (not per player in co-op — first across the team).

**Scope:** All 6 modes. PvP-IW + PvP-Maze: per-side (each side has its own first-hybrid bonus).

### Total Divinity ceiling

| Source | Floor | Max | Typical expert |
|---|---|---|---|
| R10 boss | 1 | 1 | 1 |
| R15 boss | 1 | 1 | 1 |
| R30 final boss | 1 | 1 | 1 |
| Match-completion | 1 | 1 | 1 |
| Perfect-Wave | 0 | 3 | 1–2 |
| First-Hybrid | 0 | 1 | 1 |
| **Total** | **4** | **8** | **5–6** |

Realistic expert match yield: 5–6 Divinity. Sits at-or-above 6-cap headroom (Round 7: max-Fusion no-aux = 6 Div) while preserving scarcity — the cap is genuinely reachable but not trivial.

### Cross-validation

- **PvP-IW Send-for-Interest feasibility:** 1 Div unlock (one-time) + Damage Bonus 1 Div + base 4 Div floor = 2 Div spent / 4 Div total → fits floor without escalation. Expert with perfect-wave R10 + first-hybrid bonus = +2 Div = 6 Div total = aux-build full ceiling. Confirmed feasible.
- **Hardcore winnability:** Floor 4 Div + perfect-wave bonuses gated by Round 9 skill-bar (Hardcore expert 90/80/80 thresholds required for zero-leak boss clears). Skill-bar hard-gates source escalation — novice cannot accidentally accrue ceiling.
- **Co-op Horde:** Perfect-wave shared-team trigger (one zero-leak across team = +1 Div to team Divinity pool). First-hybrid one-shot per team. Preserves per-player wallet (Round 8 Horde decision) by routing Divinity into team-shared aux pool only.

## 3x debug loop

**L1 — aggressive critique.**
- Perfect-Wave creates "save Div for boss" psychology, conflicts with current "Div as cycle currency." Counter: Perfect-Wave reward triggers ON clear, not before — doesn't change pre-clear behavior. Spending Div pre-boss is uncoupled from earning it post-boss.
- First-Hybrid is too cheap — just place two adjacent towers from different civs. Counter: hybrid topology (locked decision) requires specific cross-civ pairs, not arbitrary adjacency. Player must know which pairs spawn hybrids — meta-knowledge gate. Plus minimum 200 T spend (T1 each side) before hybrid spawns.
- Perfect-Wave at R30 is functionally guaranteed for Hardcore experts (they'll clear or lose) → +1 Div is "free" for the bracket that least needs it. Counter: Hardcore R30 zero-leak is materially harder than Hardcore R30 win — boss-spike ×5 + (k)=1.22 + leak-tolerance buffer all stack against perfectism. Empirically expect ~50% Hardcore-expert R30 perfect-clear rate.
- 8-Div ceiling exceeds 6-cap by 2 → unspent overflow risk. Counter: realistic expert is 5-6, not 8; 8 is theoretical max requiring novice-impossible perfect-runs across all three boss-waves PLUS hybrid build. Expert who hits 7+ has clear strategic surplus to spend on Fusion-stack ceiling.
- First-Hybrid in PvP-Maze creates rush-meta where both sides race to first-hybrid ASAP (turn 5-6 rather than turn 10+). Counter: Tribute floor on hybrid-eligible cross-civ T1+T1 = 200 T = ~R5 income on Easy. Rush-meta exists but is strategically interesting (early Div vs early defensive coverage tradeoff), not degenerate.

**L2 — steelman.**
- L1's R30-perfect critique is partially right but misses that R30 perfect ON HARDCORE requires the full 1.725× per-tower stack landing perfectly across the 90s round AND surviving final-boss DPS spike. Empirically: R30 Hardcore perfect ≈ 30-50% expert-rate, not 100%. Bonus is meaningful even at the tight bracket.
- L1's overflow critique is real for the 8-Div theoretical max but irrelevant for realistic 5-6 spend; worst case overflow Div is just unspent and disappears at match-end (no carry-over, per Round 3).
- PvP-Maze rush-meta is a feature, not a bug — strategic-decision lever between early-Div escalation and early-defensive consolidation.

**L3 — synthesis.**
- Lock both sources at proposed magnitudes.
- Perfect-Wave: +1 Div per boss-wave (R10/R15/R30), zero-leak gate, additive to base drop, per-side in PvP modes.
- First-Hybrid: +1 Div one-shot per match (per side in PvP), true-hybrid gate per locked topology, team-shared in co-op.
- 6 Div realistic ceiling matches design intent; 8 Div theoretical max preserves expression headroom without breaking aux-build feasibility math.

## Cascade

- §2.4a + §5.4 [LOCKED]: untouched.
- 17-item conceptual frame: untouched. Round 10 binds **Divinity source counts**, not new variables.
- Variable bindings: all unchanged. Round 10 quantifies the **earnable Divinity escalation** above the locked 4-Div floor.
- Downstream impact: Phase 5 implementation must wire perfect-wave detection (zero-leak boss-round flag) + first-hybrid detection (topology cross-reference). Both straightforward state-flag checks.

## Closes Numbers-phase Follow-up #13

This decision closes the 10-round Numbers-phase arc. All 17 conceptual-frame variables (a)-(r) + extension (s) now have ratified magnitudes. Per-tower (cd, range, attack-type variance), per-commander (effect-type variants beyond damage-floor), per-civ specialization, and per-map (good-cell authoring + wave-randomization seeds) are deferred to authoring sub-passes post-arc.

## Open follow-ups

1. **Authoring sub-pass mandate** — per-tower / per-commander / per-civ / per-map variance work scheduled post-arc. Likely 5-10 rounds each.
2. **Phase 5 telemetry hooks** — match-end scorecard surfaces all 6 Divinity sources earned + per-axis skill-bar attainment for player feedback loop.
3. **CONCEPT.md amendment pass** — roll all 10 Numbers-phase rounds + 12-round conceptual ratifications into CONCEPT.md as new §-sections. Authoring-heavy.
