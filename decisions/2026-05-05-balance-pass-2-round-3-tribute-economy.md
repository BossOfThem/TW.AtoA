# Decision — Balance-pass #2, Round 3: Tribute economy (a) — per-kill yield + boss lumps

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (item 4 (a) Tribute pool source — values now bound; item 15 boss reward shape — magnitudes now bound); CONCEPT.md (pending §-new "Tower-vs-Unit math"); `prototype/data/balance.json` (downstream); Follow-up #13.

---

## Decision

**Per-runner Tribute yield (constant across (k)):**

```
yield(R) = 5 · 1.10^R         per standard / swarm / elite-tag runner kill
```

R1=5.5 / R5=8 / R10=13 / R15=21 / R20=34 / R25=54 / R30=87.

Compound y=1.10 lags HP exponent (1.16 Easy / 1.19 Hard / 1.22 Hardcore) — yield grows but slower than HP wall, so late-game kills feel "less generous" relative to wave pressure, forcing tier-up engagement. Constant across (k) per **single-axis (k) rule** — Hardcore yields the same per kill as Easy, but each kill takes more time-on-fire (HP wall higher), so income tightens at higher tiers. Aspirational design under "Go big" doctrine.

**Boss-round Tribute lump magnitudes (Easy baseline; constant across (k)):**

| Round | Slot | Tribute lump | Divinity drop (locked Round 1) | Notes |
|-------|------|---------------|--------------------------------|-------|
| R10 | Boss | **250** | +1 | ≈19× R10 std yield. Mid-game windfall. |
| R15 | Elite | **400** | 0 | ≈19× R15 std yield. Compensates for 0 Divinity. |
| R30 | Final Boss | **1,500** | +2 | ≈17× R30 std yield. Climactic ("huge lump"). |

Boss-spike HP overlay (R10 ×3 / R15 ×2 / R30 ×5 from Round 1) means the boss runner itself is a special-HP entity; the per-kill yield from defeating the boss is **separate** from the lump (the lump is the round-clear reward, not the kill reward). Boss runner kill yield uses the same `yield(R)` formula above (so R10 boss kill = 13 Tribute per kill, plus the round-clear lump 250). Net R10 reward for clearing = `yield(10) × runners_count(10) + 250 + 1 Divinity`.

**No additional Tribute sources.** No R-clear bonus beyond the boss lumps. No interest carry-over (PM redirected to aux economy Round 7). Sell-refund schedule locked at Round 1 (100/90/80/70/60 + T4 cap 60% + (k)-coupled floors).

## Per-wave income trajectory (Easy, ~15 std runners avg / wave)

| R | Std kills | Boss/Elite lump | Cumulative Tribute |
|---|-----------|-----------------|---------------------|
| 1 | ~82 | — | 82 |
| 5 | ~123 | — | ~590 |
| 10 | ~194 | **+250** | ~2,400 |
| 15 | ~335 | **+400** | ~5,500 |
| 20 | ~504 | — | ~10,200 |
| 25 | ~810 | — | ~17,200 |
| 30 | ~1,305 | **+1,500** | ~25,000 |

R1→R30 cumulative ≈ **25,000 Tribute** (Easy). At Hardcore (1.22 HP), per-kill yield is identical, but HP wall is 7.6× → effective Tribute-per-second drops ~7.6× late, forcing aggressive prioritization of tier-up engagements over standard-tower spam.

## Context

The Round 1 conceptual frame locked: (a) Tribute as primary currency sourced from kills + sell-refunds + boss lump-sums (item 4); boss reward shape lump-Tribute + guaranteed Divinity at R10/R30 + lump-only at R15 (item 15); sell-refund 4-step schedule (item 13). Round 3 sets the magnitudes for the per-kill yield curve and the boss lumps. Sell-refund schedule percentages are unchanged (already locked).

PM redirected interest carry-over to aux economy (Round 7) at the close of balance-pass #1 Round 5, so Round 3 here does NOT include interest. R-clear bonuses are explicitly NOT introduced — keeps economy kill+boss-lump only.

## Alternatives considered

### Per-runner yield curve

- **Option A — y=1.10, base 5.** (Chosen.) Compound lagging HP. R30 = 87 per kill. Cumulative ≈ 25,000 Tribute (Easy). Late-game tightening matches design intent.
- **Option B — y=1.12, base 6.** Faster growth. R30=180/kill. Cumulative ≈45,000. Player over-economizes, T4 stack by R20–25, dilutes skill expression.
- **Option C — y=1.08, base 4.** Tighter. Cumulative ≈12,000. Forces extreme efficiency; Hardcore winnability bound becomes very thin via econ-starvation on top of HP-wall pressure.
- **Option D — HP-proportional 1%.** yield(R) = HP_std(R) / 100. Same shape as HP curve (y=1.16). No late-game tightening; economic pressure stays constant — loses design intent.

