# Agent 5 — Competitor Design Teardowns (Wave 1)

**Scope:** Direct mechanical analysis of every named competitor against the AtoA north-star, with emphasis on Promise 2 (SC1/WC3 custom-lobby recognizability + customizability + novelty).

**Date:** 2026-04-27
**Agent:** 5 of 10, Wave 1

---

## Landscape — the genre's mechanical canon vs experimental fringe

The TW genre coalesced inside the SC1/WC3 custom map ecosystem between roughly 2002 and 2008, and almost every "must-have" mechanic in modern standalone TWs was first stress-tested in that lobby culture: maze-building (Burbenog/Element), per-tower upgrade trees, leaks-as-life-loss, wave compositions with armor/damage type rock-paper-scissors, send-mob-to-opponent income wars, and the king-defense / hero-tower hybrid that produced Legion TD. The **canon that survived into standalone Steam** is narrow — discrete tower placement, wave timer, gold + interest economy, leak penalty, and a small upgrade tree (Bloons, Kingdom Rush, Defense Grid all cleave to this). What **standalone TWs almost universally failed to reproduce** is the SC1/WC3 *lobby layer*: host-configurable rule mutators (resource multipliers, mode flags like "no-build", "all random fusion", boss-rush, free-for-all vs team), persistent-name room culture, and the tactile sense that the *next match could be a totally different game*. Legion TD 2 is the one near-exception, and even it locked the meta-rule set; Bloons did the opposite (rich content, frozen rules). The experimental fringe — Anomaly's reverse-TD, Sanctum's FPS-tower hybrid, Defenders of Ardania's 3-lane symmetric PvP, OTTTD's hero-party roguelite, Random Dice's deckbuilder-TD — proves that genre-bending sells niches but doesn't replace canon, and the recognizable SC1/WC3 *feel* (lobby chaos + hero-tower + send-units) has not been packaged into a single shippable Steam product. That gap is where Promise 2 lives.

---

## Per-competitor teardowns

### WC3 Customs

**Element TD (WC3)** — Six elemental towers, each summonable per-wave by spending essence; the core innovation was *combo towers* requiring two-element prerequisites, producing a build-order puzzle layered onto wave defense.
- ✓ Build-order as primary skill expression; elemental-combo tower lattice; difficulty selector at lobby.
- ✓ Replayable because element rolls per-wave randomized the optimal lattice.
- ✗ No PvP layer; no commanders / heroes; no send-unit income loop.

**Legion TD (original WC3 map)** — Symmetric 4v4 lanes; players spawn defensive *units* (not towers) at the start of each wave; income increases passively, and units fight an AI wave; surviving units roll into the next wave. Spawned the hero/king-defense hybrid and "send" economy.
- ✓ Send-unit-to-opponent income trade-off; persistent units between waves; team-vs-team meta with individual lanes.
- ✓ Hero unit (the king) created the WC3-style commander prototype.
- ✗ Build space was tight; no civ identity; balance was famously volatile across patches.

**Burbenog TD (WC3)** — Linear maze-build TD; players race for kill-count and rely on cooperative leak-coverage. Canonized "your maze, my problem" co-op pacing.
- ✓ Maze-builder freedom on an open grid; co-op leak rescue; visible kill-count leaderboard inside a single match.
- ✗ No PvP; no economy depth beyond gold/interest; no progression beyond the match.

**Vampirism (WC3)** — Asymmetric: humans build defenses while vampires hunt. The asymmetric horde-vs-builder format that horde-mode descendants still copy.
- ✓ Asymmetric roles inside one lobby; building-under-pressure pacing; vampire-vs-human as a recognizable mode tag.
- ✗ Not pure-TD; mechanics drift into survival — but the *recognizability* is what matters for Promise 2.

**Tower Wars (the WC3 map that named the genre)** — Symmetric send-units PvP; you build towers AND send creeps to your opponent's lane; the winner is whoever leaks the other first.
- ✓ The PvP-TW canon: send-creep economy, mirrored lanes, simultaneous build/send decisions.
- ✓ Lobby-level mutators (game speed, starting gold, mode flags) — exactly the customizability that vanished from standalone TWs.
- ✗ No persistent identity; no campaign; no commander progression.

