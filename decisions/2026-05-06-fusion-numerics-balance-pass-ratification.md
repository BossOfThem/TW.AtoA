# Decision — Fusion-numerics balance-pass ratification (§4.8 exit-gate item #6 close)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md §4.3`](../concept/phase-4.md) (Fusion system — `[PROPOSAL]` qualifier on "Specific numerics + Divinity balance" flips to LOCKED with citation to this ratification + per-tower R2-R4 + Economy paper-balance), [`concept/phase-4.md §4.8`](../concept/phase-4.md) (exit-gate item #6 ✅ ticked DONE), [`concept/phase-4.md §4.11.5`](../concept/phase-4.md) (God row of DPS ladder — read-only confirm), [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md) (9-recipe lock — read-only), [`decisions/2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md) (2-type inheritance per God — read-only), [`decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md`](2026-05-05-balance-pass-2-round-5-tower-baselines.md) (God = 54×T1 = 1,080 dmg/sec baseline — read-only), [`decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md`](2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) (§4.11.8 Hardcore-expert 0.58× realized — read-only), [`decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md`](2026-05-05-balance-pass-2-round-10-divinity-sources.md) (6-cap + 4-floor + 2-escalation Divinity sources — read-only), [`decisions/2026-05-06-per-tower-r2-greek-roster.md`](2026-05-06-per-tower-r2-greek-roster.md) (Zeus / Athena / Poseidon row authoring — read-only), [`decisions/2026-05-06-per-tower-r3-aztec-roster.md`](2026-05-06-per-tower-r3-aztec-roster.md) (Quetzalcoatl / Huitzilopochtli / Tezcatlipoca row authoring — read-only), [`decisions/2026-05-06-per-tower-r4-norse-roster.md`](2026-05-06-per-tower-r4-norse-roster.md) (Odin / Thor / Tyr row authoring — read-only), [`decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) (45/45 attack-type + status-proc coherence — read-only input), [`decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md) (three-civ-three-equation-form fingerprint Phase-4-spec-level invariant — read-only), [`decisions/2026-05-06-economy-paper-balance-ratification.md`](2026-05-06-economy-paper-balance-ratification.md) (Divinity-cadence-into-Fusion 2 menu + 1/Fusion ratified — read-only).

---

## Decision

Ratify the Fusion-numerics balance-pass close. The per-tower authoring sub-pass (R2-R4, ARC CLOSED 2026-05-06) authored every magnitude row underpinning the 9 locked Fusion-Gods at the God-tier of the locked DPS ladder; the per-civ specialization sub-pass (R2-R4 + RN, ARC CLOSED 2026-05-06) locked the three-civ-three-equation-form fingerprint as a Phase-4-spec-level invariant; the Economy paper-balance ratification (2026-05-06) ratified the Divinity-cadence-into-Fusion (2 menu + 1/Fusion against the locked 6-cap). This decision is a **single-doc cross-coherence audit** verifying that the three locked surfaces compose into a Fusion-as-system that solves cleanly at the spec-level grain; it identifies **no new design surface**, authors **no fresh per-row magnitudes**, and ticks `§4.8` exit-gate item #6 (`Fusion-numerics balance-pass`) DONE.

The audit is single-axis (no per-property arc, no per-civ round queue, no fresh row authoring) because every magnitude is already locked across the three upstream surfaces. Three coherence checks land below: (i) per-God row × locked-Fusion-shape verification across 9 Gods × 4 anchors = 36 cells, (ii) cumulative-team-DPS R30-boss-clear sanity at Hardcore-expert realized multiplier with vs. without 3-fusion-stack contribution, (iii) three-civ fingerprint preservation at God tier across 3 civs × 3 Gods × 5 fingerprint-loci = 45 cells. **Zero cascade-violations across all three checks.**

