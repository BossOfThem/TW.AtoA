# Decision — Per-commander R4: signature-slot variants (The Last Stand / The Great Sacrifice / The Great Heathen Army)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** Forward-anchored to [`concept/phase-4.md §4.1`](../concept/phase-4.md) (R5 mechanical-content rewrite) + `§4.11.6` (R5 deferral-removal). No spine-doc edits this round.

---

## Decision

Bind mechanical specs for the **signature (i)-slot variants** across all 3 launch commanders against the §4.11.6 damage-floor benchmark (signature: once-per-match free tier-up T1→T2 OR T2→T3 — equivalent to a 100 T or 300 T injection at the moment of cast, plus the per-tier DPS jump applied for the rest of the match). Effect-type lane locked from R2-R3 per commander to preserve identity coherence: Leonidas=Control, Montezuma II=Economy, Ragnar=Summon. Each variant reads as the commander's **identity peak** per R3 closing readings (Greek lockdown / Aztec scaling / Norse mass-summon).

| Commander | Civ | Signature name (locked §3.2) | Effect type | Equivalent-impact mechanism |
|-----------|-----|------------------------------|-------------|-----------------------------|
| **Leonidas** | Greek | **The Last Stand** | **Control** | Peak-lockdown ult: 12s zone-denial in 4-cell radius (hard-stun all enemies entering zone for full duration; existing enemies on cast hard-stunned for 12s) |
| **Montezuma II** | Aztec | **The Great Sacrifice** | **Economy** | Peak-scaling ult: instant Tribute injection of 600 T + permanent +10% Tribute yield for rest of match on Aztec-tower kills board-wide |
| **Ragnar Lothbrok** | Norse | **The Great Heathen Army** | **Summon** | Mass-summon ult: spawn 8 Heathen Warriors at cast cell, each 180 DPS, Slashing, 12s lifespan, semi-autonomous (advance toward path frontline) |

**Cadence discipline (§4.10.5 signature-excluded-from-uptime):** All 3 signatures are **once-per-match free casts** (no Tribute / Divinity cost — the cast itself IS the spend) and explicitly **excluded from the §4.11.8 ability-uptime axis** per §4.10.5 (signatures are commitment moments, not uptime mechanics). Player chooses cast timing; cannot recast within a match.

**Signature equivalent-impact target:** §4.11.6 free-tier-up baseline = 100 T (T1→T2) or 300 T (T2→T3) injection + per-tier DPS jump applied to one tower for rest of match. Mid-match cast (R15-R20) → ~300 T value + (T2 DPS - T1 DPS) × ~450s remaining = ~300 + 40 × 450 = ~18,300 damage equivalent OR ~(T3 DPS - T2 DPS) × 450 = ~(180-60) × 450 = 54,000 damage equivalent depending on which tier-up player picks. Take **midpoint ~36,000 damage-equivalent** as R4 calibration target with ±15% band (signatures are larger swings than (g) actives, looser tolerance per scope decision).

## Context