### Boss lump magnitudes

- **Option E — R10=250 / R15=400 / R30=1,500.** (Chosen.) Maintains locked medium/medium/huge gradient. R30 lump ≈17× R30 std yield, climactic.
- **Option F — R10=200 / R15=300 / R30=1,000 (gentler).** R30 only ~11× R30 std yield; "huge" feels less huge; reward beat at climax weakened.
- **Option G — R10=300 / R15=500 / R30=2,000 (steeper).** R30=2000 affords ~4 T4 promotes; bigger reward beat. Risk: post-boss tower-spam overload at Hardcore.
- **Option H — R10=200 / R15=400 / R30=1,500 (asymmetric).** Cuts R10 to keep "R10 is best round" out of player perception (R10 already has +1 Divinity); R15 compensates. Adds a design-narrative knob.

## Reason chosen

**3x debug loop synthesis:**

- *Loop 1 (critique).* Flat per-band yield is hand-coded, doesn't scale with HP. HP-proportional at 5% breaks economic tension (R30 wave yield > total tier-up cost in one wave). Tier-cost-anchored is chicken-and-egg with Round 4/5.
- *Loop 2 (steelman).* Compound yield with y < HP exponent is the right shape — yield rises but lags HP, so late-game kills feel "less generous" relative to wave pressure. Constant-across-(k) on yield preserves single-axis (k) rule and creates the aspirational design pattern (Hardcore = same yield, harder kills, tighter income — design intent).
- *Loop 3 (synthesis).* y=1.10, base 5 lands the right cumulative trajectory (~25K Easy) and the right late-game tightening profile. Boss lumps at 250/400/1500 maintain the locked medium/medium/huge gradient and give R30 the climactic feel justified by the 2-Divinity drop also at R30. Asymmetric Option H is design-clever but adds a narrative knob without enough payoff.

PM picked Recommended on both questions; no override notes.

## Reversibility note

**Medium.** Per-kill yield base + exponent are two-knob tuning in `prototype/data/balance.json`. Boss lumps are three-value table. Re-tuning is a config change, no frame-level impact. *Shape* changes (yield becomes per-tier-band, or boss-lump becomes percentage-of-HP) would invalidate downstream Round 5 (tower stat costs balanced against yield trajectory) and would need re-ratifying both rounds.

## Cascade impact

- **Round 5 (tower stats + tier-up costs)** consumes Easy cumulative trajectory. Tower costs sized so expected on-curve player can fund: ~15 T1 placements (R1–R10), ~5 T2-merges (R10–R15), ~3 T3-merges (R15–R20), ~2 T4 promotes (R20–R25), ~1 Fusion (R28–R30). Total expected spend ≈ 8,000–12,000 Tribute, leaving ~13,000+ for sell-refund cycling and aux economy purchases.
- **Round 7 (aux economy slot costs)** sized against Tribute headroom. Tactical slots in the cheap range (~50–250 Tribute); strategic slots (Divinity-priced) don't affect Tribute budget directly. Sustained Damage/Economy bonuses in moderate Tribute range (~500–1500) per cycle.
- **Round 8 (per-mode tuning — Send-Creeps yields)** — Send-Creeps in PvE-MP / PvP-IW / PvP-Maze pulls from Tribute pool; ratification of Send-Creeps cost-vs-yield tuning consumes this trajectory.
- **Round 9 (skill-bar thresholds)** — placement-coverage threshold ties to expected wave-clear time at expected income; matchup-correctness affects effective Tribute rate (faster kills → more standard kills before next wave triggers).
- §2.4a + §5.4 [LOCKED] untouched.
- 17-item conceptual frame untouched (items 4 + 15 now have bound magnitudes; shape unchanged).
- `prototype/data/balance.json` untouched this turn.

## Follow-ups

- **Round 5 — tower stats + tier-up costs** balanced against Easy ~25K cumulative.
- **Round 7 — aux slot costs** sized against Tribute headroom.
- **Round 8 — Send-Creeps yields per mode** consumes Tribute trajectory.
- **Round 9 — skill-bar thresholds** verifies effective income at threshold uptime.
- **Decision-table row** added to [`CASCADE.md`](../CASCADE.md).