### SC1 Customs

**Turret Defence (SC1)** — Earliest mass-popularized linear TD on Battle.net; minimal economy, pure leak-survival.
- ✓ Established the canonical "wave timer + gold per kill + interest + leak = life loss" loop.
- ✗ Almost no customization; no PvP send loop; lobby variants existed but weren't first-class.

**Warcraft-style TWs in SC1** — Knock-off ports of WC3 maps, mostly 1v1 send-creep races on small maps.
- ✓ Proved the send-creep PvP template was portable and addictive.
- ✗ SC1 engine couldn't carry the upgrade-tree depth WC3 had.

**Phantom Mode adjacents (SC1)** — Social-deduction overlay onto a defense lobby (a phantom player sabotages others). Lobby-culture artifact, not pure TW.
- ✓ Demonstrated that *social mode flags layered into a defense lobby* dramatically extend replay; a phantom toggle is a per-lobby identity flag, not a different game.
- ✗ Not a TW per se; relevance is the *lobby-mutator pattern*, which standalone TWs all dropped.

### SC2 Customs

**Squadron TD (SC2)** — Spiritual Legion-TD successor; per-wave unit spawn, income trade, send-unit pressure; arguably the highest-skill-ceiling TW ever made.
- ✓ Send-unit income economy; mercenary roster; round-by-round build identity; ranked ladder inside the Arcade.
- ✓ Lobby variants (chaos, all-random) that change identity per match.
- ✗ Buried in SC2 Arcade; never shipped standalone; lost to anyone outside the SC2 ecosystem.

**Element TD (SC2)** — Polished port of the WC3 map with cleaner UI; later spawned Element TD 2 standalone.
- ✓ Difficulty selector + element roll = match identity flag.
- ✗ Single-player-leaning; no PvP send.

**Income Wars (SC2)** — Pure send-creep PvP race; minimal building, maximal economic pressure.
- ✓ Distilled the send-economy mechanic to its essence.
- ✗ Too narrow to ship as a standalone — it's a *mode*, not a game.

### Standalone Steam

**Bloons TD 6** — The genre's commercial high-water mark; deep monkey roster, paragon late-game, co-op, daily challenges, robust modding (BTD6 Mod Helper community).
- ✓ Tower-roster depth; per-tower three-path upgrade tree; meta-progression (heroes, monkey knowledge); long content tail.
- ✓ Co-op lobby with shared economy.
- ✗ No PvP; no send-creep economy; rule-set is fixed match to match (challenge editor exists but is a niche feature, not lobby culture).

**Kingdom Rush series** — Polished hand-crafted level TD; hero units with abilities; tight tower roster.
- ✓ Hero-on-the-board mechanic — closest standalone analog to a WC3 commander.
- ✓ Per-level scripted set-pieces.
- ✗ No procedural variation; no PvP; no lobby; no customizability; campaign-finite.

**Legion TD 2** — Direct standalone successor to the WC3 map; ranked PvP, mercenary draft, send-unit income, strong esports-tier balance team.
- ✓ The single best modern translation of WC3-lobby PvP TW; it ships.
- ✓ Ranked ladder + Battle Pass.
- ✗ Locked rule-set — no host mutators; no civ/commander identity; one mode-shape; lobby chaos is gone.

**Element TD 2** — Standalone refinement of Element TD; campaign + endless modes.
- ✓ Element-roll match identity preserved.
- ✗ Single-player only at launch; minimal lobby culture.

**Cursed Treasure 2** — Inverted-TD (defend treasures from heroes); flash-game-tier polish on Steam.
- ✓ Flavor inversion as identity hook.
- ✗ No depth in lobby/PvP layer.

**Mindustry** — TD + factory automation hybrid; logistics-as-tower.
- ✓ Resource-routing as a tower-design axis; sandbox + PvP modes; modding community.
- ✗ Genre-adjacent; not recognizably a TW.