Signatures are the commander identity-peak — the moment the player commits to "this is what my commander does." Per R3 readings:
- Greek = lockdown identity → signature must lock down harder/longer/wider than the (g) active.
- Aztec = scaling identity → signature must scale the economy further/permanently/larger.
- Norse = called-warrior identity → signature must summon many warriors at once (vs (g)'s 2-Berserker burst).

Per-effect-type equivalent-impact derivation for signature scale:

- **Control peak-equivalence:** R3 (g) active = 4s stun in 3-cell radius = ~2,700 marginal damage. Signature must be ~13× larger per midpoint target. Cleanest = scale up duration AND radius: 12s (3× duration) × 4-cell radius (~1.78× area) = ~5.34× spatial-temporal scale. Per cast: 12s × ~5 in-firing-range Greek T3s × 180 DPS = 10,800 base marginal — short of 36K target. Boost via **persistent zone** (any enemy entering 4-cell zone gets stunned for full remaining zone duration, not just enemies present at cast moment). Average enemy throughput at R15-R20 ≈ 8-12 enemies/12s through a path zone. Marginal damage per entered enemy = ~3-4s additional engagement-time × 540 DPS in-range = 1,620-2,160 each. 10 entries × ~1,800 = 18,000 + base = **~28,800 burst-equivalent** per cast. Within −20% of 36K midpoint, but signatures lean lockdown-strong on Hardcore (k)=1.22 where stalling matters most → R5 audit can flex.
- **Economy peak-equivalence:** Lump injection + permanent yield bump. 600 T lump = 6× T1 cost = 2 × T2 cost OR 1 × T3 tier-up. Damage-equivalent at mid-match ~120 damage/T = **72,000 from lump alone**. Plus permanent +10% yield for ~450s remaining match on Aztec-tower kills (~5 Aztec towers × ~1 kill/3s × 33 T base × 0.10 bonus × 450s) = ~2,475 T bonus = ~297,000 damage equivalent over remaining match. Total: **~370K damage-equivalent over match** — far above 36K midpoint. **Pre-bracketed:** Sun Offering's R3 amortization asymmetry compounds at signature scale; R5 audit flag applies harder here. Tune-down levers: (a) drop lump to 300 T; (b) drop permanent yield to +5%; (c) cap permanent yield duration at 5 rounds. R4 authors at the **higher** end and lets R5 simulation tune down — easier to nerf a hot signature post-playtest than to buff a cold one. Signature-as-identity-peak reading wins here (Aztec player feels the scaling in their bones).
- **Summon peak-equivalence:** 8 Heathen Warriors × 180 DPS × 12s = **17,280 burst** + Slashing-Bleed status proc (~2,000 additional DOT) + semi-autonomous targeting amplifies vs dense waves. Signature scale falls short of 36K midpoint at face value but **counts engagement-time displacement** — 8 warriors blocking the path absorb HP via taking hits, slowing creep advance through the zone (effectively a stun-by-blocking). Realistic match-impact = base burst + path-block engagement-time gain ≈ 17,280 + (8 warriors × ~3s blocked × 540 DPS in-range) = 17,280 + 12,960 = **~30,000 burst-equivalent**. Within −17% of 36K midpoint; on the lockdown-strong side per RPS positioning. Acceptable.

Authoring all 3 in R4 (per Axis B) lets the signature-tier parity table compare inline.

## Effect-type assignment rationale (per locked-name reading)

**Leonidas — The Last Stand → Control.** Locked name is the Thermopylae-final-defense imagery: "300 hold the pass to the last man." Three readings: (a) damage burst (Spartans go down swinging — but R2-R3 lock Greek into Control lane; lane break would split identity); (b) control (zone denial — the 300 *hold* the pass; nothing gets past until the duration ends, the cleanest "Last Stand" mechanical reading); (c) summon (Spartan reinforcements arrive — overlaps Norse summon lane, breaks identity). Control reads strongest: zone denial *is* the Last Stand metaphor — "this 4-cell zone does not let creeps through for 12s." The persistent-zone behavior (enemies entering during duration get stunned, not just enemies present at cast) reads as "the line holds against the next wave" — the entire historical resonance of Thermopylae. **Cultural-sensitivity Follow-up #5 advance flag:** the Last-Stand visual involves Spartan death imagery — defer to art/pose direction whether to render the Spartans "dying gloriously" vs more abstract "phalanx holding" framing per game-tone audit (mechanical spec is visual-direction-neutral).

**Montezuma II — The Great Sacrifice → Economy.** Locked name is religious-economic at peak intensity: "the great offering, the once-per-match cosmic exchange." Three readings: (a) damage burst (sacrifice → destructive divine wrath — but this lane breaks Aztec-Economy identity); (b) economy (sacrifice → reciprocal cosmic abundance, the cleanest fit to the Aztec religious-mercantile reading per R2-R3); (c) summon (sacrifice → summon a god — overlaps planned Fusion-to-Gods endgame system at §4.3 + breaks Aztec-Economy lane). Economy reads strongest: **the lump-Tribute injection IS the divine reciprocal**, and the permanent yield bump IS the lasting cosmic favor. The peak-scaling identity reading lands cleanest: at signature tier, the Aztec player gets to feel their entire economy lift permanently — this is the Aztec arc's narrative payoff. **Cultural-sensitivity Follow-up #5 advance flag:** the "Great Sacrifice" name + Aztec religious context heavily implicates human-sacrifice imagery — this is the signature most demanding of art/pose/VO sensitivity care. Mechanical spec is religion-neutral (pure Tribute economy hook); art direction must navigate between (a) generic "offering" framing avoiding human-sacrifice depiction entirely, (b) abstract ritual visual without explicit blood/heart imagery, or (c) consciously stylized historical reverence that earns the depiction. R4 authors mechanical content only; art-direction call defers to Follow-up #5 cultural-sensitivity pass.

**Ragnar Lothbrok — The Great Heathen Army → Summon.** Locked name is the historical 865 CE Viking invasion of England — the "Great Heathen Army" is the literal mass force that crossed the North Sea. Three readings: (a) damage burst (Ragnar's wrath unleashed — but R2-R3 lock Norse into Summon lane); (b) control (army intimidation / fear effect — overlaps Greek-Control lane); (c) summon (mass arrival of warriors — the cleanest fit to the historical name + R3 layered-warrior reading peak). Summon reads strongest: 8 Heathen Warriors arriving at one cell at cast moment IS the Great Heathen Army landing — a massive mid-match summon spike that dwarfs the 1 Son (passive) + 2 Berserkers (active) earlier scale. The semi-autonomous "advance toward path frontline" behavior reads as "the army marches" — they don't sit at cast point waiting for enemies, they push forward to engage. Identity peak: locked. **Cultural-sensitivity Follow-up #5 advance flag:** "Heathen" is a historically-loaded term (Christian-perspective pejorative for non-Christian Norse); pose/lore direction owns whether to (a) keep the historical name and lean into reclaimed-pride framing per Norse self-identification, (b) rename in localization for sensitivity, or (c) accompany with framing copy distinguishing in-game vocabulary from historical context. Mechanical spec stays.

## Per-commander mechanical specs

### Leonidas — The Last Stand

| Attribute | Value | Notes |
|-----------|-------|-------|
| Slot | Signature (i) | Per §4.11.6 signature slot |
| Effect type | Control (persistent zone-denial) | Per R2-R3 lane lock |
| Cast target | Player-aimed cell on click | Standard active cast pattern |
| Target class | All enemies — both present at cast AND entering zone during 12s duration (no civ/armor filter) | Persistent zone behavior is the key signature distinction |
| Radius | 4 cells (hex distance ≤ 4 from cast cell) | One step wider than (g) active 3-cell |
| Duration | 12s persistent zone (3× the (g) active 4s) | Zone exists for 12s; any enemy entering during duration is hard-stunned for the remaining duration |
| Stun behavior | Enemies present at cast moment: 12s hard-stun. Enemies entering after cast: hard-stun for whatever duration remains in the 12s zone window. Once stunned, enemies stay stunned even if pushed/moved out of zone (stun is applied, not zone-bound). | Persistent-zone-application is the signature peak |
| Knockback | None (signature is pure lockdown, no displacement) | (g) active had knockback; signature trades displacement for duration scale |
| CD | Once-per-match (no recharge) | Per §4.10.5 signature discipline |
| Cost | Free (cast-itself-IS-the-spend) | Per §4.11.6 signature pricing |
| Equivalent burst | ~28,800 marginal damage at Hard expert mid-match (~5 in-range Greek T3s × 540 DPS × ~12s effective + entering enemies' added engagement-time) | Within −20% of 36K midpoint; lockdown-strong on Hardcore (k)=1.22 per R5 audit flex |
| Civ-affinity hook | None (works for any civ towers in firing range; full-Greek-stack overlap zone produces compounding lockdown — R2 passive 15% slow + R3 active 4s stun + R4 signature 12s stun zone in same area = effective dead-zone of ~4 cells for ~12s) | Signature peak of Greek lockdown identity |
| Per-tower target-side hook interface | None — no per-tower attribute consumed | Towers benefit by being in firing range of zone |
| Status-proc interaction | Stunned enemies cannot apply status to towers; existing status-procs on enemies continue ticking on stunned target normally | §4.10 status-state factor unchanged |
| Edge cases | Bosses get **half stun duration** (6s per Hard-class boss-archetype guard, consistent with (g) active 2s reduction); enemies already stunned by other sources don't stack (max not sum); zone visual MUST clearly indicate the 4-cell radius for player UX (deferred to UI direction); §4.7 R11 wave-randomization may shift wave timing relative to cast — intentional; if cast on no-path cells, zone still applies but no enemies enter (player-skill discipline); zone persists through wave-end — if cast at end of wave R15, zone runs partially into wave R16 spawn (intentional flexibility) | Boss half-duration + zone-cross-wave-boundary explicitly allowed |

### Montezuma II — The Great Sacrifice

| Attribute | Value | Notes |
|-----------|-------|-------|
| Slot | Signature (i) | Per §4.11.6 signature slot |
| Effect type | Economy (lump injection + permanent yield bump) | Per R2-R3 lane lock |
| Cast target | None (instant board-wide effect on cast — no aimed cell) | Distinct cast UX from (g) active; no player-aim required |
| Target class | All Aztec towers board-wide (instant lump goes to commander wallet; permanent yield bump applies to all current + future Aztec towers' kills) | Civ-gated identity preserved |
| Lump Tribute | 600 T injected to commander wallet at cast moment | Worth ~6× T1 cost / 2× T2 cost / ~2× T3 tier-up |
| Permanent yield bump | +10% bonus Tribute on Aztec-tower kills board-wide for remainder of match | Applies in addition to: passive Blood Tribute +15% in aura (multiplicative stack: in-aura post-Sacrifice = base × 1.15 × 1.10 = 1.265×); active Sun Offering +35% in window (multiplicative stack: in-active-zone post-Sacrifice = base × 1.35 × 1.10 = 1.485×); §4.6a Economy Bonus aux +25% (full-stack post-Sacrifice = base × 1.25 × 1.15 × 1.35 × 1.10 = base × 2.139× per kill in overlap during active window) |
| CD | Once-per-match (no recharge) | Per §4.10.5 signature discipline |
| Cost | Free (cast-itself-IS-the-spend) | Per §4.11.6 signature pricing |
| Equivalent value | Mid-match cast: 600 T lump (~72K damage-equivalent over remaining match via T1 buys at 120 damage/T) + permanent +10% bump (~2,475 T bonus over ~450s remaining = ~297K damage-equivalent) ≈ **~370K damage-equivalent total** | Far above 36K midpoint; intentional Aztec scaling identity peak — pre-bracketed for R5 tune-down if Hard 100% breakpoint breached |
| Civ-affinity hook | Aztec-only kill bonus | Civ-gated identity preserved across (h)+(g)+(i) slots |
| Per-tower target-side hook interface | Per-Aztec-tower `permanent_tribute_yield_multiplier` flag (default 1.0; flipped to 1.10 board-wide post-Sacrifice cast) — read in tower yield calc as: `yield = base × passive_aura_factor × active_zone_factor × permanent_sacrifice_factor × economy_aux_factor` | Cross-arc per-tower authoring binds here; flag is permanent (never resets within match) |
| Status-proc interaction | None — pure economy variant, no combat-state interaction | Status-procs unaffected |
| Edge cases | If cast pre-wave-1 (round 0), permanent yield applies for full 30 rounds (~maximum value — intentional skill-cast discipline); if cast on round 30 (final round), permanent yield bonus minimal (~5 std kills × 33 T × 0.10 = 16 T, lump still 600 T = ~600 T total, intentional skill-cast discipline penalty for late cast); §4.6a Send-Creeps zone interaction: defender-side Aztec-tower kills count for sender's permanent yield bump if defender has Aztec commander Sacrifice active — flagged for R5 audit (cross-mode currency flow); boss-lump Tribute multiplier: post-Sacrifice boss kills yield 1.10× lump (R10 boss = 250×1.10 = 275 T; R30 boss = 1500×1.10 = 1650 T — significant late-match boost; intentional) | R5 audit on boss-lump amplification + cross-mode interaction |

### Ragnar Lothbrok — The Great Heathen Army

| Attribute | Value | Notes |
|-----------|-------|-------|
| Slot | Signature (i) | Per §4.11.6 signature slot |
| Effect type | Summon (mass-summon spike) | Per R2-R3 lane lock |
| Cast target | Player-aimed cell on click | Standard active cast pattern |
| Spawn count | 8 Heathen Warriors | 4× the (g) Berserker count |
| Per-Warrior DPS | 180 DPS (= T3 base DPS) | Each Warrior fights at T3 tower equivalence |
| Per-Warrior HP | 1.5 × HP_std(R) | Between Berserker (1×) and Son (2×) — durable enough to survive frontline contact |
| Lifespan | 12s (despawn at end) | 3× the (g) Berserker 4s |
| Attack type | Slashing (Norse civ-affinity) | RPS hooks: +25% vs Unarmored / Beast; -25% vs Shielded |
| Cleave | Frontal cleave 1-cell (matches Berserkers) | Hits primary target + adjacent enemies in same hex direction |
| Targeting | Auto-target nearest enemy in 1-cell radius; if no target in 1 cell, **advance toward path frontline** (toward path direction, not retreat) until target acquired | Distinguishes from passive Sons (which sit at aura) and active Berserkers (which sit at cast cell) — Heathen Warriors push forward, the "army marches" reading |
| Spawn position | At cast cell + adjacent cells in 2-cell radius (8 Warriors arranged in hex ring around cast cell) | Visual reads as army landing |
| CD | Once-per-match (no recharge) | Per §4.10.5 signature discipline |
| Cost | Free (cast-itself-IS-the-spend) | Per §4.11.6 signature pricing |
| Equivalent burst | 8 × 180 DPS × 12s = 17,280 base + Bleed status (~2K) + path-block engagement-time gain (~12,960) ≈ **~30,000 burst-equivalent** | Within −17% of 36K midpoint; on the lockdown-strong side per RPS positioning |
| Civ-affinity hook | None (Heathen Warriors are summoned units, civ-neutral targets — they do not buff or debuff Norse towers; their Slashing attack-type alignment IS the Norse identity hook) | Cross-civ play: Warriors spawn regardless of player's tower-civ composition |
| Per-tower target-side hook interface | None — Warriors are units, not tower buffs; consume `unit_dps_contribution` slot. Counting cap: `summons_alive_max` raised to **9 max during 12s Heathen Army window** (1 Son + 8 Warriors) — temporarily exceeds R3-locked 3 max for the 12s window only (signature-tier exception). After Warrior despawn at 12s, cap returns to 3. If Berserk active overlaps the window, cap caps at 9 and Berserker spawn fails (cast still consumes — no refund); player-skill timing discipline. | Cross-arc summon-cap interaction; flagged for R5 simulation |
| Status-proc interaction | Warriors' Slashing attacks apply Bleed status (per 2026-04-26 attack-type-mapping) at standard tower proc rate; with 8 warriors + cleave, Bleed application stacks rapidly across waves (within Bleed stacking rules per attack-type-mapping) | Significant DOT contribution in dense waves |
| Edge cases | If cast at boss-collision cell, Warriors absorb significant boss damage (mini-tank pattern — intentional Norse identity reading: the army takes the hit so the towers don't); §4.6a Tower-count expansion aux does NOT increase Warrior spawn count (aux affects tower slots, not summon slots — explicit clarification, consistent with Berserk); Warriors killed before 12s lifespan don't respawn (lifespan is wall-clock, not life-pool); cast on no-path cell still spawns 8 Warriors but they wander forward to find path (some travel-time inefficiency — player-skill discipline); wave-end transition: 12s lifespan persists across wave boundary (intentional flexibility for late-wave casts) | Boss-tank pattern + cross-wave-boundary explicitly allowed |

## Cross-commander parity check

Target: ±15% equivalent-impact at §4.11.8 Hard expert thresholds (looser than R3's ±10% per signature scale tolerance per scope decision). All 3 variants land within band or pre-bracketed for R5 tune.

| Commander | Signature variant | Equivalent burst (mid-match cast) | Δ vs 36K midpoint | Match-span impact (1 cast/match) | Notes |
|-----------|-------------------|-----------------------------------|---------------------|-----------------------------------|-------|
| Leonidas | The Last Stand | ~28,800 (Control persistent zone) | −20% | ~28,800 (single-cast) | Lockdown-strong on Hardcore (k)=1.22 per RPS positioning; R5 audit may flex duration to 13-14s if Hardcore breakpoint underperforms |
| Montezuma II | The Great Sacrifice | ~370,000 (Economy lump + permanent yield over remaining match) | high (+927%); ~tier-defining when fully amortized | ~370,000 (compounds) | Pre-bracketed for R5 tune-down if Hard 100% breakpoint breached: levers are (a) drop lump 600→300 T, (b) drop permanent +10%→+5%, (c) cap permanent duration at 5 rounds. Aztec scaling identity at peak — intentional asymmetry continues from R3 Sun Offering pattern |
| Ragnar | The Great Heathen Army | ~30,000 (Summon: 17,280 base + Bleed DOT + path-block engagement-time) | −17% | ~30,000 + significant Bleed DOT propagation in dense waves | Within band; Bleed propagation across wave R-cycles may amplify in late-match Hardcore — R5 simulation owns confirming |

**R5 audit flags carried forward + new:**
- (carried R3) Sun Offering amortization → **escalated** at R4 signature scale via The Great Sacrifice; R5 must simulate full Aztec stack: passive Blood Tribute (+15% in aura) + active Sun Offering (+35% in window) + signature Great Sacrifice (+10% permanent + 600 T lump) + Economy Bonus aux (+25% baseline) → full-stack base × 2.139× per kill in overlap during active window. If this breaches Hard 100% breakpoint OR pushes Aztec winrate >55% in PvP-IW vs Greek/Norse, tune-down levers above apply.
- (new) Last Stand persistent-zone duration vs Hardcore lockdown breakpoint — may need 13-14s flex on Hardcore.
- (new) Heathen Army summon-cap exception (3 → 9 during 12s window) — must be cleanly authored in §4.1 rewrite with explicit signature-scope wording; cross-Berserk-overlap cap-fail flagged.
- (new) Heathen Army Bleed DOT propagation across waves at Hardcore — simulation flag.
- Active-cast-target distinction from passive-aura-anchor in §4.1 rewrite remains owned by R5 (now has 3 active-cast variants + 3 signature variants depending on the distinction holding).

**Cross-arc per-tower target-side hooks specified across full R2-R4 sweep:**
- `aztec_tower.bonus_tribute_yield_in_active_zone` flag (R3 Sun Offering consumer)
- `aztec_tower.permanent_tribute_yield_multiplier` flag (R4 The Great Sacrifice consumer; default 1.0, set to 1.10 board-wide post-cast)
- Global `summons_alive_max = 3` (default; signature-window exception → 9 during Heathen Army 12s)
- Berserker / Heathen Warrior Slashing-Bleed status-proc cross-references 2026-04-26 attack-type-mapping
- No `greek_tower.*` flag needed across the arc (Control acts on enemies)

## Per-commander identity readings

**Leonidas** (post-R4 reading, identity arc complete): Control lane reads as a **3-tier lockdown escalation** across the kit. Passive (Spartan Training) is the *baseline tactical positioning* — slow zone keeping enemies in Greek tower kill-windows longer, always-on. Active (This Is Sparta!) is the *cinematic zone-lock* — kick + 4s hard stun in 3-cell radius, 30s CD, the "lock down a key spot" tool. Signature (The Last Stand) is the *peak last-stand zone-denial* — 12s persistent zone in 4-cell radius that keeps stunning every enemy entering the area; the "the line holds" once-per-match commitment. The full-Greek-stack overlap zone produces a compounding effect: enemies move slowly through Leonidas's aura by default, occasionally get kicked entirely off the path, and during The Last Stand the entire 4-cell zone becomes a death-stop dead-zone where Greek towers chew through stationary targets. Identity arc payoff: **the Greek player is the player who controls space.** The lockdown reads cleanly across all 3 ability slots; no internal competition or muddled mechanical language. R5 one-pager owes the narrative spine: "you are the man who holds the pass."

**Montezuma II** (post-R4 reading, identity arc complete): Economy lane reads as a **3-tier scaling escalation** across the kit. Passive (Blood Tribute) is the *steady offering* — Aztec towers in aura yield 15% more Tribute on every kill, constant bleed of bonus income. Active (Sun Offering) is the *peak local offering* — 4s window where Aztec kills in 4-cell zone yield +35%, requires active player engagement to capitalize. Signature (The Great Sacrifice) is the *peak global offering* — instant 600 T lump + permanent +10% Aztec-tower yield board-wide for rest of match. The full-Aztec-stack overlap zone during active window post-Sacrifice produces compounding economic state: base × 1.15 (passive) × 1.35 (active) × 1.10 (signature) × 1.25 (Economy Bonus aux) = base × 2.139× per kill — a 113% bonus Tribute yield in overlap during active window. Identity arc payoff: **the Aztec player is the player whose economy compounds.** The scaling reads cleanly across all 3 ability slots; no internal competition. R5 one-pager owes the narrative spine: "you are the priest-king whose offerings return tenfold." **Cultural-sensitivity Follow-up #5 advance flag escalates here** — the Aztec arc is the most dependent on careful art/lore direction across all 3 commanders, since every ability slot involves the religious-mercantile metaphor.

**Ragnar Lothbrok** (post-R4 reading, identity arc complete): Summon lane reads as a **3-tier called-warriors escalation** across the kit. Passive (Sons of Ragnar) is the *single sustained warrior* — one persistent Son @ 40 DPS, always there, low-intensity but constant — the "ever-present heir." Active (Berserk) is the *burst frenzy of warriors* — 2 short-lived Berserkers @ 360 DPS × 4s, 30s CD, the "berserk warriors strike then are gone" tool. Signature (The Great Heathen Army) is the *historical mass-arrival* — 8 Heathen Warriors @ 180 DPS × 12s with auto-advance toward path frontline; the "the army has come" once-per-match commitment. Across the kit, the player commands warriors at three distinct intensities (1 always-on, 2 burst-spike, 8 mass-arrival), all Slashing-typed (RPS positioning skill against Unarmored / Beast / Shielded waves). The semi-autonomous "advance toward frontline" Heathen Warriors distinguish themselves from the static-aura Sons and cast-cell-bound Berserkers — three distinct summon behaviors, one identity reading. Identity arc payoff: **the Norse player is the player who calls warriors.** Ragnar himself never appears on field (per §4.1) — the warriors ARE the Commander's presence on the board. The called-warrior arc reads cleanly across all 3 ability slots. R5 one-pager owes the narrative spine: "you are the king whose warriors answer the call." **Cultural-sensitivity Follow-up #5 advance flag** on "Heathen Army" historical-loaded term and on entheogenic Berserker historical accuracy.

## Alternatives considered

1. **All 3 signatures as direct damage bursts (lane-break across the board)** — rejected per R2-R3 lane lock + identity erosion. Signatures must peak the commander's identity, not defect to a generic damage-dealer fourth lane.
2. **Cost-based signatures (e.g., 3 Divinity per cast)** — rejected per §4.11.6 signature wording (free cast). Once-per-match free is the §4.11.6 baseline; pricing signatures would cascade-violate that anchor.
3. **Multi-cast signatures (2-3 uses per match)** — rejected per §4.10.5 "signature is once-per-match commitment." Multi-cast reduces the commitment moment and softens the identity-peak reading.
4. **The Last Stand as Leonidas-self-buff (Leonidas appears on field, takes hits)** — rejected per §4.1 (Commander summoned-on-cast, not persistent on-field). The persistent-zone reading respects §4.1 cleanly while delivering the "Last Stand" metaphor.
5. **The Great Sacrifice as Divinity injection (1-3 free Divinity instead of Tribute lump)** — considered, rejected. Divinity is constrained to 6-source roster per Numbers-phase R10 + §4.6 economy spec; signature should not become a 7th Divinity source. Tribute lump stays in-frame.
6. **The Great Heathen Army as semi-permanent warriors (24s instead of 12s)** — rejected at parity tier; 24s pushes burst-equivalent to ~50K, well above 36K midpoint. Could revisit at R5 if 30K under-delivers in playtest.
7. **The Great Heathen Army as one massive Hero-tier unit (1 Warrior at 1440 DPS instead of 8 at 180)** — rejected for cleave + Bleed-stack richness + visual impact (8 warriors > 1 hero in identity reading "the army has come"). Hero-tier 1-unit pattern reserved for potential Patch-1 commander or Foresight-coin item.
8. **Tighter parity band (±10% across all three at signature tier)** — considered but rejected. Signature-tier swings inherently bigger; ±15% scope decision allows the Aztec scaling asymmetry to survive R5 simulation honest, rather than being neutered to fit a tighter R3-style band.

## Reason

- Effect-type lane lock per commander preserves identity coherence across (h)/(g)/(i) — the full kit reads as one mechanical language per commander.
- Signature-tier ±15% band accommodates intentional Aztec scaling-identity asymmetry while keeping Greek + Norse within tighter parity.
- Pre-bracketed R5 tune-down levers for Aztec keep the asymmetry honest: simulation-driven, not eyeball-driven.
- Cross-arc per-tower target-side hook interfaces specified now (across R2+R3+R4) keep cross-arc per-tower authoring fully unblocked.
- Cultural-sensitivity Follow-up #5 mechanical/visual separation discipline maintained across all 3 specs (most-loaded for Aztec, second-most for Norse Heathen Army, least-loaded for Greek Last Stand).

## Reversibility

**Medium with three identity-coherence guards:**
- If R5 simulation shows Last Stand's 12s persistent zone underperforms on Hardcore → flex to 13-14s duration (still within Control-lane character).
- If R5 simulation shows The Great Sacrifice pushes Aztec past Hard 100% breakpoint OR PvP-IW winrate >55% → apply pre-bracketed tune-down (lump 600→300 T, permanent +10%→+5%, cap permanent at 5 rounds; pick one or two).
- If R5 simulation shows Heathen Army Bleed propagation overshoots in late-match Hardcore waves → drop frontal cleave (single-target only) OR shorten lifespan to 10s.

Lane locks themselves are NOT reversible at this point — R2-R3-R4 all assume them; reversing would cascade-rewrite the full identity-arc. Lane locks treated as Hard at this point in arc; can only reopen via formal cascade discipline (PROGRESS debt + decision file).

## Follow-ups

1. **R5 next** — **CLOSES arc**: cross-commander balance audit (9-spec parity check + match-impact simulation against §4.11.8 Hard + Hardcore expert thresholds + PvP-IW winrate sanity check) + 3 per-commander one-pagers (Leonidas / Montezuma II / Ragnar Lothbrok narrative-mechanical synthesis) + **`phase-4.md §4.1` mechanical-content rewrite** (consuming R2-R4 specs + resolving aura-anchor sub-decision per 3-candidate flag + clarifying active-cast vs passive-aura distinction + summon-cap with signature-window exception) + **`§4.11.6` deferral-language removal** + **`§4.8` Phase 4 exit gate item #1 tick** (commander one-pagers complete).
2. **Dual-push checkpoint after R5 close** — carries R4 + R5 per scope decision cadence.
3. **Cultural-sensitivity Follow-up #5** advance flag preserved on all 3 signature visuals — escalates for Aztec (Great Sacrifice religious imagery), secondary for Norse (Heathen Army historical-loaded term + Berserker entheogenic accuracy), least for Greek (Last Stand death imagery, more abstract-friendly).
4. **Cross-arc per-tower authoring** binds to: `aztec_tower.bonus_tribute_yield_in_active_zone` (R3 hook); `aztec_tower.permanent_tribute_yield_multiplier` (R4 hook); global `summons_alive_max = 3` default + signature-window exception to 9; Berserker + Heathen Warrior Slashing-Bleed cross-ref to 2026-04-26 attack-type-mapping.
5. **Cross-arc per-civ authoring** consumes: full-Greek-stack lockdown overlap zone (passive slow + active stun + signature persistent zone); full-Aztec-stack scaling overlap (passive +15% + active +35% + signature +10% permanent + Economy aux +25% = base × 2.139× compounding); full-Norse layered called-warrior identity (1 sustained + 2 burst + 8 mass-arrival, all Slashing).
6. **§4.6a Send-Creeps cross-mode interaction** flagged for R5: defender-side Aztec-tower kills in attacker's Sun Offering / Great Sacrifice-bumped state — currency-flow attribution rules need explicit spec.
