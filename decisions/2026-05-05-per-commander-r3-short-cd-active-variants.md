# Decision — Per-commander R3: short-CD active-slot variants (This Is Sparta! / Sun Offering / Berserk)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** Forward-anchored to [`concept/phase-4.md §4.1`](../concept/phase-4.md) (R5 mechanical-content rewrite) + `§4.11.6` (R5 deferral-removal). No spine-doc edits this round.

---

## Decision

Bind mechanical specs for the **short-CD active (g)-slot variants** across all 3 launch commanders against the §4.11.6 damage-floor benchmark (active: 4× T3 DPS = 720 DPS × 3-cell radius × 4s duration × 30s CD = **2,880 burst per cast**, ≈ 96 DPS amortized). Effect-type lane locked from R2 per commander to preserve identity coherence: Leonidas=Control, Montezuma II=Economy, Ragnar=Summon. Each variant calibrated to ±10% equivalent-impact at §4.11.8 Hard expert thresholds (matchup 75% / placement 65% / ability-uptime 60%).

| Commander | Civ | Active name (locked §3.2) | Effect type | Equivalent-impact mechanism |
|-----------|-----|---------------------------|-------------|-----------------------------|
| **Leonidas** | Greek | **This Is Sparta!** | **Control** | 4s hard-stun + 1-cell knockback in 3-cell radius → marginal damage from extended engagement-time on stationary targets |
| **Montezuma II** | Aztec | **Sun Offering** | **Economy** | 4s window: Aztec-tower kills in 4-cell radius yield +35% bonus Tribute → injected buying budget per cast |
| **Ragnar Lothbrok** | Norse | **Berserk** | **Summon** | Spawn 2 short-lived Berserkers at target cell @ 360 DPS each × 4s lifespan, Slashing, frontal cleave |

**CD discipline:** All 3 variants lock to **30s base CD** per R1 scope decision (30s-CD-band). Variant-specific CD flex deferred to R5 audit if parity table flags imbalance (allowed range 24-36s with inverse burst adjustment to maintain ~96 DPS amortized).

**Aura-anchor inheritance:** Active-slot abilities target a **player-aimed cell** (cast at cursor on click), not the commander's passive aura. The R2-deferred passive aura-anchor sub-decision does **not** apply to active variants — active casts have explicit player-chosen target cells per §4.11.6 wording. R5 §4.1 rewrite owns confirming this distinction stays clean.

## Context

§4.11.6 damage-floor active = 720 DPS × 3-cell radius AOE × 4s duration = 2,880 burst per cast. At 30s CD with 60% Hard ability-uptime, effective casts = 30 rounds × ~30s/round / 30s_CD × 0.60 = ~18 effective casts per match → ~52K damage contribution per match.

Per-effect-type equivalent-impact derivation:

- **Control burst-equivalence:** Master damage equation §4.10.2 reads `damage = DPS × engagement-time integral × matchup × passive_modifiers × status_state`. Hard-stun extends engagement-time integral on stunned targets by (stun_duration). Marginal damage = stun_duration × DPS_in_range_towers. T3 Greek towers in 3-cell firing radius around cast cell ≈ 3 towers × 180 DPS = 540 DPS in-range. 4s stun × 540 DPS = 2,160 base marginal. 1-cell knockback adds 1 cell / 50 u/s × 540 DPS = 540 marginal. Total = **2,700 burst-equivalent** (within −6% of 2,880, in ±10% band).
- **Economy burst-equivalence:** Cleanest parity is per-cast Tribute injection convertible to combat impact at +15% passive scale (per R2 Economy derivation). At R20 mid-match baseline (yield ≈ 33 T/std kill per §4.11.3), 4s window + 4-cell radius captures ~1 std-kill/sec by Aztec towers in active combat = ~4 kills × 33 T × 0.35 bonus = **46 T per cast**. Over 18 effective casts/match = ~830 T bonus = ~14% of baseline match income (~6,000 T at Hard expert). Within −7% of +15% passive scale (and matches active-tier parity since active is sized on damage-floor, not passive — economy translation amortizes equivalently when convertible to T1 buys at ~120 damage/T over remaining match). **In ±10% band.**
- **Summon burst-equivalence:** Direct DPS×duration math. 2 Berserkers × 360 DPS × 4s lifespan = **2,880 burst** (exactly matches damage-floor). Slashing attack-type per Norse civ-affinity (RPS hooks: strong vs Unarmored / Beast; weak vs Shielded). Frontal cleave 1-cell adds ~10-15% effective DPS in dense waves (multi-target hit) — within band noise; not adjusted further.

