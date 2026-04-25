---
**Status:** Draft
**Last reviewed:** 2026-04-26
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
- **Historic match-arc beats** — see [§4.7](#47-enemy-system-pve-modes) banner extension (queued in immediate follow-on turn). Commander's historic arc + round-30 antagonist drive solo-mode environmental beats; PvP retains the 2026-04-25 lane-wars shape unchanged. Round-30 antagonists per civ: **Xerxes I** (Greek, named historic) / **two-phase Tlaxcalan war-leader → Tezcatlipoca avatar** (Aztec, pre-contact framing — Cortés explicitly OUT of all acts) / **Jörmungandr or Fenrir** (Norse, myth-overlay; sub-question OPEN). Cross-civ tonal arc escalates mortal → bridge → myth — intentional, not asymmetry oversight.

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

Commander Hero Units (signature ability deployments) have richer control — direct movement + 2–3 abilities + return-to-base. One active Commander Hero per player per match.

## 4.5 Special effect units specification

Special effect units are limited in placement count per match to avoid spam. Examples:
- Timed zones (debuff aura for 20 seconds).
- Consumables (one-shot damage bursts, healing pulses).
- Terrain modifiers (e.g., a tar pit or consecrated ground that expires at the next tier gate — per-civ allocation is Phase 5 spec).

Each special effect has a cooldown, a cost (Tribute for tactical effects, Divinity for mythic-tier effects that read as one-shot "prayer" moments — final currency split deferred to §4.6), and a visible indicator on the map. Status-effect procs (Burn, Bleed, Toxin, Hex, Smite, Armor-shred, Stagger) are **not** special-effect units — they're driven by the source tower's primary attack type per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md). Specification per-item is a Phase 5 task; Phase 4 locks the *framework* only. Cultural-sensitivity pass (2026-04-25 Follow-up #5) applies to any special-effect visual tied to a civ's religious iconography (especially Aztec ritual effects).

## 4.6 Economy specification

*→ active drill-down: [stage 03 — match setup](../stages/03-match-setup.md), [stage 04 — in-match core](../stages/04-in-match-core.md). **Two-currency shape locked 2026-04-25** per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md); numerics [PROPOSAL].*

Prior three-lineage-aligned currency mapping (Gold / Faith / Cinders from Nature / Prayer / Ash) is **superseded** — the lineages that backed it don't exist under the real-cultures frame. The 2026-04-25 ratification locks a **two-currency economy** anchored to the 30-round match cap and the Fusion endgame:

### Locked shape (2026-04-25)

- **Tribute** (primary) — generated by tower placements, wave clears, enemy kills, and time. Spent on tower placement, tower T1→T2→T3 promotions, T3→T4 Demigod/Hero unlocks, unit purchases, special-effect consumables. This is the moment-to-moment economy — high-volume, always flowing.
- **Divinity** (mythic token, 6-cap per match) — earned **one per boss round** across the 30-round arc: mini-bosses at rounds 5 / 15 / 25 and main bosses at rounds 10 / 20 / 30. Spent exclusively on the **Fusion endgame**: 2 Divinity to unlock the civ-wide Fusion menu, then 1 Divinity per fusion execution. Realistic match outcome: 2 menu-unlock + 3 fusions = 5 of 6 Divinity spent; one spare for flex or a late-game ritual special effect (see §4.5).

The 2-currency shape replaces the prior 3-currency-per-lineage-producer split with a **scale split** — Tribute handles mortal-tier economy breadth, Divinity is the rare mythic token reserved for the game's identity moment (becoming a God). "Every build touches an economy lineage" is replaced by "every build touches Tribute, and every serious build reaches for Divinity."

### Multiplayer-only third currency (unchanged from prior spec)

- **Mythium** (placeholder name — not §5.4-ratified) — time-based income from workers, Legion TD 2 pattern. Spent on sending creeps / mercenaries to opponent lanes. PvP-modes only. Does not interact with Divinity.

### Open under the new shape

- **Divinity income refinement:** is the 6-cap hard (forbidden to bank over), or soft (can-earn but wastes)? Leading: hard cap with a UI indicator when a boss round won't produce Divinity because you're capped. Encourages Fusion spend cadence.
- **Tribute numerics:** starting Tribute, wave income curve, per-tier tower placement costs, T3→T4 Demigod unlock cost — all [PROPOSAL], balance pass in Phase 5.
- **Late-game Tribute sinks** past round 25 once the T4/Fusion ladder is fully built — to prevent Tribute-hoarding trivializing late waves. Candidates: consumables, board-level buffs, emergency rebuilds.
- **Status-proc cost integration:** attack-type procs from 2026-04-26 are "free" (part of the tower's kit), but should enhanced proc tiers be Tribute-purchasable at T3? Deferred to Phase 5 balance.
- **Cultural-framing of Divinity:** the currency name "Divinity" is descriptive, not §5.4-ratified. Cultural-sensitivity pass applies (an Aztec "Divinity" spend to summon Huitzilopochtli needs care — 2026-04-25 Follow-up #5).

Bookkeeping is standard; balance work is extensive and deferred to Phase 5.

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
