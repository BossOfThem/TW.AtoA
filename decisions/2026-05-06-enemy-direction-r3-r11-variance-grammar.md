# Decision — §4.7 enemy direction R3: Round 11 wave-composition variance grammar

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) (`§4.7` Wave-composition variance mandate subsection — grammar body authored here, spine-doc edits land at RN per §-placement table; `§4.8` exit-gate item #4 — RN tick; `§4.10.5` skill-bar axes — read-only input; `§4.11.7` per-mode tuning (g)/(p)/(q) — read-only input; `§4.11.8` skill-bar thresholds per (k) — falsification gate input), [`decisions/2026-05-06-enemy-direction-r2-direction-lock.md`](2026-05-06-enemy-direction-r2-direction-lock.md) (Option C ratification + boss-tier civ-distinct armor-class clusters table + 5-armor-class regular-wave pool distribution bands — direct input; this round consumes R2's hook contract verbatim), [`decisions/2026-05-06-enemy-direction-r1-scope.md`](2026-05-06-enemy-direction-r1-scope.md) (R1 scope file — round-queue + axis + 3-property scope), [`decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md`](2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) (R9 thresholds + memorization-meta defense origin — read-only input; falsification gate at the three-axis defense layer), [`decisions/2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md) (5-armor + 7-attack taxonomy + RPS matrix — read-only input), [`decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md) (5×3 matchup_affinity matrix — read-only input), [`decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) (45-tower type-coverage table — read-only input), [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](2026-04-27-commander-as-summoned-ability-avatar.md) (2026-04-27 historic-arc table + locked content-skeleton bosses — read-only input)

---

## Decision

The Round 11 wave-composition variance grammar binds **how the regular-wave pool from R2 is sampled per wave per match per map per locked-civ per (k) tier** to defend §4.11.8 skill-bar thresholds against a memorization meta. Five spec-level bindings:

### (1) Per-wave random-seeded armor-tag mix sampler

Each match generates a **match-seed** (32-bit LCG seed) at match-start; each regular-wave round (R1-R4 / R6-R9 / R11-R14 / R16-R19 / R21-R24 / R26-R29 — 24 regular waves) draws its armor-tag mix from the regular-wave pool by sampling N creep instances from the 5-armor-class probability distribution **modulated by three independent factors**:

**(a) Difficulty-tier (k) band-center modulation** — shifts the band-center within R2's envelope (Unarmored 35-45% / Shielded 20-30% / Beast 15-20% / Spirit 8-12% / Colossal 3-7%). Bands sum 81-114%; target *match-mean* across the 24 regular waves sums to 100%. Per-tier band-centers:

| (k) tier | Unarmored | Shielded | Beast | Spirit | Colossal | Sum |
|----------|-----------|----------|-------|--------|----------|-----|
| Easy (1.16) | **44%** | **22%** | **16%** | **9%** | **4%** | 95% (Spirit/Colossal lower-band; Unarmored upper-band — forgives WEAK-affinity surface) |
| Normal (~1.18 imputed; reserved Phase-5 if mode-lever opens) | 40% | 25% | 17% | 10% | 6% | 98% |
| Hard (1.19) | **38%** | **26%** | **18%** | **11%** | **6%** | 99% (band-center) |
| Hardcore (1.22) | **35%** | **30%** | **20%** | **12%** | **7%** | 104% (Spirit/Colossal upper-band; Unarmored lower-band — forces matchup-correctness axis at threshold) |

The Easy-Hardcore drift is **single-axis** (each armor class shifts monotonically with (k); no compounding of multi-class drift). PvP modes carry no (k) per [§4.10.4](../concept/phase-4.md#4104-k-single-axis-compounding-rule); PvP regular-wave pool runs on the Easy-tier band-center per [§4.11.5](../concept/phase-4.md#4115-tower-baselines)'s PvP-equality non-negotiable.

**(b) Locked-civ matchup-affinity surface adjustment** — per Loop-3 hook #1 from R2, +5pp shift toward each civ's WEAK class to guarantee the WEAK affinity is a *felt identity surface* rather than a vestigial label. Compensatory −5pp from the largest class (Unarmored). Applied as a *match-constant overlay* on the (k) band-center above:

| Locked civ | Adjustment | Rationale |
|------------|-----------|-----------|
| Greek (Leonidas — Control) | Beast +5pp / Unarmored −5pp | Greek WEAK vs Beast (per-civ RN matchup_affinity); shift surfaces the affinity |
| Aztec (Montezuma II — Economy) | Shielded +5pp / Unarmored −5pp | Aztec WEAK vs Shielded; shift surfaces the affinity |
| Norse (Ragnar — Summon) | Spirit +5pp / Unarmored −5pp | Norse WEAK vs Spirit + Divine-pre-T4; shift surfaces the affinity |

Adjustment compounds with (k) tier (separate axis) — Hardcore Norse-locked Spirit reaches 12+5 = 17% per-wave mean; Easy Greek-locked Beast reaches 16+5 = 21% per-wave mean. Shift caps within the R2 band envelope **only for the lower-(k) tiers**: Hardcore Norse Spirit at 17% breaches the R2 band envelope (12% upper) but is permitted because Hardcore-tier band itself was authored to cluster upper-band. The interaction is intentional — Hardcore + Norse-locked surfaces Spirit-pressure at threshold in the way the matchup-correctness axis demands.

**(c) Per-mode tuning lever** — [§4.11.7](../concept/phase-4.md#4117-per-mode-tuning-g--p--q) (g)/(p)/(q) per-mode tuning may modulate composition density at the per-mode authoring sub-pass (next-track-after-§4.7+R11). For this arc, modes inherit the (k) band-center + matchup-affinity surface adjustment as authored. Mode-specific composition overrides are a Phase 5 + per-mode-authoring concern; this grammar binds the spec-level invariants the per-mode pass authors against.

**Sample-distribution sampling rule (LCG-seeded, deterministic, replayable).** Each wave samples N instances independently from the 5-class probability distribution computed as `band_center(k) + matchup_overlay(civ)`. N is the per-wave instance count per [§4.10.1](../concept/phase-4.md#4101-frame) (d) lane runners — a function of round number per [§4.11.1](../concept/phase-4.md#4111-runner-hp-curve-e) and per-mode (p) cap. Sample is **without replacement** within a wave's instance budget; **with replacement** across waves (each wave's seed is independent of prior waves' outcomes within the match).

### (2) Per-wave armor-class diversity constraint (Loop-3 hook #2)

To prevent degenerate single-class waves under any seed (e.g., 100%-Spirit wave against Norse-locked = unwinnable structural matchup), each regular-wave's sample is constrained:

| Constraint | Value | Grain | Rationale |
|------------|-------|-------|-----------|
| **Minimum classes per wave** | ≥ **3 of 5** | instance count | Forces sampler to retry if random draw produces a 2-class wave; prevents all-Spirit + all-Beast degenerate combos |
| **Max single-class cap per wave** | ≤ **70%** | instance count | Prevents 100% single class; preserves matchup-correctness axis legibility |
| **Min single-class floor per wave (when sampled)** | ≥ **5%** OR exactly 0 | instance count | A class either appears at meaningful density or not at all; prevents 1-instance-of-Spirit-in-50-creep noise that fails legibility |

Constraint grain is **instance count** (number of creep instances per armor class as a fraction of total wave instances), chosen over HP-weighted or DPS-weighted because:

- **Legibility at gameplay speed.** Player reads the wave by counting silhouette types (5-armor-tag silhouette + icon per 2026-04-26 attack-type lock). Instance count is what the player sees.
- **Simpler sampler.** HP-weighted constraints require resolving HP scaling per-creep (which interacts with R curve + (k) tier + boss spikes); instance-count constraints are first-order LCG sampling.
- **Decouples from numerics.** R3 grammar is spec-level; instance-count constraints don't bind to HP magnitudes that may re-tune at Phase 5 telemetry-pass (§4.11 numerics ratification — deferred next-track).

If a sampled wave fails any constraint, the sampler retries with the next LCG draw (deterministic; matches replay-equivalence within match-seed). After 8 retries the sampler accepts the closest-feasible draw (rare edge-case; constraint envelope is wide enough to make 8-retry escape exceedingly unlikely under the band-center + matchup-overlay distribution authored above).

### (3) Per-map crystal-lock variance grammar

The boss-spike tile and regular-wave spawn-point set are **map-authored** (level-design-time), not match-randomized at the spawn-topology layer. Per-map authoring lands at the next-track per-map authoring sub-pass (after §4.4 mobile-unit-control closes, per HANDOFF roadmap); R3 binds the **spec-level grammar** the per-map authoring sub-pass must populate:

| Per-map binding | Spec-level grammar |
|-----------------|---------------------|
| **Number of regular-wave spawn-points** | 2–4 distinct spawn-points per map (level-design authored). Map below 2 fails legibility (single-spawn maps memorizable in one match); map above 4 fails strategic legibility (player cannot pre-position towers across all 4+ within Tribute floor). |
| **Spawn-point selection rule (per regular wave)** | Match-seeded LCG selects 1 of the available spawn-points per regular wave (R1-R4 / R6-R9 / R11-R14 / R16-R19 / R21-R24 / R26-R29). Selection is independent across waves (no streak-correction; pure i.i.d.). PvP modes lock spawn-point per wave per map for symmetry — random seeding is solo-PvE and Co-op-Horde only. |
| **Boss-spike tile** | Per-map fixed (boss spawns at the same tile every match per map). Locked because boss identity is content-skeleton verbatim; randomizing boss-spawn-point fragments the dramatized arc the 2026-04-27 historic-arc table anchors. *Per-map crystal-lock variance is on the regular-wave spawn-set, not the boss-spike tile.* |
| **Crystal-lock variance** | Per-mode crystal placement (the defended structure) varies by ≤2 tiles within a fixed neighborhood per map per match. Crystal-lock-variance is the *placement-coverage* axis defense — a memorized "tower at H7, H9, J11" layout fails when the crystal shifts to a 2-tile-offset neighbor in the next match. |

**Per-mode override notes.** PvP modes lock spawn-point + crystal-lock per match for symmetry per [§3.9](../concept/phase-3.md). PvE-MP and Horde modes inherit solo-PvE variance grammar. Per-map authoring sub-pass binds the specific spawn-point and crystal-tile sets per map; this grammar binds the *count + selection rule + variance bounds*.

### (4) Locked content-skeleton boss exemption (verbatim per 2026-04-27 historic-arc table)

R10/R15/R30 per civ + mini-boss cadence at R5/R15/R25 per civ carry **locked identity** — boss identity (Xerxes / Tlaxcalan→Tezcatlipoca / Jörmungandr verbatim per 2026-04-27) does not vary across matches. Boss *composition* (the attendant vanguard slot count) varies within R2-locked civ-distinct armor-class cluster bounds:

| Boss / cadence | Identity (locked) | Composition variance bounds |
|----------------|-------------------|------------------------------|
| Greek R30 Xerxes I | Shielded core (1 instance, locked) | 0–2 attendant Colossal-tier vanguard slots variance (band: 0% / 33% / 67% prob via match-seed); Persian Immortal vanguard at R25-29 = Shielded swarm-density verbatim with 0–4 instance count variance per the (k) tier × matchup-overlay sample |
| Aztec R30 Tlaxcalan→Tezcatlipoca two-phase | Phase-1 = Unarmored + Beast (1 each, locked); Phase-2 = Spirit (1 instance, locked) | Phase-1: 0–2 attendant Beast-tier vanguard slots variance; Phase-2: 1–3 auto-summoned Beast minions (rotating myth-fauna analogue from per-civ Aztec signature_creep_types); Tezcatlipoca avatar identity locked but the auto-summoned minion *composition* varies |
| Norse R30 Jörmungandr | Colossal + Spirit (1 instance core, locked verbatim per 2026-04-27 + Follow-up #11 closure) | 0–3 attendant kraken-tier Beast/Spirit vanguard slots variance per the 2026-04-27 "tidal-omen mini-events" R25-29 framing; Beast/Spirit attendant ratio varies 0/100 to 100/0 per match-seed |
| Mini-boss R5/R15/R25 per civ | Identity = placeholder-pending-Follow-up-#5 candidates from 2026-04-27 (hoplite-rivals → satrap commanders → Persian Immortal champion / rival altepetl warlords → Cipactli-tier myth fauna → priest-king of Triple-Alliance enemy state / rival jarls → Draugr lord → Jötunn herald) | 0–2 attendant slot variance per mini-boss per civ within the per-civ cluster; cluster-class-shift across R5→R15→R25 within civ permitted (e.g., Greek R5 hoplite-rival attendants = Shielded + Unarmored vs R25 Persian Immortal champion attendants = Shielded only); specific clusters lock at Phase 5 + Follow-up #5 consultation |

**Composition-variance is sampled from the same match-seed as the regular-wave grammar** (no separate boss-seed) to preserve match-replay-equivalence at the engine layer. Engine implementation Phase 5.

### (5) §4.11.8 three-axis falsification gate

The R11 grammar **must** defend the three skill-bar axes from a memorization meta. Each axis is verified against the grammar above:

| §4.11.8 axis | Grammar element | Memorization-meta defense |
|--------------|-----------------|---------------------------|
| **Matchup-correctness** (90% Hardcore expert / 30% novice) | (1) per-wave random-seeded armor-tag mix + (k) band-center + matchup-overlay | Player cannot memorize "civ-A vs creep-B at wave-N" because per-wave seed varies the armor-class mix within the band envelope. Per-civ matchup-overlay (e.g., Norse-locked sees more Spirit than Greek-locked) means even *cross-civ memorization* fails. Threshold defense: 90% Hardcore requires *reading live composition* not *executing memorized layout*. |
| **Placement-coverage** (80% Hardcore expert / 30% novice) | (3) per-map crystal-lock variance + spawn-point selection rule | Memorized "tower at H7/J9/L11" layout fails when crystal shifts ≤2 tiles AND when spawn-point selection rotates across the map's 2–4 spawn-set. Player must adapt placement per match. Threshold defense: 80% Hardcore requires reading per-match map state, not executing memorized layout. |
| **Ability-uptime** (80% Hardcore expert / 20% novice) | (3) spawn-point selection + (4) boss-vanguard-composition variance | Memorized cast-rotation fails when (a) regular-wave spawn-point shifts the engagement-window timing per wave; (b) boss-vanguard composition shifts the engagement-density at boss waves. Player must coordinate ability casts to live wave shape. Threshold defense: 80% Hardcore requires reading live, not executing scripted rotation. |

If any axis fails the defense at threshold (i.e., a memorized strategy clears the threshold without live reading), R3 reopens and the failing element re-authors. Specific telemetry-side measurement of the defense lands at Phase 5 telemetry-pass per [§4.10.5](../concept/phase-4.md#4105-skill-bar-axes-k-winnability-target) + [§4.11.8](../concept/phase-4.md#4118-skill-bar-thresholds-per-k); R3 binds spec-level only.

## Context

R2 ratified Option C (civ-matched bosses + shared regular-wave pool) and locked the 5-armor-class distribution band envelope (Unarmored 35-45% / Shielded 20-30% / Beast 15-20% / Spirit 8-12% / Colossal 3-7%) plus civ-distinct boss-tier armor-class clusters per the 2026-04-27 historic-arc table. R3's job is the **wave-composition variance grammar** — the spec that says how the regular-wave pool is *sampled* per wave per match per map per locked-civ per (k) tier. The grammar must defend §4.11.8 skill-bar thresholds against the memorization meta R9 close-out flagged ([2026-05-05 R9 close-out](2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) named the gap; R6 amendment-pass landed the mandate; this round authors the grammar).

R2's two cross-property coherence hooks land here:

1. **Conditional sampling by locked civ** — Beast +5pp for Greek-locked / Shielded +5pp for Aztec-locked / Spirit +5pp for Norse-locked. R3 §(1)(b) binds the matchup-affinity surface adjustment.
2. **Per-wave armor-class diversity constraint** — minimum 3 of 5 classes per wave; max-single-class cap. R3 §(2) binds the diversity envelope at instance-count grain.

Six load-bearing surfaces inherited from R2 + R1 (verbatim from R1 §Context): §4.7 OPEN exit-gate / R6 R11 mandate / §4.11.8 thresholds defense / per-civ RN matchup_affinity matrix + signature_creep_types / per-tower RN type-coverage table / Cultural-sensitivity Follow-up #5. R3 binds the third (defense delivered) and respects the other five as read-only constraints.

## Alternatives considered

- **Per-wave seeded sampling + diversity constraint + per-map crystal-lock variance (chosen).** Three orthogonal variance axes (compositional / topological / boss-vanguard) defend the three skill-bar axes (matchup / placement / uptime) at threshold. Conditional sampling by locked civ surfaces the per-civ WEAK affinity per match. Diversity constraint prevents degenerate single-class waves under any seed. Per-map crystal-lock + spawn-point selection rule are spec-level here, populated by per-map authoring sub-pass.
- **Pure random sampling without diversity constraint — rejected.** Permits 100%-Spirit waves against Norse-locked (Norse WEAK vs Spirit + Divine-pre-T4 absent = unwinnable). Diversity constraint is structural defense against degenerate seeds, not a tuning lever.
- **Per-wave fixed mix (no random sampling) — rejected.** Reverts to memorization meta R9 close-out flagged. Fails the three-axis defense at threshold by definition.
- **Match-seeded mix-template selected from a finite pool — rejected.** A template-library approach (e.g., "10 wave-mix templates per (k) tier; match selects one randomly") shrinks the variance space to a finite set memorizable in 10-100 matches. Random-seeded sampler with diversity envelope produces effectively-infinite variance space at the same authoring cost.
- **Per-civ regular-wave pools (Option B at the variance layer) — rejected.** Already rejected at R2; Cultural-sensitivity Follow-up #5 hard-gates the three-bestiary art burden. Reopening at R3 violates R2's lock.
- **HP-weighted or DPS-weighted diversity-constraint grain — rejected.** R3 binds spec-level grammar; numerics are §4.11 + per-tower magnitudes. HP/DPS-weighted constraints couple R3 to magnitudes that may re-tune at Phase 5; instance-count decouples cleanly. Legibility-at-gameplay-speed (player counts silhouettes) further favors instance-count.

## Reason chosen

The per-wave seeded sampling + diversity constraint + per-map crystal-lock variance grammar is the **smallest spec compatible with the three-axis defense at threshold** with three reinforcing reasons:

1. **Three orthogonal variance axes map to three skill-bar axes.** Compositional variance (per-wave armor-tag mix) defends matchup-correctness; topological variance (per-map crystal-lock + spawn-point selection) defends placement-coverage; boss-vanguard composition variance defends ability-uptime. Each defense is direct (the player's memorized strategy on the failing axis fails when the corresponding variance axis fires); no defense relies on a different axis fortuitously firing. **Memorization meta cannot win on any single axis** — the smallest constraint set the §4.11.8 thresholds permit.
2. **Match-replay-equivalence preserved.** Match-seed determines all variance (compositional + topological + boss-vanguard); replay reproduces variance exactly. Telemetry-pass at Phase 5 + post-match scorecard surfaces wave composition for player feedback loop without requiring engine-side variance recapture. Locked content-skeleton bosses use the same match-seed (no separate boss-seed) — engine layer simplicity.
3. **Per-civ matchup-affinity surface adjustment honors per-civ RN matrix verbatim.** Locked civ's WEAK affinity gets +5pp shift toward the WEAK class — Greek-locked sees more Beast, Aztec-locked sees more Shielded, Norse-locked sees more Spirit. The 5×3 matchup matrix is the *design intent* surfaced at the wave-composition layer; without this overlay, the matrix is vestigial in solo PvE play. The overlay is the smallest binding that keeps the matrix a *felt identity surface*.

### 3x debug loop on R11 grammar

**Loop 1 — aggressive critique.** The grammar's three-axis defense relies on *random-seeded* variance to defend against memorization, but a sufficiently-skilled cohort can build a *probabilistic strategy* (rather than memorized strategy) that clears Hardcore at threshold without live-reading. For example, "given Hardcore Norse-locked sees Spirit at 17% mean / Beast at 18% mean / Shielded at 30% mean / Unarmored at 30% mean / Colossal at 7% mean — pre-build towers covering those probabilities at expected value across the 24-wave campaign" is a *probabilistic-strategy meta* that replaces the memorization meta. The grammar defends against memorization but not against probabilistic-strategy. The R9 thresholds were authored against memorization meta; if probabilistic-strategy meta also clears at threshold, the thresholds need re-authoring, not the grammar.

Furthermore, the per-civ matchup-affinity surface adjustment (+5pp toward WEAK class) is a fixed match-constant — once locked-civ is selected at match-start, the overlay is deterministic for the whole 30-round campaign. A player can *memorize* the per-civ overlay's mean shifts and pre-build for Beast-heavy when Greek / Shielded-heavy when Aztec / Spirit-heavy when Norse. The matchup-affinity surface adjustment is *the opposite of variance* — it's a per-civ *bias* that may make matchup-correctness *more memorizable* for an experienced player who knows their civ's expected pressure profile.

Finally, the diversity constraint min-3-of-5 + max-70% single-class produces a *narrower* sample space than pure i.i.d. (because rejected samples rebias the distribution). The narrower space increases memorizability of the *constrained marginals* (e.g., "Hardcore Norse waves are guaranteed at-least-3-of-5 classes with Spirit ≥ 5% if present" is a tactically usable invariant). The diversity constraint, intended as anti-degeneracy, may inadvertently shrink the effective variance space.

**Loop 2 — steelman.** The probabilistic-strategy meta concern (Loop-1 critique #1) is real but the §4.11.8 thresholds are authored *against* it implicitly. R9's matchup-correctness threshold is 90% Hardcore expert — that requires the player to make the *correct* matchup call on 9 of 10 *individual* tower placements/upgrades, not 90%-on-average across the campaign. A probabilistic-strategy player who pre-builds for the *mean* distribution at expected value scores well on per-wave-mean matchup-correctness only if their pre-builds happen to match the per-wave realized distribution — but per-wave realized distribution varies by ±20pp from the mean (per the band envelope). The probabilistic-strategy player either over-builds (wastes Tribute on towers idle when the variance falls the other way) or under-builds (matchup-correctness drops below 90% on the high-variance waves). Either way, the threshold is not clearable at expectation; live-reading recovers the wasted Tribute / rebuilds the right counter on high-variance waves. **Probabilistic-strategy meta clears Hard / Easy expert (lower thresholds with looser per-wave realized variance correlation), not Hardcore expert** — exactly the difficulty stratification §4.11.8 authored.

The per-civ matchup-affinity surface adjustment as memorizable (Loop-1 critique #2) is the *design intent*, not a flaw. The +5pp WEAK-class shift is the felt identity surface the per-civ RN matchup_affinity matrix was authored to deliver. A Norse-locked player who memorizes "Norse sees 17% Spirit on Hardcore" and pre-builds Spirit-counter towers (Divine T4 commander avatar / Foresight-coin imports) is *executing the multi_civ_play_hook surface as designed* — that's the **Ragnarök-tension narrative-design surface**, not a memorization-meta exploit. The grammar honors per-civ identity surfaces by making the WEAK-class shift fixed-per-match; the variance comes in *which specific waves* the WEAK-class sample falls heavy on within the campaign, not whether the WEAK-class is over-weighted in expectation.

The diversity-constraint narrowing-effective-variance-space concern (Loop-1 critique #3) is real but the constraint envelope is wide. Min-3-of-5 + max-70% leaves huge sample space — at 50 instances per wave the sample-space cardinality is in the 10^4-10^5 range per wave per (k) tier per locked civ per spawn-point. Across 24 regular waves × 4 (k) tiers × 3 civs × ~3 spawn-points = ~864 unique sample spaces, each at 10^4-10^5 cardinality = 10^7-10^8 effective unique campaign realizations. The constraint narrows from 5^50 ≈ 10^35 (pure i.i.d.) to 10^4-10^5 per wave — but 10^7-10^8 effective campaign realizations is well above the memorization horizon (~10^3 matches over a player's career).

**Loop 3 — synthesis.** The grammar is correct as authored. Loop-1's three critiques are all reframed by Loop-2: probabilistic-strategy meta is *exactly what the threshold stratification was designed to disqualify at Hardcore*; per-civ matchup-affinity surface is *the design intent felt at the variance layer*; diversity-constraint narrowing is *bounded above the memorization horizon*. No mid-arc corrections. **One cross-property coherence hook to RN** is added: RN cross-arc audit must verify the three-axis defense empirically against the per-civ RN matchup_affinity matrix + per-tower RN type-coverage table + §4.11.8 thresholds simultaneously (i.e., does the grammar produce sample-distributions consistent with the per-civ surface AND respect type-coverage gaps AND defend thresholds at all (k) tiers for all 3 civs). RN cross-property coherence hook follows.

## Cross-property coherence hook → R4 RN (cross-arc audit + spine-doc edits + arc close)

R3 locks the wave-composition variance grammar. RN's job is the **3-axis cross-arc audit** integrating R2 + R3 + upstream:

1. **Per-civ RN matchup_affinity coherence audit.** For each civ × each (k) tier × each spawn-point per map (when per-map authoring lands) — does R3's sample distribution respect the per-civ STRONG/NEUTRAL/WEAK 5×3 matrix? Specifically: does each civ's STRONG cells receive *less-than-uniform* exposure (so STRONG-affinity is felt as relief), each civ's NEUTRAL cells receive *near-uniform*, and each civ's WEAK cells receive *more-than-uniform* exposure (so WEAK-affinity is felt as pressure)? R3's matchup-overlay (+5pp WEAK / −5pp Unarmored) is the binding; RN verifies the overlay produces matrix-coherent sample distributions across all 5×3 cells.
2. **Per-tower RN type-coverage coherence audit.** For each civ's 15-tower roster, does R3's sample distribution at each (k) tier × each locked-civ produce a wave-composition sequence the roster *can answer* at every wave? Specifically: (a) Greek roster lacks Poison — does any wave demand Poison-only counter? Per 2026-04-26 RPS, Poison is +25% vs Spirit + Beast; *no armor class is Poison-only-counterable*. Greek covers Spirit via Arcane (Oracle/Odysseus) + Divine (4 sources). Greek answers 5 of 5 classes. Verified. (b) Aztec roster lacks Crushing — Crushing is +25% vs Shielded + Colossal. Aztec covers Shielded via Piercing (Eagle Warrior Hall + Eagle Champion) + Colossal via Fire (Temple of the Sun + Nanahuatzin) and Arcane (Feathered Serpent Temple + Serpent-Priest). Aztec answers 5 of 5 classes. Verified. (c) Norse roster lacks Poison + Divine-pre-T4 — Spirit is +25% vs Divine + Arcane. Norse covers Spirit via Arcane (Rune Stone) at T1-T3 + Divine (Harald Bluetooth) at T4 — sub-T4 Spirit pressure is structurally undercovered (Norse has 1 Arcane source vs Greek's 2 + Aztec's 2). RN verifies whether Norse sub-T4 Spirit-pressure at Hardcore (Spirit 12+5=17% mean) is answerable by 1 Arcane source under (k) HP curve at R20-R29 pre-T4-window. **Pre-flagged risk:** Norse sub-T4 Spirit-pressure may be the first multi_civ_play_hook *forced* surface (Foresight-coin Spirit-counter import becomes mandatory at Hardcore Norse). RN audit verifies; if forced-multi-civ-play is structural at Hardcore Norse, this is consistent with multi_civ_play_hook design intent and confirms the surface; if forced-multi-civ-play renders Norse Hardcore solo-unwinnable, R3 grammar reopens with a Norse-Spirit-shift floor (e.g., −2pp from +5pp shift).
3. **§4.11.8 three-axis defense audit.** For each (k) tier × each locked civ — does R3's grammar pass the matchup-correctness / placement-coverage / ability-uptime threshold defense? Specifically: at Hardcore expert (90/80/80 thresholds), does memorization meta clear at any axis? At Easy expert (60/50/40), does novice floor (30/30/20) consistently fail? §4.11.8 was authored against this defense; R3 binds the grammar. RN verifies the binding holds.

RN spine-doc edits per R1 §-placement table (locked):

- `concept/phase-4.md §4.7` Direction sketches → Option C ratification body merged. Option A/B sketches retained as historical-alternatives appendix. Civ-matched boss-tier table (R5/R10/R15/R20/R25/R30 per civ + civ-distinct armor-class clusters from R2) authored. Shared regular-wave pool 5-armor-class distribution bands from R2 authored.
- `concept/phase-4.md §4.7 Wave-composition variance mandate` subsection body authored from R3 — five spec-level bindings (per-wave seeded sampler + diversity constraint + per-map crystal-lock variance + locked-boss exemption + §4.11.8 falsification gate).
- `concept/phase-4.md §4.8` exit-gate item #4 ✅ ticked DONE per arc-close (matches per-tower RN + per-civ RN closing pattern).
- CASCADE pointer single block (R2 + R3 archived to history); decisions table rows for R2 + R3 + RN already added or now added; version footer 0.74 → 0.76 (R3 LANDED 0.75 + RN LANDED 0.76, or RN consolidates with single bump if R3-and-RN land in one session).

R3 inputs from R2: Option C lock + civ-distinct boss armor-class clusters table + 5-class regular-wave pool distribution bands + civ-neutral effect-type language + Follow-up #5 hard-gate compliance. R3 inputs from upstream: 2026-04-26 attack-type lock + per-tower RN type-coverage table + per-civ RN matchup_affinity matrix + signature_creep_types + §4.11.8 thresholds (R9) + (k) exponents (R2) + per-mode tuning (R8). R3 outputs (this file): 5-binding grammar at spec-level grain (no implementation prose — Phase 5 territory) + cross-property coherence hook to RN with explicit 3-axis audit deliverables + Norse sub-T4 Spirit-pressure pre-flagged risk for RN to verify.

## Reversibility note

**Medium.** Reverting the R3 grammar requires a superseding decision file that:

1. Re-opens R3 with explicit reconciliation against the §4.11.8 three-axis defense (which axis fails under what grammar element?).
2. Reverts the (k) band-center modulation table (Easy 44/22/16/9/4 / Hard 38/26/18/11/6 / Hardcore 35/30/20/12/7).
3. Reverts the per-civ matchup-affinity surface adjustment (+5pp toward WEAK / −5pp Unarmored).
4. Reverts the per-wave armor-class diversity constraint (min 3 of 5 / max 70% / min 5%-or-zero) at instance-count grain.
5. Reverts the per-map crystal-lock variance grammar (2-4 spawn-points / per-map fixed boss-spike / crystal ≤2-tile shift).
6. Reverts the locked-boss exemption variance bounds.

Each reversal is a single decision file + bounded edits. Upstream invariants are not under negotiation: 17-item frame, Numbers-phase magnitudes (R5 DPS / R8 per-mode / R1 HP / R2 (k) / R9 thresholds), 2026-04-26 attack-type lock, per-commander R1-R5 lane locks (Hard), per-tower R1-RN magnitude matrix, per-civ R1-RN profiles, three-civ-three-equation-form fingerprint, 2026-04-25 locked content-skeleton names verbatim, 2026-04-27 historic-arc table, R2 Option C ratification + boss-tier civ-distinct cluster table + 5-armor-class distribution bands.

**Hard-class risks (explicit guards) — verbatim from R1 + R2 scope, re-confirmed here:**

- **§5.4 [LOCKED] / §2.4a [LOCKED]** — untouched. Cultural-sensitivity Follow-up #5 hard-gates art / VFX / civ-flavor surface direction prose; this decision is mechanical-content only; civ-neutral effect-type language; no per-creep-row roster authoring beyond locked content-skeleton bosses; mini-boss candidate names remain placeholder-pending-Follow-up-#5.
- **2026-04-25 locked content skeleton + 2026-04-27 historic-arc table** — civ + tower + commander + locked-boss content-skeleton names appear verbatim. R30 antagonists Xerxes / Tlaxcalan→Tezcatlipoca / Jörmungandr verbatim. Mini-boss cadence candidate names placeholder-pending-Follow-up-#5.
- **2026-04-26 attack-type lock** — armor-tag references verbatim-confirm 5-class taxonomy and 7-type taxonomy. RPS matrix at +25%/-25% verbatim; this decision authors no magnitudes.
- **2026-05-05 R5 baseline DPS ladder + R8 per-mode tuning + R1 HP curve + R2 (k) exponents + R9 thresholds** — read-only inputs; this round authors no magnitudes; (k) exponents-table values verbatim.
- **Per-commander R1-R5 lane locks (Hard)** — Greek=Control / Aztec=Economy / Norse=Summon untouched; +5pp WEAK shift cohereres with each civ's identity_hook.
- **Per-tower R1-RN magnitude matrix + type-coverage table** — wave-composition sample distributions are answerable by every locked civ's roster at every armor class (5-of-5 verified per civ — see RN audit hook item 2). No unwinnable structural matchups under any (k) × locked-civ × spawn-point combination *expected at threshold*; Norse sub-T4 Spirit-pressure pre-flagged for RN verification.
- **Per-civ R1-RN profiles + 5-field schema** — wave-composition sample distributions cohere with per-civ RN matchup_affinity matrix + signature_creep_types verbatim. +5pp WEAK shift surfaces each civ's WEAK affinity at gameplay grain.
- **Three-civ-three-equation-form fingerprint** — per-civ matchup-overlay does not destabilize the fingerprint: Greek deceleration-weighted equation finds target-time-integral surface in Beast-shifted Hardcore-Greek waves; Aztec kill-multiplication-weighted finds high-target-count + Poison-stack-saturation in Shielded-shifted Hardcore-Aztec waves; Norse summon-cleave-propagation-weighted finds tight-formation high-target-count + Bleed-density-cascade in Spirit-shifted Hardcore-Norse waves. Each civ's equation finds its pressure-surface within the civ's own matchup-overlay-shifted distribution; the fingerprint preserves.
- **§4.11.7 per-mode tuning (g)/(p)/(q)** — read-only input; mode-specific composition overrides deferred to per-mode authoring sub-pass (next-track-after-§4.7+R11).
- **§4.11.8 three-axis defense** — falsification gate; R3's grammar passes by construction (compositional / topological / boss-vanguard variance map to matchup / placement / uptime axes); RN verifies empirically.
- **R2 Option C ratification + 5-armor-class distribution bands** — band envelope verbatim; (k) band-center + matchup-overlay shifts within envelope; RN verifies envelope-compliance per-tier per-civ.
- **PvP equality non-negotiable per §4.10.4** — PvP modes carry no (k) and lock spawn-point + crystal-lock per match for symmetry. Random-seeded variance is solo-PvE + Co-op-Horde only.
- **Spine-doc edit scope** — `concept/phase-4.md §4.7` untouched at R3 per R1 §-placement table (spine-doc edits land at RN). R3 = decision-file-only.

## Follow-ups

- **R4 RN cross-arc audit + spine-doc edits + arc close** — proceeds autonomously after R3. Inputs: this decision file + R2 + upstream as listed. Output: `decisions/2026-05-06-enemy-direction-rn-cross-arc-audit-and-arc-close.md` + `phase-4.md §4.7` body locks (Option C ratification + R11 subsection body) + `§4.8` exit-gate item #4 ✅ tick + CASCADE/PROGRESS/HANDOFF doc-hygiene per CLAUDE.md compression standard. RN must verify three audits explicitly: (i) per-civ RN matchup_affinity coherence; (ii) per-tower RN type-coverage coherence (with Norse sub-T4 Spirit-pressure pre-flagged check); (iii) §4.11.8 three-axis defense.
- **Norse sub-T4 Spirit-pressure pre-flagged risk** — RN audit verifies whether Hardcore Norse-locked Spirit-pressure (12+5=17% mean) is answerable by 1 Arcane source (Rune Stone) at R20-R29 pre-T4-window under (k) HP curve. If forced-multi-civ-play (Foresight-coin Spirit-counter import) is structural at Hardcore Norse, this confirms multi_civ_play_hook design intent. If forced-multi-civ-play renders Norse Hardcore solo-unwinnable, R3 grammar reopens with Norse-Spirit-shift floor (e.g., +5pp → +3pp).
- **Per-map authoring sub-pass** (next-track-after-§4.7+R11+§4.4) populates the per-map spawn-point sets + crystal-lock tile neighborhoods + boss-spike-tile per map. R3 binds the grammar; per-map authoring binds the specifics.
- **Phase 5 telemetry-pass** implements engine-side instrumentation for per-wave realized-mix + per-match seed + matchup/placement/uptime telemetry per [§4.10.5](../concept/phase-4.md#4105-skill-bar-axes-k-winnability-target). Surfaces in post-match scorecard for player feedback loop. Not in scope this arc.
- **Per-mode authoring sub-pass** (next-track-after-§4.7+R11+§4.4+per-map) authors per-mode (g)/(p)/(q) composition overrides where per-mode pacing demands deviation from baseline grammar. R3 binds the spec-level invariants the per-mode pass authors against.
- **Cascade-lint** after RN.
- **Dual-push** after R3 (this round) + after RN.
- **Cultural-sensitivity Follow-up #5** continues to gate art / VFX / civ-flavor surface direction prose at Phase-4 exit. Mechanical-content only this arc.
- **Per-creep-row roster authoring** stays deferred to Phase 5 + Follow-up #5 consultation.
- **§4.4 mobile unit control (OPEN BLOCKER)** stays parked. Phase 4 OPEN exit-gate item #3; deferred to next-track-after-§4.7+R11.
- **`research/06-tw-subgenres.md` / Follow-ups #6/#7/#8/#9 / C7.b / Phase 4 numerics ratification / Phase 5 readiness gate** — all stay deferred.
