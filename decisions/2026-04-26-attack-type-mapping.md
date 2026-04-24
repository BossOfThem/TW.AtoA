# Decision — Attack-type mapping: 7-type taxonomy + per-tower/demigod/god assignment + RPS armor matrix + status-proc table

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Medium — taxonomy shape (the 7 types, the RPS matrix skeleton, the armor tag list) would be painful to unwind once towers, demigods, gods, and enemy archetypes are balanced against them, but individual per-tower / per-demigod assignments can flex during balance passes without touching the structural shape. All magnitudes ([+25%/−25%], DoT durations, stagger lengths, etc.) are flagged [PROPOSAL] and re-ratified by a dedicated balance pass.
**Affects:** combat math across every tower, every unit, every T4 demigod, every God; enemy roster design (once it opens); UI (armor-tag icons, damage-type icons, damage-number coloring); prototype (deferred — prototype frozen until cascade lands); `concept/phase-4.md §4.7` (enemy direction — RPS matrix constrains enemy archetype design); eventual balance/tuning decisions.
**Does NOT affect:** `concept/phase-2.md §2.4a` [LOCKED] (accessibility floor — colorblind glyphs add-on for type icons is a §2.4a compliance consumer, not a violation); `concept/phase-5.md §5.4` [LOCKED] (naming conventions — all 7 type names tested against "high-school recognizable" heuristic); mechanics (TD/merge/debuff/magic preserved — debuff+magic mechanics map cleanly onto Arcane/Divine type procs; the 7-type system is the implementation of the "debuff" surface the 2026-04-24 reopen locked); locked names from 2026-04-25 ratification (no civ, commander, tower, unit, T4 demigod, god, or God recipe renamed).

---

## Decision

Ship a **7-type attack taxonomy** — **Piercing, Slashing, Crushing, Fire, Poison, Arcane, Divine** — with a single primary type per T1–T3 tower and per T4 Demigod/Hero, and inherited 2-type damage on each of the 9 Gods via the locked fusion recipes. Enemies carry 1 of **5 armor tags** — **Unarmored, Shielded, Beast, Spirit, Colossal** — and each attack type gets **+25% vs one tag / −25% vs one tag** in a rock-paper-scissors matrix. Each type triggers one light, non-stacking status proc (Poison is the sole stacking exception, up to 5 stacks). All numbers are [PROPOSAL] pending the balance pass.

---

## Context

Q2 real-cultures direction ratified 2026-04-25 locked the full launch-match content skeleton (3 civs; 3 launch commanders + kits; 18 T1–T3 towers; 15 units; 18 T4 Demigods & Heroes; 9 Gods via fixed 2-demigod Fusion recipes; Tribute/Divinity economy; lane-wars 30-round match arc; "high-school recognizable" naming discipline; "mundane names outside, myth inside" heuristic). Every tower/demigod/god needs a damage identity; every enemy will need armor tags; player-side build decisions depend on a legible rock-paper-scissors counter layer. The 2026-04-24 reopen preserved the **debuff/magic** mechanics surface — status procs are the landing zone for that preservation. The handoff pre-locked: 6–8 types soft cap; single primary per tower; Gods as the only 2-type sources; simple +25/−25 RPS; light non-stacking procs. This decision delivers the first concrete instantiation.

## Alternatives considered

- **Option A — 5-type minimal (Piercing / Slashing / Magic / Fire / Poison, merging Divine into Magic and dropping Crushing).** Simplest UI, smallest icon set, easy balance. Rejected: collapses real mythic distinctions (Oracle-prophecy vs Pyramid-ritual vs Rune-magic all land on one icon), leaves siege-weapons (Acropolis ballista, Trireme ram, Hercules' club, Beowulf's bare-hands) without a thematic home, forces Forge-fire and Colossus-sun-bronze to compete for the same slot.
- **Option B — 9+ type maximal (split Arcane into Prophecy/Wind/Rune; split Divine into Holy/Ritual; split Slashing into Sword/Axe).** Maximum thematic precision per culture. Rejected: blows past the 6–8 soft cap; forces civ-coded damage types that punish cross-civ play; each added type doubles the RPS-matrix surface area the player must hold in head at gameplay speed; violates the "high-school recognizable" heuristic (Prophecy and Ritual as distinct damage types is a TTRPG-nerd-floor distinction).
- **Option C — 7-type unified (Piercing / Slashing / Crushing / Fire / Poison / Arcane / Divine).** (Chosen.) Within the 6–8 soft cap. Every type is a word a high-school student recognizes. Each civ gets 4–6 type-coverage slots across its T1–T3 roster (forcing meaningful cross-civ play). Arcane vs Divine preserves the meaningful distinction between "wielded magic" (prophecy, rune, wind) and "channeled godhood" (temple, ritual, anointed king). Each of the 9 Gods lands on a non-mono-type 2-pair via locked recipes (verified below). Status procs cleanly fulfill the locked debuff/magic mechanic preservation.

