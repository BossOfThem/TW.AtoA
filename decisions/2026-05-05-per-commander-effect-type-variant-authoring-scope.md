# Decision — Per-commander effect-type-variant authoring sub-pass: 5-round queue + per-ability-slot axis

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) (`§4.1` per-commander writeups, `§4.11.6` deferred-variant amendment, `§4.8` exit-condition tick), [`concept/phase-3.md §3.2`](../concept/phase-3.md) (locked ability-name table cross-references — read-only)

---

## Decision

Open a **5-round per-commander effect-type-variant authoring sub-pass** to spec the control / summon / economy effect-type variants of the 3 (h) ability slots across the 3 launch commanders (Leonidas / Montezuma II / Ragnar Lothbrok), equivalent-impact to the §4.11.6 damage-floor magnitudes (passive +15% civ-matched / 4 × T3_DPS × 4s burst @ 30s CD / once-per-match instant tier-up signature).

Round structure axis is **per-ability-slot** (Axis B): each authoring round binds one (h) slot across all 3 commanders simultaneously, forcing the equivalent-impact-to-damage-floor constraint to be parity-checked every round on the same slot. Per-commander coherence is owned by the §4.1 commander-one-pager rollup in the closing round.

**Locked ability names from `concept/phase-3.md §3.2` carry forward unchanged** — the names are the surface; this arc binds the *mechanical content* the names describe. §5.4 [LOCKED] is untouched. §2.4a [LOCKED] is untouched. 2026-04-25 locked content skeleton is untouched.

