# Decision — Balance-pass #2, Round 8: Per-mode tuning (Send-Creeps mode-variants + N-scaling + PvP tie-break)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-round-6-aux-economy-ratifications.md`](2026-05-04-round-6-aux-economy-ratifications.md) (binds Send-Creeps mode-variant magnitudes locked Round 6 Q4), [`decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md`](2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) (consumes 100 T tactical baseline + Divinity-priced Send-for-Interest carve-out), [`decisions/2026-05-04-round-8-horde-coop-deep-dive.md`](2026-05-04-round-8-horde-coop-deep-dive.md) (binds Horde-B linear N-scaling formula), [`decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md`](2026-05-04-round-9-pvp-interest-wars-deep-dive.md) (binds PvP-IW tie-break magnitude), [`decisions/2026-05-04-round-10-pve-mp-deep-dive.md`](2026-05-04-round-10-pve-mp-deep-dive.md) (confirms PvE-MP per-lane N=24), [`decisions/2026-05-04-round-11-pvp-maze-deep-dive.md`](2026-05-04-round-11-pvp-maze-deep-dive.md) (binds PvP-Maze N_maze + Send-Through-Maze income), [`decisions/2026-05-05-balance-pass-2-round-4-map-speed.md`](2026-05-05-balance-pass-2-round-4-map-speed.md) (defers per-mode N-scaling resolved here), CONCEPT.md (pending §-new "Auxiliary economy structure" + "Game modes" magnitudes).

---

## Decision

Round 8 binds six per-mode magnitudes consuming the universal-baseline anchors from Round 7:

| Slot variant / parameter | Mode | Magnitude |
|---|---|---|
| **Solo Offensive Wave** | Solo | 100 T → 3 Standard creeps at current R HP/speed + **+50% kill-bonus on yield(R)** |
| **PvE-MP Lane-Trade** | PvE-MP | 100 T → 3 Standard creeps at current R HP/speed + **+50% kill-bonus on yield(R)** (identical to Solo Offensive Wave) |
| **Horde Reinforce-Lane** | Horde-A + Horde-B | 100 T → **1 helper unit @ 4× R-runner HP** (= `400 · 1.16^R`); cap 1 active per send (re-cast replaces) |
| **PvP-Maze Send-Through-Maze** | PvP-Maze | 100 T → 1 Standard creep into opponent's maze; **success (reaches opponent base) → +5 T/round permanent rest-of-match to sender**; opponent kill → opponent gets yield(R) refund |
| **PvP-IW Send-for-Interest** | PvP-IW | **1 Divinity unlocks slot (one-time)** + **150 T/send** + **+3 T/round permanent rest-of-match** (regardless of kill outcome); opponent kill → opponent gets yield(R) refund |
| **Per-mode N-scaling** | All | Solo / Horde-A / PvP-IW (per-side) / PvE-MP (per-lane) = **N=24** (Round 4 baseline). Horde-B = **N = 24 × player_count (linear)**. PvP-Maze per side = **N_maze = 30** |
| **PvP tie-break (PvP-IW + PvP-Maze shared)** | PvP-IW + PvP-Maze | Post-R30 HP × **1.5^(R-30)** compound escalation R31+; **co-victory floor at R45** (any players alive = co-victors) |

## Detailed magnitudes + design rationale

### Solo Offensive Wave + PvE-MP Lane-Trade (identical archetype)

Both are kill-bonus refund variants on the Round 7 100 T tactical baseline. Per-kill yield uses `yield(R) = 5 · 1.10^R` (Round 3) with +50% bonus = `7.5 · 1.10^R` per offensive-wave creep.

**Crossover analysis (3 creeps × bonus yield):**
| R | Base yield | Bonus yield | 3-creep return | Net vs 100 T spend |
|---|---|---|---|---|
| R5 | 8 T | 12 T | 36 T | **-64 T** (heavy early-tempo cost) |
| R10 | 13 T | 19.5 T | 58.5 T | **-41.5 T** (still net loss) |
| R12-13 | ~15-16 T | ~23 T | ~70 T | **break-even region** |
| R20 | 34 T | 51 T | 153 T | **+53 T** (positive EV) |
| R30 | 87 T | 130.5 T | 391.5 T | **+291.5 T** (heavy late-snowball) |

Crossover R12-13. Early-game = tempo-acceleration cost; late-game = compound snowball reward. Spam-prevented by lane-leak penalty: if creeps leak past your towers, you eat lives AND lose Tribute. Only safe-spam play is execution-gated.

