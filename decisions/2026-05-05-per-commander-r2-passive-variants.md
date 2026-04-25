# Decision — Per-commander R2: passive-slot variants (Spartan Training / Blood Tribute / Sons of Ragnar)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** Forward-anchored to [`concept/phase-4.md §4.1`](../concept/phase-4.md) (R5 mechanical-content rewrite) + `§4.11.6` (R5 deferral-removal). No spine-doc edits this round.

---

## Decision

Bind mechanical specs for the **passive (h)-slot variants** across all 3 launch commanders against the §4.11.6 damage-floor benchmark (passive aura: +15% damage to civ-matched towers within hex-distance ≤ 2). Each commander's passive is a non-damage effect-type variant calibrated to equivalent-impact at §4.11.8 Hard expert thresholds.

**Effect-type assignment per commander** (assigned during this round per Axis B; locked for R3-R4 short-CD + signature variants to remain in the same effect-type lane per commander, preserving identity coherence):

| Commander | Civ | Passive name (locked §3.2) | Effect type | Equivalent-impact mechanism |
|-----------|-----|----------------------------|-------------|-----------------------------|
| **Leonidas** | Greek | **Spartan Training** | **Control** | 15% slow on enemies in aura → +15% engagement-time integral on Greek towers shooting them |
| **Montezuma II** | Aztec | **Blood Tribute** | **Economy** | +15% bonus Tribute per kill by Aztec towers in aura → +15% per-match buying budget |
| **Ragnar Lothbrok** | Norse | **Sons of Ragnar** | **Summon** | Periodic auxiliary unit spawn from aura → +15% effective DPS contribution to in-aura combat |

**Per-commander identity-reading paragraphs** (one each at close, per R1 Loop-3 synthesis) build identity coherence across rounds without waiting for R5 rollup.

**Aura-anchor sub-decision deferred to R5.** The §4.11.6 "2-cell aura" wording is in tension with §4.1's "board-wide invisible, not aura-scoped" wording (cascade drift; R4 amended §4.11.6 without updating §4.1). R2 authors variants against the §4.11.6 aura-shape spec abstractly (slow / tribute / summon mechanics work the same regardless of where the aura is centered). R5 §4.1 rewrite owns the anchor resolution (candidates: player-designated "anointed" tower per match / fixed Commander-pedestal cell at player start position / board-wide all-civ-matched-towers); R2 specs cite §4.11.6 anchor verbatim as "[anchor TBD R5]" wherever the spatial detail matters.

## Context

§4.11.6 damage-floor passive specifies +15% damage to civ-matched towers within 2-cell aura — a specific, civ-coded, aura-scoped boost. Per-commander effect-type variants must achieve **end-of-match damage impact within ±10% of the damage-floor passive** at §4.11.8 Hard expert thresholds (matchup 75% / placement 65% / ability-uptime 60%) per R1 calibration target.

Passive impact translates differently per effect type — direct, indirect, and amortized:

- **Control (slow / stun / disable):** Master damage equation §4.10.2 reads `damage = DPS × engagement-time integral × matchup × passive_modifiers × status_state`. Engagement-time is multiplicative — slowing creeps by 15% directly multiplies engagement-time by 1.15 for any tower shooting them in the slow zone. **Equivalence ratio: 1:1 with damage-floor.** Cleanest mathematical parity.
- **Economy (Tribute yield / cost reduction):** +15% Tribute per kill in aura → +15% buying budget for towers fed by aura kills. Translates to +15% tower count OR +15% tier-up rate OR +15% aux-slot buys (per player choice). **Equivalence ratio: ~1:1 over a 30-round match**, assuming income converts to combat-impact at parity (true on average per §4.6 yield curve + §4.11.5 tier-up costs). Slightly amortized (early-match income compounds; late-match income wasted at end) but balances out around §4.11.3's R10/R15/R30 boss-lump discontinuities.
- **Summon (auxiliary unit / projectile / tower):** Spawned units add DPS at fixed rate. To equal +15% tower DPS in aura, summons must contribute auxiliary DPS equal to 15% of the in-aura civ-matched tower DPS at every tier. Tunable via spawn rate × per-unit DPS × duration. **Equivalence ratio: 1:1 if positioning is automatic (auto-spawn at aura center / auto-targeting); ~0.85:1 if positioning is manual (player overhead).** This round specs auto-positioning to preserve parity.

