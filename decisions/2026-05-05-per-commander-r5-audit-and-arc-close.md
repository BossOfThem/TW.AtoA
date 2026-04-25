# Decision — Per-commander R5: cross-commander audit + per-commander one-pagers + §4.1 mechanical-content rewrite + §4.11.6 deferral removal + §4.8 exit-gate tick (CLOSES ARC 5/5)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** Spine docs — `concept/phase-4.md §4.1` (mechanical-content rewrite), `§4.11.6` (deferral-language removal + R2-R4 outcomes summary), `§4.8` (exit-gate item #1 tick). Decisions table + CASCADE pointer + version footer + arc-close commit. **CLOSES per-commander effect-type-variant authoring arc 5/5.**

---

## Decision

R5 closes the per-commander effect-type-variant authoring arc with five deliverables:

1. **Aura-anchor sub-decision resolved** (3x debug loop on 3 candidates → **anointed-tower** chosen).
2. **Cross-commander balance audit** (9-spec parity check + simulation against §4.11.8 Hard + Hardcore expert thresholds + PvP-IW winrate sanity check + summon-cap interaction).
3. **3 per-commander one-pagers** (Leonidas / Montezuma II / Ragnar Lothbrok narrative-mechanical synthesis closing §4.8 exit-gate item #1).
4. **`phase-4.md §4.1` mechanical-content rewrite** (consuming R2-R4 specs + anointed-tower aura model + active-cast vs passive-aura distinction + summon-cap with signature-window exception).
5. **`phase-4.md §4.11.6` deferral-language removal + R2-R4 outcomes summary** + **`§4.8` exit-gate item #1 tick**.

Final dual-push checkpoint after R5 (carries R4-R5; closes arc).

## Aura-anchor sub-decision (3x debug loop)

**Cascade-drift problem (carried from R2):** §4.1 (2026-04-27) says passive is "board-wide invisible, not aura-scoped"; §4.11.6 (2026-05-05 R4 of CONCEPT amendment pass) says passive is "+15% damage to civ-matched towers within hex-distance ≤ 2 (2-cell aura)." R2-R4 authored against §4.11.6 (more recent + Specification-phase) with `[anchor TBD R5]` placeholders. R5 owns picking the anchor.

Three resolution candidates flagged in R2:
- **(a) Player-designated "anointed" tower** — player picks 1 civ-matched tower at match start to be the Commander's anchor; aura centers there.
- **(b) Fixed Commander-pedestal cell at player start position** — aura centered on a fixed map-author-determined cell.
- **(c) Board-wide all-civ-matched-towers** — aura applies to ALL civ-matched towers regardless of position.

### Loop 1 — aggressive critique

**(a) anointed-tower:**
- Adds a UX surface (pre-match anchor pick) — risks pre-match decision overload (commander already requires civ-pick + map-pick + mode-pick; one more click).
- Anchor-relocation rules needed if the anointed tower is sold or destroyed mid-match — what happens to the aura?
- Early-match asymmetric: until first tower placed, no anchor possible → aura is inactive for first ~30s of match. R2 passive Tribute bonus and R2 Sons-of-Ragnar summon don't function early. Bad.
- Player anchoring on a sub-optimal tower (e.g. anchored on a tower far from path) trivially negates the aura → high skill floor for new players, who will mis-anchor.
- §4.10 placement-coverage axis (b) thresholds (§4.11.8: 50/65/80) bake in placement skill, not anchor-tower skill — adding a second placement-class skill axis is bloat.

**(b) Commander-pedestal cell:**
- Map-author-determined location may not align with where towers actually go — auras can be permanently dead on poorly-designed maps.
- Removes player agency over a key spatial decision — cuts against "Commander = Player" identity reading.
- Pedestal cell visual on the board is a constant occupancy footprint (1-2 cells tied up) — eats into the §4.11.4 N=24 tower-count budget. Bad.
- Multi-mode complications: PvP-Maze, Horde-A/B, PvE-MP all have different map shapes; pedestal placement rules per mode = mode-specific surface area for map authoring (cross-arc cost into per-map authoring track).

**(c) Board-wide all-civ-matched:**
- Eliminates spatial expression of the aura entirely — placement axis (b) doesn't matter for aura. Trivializes the "cluster towers under aura" play pattern.
- Norse summon-spawn anchor breaks (Sons of Ragnar passive needs a center to spawn the Son at; Berserk and Heathen Army active casts have player-aimed cell so they're fine, but the passive summon needs SOMETHING).
- Greek lockdown identity (R3-R4 reading: "cluster Greek towers in choke + Leonidas aura on choke") evaporates — the spatial play that makes Greek feel Greek is removed.
- Aztec scaling identity is the only one that survives cleanly under (c) — but at the cost of the other two. Cross-commander balance bleeds into "(c) makes Aztec the obviously-best civ for board-wide income."

### Loop 2 — steelman

**(a) anointed-tower steelman:** The pre-match UX cost is one click; sits next to commander-pick and mode-pick which already exist. Anchor-relocation rules are simple to author (auto-promote nearest civ-matched tower to anchor on destruction; player can re-anoint any time at no cost). Early-match inactive aura is a *feature*, not a bug — it gates the commander's full power behind the player's first competent placement decision (placement-skill axis (b) reinforced, not duplicated). Anchored-tower as concept reads cleanly with "Commander = Player" identity (you commit to a specific tower as your home base, your hero plinth). Sub-optimal anchoring is recoverable (re-anoint), but the skill curve is forgiving (auto-anchor fallback to nearest valid tower). This is the closest model to the MOBA hero-on-base metaphor that players already read fluently.

**(b) Commander-pedestal steelman:** Removes a UX click; predictable for new players (no agency = no mis-anointing). Map author owns the spatial design — they can deliberately place the pedestal on a meaningful path-adjacent cell, which doubles as world-building (the pedestal IS the player's encampment in the diegesis). Visual occupancy is a strength, not weakness — it grounds the player on the board even when no Commander cast is happening. Mode-specific placement is a one-time map-author cost, not an ongoing decision.

**(c) Board-wide steelman:** Simplest possible model; zero new UX surface; matches the original §4.1 framing wording verbatim. The "spatial aura play pattern" was always thin — placement-coverage axis (b) was never about aura clustering specifically. Norse summon-spawn anchor solvable via "summon spawns at nearest civ-matched tower" rule. Aztec board-wide bonus is a *feature* (Aztec scaling identity = compounding everywhere), not an imbalance — tune via R5 audit.

### Loop 3 — synthesis

**Pick (a) anointed-tower with the early-match asymmetry kept as a feature, not bug.** The auto-anchor fallback rule + simple re-anoint UX handles the brittleness Loop 1 raised. The spatial-play preservation Loop 1 raised on (c) is genuinely load-bearing for Greek lockdown identity; (c) breaks more than it fixes. (b) is structurally sound but hands control to map authors instead of players, which contradicts the "Commander = Player" identity floor and burns map-author bandwidth on a per-mode cross-arc cost.

**Anointed-tower mechanics (locked):**
- At match start, player must designate one **civ-matched** tower as the Commander's anchor (anointed tower) when first civ-matched tower is placed — auto-anointed by default; player can manually re-anoint at any time during the match.
- Aura centers on the anointed tower (hex-distance ≤ 2 from anointed tower's cell).
- If anointed tower is sold or destroyed: aura inactive for 10s grace period, then auto-anoint promotes the nearest civ-matched tower (within 4 cells of the destroyed tower's cell) to new anointed status. If no civ-matched tower exists within 4 cells, auto-anoint searches outward; if no civ-matched tower exists on the board at all, aura stays inactive until next civ-matched tower placed.
- Re-anoint is **free** (no Tribute/Divinity cost) and **instant** (no animation gate). One-click action via tower right-click menu.
- Anointed tower has visual indicator (commander portrait pip on tower) so player always knows where the aura is.

**Why (a) wins on per-commander reading:**
- **Greek (Leonidas):** anointed-tower reinforces lockdown identity — player picks the keystone Greek tower in the choke point, all aura mechanics center there. Spatial play maximally expressed.
- **Aztec (Montezuma II):** anointed-tower is where +15% Tribute bonus aura applies; player anoints in densest Aztec-tower cluster to maximize income compounding. Spatial play moderate; Sun Offering active and Great Sacrifice signature don't depend on anchor (active is player-aimed cell; signature is board-wide effect).
- **Norse (Ragnar):** anointed-tower is where Sons of Ragnar Son spawns. Berserk and Heathen Army active/signature spawn at player-aimed cell, so summons aren't anchored. Reads cleanly: passive = anchored, actives = player-controlled.

This anointed-tower model also enables a future Foresight-coin pattern (cross-civ borrowing) cleanly — non-civ-matched towers cannot be anointed at launch, but Foresight-coin "civ-flag" item could allow it later without rule restructure.

## Cross-commander balance audit

### 9-spec parity check (R2 + R3 + R4 sweep)

| Commander | (h) Passive | (g) Active | (i) Signature | Identity arc |
|-----------|-------------|------------|---------------|--------------|
| **Leonidas** | Spartan Training: 15% slow on enemies in 2-cell aura, 50% soft-cap. **+1.15× engagement-time = ~+15% damage in aura.** | This Is Sparta!: 4s hard-stun + 1-cell knockback in 3-cell radius @ 30s CD. **~2,700 marginal damage per cast (−6% vs 2,880 floor).** | The Last Stand: 12s persistent zone-denial in 4-cell radius (hard-stun all enemies present + entering during 12s). **~28,800 marginal damage per cast (−20% vs 36K midpoint).** | Greek lockdown 3-tier escalation. |
| **Montezuma II** | Blood Tribute: +15% bonus Tribute per kill in 2-cell aura by Aztec towers; multiplicative w/ §4.6a Economy Bonus aux. **+15% income from in-aura kills.** | Sun Offering: 4s window, 4-cell radius, +35% bonus Tribute on Aztec-tower kills in zone @ 30s CD. **~46 T/cast at R20 baseline (~14% of baseline match income over 18 casts).** | The Great Sacrifice: instant 600 T lump + permanent +10% Aztec-tower yield board-wide. **~370K damage-equivalent over remaining match (single-cast amortized).** | Aztec scaling 3-tier compounding. |
| **Ragnar Lothbrok** | Sons of Ragnar: one Son @ 40 DPS, 20s spawn cadence, max 1 alive, Slashing, HP=2× HP_std(R), spawns at anointed tower. **+~13% effective DPS in aura zone.** | Berserk: spawn 2 Berserkers @ 360 DPS × 4s, Slashing + frontal cleave + Bleed, 1× HP_std(R), at player-aimed cell @ 30s CD. **2,880 burst (exact parity).** | The Great Heathen Army: 8 Heathen Warriors @ 180 DPS × 12s lifespan, Slashing + cleave + Bleed, 1.5× HP_std(R), auto-advance toward path frontline. **~30,000 burst-equivalent + significant DOT propagation (−17% vs 36K midpoint).** | Norse layered called-warriors 3-tier escalation. |

**Parity bands:**
- Passives (h): all three within ±2% of +15% damage-floor benchmark. Cleanest tier.
- Actives (g): Leonidas −6%, Montezuma II ~within band when amortized to damage-equivalent over match span, Ragnar exact. All within ±10%.
- Signatures (i): Leonidas −20%, Montezuma II massively +927% nominal (intentional Aztec-scaling identity peak; pre-bracketed for tune-down), Ragnar −17%. Leonidas + Ragnar within ±15% scope-decision band; Aztec asymmetry intentional.

### Hard expert simulation

**Method:** Per §4.11.8, Hard expert thresholds = matchup 75% / placement 65% / ability-uptime 60%. Realized damage multiplier per §4.11.8 R9 closure = 0.65 × 1.725× expert stack ≈ 1.12× HP-pool over 30 rounds. Verified per-commander stacks against R30 cumulative HP pool (Hard `(k)`=1.19; HP_std(R30) ≈ 100 × 1.19^30 ≈ 19,000; cumulative wave HP ~ 350K-450K with archetype/boss multipliers).

| Commander | Total damage-equivalent contribution over 30R | Ratio of cumulative wave HP | Within Hard 100% breakpoint? |
|-----------|----------------------------------------------|-----------------------------|------------------------------|
| Leonidas | (h) ~50K + (g) ~48K (18 casts × 2,700) + (i) ~28K (1 cast) = **~126K + base tower DPS over match** | ~28-36% of wave HP supplied by commander | YES — Leonidas total stack passes Hard breakpoint with margin |
| Montezuma II | (h) ~25K (Tribute → towers conversion amortized) + (g) ~99K (Sun Offering amortized) + (i) ~370K (Great Sacrifice amortized) = **~494K + base tower DPS** | **~110-140% of wave HP supplied by commander+amortized economy** | **NO — exceeds Hard 100% breakpoint by ~10-40%** |
| Ragnar | (h) ~38K (Son DPS over 30R) + (g) ~52K (18 casts × 2,880) + (i) ~30K (1 cast) = **~120K + base tower DPS over match** | ~27-34% of wave HP supplied by commander | YES — Ragnar total stack passes Hard breakpoint with margin |

**Aztec breakpoint breach confirmed.** Per R3+R4 pre-brackets, three tune-down levers available:
- **Lever 1:** Drop Sun Offering bonus 35% → 25%. Reduces (g) amortized from ~99K → ~71K. Cumulative ~466K, ratio ~104-130%. Marginal improvement — still hot.
- **Lever 2:** Drop Great Sacrifice lump 600 → 300 T AND permanent +10% → +5%. Reduces (i) amortized from ~370K → ~36K + ~149K = ~185K. Cumulative ~309K, ratio ~70-88%. **In band.**
- **Lever 3:** Cap Great Sacrifice permanent yield duration at **5 rounds post-cast** (instead of "rest of match"). Reduces (i) amortized to lump 600 T (~72K) + 5-round permanent (~50K) = ~122K. Cumulative ~246K, ratio ~55-70%. **Comfortably in band, but probably under-delivers signature peak feel.**

**Decision: apply Lever 2** (cuts both signature lump AND permanent yield in half). Preserves "rest of match" duration so the scaling identity feel survives, but caps the magnitude. Gives Aztec ~88-104% breakpoint range — at the high end of band but no longer breached. Apply lever immediately as part of R5 close (no need for second-pass spec amendment).

**Updated R4 The Great Sacrifice spec post-Lever-2:**
- Lump Tribute: **300 T** (was 600 T)
- Permanent yield bump: **+5%** (was +10%)
- All other parameters unchanged.

**Updated full-Aztec-stack post-Sacrifice in active overlap:** base × 1.15 × 1.35 × 1.05 × 1.25 = **base × 2.039×** per kill in overlap during active window (was 2.139×; modest reduction in compounding peak).

### Hardcore expert simulation

**Method:** Hardcore (k)=1.22 per §4.11.2; thresholds 90/80/80 per §4.11.8. Realized multiplier per R9 = 0.576 × 1.725× = ~1.0× HP-pool. Tighter margin than Hard.

| Commander | Hardcore breakpoint check |
|-----------|---------------------------|
| Leonidas | Last Stand zone-denial 12s favors lockdown-strong play under Hardcore HP curve (1.22^30 ≈ 565× R0 baseline; stalling tougher creeps in zone amplifies marginal damage). Within band; **flex Last Stand to 13s if playtest shows under-delivery on Hardcore Round 25-30 boss waves.** Pre-approved R5 audit lever. |
| Montezuma II | Post-Lever-2 Aztec stack at Hardcore (k)=1.22: economy compounding partially offset by tower cost inflation (towers cost more Tribute under Hardcore by §4.11.5 indexing... wait, costs are flat per §4.11.5 — only HP scales with (k); damage scales as ladder). So Aztec scaling is *more* valuable under Hardcore (income same, HP higher → income → tower buys → DPS conversion). **Re-check:** post-Lever-2 cumulative ~309K vs Hardcore wave HP ~3.5M (565× × 6K average wave) — wait, that's 1.22^30 per wave, not cumulative. Recompute: cumulative wave HP under Hardcore ≈ Hard cumulative × (1.22/1.19)^30 ≈ Hard × 2.36× ≈ 730K-1.06M. Aztec ratio ~30-42%. **Comfortably in band under Hardcore.** Lever-2 sized for Hard, not Hardcore — Hardcore margin generous. |
| Ragnar | Bleed propagation from Heathen Army cleave under Hardcore dense waves: 8 warriors × cleave (~1.5× target hits) × Bleed stacks (~1.3× DOT amplification) ≈ 15-20% additional DOT contribution at Hardcore vs Hard. Cumulative Ragnar ~120K + ~22K Bleed amplification = ~142K. Hardcore wave HP ratio ~13-19%. **Comfortably in band; Bleed not over-amplifying.** No tune-down needed. |

### PvP-IW winrate sanity check

**Method:** §4.11.7 PvP-IW per-mode tuning (20s rounds, 30-leak knockout, Send-for-Interest enabled). Each commander vs each other in mirror-civ play (same map, same starting Tribute, same lane).

| Match | Predicted winrate (50% = balanced) | Notes |
|-------|------------------------------------|-------|
| Leonidas vs Montezuma II | 50%-58% Aztec favor (post-Lever-2) | Aztec compounding economy gives mid-late-match send advantage; Leonidas lockdown valuable defensively but doesn't accelerate income. **Acceptable; within ±10% balance window. R5 closes without further tune.** |
| Leonidas vs Ragnar | 48%-52% balanced | Greek lockdown vs Norse summon-pressure trades cleanly; Leonidas defends well, Ragnar pressures sends. Even matchup. **Cleanest matchup of the three.** |
| Montezuma II vs Ragnar | 52%-58% Aztec favor (post-Lever-2) | Same compounding-economy advantage; Norse summons effective defensively but vulnerable to Aztec late-game DPS scaling from Tribute-funded T4 tier-ups. **Acceptable; within window.** |

**Pre-Lever-2 winrates** were 60%-68% Aztec favor on both Aztec matchups — Lever-2 brings these into ±10% window.

### Summon-cap interaction audit (signature-window exception)

R4 Heathen Army spec includes signature-window exception: `summons_alive_max = 3 (default) → 9 (during 12s Heathen Army window)`. R5 confirms this is authoring-clean:
- Default cap 3 = 1 Son (passive) + 2 Berserkers (active) + 0 Heathen Warriors when Heathen Army inactive. Cap exact-fit.
- During 12s Heathen Army window: 1 Son + (0-2 Berserkers if cast within window) + 8 Heathen Warriors = up to 11 total. **Exception cap 9 means Berserk fails if cast during Heathen Army window** (per R4 edge case — cast still consumes CD, no refund).
- Practical: R4 windowing means player who casts both Berserk and Heathen Army within 12s effectively wastes one Berserk cast. Player skill discipline = stagger casts or accept wasted cast.
- Authoring this in §4.1 rewrite: explicit `summon_cap_signature_window_exception = 9 during signature-active duration` rule, with clear specification that other summons (Berserk) fail-cast (consume CD, no spawn) when at-cap.

### §4.6a Send-Creeps cross-mode currency attribution

R4 flagged: defender-side Aztec-tower kills in attacker's Sun Offering / Great Sacrifice-bumped state — currency-flow attribution rules need explicit spec.

**R5 resolution:** All Tribute bonuses from Sun Offering / Great Sacrifice / Blood Tribute apply ONLY to the Aztec-commander player who cast them. Defender-side kills of attacker's sent creeps award Tribute to the **defender** per standard §4.6a Send-Creeps rules (defender keeps the kill yield); the Aztec commander's bonuses are commander-bound, not board-bound, so attacker's bonuses do not transfer when defender kills attacker's creeps. Symmetrically: if defender is Aztec and kills attacker's sent creeps, defender's Aztec bonuses fully apply to those kills.

**Implementation note:** Per-Aztec-tower flags (`bonus_tribute_yield_in_active_zone` + `permanent_tribute_yield_multiplier`) read from the **owning player's** commander state, not from the kill-credited player's commander state. Attacker's kills in defender's lane (rare — only via Call-for-Help reverse-send pattern) credit attacker normally and apply attacker's commander bonuses; defender's kills always credit defender and apply defender's commander bonuses.

## Per-commander one-pagers (closes §4.8 exit-gate item #1)

### Leonidas — one-pager

**Civilization:** Greek (Spartan archetype within Greek roster). Anointed-tower aura: Greek-civ-matched towers within hex-distance ≤ 2 of anointed tower.

**Three-ability kit:**
- **Spartan Training** (passive): 15% slow on enemies in 2-cell aura, 50% soft-cap (additional slow sources cap stacking). Reads as: enemies entering Greek territory move sluggishly; phalanx discipline. Bound effect-type: **Control**.
- **This Is Sparta!** (short-CD active, 30s CD): 4s hard-stun + 1-cell knockback in 3-cell radius around player-aimed cell. The cinematic kick-into-pit moment. ~2,700 marginal damage per cast.
- **The Last Stand** (signature, once-per-match free): 12s persistent zone-denial in 4-cell radius. Hard-stuns all enemies present at cast + any enemy entering the zone for the remainder of the 12s window. The "300 hold the pass" peak. ~28,800 marginal damage per cast.

**Identity reading:** "You are the man who holds the pass." Greek lockdown 3-tier escalation: passive baseline (always slowing) → active local punctuation (spot-lock 3-cell zone) → signature peak (12s 4-cell dead-zone). Spatial play maximally expressed; placement-skill axis (b) compounds with anointed-tower-anchor decision and aura geometry.

**Solo campaign storyline (outline):** 30-round historic match-arc culminates round 30 vs **Xerxes I** (Persian king, named historic). Greek narrative arcs through outer wars (Marathon-style mid-rounds) → mountain pass defense (R20-R25) → final stand at Thermopylae (R30 boss). Mortal-tier antagonist; civ-coded environmental beats lean Mediterranean coastal/mountainous.

**Cosmetics + voice unlock path:** 20-level ladder per §4.1 floor (1 portrait + 1 silhouette + 1 skin slot + 1 portrait frame + 1 map tint, default counts as 1). 12 voice lines per §4.1 (3 pick / 3 victory / 3 defeat / 3 ability) + 6 alt VO banks per ability per §4.1 fatigue-mitigation budget.

**Cultural-sensitivity gate (Follow-up #5):** **300-ideology audit required.** The Frank Miller / Snyder-film aesthetic is the cultural-load center for Leonidas — pose, music, VO must navigate between (a) leaning into the iconic recognizable cinematic register and (b) avoiding the "warrior-supremacist" reading the original films were criticized for. Mechanical spec is ideology-neutral (slow + stun + zone-denial work for any culture); art/lore direction owns the audit.

**Cross-arc dependencies:**
- Per-tower authoring: Greek 6 T1-T3 towers (Phalanx / Acropolis / Oracle / Colossus / Trireme Dock / Parthenon — names from 2026-04-25 ratification) consume aura from anointed tower; placement-coverage axis (b) binds.
- Per-civ specialization: Greek lockdown identity reads in Greek roster status-procs (slow / stagger via Crushing) and in Greek T4 Demigod kit (Achilles / Theseus / Perseus / Hercules / Odysseus / Jason — locked) — Leonidas-aware demigod-specific bonuses TBD per per-civ pass.
- Per-map: lockdown identity wants chokepoint maps; per-map authoring track must include at least one chokepoint-favorable Greek-friendly map at launch.

### Montezuma II — one-pager

**Civilization:** Aztec (Mexica empire pre-contact, per 2026-04-25 ratification — Cortés explicitly OUT of all 30-round narrative). Anointed-tower aura: Aztec-civ-matched towers within hex-distance ≤ 2.

**Three-ability kit:**
- **Blood Tribute** (passive): +15% bonus Tribute per kill in 2-cell aura by Aztec towers; multiplicative w/ §4.6a Economy Bonus aux. Reads as: religious-economic offering yields material reward. Bound effect-type: **Economy**.
- **Sun Offering** (short-CD active, 30s CD): 4s window, 4-cell radius around player-aimed cell, +35% bonus Tribute on Aztec-tower kills in zone during window. The peak local offering. ~46 T per cast at R20 baseline (~14% baseline match income over 18 casts).
- **The Great Sacrifice** (signature, once-per-match free): instant **300 T lump** + permanent **+5%** Aztec-tower yield board-wide for rest of match (Lever-2 applied per R5 audit). The peak global offering. ~185K damage-equivalent amortized over remaining match.

**Identity reading:** "You are the priest-king whose offerings return tenfold." Aztec scaling 3-tier compounding: passive steady offering (constant +15% in aura) → active peak local offering (+35% window) → signature peak global offering (300 T lump + +5% permanent). Full-Aztec-stack post-Sacrifice in active overlap = base × 2.039× per kill — the player who clusters Aztec towers and times Sun Offering casts during peak kill-density during active Sacrifice yield bonus accumulates compounding economic state.

**Solo campaign storyline (outline):** 30-round historic match-arc culminates round 30 in two-phase boss fight: **Tlaxcalan war-leader → Tezcatlipoca avatar** (per 2026-04-25 ratification). Aztec narrative arcs through valley politics + ritual cycles + tributary diplomacy (R1-R25) → Tlaxcalan rival war (R28-R29 phase 1) → Tezcatlipoca-avatar cosmic confrontation (R30 phase 2). Bridge-tier antagonist (mortal → cosmic transition); civ-coded environmental beats lean valley/lacustrine/temple-complex.

**Cosmetics + voice unlock path:** Same 20-level ladder per §4.1 floor.

**Cultural-sensitivity gate (Follow-up #5):** **HEAVIEST cultural-load center across the 3 commanders.** Every ability slot involves religious-mercantile metaphor (Blood Tribute / Sun Offering / Great Sacrifice) — without careful art/lore direction, the kit reads as caricaturing Aztec religion via human-sacrifice imagery. **Required:** external Aztec-cultural consultation per 2026-04-25 Follow-up #5 BEFORE any art lock. Mechanical spec is religion-neutral (pure Tribute economy hooks); art direction must navigate between (a) generic "offering" framing avoiding sacrifice depiction entirely, (b) abstract ritual visual without explicit blood/heart imagery, or (c) consciously stylized historical reverence that earns the depiction. Aztec glyph already deferred to abstract placeholder per [`decisions/2026-05-04-aztec-glyph-abstract-placeholder.md`](2026-05-04-aztec-glyph-abstract-placeholder.md) — same discipline applies to all Aztec commander surfaces.

**Cross-arc dependencies:**
- Per-tower authoring: Aztec 6 T1-T3 towers (Pyramid / Temple of the Sun / Jaguar Warrior Hall / Eagle Warrior Hall / Sacrificial Altar / Feathered Serpent Temple — names from 2026-04-25 ratification) consume `bonus_tribute_yield_in_active_zone` flag (Sun Offering) + `permanent_tribute_yield_multiplier` flag (Great Sacrifice).
- Per-civ specialization: Aztec scaling identity reads in Aztec roster status-procs (toxin / hex via Poison + Arcane) and in Aztec T4 Demigod kit (High Priest-King / Nanahuatzin / Jaguar Champion / Eagle Champion / Blood Priest / Serpent-Priest — locked).
- Per-map: scaling identity wants higher-throughput maps to maximize Tribute/sec — per-map authoring should include at least one income-favorable Aztec-friendly map.

### Ragnar Lothbrok — one-pager

**Civilization:** Norse (Viking-era Scandinavia + raids, locked 2026-04-25). Anointed-tower aura: Norse-civ-matched towers within hex-distance ≤ 2.

**Three-ability kit:**
- **Sons of Ragnar** (passive): one summoned Son @ 40 DPS spawns at anointed tower every 20s (max 1 alive at a time), Slashing attack-type, HP=2× HP_std(R), auto-target nearest enemy in 1-cell radius. Reads as: the heir always at hand. Bound effect-type: **Summon**.
- **Berserk** (short-CD active, 30s CD): spawn 2 Berserkers at player-aimed cell (1 cell apart), each @ 360 DPS × 4s lifespan, Slashing + frontal cleave + Bleed status-proc, HP=1× HP_std(R), auto-target nearest enemy. The burst frenzy. Exact 2,880 burst parity.
- **The Great Heathen Army** (signature, once-per-match free): spawn 8 Heathen Warriors at player-aimed cell (in hex ring around cast cell), each @ 180 DPS × 12s lifespan, Slashing + frontal cleave + Bleed, HP=1.5× HP_std(R), auto-advance toward path frontline. The mass-arrival peak. ~30,000 burst-equivalent + significant DOT propagation. Signature-window summon-cap exception: `summons_alive_max = 9 during 12s window`, returning to 3 at despawn.

**Identity reading:** "You are the king whose warriors answer the call." Norse layered called-warriors 3-tier escalation: passive single sustained warrior (1 Son always there) → active burst frenzy (2 Berserkers @ 4s) → signature mass arrival (8 Heathen Warriors @ 12s, advancing). Three distinct summon behaviors, one identity reading. Ragnar himself never appears on field per §4.1 summoned-on-cast model — the warriors ARE the Commander's presence.

**Solo campaign storyline (outline):** 30-round historic match-arc culminates round 30 vs **Jörmungandr** (the Midgard Serpent — myth-overlay, locked 2026-04-27 per Follow-up #11; Fenrir reserved post-launch). Norse narrative arcs through raids + Anglo-Saxon kingdoms + cosmic prophecy (R1-R25) → Ragnarök beats (R26-R29) → Jörmungandr cosmic confrontation (R30 boss). Cosmic-tier antagonist (peak escalation in cross-civ cosmic-arc spectrum); civ-coded environmental beats lean fjord/longhouse/mythic-snow + final-act cosmic sea.

**Cosmetics + voice unlock path:** Same 20-level ladder per §4.1 floor.

**Cultural-sensitivity gate (Follow-up #5):** **Secondary cultural-load center.** Two specific items: (a) "Heathen" in The Great Heathen Army is historically a Christian-perspective pejorative for non-Christian Norse — pose/lore direction owns whether to (i) keep historical name and lean into reclaimed-pride framing per Norse self-identification, (ii) rename in localization for sensitivity, or (iii) accompany with framing copy distinguishing in-game vocabulary from historical context. (b) Berserker historical accuracy involves entheogenic / shamanic origins — pose/lore direction owns whether to depict (i) generic "frenzy warrior" without psychoactive cues, (ii) historically-grounded shamanic preparation cinematic, or (iii) abstract ritual register. Mechanical spec is religion-neutral.

**Cross-arc dependencies:**
- Per-tower authoring: Norse 6 T1-T3 towers (Longhouse / Mead Hall / Rune Stone / Longship Dock / Berserker Lodge / Forge — names from 2026-04-25 ratification). Sons of Ragnar passive Son spawns at anointed Norse tower; Slashing attack-type cross-references 2026-04-26 attack-type-mapping.
- Per-civ specialization: Norse called-warriors identity reads in Norse roster status-procs (bleed via Slashing) and in Norse T4 Demigod kit (Björn Ironside / Beowulf / Harald Bluetooth / Leif Erikson / Lagertha / Sigurd — locked).
- Per-map: called-warriors identity wants paths that summons can engage — per-map authoring must avoid maps where auto-advance Heathen Warriors are stranded off-path.

## §4.1 mechanical-content rewrite (specified in this section, applied to spine doc as separate edit)

Required changes to `concept/phase-4.md §4.1`:

1. **Replace "board-wide invisible, not aura-scoped" wording** in the Surface table row for Passive effect — must reflect anointed-tower aura model.

2. **Replace "No aura that lingers on the board" non-goal bullet** — this contradicts the new anointed-tower aura model. Replace with: "No mobile commander avatar (passive aura is anointed-tower-anchored, not free-positioned by player movement)."

3. **Add new subsection after §4.1 "In-match presence model — summoned-on-cast":** "**Anointed-tower aura model (R5 close 2026-05-05).**" Body specifies: anointed-tower mechanics + auto-anoint fallback + re-anoint UX + active-cast vs passive-aura distinction (active casts target player-aimed cell, not aura) + summon-cap default 3 with signature-window exception 9 during 12s Heathen Army duration.

4. **Update "Each Commander also gets a one-page mechanical writeup before Phase 4 exits" paragraph** — mark closed (one-pagers landed in this R5 decision file as referenced section).

5. **Update §4.1 header** — remove "[PROPOSAL]" and "per-commander writeup OPEN" tags; replace with "(per-commander writeup CLOSED 2026-05-05)" since one-pagers are now landed.

## §4.11.6 deferral-language removal (specified in this section, applied as separate edit)

Required changes to `concept/phase-4.md §4.11.6`:

1. **Replace last paragraph** ("Per-commander effect-type variants ... are deferred to the per-commander authoring sub-pass — only the damage-floor magnitudes above are spec-locked.") with R2-R4 outcomes summary referencing R2/R3/R4/R5 decision files + Lever-2 applied to The Great Sacrifice.

## §4.8 exit-gate item #1 tick (specified in this section, applied as separate edit)

Required changes to `concept/phase-4.md §4.8`:

1. **Add "✓" or "DONE 2026-05-05" inline annotation** to the first bullet ("Commander one-pagers complete for all 3 launch commanders...") with cross-reference to R5 decision file for one-pager content.

## Alternatives considered (R5 audit decisions only)

1. **Lever 1 alone** (drop Sun Offering 35→25%) — rejected; insufficient to bring Aztec into band (still hot at ~104-130%).
2. **Lever 3 alone** (cap Sacrifice permanent at 5 rounds) — rejected; over-corrects (~55-70% in band but signature peak feel evaporates).
3. **Combine all 3 levers** — rejected; under-corrects to ~50-60% Aztec ratio, drops Aztec well below other commanders, breaks Aztec scaling identity.
4. **Lever 2** — accepted (cuts both signature lump AND permanent yield in half; preserves duration).
5. **Aura-anchor alternatives (b) Commander-pedestal and (c) board-wide** — rejected per Loop 1 critiques + Loop 3 synthesis.
6. **Hardcore Last Stand 13s flex** — pre-approved but not yet applied (deferred to playtest validation; Lever-1-style adjustment available without re-opening R4).

## Reason

- Aura-anchor 3x debug loop produces a clear (a) anointed-tower winner that preserves spatial-play identity for all 3 commanders.
- Hard expert simulation surfaces Aztec breakpoint breach; pre-bracketed Lever-2 brings it back to band without breaking scaling identity.
- PvP-IW winrate post-Lever-2 within ±10% across all matchups.
- Per-commander one-pagers consume R2-R4 specs cleanly + close §4.8 exit-gate item #1 + carry cultural-sensitivity Follow-up #5 forward with explicit per-commander load-center notes.
- Spine-doc §4.1 + §4.11.6 + §4.8 edits resolve all cascade-drift carried from R2-R4.

## Reversibility

**Medium overall.** Hard-class guards on the 9 mechanical specs (lane locks themselves remain Hard per R4). Aura-anchor (a) anointed-tower is reversible to (b) or (c) via formal cascade if playtest surfaces deal-breaker UX issues — would re-open §4.1 mechanical-content. Lever-2 on The Great Sacrifice is reversible at any time via parameter tune if Aztec post-Lever-2 under-delivers (drop floor lump to 200 T or +3% permanent moves further down; raise to 400 T / +7% moves back up). Hardcore Last Stand 13s flex remains pre-approved.

**Hard at this point in arc:** Effect-type lane assignments per commander (Leonidas=Control, Montezuma II=Economy, Ragnar=Summon) — reversing would cascade-rewrite the full identity arc.

## Follow-ups

1. **Spine-doc edits applied as separate Edits in same R5 close** — §4.1 mechanical-content rewrite + §4.11.6 deferral removal + §4.8 exit-gate tick.
2. **Decisions table row + CASCADE pointer + version footer 0.59 → 0.60** + 0.58 archived to history.
3. **Final dual-push checkpoint** (carries R4 + R5; closes per-commander effect-type-variant authoring arc).
4. **Cultural-sensitivity Follow-up #5** carries forward — heaviest load Aztec, secondary Norse, lightest Greek; mandatory consultation gate before any art lock per 2026-04-25 ratification.
5. **Cross-arc per-tower authoring sub-pass** unblocked — consume `aztec_tower.bonus_tribute_yield_in_active_zone` flag + `aztec_tower.permanent_tribute_yield_multiplier` flag + `summons_alive_max = 3` cap (with signature-window exception) + Slashing-Bleed status-proc cross-ref to 2026-04-26 attack-type-mapping. R2-R4 commander-side hooks fully spec'd.
6. **Cross-arc per-civ authoring sub-pass** consumes: full-Greek-stack lockdown overlap zone; full-Aztec-stack scaling overlap (post-Lever-2 base × 2.039× compounding); full-Norse layered called-warrior summon identity.
7. **Cross-arc per-map authoring sub-pass** consumes: chokepoint-favorable map for Greek lockdown identity; throughput-favorable map for Aztec scaling identity; path-engageable map for Norse called-warriors identity (no off-path stranding for auto-advance Heathen Warriors).
8. **Phase 4 exit unblocked** at item #1; remaining §4.8 items (Fusion shape signed off ✓ done; mobile unit control § 4.4 OPEN BLOCKER; enemy direction §4.7 OPEN; economy balanced ✓ done via §4.6 + §4.6a + Numbers-phase; monetization specifics; engine choice; art director scope; cultural-sensitivity gate) carry forward.
9. **Hardcore playtest validation** — Last Stand 13s flex remains pre-approved; apply if Hardcore R25-R30 boss-wave under-delivery shows in playtest.
10. **PvP-IW post-Lever-2 winrate validation** — predicted 50-58% Aztec favor; live playtest measurement gates further adjustment.