PvE-MP Lane-Trade = identical magnitudes (same kill-bonus archetype; mode just changes from solo-pacing-decision to last-alive-econ-optimization).

### Horde Reinforce-Lane

Cooperative anti-leak buffer. Helper unit sits in teammate's lane and absorbs hits from runners. Helper HP = `400 · 1.16^R` ties to runner HP curve so helper stays proportionally tanky as match scales.

**Effective leak-blocking by R:**
- R1: 464 HP / 116 HP std runner ≈ **4 runners absorbed**
- R10: 1,765 HP / 441 HP std runner ≈ **4 runners absorbed**
- R30: 34,340 HP / 8,585 HP std runner ≈ **4 runners absorbed**

Constant 4-runner leak-block across all R. Cap 1 per send (re-cast replaces) prevents helper-spam replacing tower play. Tactical recovery, not strategic substitute.

### PvP-Maze Send-Through-Maze

Asymmetric outcome lever:
- **Success path:** 100 T spend → creep reaches opponent base → sender gets **+5 T/round permanent** rest-of-match. Volume builds the snowball.
- **Failure path:** Opponent's defense kills creep → sender loses 100 T entirely; opponent gets `yield(R)` Tribute refund as defensive incentive.

**Send-cost ROI on success:**
| Send round | Remaining rounds | Total income | Net (vs 100 T) |
|---|---|---|---|
| R5 | ~25 | +125 T | **+25 T** |
| R10 | ~20 | +100 T | **break-even** |
| R20 | ~10 | +50 T | **-50 T** |
| R30 | 0+escalation | minimal | **net loss** |

Early-send compounding incentive — late-send is purely tempo (force opponent reactive defense). PvP-Maze rounds aren't strictly time-bound (continuous send-loop), so "remaining rounds" is the post-R30 escalation period.

### PvP-IW Send-for-Interest

Hybrid currency reconciles Round 6 Q2 (Divinity = match-arc unlock) + Q4 (Tribute = per-send tactical):
- **One-time:** 1 Divinity to unlock slot (couples vs Fusion menu unlock @ 2 Div = real Divinity strategy decision).
- **Per-send:** 150 T (PvP-tier above 100 T baseline; reflects PvP context).
- **Recurring income on send:** +3 T/round permanent, **regardless of kill outcome** (Squadron pattern centerpiece — every spend creates income; defense yields kill-refund).

**Send-cost ROI:**
| Send round | Remaining rounds | Total income | Net (vs 150 T) |
|---|---|---|---|
| R5 | ~25 | +75 T | **-75 T** (Squadron pattern: short-term loss, long-term snowball via volume) |
| R10 | ~20 | +60 T | **-90 T** |
| R20 | ~10 | +30 T | **-120 T** |
| R30 | escalation | minimal | **net loss** |

Single send is always net-negative. **Squadron TD's design intent is volume:** sending 5x in R5-R10 ladders the income stream up; opponent must counter-send or counter-defend to keep economic parity. Real interest rate emerges from cumulative-send pressure, not single-send ROI.

Opponent kill → opponent gets yield(R) refund (defense incentive); sender still gets recurring income (volume reward). Symmetric trade in cumulative play.

### Per-mode N-scaling

| Mode | N (buildable hexes) | Rationale |
|---|---|---|
| Solo | 24 | Round 4 baseline |
| Horde-A | 24/player (each player owns adjacent lane) | Per Round 8 deep-dive locked |
| Horde-B | **24 × player_count (linear)** | Density-per-player constant; ring-of-zones map architecture parameterized 2-8 |
| PvE-MP | 24/lane × 8 lanes | Per Round 10 deep-dive locked |
| PvP-IW | 24/side | Per Round 9 deep-dive locked |
| PvP-Maze | **30/side** | Slightly above Solo to fit stone-blocker pathing per Round 11 lock |

**Horde-B authoring impact:** parameterized map serves 2p (N=48) through 8p (N=192) via modular zone-ring architecture. Engine concern (Phase 4): one map asset, per-player-count instantiation. No 7 separate maps.

### PvP tie-break

Post-R30 escalation forces stalemate resolution. Single mechanic shared across PvP-IW + PvP-Maze.

**HP × 1.5^(R-30) compound escalation starting R31:**
| R | HP multiplier vs R30 std |
|---|---|
| R31 | 1.5× |
| R35 | 7.6× |
| R40 | 57× |
| R45 | 437× (mathematically unwinnable for any tower-stack) |

