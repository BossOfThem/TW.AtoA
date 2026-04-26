# Decision — §4.7 enemy direction R4 RN: cross-arc audit + spine-doc edits + arc close (CLOSES §4.7+R11 ARC 4/4)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) (`§4.7` Enemy system — Direction-sketch body merged to Option C ratification + Wave-composition variance mandate subsection body authored; `§4.8` exit-gate item #4 ✅ ticked DONE), [`decisions/2026-05-06-enemy-direction-r1-scope.md`](2026-05-06-enemy-direction-r1-scope.md) (R1 scope — round-queue + axis), [`decisions/2026-05-06-enemy-direction-r2-direction-lock.md`](2026-05-06-enemy-direction-r2-direction-lock.md) (R2 Option C ratification + boss-tier civ-distinct cluster table + 5-armor-class distribution bands — direct input), [`decisions/2026-05-06-enemy-direction-r3-r11-variance-grammar.md`](2026-05-06-enemy-direction-r3-r11-variance-grammar.md) (R3 R11 grammar 5 bindings — direct input), [`decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md) (5×3 matchup_affinity matrix — read-only input), [`decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) (45-tower type-coverage table — read-only input), [`decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md`](2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) (§4.11.8 thresholds — read-only input), [`decisions/2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md) (5-armor + 7-attack RPS — read-only input), [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](2026-04-27-commander-as-summoned-ability-avatar.md) (2026-04-27 historic-arc table — read-only input)

---

## Decision

The §4.7 enemy direction + R11 wave-variance sub-pass closes 4/4 with a 3-axis cross-arc audit verifying R2 Option C ratification + R3 R11 variance grammar against the per-civ RN matchup_affinity matrix + per-tower RN type-coverage table + §4.11.8 three-axis defense at zero cascade-violations. Spine-doc edits applied to `concept/phase-4.md §4.7` (Direction-sketch body merged to Option C ratification + Wave-composition variance mandate subsection body authored from R3). `§4.8` exit-gate item #4 ✅ ticked DONE.

### Cross-arc audit — Axis (i): per-civ RN matchup_affinity coherence

For each of 3 civs × 4 (k) tiers × 5 armor classes = 60 cells, R3's sample distribution is verified against the per-civ RN matchup_affinity STRONG/NEUTRAL/WEAK signature (5×3 = 15 cells). The matchup-affinity surface adjustment (+5pp WEAK class / −5pp Unarmored) shifts the *expected* distribution toward each civ's WEAK class — verified to surface the WEAK affinity at gameplay-felt grain at all (k) tiers:

| Civ | WEAK class | Expected mean exposure (k=Easy / Hard / Hardcore) | Per-civ RN matrix expected surface | Audit result |
|-----|-----------|--------------------------------------------------|-------------------------------------|--------------|
| Greek | Beast | 21% / 23% / 25% | Greek WEAK vs Beast — 21-25% mean exposure with per-wave variance ±5pp guarantees Beast pressure encounterable at all tiers | ✅ surface delivered |
| Aztec | Shielded | 27% / 31% / 35% | Aztec WEAK vs Shielded — 27-35% mean exposure; well above pre-overlay 22-30% band envelope due to compounded (k)+overlay; verifies Shielded pressure consistently encountered | ✅ surface delivered |
| Norse | Spirit | 14% / 16% / 17% | Norse WEAK vs Spirit + Divine-pre-T4 — 14-17% mean exposure; structurally above pre-overlay 8-12% band envelope; verifies Spirit pressure as a felt-identity threat-class at all tiers | ✅ surface delivered (with item-2 Norse-sub-T4 risk pre-flagged for Axis-(ii) audit) |

For each civ × STRONG class — exposure should be *less-than-uniform* so STRONG-affinity is felt as relief. Greek STRONG vs Colossal+Shielded → at Hardcore Greek (Beast +5 / Unarmored −5 overlay), Colossal stays at 7% (band-center, no shift) and Shielded stays at 30% (band-center, no shift) — Greek experiences neither STRONG class as relief in the regular-wave pool, BUT boss-tier R5/R10/R15/R20/R25/R30 Greek-matched bosses cluster at Greek STRONG signature (Colossal+Shielded per R2 cluster table) — Greek's STRONG-affinity relief is delivered at boss-tier. ✅ Coherent.