## Reason chosen

Option C threads the needle on the locked constraints:
- **Soft cap honored.** 7 types sits inside 6–8.
- **High-school recognizable.** Piercing / Slashing / Crushing / Fire / Poison / Arcane / Divine are all words a general audience holds without glossary.
- **"Mundane outside, myth inside" honored.** Damage *type* names are mundane; the myth is embedded in which tower/demigod/god uses them (Oracle=Arcane is prophecy-magic, but "Arcane" on the icon is legible without myth-literacy).
- **Mechanics preservation.** The locked debuff/magic mechanic from the 2026-04-24 reopen is implemented by the 7 status procs. Debuff surface covers: armor-shred (Piercing), bleed DoT (Slashing), stagger-slow (Crushing), burn DoT + splash (Fire), stacking toxin DoT (Poison), hex attack-speed-slow (Arcane), smite % bonus vs Spirit/Colossal (Divine).
- **Cross-civ play incentive.** Each civ has clear type-holes (Greek has no Slashing or Poison tower; Aztec has no Crushing; Norse has no Poison or Divine). Multi-civ mixing fills gaps. Reinforces the content skeleton's implicit multi-civ future (patch-1 commanders, Foresight-coin).
- **Locked Gods verified.** All 9 locked fusion recipes produce a 2-type pair where each God's two types are distinct and thematically legible (see tables below). No recipe collapses to mono-type.

### 3x debug loop

**Loop 1 — aggressive critique.** (a) 7 types is the upper end of the soft cap; pushes UI icon-budget close to a ceiling. (b) Arcane vs Divine overlap — players may not grok the difference mid-wave. (c) Poison is Aztec-exclusive at launch (Sacrificial Altar, Blood Priest, Tezcatlipoca only) — lock a player out of Poison access unless they invest in Aztec. (d) Fire is over-represented — Greek Colossus, Aztec Temple of the Sun, Norse Forge — every civ has Fire while Poison/Arcane/Divine are civ-concentrated. (e) Thor recipe is Björn (Slashing) + Beowulf (Crushing) → Slashing+Crushing; the myth expectation is Crushing+Arcane (Mjölnir + lightning), but the locked recipe does not include an Arcane source. Thor inherits a non-lightning 2-type pair. (f) +25%/−25% may be too tame compared to Tower Wars genre norms (often +100% / −50%+), risking a "numbers don't matter" feel. (g) Every Greek God ends up with Divine in its pair (Zeus=Crushing+Divine via Jason; Athena=Slashing+Divine via Perseus; Poseidon=Piercing+Arcane — only Poseidon escapes Divine). Greek Gods feel same-y. (h) Status procs are all single-effect floor — no real mythic flavor per God at the proc layer.

**Loop 2 — steelman.** (a) 7 types remains inside the soft cap; the UI burden is one icon per type plus armor-tag icon — well within the accessibility floor the §2.4a compliance already anticipates. (b) Arcane/Divine distinction lands cleanly in the RPS matrix: Arcane +Spirit/−Beast vs Divine +Colossal/−Shielded. Different rows reinforce different playstyles; a player who confuses them quickly learns from mismatched counter-picks. (c) Poison as civ-exclusive is a *feature*: signature types are the reason to pick a civ; every civ has one or two signature types unavailable elsewhere. This is the multi-civ-future hook working as intended. (d) Fire-everywhere is thematically correct — every civilization used fire. The differentiator is the *proc flavor* attached (Fire burn + splash) which is the same across civs, while the *tower* using Fire varies by civ identity. Fire being type-of-last-resort is OK. (e) Thor-recipe dissonance is recipe-level, not taxonomy-level: the taxonomy faithfully reads the locked recipe. If Thor-Arcane is desired, it's a recipe decision (change Björn or Beowulf → Arcane source), not a taxonomy decision. Flag as follow-up. (f) +25/−25 is a floor for *clarity-first*; large deltas can be added in balance pass if playtest reveals a damp feel, but starting tame preserves mistake-recoverability (players who misread armor aren't punished catastrophically). (g) Greek-Divine prevalence reflects Greek myth — temples and god-born heroes (Jason, Perseus) *are* the Greek mythic texture. Aztec has its own dominant flavor (Fire + Poison + Arcane), Norse has its own (Slashing + Crushing + Divine-via-rune-king). (h) Proc-per-type instead of proc-per-god is the locked "light, not stacking" constraint; per-god proc richness is a downstream (Fusion-combo) layer the handoff explicitly parks.