**Co-victory floor at R45:** any surviving players declared co-victors. Match length cap:
- PvP-IW: ~15 minutes (20s/round × 45) total wall-clock.
- PvP-Maze: faster (continuous send-loop, not round-paced); R45 reached on cumulative-send escalation but match-clock often shorter.

Speed (f) and other curves untouched (preserves Round 2 single-axis (k) discipline — escalation lives entirely in HP curve).

## Currency-budget audit (post-Round-8)

### Divinity drain catalog (cap 6/match)

| Drain | Cost | Round status |
|---|---|---|
| Fusion menu unlock (one-time) | 2 Div | Locked 2026-04-25 |
| Per Fusion | 1 Div | Locked 2026-04-25 |
| Damage Bonus aux | 1 Div | Round 7 |
| Economy Bonus aux | 1 Div | Round 7 |
| Tower-count expansion | 1 Div / +2 N (max 3) | Round 7 |
| **Send-for-Interest unlock** | **1 Div (one-time)** | **Round 8 (NEW)** |

**PvP-IW build feasibility (Send-for-Interest is PvP-IW-only; competes with aux on the 6-cap):**
- *PvP-IW max-Send-for-Interest + 1 Damage Bonus:* 1 (SfI unlock) + 1 (Dmg) = 2 Div ✓ leaves 4 Div for tactical aux + escalation.
- *PvP-IW SfI + Eco + N-expansion ×2:* 1 + 1 + 2 = 4 Div ✓ fits within standard 4-Div PvE-mode source floor (PvP-IW source floor TBD Round 10 — likely similar or higher given 30-leak knockout cadence).
- Note: PvP-IW has no Fusion-menu-unlock requirement enforcement (Fusion is still available; just no AI-difficulty constraint), so Fusion competes with SfI but not mandatorily.

### Tribute drain catalog impact

Per-mode aux Tribute drains added or refined:

| Mode | Aux drain | Typical/match | Note |
|---|---|---|---|
| Solo | Send-Creeps (Off-Wave) ×8-12 | ~1,000 T | Skill-gated kill-bonus refund offsets cost crossover R12+ |
| Horde-A/B | Reinforce-Lane ×3-5 | ~400 T | Co-op recovery; no income offset |
| PvE-MP | Lane-Trade ×8-12 | ~1,000 T | Same as Solo (kill-bonus refund) |
| PvP-IW | Send-for-Interest ×5-10 | ~750-1,500 T | Recurring-income volume play |
| PvP-Maze | Send-Through-Maze ×5-10 | ~500-1,000 T | Asymmetric success/fail outcome |

PvP-IW Tribute residual: 25K Easy income (assuming PvE-equivalent (a) curve in PvP — TBD Round 10 if PvP modes get separate (a) tuning) − ~10.7K tier-ups − ~1.5K Send-for-Interest = **~12.8K residual** for cycling + Call-for-Help (no — PvP-IW is not Co-op/PvE so no Call-for-Help slot).

Note: **PvP modes do not have AI-(k) per Round 12 ratification** — opponent skill IS the difficulty axis. So (a) yield curve in PvP is the locked Easy-equivalent baseline (5 · 1.10^R). PvP-specific yield-curve tuning is not on the Round 8 docket; remains an open question for post-launch telemetry.

## Context

Round 7 bound aux-slot universal baselines (Send-Creeps 100 T tactical anchor + Divinity-priced Send-for-Interest carved out for Round 8 magnitude binding) and the (s) headline magnitude. Round 8 was always slated for per-mode tuning of Send-Creeps mode-variants + per-mode N-scaling resolution (Horde-B linear formula deferred from Round 4 + PvE-MP per-lane confirmed) + PvP-IW tie-break magnitude (deferred from Round 9 deep-dive). Six magnitudes bound across 3 PM `AskUserQuestion` batches (Recommended on all 6).

## Alternatives considered (per question, summary)

**Q1 (Solo Off-Wave + PvE-MP Lane-Trade):** Recommended (3 creeps + +50% bonus) chose over (5 creeps + +25%) (more DPS pressure, overwhelms early), (2 elite + +75%) (different DPS pattern, authoring complexity), (3 creeps + +100%) (snowball degeneracy from R8+).