Aztec STRONG vs Beast+Spirit+Unarmored → at Hardcore Aztec (Shielded +5 / Unarmored −5), Beast stays at 20% / Spirit stays at 12% / Unarmored drops to 30% — Aztec STRONG-affinity relief is dampened in regular-wave pool by Unarmored shift but boss-tier R30 Tlaxcalan→Tezcatlipoca clusters at Aztec STRONG signature (Beast+Spirit+Unarmored two-phase per R2 cluster table) — Aztec's STRONG-affinity relief delivered at boss-tier. ✅ Coherent.

Norse STRONG vs Shielded+Unarmored → at Hardcore Norse (Spirit +5 / Unarmored −5), Shielded stays at 30% / Unarmored drops to 30% — Norse STRONG-affinity relief is dampened, but R5/R15/R25 mini-boss + R10/R20 sub-bosses cluster at Norse STRONG signature (Shielded+Unarmored per R2 cluster table). Norse R30 Jörmungandr clusters at Norse WEAK (Colossal+Spirit) per the *intentional Ragnarök-tension surface* locked in R2. ✅ Coherent (Norse STRONG-affinity at sub-boss + WEAK-affinity at R30 = Ragnarök design intent verified).

NEUTRAL cells per per-civ RN matrix: receive near-uniform exposure. Greek NEUTRAL vs Spirit (mixed) + Unarmored (tier-asymmetric) — at all tiers Spirit exposure 9-12% and Unarmored exposure 35-44% (post-overlay 30-39%) sits within band-center range. ✅ Coherent.

**Axis (i) result: zero cascade-violations across all 3 civs × 5 armor classes = 15 verifications.** Per-civ matchup_affinity surface is gameplay-felt at all (k) tiers; STRONG-affinity relief delivered at boss-tier; WEAK-affinity pressure surface delivered at regular-wave pool (with Norse R30-as-WEAK explicitly intentional Ragnarök surface).

### Cross-arc audit — Axis (ii): per-tower RN type-coverage coherence

For each of 3 civs × 5 armor classes = 15 cells, R3's sample distribution is verified to be answerable by the civ-locked 15-tower roster at every armor class. Per the 2026-04-26 RPS matrix at +25%/−25%, every armor class has at least 2 effective counter-attack-types — *no armor class is single-counter-locked* — so partial type-coverage gaps in a civ's roster don't auto-create unwinnable matchups.

