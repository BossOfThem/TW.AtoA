---
**Status:** Draft
**Last reviewed:** 2026-04-26
---

# Phase 3 — Design

*The shape of the game. High-level, not detailed.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-2.md](phase-2.md). Next: [phase-4.md](phase-4.md).

---

**Amendment banner — 2026-04-26 real-cultures frame cascade (§3.1 / §3.5 / §3.8 follow-on turn).** The 2026-04-25 ratification ([`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md), Reversibility Hard) replaced the "3 lineages (Ash / Nature / Prayer) × 3 tiers (Dust / Form / Apotheosis) under dungeon-cosmology arc" frame with **3 real-world civilizations (Greek / Aztec / Norse) × 4-tier-then-fusion ladder (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero → Fusion to God)**. Prior cascade turn rewrote §3.2 + §3.3. This turn rewrites **§3.1 (core match loop), §3.5 (tier arc), and §3.8 (exit condition)** to the new frame. Residual "lineage"/"Dust-Form-Apotheosis" traces in §3.4 and §3.6 are narrowed in-line. The debuff/magic mechanics surface referenced throughout is implemented by the 2026-04-26 attack-type mapping ([`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md)).

---

## 3.1 Core match loop (shared across all modes)

*→ active drill-down: [stage 03 — match setup](../stages/03-match-setup.md), [stage 04 — in-match core](../stages/04-in-match-core.md), [stage 05 — age evolution](../stages/05-age-evolution.md).*

A match proceeds through the **4-tier tower ladder** (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero) with an optional **Fusion endgame** (two T4 Demigods merge into a locked named God of the civilization's pantheon) per §3.5. Matches run on a **30-round cap**, with mini-bosses at rounds 5/15/25 and main bosses at rounds 10/20/30 per the 2026-04-25 ratification's locked pacing.

Between tiers, a **Tier Gate** pauses play and offers:
- Automatic advancement of existing towers to the next tier's form (T1 → T2 → T3 → T4 Demigod/Hero).
- A **Divergence Fork** at tier transitions (rescoped OPEN per §4.2 — at most 2 forks across the T1→T4 arc), presenting 2–3 path choices that re-skin future tiers.
- A marketplace of new towers/units unlocked by the advancing tier.

Combat within a tier uses standard tower wars mechanics: towers defend your lane, units attack enemy lanes (in PvP), economy drives everything. The **two-currency economy** (Tribute primary + Divinity mythic token, 6-cap/match) is specced in §4.x. Combat resolution runs through the **7-attack-type × 5-armor-tag RPS matrix + status procs** per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md).

The **Fusion endgame** sits outside the tier-gate sequence: once a player has two compatible T4 Demigods on the board and 2+ Divinity banked, the Fusion menu unlocks (2 Divinity to open + 1 per fusion). Fusion consumes both source Demigods into one God slot. A 30-round match with a 6-Divinity cap realistically yields 2–3 fusions — Gods are intentional rare events, not a routine late-game spam.

What makes this game different is what happens *between* tiers, the Fusion-to-God endgame, and the fact that your starting Commander choice persists as a visible identity through the entire mortal-to-mythic arc.

## 3.2 The Commander system (central feature)

*→ active drill-down: [stage 01 — commander pick](../stages/01-commander-pick.md), [stage 08 — meta progression](../stages/08-meta-progression.md). Backing research: [commander archetypes](../research/03-commander-archetypes.md).*

A **Commander** is the player's persistent identity in the game world. At first login, the player chooses a Commander from the launch roster — one legendary historical leader per launch civilization. Each Commander has:

- A distinctive visual identity (portrait, silhouette, color accent, voice) grounded in their historical culture.
- A thematic backstory drawn from history + native myth, usable as solo campaign framing.
- A **civilization affinity** — each Commander is tied to one of the three launch civilizations (Greek / Aztec / Norse) and has natural access to that civilization's full tower roster, unit roster, and Demigod/God fusion ladder. Cross-civilization tower access is parked as a future "Foresight-coin" mechanic.
- A **3-ability kit**: one passive + one short-CD active + one long-CD active. All nine ability names locked 2026-04-25 under "high-school recognizable" naming discipline (see table below).
- A **progression track** — XP, levels, unlocked cosmetics, voice lines, portrait frames.