**Loop 3 — synthesis.** Ship the 7-type taxonomy and the RPS matrix as specified. Accept that:
- Type icons will be 7 + 5 armor tags = 12 total small glyphs — UI-budget-acceptable, accessibility-floor-compatible with colorblind glyph add-on.
- Poison / Arcane / Divine being civ-concentrated is a feature enforcing multi-civ play.
- Thor recipe dissonance is a recipe-side follow-up, not a reason to bend the taxonomy.
- +25%/−25% magnitudes are [PROPOSAL] floors — flagged for balance-pass re-ratification.
- Greek-Divine prevalence is mythologically correct and flagged as a taxonomy-audit item for the balance pass, not a taxonomy redesign trigger.
- Fusion-combo status-proc richness is explicitly deferred (e.g., Fire+Poison = "burning plague" combo emergent effect) — that is a later decision, not this one.
- All per-tower and per-demigod assignments are balance-flexible inside the taxonomy without reopening this decision.

## The taxonomy

### Types + status procs (all [PROPOSAL] numbers)

| # | Type | Status proc | Magnitude (proposed) | Stacks? |
|---|------|-------------|----------------------|---------|
| 1 | **Piercing** | Armor-shred | −1 armor for 3s, refreshes | No (refreshes) |
| 2 | **Slashing** | Bleed | DoT ~5% weapon damage/sec for 3s | No (refreshes) |
| 3 | **Crushing** | Stagger | Move-speed −20% for 1s | No (refreshes) |
| 4 | **Fire** | Burn + splash | DoT ~4%/sec for 3s + ~25% splash on adjacent target | No (refreshes) |
| 5 | **Poison** | Toxin | DoT ~2% max-HP/sec per stack for 4s, up to 5 stacks | **Yes** (locked stacking exception per handoff) |
| 6 | **Arcane** | Hex | Attack-speed / cast-speed −25% for 2s | No (refreshes) |
| 7 | **Divine** | Smite | +10% true damage vs Spirit & Colossal armor; reveals stealth (PvE only) | No |

### Enemy armor taxonomy

| # | Armor tag | Enemy archetypes (indicative) | Type attitude summary |
|---|-----------|-------------------------------|-----------------------|
| 1 | **Unarmored** | Common swarm, light infantry, civilians, lesser monsters | Weak to Slashing; resists Crushing |
| 2 | **Shielded** | Heavy infantry, armored elites, armored mini-bosses | Weak to Piercing & Crushing; resists Slashing & Divine |
| 3 | **Beast** | Myth monsters, wildlife, feral PvE | Weak to Fire & Poison; resists Arcane |
| 4 | **Spirit** | Undead, ethereal, magic-born | Weak to Arcane; resists Piercing & Fire |
| 5 | **Colossal** | Giants, titans, huge bosses | Weak to Divine; resists Poison |

*Enemy archetype roster itself is out of scope for this decision — Follow-up #3.*

### RPS matrix (attack type × armor tag)

| Attack ↓ / Armor → | Unarmored | Shielded | Beast | Spirit | Colossal |
|--------------------|-----------|----------|-------|--------|----------|
| Piercing | — | **+25%** | — | **−25%** | — |
| Slashing | **+25%** | **−25%** | — | — | — |
| Crushing | **−25%** | **+25%** | — | — | — |
| Fire | — | — | **+25%** | **−25%** | — |
| Poison | — | — | **+25%** | — | **−25%** |
| Arcane | — | — | **−25%** | **+25%** | — |
| Divine | — | **−25%** | — | — | **+25%** |

Coverage sanity per armor:
- Unarmored: 1 strong counter (Slashing), 1 hard counter-wall (Crushing). Symmetric.
- Shielded: 2 strong counters (Piercing, Crushing), 2 weak attacks (Slashing, Divine). Busiest — as expected for the "hard-armor" archetype; multiple answers exist.
- Beast: 2 strong counters (Fire, Poison), 1 weak attack (Arcane).
- Spirit: 1 strong counter (Arcane), 2 weak attacks (Piercing, Fire). Incentivizes magic investment.
- Colossal: 1 strong counter (Divine), 1 weak attack (Poison). Tight — bosses warrant Divine-coverage, Poison underperforms on the big stuff.

