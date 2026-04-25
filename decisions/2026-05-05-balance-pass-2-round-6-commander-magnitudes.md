# Decision — Balance-pass #2, Round 6: Commander (h) ability magnitudes

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (item (h) commander-avatar contribution — magnitudes now bound across passive/active/signature × damage slots); [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](2026-04-27-commander-as-summoned-ability-avatar.md) (consumes ability-magnitude floor); CONCEPT.md (pending §-new "Tower-vs-Unit math"); `prototype/data/commanders.json` (downstream); Follow-up #13.

---

## Decision

The commander (h) contribution operates across three slots: **passive (always-on aura)**, **active (~30s CD)**, **signature (long CD / once-per-match)**. Round 6 binds the magnitudes for the **damage** effect-type variant; control / summon / economy variants of the same slot family are deferred to per-commander authoring sub-pass (post-Round 10). The damage variant is the baseline floor — every commander has at least these magnitudes equivalent on their three slots.

### Passive — `+15% damage to civ-matched towers, 2-cell aura`

```
passive_modifier(T, h) = 1.15  if (T.civ == commander.civ) AND (hex_distance(T, commander) <= 2)
                       = 1.00  otherwise
```

- Always-on; aura follows commander avatar position.
- Multiplicative against (c) tower damage; stacks multiplicatively with (g) matchup, (s) aux, status (q).
- Civ-gated: cross-civ towers in aura don't benefit (preserves civ-identity skill-axis from locked content skeleton).
- 2-cell hex radius covers ~7 hexes (1 center + 6 ring); typical tower roster of 8 placements means ~3–5 are in-aura at expert positioning. Expert vs casual delta ≈ 30% (3 in-aura) → ≈ 75% (5 in-aura) of own-civ towers benefiting; closes ~5–10% of total damage output.

### Active — `Damage burst: 4× T3 DPS in 3-cell radius for 4s, 30s CD`

```
active_burst_damage = 4 × T3_DPS × 4s = 4 × (9.0 × T1_base) × 4 = 4 × 180 × 4 = 2,880 burst damage
                      (using T1_base = 20 dmg/sec from Round 5)
```