Commanders level up through play. Towers in a match start at T1 swarm and progress through the tier ladder (T1 → T2 → T3 → T4 Demigod/Hero, then optionally Fusion to a named God) during that match. Commander progression is match-to-match meta. Tier progression is within-match tactical. These are two distinct progression systems operating at different timescales.

**Identity floor per commander** — see [§4.1](phase-4.md#41-commander-mechanical-spec-identity-floor-proposal-per-commander-writeup-open) for the minimum-shape spec (portrait + silhouette variants, voice lines, signature, passive, tilt, progression ladder, cosmetic slots). Entry: [2026-04-20 commander identity floor](../decisions/2026-04-20-commander-identity-floor.md) (rebased by [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) — **now Superseded by 2026-04-24 reopen**; re-rebase to [2026-04-25 real-cultures ratification](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) is tracked as 2026-04-25 Follow-up #10). Floor shape (portrait + silhouette + voice + passive + signature + progression + cosmetic slots) survives the reframing unchanged. Numerical floors are [PROPOSAL]; shape is committed.

**Launch commander roster (locked 2026-04-25):**

| Civ | Launch commander | Passive | Short-CD active | Long-CD active |
|-----|------------------|---------|-----------------|----------------|
| Greek | **Leonidas** | Spartan Training | This Is Sparta! | The Last Stand |
| Aztec | **Montezuma II** | Blood Tribute | Sun Offering | The Great Sacrifice |
| Norse | **Ragnar Lothbrok** | Sons of Ragnar | Berserk | The Great Heathen Army |

All nine ability names pass the "high-school recognizable" heuristic. Rejected in-session as too niche: Agoge, Molon Labe, Hot Gates. All numbers and full ability specs are [PROPOSAL] pending balance pass.

**Launch roster size: 3** (one per launch civilization). One additional commander per civilization planned for first post-launch patch (TBD — parked as 2026-04-25 Follow-up #6, requires PM direction). 3 is a lean-launch floor, not an expansion ceiling.

**"Civ affinity, not cage" principle:** a Greek commander plays Greek towers; cross-civilization borrowing is parked. This is a stronger cage than the prior "lineage tilt" frame — a civilization is a coherent thematic unit, not a mechanical tilt. Multi-civ play arrives via patch-1 commanders and the future Foresight-coin mechanic, not in-match mixing for the launch commanders.

## 3.3 The three civilizations (mechanical identity within a match)

*→ active drill-down: [stage 04 — in-match core](../stages/04-in-match-core.md).*

Each launch civilization has a coherent mechanical identity drawn from its native myth and history. Civilizations are the top-level *roster unit* — each civ owns 6 T1-T3 towers, 5 unit classes, 6 T4 Demigods/Heroes, and 3 Gods reachable via Fusion. Names locked 2026-04-25.

### Greek

- **Signature flavor:** Spartan discipline, phalanx, defensive anchor. Divine-heavy endgame via temple-and-oracle pantheon.
- **T1-T3 towers (6):** Phalanx, Acropolis, Oracle, Colossus, Trireme Dock, Parthenon.
- **Units (5):** Hoplite, Peltast, Hippeis, Toxotes, Krypteia.
- **T4 Demigods & Heroes (6):** Achilles, Theseus, Perseus, Hercules, Odysseus, Jason.
- **Gods (3, via locked Fusion recipes):** Zeus (Hercules + Jason), Athena (Theseus + Perseus), Poseidon (Achilles + Odysseus).
- **Attack-type coverage:** Piercing, Crushing, Arcane, Fire, Divine. No Slashing or Poison at tower-tier. (Per [2026-04-26 attack-type mapping](../decisions/2026-04-26-attack-type-mapping.md).)

### Aztec

- **Signature flavor:** Priest-warrior king, blood sacrifice, ritual. Poison and Fire native, Arcane via feathered-serpent wisdom.
- **T1-T3 towers (6):** Pyramid, Temple of the Sun, Jaguar Warrior Hall, Eagle Warrior Hall, Sacrificial Altar, Feathered Serpent Temple.
- **Units (5):** Macehualli, Jaguar Warrior, Eagle Warrior, Atlatl Thrower, Aztec Priest.
- **T4 Demigods & Heroes (6):** High Priest-King, Nanahuatzin, Jaguar Champion, Eagle Champion, Blood Priest, Serpent-Priest.
- **Gods (3):** Quetzalcoatl (Serpent-Priest + High Priest-King), Huitzilopochtli (Nanahuatzin + Jaguar Champion), Tezcatlipoca (Blood Priest + Eagle Champion).
- **Attack-type coverage:** Divine, Fire, Slashing, Piercing, Poison, Arcane. No Crushing at tower-tier.

### Norse

- **Signature flavor:** Raider-chieftain, sons-of-Ragnar, berserker fury. Slashing-heavy with rune-magic endgame and forge-fire.
- **T1-T3 towers (6):** Longhouse, Mead Hall, Rune Stone, Longship Dock, Berserker Lodge, Forge.
- **Units (5):** Viking Raider, Shieldmaiden, Huscarl, Berserker, Skald.
- **T4 Demigods & Heroes (6):** Björn Ironside, Beowulf, Harald Bluetooth, Leif Erikson, Lagertha, Sigurd.
- **Gods (3):** Odin (Harald Bluetooth + Leif Erikson), Thor (Björn Ironside + Beowulf), Tyr (Lagertha + Sigurd).
- **Attack-type coverage:** Slashing, Crushing, Arcane, Piercing, Fire. No Poison or Divine at tower-tier.

### Cross-civ coverage and the Fusion endgame

No civilization covers all 7 attack types unaided — Greek lacks Slashing/Poison, Aztec lacks Crushing, Norse lacks Poison/Divine. This is a feature: multi-civ play (via patch-1 commanders and the future Foresight-coin mechanic) fills the holes. At launch, each civilization is a coherent thematic unit with clear type-identity gaps that tell the player what to counter-pick.

**Fusion rule** (detail in [§4.3](phase-4.md#43-hybrid-combinations-the-signature-mechanic)): within a civilization, two specific T4 Demigods combine via a **locked recipe** into one named God. Each civilization has exactly 3 Gods and 3 recipes. Gods are the **only 2-type damage sources** in the game, inheriting both source Demigods' primary attack types. Fusion consumes the source Demigods into a single board slot and requires a **Divinity** currency spend (2 to unlock Fusion menu + 1 per fusion — see §4.x economy when specced). Across a 30-round match with a 6-Divinity cap, players realistically reach 2-3 fusions.

A player who ignores their civilization's T4/God ladder will miss the endgame identity of their civ. A player who fuses early and greedily will run out of Divinity for late-game flex. The game is built to reward **civ-appropriate escalation through the tier ladder**, not early-rush or late-cram.

**Open issue:** cross-civilization borrowing is parked as the future "Foresight-coin" mechanic. At launch, a Commander is locked into their civ's roster. Patch-1 adds one commander per civ (TBD). Specification of Foresight-coin economy + access rules deferred to post-launch (2026-04-25 Follow-up #7).

## 3.4 Unit categories (cross-cutting, not lineage-exclusive)

Units come in three categories:

- **Towers** — static placements. Attack within their range. Most tower-wars units are towers. Evolve through the ages.
- **Mobile units** — active units placed on the board that move along paths or patrol routes. Include melee front-liners, skirmishers, and hero-class units. Can be directed with waypoint-style commands, not full RTS micro.
- **Special effect units** — timed abilities, temporary zones, consumables, debuff fields. Cross-civilization (not civ-exclusive under the real-cultures frame); per-civ allocation is Phase 4 spec. Limited in placement count per match to avoid spam. Status-effect proc attachment (Burn splash, Bleed DoT, Toxin stacks, Hex, Smite, Armor-shred, Stagger) is driven by the source tower's attack type per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md).

The Commander, when deployed via signature ability, acts as a Hero Unit — a special high-value mobile unit with abilities. Only one Commander Hero per player on the map at a time.

## 3.5 The four-tier ladder + Fusion endgame (in-match tower evolution arc)

*→ active drill-down: [stage 05 — age evolution](../stages/05-age-evolution.md). Backing research: [theme & era](../research/02-theme-era.md).*

The structural backbone is a **4-tier tower ladder** with an optional **Fusion endgame**, compressing the mortal-to-mythic arc inside a single 30-round match. Each tier re-skins a civilization's towers; the heuristic is **"mundane outside, myth inside"** — T1-T3 read as culturally-recognizable real-world buildings (phalanx, pyramid, longhouse), T4 surfaces named Demigods/Heroes from native myth and history, Fusion produces named Gods of the civilization's pantheon.

1. **T1 — swarm.** Provisional openers. Many placements, low individual threat, civilization-legible at silhouette (shield-walls, stepped platforms, gabled halls).
2. **T2 — mainline.** The workhorse tier. Consolidated culture-specific forms; civilization identity fully readable.
3. **T3 — elite.** Signature tower-tier pieces. The roster's distinctive counters and specialists; late-mortal ceiling.
4. **T4 — Demigod / Hero.** Named mythic/historical individuals (Achilles, Nanahuatzin, Björn Ironside). Mortal-peak characters with proper-noun identity. Each civ has 6 T4s.
5. **Fusion — God.** Two specific T4 Demigods merge via a **locked recipe** into one named God (Zeus, Quetzalcoatl, Odin, etc.). Each civ has exactly 3 Gods. Gods are the **only 2-type damage sources** in the game, inheriting both source Demigods' primary attack types. Fusion gated by the **Divinity** currency (2 to unlock Fusion menu + 1 per fusion) — see §4.x.

This replaces the prior 3-tier Dust / Form / Apotheosis "dungeon-cosmology" arc and the preceding 11-age civilizational scaffolding, per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (superseding the [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md)). The arc is **not a timeline**; it is a compressed mortal-to-mythic escalation within one match. Per-tier biome / enemy / mapmod variety compresses into in-tier rotation pools; the [2026-04-20 age-history flavor + mapmods](../decisions/2026-04-20-age-history-flavor-mapmods.md) decision is rebased on that basis (logic survives; data collapses to the T1-T4+God shape). Re-rebase to the 2026-04-25 ratification is tracked as Follow-up #10.

Not every match reaches every tier. Match length and mode determine max tier reached — short solo missions may cap at T3; full Campaign and competitive modes reach T4 and routinely land 2–3 Fusions. Fusion is intentionally rare (6-Divinity cap × 1-per-fusion cost after a 2-Divinity unlock), not a routine late-game spam. This is a design lever, not a bug.

Early tiers are short and brittle. Late tiers are longer and more strategic. Fusion moments are the trailer-beats. Total playtime stays within mode target (30-round cap).

**Tier-level mechanical identity** (what *feels* different between T1 / T2 / T3 / T4 / Fusion beyond cosmetic re-skin) is owed to Phase 4 (§4.2 divergence, §4.3 Fusion system, §4.7 enemy system under the real-cultures frame) and Phase 5 (§5.1 MVP, §5.3 art direction — "stylized vector for T1-T3, silhouette-forward mythic for T4 / Gods"). Attack-type identity per tier is locked per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md).

## 3.6 Game modes (launch roster)

*→ active drill-down: [stage 02 — mode select](../stages/02-mode-select.md). Backing research: [genre pulse](../research/01-genre-pulse.md).*

1. **Solo Campaign** — story missions tied to each Commander (Leonidas, Montezuma II, Ragnar Lothbrok). Progresses through the tier ladder (T1 → T2 → T3 → T4 → Fusion). Introduces mechanics gradually. Non-negotiable at launch. This is how the solo promise is kept.
2. **Solo vs AI (Skirmish)** — pick map, difficulty, civilization restrictions. Quick game against AI.
3. **Co-op Horde** — 2–4 players defend shared lanes against escalating waves. User-hosted or matchmade.
4. **Lane Wars 1v1** — classic competitive tower wars PvP.
5. **Lane Wars 2v2** — team PvP, matchmaking or party.

**Post-launch expansion (not at launch):**
- **Hero Line Wars** — hero-controllable extended mode. Builds on the signature ability system.
- **Ranked** — competitive laddered play with seasons.
- **Custom modes** — community-driven, tied to modding support if we add it.
- **Roguelite TD** — single-player run-based mode that borrows TTA concept ideas.

## 3.7 Meta systems (between-match progression)

*→ active drill-down: [stage 07 — match end](../stages/07-match-end.md), [stage 08 — meta progression](../stages/08-meta-progression.md). Backing research: [monetization & live-ops](../research/04-monetization-liveops.md).*

1. **Commander progression** — XP, levels, unlocks (cosmetics, voice lines, commander passive tiers, signature ability tiers).
2. **Backpack / Inventory** — gifts, evolution components, consumables, cosmetic items. Earned through play or events. Inventory UI in main menu.
3. **Battle Pass** — seasonal progression track. Free tier earnable by playing. Premium tier unlocked by purchase, rewarding cosmetics only (never gameplay power).
4. **Cosmetic Store** — skins, emotes, commander voice packs, map tints. Never sells gameplay advantage.

## 3.9 Meta-UI surfaces (launch envelope)

*Decision entry: [2026-04-20 meta-UI envelope](../decisions/2026-04-20-meta-ui-envelope.md). Reversibility: Easy.*

The intro-game and in-match flows surface at minimum:
- **Options** menu, reachable from both main menu and in-match Pause overlay.
- **Pause overlay** mapped to `Esc` whose contents differ by mode.
- **Quit / Save-and-Exit / Concede** path appropriate to mode.

Mode-aware split:

| Mode | Esc | Pause contents | Restart | Save | Quit |
|------|-----|----------------|---------|------|------|
| Solo Campaign | Hard pause | Resume / Options / Restart Mission / Save-and-Exit / Quit-to-Menu | Allowed | Save-and-Exit (mid-mission) | Confirm if unsaved |
| Solo Skirmish | Hard pause | Resume / Options / Restart / Quit-to-Menu | Allowed | Auto-save on end | Confirm if mid-match |
| Co-op Horde | Host-pause, vote-or-timeout (principle; spec deferred) | Resume / Options (local) / Concede / Quit-to-Menu | Disabled | Auto-save on end | Concede |
| Lane Wars 1v1 / 2v2 | Read-only overlay (state runs; local menus open) | Options / View Build / Concede / Quit-to-Menu | Disabled | None | Concede + leave |

Principle: competitive integrity > solo convenience. Exhaustive per-setting list deferred to Phase 5.

## 3.10 Audio architecture

*Decision entry: [2026-04-20 audio architecture](../decisions/2026-04-20-audio-architecture.md). Reversibility: Easy.*

5-bus mixer: **Master, Music, SFX, UI, Voice**. Voice bus sidechain-ducks Music and SFX during playback. Focus-loss behavior: mute Music + ambient SFX in solo modes by default; leave audio running in competitive PvP by default (no alt-tab audio-cue advantage). Both behaviors user-overridable in Options. Per-bus slider UI, ducking threshold/ratio/release numbers, and per-channel content (SFX inventory, music tracks, voice lines) are Phase 5.

## 3.11 First-run and returning-player flow

*Decision entry: [2026-04-20 first-run flow](../decisions/2026-04-20-first-run-flow.md). Reversibility: Easy. Full per-screen spec owner: [stages/00-session-start.md](../stages/00-session-start.md).*

**First-run path** (no save): launch → splash (≤3s, skippable) → main menu (first-time variant, no Continue) → New Game → Commander Pick → Tutorial with skip option ("I've played Tower Wars before — skip") → match. Tutorial completion incentivized via cosmetic reward (funded by the §4.1 identity-floor cosmetic slot), not gated.

**Returning-player path** (save detected): launch → splash (skippable) → main menu (returning variant, prominent Continue) → Continue routes to last in-progress state.

**Click budget [PROPOSAL]:** ≤6 clicks from launch to in-match for first-time; ≤3 clicks for returning.

Tutorial style: **contextual + interactive + skippable**, not pop-up-based. Per-screen spec is Phase 5 (stage 00 + stage 01).

## 3.8 Exit condition for Phase 3

The shape of the game can be drawn on a whiteboard in five minutes: **3 commanders (Leonidas / Montezuma II / Ragnar Lothbrok), 3 civilizations (Greek / Aztec / Norse), a 4-tier tower ladder (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero) with a locked Fusion endgame (2 T4 Demigods → 1 named God, 9 Gods via 9 locked recipes), 3 unit categories, 5 launch modes, 4 meta systems, a 2-currency economy (Tribute + Divinity), and a 7-attack-type × 5-armor-tag combat matrix**. Nothing in Phase 4 introduces a new system that contradicts Phase 3.

→ **Hand off to [Phase 4](phase-4.md).**