**Defense Grid (1/2)** — Pure tower placement on a maze-controllable grid; leak penalty is *core power cells stolen*, recoverable if you kill the carrier.
- ✓ Recoverable-leak mechanic — a unique experimental knob barely copied since.
- ✗ No PvP; no commander; rigid rule-set.

**Sanctum 1/2** — FPS + TD hybrid; you place towers AND shoot during waves.
- ✓ Player-as-active-defender layered onto TD; co-op.
- ✗ Genre-bender, not canon; small audience.

**Iron Marines** — Ironhide's RTS-TD hybrid; controllable hero squads on TD-ish maps.
- ✓ Commander-as-controllable-unit mechanic done well in standalone form.
- ✗ Campaign-only; no lobby; no PvP.

**Anomaly series** — Reverse-TD; you ARE the leaking convoy; player plans routes through enemy towers.
- ✓ Inversion as identity; proves the TD verb-set works backwards.
- ✗ Niche; not lobby-shaped.

**Defenders of Ardania** — 3-lane symmetric PvP TW with send-creep; a direct attempt to ship the WC3 Tower Wars formula standalone.
- ✓ Ambition was correctly aimed at Promise-2 territory.
- ✗ Universally panned for shallow content + no lobby mutators; the cautionary tale for "send-creep PvP isn't enough on its own."

**OTTTD** — Hero-party + TD; roguelite-flavored.
- ✓ Hero-party-as-towers experiment.
- ✗ Small footprint; didn't replicate.

### Mobile

**Bloons series mobile** — Same canon as BTD6; mobile-first monetization (premium upfront on BTD6, F2P with timers on Bloons TD Battles).
- ✓ Battles 2 has PvP send-bloons economy — closest mobile to the SC1/WC3 PvP TW shape.
- ✗ Battles 2 monetization was so aggressive it tanked goodwill; cautionary tale for Promise 3.

**Kingdom Rush mobile** — Original platform for the series; per-level hero unlock + iAP heroes.
- ✓ Hero gating as monetization without pay-to-win in PvE.
- ✗ No lobby; no PvP.

**Random Dice** — Deckbuilder-TD PvP; you roll dice that become towers; co-op and competitive.
- ✓ Deck-as-loadout PvP TD; daily-shifting meta via balance patches.
- ✓ Demonstrates that randomization-per-match (dice rolls) recreates *some* of the lobby-chaos feeling without explicit host mutators.
- ✗ Heavy gacha monetization; not a Steam-shippable shape under Promise-3 constraints.

---

## Aggregated findings