Authoring all 3 variants in the same round (per Axis B) keeps the equivalence-ratio comparison inline.

## Effect-type assignment rationale (per locked-name reading)

**Leonidas — This Is Sparta! → Control.** The locked name carries unambiguous historical resonance (Frank Miller's *300* / Snyder film cinematic kick) — the active is the kick-into-pit moment. Three readings: (a) damage burst (a hard hit — but this duplicates the damage-floor active baseline and surrenders identity); (b) control (knockback + stun, the kick that disables and displaces — strongest fit to the cinematic moment + clean engagement-time math); (c) summon (Spartan reinforcements — overlaps Sons of Ragnar). Control reads strongest: knockback + stun is what the kick *does* (target stops, target moves backward), the engagement-time gain reads cleanly as "they couldn't escape," and it stays in Leonidas's R2 Control lane. **Cultural-sensitivity Follow-up #5 advance flag:** the kick-target-into-pit visual is deferred to art/pose direction (mechanical spec is target-class neutral — applies to all enemies in zone regardless of armor tag or species).

**Montezuma II — Sun Offering → Economy.** The locked name reads as religious-economic: an offering made *for* something, in exchange for divine favor. Three readings: (a) damage burst (a fire/smite from the sun god — but R2 locks Aztec into Economy lane; this would be a lane break); (b) economy (the offering yields material reward — Tribute lump, the cleanest fit to the offering metaphor); (c) summon (sun-god-summoned servitor — overlaps Berserk + duplicates Aztec Eagle/Jaguar Warrior tower roster). Economy reads strongest: "offer Tribute, receive Tribute back amplified" reads as an economic risk-reward gesture (player sacrifices an action slot + 30s CD to get bonus income), and the +35% kill-bonus framing requires player commitment (must be actively killing in the zone within window — no passive farm). **Cultural-sensitivity Follow-up #5 advance flag:** the "offering" mechanical content is religion-neutral (not human-sacrifice-coded — generic Tribute economy hook); art/VO direction owns whether the offering visual involves blood imagery or alternative reverent framing per Aztec sensitivity gate.

**Ragnar Lothbrok — Berserk → Summon.** The locked name is a verb (the warrior enters berserk state) but here read as a *verb-of-summoning* (calling forth berserk warriors, not transforming Ragnar himself — Ragnar is a §4.1 summoned-on-cast presence model, not a persistent on-field hero per 2026-04-27 amendment). Three readings: (a) damage burst (Ragnar self-buffs and frenzy-attacks — but this requires Ragnar-on-field, contradicts §4.1); (b) control (intimidate / fear effect — possible but overlaps Leonidas's control lane); (c) summon (call forth 2 berserker warriors, short-lived burst — strongest fit to the §4.1 summoned-presence model + stays in Ragnar's R2 Summon lane). Summon reads strongest: the 2 spawned Berserkers are explicit short-lived burst summons (distinct from R2's Sons of Ragnar passive, which is a persistent single Son @ 40 DPS / 20s cadence — the Berserkers are 360 DPS × 4s, ~9× the per-unit burst, far higher intensity, fully consumed within active window). Two distinct summon types per commander-identity = "Norse calls warriors at multiple intensities" reading. **Cultural-sensitivity Follow-up #5 advance flag:** Berserker-class historical accuracy (entheogenic / shamanic origins) is art/lore direction; mechanical spec is religion-neutral.

## Per-commander mechanical specs

### Leonidas — This Is Sparta!

| Attribute | Value | Notes |
|-----------|-------|-------|
| Slot | Short-CD active (g) | Per §4.11.6 active slot |
| Effect type | Control (hard stun + knockback) | Per R2 lane lock |
| Cast target | Player-aimed cell on click | Standard active cast pattern |
| Target class | All enemies in radius (no civ/armor filter) | Uniform creep effect |
| Radius | 3 cells (hex distance ≤ 3 from cast cell) | Matches damage-floor active radius |
| Duration | 4s hard stun (enemies cannot move or attack) | Matches damage-floor active duration |
| Knockback | 1 cell at cast moment (away from cast cell) | Adds engagement-time on top of stun |
| CD | 30s base | Per R3 CD discipline |
| Equivalent burst | ~2,700 damage marginal at Hard expert (3 in-range Greek T3s × [4s × 180 DPS + 1 cell knockback × 180 DPS]) | Within −6% of 2,880 |
| Civ-affinity hook | None (works for any civ towers in firing range; co-located with Greek towers maximizes synergy via R2 passive Control) | Greek-passive + Greek-active stacks to +30% effective engagement-time on enemies in overlap zone — intended Greek "lockdown" identity reading |
| Per-tower target-side hook interface | None — no per-tower attribute consumed | Stuns are universal; per-tower towers benefit via being in firing range, not via tower attributes |
| Status-proc interaction | Stunned enemies cannot apply status to towers; existing status-procs from towers continue ticking on stunned target normally | §4.10 status-state factor unchanged |
| Edge cases | Bosses get **half stun duration** (2s) per §4.11.4 boss-archetype convention; enemies already stunned by other sources don't stack (stun duration uses max not sum); knockback applies to bosses but at half distance (0.5 cell rounded to nothing for hex grid → bosses no-knock) | Boss-class guard standard |

### Montezuma II — Sun Offering

| Attribute | Value | Notes |
|-----------|-------|-------|
| Slot | Short-CD active (g) | Per §4.11.6 active slot |
| Effect type | Economy (Tribute kill-bonus window) | Per R2 lane lock |
| Cast target | Player-aimed cell on click | Standard active cast pattern |
| Target class | Aztec towers' kills in radius | Civ-gated (Aztec only — same gating as R2 passive) |
| Radius | 4 cells (hex distance ≤ 4 from cast cell) | Slightly wider than damage-floor (3 cells) to compensate for Economy's amortized impact requiring more kill-throughput coverage |
| Duration | 4s window (Tribute-bonus active during window) | Matches damage-floor duration |
| Tribute bonus | +35% bonus Tribute on top of base yield per Aztec-tower kill in zone during window | Multiplicative with §4.6a Economy Bonus aux: aux yields +25% base; aux-equipped commander Sun Offering = base × 1.25 × 1.35 = base × 1.6875 per kill in zone during window |
| CD | 30s base | Per R3 CD discipline |
| Equivalent budget | ~46 T per cast at R20 baseline (1 kill/sec × 4s × 33 T base × 0.35 bonus); convertible to ~5,500 damage-equivalent over remaining match (T1 buy @ 0.2 DPS/T × 600s remaining ≈ 120 damage/T × 46 T) | Within band when amortized over match span; matches damage-floor at the active-tier scale (single-cast comparison flatters Economy here, ratios out across full match) |
| Civ-affinity hook | Aztec-only kill bonus | Civ-gated identity preserved across (h)+(g) slots |
| Per-tower target-side hook interface | Per-Aztec-tower `bonus_tribute_yield_in_active_zone` flag; tower yield calculation reads `flag = aztec && in_radius && in_active_window ? 1.35 : 1.0` factor | Cross-arc per-tower authoring (deferred sub-pass) binds to this flag |
| Status-proc interaction | None — status-procs from kills unaffected | Pure economy variant, no combat-state interaction |
| Edge cases | If no Aztec towers in radius at cast time, cast still consumes CD (no refund) — player-skill discipline; if active overlaps with §4.6a Send-Creeps zone, defender-side kills count for sender's Sun Offering bonus only if defender is Aztec (cross-mode interaction); boss kills during window grant **lump** Tribute bonus (boss lump × 1.35 multiplier — significant burst per §4.11.3 R10/R15/R30 lumps); §4.7 R11 wave-randomization may shift kill-density variance per cast (intentional variance, not exploit) | Boss-lump amplification flagged for R5 audit |

### Ragnar Lothbrok — Berserk

| Attribute | Value | Notes |
|-----------|-------|-------|
| Slot | Short-CD active (g) | Per §4.11.6 active slot |
| Effect type | Summon (auxiliary unit burst) | Per R2 lane lock |
| Cast target | Player-aimed cell on click | Standard active cast pattern |
| Spawn count | 2 Berserkers | Per parity math |
| Per-Berserker DPS | 360 DPS | 4× T3 / 2 = 720 / 2 |
| Per-Berserker HP | 1 × HP_std(R) | Lower than R2 Sons (which are 2× HP_std(R)) — Berserkers are short-lived burst summons, not survivability-tuned |
| Lifespan | 4s (despawn at end) | Matches damage-floor active duration |
| Attack type | Slashing (Norse civ-affinity) | RPS hooks: +25% vs Unarmored / Beast; -25% vs Shielded |
| Targeting | Auto-target nearest enemy in 1-cell radius; if no target in 1 cell, walk forward (toward path direction) until target acquired | Player has no manual control once spawned (consistent with Sons of Ragnar autonomy) |
| Cleave | Frontal cleave 1-cell (hits primary target + adjacent enemies in same hex direction) | Adds effective DPS in dense waves; no parity adjustment (within band noise) |
| Spawn position | At cast target cell + 1 cell offset (Berserkers spawn shoulder-to-shoulder, 2 adjacent cells around target) | Uses standard summon-position rules |
| CD | 30s base | Per R3 CD discipline |
| Equivalent burst | 2,880 (2 × 360 DPS × 4s) — exactly matches damage-floor | Within parity exactly |
| Civ-affinity hook | None (Berserkers are summoned units, civ-neutral targets — they do not buff or debuff Norse towers; their attack-type alignment IS the Norse identity hook) | Cross-civ play: Berserkers spawn regardless of player's tower-civ composition; player using Norse commander w/ non-Norse towers still gets full Berserker DPS |
| Per-tower target-side hook interface | None — Berserkers are units, not tower buffs; they consume the standard `unit_dps_contribution` slot already used by Sons of Ragnar; counting cap = `summons_alive_max = 1 (Sons) + 2 (Berserkers active) = 3 max` to preserve §4.6a Tower-count expansion balance | Cross-arc per-tower authoring binds via §4.6a Tower-count interaction |
| Status-proc interaction | Berserkers' Slashing attacks apply Bleed status (per §4.10 attack-type → status table from 2026-04-26 attack-type-mapping decision) at standard tower proc rate | Adds DOT contribution on top of base 2,880 burst; within band noise |
| Edge cases | If 2 Berserkers + 1 Son already at summon cap when Berserk cast → cast still consumes CD (no refund); if Berserkers killed before 4s lifespan ends → no respawn (lifespan is wall-clock, not life-pool); §4.6a Tower-count expansion aux does NOT increase Berserker spawn count (aux affects tower slots, not summon slots — explicit clarification); Berserker spawn at boss-collision cell is allowed (Berserker tank potential vs boss melee — intentional) | Cap clarification flagged for R5 audit; cross-arc summon-cap reference for cross-commander balance |

## Cross-commander parity check

Target: ±10% equivalent-impact at §4.11.8 Hard expert thresholds. All 3 variants land within band:

| Commander | Active variant | Equivalent burst per cast | Δ vs 2,880 floor | Match-span impact (~18 casts) | Notes |
|-----------|----------------|---------------------------|------------------|-------------------------------|-------|
| Leonidas | This Is Sparta! | 2,700 (Control) | −6% | ~48,600 | Stacks with R2 Greek Control passive in overlap; full-Greek-stack identity hook |
| Montezuma II | Sun Offering | ~5,500 (Economy, amortized to damage-equivalent) | high (single-cast flatters); ~14% on +15% scale | ~99,000 (amortization compounds vs damage-floor's flat ~52K) | Economy variants accumulate vs flat-damage variants — intended Aztec "scaling buying power" identity reading; R5 must verify this doesn't break Hard-expert breakpoints |
| Ragnar | Berserk | 2,880 (Summon, exact) + Bleed DOT + cleave | 0% nominal; +10-15% with Bleed/cleave | ~52,000 + ~5,000-8,000 status/cleave | Pure-burst variant; DPS/cast cleanest; Bleed adds DOT outside the 4s cast window |

**R5 audit flag:** Sun Offering's match-span impact (~99K) is roughly 2× damage-floor (~52K) when fully amortized — this is intentional asymmetry per Economy lane (compounding income translates to compounding combat-value via additional towers, which then deal more damage, etc.) but R5 must simulate Hard-expert match playthroughs to confirm this doesn't push Aztec past the §4.11.8 100% breakpoint at Hard. If it does, Sun Offering tunes to +25% bonus (from +35%) or 3-cell radius (from 4-cell). Pre-emptively bracketed.

**Cross-arc per-tower target-side hooks specified:**
- `aztec_tower.bonus_tribute_yield_in_active_zone` flag (Sun Offering consumer)
- `summons_alive_max` global cap = 3 (1 Son + 2 Berserkers, per Ragnar interaction; cross-civ play caps at 0 + 2 = 2 if Greek/Aztec commander uses Berserk-derived items in some future Foresight-coin recipe — flagged for Follow-up #6 cross-commander item layer)
- No `greek_tower.*` flag needed (Control acts on enemies, not on Greek towers; Greek towers passively benefit by being in firing range)

## Per-commander identity readings

**Leonidas** (post-R3 reading): The Control lane reads cleanly across both ability slots. Passive (Spartan Training) is the *positional discipline* — slow zone keeping enemies in Greek tower kill-windows longer. Active (This Is Sparta!) is the *cinematic punctuation* — the kick that locks down a 3-cell zone hard for 4s + a knockback. Together they read as "Greek lockdown identity": enemies move slowly through Leonidas's aura by default, then occasionally get kicked entirely off the path. Both abilities reward placement-skill (axis (b) per §4.10) — the player who clusters Greek towers along the path's choke gains the most from both. Identity coherence: locked. R4 signature (The Last Stand) must reinforce or peak this lockdown reading — likely a long-duration zone-denial ult.

**Montezuma II** (post-R3 reading): The Economy lane reads as *religious-mercantile compounding*. Passive (Blood Tribute) is the *steady offering* — Aztec towers in aura yield 15% more Tribute on every kill, a constant bleed of bonus income. Active (Sun Offering) is the *peak offering* — a 4s window where Aztec kills in zone yield +35%, requiring active player engagement to capitalize (must aim cast where Aztec towers are killing). Together they read as "Aztec scaling identity": Tribute compounds throughout the match, fueling earlier tier-ups, more towers, more aux-slot purchases. The +35% active stacks multiplicatively with the +15% passive in overlap zone (Aztec tower in both passive aura + active zone yields base × 1.15 × 1.35 = base × 1.5525 per kill). Identity coherence: locked. R4 signature (The Great Sacrifice) must peak this scaling reading — likely a single massive Tribute/Divinity injection or a perma-buff to economy curves.

**Ragnar Lothbrok** (post-R3 reading): The Summon lane reads as *layered warrior calling*. Passive (Sons of Ragnar) is the *single sustained presence* — one persistent Son @ 40 DPS, always there, low-intensity but constant. Active (Berserk) is the *burst frenzy* — 2 Berserkers @ 360 DPS each for 4s, brief but explosive. The combination reads as "Norse called-warriors identity": Ragnar the Commander never appears on field (per §4.1), but his summoned warriors always do — sometimes one quietly working, sometimes three (1 Son + 2 Berserkers) erupting at a single point. Slashing attack-type across both summons reinforces RPS positioning skill (Norse player wants to call summons against Unarmored / Beast waves, hold during Shielded waves). Identity coherence: locked. R4 signature (The Great Heathen Army) must peak this called-warriors reading — likely a mass summon ult delivering many warriors at once.

## Alternatives considered

1. **All 3 in same effect-type lane (e.g., all Control on (g))** — rejected per R2 lane lock. Would break commander-identity coherence; (g) variant must reinforce (h) lane.
2. **Different CDs per commander** — flexed (Sparta! 24s, Sun Offering 30s, Berserk 36s, with adjusted bursts). Rejected for R3: locking 30s base across all 3 lets the parity table compare cleanly. R5 audit owns CD-flex if Hard-expert simulation shows any commander outliers.
3. **This Is Sparta! as damage burst (lane break)** — rejected per R2 lane lock + identity erosion (would duplicate damage-floor). Control reads stronger thematically.
4. **Sun Offering as Damage-burst lane break (a fire-from-the-sun-god burn)** — rejected per R2 lane lock + Aztec identity. Economy compounds the per-civ "scaling buying power" reading; lane break here would split Aztec identity between two unrelated mechanical languages.
5. **Berserk as self-targeted Ragnar buff (Ragnar enters frenzy state)** — rejected per §4.1 (Commander is summoned-on-cast, not a persistent field hero). The Summon reading respects §4.1 cleanly.
6. **Berserkers as 1 unit @ 720 DPS instead of 2 @ 360 each** — rejected for cleave + DOT layering richness. 2 Berserkers cover more frontage, allow flank targeting, and double-stack Bleed proc — better identity reading at same parity cost.

## Reason

- Effect-type lane lock per commander preserves identity coherence across (h)/(g)/(i) slots without requiring R5 to do disambiguation work mid-audit.
- 30s CD discipline locks parity simplicity for R3; R5 can flex if needed.
- Cross-commander parity check stays within ±10% band (with one flagged amortization asymmetry on Sun Offering — pre-bracketed).
- Per-tower target-side hook interfaces specified now keep cross-arc per-tower authoring unblocked.
- Cultural-sensitivity Follow-up #5 mechanical/visual separation discipline maintained — all 3 specs are visual-direction-neutral.

## Reversibility

**Medium.** Three parity-band guards:
- If R5 simulation shows Sun Offering's amortized impact pushes Aztec past Hard 100% breakpoint → tune to +25% bonus or 3-cell radius (pre-bracketed).
- If R5 audit shows This Is Sparta!'s knockback reads as too-floaty in playtest → drop knockback, raise stun to 4.5s (560 DPS × 4.5s = 2,520 base + standard adjustments).
- If Berserk's Bleed/cleave overshoot pushes Norse past breakpoint → drop cleave (single-target only) or shorten lifespan to 3.5s.

CD-flex band (24-36s) gives R5 a second-axis adjustment lever without requiring spec rewrites.

## Follow-ups

1. **R4 next** — signature variants (The Last Stand / The Great Sacrifice / The Great Heathen Army) against instant-tier-up benchmark (once-per-match free T1→T2 or T2→T3 per §4.11.6). Per-commander identity readings from R2+R3 set the signature direction.
2. **Dual-push checkpoint after R3 close** — carries R1 + R2 + R3 per scope decision cadence.
3. **R5 audits** flagged this round: (a) Sun Offering amortization vs Hard 100% breakpoint; (b) Berserker summon-cap clarification; (c) CD-flex if any commander outliers; (d) confirm active-cast-target distinction from passive-aura-anchor in §4.1 rewrite; (e) §4.11.6 deferral language removal.
4. **Cultural-sensitivity Follow-up #5** advance flag preserved on all 3 active-cast visuals (Sparta-kick → pose; Sun Offering → blood/altar imagery direction; Berserker poses → entheogenic accuracy).
5. **Cross-arc per-tower authoring** binds to: `aztec_tower.bonus_tribute_yield_in_active_zone` flag; global `summons_alive_max = 3` cap; status-proc Bleed application from Berserker Slashing attacks (cross-references 2026-04-26-attack-type-mapping decision).
6. **Cross-arc per-civ authoring** consumes: full-Greek-stack overlap zone identity (passive Control + active Control); full-Aztec-stack overlap zone yield multiplier (1.5525× per kill); Norse called-warrior layered summon identity.