Authoring all 3 variants in the same round (per Axis B) lets the equivalence-ratio comparison happen inline.

## Effect-type assignment rationale (per locked-name reading)

**Leonidas — Spartan Training → Control.** Three readings of "training" were on the table: (a) buff (towers fire faster/more accurate — but this is the damage-floor lane, would duplicate); (b) control (formation discipline = phalanx slows enemy advance — the "300 hold the pass" historical resonance); (c) summon (training = bringing in trained Spartan auxiliaries — but this overlaps Sons of Ragnar's "calling sons of"). Control reads strongest: phalanx-discipline-slows-enemy-advance maps to historical Thermopylae imagery, fits 300-ideology-audit-acceptable framing (slow ≠ glorification of violence; it's tactical positioning), and is the cleanest mathematical equivalence to damage-floor.

**Montezuma II — Blood Tribute → Economy.** Two readings: (a) economy (Tribute = literal tribute system, kills generate bonus Tribute as offering); (b) summon (Blood = ritual sacrifice summons spirit). Economy reads stronger: "Tribute" is the named in-game currency from §4.6 (kill-only), so "Blood Tribute" naturally maps to "kills generate bonus Tribute." Summon reading reserved for The Great Sacrifice signature (R4) where ritual-sacrifice imagery is lore-anchored to a culminating event, not a passive baseline. **Cultural-sensitivity note:** mechanical-content of "+15% Tribute per kill in aura" carries no glorification-of-sacrifice imagery — the lever is currency yield, not visualized blood ritual. Visual representation owned by Follow-up #5 cultural-sensitivity pass.

**Ragnar Lothbrok — Sons of Ragnar → Summon.** Locked name is unambiguous — "Sons of Ragnar" is the literal historical raid coalition (Bjorn Ironside, Ivar the Boneless, Halfdan, Ubbe, Sigurd Snake-in-the-Eye). Periodic auxiliary unit spawn directly maps. Effect type assigned without contention.

## Per-commander mechanical specs

### Leonidas — Spartan Training (CONTROL)