```
FINDING-1-05-01:
  CLAIM: Host-configurable lobby mutators (resource multipliers, mode flags, all-random toggles) are the single most consistent mechanic SC1/WC3 customs had that no standalone TW (except a partial Legion TD 2) reproduced.
  SOURCE: WC3 Tower Wars, SC2 Squadron TD lobby UI, Phantom Mode lobby pattern
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Bloons TD 6 has a Challenge Editor; Legion TD 2 has limited custom games — but neither exposes per-match rule reshaping as the default lobby flow.
  PROMISE-1 RELEVANCE: 2
  PROMISE-2 RELEVANCE: 5
  PROMISE-3 RELEVANCE: 1
  RELEVANCE NOTE: This is the literal definition of Promise 2's recognizability/customizability axis.

FINDING-1-05-02:
  CLAIM: The send-unit income economy (sacrifice gold to spawn creeps in opponent's lane for kill-bounty) is canonical to PvP TW and survives intact only in Legion TD 2 + SC2 Squadron TD.
  SOURCE: WC3 Legion TD, WC3 Tower Wars, SC2 Squadron TD, Legion TD 2
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Bloons Battles has a similar send-bloon loop, mobile-first.
  PROMISE-1 RELEVANCE: 4
  PROMISE-2 RELEVANCE: 4
  PROMISE-3 RELEVANCE: 2
  RELEVANCE NOTE: Necessary for PVP-Co-op promise coverage.

FINDING-1-05-03:
  CLAIM: Hero-on-the-board (a controllable, leveling unit alongside towers) is the core WC3 commander pattern, partially captured by Kingdom Rush + Iron Marines but never inside a customizable lobby.
  SOURCE: WC3 Legion TD king, Kingdom Rush heroes, Iron Marines
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE: 4
  PROMISE-2 RELEVANCE: 4
  PROMISE-3 RELEVANCE: 1
  RELEVANCE NOTE: AtoA's commander system stakes claim to ground that's been split between two competitor camps.

FINDING-1-05-04:
  CLAIM: Element / faction / civ rolls per-match (Element TD's wave-element randomization, Random Dice's deck dice) recreate "lobby chaos" feeling through procedural randomness when explicit host mutators aren't available.
  SOURCE: Element TD (WC3 + SC2), Element TD 2, Random Dice
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Players in the SC1/WC3 era preferred chosen mutators to imposed randomness.
  PROMISE-1 RELEVANCE: 2
  PROMISE-2 RELEVANCE: 3
  PROMISE-3 RELEVANCE: 1
  RELEVANCE NOTE: A fallback Promise-2 lever if explicit-mutator UI is too costly to ship.

FINDING-1-05-05:
  CLAIM: Maze-builder freedom (open-grid tower placement with player-shaped paths) was canonical to WC3 customs (Burbenog, Element TD's open variants) but was deliberately dropped by most standalone TWs in favor of fixed paths.
  SOURCE: Burbenog TD, Element TD WC3, Defense Grid (partial)
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Defense Grid kept maze-shaping; Bloons / Kingdom Rush deliberately dropped it for level-design tightness.
  PROMISE-1 RELEVANCE: 3
  PROMISE-2 RELEVANCE: 4
  PROMISE-3 RELEVANCE: 0
  RELEVANCE NOTE: Maze-build mode is a recognizable WC3-lobby tag the standalone genre vacated.

FINDING-1-05-06:
  CLAIM: Asymmetric-role lobbies (Vampirism, Phantom mode adjacents) extend replay enormously and are nearly absent from standalone TWs.
  SOURCE: WC3 Vampirism, SC1 Phantom variants
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Sanctum 2's co-op classes are a mild echo.
  PROMISE-1 RELEVANCE: 3
  PROMISE-2 RELEVANCE: 4
  PROMISE-3 RELEVANCE: 1
  RELEVANCE NOTE: Horde-mode coverage in Promise 1 can absorb this pattern.

FINDING-1-05-07:
  CLAIM: Recoverable-leak (Defense Grid's power-cell mechanic) is an underused experimental knob: leaks aren't permanent; the player can recover them by killing the carrier.
  SOURCE: Defense Grid 1 + 2
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Adds tension-management complexity that not all modes want.
  PROMISE-1 RELEVANCE: 2
  PROMISE-2 RELEVANCE: 2
  PROMISE-3 RELEVANCE: 0
  RELEVANCE NOTE: Candidate "dead niche mechanic worth resurrection" for one of AtoA's mode-types.

FINDING-1-05-08:
  CLAIM: Defenders of Ardania is the cautionary precedent: shipping a WC3-style PvP-TW standalone WITHOUT lobby mutators or content depth fails commercially.
  SOURCE: Defenders of Ardania (Steam reception, 2012)
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE: 3
  PROMISE-2 RELEVANCE: 5
  PROMISE-3 RELEVANCE: 1
  RELEVANCE NOTE: Validates that Promise 2 needs the FULL lobby + mode-coverage stack, not just send-creep PvP.

FINDING-1-05-09:
  CLAIM: Bloons TD 6 demonstrates that meta-progression (monkey knowledge, heroes, paragons) layered onto a frozen rule-set sustains long-tail engagement, but does not satisfy lobby-customizability hunger.
  SOURCE: Bloons TD 6 (Ninja Kiwi)
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Some players prefer the locked meta — easier to balance.
  PROMISE-1 RELEVANCE: 3
  PROMISE-2 RELEVANCE: 1
  PROMISE-3 RELEVANCE: 5
  RELEVANCE NOTE: Direct template for Promise-3's optional progression layered without compromising regular play.

FINDING-1-05-10:
  CLAIM: Random Dice and Bloons TD Battles 2 both prove that aggressive PvP-TW monetization (gacha, paywalled towers) corrodes audience trust quickly; mobile is a cautionary precedent for Promise 3's "no pay-to-win" stake.
  SOURCE: Random Dice, Bloons TD Battles 2 (Steam + mobile reception)
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Both still print money — commercial success != audience goodwill.
  PROMISE-1 RELEVANCE: 1
  PROMISE-2 RELEVANCE: 2
  PROMISE-3 RELEVANCE: 5
  RELEVANCE NOTE: Direct constraint on AtoA's Battle Pass design.

FINDING-1-05-11:
  CLAIM: Iron Marines (Ironhide) is the closest existing proof that controllable-hero-squad + TD verb-set is shippable in standalone form for a PvE audience.
  SOURCE: Iron Marines, Iron Marines Invasion
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: It's RTS-leaning; some players don't read it as TD.
  PROMISE-1 RELEVANCE: 4
  PROMISE-2 RELEVANCE: 2
  PROMISE-3 RELEVANCE: 1
  RELEVANCE NOTE: De-risks the hero-tower hybrid for Hero / PVE-Campaign mode-types.

FINDING-1-05-12:
  CLAIM: SC2 Squadron TD's lobby remains the unmatched ceiling for TW depth-per-match (per-wave merc draft, send-economy, ladder), and it never shipped outside Blizzard's Arcade — the audience is portable.
  SOURCE: SC2 Squadron TD (Arcade)
  STRENGTH: high
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Audience size at SC2 EOL was small; portability is uncertain in absolute terms.
  PROMISE-1 RELEVANCE: 3
  PROMISE-2 RELEVANCE: 5
  PROMISE-3 RELEVANCE: 3
  RELEVANCE NOTE: A directly addressable orphan audience for AtoA's Promise 2 pitch.

FINDING-1-05-13:
  CLAIM: Anomaly series proved reverse-TD ships standalone but stays niche; inversion is a flavor not a category.
  SOURCE: Anomaly: Warzone Earth, Anomaly 2, Anomaly Korea
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE: 1
  PROMISE-2 RELEVANCE: 2
  PROMISE-3 RELEVANCE: 0
  RELEVANCE NOTE: Reverse-mode could be a Custom-mode flag, not a mode-type slot.

FINDING-1-05-14:
  CLAIM: Kingdom Rush's hand-crafted level + scripted set-piece pacing is the gold standard for PVE-Campaign mode-type but is incompatible with procedural lobby chaos — they are different products glued at the spine.
  SOURCE: Kingdom Rush series (Ironhide)
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: BTD6's daily challenges blur the line slightly.
  PROMISE-1 RELEVANCE: 5
  PROMISE-2 RELEVANCE: 1
  PROMISE-3 RELEVANCE: 2
  RELEVANCE NOTE: Promise 1's PVE-Campaign needs a different production discipline from its custom-lobby modes.
```

---

## Open questions for the PM

1. **Which experimental mechanic from a dead/niche TW deserves resurrection in AtoA?** Defense Grid's recoverable-leak, Vampirism's asymmetric-role lobby, Anomaly's reverse-TD-as-mutator, and Phantom-mode social-deduction are the four strongest dormant candidates; recoverable-leak is the cleanest fit because it's a single tunable knob, while asymmetric-role would absorb most of Horde mode-type's design budget.

2. Is Promise 2's "lobby recognizability" satisfied by **explicit host mutators** (the SC1/WC3 way), **procedural per-match identity rolls** (the Element TD / Random Dice way), or both? The cost gap between these is large.

3. Does AtoA's Custom mode-type need to expose **modding hooks** (à la BTD6 Mod Helper or Mindustry) to fully claim Promise-2 territory, or is host-mutator UI sufficient at launch?

4. SC2 Squadron TD's orphan audience is real but small — is it a **target demographic** for AtoA marketing, or a **design-validation reference** only?

5. Defenders of Ardania is the explicit failure precedent for "ship WC3 PvP-TW standalone." What is AtoA's **content-floor commitment** to avoid the same thinness verdict — and is that floor reflected in the current Phase-4 scope?
