---
**Status:** Draft
**Last reviewed:** 2026-04-26
---

# Phase 4 — Specification

*Detailed system design. This is where the game actually becomes a game.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-3.md](phase-3.md). Next: [phase-5.md](phase-5.md).

---

**Amendment banner — 2026-04-26 real-cultures frame cascade (partial).** Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility Hard), this turn rewrites **§4.1 (commander spec)**, **§4.3 (hybrid system → Fusion system)**, and **§4.7 (enemy system)** to the real-cultures frame. **§4.2 (divergence), §4.5 (special effects), §4.6 (economy), §4.8 (exit condition)** retain their prior frame for traceability — they will be rewritten in follow-on turns of the same cascade queue (2026-04-25 ratification Follow-up #1). Attack-type / armor / RPS surfaces reference the 2026-04-26 mapping ([`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md), Reversibility Medium).

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

## 4.2 Divergence system

*→ active drill-down: [stage 05 — age evolution](../stages/05-age-evolution.md). **Rescoped OPEN** under the 3-tier Ash→Altar arc per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md).*

At tier transitions, the player picks a fork that re-skins every lineage's expression for that tier and all future tiers of the match. The fork does not change the lineage's mechanical role — it changes how that role is expressed visually and subtly mechanically (damage types, tempo, etc.).

Under the 3-tier arc there are at most **2 tier-transition forks** per match (Dust→Form, Form→Apotheosis); prior 4-fork × 3-option (81-path) variety math no longer applies. New fork pool and per-fork-option themes are **OPEN** — they must:
- Sit inside the dungeon-cosmology aesthetic (`concept/phase-5.md §5.3`).
- Express the Ash→Altar arc rather than a technology timeline.
- Preserve enough combinatorial variety that two matches on the same commander feel different.

**Placeholder shape (not ratified):**
- **Dust → Form fork:** 3 options, themes OPEN (candidates: salvage-lean / bloom-lean / rite-lean as tier-coloration).
- **Form → Apotheosis fork:** 3 options, themes OPEN (candidates: ascension / descent / threshold).

Run variety ceiling under 2×3=6 paths is narrow; heirloom / commander-affinity / mapmod layering may reopen breadth. Full fork design is a Phase 4/5 deliverable under the new tier frame.

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
- Terrain modifiers (e.g., a tar pit or consecrated ground that expires at the next tier gate — per-lineage allocation is Phase 5 spec).

Each special effect has a cooldown, a cost, and a visible indicator on the map. Specification per-item is a Phase 5 task; Phase 4 locks the *framework* only.

## 4.6 Economy specification

*→ active drill-down: [stage 03 — match setup](../stages/03-match-setup.md), [stage 04 — in-match core](../stages/04-in-match-core.md). **Currency mapping rescoped OPEN** under 3-lineage shape per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md).*

Prior three-currency mapping (Gold / Knowledge / Influence from Forge / Ember / Crown, with Sinew + Veil as pure consumers) no longer applies — the lineages that backed those pillars don't exist in the 3-lineage shape. Under Ash / Nature / Prayer, the "every build must touch an economy lineage" invariant is auto-satisfied (only 3 lineages exist; any build touches at least one), so the prior *structural enforcement* of economy breadth is replaced by the lineage count itself.

**Placeholder mapping [PROPOSAL] — flagged OPEN for Phase 4 resolution:**
- **Gold** — generated by Nature towers (growth / economy pillar) and wave kills. Spent on tower placement and tower upgrades.
- **Faith** — generated by Prayer towers (aura / order pillar). Spent on aura upgrades and fork choices.
- **Cinders** — generated by Ash towers and tower losses / recycles. Spent on hybrid crafting and salvage-line upgrades. The salvage-loop is a load-bearing identity piece: Ash is the only lineage that converts *losing* towers into currency.

**Multiplayer-only fourth currency (unchanged from prior spec):**
- **Mythium** (placeholder) — time-based income from workers (Legion TD 2 pattern). Spent on sending creeps/mercenaries to opponent lanes.

**OPEN under new shape:**
- Whether all three lineages produce currency (breadth-by-default) or whether one lineage is a pure consumer (breadth-by-constraint). Prior design used a producer/consumer split for deliberate tension; with a 3-lineage roster, making any one lineage pure-consumer risks making it skip-able.
- Currency names (Gold / Faith / Cinders) are placeholders, not §5.4-ratified.
- Hybrid-crafting cost model (does Cinders gate hybrid unlock, or just accelerate?) — depends on §4.3 blocker #1 resolution.

Bookkeeping is standard; balance work is extensive and deferred to Phase 5 under the new shape.

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

- Commander spec complete (one-page per commander).
- Hybrid discovery mechanic resolved.
- Mobile unit control model resolved.
- Enemy direction locked.
- Economy balanced on paper (spreadsheet with currencies, costs, income curves).
- Monetization model specifics resolved.
- Engine choice locked.
- Art director engaged or scoped.

→ **Hand off to [Phase 5](phase-5.md).**