The arc opens immediately. PM autonomy mandate from 2026-05-05 (Numbers-phase Follow-up #13 mid-arc → CONCEPT amendment pass mid-arc) carries forward — surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / handoff trigger / cultural-sensitivity surface (Follow-up #5).

## Context

Three load-bearing surfaces converge on this arc:

1. **`§4.11.6` Commander magnitudes (h)** explicitly defers per-commander effect-type variants: *"Per-commander effect-type variants (Leonidas / Montezuma II / Ragnar Lothbrok control / summon / economy spreads beyond the damage-floor) are deferred to the per-commander authoring sub-pass — only the damage-floor magnitudes above are spec-locked."* This arc is the named owner.
2. **`§4.8` Phase 4 exit condition** lists *"Commander one-pagers complete for all 3 launch commanders (Leonidas / Montezuma II / Ragnar Lothbrok) — passive + short-CD active + long-CD active full specs under the §4.1 identity floor"* as gate item #1. This arc closes that gate.
3. **`§4.1` Commander mechanical spec** carries the identity floor (portrait / silhouette / 12 VO lines / 3-ability kit / civ affinity / 20-level progression / 3 cosmetic slots) but the kit row reads *"all 9 names locked 2026-04-25 — see `concept/phase-3.md §3.2` table"* with no mechanical content. This arc fills that content.

The CONCEPT amendment pass closed the §-anchor gap (variables (a)-(r)+(s) bound; §4.11.6 damage-floor live). Authoring is now downstream of stable spine — the three surfaces above are the spec-floor inputs, not under negotiation.

**Equivalent-impact constraint.** §4.11.6 damage-floor is the calibration target: a non-damage commander (control / summon / economy variant) must achieve match-impact within ±10% of a damage commander against the §4.11.8 skill-bar thresholds at Hard expert (the median calibration point). This is the Phase-4 exit-condition test the arc unblocks.

**Cultural-sensitivity gate (Follow-up #5).** This arc binds *mechanical content* (numbers / cooldowns / effect-type behavior). **Visual content** (silhouette pose / cast animations / VO line direction) remains hard-gated by Follow-up #5 cultural-sensitivity pass. Mechanical-spec writing references the locked ability names verbatim and flags any prose that strays into visual / tonal direction (e.g., "Berserk causes Ragnar to roar like X" is out-of-scope; "Berserk grants the targeted tower +N% attack-speed for Ts on Ms CD" is in-scope).

## Alternatives considered

- **Axis A — per-commander rounds.** One commander per authoring round (R2 Leonidas full kit / R3 Montezuma II full kit / R4 Ragnar full kit / R5 audit + amendment). Cleanest single-commander coherence per round. **Rejected:** locks Leonidas's three slot magnitudes before Montezuma II's variants reveal boundary cases for the equivalent-impact constraint. Cross-commander parity is the load-bearing test (per §4.11.6 deferral language); per-commander axis defers the parity check to R5 audit, where any imbalance surfaces as rework spread across all three commanders.
- **Axis B — per-ability-slot rounds (chosen).** R2 all 3 passives / R3 all 3 short-CD actives / R4 all 3 signatures / R5 audit + §4.1 commander writeups + §4.11.6 amendment. Forces equivalent-impact parity check every round on the same slot.
- **Axis C — per-effect-type rounds.** R2 control variants / R3 summon variants / R4 economy variants / R5 audit. Forces equivalent-impact-by-type discipline most strictly. **Rejected:** presumes commander↔type assignment up-front, which itself is a load-bearing decision (e.g., is Montezuma II a *summon* commander because of "Sun Offering" or an *economy* commander because of "Blood Tribute"? both readings are plausible against the locked names). Axis C compresses the assignment fork into R1 scope, where it would burn the round on a meta-decision before any authoring starts. Axis B keeps the assignment as a first-class authoring decision inside R2-R4 where it can co-evolve with the magnitudes.

## Reason chosen

**Axis B — per-ability-slot rounds.** Three reinforcing reasons:

1. **Equivalent-impact-to-damage-floor is a per-slot test, not a per-commander test.** §4.11.6 binds the damage-floor *per slot*: passive +15% / short-CD 2,880 burst / signature instant tier-up. The non-damage variants must match impact *at the same slot the damage-floor occupies*, against the same §4.11.8 skill-bar threshold. Authoring all 3 commanders' passives in the same round means the parity check runs three-way against the +15% damage benchmark inside one decision file — not across three files where the benchmark restates and drifts.
2. **Commander↔effect-type assignment co-evolves with magnitudes.** The locked ability names hint at type leanings (Leonidas "Spartan Training" reads control; Montezuma II "Blood Tribute" reads economy; Ragnar "Sons of Ragnar" reads summon — but each has alternative readings). Per-slot rounds let assignment emerge from authoring three magnitudes side-by-side, where mis-assignments surface immediately ("if Montezuma II's passive is economy, what's the economy benchmark for +15% damage?"). Per-commander axis (A) locks one commander's full type-spread before testing it against the next commander.
3. **§4.1 commander one-pager rollup is the right closing-round artifact.** R5 audit + §4.1 writeups + §4.11.6 amendment is one coherent integration step: audit the 9 slot specs (3 commanders × 3 slots) for cross-commander balance + equivalent-impact, then roll them into 3 per-commander one-pagers (the §4.8 exit-condition deliverable), then amend §4.11.6 to remove the deferral language. Per-commander axis (A) doesn't have a natural closing artifact distinct from the per-commander rounds themselves; per-effect-type axis (C) has the same closing structure as B but pays the up-front assignment tax.

### 3x debug loop on axis

**Loop 1 — aggressive critique.** Per-ability-slot axis fragments commander identity across three rounds. A reader following the arc round-by-round sees Leonidas's passive in R2, then his short-CD in R3, then his signature in R4 — and only sees the *commander* (the unified kit, the historical character coherence) in the R5 one-pager rollup. That's three rounds of "where's the commander?" before identity emerges. Per-commander axis (A) gives a complete commander per round — readable, shippable, demoable. Furthermore, equivalent-impact parity isn't only a per-slot test: a commander whose passive is weak but whose signature is overwhelming might still achieve match-impact within ±10%, but per-slot authoring would flag the passive as out-of-balance and force re-spec. The constraint per §4.11.6 is "non-damage commander match damage commander match-impact" — match-impact is a *kit-level* metric, not a *slot-level* metric. Axis B optimizes for the wrong granularity.

**Loop 2 — steelman.** Identity coherence (Loop-1 critique #1) is what the §4.1 one-pager rollup *exists* to deliver. The arc isn't shipping commander demos round-by-round; it's authoring magnitudes that get integrated into one-pagers in R5. Reader experience during the arc is "spec authoring in progress" — not "demo each commander." A round-by-round reader who expects narrative coherence is reading the wrong artifact; the per-commander one-pagers (R5 deliverable) are the readable artifact. The match-impact granularity argument (Loop-1 critique #2) is partially true but cuts the wrong way: a kit with three balanced slots achieves balanced match-impact more reliably than a kit with one underpowered slot compensated by one overpowered slot. The latter is technically equivalent-impact-on-average but creates degenerate gameplay (cast the strong slot, ignore the weak one). Per-slot equivalent-impact discipline *prevents* the degenerate compensation pattern that per-kit equivalent-impact would tolerate. Axis B is the stronger constraint, and the stronger constraint is the right one for an authoring sub-pass — looser constraints are recoverable in audit; tighter constraints catch errors in-round.

**Loop 3 — synthesis.** Axis B is correct for *authoring discipline* (per-slot equivalent-impact prevents degenerate compensation; cross-commander parity surfaces in-round) but Loop-1 names a real reader-experience cost (commander identity fragments across rounds) that the R5 rollup mitigates only at the close. Mitigation: each per-slot round (R2-R4) closes with a brief per-commander reading (one paragraph per commander summarizing how the round's slot fits the commander's locked identity name + civ flavor), so identity coherence builds incrementally rather than landing in a single R5 dump. R5 then assembles the three slot-level rounds plus the per-round identity readings into the §4.1 one-pagers as the integration artifact. This combines Axis B's authoring discipline with Axis A's identity-readability across rounds.

**Synthesis-locked output:** Axis B with embedded per-commander identity readings at the close of R2 / R3 / R4. R5 integrates.

## §-placement table (locked)

| Source | Target § | Round |
|--------|----------|-------|
| Passive variant magnitudes (Spartan Training / Blood Tribute / Sons of Ragnar) — control / summon / economy spreads + equivalent-impact-to-+15%-damage benchmark + per-civ affinity hooks | New `decisions/2026-05-05-per-commander-r2-passive-variants.md` (mechanical specs); §4.1 / §4.11.6 untouched until R5 | 2 |
| Short-CD active variant magnitudes (This Is Sparta! / Sun Offering / Berserk) — control / summon / economy spreads + equivalent-impact-to-2,880-burst benchmark + 30s-CD-band discipline | New `decisions/2026-05-05-per-commander-r3-short-cd-variants.md` (mechanical specs); §4.1 / §4.11.6 untouched until R5 | 3 |
| Signature variant magnitudes (The Last Stand / The Great Sacrifice / The Great Heathen Army) — control / summon / economy spreads + equivalent-impact-to-instant-tier-up benchmark + once-per-match discipline + signature-excluded-from-uptime-axis preserved (per §4.10.5) | New `decisions/2026-05-05-per-commander-r4-signature-variants.md` (mechanical specs); §4.1 / §4.11.6 untouched until R5 | 4 |
| Cross-commander balance audit (9-spec parity check + match-impact simulation against §4.11.8 thresholds) + 3 per-commander one-pagers (Leonidas / Montezuma II / Ragnar Lothbrok) + §4.1 mechanical-content rewrite + §4.11.6 deferral-language removal + §4.8 exit-condition tick | `phase-4.md §4.1` rewrite (mechanical-content body) + `§4.11.6` amendment (deferral language removed; cross-link to one-pagers) + `§4.8` checkbox tick + new `decisions/2026-05-05-per-commander-r5-audit-and-onepagers.md` | 5 |

## Round queue (locked)

1. **Round 1 (this file)** — scope decision + axis 3x debug loop + §-placement table + 5-round queue.
2. **Round 2** — passive variant magnitudes across all 3 commanders. Decision file with mechanical specs (effect type per commander + magnitude + duration / range / target-class / per-civ affinity hook + equivalent-impact derivation against +15% damage benchmark). Per-commander identity reading at close.
3. **Round 3** — short-CD active variant magnitudes across all 3 commanders. Decision file with mechanical specs (effect type per commander + magnitude + duration / range / CD-band placement + equivalent-impact derivation against 2,880-burst benchmark). Per-commander identity reading at close.
4. **Round 4** — signature variant magnitudes across all 3 commanders. Decision file with mechanical specs (effect type per commander + magnitude + duration / range / once-per-match resource cost + equivalent-impact derivation against instant-tier-up benchmark + signature-excluded-from-uptime preserved). Per-commander identity reading at close.
5. **Round 5 (CLOSES arc)** — cross-commander balance audit + per-commander one-pager assembly + spine-doc amendments. `phase-4.md §4.1` rewrites the mechanical-content body of the kit row (currently "all 9 names locked 2026-04-25 — see `concept/phase-3.md §3.2` table" → expanded mechanical-content table cross-referencing R2-R4 decision files). `§4.11.6` amendment removes the deferral-language paragraph and cross-links to the one-pagers. `§4.8` exit-condition gate item #1 ticks. CASCADE pointer + decisions table + version footer bump. Dual-push closes arc.

Dual-push points: after Round 3 (carries Rounds 1-3), after Round 5 (carries Rounds 4-5 + closes arc). Cascade-lint after every round.

## Reversibility note

**Medium.** Each round produces a decision file with mechanical specs that bind 3 slots × 3 commanders = 9 magnitude rows; the R5 amendment adds them to `§4.1` and removes deferral language from `§4.11.6`. Reverting requires:

1. Superseding decision entry per round to be reverted (re-opens the slot-level magnitudes).
2. R5 spine-doc edits reverted (re-add deferral language to §4.11.6; re-collapse §4.1 mechanical-content row to the locked-names-only state).
3. §4.8 exit-condition gate item un-ticked (re-opens Phase 4 exit).

Each reversal is a single decision file + bounded edits. The damage-floor magnitudes in §4.11.6 are *not* under negotiation — this arc adds variants alongside, never overwrites. §3.2 locked ability names are *not* under negotiation — this arc binds mechanical content under those names, never re-names.

**Hard-class risks (explicit guards):**

- **§5.4 [LOCKED] / §2.4a [LOCKED]** — every round verifies untouched headers before commit. Cultural-sensitivity Follow-up #5 hard-gates art lock; this arc is mechanical-content only (no visual / VO direction prose).
- **§3.2 locked ability names** — every round verifies the 9 names appear verbatim in the new decision files; any rephrasing is a cascade violation.
- **§4.11.6 damage-floor magnitudes** — the +15% / 2,880 burst / instant tier-up benchmarks are the equivalent-impact calibration target. Variants are authored *alongside* (never *instead of*) the damage-floor; §4.11.6 R5 amendment removes the deferral paragraph but preserves the damage-floor magnitudes verbatim.

## Follow-ups

- **Round 2 onward** runs autonomously per 2026-05-05 PM autonomy mandate (carried from Numbers-phase Follow-up #13 + CONCEPT amendment pass). Surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / cultural-sensitivity surface / handoff trigger.
- **Cascade-lint** after every round.
- **Dual-push** at the two checkpoints (after R3, after R5).
- **Per-civ specialization sub-pass (post-arc track #3)** — intersects this arc at per-civ affinity hooks (e.g., Leonidas's passive interacts with Greek tower civ-tag). The hook *interface* is bound by this arc; the *target-tower-side* spec is owned by the per-tower authoring sub-pass (post-arc track #2). Cross-arc parity guaranteed by both sides referencing §4.11.6 + §4.10.5 anchors.
- **Cultural-sensitivity Follow-up #5** continues to gate art / pose / VO direction. This arc explicitly defers all visual / tonal direction prose to the Follow-up #5 pass; mechanical specs use civ-neutral effect-type language.
- **Foresight-coin (Follow-up #7)** — cross-civ Commander mechanic stays parked. This arc binds within-civ commander↔roster affinity per §4.1 ("Commander plays only their own civ's roster at launch").
- **`research/06-tw-subgenres.md` / `admin/concept.json` migration** — both stay deferred (separate post-arc tracks, unchanged from prior handoff).