### Per-tower primary attack type (T1–T3, all 18)

#### Greek
| Tower | Type | Rationale |
|-------|------|-----------|
| Phalanx | **Piercing** | Dory spears, classic hoplite |
| Acropolis | **Crushing** | Stone-throwers, siege-platform |
| Oracle | **Arcane** | Prophecy / divination |
| Colossus | **Fire** | Bronze statue of Helios, solar / forge bronze |
| Trireme Dock | **Piercing** | Deck-archer fire + javelin (the ram is moot at land-based tower model) |
| Parthenon | **Divine** | Temple of Athena |

#### Aztec
| Tower | Type | Rationale |
|-------|------|-----------|
| Pyramid | **Divine** | Ceremonial center, god-channeling |
| Temple of the Sun | **Fire** | Solar rite, Huitzilopochtli |
| Jaguar Warrior Hall | **Slashing** | Obsidian-edged macuahuitl |
| Eagle Warrior Hall | **Piercing** | Atlatl + spear |
| Sacrificial Altar | **Poison** | Blood-rite / ritual toxin |
| Feathered Serpent Temple | **Arcane** | Quetzalcoatl wind / wisdom |

#### Norse
| Tower | Type | Rationale |
|-------|------|-----------|
| Longhouse | **Slashing** | Axe-militia baseline |
| Mead Hall | **Crushing** | Housecarl Dane-axes / mauls (differentiated from Longhouse) |
| Rune Stone | **Arcane** | Rune-magic |
| Longship Dock | **Piercing** | Raider javelins / bows |
| Berserker Lodge | **Slashing** | Axe-fury |
| Forge | **Fire** | Forge-fire / smelted damage |

#### Civ-level type coverage

| Civ | Types covered (T1–T3) | Types missing | Signature |
|-----|----------------------|---------------|-----------|
| Greek | P / C / A / F / D | Slashing, Poison | Divine + Crushing |
| Aztec | D / F / S / P / Po / A | Crushing | Poison + Divine |
| Norse | S / C / A / P / F | Poison, Divine | Slashing + Crushing |

No civ covers all 7 types unaided. Multi-civ play (patch-1 commanders, Foresight-coin) fills holes.

### Per-T4 Demigod primary attack type (all 18)

Demigods are assigned by **mythic fit** rather than strict T3-tower-inheritance, since their identity comes from the hero, not the tower of origin. Verified each assignment supports non-mono-type Gods (see next section).