Phase 4 advances to **9 of 11 exit-gate items closed** (#1 commander one-pagers / #2 per-tower spec / #3 per-civ specialization / #4 enemy direction / #5 mobile unit control / **#6 Fusion-numerics balance-pass** / #7 economy / #8 monetization / #11 cultural-sensitivity gate). 2 items remaining: #9 Engine choice locked (Hard-class fork; deserves 3x debug loop) and #10 Art director engaged or scoped (PM-decisional).

## Context

The Fusion mechanic anchors three load-bearing locks that all converged before this audit:

- **Recipe lock (2026-04-25, Hard).** 9 Gods × 9 locked 2-Demigod recipes × within-civ-only fusion. Names, civs, recipes, and 2-type inheritance are all Hard-class locked content-skeleton; reopen requires PM input.
- **Attack-type inheritance lock (2026-04-26, Medium).** Each God inherits both source Demigods' primary attack types per the 7-type taxonomy (Piercing / Slashing / Crushing / Fire / Poison / Arcane / Divine) × 5-armor RPS matrix.
- **DPS ladder lock (2026-05-05 Numbers-phase #13 R5, Medium).** God-tier baseline = 54× T1 = 1,080 dmg/sec; ±20% per-tower variance band per per-tower R1 scope.

Three downstream sub-passes then bound the row-level + system-level magnitudes:

- **Per-tower R2-R4 (2026-05-06, Medium).** Authored 9 God rows (3 per civ) under the locked 7-field schema (attack_type / cd / range / status_proc / dps / aux_slot_compat / notes). All 9 within ±20% DPS band; all 9 verbatim-confirm 2026-04-26 attack-type pairs; all 9 use locked 2026-04-25 recipe-input names. Per-tower RN audited 45/45 attack-type matches + 45/45 status-proc kind matches + God-tier alternating-per-shot policy verified across all 9 Gods.
- **Per-civ R2-R4 + RN (2026-05-06, Medium).** Locked the three-civ-three-equation-form fingerprint as a Phase-4-spec-level invariant: Greek = deceleration-weighted per-target-time-integral / Aztec = kill-multiplication-weighted per-cast-multiplier × per-kill-bonus / Norse = summon-cleave-propagation-weighted per-summoned-unit-DPS × cleave-radius × Bleed-stack-density. Three structural type-holes (Greek Poison + Slashing-pre-T4 / Aztec Crushing / Norse Poison + Divine-pre-T4) resolve only via cross-civ play; type-holes are not bugs per the 2026-04-25 multi-civ-future commitment.
- **Economy paper-balance ratification (2026-05-06, Medium).** Ratified the Divinity 6-cap × Fusion-spend-cadence: 2 menu-unlock + 1 per Fusion = 5 of 6 Div on a realistic 3-Fusion match; Hard-cap structural with UI indicator on incoming-at-cap. Skipped Fusion-numerics audit explicitly: *"Fusion magnitudes-per-God remain a separate sub-pass; Economy ratifies the Divinity cadence into Fusion (2 menu + 1/Fusion) without authoring God magnitudes themselves."* This audit closes that deferral.

The paper-balance question this audit answers: **do the three load-bearing locks + three sub-passes compose into a Fusion-as-system without contradicting each other or §4.11.8 skill-bar gate?**

## Coherence audit — 3 checks, zero cascade-violations

### Check 1 — Per-God row × locked-Fusion-shape verification (9 × 4 = 36 cells)

Each authored God row (per-tower R2-R4) is verified across four locked anchors: recipe (§4.3 / 2026-04-25), attack-type pair (2026-04-26), DPS within ±20% of 1,080 baseline (2026-05-05 R5), and Divinity-cadence (§4.6 / Economy ratification: 1 Div per Fusion + 2 Div menu unlock).

| God | Recipe (§4.3 / 2026-04-25) | 2-type pair (2026-04-26) | DPS (band 864–1,296) | Div cadence | Verdict |
|-----|---|---|---|---|---|
| **Zeus** | Hercules + Jason ✓ | Crushing + Divine ✓ | 1,100 ✓ (+1.85%) | 1 Div / Fusion ✓ | **PASS** |
| **Athena** | Theseus + Perseus ✓ | Slashing + Divine ✓ | 1,050 ✓ (−2.78%) | 1 Div / Fusion ✓ | **PASS** |
| **Poseidon** | Achilles + Odysseus ✓ | Piercing + Arcane ✓ | 1,080 ✓ (0.00%) | 1 Div / Fusion ✓ | **PASS** |
| **Quetzalcoatl** | Serpent-Priest + High Priest-King ✓ | Arcane + Divine ✓ | 1,100 ✓ (+1.85%) | 1 Div / Fusion ✓ | **PASS** |
| **Huitzilopochtli** | Nanahuatzin + Jaguar Champion ✓ | Fire + Slashing ✓ | 1,200 ✓ (+11.11%) | 1 Div / Fusion ✓ | **PASS** |
| **Tezcatlipoca** | Blood Priest + Eagle Champion ✓ | Poison + Piercing ✓ | 1,080 ✓ (0.00%) | 1 Div / Fusion ✓ | **PASS** |
| **Odin** | Harald Bluetooth + Leif Erikson ✓ | Divine + Piercing ✓ | 1,080 ✓ (0.00%) | 1 Div / Fusion ✓ | **PASS** |
| **Thor** | Björn Ironside + Beowulf ✓ | Slashing + Crushing ✓ | 1,100 ✓ (+1.85%) | 1 Div / Fusion ✓ | **PASS** |
| **Tyr** | Lagertha + Sigurd ✓ | Slashing + Fire ✓ | 1,080 ✓ (0.00%) | 1 Div / Fusion ✓ | **PASS** |

**36 cells / 36 verified.** Zero cascade-violations.

DPS variance: 9 Gods cluster tightly around the 1,080 baseline. Mean = 1,096.7 (+1.55%); range = [1,050, 1,200]; max deviation = Huitzilopochtli +11.11% (Aztec yield-stack archetype calls for sustained-economy-tier pull-up, well within ±20% band per per-tower R1 scope). All other 8 Gods within ±2% of baseline. Greek aggregate = 1,076.7 (deceleration-control archetype; tight to baseline as control-civ value lives in proc shape, not raw DPS). Aztec aggregate = 1,126.7 (yield-stack archetype; pulled up by Huitzilopochtli splash-bleed). Norse aggregate = 1,086.7 (summon-cleave archetype; tight to baseline as Norse value lives in cd-density × cleave-propagation, not raw DPS). Per-civ DPS-aggregate signature is therefore **falsifiable** at the God tier — Aztec > Norse > Greek mean DPS = +5%/+1%/0% above baseline = correct civ-archetype magnitude direction.

dps_split policy across the 2-type pair = **alternating per shot** uniformly across all 9 Gods per per-tower RN row 30 ("God-tier alternating-per-shot follows locked 2-type Fusion model"). This delivers effective 50/50 damage allocation across the 2 attack types per God × per second, preserving the locked "Gods are the only 2-type damage sources" rule from 2026-04-25 ratification at the gameplay-felt grain (RPS computations against incoming armor classes use both types every other shot).

### Check 2 — Cumulative-team-DPS R30-boss-clear sanity (Hardcore-expert realized)

The load-bearing question: do the 3 fused Gods materially contribute to the R30 final boss kill-window in the realistic-expert match composition, or could the player skip Fusion entirely without consequence?

**Realistic Hardcore-expert R30 endgame board composition** (consumes Economy ratification ~10,700 T placement spend + 2 menu + 3-Fusion Divinity spend):

| Tier | Count | Per-tower DPS | Subtotal raw DPS |
|------|-------|---------------|------------------|
| God (Fusion) | 3 | 1,080 | 3,240 |
| T4 Demigod | 3 | 540 | 1,620 |
| T3 elite | 6 | 180 | 1,080 |
| T2 mainline | 6 | 60 | 360 |
| T1 swarm | 4 | 20 | 80 |
| **Cumulative raw** | **22 towers** | — | **6,380 dmg/sec** |

(3+3+6+6+4 = 22 towers; matches §4.11.7 N=24 buildable-hex baseline minus 2 spare cells for cycling/aux.)

**Hardcore-expert realized multiplier** (per §4.11.8 R9 anchor + Economy ratification Check 3):

`0.576 (base survival margin) × 1.20 (Damage Bonus aux (s)) × 1.15 (Commander stack (h)) × 1.25 (RPS matchup-favorable) = 0.993`

`6,380 × 0.993 ≈ 6,335 effective dmg/sec`

**R30 final boss HP** (per §4.11.1 + §4.11.2 + ×5 boss multiplier):

| Difficulty | (k) | R30 std HP | R30 boss HP (×5) | Kill window @ 6,335 effective DPS |
|---|---|---|---|---|
| Easy | 1.16 | 8,585 | 42,925 | 6.78s |
| Hard | 1.19 | 23,737 | 118,685 | 18.74s |
| Hardcore | 1.22 | 65,498 | **327,490** | **51.69s** |

Hardcore expert R30 final boss clears in **~52 seconds** of focused-DPS — squarely inside the structural-boss-fight window for a 30-round-cap tower defense (boss arrival around R30 timer; not a multi-minute war of attrition). **PASS.**

**Counterfactual: no-fusion expert (2 Div banked unspent + 8,800 T sunk into 4× T4 Demigod placement instead of 3× God × 1× T4 mix):**

| Tier | Count | Per-tower DPS | Subtotal raw DPS |
|------|-------|---------------|------------------|
| God (Fusion) | 0 | — | 0 |
| T4 Demigod | 6 | 540 | 3,240 |
| T3 elite | 6 | 180 | 1,080 |
| T2 mainline | 6 | 60 | 360 |
| T1 swarm | 4 | 20 | 80 |
| **Cumulative raw** | **22 towers** | — | **4,760 dmg/sec** |

`4,760 × 0.993 ≈ 4,727 effective dmg/sec` → Hardcore R30 boss clears in `327,490 / 4,727 ≈ 69.3s`.

**Fusion contribution.** With 3 Gods: 51.7s. Without: 69.3s. Fusion delivers a **~25% reduction in R30 final boss kill-time** (or equivalently +33.5% effective boss-burst DPS) at the Hardcore expert margin. This is the load-bearing payoff that justifies the 8,800 T sunk + 3 Div spend into the 3-Fusion path. PASS.

**Floor counterfactual: novice on Hardcore (no Fusion, no Damage Bonus, RPS-neutral, novice multiplier 0.30 × 0.30 × 0.20 = 0.018).** R30 boss kill-time = `327,490 / (4,760 × 0.018) ≈ 3,820 seconds`. Novice on Hardcore is structurally locked out of R30 clear well before reaching it — matches the §4.11.8 "Novice on Hardcore expects to fail before R20 (intended)" lock. PASS.

**Easy expert with 3-Fusion stack:** `42,925 / (6,380 × 0.993) ≈ 6.78s` boss-clear window. Easy clears Fusion-included in well under the boss-fight time-budget; expected. The Fusion payoff at Easy is therefore not boss-clear-DPS but rather *Divinity-economy expression* (the player who routes through Fusion exercises the mythic-ladder identity arc; the player who skips it banks Divinity and clears via aux instead — both paths viable on Easy, only the Fusion path competitive on Hardcore expert).

### Check 3 — Three-civ fingerprint preservation at God tier (3 × 3 × 5 = 45 cells)

The per-civ R2-R4 + RN sub-pass locked three-civ-three-equation-form fingerprint as a Phase-4-spec-level invariant. This check verifies the 9 authored God rows preserve the per-civ fingerprint signal at the peak tier (where mythic-identity weight is heaviest).

Per-civ fingerprints (locked per per-civ RN):

- **Greek = deceleration-weighted per-target-time-integral** (slow / stagger / hex / armor-shred-amplifying-time-on-target / bleed-as-time-integral all express).
- **Aztec = kill-multiplication-weighted per-cast-multiplier × per-kill-bonus** (active-cast-amplifier under Sun Offering / splash / per-stack-toxin / yield-stacking via Blood Tribute all express).
- **Norse = summon-cleave-propagation-weighted per-summoned-unit-DPS × cleave-radius × Bleed-stack-density** (Bleed-density / cleave-splash / Heathen-Army-summon-anchor all express).

Five fingerprint-loci per God × civ:

| Locus | Greek expression | Aztec expression | Norse expression |
|---|---|---|---|
| **L1: status_proc kind** | slow/stagger/hex/armor-shred/bleed-time-integral | active-amplifier/splash/per-stack/per-kill-bonus | bleed-density/cleave/summon-anchor |
| **L2: cd-band signal** | mid-band (control-time sustains zone-denial; no need fast cd) | mid-band (active-window amortization tolerates moderate cd) | fast-band (cleave-density needs swing-frequency) |
| **L3: range-band signal** | long (Greek control wide-area) | mid (Aztec mid-range yield-stack) | short (Norse melee-adjacent summon-cleave) |
| **L4: DPS-aggregate signal** | tight-to-baseline (control value in proc shape) | pulled-up (yield-stack compounding) | tight-to-baseline (value in cd-density × cleave) |
| **L5: notes-prose civ-identity hook verbatim cited** | "Greek sky-father" / "strategic warrior" / "trident + sea-magic" | "feathered-serpent" / "sun-war-god" / "night-trickster obsidian-mirror" | "Allfather" / "hammer-and-axe peak" / "sword-and-sacrifice-fire" |

**Per-God × per-locus expression matrix (3 civs × 3 Gods × 5 loci = 45 cells):**

#### Greek (deceleration-weighted)

| God | L1 status_proc | L2 cd | L3 range | L4 DPS | L5 notes-hook | Verdict |
|---|---|---|---|---|---|---|
| Zeus | stagger −30%/1.5s + smite ✓ (deceleration core) | 2.2s (longest in roster — control-archetype max) ✓ | 5 ✓ (long) | 1,100 (+1.85%) ✓ (tight to baseline) | "Greek sky-father; thunder + judgment" ✓ | **PASS 5/5** |
| Athena | bleed ~7%/3s + smite ✓ (bleed = per-target-time-integral) | 1.4s (mid) ✓ | 4.5 ✓ (long-mid) | 1,050 (−2.78%) ✓ | "strategic warrior + wisdom-blessed" ✓ | **PASS 5/5** |
| Poseidon | armor-shred + hex −35%/3s ✓ (hex = deceleration; armor-shred amplifies time-on-target) | 1.2s (fastest in Greek God set; tradeoff: range maxed at 5.5) ✓ | 5.5 ✓ (longest in entire 45-tower roster) | 1,080 (0.00%) ✓ | "trident + sea-magic; longest range" ✓ | **PASS 5/5** |

**Greek 15/15.** Civ-fingerprint expressed at full coherence across the 3-God set: deceleration-weighted procs / mid-to-long cd / longest range-band / tight-to-baseline DPS / verbatim-civ-identity-hook prose all align.

#### Aztec (kill-multiplication-weighted)

| God | L1 status_proc | L2 cd | L3 range | L4 DPS | L5 notes-hook | Verdict |
|---|---|---|---|---|---|---|
| Quetzalcoatl | hex + smite, both under Sun Offering 4-cell active-window ✓ (active-cast-multiplier × per-kill-bonus) | 1.8s (mid; tolerates active-window amortization) ✓ | 5 ✓ (long-mid) | 1,100 (+1.85%) ✓ | "feathered-serpent + creator-god; cluster inside Sun Offering 4-cell zone" ✓ | **PASS 5/5** |
| Huitzilopochtli | burn DoT + ~30% splash + bleed ✓ (splash = canonical kill-mult; one swing kills many) | 1.2s ✓ (fast for splash density) | 4 ✓ (mid) | 1,200 (+11.11%) ✓ (Aztec yield-stack pull-up) | "sun-war-god; splash + bleed double-compounds inside Sun Offering — peak Aztec sustained-economy God" ✓ | **PASS 5/5** |
| Tezcatlipoca | toxin per-stack ~3%-max-HP × 5 stacks for 5s + armor-shred ✓ (per-stack = stacking-multiplier; armor-shred amplifies post-Sacrifice yield-stack) | 1.4s ✓ (mid) | 4.5 ✓ (mid) | 1,080 (0.00%) ✓ | "night-trickster obsidian-mirror; 5-stack toxin × −2 armor produces peak Beast/Shielded kill-rate" ✓ | **PASS 5/5** |

**Aztec 15/15.** Civ-fingerprint expressed at full coherence: kill-multiplication-weighted procs (active-cast / splash / per-stack) / mid cd / mid range-band / pulled-up DPS aggregate / verbatim-civ-identity-hook prose all align.

#### Norse (summon-cleave-propagation-weighted)

| God | L1 status_proc | L2 cd | L3 range | L4 DPS | L5 notes-hook | Verdict |
|---|---|---|---|---|---|---|
| Odin | smite + armor-shred (anti-Spirit + anti-Shielded boss profile) | 1.4s (fast-mid) ✓ | 4.5 ✓ (Norse longest; still under Greek/Aztec longest-range Gods) | 1,080 (0.00%) ✓ | "Allfather; Gungnir-spear + sky-judgment; non-Bleed God peak — anti-Spirit + anti-Shielded" ✓ | **PASS 4/5 (L1 anti-type-hole-coverage slot)** |
| Thor | bleed + stagger ✓ (Bleed-density core; stagger pins for cleave-window) | 1.0s (Norse fast cd density signal) ✓ | 3.5 ✓ (Norse short-range melee-adjacent) | 1,100 (+1.85%) ✓ | "hammer-and-axe peak; stagger pins targets into summon-cleave zone for Bleed-tick coverage — peak Norse summon-cleave-Bleed God" ✓ | **PASS 5/5** |
| Tyr | bleed + burn + ~30% splash ✓ (Bleed-density × cleave-splash core) | 0.9s (fastest cd in entire 45-tower roster) ✓ | 3.5 ✓ (short) | 1,080 (0.00%) ✓ | "sword-and-sacrifice-fire God; Burn splash spreads burn across cleave-group; Bleed propagates per cleave-swing — peak Norse DoT-density God" ✓ | **PASS 5/5** |

**Norse 14/15.** L1 expressed at 2-of-3 coherence (Thor + Tyr Bleed-cleave core) + 1-of-3 anti-type-hole-coverage slot (Odin Divine-Piercing). The L1 partial-expression is **not a fingerprint violation** — it is the locked **multi_civ_play_hook resolution at peak tier**: Norse has structural type-holes (Poison + Divine-pre-T4 per per-civ R4 Norse profile); Odin's Divine + Piercing inheritance from the locked 2026-04-25 recipe (Harald Bluetooth Divine + Leif Erikson Piercing per per-tower R4) patches the Divine-coverage hole at God tier as an in-civ resolution before the cross-civ-play multi_civ_play_hook engages. L2-L5 all express Norse fingerprint at full coherence (fastest cd-band aggregate / shortest range-band aggregate / tight-to-baseline DPS / verbatim summon-cleave / Bleed-density / DoT-density notes prose). The 14/15 verdict reflects locked-input coherence, not fingerprint drift.

**Aggregate: 44/45 cells = 97.8% civ-fingerprint expression at God tier.** The single non-expression cell (Odin L1) is a *locked-input resolution of a locked-fingerprint-known type-hole* per the 2026-04-25 multi-civ-future commitment, not a cascade violation.

**Cross-civ orthogonality at the 3-aggregate signal level** (the per-civ RN-locked falsifiability test):

| Aggregate signal | Greek | Aztec | Norse | Orthogonality |
|---|---|---|---|---|
| cd-band mean | 1.60s (longest) | 1.47s (mid) | 1.10s (fastest) | ✓ orthogonal |
| range-band mean | 5.00 (longest) | 4.50 (mid) | 3.83 (shortest) | ✓ orthogonal |
| DPS-aggregate signal | +0% (tight) | +5% (pulled-up) | +1% (tight) | ✓ Aztec distinct |
| status_proc-kind primary | deceleration | kill-mult | Bleed-cleave | ✓ orthogonal |

Three-civ fingerprint at the God-tier-aggregate is **falsifiably distinct** along all 4 signal axes. **PASS.**

## Spine-doc edits

§4.3 + §4.8 carry the locked outputs of this audit; no fresh per-row prose is authored (per-tower R2-R4 already carries that). Two edits land:

1. `§4.3` opening italics flip: `"Specific numerics + Divinity balance [PROPOSAL]"` → `"Specific numerics LOCKED 2026-05-06 per Fusion-numerics balance-pass ratification (per-tower R2-R4 + per-civ RN + Economy paper-balance + this audit). Divinity balance LOCKED 2026-05-05 Numbers-phase #13 R10 + 2026-05-06 Economy paper-balance ratification."` Removes the `[PROPOSAL]` qualifier; cites this ratification and the upstream surfaces.
2. `§4.8` exit-gate item #6 flips ✅ DONE with reference to this ratification + the per-tower R2-R4 row chain + per-civ RN fingerprint lock + Economy paper-balance Divinity-cadence chain.

## Cascade discipline check

Hard guards verified untouched verbatim:

- **§5.4 [LOCKED]** — Civilizations row only; this audit binds magnitude composition, not naming. Untouched.
- **§2.4a [LOCKED]** — accessibility floor. Untouched.
- **2026-04-25 locked content skeleton** — 9 Fusion-recipe entries verbatim-cited (Hercules + Jason → Zeus; Theseus + Perseus → Athena; Achilles + Odysseus → Poseidon; Serpent-Priest + High Priest-King → Quetzalcoatl; Nanahuatzin + Jaguar Champion → Huitzilopochtli; Blood Priest + Eagle Champion → Tezcatlipoca; Harald Bluetooth + Leif Erikson → Odin; Björn Ironside + Beowulf → Thor; Lagertha + Sigurd → Tyr). Zero deviation.
- **2026-04-26 attack-type lock** — 9-of-9 2-type pairs verbatim-confirmed against locked taxonomy. Zero deviation.
- **2026-05-05 R5 baseline DPS ladder** — all 9 Gods within ±20% of 1,080 baseline (max deviation Huitzilopochtli +11.11%); ladder magnitudes read-only. Zero deviation.
- **17-item conceptual frame (a)-(r)+(s)** — read-only input. Untouched.
- **All R1-R7 CONCEPT amendment-pass §-anchors** — read-only input. Untouched.
- **Per-commander R1-R5 lane locks (Hard)** — `controlled_by: leonidas` / `economy_target: montezuma_ii` / `summon_anchor: ragnar` per per-tower R2-R4 notes-field tags read-only; cross-civ tag drift would surface here as cascade violation; zero deviation across 9 Gods.
- **Per-tower R1-RN 45-tower magnitude matrix** — 9 God rows read-only input. Zero deviation.
- **Per-civ R1-RN three-civ-three-equation-form fingerprint** — Phase-4-spec-level invariant; this audit confirms preservation at God tier (44/45 expression with locked multi_civ_play_hook resolution at the 1 non-expression cell). Untouched.
- **§4.7 Option C + R11 wave-variance grammar** — read-only input; civ-matched-boss-tier × shared-regular-wave-pool composes with God-tier RPS-favorable matchup multipliers in Check 2 cumulative-DPS realized math. Untouched.
- **§4.6 + §4.6a Economy** — Divinity 6-cap + Fusion-cadence (2 menu + 1/Fusion) read-only; Check 2 builds on Economy ratification's 0.993 ≈ 1.0 closure verbatim. Untouched.
- **§4.10 master-equation variable nomenclature (a)-(r)+(s)** — read-only; multipliers (s) Damage Bonus / (h) Commander stack composed multiplicatively per §4.10.2 with no double-counting. Untouched.
- **§4.11.8 skill-bar thresholds per (k)** — Hardcore-expert 0.576 × 1.20 × 1.15 × 1.25 = 0.993 closure (Economy Check 3) extended to Fusion cumulative-DPS in Check 2. Untouched.
- **Three structural type-holes (Greek Poison + Slashing-pre-T4 / Aztec Crushing / Norse Poison + Divine-pre-T4)** — locked; Norse Odin's L1 anti-type-hole-coverage slot at God tier is the *locked-input resolution* of the Norse Divine-pre-T4 hole, consistent with the 2026-04-25 multi-civ-future commitment. Untouched.

`cascade-lint` to be run post-commit; expected clean (no surface authored, only locked-output citations added to §4.3 + §4.8 ✅ tick).

## Reversibility note

**Medium.** This audit binds no fresh magnitude rows; it ratifies cross-coherence between four already-Medium-or-Hard-locked surfaces (recipe lock Hard / attack-type lock Medium / DPS ladder lock Medium / per-tower row authoring Medium). Reverting requires:

1. Identify which underlying lock to reopen (recipe / attack-type / DPS-ladder / per-tower row authoring / per-civ fingerprint / Economy Divinity-cadence). Each carries its own reversibility class — recipe is Hard, others are Medium.
2. Superseding decision entry against the chosen surface; this audit is automatically invalidated downstream.
3. `§4.3` opening italics + `§4.8` exit-gate item #6 ✅ revert; re-flag `[PROPOSAL]` qualifier on §4.3 numerics line; un-tick exit-gate item #6.
4. CASCADE pointer + decisions-table row + version-footer rollback.

The audit identifies **no new design surface and authors no fresh magnitudes**; it is structurally robust to PM input on any underlying lock without requiring re-audit (the 3-check cross-coherence pattern would re-execute against the new lock).

**Hard-class risks (explicit guards):** none introduced by this audit. All four upstream locks verified untouched verbatim above. No prose strays into visual / VFX / civ-flavor surface direction (Cultural-sensitivity Follow-up #5 hard-gate respected — every proc-magnitude / cd / range / DPS / status-proc reference is mechanical-content language only).

## Follow-ups

- **#9 Engine choice locked** stays open as remaining Phase-4 exit-gate item. Hard-class fork between Godot 4 / Unity / Unreal; deserves dedicated 3x debug loop. Reserved for fresh window.
- **#10 Art director engaged or scoped** stays open as remaining Phase-4 exit-gate item. PM-decisional.
- **Patch-1 commanders + Thor recipe-layer dissonance (2026-04-26 Follow-up #6)** stays parked. Thor's Slashing + Crushing rather than expected Arcane (lightning) + Crushing remains flagged for later recipe-layer reconsideration; this audit does not reopen the 2026-04-25 recipe lock.
- **Cultural-sensitivity Follow-up #5** continues to gate art / VFX / civ-flavor surface direction at Phase-5 sprint pre-art-lock per Cultural-sensitivity Phase-4-exit gate ratification (2026-05-06). This audit is mechanical-content-only and uses civ-neutral effect-type language throughout.
- **Per-mode tuning sub-pass + per-map authoring sub-pass + Phase-5 telemetry pass** stay downstream of Phase-4 exit; not exit-gate items.
- **`research/06-tw-subgenres.md` / `admin/concept.json` migration** — both stay deferred (separate post-arc tracks; `admin/concept.json` retired 2026-05-06 from source-of-truth chain, repository historical artifact only).

## Cross-arc citation manifest

This audit reads all upstream surfaces as locked inputs and cites them by name + date for traceability:

| Lock | Date | Reversibility | Cite |
|---|---|---|---|
| 9-recipe lock + 2-type inheritance per recipe | 2026-04-25 | **Hard** | `decisions/2026-04-25-q2-real-cultures-direction-ratified.md` |
| 7-type taxonomy + RPS armor matrix + status-proc table | 2026-04-26 | Medium | `decisions/2026-04-26-attack-type-mapping.md` |
| God = 54×T1 = 1,080 DPS baseline | 2026-05-05 R5 | Medium | `decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md` |
| §4.11.8 Hardcore-expert 0.576 base survival margin | 2026-05-05 R9 | Medium | `decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md` |
| Divinity 6-cap + 4-floor + 2-escalation sources | 2026-05-05 R10 | Medium | `decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md` |
| 9 God row magnitudes (cd / range / status_proc / dps / aux_slot_compat / notes) | 2026-05-06 | Medium | `decisions/2026-05-06-per-tower-r{2,3,4}-{greek,aztec,norse}-roster.md` |
| Three-civ-three-equation-form fingerprint Phase-4-spec-level invariant | 2026-05-06 | Medium | `decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md` |
| Divinity-cadence-into-Fusion (2 menu + 1/Fusion against 6-cap) | 2026-05-06 | Medium | `decisions/2026-05-06-economy-paper-balance-ratification.md` |
| Cultural-sensitivity Phase-4-exit gate (gate body Hard / execution Easy) | 2026-05-06 | **Hard** for body | `decisions/2026-05-06-cultural-sensitivity-phase-4-exit-gate-ratification.md` |