**Q2 (Horde Reinforce-Lane):** Recommended (1 helper @ 4× R-HP) chose over (3 helpers @ 1× R-HP each) (stack-prevention complexity), (1 helper @ flat 500 HP) (falls off late), (1 helper @ 8× R-HP, max 1/match) (commander-signature-tier weight; off-design).

**Q3 (PvP-Maze recurring income):** Recommended (+5 T/round) chose over (+10 T/round) (decisive-on-first-blood degeneracy), (+3 T/round + 200 T lump on success) (UI complexity), (+2 T/round + 50 T consolation) (low engagement).

**Q4 (PvP-IW Send-for-Interest):** Recommended (1 Div unlock + 150 T/send + +3 T/round) chose over (1 Div + 100 T + +5 T/round) (decisive-early-send degeneracy), (0 Div + 200 T + +2 T/round) (breaks Round 6 Q2 currency rule), (2 Div unlock + 100 T + +5 T/round) (Divinity-strategy domination).

**Q5 (Per-mode N-scaling):** Recommended (Horde-B linear) chose over (sub-linear sqrt) (density-per-player drops with count), (lighter linear N=18×count) (tighter runway differentiates Horde from Solo but at cost of full density-equivalence), (additive N=24+8×(count-1)) (less obvious scaling intuition).

**Q6 (PvP tie-break):** Recommended (HP × 1.5^(R-30) + R45 co-victory) chose over (×2.0^(R-30) + R40 co-vic) (over-aggressive forced resolution), (HP×1.3 + Speed×1.1 + R50) (violates single-axis (k) discipline from Round 2), (sudden-death R31) (arbitrary; conflicts with co-victory framework).

## 3x debug loop summary

Each question ran inline:
- **L1 critique** — spam-meta, snowball, currency-rule conflicts, authoring cost.
- **L2 steelman** — execution-gated skill floors, volume-based Squadron pattern, parameterized authoring, single-axis discipline.
- **L3 synthesis** — recommended values; capped where degenerate; tied to existing curves where possible (HP curve for Reinforce, yield curve for kill-bonus, single-axis for tie-break).

Full per-question loops in main thread inline.

## Reason chosen

PM Recommended on all 6. Magnitudes anchor on existing locked structure: yield(R) curve (kill-bonus crossover), HP(R) curve (Reinforce helper proportional), Round 7 currency split (Send-for-Interest hybrid), Round 4 baseline N (per-mode scaling), Round 2 single-axis (k) (tie-break HP-only). Squadron TD's volume-based recurring-income centerpiece preserved as PvP-IW headline; co-victory framework from Round 9 honored.

## Reversibility note

Medium. Magnitudes can be retuned in Patch-1 telemetry. Anchored points (yield curve, HP curve, currency split, baseline N, single-axis (k)) stay locked. Adding per-mode (a) yield curves for PvP modes (currently using PvE Easy baseline) is a future Patch-1 question, not a Round 8 reversal.

## Cascade impact

- **Round 8 closure:** all six per-mode tuning items bound.
- **Numbers-phase status:** 8 of ~10 rounds complete. Rounds 9 (skill-bar thresholds) + 10 (Divinity source escalation hooks) remaining.
- **Frame extension:** no new variables; consumes existing (a) yield curve, (e) HP curve, (j) N parameter, currency-split rules. Per-mode N-scaling formalized as `N(mode, player_count)` lookup.
- **CONCEPT.md amendment scope:** §-new "Auxiliary economy structure" + "Game modes" sections will enumerate per-mode magnitudes.
- `prototype/data/balance.json` **untouched.** Numbers-phase concept-only.
- §2.4a + §5.4 [LOCKED] + 17-item conceptual frame untouched.

## Follow-ups

- **Round 9** — Skill-bar threshold magnitudes (matchup-correctness rate / placement-coverage / ability-uptime per (k) tier).
- **Round 10** — Divinity source escalation hooks (2 TBD sources to fill 6-cap from confirmed 4-Div floor).
- **Per-mode (a) yield curve tuning (post-Round-10 / Patch-1 telemetry)** — PvP modes currently use PvE Easy baseline `yield(R) = 5 · 1.10^R`; may need separate PvP curve if telemetry shows imbalance.
- **PvP-IW source floor (Round 10 dependency)** — Send-for-Interest unlock + Damage Bonus + Economy Bonus + N-expansion competes with potential Fusion play on 6-cap; Round 10 escalation hooks must validate.
- **CONCEPT.md amendment** — §-new "Auxiliary economy structure" + "Game modes" with per-mode tables.