#### Greek
| Demigod | Type | Rationale |
|---------|------|-----------|
| Achilles | **Piercing** | Pelian spear |
| Theseus | **Slashing** | Sword, Minotaur-slayer |
| Perseus | **Divine** | Divinely-equipped (Athena's shield, Hermes' sandals, Hades' helm) |
| Hercules | **Crushing** | Club, bare-hand strength |
| Odysseus | **Arcane** | Cunning / trickster-cleverness as damage archetype |
| Jason | **Divine** | Blessed-quest / Argonaut divine favor |

#### Aztec
| Demigod | Type | Rationale |
|---------|------|-----------|
| High Priest-King | **Divine** | God-king channel |
| Nanahuatzin | **Fire** | God-of-the-sun origin myth |
| Jaguar Champion | **Slashing** | Obsidian-edged claws |
| Eagle Champion | **Piercing** | Atlatl / talon |
| Blood Priest | **Poison** | Ritual toxin |
| Serpent-Priest | **Arcane** | Feathered-serpent wisdom |

#### Norse
| Demigod | Type | Rationale |
|---------|------|-----------|
| Björn Ironside | **Slashing** | Axe-raider |
| Beowulf | **Crushing** | Bare-hand-Grendel wrestling strength |
| Harald Bluetooth | **Divine** | Unifier-king, rune-stone builder |
| Leif Erikson | **Piercing** | Explorer-bow / spear |
| Lagertha | **Slashing** | Shieldmaiden sword |
| Sigurd | **Fire** | Dragon-slayer, bathed in dragon's blood |

### Per-God fusion damage profile (2-type, via locked recipes)

| Civ | God | Recipe (locked) | 2-type inherited | Thematic fit |
|-----|-----|-----------------|------------------|--------------|
| Greek | **Zeus** | Hercules + Jason | **Crushing + Divine** | Thunder + sky-father judgment |
| Greek | **Athena** | Theseus + Perseus | **Slashing + Divine** | Strategic warrior + wisdom-blessed |
| Greek | **Poseidon** | Achilles + Odysseus | **Piercing + Arcane** | Trident + sea-magic |
| Aztec | **Quetzalcoatl** | Serpent-Priest + High Priest-King | **Arcane + Divine** | Feathered-serpent + creator-god |
| Aztec | **Huitzilopochtli** | Nanahuatzin + Jaguar Champion | **Fire + Slashing** | Sun-war-god |
| Aztec | **Tezcatlipoca** | Blood Priest + Eagle Champion | **Poison + Piercing** | Night-trickster obsidian mirror |
| Norse | **Odin** | Harald Bluetooth + Leif Erikson | **Divine + Piercing** | Allfather + Gungnir spear |
| Norse | **Thor** | Björn Ironside + Beowulf | **Slashing + Crushing** | Hammer-&-axe (lightning deferred — see Follow-up #6) |
| Norse | **Tyr** | Lagertha + Sigurd | **Slashing + Fire** | Sword + sacrifice-fire |

**Verified:** every God has a 2-type pair (no mono-type collapses). All 7 types appear across the 9 Gods. Thor's lightning-association is a recipe-level consideration parked as Follow-up #6 — the taxonomy faithfully reads the recipe as locked.

## Reversibility note

Taxonomy shape (7 types, 5 armor tags, RPS skeleton) reversal would require:
- Rewriting all 18 tower entries, all 18 demigod entries, all 9 God damage profiles.
- Reworking the enemy armor taxonomy (Follow-up #3) once it lands against the new matrix.
- UI icon set rework (7 type icons + 5 armor icons).
- Any data-model or prototype code assuming the 7-type enum (prototype is currently frozen, so no cost there yet).

**Per-tower / per-demigod assignments** are inexpensive to flex inside the taxonomy shape — changing Phalanx from Piercing to Slashing is a one-line balance-pass tweak, does not reopen this decision.

**Per-God 2-type inheritance** flexes only via recipe change (PM-input-required — locked). Changing Thor from Slashing+Crushing to Arcane+Crushing requires reassigning Björn-or-Beowulf's primary type, which is a taxonomy-layer change.

**Magnitudes** ([+25%/−25%], DoT numbers, stagger durations) are entirely balance-layer; re-ratification in a balance pass does not reopen this decision.

## Follow-ups

1. **Balance pass** re-ratifies +25%/−25% magnitudes, DoT numerics, stagger duration, Poison stack cap, Divine smite %. Likely happens after prototype reshape lands and playtest data exists.
2. **Cultural-sensitivity pass** (mandatory gate on content lock — carried from 2026-04-25 ratification Follow-up #5) may flex specific type names (e.g., "Poison" on Aztec Sacrificial Altar — consider framing as "Ritual" or "Bloodletting" depending on consultation outcome; does not change taxonomy structure).
3. **Enemy archetype roster** populating the 5 armor tags — next design cluster after this decision lands. Each archetype gets 1–2 armor tags + a canonical HP/speed/behavior. Must not expand the armor-tag set without reopening this decision.
4. **Tier-2 / tier-3 tower-upgrade interaction with damage type**: locked as "primary type stays constant, upgrades increase proc intensity / add splash / add crit-on-proc". Explicit sub-decision deferred to balance pass.
5. **Fusion-combo emergent status procs** (e.g., Thor Slashing+Crushing synergy, Tyr Slashing+Fire synergy, Huitzilopochtli Fire+Slashing synergy — "burning plague" for Fire+Poison already suggested in handoff). Not in scope here; separate Gods-stats decision.
6. **Thor recipe reconsideration for lightning (Arcane)**: the locked Björn+Beowulf recipe produces Slashing+Crushing. If playtest shows Thor feels undersold without lightning, the recipe may be revisited by PM — which would also reassign Björn or Beowulf's primary type. Flagged only; no action this decision.
7. **CASCADE.md v0.20 → v0.21 bump** — next turn, same autonomous run.
8. **PROGRESS.md session-log row** — next turn after CASCADE.
9. **§2.4a accessibility-floor compliance check**: 7 type icons + 5 armor icons need colorblind-distinct glyphs. Downstream UI decision; no §2.4a text edit required from this decision.
10. **Cascade into `concept/phase-4.md §4.7`** (enemy direction is now RPS-matrix-constrained) — deferred to the real-cultures content cascade pass (Follow-up #1 from 2026-04-25 ratification).
11. **Prototype reshape** (post-cascade) will encode 7-type enum + 5-armor-tag enum + RPS matrix in `prototype/data/*.json`. Deferred.