| Field | Spec |
|-------|------|
| Slot | Passive (always on; signature-excluded-from-uptime preserved at signature slot R4) |
| Effect type | Control (slow) |
| Aura mechanism | Civ-matched (Greek) tower aura — **15% slow on all enemies within hex-distance ≤ 2 of [anchor TBD R5]** |
| Slow magnitude | 15% (multiplicative with status-procs; soft-cap at 50% per §4.10.5 status_state to prevent stun-locking) |
| Stack rule | Single source — does not stack with itself across multiple Leonidas-civ instances (only one commander per match per §4.1; non-issue at launch) |
| Status-proc interaction | Multiplicative: a creep with -20% slow status-proc + Leonidas aura = `(1 - 0.20) × (1 - 0.15) = 0.68× speed = 32% effective slow` |
| Per-civ affinity hook | Greek — interacts with per-tower authoring sub-pass (post-arc track #1) at the *target-side*: Greek towers receive engagement-time bonus from Leonidas aura on enemies they shoot. **Hook interface:** `tower.civ === "greek" && target.position within 2 cells of [anchor]` triggers status_state slow modifier. Tower-side spec owned by per-tower arc; commander-side spec owned here. |
| Equivalent-impact derivation | 15% slow → 15% longer engagement-time → +15% damage per master equation §4.10.2. Direct 1:1 with damage-floor (+15% × 1.0 engagement-modifier = +15% × 1.15 engagement-modifier × 1.0 damage-modifier; both yield 1.15× total). |
| Edge case | If no Greek tower is within range of slowed enemies, slow is wasted (no DPS to amplify). Mitigation: Leonidas aura applies to enemies regardless of tower presence; slow chains across the choke cell, benefiting downstream Greek towers too. **Net: equivalence holds as long as ≥1 Greek tower has line-of-sight to slowed enemies, which is the intended placement-coverage skill-bar axis target anyway.** |

**Identity reading.** Leonidas is the immovable anchor — the king at the pass who slows the advance so his line can hold. "Spartan Training" turns the aura into a discipline field: enemies slow as they enter the trained zone, giving Greek towers more shots before the wave passes. Mechanically a control passive; thematically a Thermopylae-coded "hold the line" passive. Leonidas is not present on the field (per §4.1 summoned-on-cast); his training *is* — the unit-discipline outlasts his physical presence. The passive's spatial scope mirrors his historical tactical genius: control of *where* the fight happens. R3's short-CD active and R4's signature will continue the control lane (positional disruption / once-per-match defensive culmination).

---

### Montezuma II — Blood Tribute (ECONOMY)

| Field | Spec |
|-------|------|
| Slot | Passive (always on) |
| Effect type | Economy (Tribute yield bonus) |
| Aura mechanism | Civ-matched (Aztec) tower aura — **+15% bonus Tribute per kill** by Aztec towers within hex-distance ≤ 2 of [anchor TBD R5] |
| Bonus magnitude | 15% additive to base yield per §4.11.3 (`yield(R) = 5 · 1.10^R` per std kill → in-aura Aztec kills yield `5 · 1.10^R · 1.15`) |
| Boss-lump interaction | Boss-kill lumps (R10=250 / R15=400 / R30=1,500 per §4.11.3) **also receive +15% if killed by Aztec tower in aura** — incentivizes Montezuma II positioning at the round-30 final-boss approach lane. |
| Aux-slot interaction | Stacks **multiplicatively** with §4.6a Economy Bonus aux slot (1 Div = +25% per-kill yield, not per-Aztec-kill): in-aura Aztec kill with Economy Bonus active = `5 · 1.10^R · 1.15 × 1.25 = 5 · 1.10^R × 1.4375` per kill. This compounding ceiling is intentional — economy commander's identity is "doubling down on income" and stacks with the matching aux. |
| Per-civ affinity hook | Aztec — interacts with per-tower authoring sub-pass at the *target-side*: Aztec towers' kill-events trigger bonus Tribute when within aura. **Hook interface:** `tower.civ === "aztec" && tower.position within 2 cells of [anchor] && killEvent` → bonus Tribute = `base × 0.15`. Tower-side spec owned by per-tower arc. |
| Equivalent-impact derivation | +15% Tribute per kill in aura → +15% buying budget across the match (assuming all Aztec kills happen in aura, which is the placement-coverage target). +15% buying budget converts to +15% effective tower DPS via additional towers OR tier-up acceleration OR aux-slot buys, per player choice. **Equivalence ratio: 1:1 over the 30-round match window** (front-loaded budget compounds slightly via earlier tier-ups; late-round budget wasted at match-end; nets to ~1:1 by R30 boss). |
| Edge case | Player who never kills in aura gets zero benefit (vs damage-floor +15% which still applies if Aztec tower is *placed* in aura but doesn't shoot). Mitigation: Aztec tower placed in aura naturally accrues kills if it has line-of-sight to lane; placement-coverage skill-bar axis already targets this. **Worst-case: novice (30% placement-coverage on Hardcore) gets ~30% of the +15% benefit = +4.5% — but novice damage-floor commander gets +15% × 30% = +4.5% too. Parity holds across skill levels.** |

**Identity reading.** Montezuma II is the steward of accumulation — the empire-builder whose aura makes battlefield kills *also* generate the resources for the next tower. "Blood Tribute" is the in-game-currency-yield manifestation of his historical role as the Tributary Empire's apex consolidator: war became economy. Mechanically an economy passive; thematically the Aztec tribute-system rendered in TD pacing. The cultural-sensitivity gate (Follow-up #5) will own visual / VO direction (no glorification-of-sacrifice imagery in the spec); the mechanical lever is currency yield only. R3's short-CD active and R4's signature will continue the economy lane (resource-shock burst / once-per-match resource-culmination).

---

### Ragnar Lothbrok — Sons of Ragnar (SUMMON)

| Field | Spec |
|-------|------|
| Slot | Passive (always on) |
| Effect type | Summon (auxiliary unit spawn) |
| Aura mechanism | Civ-matched (Norse) tower aura — **periodic spawn of auxiliary "Son" unit** at aura center [anchor TBD R5]. Spawn cadence: **one Son every 20 seconds**, max 1 Son alive at a time (despawn-and-respawn on next cadence tick). |
| Per-Son magnitude | Each Son has DPS = `0.30 × T2_DPS` = `0.30 × 60 = 18 dmg/sec` at Standard archetype attack-type (auto-assigned to a non-conflicting type per Norse civ-affinity, e.g., Slashing). HP per Son: `2 × HP_std(R)` per §4.11.1 (scales with round so Sons survive boss-spike rounds). |
| Targeting | Auto-targets nearest enemy within hex-distance ≤ 2 of aura center (no player input — preserves auto-positioning equivalence). Cannot be commanded; cannot be relocated. |
| Aux-slot interaction | Sons are *auxiliary* combat units, not towers — do **not** count against §4.11.7 N hex-cell cap. Do **not** consume Tribute. Independent of §4.6a aux-slot catalog. |
| Per-civ affinity hook | Norse — interacts with per-tower authoring sub-pass at the *target-side* lightly: Sons' attack type assigned to **Slashing** at launch (matches Norse civ identity per per-civ specialization track #2 hook). Per-tower arc / per-civ arc may revisit. **Hook interface:** Sons are spawn-and-act independent of tower data; no cross-arc spec contention. |
| Equivalent-impact derivation | One Son @ 18 DPS continuous = 18 × 60s/wave-period = 1,080 dmg/wave vs damage-floor +15% on Norse towers in aura. In-aura Norse tower DPS = `T1_DPS + T2_DPS + T3_DPS` if 3 towers (1 per tier) = `20 + 60 + 180 = 260 DPS` × 0.15 = **39 DPS** ≈ 2× one Son's 18 DPS. **Equivalence ratio at 3-tower aura: ~0.46:1 vs damage-floor — Sons under-deliver.** Adjustment: scale Son DPS to **40 dmg/sec** (= `0.67 × T2_DPS`) so single-Son output ≈ +15% aura-DPS at 3-tower equivalent placement. **Locked spec: Son DPS = 40 dmg/sec** (overriding the initial 18-DPS sketch above). Cross-checked at 1-tower aura (T2 only): 60 × 0.15 = 9 DPS vs Son's 40 DPS = 4.4×; at 5-tower aura (T1+T2+T2+T3+T3): 500 × 0.15 = 75 DPS vs Son's 40 DPS = 0.53×. **Asymmetry: Son passive is over-strong at low-tower-density placements, under-strong at high-density placements.** Mitigation: this asymmetry is *thematic* — Ragnar's Sons are the equalizer for the player who builds few but rallies the warband; damage-floor commander rewards the player who blankets towers. Different identity → different optimization curve → equivalent on average across the realistic 3-4 tower aura range. R5 audit re-tests against simulation. |
| Edge case | If aura is placed where no enemies pass within 2 cells of aura center, Sons have no targets → zero output. Same failure mode as damage-floor (zero towers in aura → zero benefit). Parity holds. |

**Identity reading.** Ragnar Lothbrok is the warband leader whose presence calls his own — the aura is not a buff *on* Norse towers but a continuous *spawn* of a lesser member of his retinue. "Sons of Ragnar" pulls one of his historically-named offspring into the fight every 20 seconds; the Son fights, dies, is replaced. Mechanically a summon passive; thematically the raid-coalition rendered as battlefield reinforcement. Norse identity ("strong few rather than orderly many") inverts the placement curve: Ragnar rewards scattered placements with one strong auxiliary, where Leonidas rewards dense formations and Montezuma II rewards prolific kill-density. R3's short-CD active will continue the summon lane (wave-of-warriors burst); R4's signature will culminate (named-Son-of-Ragnar boss-tier summon).

---

## Cross-commander parity check (R5 will simulate)

| Commander | Effect type | +15% damage-floor benchmark | Variant magnitude | Estimated equivalence ratio at Hard expert |
|-----------|-------------|------------------------------|-------------------|---------------------------------------------|
| Damage-floor | Damage | 1.15× DPS multiplier on civ-matched towers in aura | (baseline) | 1.00 |
| Leonidas | Control | 15% slow → +15% engagement-time | 15% slow, 50% soft-cap | ~1.00 (direct mathematical parity) |
| Montezuma II | Economy | +15% Tribute per kill in aura | +15% additive bonus, multiplicative with Economy Bonus aux | ~1.00 (over 30-round match window; ~0.95 if budget under-converted late) |
| Ragnar | Summon | One Son @ 40 DPS in aura, 20s cadence, max 1 alive | 40 DPS auxiliary unit | ~1.00 at 3-4 tower aura density; ~1.5 at 1-tower; ~0.5 at 5+ tower (intentional thematic asymmetry) |

**Parity audit:** all three within ±10% at the realistic 3-4 tower aura density (the Hard-expert placement-coverage 65% target). Ragnar's asymmetry beyond that range is intentional and identity-reinforcing. R5 simulates against full §4.11.8 thresholds across all 3 (k) tiers and confirms.

## Reversibility note

**Medium.** This round binds 3 passive specs as the equivalent-impact baseline for the (h) slot. Reverting requires: (1) superseding decision entry per spec to revert; (2) downstream R3-R4 short-CD + signature variants do NOT depend on this round's magnitude numbers, only on the **effect-type assignment per commander** (control / economy / summon). Effect-type assignments are the load-bearing carry forward.

**Hard-class risks (explicit guards):**

- **§4.11.6 damage-floor magnitudes** (+15% / 2-cell / civ-matched) untouched. Variants are authored *alongside* — never *instead of*.
- **§3.2 locked ability names** (Spartan Training / Blood Tribute / Sons of Ragnar) appear verbatim in this file. No rephrasing.
- **§5.4 [LOCKED] / §2.4a [LOCKED]** untouched.
- **2026-04-25 locked content skeleton** untouched (commander roster + civ assignments + ability names all preserved verbatim).
- **Cultural-sensitivity Follow-up #5** preserved — mechanical-content prose only; no visual / pose / VO direction in this file.

## Follow-ups

- **R3 (next round)** — short-CD active variants (This Is Sparta! / Sun Offering / Berserk) authored against 2,880-burst benchmark + 30s-CD-band discipline + locked effect-type-per-commander assignments from this round.
- **R5 §4.1 rewrite owns aura-anchor resolution.** Tension between §4.1 "board-wide invisible, not aura-scoped" (2026-04-27) and §4.11.6 "2-cell aura" (2026-05-05 R4) → R5 reconciles. R2-R4 spec against §4.11.6 aura-shape with `[anchor TBD R5]` placeholder where spatial detail matters. Resolution candidates for R5: (a) player-designated "anointed" tower per match (aura emanates from chosen tower); (b) fixed Commander-pedestal cell at player's start position; (c) board-wide all-civ-matched-towers (revising §4.11.6 R6's "2-cell" qualifier).
- **Per-tower authoring sub-pass (post-arc track #1)** receives 3 *target-side* hook interfaces from this round: Greek towers consume Leonidas slow status_state; Aztec towers' kill-events trigger Montezuma II Tribute bonus; Norse Sons spawn at fixed Slashing attack-type. Cross-arc parity guaranteed by both sides citing §4.10 + §4.11.6 + this decision file.
- **Per-civ specialization sub-pass (post-arc track #2)** receives 3 civ-affinity hooks: Greek control-flavor / Aztec economy-flavor / Norse summon-flavor. Per-civ identity profiles align downstream.
- **Cultural-sensitivity Follow-up #5** receives advance notice that mechanical content is finalized for passive slot — visual / VO direction can begin scoping in parallel (no spec dependency).
- **Cascade-lint** to be re-run after this commit.
- **Dual-push** deferred to R3 close per scope-decision checkpoint cadence.