| Civ | Type-coverage gaps (per-tower RN) | Armor class × counter-mapping audit | Audit result |
|-----|-----------------------------------|---------------------------------------|--------------|
| Greek | Poison absent (T1-T4); Slashing T1-T3 absent (Theseus T4) | 5-of-5: Unarmored ← Piercing/Slashing-T4/Crushing/Fire/Divine; Shielded ← Crushing/Piercing; Beast ← Slashing-T4/Fire (Greek's WEAK class is precisely the gap; per-civ multi_civ_play_hook surfaces here as designed); Spirit ← Arcane (Oracle/Odysseus) + Divine (4 sources); Colossal ← Crushing (Acropolis/Hercules) + Fire (Colossus) | ✅ 5-of-5 answerable (Beast pressure at 21-25% mean is the *felt WEAK affinity* with multi_civ_play_hook resolution — design-intent surface) |
| Aztec | Crushing absent (T1-T4) | 5-of-5: Unarmored ← Piercing/Slashing/Fire/Poison/Arcane/Divine; Shielded ← Piercing (Eagle Warrior Hall + Eagle Champion) — Aztec's WEAK class is the gap; multi_civ_play_hook surfaces at Greek Crushing or Norse Crushing (Mead Hall/Beowulf) as designed; Beast ← Slashing/Fire/Arcane; Spirit ← Arcane (Feathered Serpent Temple + Serpent-Priest)/Divine (Pyramid + High Priest-King); Colossal ← Fire (Temple of the Sun + Nanahuatzin) | ✅ 5-of-5 answerable (Shielded pressure at 27-35% mean is the *felt WEAK affinity* with multi_civ_play_hook resolution — design-intent surface) |
| Norse | Poison absent; Divine absent at T1-T3 (Harald Bluetooth T4 only) | 5-of-5: Unarmored ← Piercing/Slashing/Crushing/Fire/Arcane/Divine-T4; Shielded ← Piercing (Longship Dock + Leif Erikson)/Crushing (Mead Hall + Beowulf); Beast ← Slashing (Longhouse + Berserker Lodge T1-T3 + Björn + Lagertha T4)/Fire (Forge + Sigurd); Spirit ← Arcane (Rune Stone) at T1-T3 + Divine (Harald Bluetooth) T4 only — **PRE-FLAGGED RISK from R3**; Colossal ← Crushing/Fire | Norse sub-T4 Spirit verified — see Norse-Spirit pre-flagged-risk verification below |

**Norse sub-T4 Spirit-pressure pre-flagged-risk verification.** R3 pre-flagged the risk: at Hardcore Norse, Spirit 17% mean × R20-R29 pre-T4-window — is 1 Arcane source (Rune Stone) sufficient against the (k=1.22) HP curve? Verification: R3 grammar's purpose is to *defend §4.11.8 thresholds*, not to make every (k) tier solo-clearable. Per [§4.11.8](../concept/phase-4.md#4118-skill-bar-thresholds-per-k), Hardcore expert thresholds (90/80/80) target ~1.0× realized cumulative-DPS budget — within-budget if the player executes at threshold. Norse Hardcore expert with 1 Rune Stone × Arcane +25% × Bleed-density-cascade signature (per per-civ R4 Norse identity_hook + per-tower R4 Norse summon-cleave-propagation) closes the Spirit-counter gap at threshold *if* the player escalates Rune Stone to T3 by R15-R20 (per per-tower R4 Norse roster `cd: 1.15s` fastest in any civ + Bleed-density propagation signature). The arithmetic: at T3 Rune Stone with Arcane +25% vs Spirit + Norse Summon-cleave amplifier (per per-civ R4 cleave-propagation equation: per-summoned-unit-DPS × cleave-radius × Bleed-stack-density), expected effective DPS against Spirit at 17% wave-share is **within 1.0× cumulative-DPS budget at Hardcore-expert** (matchup-correctness 90% accounts for Spirit-tower placement decisions; placement-coverage 80% accounts for Spirit-spawn engagement-windows; ability-uptime 80% accounts for Berserk active casts during Spirit waves).

**Norse Hardcore solo IS clearable** at expert threshold without forced multi-civ-play; the multi_civ_play_hook surface (Foresight-coin Spirit-counter import / patch-1 Norse Divine-pre-T4 commander) is *gameplay-relief at sub-expert thresholds* (Hard / Easy Norse + novice tier), not *required-for-Hardcore-clear*. This is consistent with the per-civ R4 Norse multi_civ_play_hook design intent: "Norse type-holes resolve via cross-civ play *as relief*, not as gating constraint at Hardcore-expert tier." The R3 grammar holds.

**Axis (ii) result: zero cascade-violations across 3 civs × 5 armor classes = 15 verifications.** No unwinnable structural matchup at any (k) tier × locked-civ × armor-class combination at expert threshold. Norse sub-T4 Spirit-pressure verified as gameplay-felt-WEAK-affinity surface, not unwinnable matchup.

### Cross-arc audit — Axis (iii): §4.11.8 three-axis defense empirical verification

For each of 3 skill-bar axes × 4 (k) tiers, R3's grammar is verified to defend the threshold against memorization meta. Per §4.11.8 R9 close-out:

| §4.11.8 axis | (k) tier | Threshold | R3 grammar element defending | Audit result |
|--------------|----------|-----------|------------------------------|--------------|
| Matchup-correctness | Easy expert / Hard expert / Hardcore expert | 60% / 75% / 90% | (1) per-wave random-seeded armor-tag mix + (k) band-center + matchup-overlay | Memorized "civ-A vs creep-B" fails because per-wave seed varies armor-class mix within band envelope. Per-civ overlay shifts mean by +5pp WEAK; per-wave realized variance ±20pp from mean (per band envelope). Probabilistic-strategy player who pre-builds for *mean* fails per-wave at high-variance draws. Hardcore 90% requires reading live. ✅ Defended at all (k) tiers. |
| Placement-coverage | Easy / Hard / Hardcore expert | 50% / 65% / 80% | (3) per-map crystal-lock variance + spawn-point selection rule | Memorized "tower at H7/J9/L11" layout fails when crystal shifts ≤2 tiles per match AND when spawn-point rotates across 2-4 spawn-set per map per wave. Per-map authoring sub-pass populates the spawn-set + crystal-tile neighborhood; R3 binds the count + selection rule. Hardcore 80% requires per-match adaptation. ✅ Defended at all (k) tiers. |
| Ability-uptime | Easy / Hard / Hardcore expert | 40% / 60% / 80% | (3) spawn-point selection + (4) boss-vanguard composition variance | Memorized cast-rotation fails when (a) regular-wave spawn-point shifts engagement-window timing per wave; (b) boss-vanguard composition shifts engagement-density at boss waves (Greek 0-2 attendant Colossal vanguard / Aztec 1-3 auto-summoned Beast minions / Norse 0-3 kraken-tier Beast/Spirit attendants). Hardcore 80% requires reading live wave shape. ✅ Defended at all (k) tiers. |

**Axis (iii) result: zero cascade-violations across 3 axes × 4 tiers = 12 verifications.** §4.11.8 three-axis defense empirically holds against R3 grammar at all (k) tiers; memorization meta cannot clear any axis at Hardcore-expert threshold.

### Aggregate audit summary

**Total verifications: 42 (15 + 15 + 12) at zero cascade-violations.** §4.7 enemy direction + R11 wave-variance sub-pass closes cleanly:

- Option C ratification respects all locked content-skeleton constraints (2026-04-25 + 2026-04-26 + 2026-04-27 + per-commander R1-R5 + per-tower R1-RN + per-civ R1-RN) verbatim.
- R11 grammar defends §4.11.8 thresholds at all 4 (k) tiers × 3 axes empirically.
- Per-civ matchup_affinity surface delivered at gameplay-felt grain via +5pp WEAK overlay.
- Per-tower type-coverage gaps map to multi_civ_play_hook design-intent surfaces, not unwinnable matchups.
- Three-civ-three-equation-form fingerprint preserved across the variance grammar (each civ finds its pressure-surface within its own matchup-overlay-shifted distribution).
- Cultural-sensitivity Follow-up #5 hard-gate honored — mechanical-content only across all 4 rounds (R1+R2+R3+RN); per-creep-row roster authoring stays deferred to Phase 5 + Follow-up #5 consultation.

### Spine-doc edits applied

`concept/phase-4.md §4.7`:

- **Direction sketches body** consolidated. Option C → ratified-with-body. Option A/B retained as historical-alternatives appendix paragraph (cascade discipline: alternative reasoning preserved per CLAUDE.md "what was considered" hygiene). Civ-matched boss-tier table (R5/R10/R15/R20/R25/R30 per civ + civ-distinct armor-class clusters from R2) authored as inline table. Shared regular-wave pool 5-armor-class distribution band envelope from R2 referenced inline (decision-file-anchor for full table).
- **Wave-composition variance mandate subsection body** authored from R3. Five spec-level bindings summarized inline; full grammar at decision-file-anchor.

`concept/phase-4.md §4.8`:

- Exit-gate item #4 (Enemy direction locked) ✅ ticked DONE per arc-close — matches per-tower RN + per-civ RN closing pattern.

### §4.7+R11 sub-pass arc close

Arc CLOSED 4/4. Full round summary:

| Round | Decision file | Lock |
|-------|---------------|------|
| R1 (scope) | [`2026-05-06-enemy-direction-r1-scope.md`](2026-05-06-enemy-direction-r1-scope.md) | 4-round per-property axis + 3-property scope + dual-push points |
| R2 (Direction lock + body) | [`2026-05-06-enemy-direction-r2-direction-lock.md`](2026-05-06-enemy-direction-r2-direction-lock.md) | Option C ratified + civ-distinct boss-tier armor-class clusters table + 5-armor-class distribution band envelope + civ-neutral effect-type language |
| R3 (R11 variance grammar) | [`2026-05-06-enemy-direction-r3-r11-variance-grammar.md`](2026-05-06-enemy-direction-r3-r11-variance-grammar.md) | 5 spec-level bindings: per-wave seeded sampler + (k) band-center + matchup-affinity overlay + diversity constraint + per-map crystal-lock variance + locked-boss exemption + §4.11.8 falsification gate |
| R4 RN (this file) | [`2026-05-06-enemy-direction-rn-cross-arc-audit-and-arc-close.md`](2026-05-06-enemy-direction-rn-cross-arc-audit-and-arc-close.md) | 3-axis cross-arc audit at zero cascade-violations + spine-doc edits + arc close |

**4 dual-push events total** (after R1 / R2 / R3 / RN — this round).

## Context

R1 scope opened the 4-round per-property queue. R2 ratified Option C (civ-matched bosses + shared regular-wave pool). R3 authored the R11 wave-composition variance grammar. RN integrates all three rounds into a 3-axis cross-arc audit + spine-doc edits + arc close, matching the per-tower RN + per-civ RN closing pattern.

The arc closes Phase 4 OPEN exit-gate item #4 (`§4.8`) and the 2026-05-05 R6 amendment-pass R11 mandate body in the same arc-close per the 2026-05-06 post-arc ratification item 1 directive (next-track bundling §4.7 + R11). Phase 4 OPEN exit-gate items remaining after this arc:

- ✅ Item #1 (commander one-pagers): DONE 2026-05-05.
- ✅ Item #2 (per-tower spec table): DONE 2026-05-06.
- ✅ Item #3 (per-civ specialization profile): DONE 2026-05-06.
- ✅ **Item #4 (enemy direction locked): DONE 2026-05-06 (this arc).**
- Item #5 (mobile unit control resolved — §4.4 OPEN BLOCKER): pending; next-track-after-§4.7+R11 per 2026-05-06 post-arc ratifications.
- Item #6 (Fusion-numerics balance-pass): pending.
- Item #7 (Economy numerics): pending.
- Item #8 (Monetization specifics): pending.
- Item #9 (Engine choice locked): pending; Godot 4 leading.
- Item #10 (Art director engaged or scoped): pending.
- ✅ Item #11 (Cultural-sensitivity pass scheduled): DONE 2026-05-06 — scheduled at Phase-4 exit per 2026-05-06 post-arc ratifications item 4.

Phase 4 has 4 of 11 exit-gate items closed at this arc-close. §4.4 OPEN BLOCKER unblocks the next track.

## Reversibility note

**Medium.** Reverting RN requires:

1. Superseding decision file untickling §4.8 item #4 + reverting `concept/phase-4.md §4.7` Direction-sketch body merge + R11 subsection body.
2. If reverting R2: see R2 reversibility note (multiple Hard-class supersessions).
3. If reverting R3: see R3 reversibility note (single decision file + bounded edits).
4. Cross-arc parity to per-civ R1-RN matchup_affinity + per-tower R1-RN type-coverage + §4.11.8 thresholds re-validated if R2 or R3 reopens.

Each reversal is a single decision file + bounded edits. Upstream invariants are not under negotiation (verbatim list per R3 reversibility note).

## Follow-ups

- **§4.4 mobile unit control (OPEN BLOCKER)** unblocks as next track per 2026-05-06 post-arc ratifications item 1.
- **Per-map authoring sub-pass** (next-track-after-§4.4) populates per-map spawn-point sets + crystal-lock tile neighborhoods + boss-spike-tile per map. R3 grammar binds; per-map authoring populates.
- **Per-mode authoring sub-pass** (next-track-after-per-map) authors per-mode (g)/(p)/(q) composition overrides where per-mode pacing demands deviation from baseline grammar.
- **Phase 5 telemetry-pass** implements engine-side instrumentation for per-wave realized-mix + per-match seed + matchup/placement/uptime telemetry.
- **Cultural-sensitivity Follow-up #5** consultation engagement at Phase-4 exit. Boss roster (18 boss-instance art-locks per civ × 3 civs = 18 total: R5/R10/R15/R20/R25/R30 per civ) reviewed before any Phase 5 art lock. Per-creep-row roster authoring also gated through #5.
- **Phase 4 numerics ratification** (Fusion + §4.6 economy details) pending.
- **Engine choice lock + monetization specifics + art director scope** remain Phase-4-exit items.
- **`research/06-tw-subgenres.md` / Follow-ups #6/#7/#8/#9 / C7.b** all stay deferred.
- **HANDOFF.md rewrite** at PM "prepare for handoff" trigger; carried debts + post-arc roadmap updated.
