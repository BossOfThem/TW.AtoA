---
**Status:** Draft
**Last reviewed:** 2026-05-05
---

# Phase 4 — Specification

*Detailed system design. This is where the game actually becomes a game.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-3.md](phase-3.md). Next: [phase-5.md](phase-5.md).

---

**Amendment banner — 2026-04-26 real-cultures frame cascade (§4.2 / §4.5 / §4.6 / §4.8 follow-on turn).** Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility Hard), prior cascade turn rewrote §4.1 + §4.3 + §4.7. This turn rewrites **§4.2 (divergence forks under T1→T4 ladder), §4.5 (special effects under real-cultures), §4.6 (economy — Tribute + Divinity per 2026-04-25 ratification), and §4.8 (exit condition)** to the new frame. Attack-type / armor / RPS surfaces reference the 2026-04-26 mapping ([`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md), Reversibility Medium). §2.4a + §5.4 [LOCKED] untouched.

**Amendment banner — 2026-04-27 commander-as-summoned-ability-avatar cascade (§4.1 turn; §4.4a + §4.7 queued).** Per [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](../decisions/2026-04-27-commander-as-summoned-ability-avatar.md) (Accepted; Reversibility Medium; supersedes [`decisions/2026-04-20-commander-on-field-hero.md`](../decisions/2026-04-20-commander-on-field-hero.md)). **This turn lands §4.1 in-match presence model subsection (summoned-on-cast).** Immediate follow-on turns under the same decision: §4.4a NEW (Builder unit class) + §4.4 stale on-field-hero sentence redaction + §4.7 historic-match-arc-beats banner extension (solo-only; round-30 antagonists per civ — Greek Xerxes / Aztec two-phase Tlaxcalan→Tezcatlipoca pre-contact / Norse Jörmungandr-or-Fenrir myth). 8-question PM refinement same-day amendment on the 2026-04-27 decision narrows cultural-sensitivity scope (Cortés OUT of all acts; Aztec framing locked pre-contact). §2.4a + §5.4 [LOCKED] untouched. Locked content-skeleton names from 2026-04-25 ratification untouched.

---

## 4.1 Commander mechanical spec (identity floor [PROPOSAL], per-commander writeup OPEN)

*Decision entries: [2026-04-20 commander identity floor](../decisions/2026-04-20-commander-identity-floor.md) (rebased by [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md), **Superseded by 2026-04-24 reopen**; re-rebase to [2026-04-25 real-cultures ratification](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) tracked as 2026-04-25 Follow-up #10). Floor shape (portrait + silhouette + voice + passive + signature + progression + cosmetic slots) survives the reframing unchanged. Reversibility: Medium.*

The **3 launch commanders** are the legendary historical leaders locked 2026-04-25: **Leonidas** (Greek), **Montezuma II** (Aztec), **Ragnar Lothbrok** (Norse) — one per launch civilization per `concept/phase-3.md §3.2`. Each ships with a minimum identity floor (numbers [PROPOSAL], shape committed):

| Component | [PROPOSAL] floor |
|-----------|------------------|
| Portrait | 1 default + 1 unlockable variant |
| Silhouette skin | 1 default + 1 unlockable variant |
| Voice lines | 12 lines (3 pick / 3 victory / 3 defeat / 3 ability) — routes through §3.10 Voice bus; captioned per §2.4a; period- and culture-appropriate VO direction (subject to cultural-sensitivity pass per 2026-04-25 Follow-up #5) |
| 3-ability kit | 1 passive + 1 short-CD active + 1 long-CD active (all 9 names locked 2026-04-25 — see `concept/phase-3.md §3.2` table) |
| Civilization affinity | Commander plays **only their own civ's roster** at launch (6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods). Cross-civ borrowing parked as future Foresight-coin mechanic. |
| Progression ladder | 20 levels at launch; cosmetic + VO + portrait-frame unlocks paced across. **No gameplay-power gates** (solo-first + no-pay-to-win). |
| Cosmetic slot types | 3: commander skin, portrait frame, map tint. Launch floor = 1 item per slot per commander (default counts as the 1). |

A commander shipped below this floor is "a skin with a stat modifier" — the failure mode §7.4 explicitly calls out.

Each Commander also gets a one-page mechanical writeup before Phase 4 exits, covering:
- Passive + short-CD active + long-CD active full specs (cooldown, duration, effect, visual). Names locked 2026-04-25; all numbers [PROPOSAL].
- Solo campaign storyline (outline only at Phase 4; full script in Phase 5 polish) anchored in the commander's real historical arc + civ's native myth.
- Unlock path for cosmetics and voice lines (by commander level within the 20-level ladder).
- **Cultural-sensitivity review** per 2026-04-25 Follow-up #5 (mandatory gate on content lock; external consultation for Aztec representation, 300-ideology audit for Leonidas, TV-show-vs-history framing for Ragnar).

### In-match presence model — summoned-on-cast (NEW 2026-04-27)

*Decision entry: [`2026-04-27 commander-as-summoned-ability-avatar`](../decisions/2026-04-27-commander-as-summoned-ability-avatar.md) (Accepted; Reversibility Medium; supersedes [`2026-04-20 commander-on-field-hero`](../decisions/2026-04-20-commander-on-field-hero.md)). 8-question PM refinement amendment landed same-day on the 2026-04-27 entry (Aztec pre-contact framing; round-30 antagonists per civ; mixed historicity; myth-mode counterfactual arc; Builder labels working). The per-commander one-page mechanical writeup gates above inherit this subsection's three-surface model. Reversibility: Medium.*

The Commander has **three in-match surfaces and no others.** The board itself shows the Commander **only during a cast window** — between casts, the Commander is not present on the play field. This is load-bearing for tone: Leonidas does not stand around between "This Is Sparta!" invocations; he appears because he was invoked, then the moment ends.

| Surface | Where | Player input | Physical avatar? |
|---------|-------|--------------|------------------|
| **Identity plinth** | HUD frame top-left (portrait + name + level + XP tick) | none — passive display | no — 2D portrait only |
| **Passive effect** | per-tower icon pip on buffed towers (hoverable for tooltip explaining the rule) | none — always on | no — pip sprite only; **board-wide invisible**, not aura-scoped |
| **Active cast** (short-CD / long-CD / signature) | emerges onto board, acts at target, retreats off-board | button / hotkey + click-target | **yes — summoned-on-cast avatar** |

**Three-tier cast animation budget.** Commander emerges for *every active cast* (passive excluded). Tiered durations balance flavor against fatigue:

| Cast class | Duration target [PROPOSAL] | Beats |
|------------|----------------------------|-------|
| Short-CD active | ~1.2s end-to-end | fade-in at target (0.2s) → pose + VO bark (0.6s) → fade-out (0.4s); no path travel |
| Long-CD active | ~2.8s end-to-end | run-in from off-board (0.6s) → cast + full VO line (1.6s) → retreat (0.6s); screen-shake / civ-VFX at peak |
| Signature (long-CD, match-changing) | ~4.5s cinematic | camera nudge → stride to target → cast peak with full VO + VFX + optional historical-event vignette → retreat. **Input non-blocking** (towers fire, enemies advance, player can click) |

**Explicit non-goals** (these were prototype-scope inventions in the now-superseded 2026-04-20 on-field-hero design; none are concept-level intent):

- No movement command. No relocate gesture.
- No aura that lingers on the board (passive is board-wide invisible, signaled by per-tower pips).
- No HP bar. No collision. No knock-back logic.

**Fatigue mitigation.** Short-CD ceiling ~1.2s means even at minimum CD the Commander is on-screen <20% of the time during mashing. Variable VO banks ([PROPOSAL] 6 alts per commander per short-CD class) rotate to prevent line-repetition. **Reduce-motion accessibility toggle** (per §2.4a [LOCKED] floor) collapses short-CD emergence to a non-avatar VFX burst — opt-out path is built in, not patched on.

**Cross-references:**

- **Builder unit class** — see [§4.4a](#44a-builder-unit-class-new-2026-04-27) (queued in immediate follow-on turn). Commander does not place towers; the civ-coded Builder unit (Greek Mason Crew / Aztec Priest-Builder / Norse Thrall Gang — all working labels per Follow-up #5) handles construction. "Priest-Builder" specifically flagged for caste-accuracy review in the cultural-sensitivity pass (macehualtin commoners did Aztec construction, not priests).
- **Historic match-arc beats** — see [§4.7](#47-enemy-system-pve-modes) banner extension (queued in immediate follow-on turn). Commander's historic arc + round-30 antagonist drive solo-mode environmental beats; PvP retains the 2026-04-25 lane-wars shape unchanged. Round-30 antagonists per civ: **Xerxes I** (Greek, named historic) / **two-phase Tlaxcalan war-leader → Tezcatlipoca avatar** (Aztec, pre-contact framing — Cortés explicitly OUT of all acts) / **Jörmungandr** (Norse, myth-overlay — locked 2026-04-27 per Follow-up #11 closure; Fenrir reserved for post-launch PvE/Hero-Mode content). Cross-civ tonal arc escalates mortal → bridge → cosmic — intentional, not asymmetry oversight.

**Cultural-sensitivity inheritance.** Cast-emerge pose (the summoned avatar's silhouette + animation) inherits the [`concept/phase-5.md §5.3`](phase-5.md) silhouette-forward art-direction gate + the 2026-04-25 Follow-up #5 cultural consultation requirement. **No pose lock until the consultation pass closes** — placeholder neutral-abstract silhouettes carry the cast-emerge pipeline through the reshape-plan C7.b prototype step.

**Phase-3 cascade note.** Any prior on-field-hero references in [`concept/phase-3.md §3.2`](phase-3.md) (Commander system framing) and [`§3.4`](phase-3.md) (match loop) are **superseded transitively** by this subsection — no phase-3 amendment turn is owed as long as the §3.2 / §3.4 prose stays at framing level (no specific stale primitives like "aura," "Shift+click move," or "Q signature global empowerment"). If a phase-3 prose review surfaces specific stale primitives, file a banner there as a corollary turn under the same 2026-04-27 decision.

## 4.2 Divergence system

*→ active drill-down: [stage 05 — age evolution](../stages/05-age-evolution.md). **Rescoped OPEN** under the real-cultures 4-tier ladder + Fusion endgame per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) — supersedes the 2026-04-21 3-tier Ash→Altar rescope.*

At tier transitions, the player picks a fork that re-skins the civ's roster expression for the advancing tier and all future tiers of the match. The fork does not change a tower's mechanical role or primary attack type (that's locked per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md)); it changes how that role is expressed visually and secondary mechanically (status-proc intensity, tempo, splash radius, etc.).

Under the T1→T4 ladder there are at most **2 tier-transition forks** per match — at the **T2→T3** and **T3→T4** gates (T1→T2 is the first consolidation and too early for a meaningful fork; the Fusion step is gated by Divinity and locked-recipe selection, not by a fork). New fork pool and per-fork-option themes are **OPEN** — they must:
- Sit inside the civ-coded visual identity (`concept/phase-5.md §5.3` hybrid — stylized vector for T1-T3, silhouette-forward mythic for T4 / Gods).
- Express the mortal-to-mythic escalation (the T4 fork in particular is the "which Demigod face does your civ wear this run" moment).
- Preserve enough combinatorial variety that two matches on the same commander feel different — especially given the locked 6 T4 Demigods per civ and 3 locked Fusion recipes.

**Placeholder shape (not ratified):**
- **T2 → T3 fork:** 3 options, themes OPEN. Candidates (civ-agnostic coloration): martial-lean / ritual-lean / craft-lean.
- **T3 → T4 fork:** 3 options, themes OPEN. Candidates: which pair of the civ's 6 T4 Demigods are *emphasized* this run (affecting which 1–2 Fusion recipes are most reachable) — the fork nudges the Fusion endgame toward a specific God without locking the player out of others.

Run variety ceiling under 2×3=6 paths is narrow; commander-affinity / heirloom / mapmod / enemy-civ-match layering (§4.7 hybrid direction) may reopen breadth. Full fork design is deferred to Phase 4/5 under the real-cultures frame; Fork ratification is a PM-input gate.

## 4.3 Fusion system (signature mechanic)

*→ active drill-down: [stage 06 — hybrids & fusion](../stages/06-hybrids-fusion.md). **Shape locked 2026-04-25** per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md). Specific numerics + Divinity balance [PROPOSAL].*

**Fusion model — within-civ, locked recipes, Divinity-gated (locked 2026-04-25).** The signature mechanic is the **mortal-to-mythic Fusion ladder**: within a civilization, two specific T4 Demigods/Heroes merge via a **locked recipe** into one named God. Each civilization has exactly 3 Gods and 3 recipes. Gods are the **only 2-type damage sources** in the game — they inherit both source Demigods' primary attack types (per [2026-04-26 attack-type mapping](../decisions/2026-04-26-attack-type-mapping.md)).

### Ladder

`T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero → Fusion → God (consumes both source Demigods into one board slot)`

T1 → T2 → T3 promotions happen via **within-civ merge** (merging two same-tier towers of the same civ). T3 → T4 Demigod promotion is **Tribute-unlocked via merge/purchase** (not Divinity-gated). The final Fusion step is **Divinity-gated**: 2 Divinity to unlock the Fusion menu civ-wide, then 1 Divinity per fusion execution. A match earns up to 6 Divinity total (one per mini-boss and main-boss round every 5 waves across 30 rounds), so practical fusion count is 2-3 per match (2 spent on menu-unlock + 3 fusions = 5 of 6 Divinity).

### Locked fusion recipes (9 Gods, 3 per civ)

| Civ | God | Recipe | 2-type damage (from 2026-04-26 mapping) |
|-----|-----|--------|-----------------------------------------|
| Greek | **Zeus** | Hercules + Jason | Crushing + Divine |
| Greek | **Athena** | Theseus + Perseus | Slashing + Divine |
| Greek | **Poseidon** | Achilles + Odysseus | Piercing + Arcane |
| Aztec | **Quetzalcoatl** | Serpent-Priest + High Priest-King | Arcane + Divine |
| Aztec | **Huitzilopochtli** | Nanahuatzin + Jaguar Champion | Fire + Slashing |
| Aztec | **Tezcatlipoca** | Blood Priest + Eagle Champion | Poison + Piercing |
| Norse | **Odin** | Harald Bluetooth + Leif Erikson | Divine + Piercing |
| Norse | **Thor** | Björn Ironside + Beowulf | Slashing + Crushing |
| Norse | **Tyr** | Lagertha + Sigurd | Slashing + Fire |

Names, civs, recipes, and 2-type inheritance are all **locked** — changing any of them requires PM input (escalation trigger from 2026-04-25 ratification). Thor's Slashing+Crushing rather than an expected Arcane+Crushing (lightning) is flagged as 2026-04-26 attack-type Follow-up #6 for later recipe-layer reconsideration; does not reopen this specification.

### Discovery

Prior "hybrid adjacency discovery" blocker is **closed**. Fusion is **menu-driven**, not positional: once the player earns 2 Divinity and has two eligible T4 Demigods on the board, the Fusion menu opens and lists the locked recipe(s) the player qualifies for. No hidden adjacency puzzles, no rote wiki-lookup. The 9 locked recipes are transparent in a codex accessible from the Commander pick screen and from the in-match Fusion menu — discovery is "which recipe do I aim for this match," not "what combines with what."

### Legibility payoff

- Every God reads as "CivA + CivA" — within-civ, no cross-civ surprise fusions at launch.
- The 9 locked recipes are learnable in minutes and restate the civ's pantheon identity.
- 2-type damage via inheritance preserves a simple "each tower has one type; Gods have two" rule.

Cross-civilization fusion is **parked** as the future Foresight-coin mechanic (2026-04-25 Follow-up #7). Post-launch; not in launch scope.

## 4.4 Mobile hero units specification

*→ active drill-down: [stage 04 — in-match core](../stages/04-in-match-core.md). **Contains OPEN BLOCKER** (control model).*

Mobile units need:
- Movement speed per unit tier.
- Pathing mode (patrol, follow lane, direct to waypoint, attack-move).
- Engagement rules (auto-engage, hold, fall back).
- Control complexity: waypoint + mode flags, NOT full RTS per-unit micro.

**OPEN ISSUE:** Exact control model. Full RTS per-unit micro is scope-blowing and wrong genre. Waypoint + mode flags is achievable. Attack-Move command is useful. Must resolve before unit spec work starts.

~~Commander Hero Units (signature ability deployments) have richer control — direct movement + 2–3 abilities + return-to-base. One active Commander Hero per player per match.~~ **Superseded 2026-04-27** by [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](../decisions/2026-04-27-commander-as-summoned-ability-avatar.md) — Commander is no longer a controllable on-field unit; emerges only on cast (see [§4.1 in-match presence model](#in-match-presence-model--summoned-on-cast-new-2026-04-27)). Mobile units in this section refer exclusively to the 15 launch-roster units (5/civ) per [`concept/phase-3.md §3.2`](phase-3.md), not to the Commander.

## 4.4a Builder unit class (NEW 2026-04-27)

*Decision entry: [`2026-04-27 commander-as-summoned-ability-avatar`](../decisions/2026-04-27-commander-as-summoned-ability-avatar.md) (Accepted; Reversibility Medium). Reshape-plan execution surface: [`decisions/2026-04-26-prototype-reshape-plan.md`](../decisions/2026-04-26-prototype-reshape-plan.md) Amendment 2026-04-27 step C7.b. Reversibility: Medium.*

Tower placement is performed by a **Builder unit** dispatched from the home base — not by the Commander, not by an invisible cursor-build. The Builder is a deliberately degenerate mobile-hero subclass: it exists to make construction **legible in time and space** (you see the Mason walk to the cell; the wall isn't free or instant) without inflating the unit-control surface §4.4 already constrains.

**Builder spec (numerics [PROPOSAL], shape committed):**

| Property | [PROPOSAL] |
|----------|------------|
| Visual | Civ-coded silhouette per [`concept/phase-5.md §5.3`](phase-5.md). Working labels (subject to 2026-04-25 Follow-up #5 cultural-sensitivity pass): Greek **Mason Crew** / Aztec **Priest-Builder** *(caste-accuracy flagged — historical Aztec construction was performed by macehualtin commoners, not priests; rename pending consultation)* / Norse **Thrall Gang** *(slavery framing flagged for review)*. |
| Animation | **Single walk loop.** No idle, no combat, no targeting, no animation states beyond walk + despawn-on-arrive. |
| Spawn | From home-base anchor on player issuing a build/upgrade order. |
| Despawn | On arrival at the build cell — the tower assembles in-place; the Builder vanishes (cloud-puff or civ-coded VFX). |
| AI | **None.** Pathfinder follows the walkable-build-grid only. No engagement rules, no fallback, no auto-retreat under threat. If the build cell becomes unreachable mid-walk, the Builder dies silently and the order auto-cancels at the 90% refund tier. |
| Combat | **None.** Builders cannot attack, be targeted by single-target enemy AI, or block path. They are visually present but mechanically inert. |
| Concurrency cap | **3 simultaneous Builders per player.** Issuing a 4th order queues until a slot frees. |
| Cancel refund | **90% of the Tribute cost** if the player cancels mid-walk (before despawn-on-arrive). 100% if cancelled in the same tick as the order. After despawn, refund is the normal tower-sell rate (§4.6). |
| **Walkable-build-grid** | **Distinct from the enemy-path-grid.** Builders cross terrain enemies cannot (and vice versa) — supports buildable platforms over enemy-only chokes, water tiles enemies path through but Builders bridge, etc. The two grids are authored side-by-side per map; mismatches are a §5.6 lint rule. |

**Why a Builder unit (load-bearing rationale).** Three threads converge:

1. **Commander-as-summoned-ability-avatar** (§4.1) explicitly removes the Commander from the field except during a cast window. *Something* has to physically construct towers if the genre's "build a thing on a cell" verb stays grounded — a free instant placement reads as cursor-magic and undoes the §3.10 mortal-to-mythic identity arc.
2. **Civ-coded labor** is the cheapest legible-civ payoff in the build phase: seeing a Mason vs a Priest-Builder vs a Thrall walk is faster pattern-recognition than any tower-skin diff.
3. **Sniping / harassment surface.** Builders walking the map create a small attention sink that lane-pressure / sending-creeps PvP modes (§4.6 Mythium) can target — without exposing the Commander to harassment risk.

**Explicit non-goals** (these would re-create the on-field-hero surface §4.1 just removed):

- No combat capability — ever, even as a "self-defense bite."
- No multi-state animation beyond walk + despawn.
- No player-issued waypoint or attack-move commands. Builders go to the build cell. That is all.
- No XP, no levels, no progression — Builders are infrastructure, not content.

**Cross-references:**

- §4.1 in-match presence model — Commander does not place towers; the Builder does.
- §4.4 mobile hero units — Builders are explicitly **out of scope** for the §4.4 control-model question (which addresses the 15 combat-capable launch units).
- [`concept/phase-2.md §2.4a`](phase-2.md) [LOCKED] — reduce-motion accessibility toggle: when active, Builder walk collapses to a 0.3s teleport-fade (preserving the time-cost legibility while removing the motion).
- 2026-04-25 Follow-up #5 cultural-sensitivity pass — all three working labels (Mason Crew / Priest-Builder / Thrall Gang) gate on that pass; rename allowed pre-content-lock.

## 4.5 Special effect units specification

Special effect units are limited in placement count per match to avoid spam. Examples:
- Timed zones (debuff aura for 20 seconds).
- Consumables (one-shot damage bursts, healing pulses).
- Terrain modifiers (e.g., a tar pit or consecrated ground that expires at the next tier gate — per-civ allocation is Phase 5 spec).

Each special effect has a cooldown, a cost (Tribute for tactical effects, Divinity for mythic-tier effects that read as one-shot "prayer" moments — final currency split deferred to §4.6), and a visible indicator on the map. Status-effect procs (Burn, Bleed, Toxin, Hex, Smite, Armor-shred, Stagger) are **not** special-effect units — they're driven by the source tower's primary attack type per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md). Specification per-item is a Phase 5 task; Phase 4 locks the *framework* only. Cultural-sensitivity pass (2026-04-25 Follow-up #5) applies to any special-effect visual tied to a civ's religious iconography (especially Aztec ritual effects).

## 4.6 Economy specification

*→ active drill-down: [stage 03 — match setup](../stages/03-match-setup.md), [stage 04 — in-match core](../stages/04-in-match-core.md). **Two-currency shape locked 2026-04-25** per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md). Magnitudes locked 2026-05-05 Numbers-phase #13 Rounds 3 + 7 + 10; bound to [§4.11](#411-numbers-floor) (curves) + [§4.6a](#46a-auxiliary-economy) (aux spend). Reversibility: Medium.*

Prior three-lineage-aligned currency mapping (Gold / Faith / Cinders from Nature / Prayer / Ash) is **superseded** — the lineages that backed it don't exist under the real-cultures frame. The 2026-04-25 ratification + 2026-05-05 magnitudes lock a **two-currency economy** anchored to the 30-round match cap, the Fusion endgame, and the [§4.6a](#46a-auxiliary-economy) auxiliary surface.

### Tribute (primary; kill-driven, k-invariant)

Generated by enemy kills + boss-round lump rewards. Per-runner yield: `yield(R) = 5 · 1.10^R` (anchors per [§4.11.3](#4113-tribute-economy-a)). Boss lumps: R10 = 250 T, R15 = 400 T, R30 = 1,500 T. Cumulative Easy R1→R30 income: ~25,000 T.

Spent on tower placement (T1 = 100 T), tier-up merges (T2 = 300 T, T3 = 900 T, T4 promote = 2,500 T) per [§4.11.5](#4115-tower-dps-ladder-c--tier-up-costs); send-creeps / call-for-help / Maze Stones per [§4.6a](#46a-auxiliary-economy). Sell-refund schedule per [§4.10.6](#4106-sell-refund-schedule-locked-2026-05-04). On-curve Easy spend ~10,700 T → ~14,300 T headroom for aux + cycling.

**No time-income.** Tribute generation is kill-only — there is no worker / passive-tick income. This applies in **every mode including PvP** (the Legion-TD-2 worker pattern is retired; see Mythium-retirement note below).

### Divinity (mythic; 6-cap, hard)

Earned across **6 sources** (4 floor + 2 escalation, locked 2026-05-05 R10):

| # | Source | Yield | Trigger |
|---|---|---|---|
| 1 | R10 Boss drop | +1 Div | Clear R10 boss |
| 2 | R15 Elite drop | +1 Div | Clear R15 elite |
| 3 | R30 Final Boss drop | +1 Div | Clear R30 boss |
| 4 | Match-completion bonus | +1 Div | Survive to R30 (any leak count) |
| 5 | Perfect-Wave Bonus | +1 Div per perfect boss (cap +3 Div / match) | Clear R10 / R15 / R30 boss with **zero leak** |
| 6 | First-Hybrid Construction | +1 Div one-shot | First true cross-civ hybrid built per locked adjacency topology, per side / per team |

Theoretical ceiling: 4 floor + 3 perfect-wave + 1 first-hybrid = **8 Div**. Realistic expert: **5–6 Div**. Hard 6-cap (banking past 6 wastes; UI indicator on incoming Div if at cap).

PvP: Sources 1–4 award **per side**, Sources 5–6 award **per side** (PvP) or **shared-team** (co-op). Skill-bar (Round 9 thresholds per [§4.11.8](#4118-skill-bar-thresholds-per-k)) hard-gates the escalation sources — novice stacks cannot accidentally reach the ceiling.

**Spent on:** Fusion endgame (1 Div per Fusion execution; 2 Div one-shot menu-unlock per match; 9 locked recipes per [§4.3](#43-fusion-system-signature-mechanic)) and the aux-slot catalog per [§4.6a](#46a-auxiliary-economy). Realistic match outcome: 2 menu-unlock + 3 Fusions + 1 aux Damage Bonus = 6 of 6 Div spent; expert Perfect-Wave + First-Hybrid surplus opens room for a second aux slot.

### Mythium retirement (2026-05-05)

The Mythium "time-based PvP-only worker income" placeholder is **superseded**. Round 3 of Numbers-phase #13 ratified Tribute as a **kill-only currency across every mode including PvP**, and Round 7 ratified the Universal aux slot pricing (Tribute or Divinity). Mythium does not exist in any launch mode. The Squadron-TD send-volume pattern is preserved for PvP-IW Send-for-Interest (1 Div unlock + 150 T/send + +3 T/round recurring per [§4.11.7](#4117-per-mode-tuning-g--p--q)) — same shape, different currency.

**Open:** late-game Tribute sinks past R25 (currently §4.6a aux catalog absorbs cycling; per-mode sub-pass may identify additional sinks); enhanced status-proc tiers as Tribute-purchasable upgrades stay [PROPOSAL] for per-tower authoring; "Divinity" name is descriptive — §5.4 + 2026-04-25 Follow-up #5 cultural-sensitivity pass applies.

## 4.6a Auxiliary economy

*Decision entries: [`2026-05-05 R7 aux costs + (s) ranges`](../decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) + [`R8 per-mode tuning`](../decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) + [`R10 Divinity sources`](../decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md) (all Accepted; Reversibility Medium). Forward-anchored from [§4.10.1 (s)](#4101-variable-nomenclature-locked-2026-05-04-extension-2026-05-04-r12) + [§4.10.7](#4107-tower-target-priority-locked-2026-05-04). Reversibility: Medium.*

The auxiliary economy is the universal-aux-slot surface — every mode draws from a shared catalog of 6 spendable slots, each priced in either Tribute or Divinity. This is the consolidated home for the (s) global multiplier extension to the conceptual frame and for the Send-Creeps / Call-for-Help / Maze-Stone tactical levers across modes.

### Universal aux-slot catalog

| Slot | Cost | Effect | Cap | Mode availability |
|---|---|---|---|---|
| **Damage Bonus** (s = 1.20) | 1 Divinity | (s) = 1.20 global multiplicative on damage equation per [§4.10.2](#4102-master-damage-equation) | 1 active / match | All modes |
| **Economy Bonus** | 1 Divinity | +25% per-kill Tribute on `yield(R)` curve (boss lumps unchanged) | 1 active / match | All modes |
| **Tower-count expansion** | 1 Divinity per tier | +2 N (buildable hexes) per Div spent; cap 3 Div → +6 N (e.g., N = 24 → 30) | 3 Div / match | All modes |
| **Send-Creeps** (mode-variant) | 100 Tribute baseline | Mode-variant payload + reward shape per [§4.11.7](#4117-per-mode-tuning-g--p--q) | per-send (no cap on send volume) | Solo / PvE-MP / Horde / PvP-Maze |
| **Send-for-Interest** (PvP-IW only) | 1 Div unlock + 150 T/send | +3 T/round recurring; opponent kill yields refund | 1 unlock / match, unlimited sends after | PvP-IW only |
| **Call-for-Help** | 300 Tribute | One-shot summon support unit | 1 / match | All modes |
| **Maze Stone** | 25 Tribute (+75 T → upgradeable to T1 = 100 T parity) | Pathing blocker on hex grid | per-stone (no cap on count) | PvP-Maze only |

### Currency-budget audit (locked 2026-05-05 R7)

Max-aux+1-Fusion = 1+1+3+1 = **5 Div** ✓ vs 6-cap; Max-Fusion (3) + menu (2) = **5 Div** ✓ (no aux). Combined per-tower expert stack: 1.20 (s) × 1.15 ([h](#4116-commander-magnitudes-h)) × 1.25 (matchup) = **1.725× pre-(i)/(q)**, anchoring [§4.11.8](#4118-skill-bar-thresholds-per-k) Hardcore-expert realized math (0.576 × 1.725 ≈ 1.0× realized). Tribute headroom: ~14,300 T baseline drops to ~12,400 T at Co-op/Maze-typical aux-spend — healthy cycling preserved. PvP-IW Send-for-Interest feasibility: 1 Div unlock + 1 Div Damage Bonus = 2 Div vs 4-Div floor → fits pre-escalation.

**Mode-optimization** (which slots a given mode prefers — e.g., Horde-B Tower-count vs PvP-IW Send-for-Interest rush) is deferred to the per-mode authoring sub-pass; cross-link to [§4.11.7](#4117-per-mode-tuning-g--p--q) for tuning rules.

## 4.7 Enemy system (PvE modes)

**Rescoped OPEN** under the 2026-04-25 real-cultures frame per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) — prior Ash→Altar dungeon-cosmology framing ("residue of the descent, things sealed in Ash, dormant under Nature, forbidden by Prayer") is **superseded**. Attack-type / armor-tag constraints are **locked** per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md); the enemy archetype roster populating those constraints is **OPEN**.

### Locked constraints (from 2026-04-26 attack-type mapping)

Every enemy archetype must carry **1–2 armor tags** from the 5-tag taxonomy:

| Tag | Intended archetype family |
|-----|---------------------------|
| **Unarmored** | Common swarm, light infantry, civilians, lesser monsters |
| **Shielded** | Heavy infantry, armored elites, armored mini-bosses |
| **Beast** | Myth monsters, wildlife, feral PvE |
| **Spirit** | Undead, ethereal, magic-born |
| **Colossal** | Giants, titans, huge bosses |

Rock-paper-scissors matrix (attack type × armor tag at +25% / −25%) is locked per 2026-04-26 mapping. Enemy design must make armor tags **read at gameplay speed** (icon + silhouette cue).

### Direction sketches under real-cultures frame (themes OPEN)

- **A — Cross-cultural myth creatures (shared PvE pool).** A unified bestiary drawing from Greek / Aztec / Norse myth — Minotaurs, Hydra, Cyclops, Jaguar-spirits, Cihuateteo, Draugr, Jötnar, Trolls, serpents, etc. Assigned to armor tags per archetype (e.g., Draugr = Spirit + Shielded; Jötunn = Colossal + Shielded; Hydra = Beast + Colossal). Easier to build one shared PvE pool; thematically legible across all 3 civs.
- **B — Civ-matched native-myth creatures (per-civ PvE pools).** Greek PvE faces Greek myth antagonists (Minotaur, Hydra, Medusa, Titans); Aztec faces Aztec myth (Cipactli, Cihuateteo, Tzitzimimeh); Norse faces Norse myth (Jötnar, Draugr, Fenrir, Midgard Serpent). Thematically richer; three times the art burden; harder matchmaking in co-op Horde if players pick different civs.
- **C — Hybrid (leading placeholder).** Civ-matched **boss-tier** enemies (mini-boss every 5 rounds + main-boss every 10 rounds — aligns with the 30-round match arc + 6-Divinity cap from 2026-04-25 ratification). Regular-wave enemies drawn from a shared cross-cultural pool. Trailer moments without tripling the art burden.

**Leading direction (placeholder, not ratified): Option C — hybrid.** Civ-matched bosses at 5/10/15/20/25/30, shared regular-wave pool between.

### Blockers before Phase 5 begins

1. **Direction A / B / C ratification** (PM input required).
2. **Boss roster locked** — 2026-04-25 Follow-up #3, requires PM-ratified myth-creature list per civ once direction lands.
3. **Regular-wave archetype roster + armor-tag assignments** (populates the 5 armor tags at waves 1–29).
4. **Cultural-sensitivity pass** — boss names drawn from myth must pass the 2026-04-25 Follow-up #5 review before any Phase 5 art lock (especially Aztec creatures, which carry the highest representational risk).
5. **PvE campaign scope** — the deferred AGES concept (PvE campaign + leveling + attributes per 2026-04-25 Follow-up #8) may reopen this decision by introducing per-chapter enemy-direction overrides.

Full enemy roster and per-wave archetype list deferred to Phase 5 under the §5.3 silhouette-forward aesthetic **and** the 2026-04-26 armor-tag legibility constraint. Decision required before Phase 5 begins.

### Historic match-arc beats (solo-only) — NEW 2026-04-27

*Decision entry: [`2026-04-27 commander-as-summoned-ability-avatar`](../decisions/2026-04-27-commander-as-summoned-ability-avatar.md) (Accepted; Reversibility Medium). Same-day amendment captures 8-question PM refinement. Follow-up #11 (Norse round-30 antagonist) **closed 2026-04-27** — Jörmungandr locked. Reversibility: Medium.*

The 30-round match arc (mini-bosses at 5/15/25, main bosses at 10/20/30) is **dramatized in solo modes** as the commander's compressed historic-and-mythic narrative. PvP retains the 2026-04-25 lane-wars shape unchanged — historic beats are environmental flavor (banner art, music cues, boss skin), not mechanical asymmetry between modes.

**Cross-civ tonal escalation** (intentional, not oversight): every civ traverses *mortal → bridge → mythic* across the 30 rounds, but each civ's round-30 antagonist sits at a different tier of that arc — by design, so each commander's run feels distinct rather than three reskins of one beat:

| Civ | Commander | Round-30 antagonist | Historicity tier | Art / cinematic note |
|-----|-----------|---------------------|------------------|----------------------|
| Greek | Leonidas | **Xerxes I** | Named historic figure (Persian Wars / Thermopylae 480 BCE) | Mortal scale. Persian Immortal vanguard at rounds 25-29; Xerxes himself emerges at 30. Ties Leonidas's identity to his actual recorded enemy. |
| Aztec | Montezuma II | **Tlaxcalan war-leader → Tezcatlipoca avatar (two-phase boss)** | Pre-contact framing. **Cortés explicitly OUT of all acts** per 2026-04-27 same-day amendment | Phase 1 (rounds 28-29 lead-in + round-30 phase 1): mortal Tlaxcalan antagonist (Aztec-Tlaxcalan rivalry was a real pre-Columbian conflict). Phase 2 (round-30 phase 2 + post-clear cinematic): the Tlaxcalan reveals as a Tezcatlipoca (Smoking Mirror) avatar, escalating to mythic. Mortal-to-mythic in a single round. |
| Norse | Ragnar Lothbrok | **Jörmungandr (the World-Serpent)** | Pure myth (Eddic; Ragnarök foreshadow). Locked 2026-04-27 per Follow-up #11 closure | Cosmic scale. Sea-emergence pageant: rounds 25-29 deliver tidal-omen mini-events (kraken-tier Beast+Spirit minions), round-30 Jörmungandr breaches the lane as a Colossal+Spirit boss. Fenrir reserved for post-launch PvE / Hero-Mode content per Follow-up #11 closure rationale. |

**Mini-boss cadence (rounds 5/15/25; same per-civ pool, lighter framing).** Mini-bosses pull from the same civ's myth/history pool as the round-30 boss but at one tier below in scale: Greek 5/15/25 candidates include hoplite-rivals → satrap commanders → Persian Immortal champion; Aztec candidates include rival altepetl warlords → Cipactli-tier myth fauna → priest-king of a Triple Alliance enemy state; Norse candidates include rival jarls → Draugr lord → Jötunn herald of Jörmungandr. Specific roster is OPEN under §4.7 Direction-C ratification + 2026-04-25 Follow-up #5 cultural-sensitivity pass.

**Mixed historicity is intentional.** A Greek run reads as recorded history; an Aztec run shifts mortal-to-mythic mid-act-3; a Norse run is myth from minute one. This is not three failed attempts to be the same — it is three distinct flavors of "what does *this* commander's apocalypse look like." Same 30-round chassis; different narrative scale per civ.

**Myth-mode counterfactual arc** (post-launch direction, confirmed in 2026-04-27 amendment but **not in launch scope**). A future modifier could collapse all three civs to pure-myth framing (Leonidas vs. Hydra at round 30, Montezuma vs. Tezcatlipoca un-veiled from round 1, Ragnar vs. Jörmungandr on a synchronized Ragnarök timeline) for replay variety. Tracked as a deferred direction; no concept-constraint impact at launch.

**Solo-only.** PvP modes do **not** dramatize round-30 as the commander's antagonist — PvP round-30 is the symmetric "either side wins" lane-wars climax per `concept/phase-3.md §3.9`. The historic-arc framing is solo-only environmental theater layered over the same wave-shape backbone the matchmaker assumes for PvP, so co-op Horde inherits whichever player's commander is set as session host (or rotates per round per a future co-op-direction decision; OPEN).

**Cultural-sensitivity gate (Follow-up #5).** Every name in the table above (Xerxes / Tlaxcalan / Tezcatlipoca / Jörmungandr) and every mini-boss candidate is **placeholder-pending-consultation**. The Aztec two-phase reveal in particular requires consultation review for the Tezcatlipoca framing (Smoking Mirror is an active living-religion deity figure for some communities, not a museum-cabinet myth); the Tlaxcalan-as-villain framing requires care to avoid flattening Aztec-Tlaxcalan history into a simple good-vs-evil. No round-30 art-lock until the 2026-04-25 Follow-up #5 pass closes.

### Wave-composition variance mandate (NEW 2026-05-05 R9 close-out)

Per [`decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md`](../decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md), the [§4.11.8](#4118-skill-bar-thresholds-per-k) skill-bar thresholds are vulnerable to a **memorization meta** — a player who learns one fixed wave script can clear Hardcore at novice skill-bar values. To defend threshold integrity, the wave-composition system must support: (a) **random-seeded armor-tag mix per wave** (within difficulty-appropriate distributions; the matchup-correctness axis stays measurable but non-memorizable); (b) **per-map crystal-lock variance** (the boss-spike tile or wave-spawn point is map-specific and not editor-cloned across modes). Implementation lives in Phase 5; this section is the spec mandate. Locked content-skeleton bosses (R10 / R15 / R30 per civ) are exempt — their *composition* can vary but the *identity* (Xerxes / Tezcatlipoca / Jörmungandr) is fixed per the locked roster.

## 4.9 Save model

*Decision entry: [2026-04-20 save model](../decisions/2026-04-20-save-model.md). Reversibility: Medium.*

Mode-aware save model + always-persistent commander profile:

| Mode | Save | Autosave | Cloud |
|------|------|----------|-------|
| Solo Campaign | Manual Save-and-Exit (single slot per mission) + auto-save at mission-end | Age-gate boundaries + manual | Steam Cloud |
| Solo Skirmish | Per-run only; auto-save on end | End only | Steam Cloud (summary + settings) |
| Co-op Horde | Per-run only; auto-save on end (host) | End only | Steam Cloud (host) |
| Lane Wars 1v1 / 2v2 | None (no mid-match save, no restart — per §3.9) | N/A | Stats to profile on end |
| Commander profile | Always-persistent (XP, unlocks, cosmetics, settings, keybinds, audio levels, accessibility toggles) | Continuous (debounced) | Steam Cloud |

**Launch identity model:** single local profile per install. No account system at launch (FLOW-03 Post-launch-ok). Steam Cloud is the launch-day sync mechanism; cross-platform cloud parity evaluates per storefront on expansion.

**No ironman default** (reaffirmed from §3.9 Alternative D). Ironman as an optional Solo Skirmish modifier is a Phase 5 concern.

**Autosave loss-window:** in Solo Campaign, capped at one age's worth of play (age-gate autosave floor) — typically 2–4 minutes at target pacing.

Per-slot UI, cloud-conflict resolution UX, corruption-recovery protocol, and multi-profile-per-install are Phase 5.

## 4.10 Tower-vs-Unit math (conceptual frame)

*Decision entries: [`2026-05-04 Balance-pass #1 conceptual frame`](../decisions/2026-05-04-balance-pass-1-conceptual-frame.md) (Accepted; Reversibility Medium) + [`2026-05-04 Round 12 aux UX + frame extension (s)`](../decisions/2026-05-04-round-12-aux-ux-frame-extension.md) (Accepted; Medium) + [`2026-05-05 Concept amendment pass scope`](../decisions/2026-05-05-concept-amendment-pass-scope.md) (Easy). Numbers consumed by [§4.11](#411-numbers-floor) — this section binds **shape**; §4.11 binds **values**. Reversibility: Medium.*

This section anchors the equation governing tower-vs-runner combat. Magnitudes (HP curves, DPS ladders, commander-ability numbers, per-mode tuning) live in [§4.11](#411-numbers-floor); auxiliary-economy slot magnitudes live in [§4.6a](#46a-auxiliary-economy). The frame here is the source-of-truth for *what variables exist and how they combine*; §4.11 bind*s their values.*

### 4.10.1 Variable nomenclature (locked 2026-05-04, extension 2026-05-04 R12)

| Var | Meaning |
|-----|---------|
| (a) | **Tribute pool** — primary currency, sourced from kills + sell refunds + boss lump-sums. |
| (b) | **Friendly tower roster** — count + type composition. |
| (c) | **Tower base damage** — per-tower per-shot, scaled by level via `effectiveTowerStats` multipliers. |
| (d) | **Lane runners** — count + type composition per wave. |
| (e) | **Runner HP pool** — per-runner. |
| (f) | **Runner speed** — per-runner; modifiable by status procs. |
| (g) | **Tower-vs-runner type bonus** — RPS matrix lookup, **bidirectional ±25%** (1.25× / 0.75×). |
| (h) | **Commander-avatar contribution** — three slots (passive / short-CD active / long-CD signature) × four effect types (damage / control / summon / economy). |
| (i) | **Tower placement** — player-skill axis, function-shaping (sets engagement-time integral). |
| (j) | **Map** — per-map (ε, N) tuple: ε engagement coefficient ∈ [0,1], N buildable hex count. |
| (k) | **Difficulty tier** — Easy / Hard / Hardcore. Modifies HP-curve exponent only (single-axis compounding). |
| (l) | **Tower lifecycle state** — (tier, level) tuple. Tier ∈ {T1, T2, T3, T4 Demigod, God}; Level ∈ {1, 2, 3}. Both axes first-class. |
| (m) | **Adjacency / placement-coupling** — merge requires same-civ same-tier within `CIV_MERGE_RADIUS`. Promote requires single T3 + Tribute spend (per [§4.11](#411-numbers-floor)) + valid demigod mapping. Fusion requires two T4 Demigods of same civ + 1 Divinity (after 2-Divinity menu unlock). |
| (n) | **Buildable-slot binding** — derived from (j) N; binds once (a) > N × cost-of-cheapest. |
| (o) | **Divinity** — second currency. Cap 6/match. Drains 2 (Fusion menu unlock) + 1 per fusion. Source pattern locked per [`2026-05-05 Round 10 Divinity sources`](../decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md): 4-source floor (R10 / R15 / R30 boss + match-completion = 1 each) + 2 escalation sources (Perfect-Wave +1 per zero-leak boss-clear, max +3; First-Hybrid +1 one-shot per topology-true cross-civ hybrid). |
| (p) | **Runner armor tag** — 5 buckets (Unarmored / Shielded / Beast / Spirit / Colossal). RPS matrix routes through this per [`2026-04-26 attack-type mapping`](../decisions/2026-04-26-attack-type-mapping.md). |
| (q) | **Status-proc layer** — 7 procs (Armor-shred / Bleed / Stagger / Burn+splash / Toxin / Hex / Smite). Cross-tower feedback explicit (e.g., Piercing Armor-shred lowers (p) effective armor for downstream towers' damage). |
| (r) | **Lives** — per-mode declarable per [`2026-05-04 Round 9 PvP-IW deep-dive`](../decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md): Solo / Horde / PvE-MP / PvP-IW = 30 leak knockout; PvP-Maze = 10. Per-leak severity tunable. |
| **(s)** | **Auxiliary multiplicative bonus** — first-class multiplier on the damage equation, applied globally per active aux slot. Magnitudes per [§4.6a](#46a-auxiliary-economy): Damage Bonus = 1 Divinity = (s) = 1.20× global, max 1 active/match. Round-12 extension; first-class to avoid pollution of (c)/(g)/(h). |

### 4.10.2 Master damage equation

For each runner R in a wave:

```
Damage_dealt(R) = (s) × Σ_T [ DPS(T) × t_engaged(T, R) × matchup(T, R, p) × passive_modifiers(T, h) × status_state(R, q, t) ]
```

Where:
- `DPS(T) = damage(T) / (cd(T) / 60)` — damage per second.
- `t_engaged(T, R) = path_length_in_range(T, j) / speed(R, q)` — engagement-time integral over the path within tower T's range.
- `matchup(T, R, p) ∈ {0.75, 1.00, 1.25}` per the 7-attack × 5-armor RPS matrix.
- `passive_modifiers(T, h)` — commander passive applies multiplicatively (e.g., +15% civ-matched aura per [§4.11](#411-numbers-floor)).
- `status_state(R, q, t)` evolves as (q) procs accumulate on R; cross-tower feedback expressed (Armor-shred lowers (p) effective armor for downstream towers).
- `(s)` global multiplier outside the sum — applied once per damage event regardless of tower count.

**Win condition:** lives > 0 at end of round 30 (PvE modes) or last-alive (PvP modes per [§3.6](phase-3.md)). Each leaked runner deducts lives per its severity tag.

### 4.10.3 Round-slot typology (locked 2026-05-04)

Seven slot types: **Standard / Swarm / Elite / Modifier / Telegraph / Boss / Recovery**.

R-assignments across the 30-round arc:

- **R5** — Modifier
- **R10** — Boss (drops 1 Divinity + Tribute medium lump)
- **R15** — Elite (mini-boss; drops 1 Divinity per Round-10 Divinity-sources amendment)
- **R20** — Modifier
- **R25** — Telegraph
- **R30** — Final Boss (drops 1 Divinity + Tribute huge lump; match-completion drops +1 Divinity for floor=4 sources)
- **Recovery slots** float post-special (e.g., R6, R11)
- **Standard** fills the remainder (~22 rounds)

### 4.10.4 (k) single-axis compounding rule

(k) modifies the **HP-per-wave curve exponent only**. All other R-curves identical across tiers. Easy / Hard / Hardcore diverge geometrically late, not flatly. **Anti-pattern explicitly flagged:** stacking HP + speed + reward + cost penalties simultaneously per tier compounds geometrically and makes R30 Hardcore mathematically unwinnable independent of skill execution. Single-axis discipline preserved across all numbers-phase ratifications.

PvP modes (PvP-IW + PvP-Maze) declare no (k) — they are player-driven; tie-break uses HP-only escalation per [§3.6](phase-3.md) (R31+ HP × 1.5^(R−30) compound + R45 co-victory floor).

### 4.10.5 Skill-bar axes (k winnability target)

Three QA-instrumentable axes drive (k) winnability:

1. **Matchup-correctness rate** — % of damage dealt with type advantage (drives (q) coverage).
2. **Placement-coverage** — `ε_actual / ε_max` for the map (drives (i) bonus + engaged-time ε from (j)).
3. **Ability-uptime** — % of commander cooldowns spent in engaged windows; signature explicitly excluded as once-per-match strategic-decision lever.

Per-(k) thresholds locked per [§4.11](#411-numbers-floor); telemetry definitions per [`concept/phase-6.md`](phase-6.md).

### 4.10.6 Sell-refund schedule (locked 2026-05-04)

| Timing | Refund |
|--------|--------|
| Pre-wave (before "Send Wave" pressed) | **100%** |
| Same wave post-send | **90%** |
| R+1 (next round) | **80%** |
| R+2 | **70%** |
| R+3 onward | **60% flat** |
| T4 / God (any timing) | **60% capped** |

(k)-coupled: Easy = full schedule; Hard = floor at 60%; Hardcore = steeper schedule, floor at 50%.

### 4.10.7 Tower target-priority (locked 2026-05-04)

AI default = First (closest to base). Per-tower override via right-click → {First / Last / Strongest / Weakest / Closest}. Available as a Universal aux slot per [§4.6a](#46a-auxiliary-economy).

### 4.10.8 Boss / Elite reward shape (locked 2026-05-04, amended 2026-05-05 R10)

- **R10 Boss:** medium Tribute lump (250 T per [§4.11](#411-numbers-floor)) + 1 Divinity drop.
- **R15 Elite:** medium Tribute lump (400 T) + 1 Divinity drop (per R10 Divinity-sources amendment promoting R15 from 0 → 1 Divinity).
- **R30 Final Boss:** huge Tribute lump (1,500 T) + 1 Divinity drop (R30 specifically) + 1 Divinity at match-completion.
- **Standard / Swarm / Modifier / Telegraph / Recovery:** per-runner reward curve only per yield(R) in [§4.11](#411-numbers-floor).

### 4.10.9 Engine-port discipline

The DPS×integral form translates 1:1 to Godot 4 process-tick math: `delta` is the engagement-time differential, summed per tower per tick. `(s)` and `passive_modifiers(T, h)` apply at damage-event resolution, not per-tick. `status_state(R, q, t)` is a per-runner state vector evolving in `_physics_process`. No structural rewrite required for the prototype-to-engine port.

## 4.11 Numbers floor

*Decision entries: [`2026-05-05 Round 1 HP curve`](../decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md) + [`Round 2 (k) exponents`](../decisions/2026-05-05-balance-pass-2-round-2-k-exponents.md) + [`Round 3 Tribute economy`](../decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md) + [`Round 4 map+speed`](../decisions/2026-05-05-balance-pass-2-round-4-map-speed.md) + [`Round 5 tower baselines`](../decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md) + [`Round 6 commander magnitudes`](../decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md) + [`Round 8 per-mode tuning`](../decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) + [`Round 9 skill-bar thresholds`](../decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) (all Accepted; Reversibility Medium). All magnitudes consume the [§4.10](#410-tower-vs-unit-math-conceptual-frame) frame. Reversibility: Medium.*

This section binds the Round 4 amendment-pass placeholder. Per-tower (cd / range / attack-type / status-proc variance) + per-commander effect-type variants (control / summon / economy beyond damage-floor) + per-civ specialization + per-map good-cell authoring are **deferred** to post-amendment-pass authoring sub-passes. The numbers here are the **floor**: every authoring sub-pass starts from these magnitudes and tunes within them.

### 4.11.1 HP curve (e)

`HP_std(R) = 100 · 1.16^R` (Easy default base) — applies to runners on the standard runner-archetype track. Boss / Elite rounds spike via multiplier `m(R)`:

| Round | m(R) |
|---|---|
| R10 Boss | ×3 |
| R15 Elite | ×2 |
| R30 Final Boss | ×5 |
| All others | ×1 |

Anchor values (Easy, std unless flagged): R1 = 116; R5 = 210; R10 = 442; R10 boss = 1,326; R15 = 919; R15 elite = 1,839; R20 = 1,931; R25 = 4,058; R30 = 8,585; R30 boss = 42,925.

### 4.11.2 (k) exponents

Per [§4.10.4](#4104-k-single-axis-compounding-rule), (k) compounds the **HP exponent only** — DPS, costs, yields, speeds are k-invariant.

| Difficulty (k) | HP exponent b | R30 std HP | R30 boss HP (×5) |
|---|---|---|---|
| Easy | 1.16 | 8,585 | 42,925 |
| Hard | 1.19 | 23,737 | 118,685 |
| Hardcore | 1.22 | 65,498 | 327,490 |

Sample R1 / R10 / R30 trajectories: Easy 116 / 442 / 8,585 | Hard 119 / 567 / 23,737 | Hardcore 122 / 731 / 65,498. PvP modes carry **no (k)** (PvP equality non-negotiable per [§4.10.4](#4104-k-single-axis-compounding-rule)); PvP HP runs on the Easy track and tie-breaks via the §4.11.7 R31+ HP-only escalation.

### 4.11.3 Tribute economy (a)

Per-runner yield (k-invariant): `yield(R) = 5 · 1.10^R`. Anchors: R1 = 5.5; R5 = 8; R10 = 13; R15 = 21; R20 = 34; R25 = 54; R30 = 87.

Boss / Elite lump rewards (per [§4.10.8](#4108-boss--elite-reward-shape-locked-2026-05-04-amended-2026-05-05-r10)):

| Round | Tribute lump | Divinity |
|---|---|---|
| R10 Boss | 250 T | +1 |
| R15 Elite | 400 T | +1 (per 2026-05-05 R10 amendment) |
| R30 Final Boss | 1,500 T | +1 (lump) + match-completion +1 |

Cumulative Easy R1→R30 income: **~25,000 T** (run-curve + lumps).

### 4.11.4 Speed (f) + per-map (j)

Speed base: **`f_base = 50 u/s`** (constant across R; movement difficulty lives in HP, not speed).

Archetype multipliers (off `f_base`):

| Archetype | × | u/s |
|---|---|---|
| Standard | 1.0 | 50 |
| Swarm | 1.5 | 75 |
| Elite | 1.0 | 50 |
| Boss | 0.7 | 35 |
| Colossal | 0.5 | 25 |

Per-map defaults: engagement coefficient **ε = 0.6** (fraction of lane length covered by tower range under reasonable placement); buildable-hex baseline **N = 24** (per-mode overrides in §4.11.7).

### 4.11.5 Tower DPS ladder (c) + tier-up costs

DPS ladder off `T1_base = 20 dmg/sec`:

| Tier | × | DPS |
|---|---|---|
| T1 | 1.0 | 20 |
| T2 | 3.0 | 60 |
| T3 | 9.0 | 180 |
| T4 (Demigod) | 27.0 | 540 |
| God (Fusion) | 54.0 | 1,080 |

Tier-up costs (Tribute; sell-refund schedule per [§4.10.6](#4106-sell-refund-schedule-locked-2026-05-04)):

| Step | Tribute | Cumulative sunk |
|---|---|---|
| T1 placement | 100 | 100 |
| T2 merge | 300 | 500 |
| T3 merge | 900 | 1,900 |
| T4 promote | 2,500 | 4,400 |
| Fusion (T4×2 → God) | 0 T (1 Divinity + valid recipe) | 8,800 sunk + 1 Div |

On-curve Easy spend ≈ 10,700 T per match → ~14,300 T headroom against ~25,000 T income, sized for skill-bar (k)-induced overspend (placement misses, sells, redundant matchup buys).

### 4.11.6 Commander magnitudes (h)

Per [§4.10.1](#4101-variable-nomenclature-locked-2026-05-04-extension-2026-05-04-r12) (h) and [`§4.1`](#41-commander-mechanical-spec-identity-floor-proposal-per-commander-writeup-open) identity-floor:

- **Passive aura:** **+15% damage** to civ-matched towers within hex-distance ≤ 2 (2-cell aura).
- **Active burst (short CD):** `4 × T3_DPS × 4s` = 4 × 180 × 4 = **2,880 burst damage** to target tower's volley over 4s; 30s CD (~13% uptime).
- **Signature ability (long CD):** **once per match** — instant tier-up of target tower (T1→T2 or T2→T3); bypasses Tribute cost only (no merge requirement). Excluded from §4.10.5 ability-uptime axis per locked rule.

Per-commander effect-type variants (Leonidas / Montezuma II / Ragnar Lothbrok control / summon / economy spreads beyond the damage-floor) are deferred to the per-commander authoring sub-pass — only the **damage-floor magnitudes above are spec-locked**.

### 4.11.7 Per-mode tuning (g / p / q)

**Send-Creeps variants** (100 T baseline send cost; per-mode reward shape):

| Mode | Send shape | Reward |
|---|---|---|
| Solo / PvE-MP Lane-Trade | 3 std creeps | +50% kill-bonus yield |
| Horde Reinforce-Lane | 1 helper @ 4× R-runner HP | shared lane support |
| PvP-Maze Send-Through-Maze | 1 creep, success-gated | +5 T/round on success |
| PvP-IW Send-for-Interest | 1 Div unlock + 150 T/send | +3 T/round recurring (Squadron-TD) |

**Per-mode N-scaling (buildable hexes):**

| Mode | N |
|---|---|
| Solo / Horde-A / PvE-MP / PvP-IW | 24 |
| Horde-B (shared lane) | 24 × player_count |
| PvP-Maze | 30 |

**PvP R31+ tie-break:** HP scales `× 1.5^(R-30)` (HP-only per [§4.10.4](#4104-k-single-axis-compounding-rule)); co-victory declared at **R45** if no leak.

### 4.11.8 Skill-bar thresholds per (k)

Per [§4.10.5](#4105-skill-bar-axes-k-winnability-target) the 3 skill-bar axes (matchup / placement / ability-uptime) carry per-(k) expert / novice thresholds:

| Axis | Easy expert | Hard expert | Hardcore expert | Novice (all k) |
|---|---|---|---|---|
| Matchup-correctness | 60% | 75% | 90% | 30% |
| Placement-coverage | 50% | 65% | 80% | 30% |
| Ability-uptime | 40% | 60% | 80% | 20% |

Hardcore expert realized DPS multiplier: 0.90 × 0.80 × 0.80 ≈ **0.58× realized** vs nominal — sized so a Hardcore expert clears R30 (65,498 HP boss) on-curve with ~1.0× realized headroom against the cumulative-DPS budget. Novice on Hardcore expects to fail before R20 (intended). Telemetry definitions per [`concept/phase-6.md`](phase-6.md) (forward-anchor).

## 4.8 Exit condition for Phase 4

- Commander one-pagers complete for all 3 launch commanders (Leonidas / Montezuma II / Ragnar Lothbrok) — passive + short-CD active + long-CD active full specs under the §4.1 identity floor.
- Fusion system shape signed off (done 2026-04-25: 9 locked Gods via 9 locked 2-Demigod recipes, Divinity-gated, menu-driven discovery). Fusion-numerics balance-pass remains [PROPOSAL].
- Mobile unit control model resolved (§4.4 OPEN BLOCKER).
- Enemy direction locked (§4.7 A/B/C choice ratified; leading placeholder = Option C hybrid).
- Economy balanced on paper (Tribute + Divinity income curves, per-tier tower costs, Fusion spend cadence; §4.6 locks shape, numerics [PROPOSAL]).
- Monetization model specifics resolved (cosmetic-only; no-pay-to-win non-negotiable).
- Engine choice locked (leading: Godot 4 per `concept/phase-5.md §5.5`).
- Art director engaged or scoped.
- **Cultural-sensitivity pass scheduled** — 2026-04-25 Follow-up #5 gate landed before any Phase 5 content lock touches Aztec representation, Leonidas visual framing, or Ragnar TV-vs-history framing.

→ **Hand off to [Phase 5](phase-5.md).**