- Re-targetable; player-cast on demand.
- Affects all runners in 3-cell radius (~19 hexes) for the 4-second duration.
- Scales with R indirectly via T3_DPS reference (which is Round 5's per-tier ladder anchor — 9× T1_base).
- Uptime = 4s / 30s = ~13.3% — feeds the skill-bar ability-uptime axis (Round 9 thresholds) cleanly.
- Burst sizing: 2,880 damage clears 6 R10 std runners (442 HP each) or ~3.4× R15 std runners (919 HP) or chunks ~6.7% off R30 final boss (42,925 HP). Meaningful but not boss-deciding alone; combos with signature + passive aura + tower DPS to clear R30.

### Signature — `Once per match: instant tier-up of one targeted tower`

```
signature_effect = promote(target, target.tier + 1)   for target.tier ∈ {T1, T2}     (free of Tribute and adjacency cost)
                 = no-op                              for target.tier ∈ {T3, T4, God} (locked out)
```

- Once per match; consumed on use.
- Bypasses **Tribute cost only** (saves 300 if used on T1→T2; saves 900 if used on T2→T3); adjacency rule (m) is not bypassed — target T1 must still be at a position where the resulting T2 is valid.
- Held-strategic-decision lever: PM uses pre-R10 boss for damage tempo, or pre-R15 elite for matchup-target prep, or pre-R20 modifier for skill-axis insulation, or holds for emergency.
- Locked out of T3→T4 promote (would be too generous — saves 2,500 Tribute = ~10% of total Easy income).
- Skill-bar ability-uptime axis credits a *correct-moment* use, not a scheduled use (Round 9 will operationalize).

### Effect-type slot variants (deferred)

The locked frame item (h) ratifies four effect types per slot: **damage / control / summon / economy**. Round 6 binds the **damage variant** as the baseline floor. Per-commander authoring (post-Round 10) substitutes control / summon / economy variants on the same slot tiers, sized to be **roughly equivalent in expected-impact** (e.g., a control-variant active that Stuns 5 runners for 3s should approximate the same wave-damage-prevented as the damage-variant burst's 2,880 damage). Equivalence math deferred to authoring; floor magnitudes are this decision.

## Context

Rounds 1–5 ratified HP curve, (k) exponents, Tribute economy, speed + per-map (j), and tower (c) DPS ladder + tier-up costs. Round 6 sizes the **commander-side** of the master damage equation:

```
Damage_dealt(R) = Σ_T [DPS(T) × t_engaged × matchup × passive_modifiers(T, h) × status_state × s]
```

The `passive_modifiers(T, h)` term is bound by the passive magnitude (commander aura). The active and signature contributions enter the equation as **additive damage events** (active burst) or **state changes** (signature tier-up shifts T's tier of a single target). The 17-item conceptual frame locks the slot count (3) and effect-type count (4) per slot — Round 6 binds the magnitudes for the damage variant.

The locked 2026-04-27 commander-as-summoned-ability-avatar decision establishes commander as a movable on-field avatar (not a static buff source) — this is what makes the 2-cell aura a placement-skill axis rather than a flat global buff.

## Alternatives considered

### Passive

- **Option A — +15% / 2-cell aura, civ-gated.** (Chosen.) Modest %, modest radius, civ-identity preserved. Closes ~5–10% damage; meaningful positioning skill axis without degenerate clustering.
- **Option B — +10% / 3-cell.** Broader, weaker. Easy to cover most lane; positioning bite reduced.
- **Option C — +25% / 1-cell.** Sharp %, very tight. Degenerate cluster meta; fights merge adjacency.
- **Option D — +15% map-wide.** Drops spatial axis; commander avatar becomes ambient flavor; conflicts with 2026-04-27 design intent.

### Active

- **Option E — 4× T3 DPS / 3-cell / 4s / 30s CD.** (Chosen.) 2,880 burst; 13% uptime; meaningful but not boss-deciding alone.
- **Option F — 3× T3 / 2-cell / 3s / 25s CD.** Tighter. 324 burst — wait, that's wrong; should be 3 × 180 × 3 = 1,620 burst. Lower dopamine; uptime 12%. Easier to balance.
- **Option G — 6× T3 / 4-cell / 5s / 45s CD.** Bigger rarer. 5,400 burst. "Rotate and coast" risk; uptime 11% reduces axis bite.
- **Option H — Status burst (no direct damage).** Pure utility. Weak vs HP wall; archetype-specific edge cases.

### Signature

- **Option I — Once-per-match instant tier-up of one tower (T1→T2 or T2→T3).** (Chosen.) Strategic-decision lever; tempo swing; no schedule degeneracy.
- **Option J — Every 5 rounds: 10× T3 DPS / 5-cell / 8s burst.** Scheduled big-damage. ~14,400 burst. Boss-rotation degeneracy.
- **Option K — Once-per-match: temporary +1 Divinity.** Economic spike. Cheapens Divinity cap.
- **Option L — Every 10 rounds: full status-proc cascade.** Predictable; boss-save degeneracy; conflicts with Round 8 Send-Creeps.

## Reason chosen

**3x debug loop synthesis:**

- *Loop 1 (critique).* Too-broad passive aura collapses positioning; too-tight degenerates to clustering. Active burst that's too big takes over the wave-clear math (commander becomes the primary damage source, not a multiplier on towers). Signature on a fixed schedule degrades to "rotate on boss rounds" with no decision axis.
- *Loop 2 (steelman).* The three slots map cleanly to three time horizons: passive = continuous spatial decision (where to stand); active = tactical decision (when to cast); signature = strategic decision (which tier-up to spike). Each slot at a magnitude that *contributes* to the damage equation without *dominating* it preserves the design intent: commander is a multiplier on the tower-roster damage core, not a replacement for it. The passive +15% / 2-cell, active 4×T3-DPS burst, and once-per-match tier-up land at modest-but-meaningful levels for each horizon.
- *Loop 3 (synthesis).* The chosen magnitudes give:
  - Passive: ~5–10% own-civ damage uplift at expert positioning; closes a slice of the Hardcore margin via continuous play.
  - Active: ~6.7% of R30 final boss HP per cast; ~3 casts during a 90s-duration R30 round = ~20% of the boss HP from active alone — meaningful chunk, not solo-clear.
  - Signature: 300–900 Tribute saved + tempo swing; held-strategic-decision; rewards correct-moment optimization (Round 9 ability-uptime axis).
  Combined with the ×54 tier ladder (Round 5), ε=0.6 placement (Round 4), 1.25× matchup (Round 1 frame), 1.2× aux (s) (Round 7 deferred), and Fusion endgame (Round 5 cost-locked at 1 Divinity), the math closes Hardcore R30 at expert play with margin = exactly what Round 2 winnability-ground projected.

PM picked Recommended on all three questions; no override notes.

## Reversibility note

**Medium.** Passive % + radius + civ-gate are 3 values. Active multiplier + radius + duration + CD are 4 values. Signature target-tier-cap is 1 value (T2 cap). All parameters in `prototype/data/commanders.json` once that data layer ratifies. *Shape* changes (passive becomes additive flat damage instead of multiplicative %, signature gains an additional charge per match, active gains scaling-with-R) would require re-ratifying Round 9 skill-bar thresholds (uptime axis depends on CD shape) and would invalidate the Round 5 ladder math.

## Cascade impact

- **Round 7 (aux economy + (s) ranges)** — (s) tuned to give ~1.2× DPS at maxed aux; combined with passive ~1.15× (in-aura) and matchup 1.25×, expert effective per-tower multiplier ≈ 1.15 × 1.25 × 1.2 = 1.725× over base. Plus active burst additive. Plus signature tier-up shifts one tower's base. Hardcore margin closes via the multiplicative stack.
- **Round 9 (skill-bar thresholds)** — ability-uptime axis bracket bands set against active 30s CD (uptime % = casts × 4s / round_duration); signature credit on correct-moment use only.
- **Round 8 (per-mode tuning)** — Send-Creeps in PvP modes interacts with commander active (active burst clears sent creeps cleanly at 2,880 damage); aux economy-sourced creep-defense uses the same magnitude floor.
- **Per-commander authoring sub-pass** (post-Round 10) — substitutes control / summon / economy effect-type variants on the three slots. Equivalence math: variant X on slot Y must be impact-equivalent to the damage-variant magnitude bound here.
- §2.4a + §5.4 [LOCKED] untouched.
- 17-item conceptual frame untouched (item (h) magnitudes for damage variant now bound; shape unchanged).
- `prototype/data/commanders.json` untouched this turn.

## Follow-ups

- **Round 7 — aux costs + (s) ranges** consumes commander multiplier stack to size (s) range.
- **Round 8 — Send-Creeps yields** sized against active-burst damage floor.
- **Round 9 — ability-uptime axis bands** verified against 30s active CD.
- **Per-commander authoring sub-pass** (post-Round 10) — control/summon/economy variant equivalence.
- **Decision-table row** added to [`CASCADE.md`](../CASCADE.md).
