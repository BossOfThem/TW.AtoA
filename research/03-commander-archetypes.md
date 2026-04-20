# Research 03 — Commander / Hero Archetype Appeal

**Status:** Draft
**Feeds into:** [Stage 01 — commander pick](../stages/01-commander-pick.md), [Stage 08 — meta progression](../stages/08-meta-progression.md)
**Methodology:** [00-methodology.md](00-methodology.md)
**Last reviewed:** 2026-04-20

---

## Purpose

Which hero fantasies are players repeatedly picking in live-service games across 2024–2026? How should that shape our starter roster size (3/5/8) and archetype slots? This doc writes *before* [Stage 01](../stages/01-commander-pick.md). Stage 01 depends on the matrix below.

Scope note: Commander = player's persistent identity across matches (first-person). An archetype here is a *fantasy label* (scholar-exile, warmother, trickster-courier), not a mechanical kit. Kits slot under lineages (Sinew / Ember / Forge / Crown / Veil).

---

## 1. Reference rosters mined

Six titles carry the weight of this survey. I prioritized live games with public pick-rate data (Tier 1/2) over titles where I'd have to rely on vibes.

**Overwatch 2 (Blizzard, 2022–2026).** Launched 2016 with 21 heroes and has slowly tripled the roster. In the September 2025 competitive snapshot, the newly released support Wuyang hit ~56% pick rate, with Kiriko, Reinhardt, Orisa, Ana, Mercy, and Cassidy rounding out the most-picked slots *(Fenixbazaar, "Overwatch 2 Hero Pick Rates guide for September 2025", retrieved 2026-04; Blizzard, "Overwatch Hero Statistics", retrieved 2026-04)*. Signal: the most-picked hero at any given time is often the *newest* — novelty dominates — but the durable mainstays (Reinhardt, Ana, Mercy) are emotional anchors, not power picks. Two are middle-aged women. One is a grandmother.

**Valorant (Riot, 2020–2026).** VCT Stage 2 2025 had Omen as the most-picked agent in *all four* regions, with 74–86% pick rates, and Sova/Viper alternating second across regions *(Esports Insider, "VCT reveals most-picked VALORANT Agents from Stage 2", retrieved 2026-04; VLR.gg, VCT 2025 agent stats, retrieved 2026-04)*. Omen and Viper are older, weathered, morally sketchy figures — not the shiny new agents marketing leans on. Durable picks skew *adult and compromised*, not *young and eager*.

**Marvel Rivals (NetEase, 2024–2026).** Launched Dec 2024 with **33 heroes**, all free — an unusually large opening hand versus Overwatch's 21 at launch or Apex's 8 *(Inverse, "Marvel Rivals Roster: All 33 Characters Playable at Launch", retrieved 2026-04)*. First-half Season 7 pick rates: Cloak & Dagger, Invisible Woman, Doctor Strange, Magneto top competitive; Jeff the Land Shark, Gambit top Quickplay *(Dexerto, "Most popular Marvel Rivals characters", retrieved 2026-04; MitchCactus, "Marvel Rivals Competitive Hero Pick Rates August 2025", retrieved 2026-04)*. Jeff — a tiny land shark — is a top-5 Quickplay pick. Lesson: readable silhouettes and charm beat "coolness" in casual modes. The least-picked list (Deadpool, Human Torch, Blade, Black Widow) is largely the *most predictable* archetypes — brooding vigilante, flaming flyboy, spy-girl-in-catsuit. Saturation penalty.

**League of Legends (Riot, 2024–2026).** Roster at 172 champions by late 2025 with a measured three-per-year cadence *(LoLBoost.gg, "Newest LoL Champions 2025", retrieved 2026-04; League of Legends Wiki champion list, retrieved 2026-04)*. 2025 releases — Mel, Yunara, Zaahen — fill deliberate identity gaps rather than fantasy duplicates. K'Sante (2022) and Ambessa Medarda (2024) are repeatedly cited as Riot pushing roster diversity in ethnicity, queerness, and age *(Esports-Insights, "The Evolution of League of Legends Champion Design: A Look at the 2024 Roster", retrieved 2026-04; freshness flag — 2024)*.

**Hades II (Supergiant, 2024–2026 EA).** Protagonist Melinoë, a witch-princess, received broadly positive critical reception (Rolling Stone, Destructoid) though Steam threads surface a small but loud cohort demanding a male alternative *(Wikipedia, "Melinoë (Hades)", retrieved 2026-04; Steam Community discussions, Tier 3 sentiment flag)*. Signal: a non-combat-coded female lead in a combat game ships fine commercially; the loudest forum reaction is not the revealed preference.

**Warcraft Rumble (Blizzard, 2023–2026).** Leaders-as-commanders model directly analogous to our use case. Community-consensus strong leaders — Baron Rivendare, Rend Blackhand, Tirion Fordring, Maiev Shadowsong, Cairne Bloodhoof *(Dot Esports, "Warcraft Rumble Leaders tier list", retrieved 2026-04; Tier 2)* — span undead lord, orc warlord, paladin-king, night elf warden, tauren elder. No two share an archetype. The roster is *fantasy-silhouette-diverse* even when mechanically narrow.

**Briefly referenced, not mined deep:** Apex Legends (8 at launch, gradually adding across gender/sexuality/age), Clash Royale Champions (seven champion-rarity cards by Oct 2024, deliberately slow cadence; Tier 2 *SportsKeeda, "Clash Royale October 2024 update"*), Mechabellum and Stormgate (commander systems still maturing, limited public pick data — Tier 3 only), Deadlock (Valve closed beta, no reliable public pick data — excluded).

### So-what for this game

**Loop 3 synthesis.** Durable-pick patterns point one direction and novelty-pick patterns point another, and we need to design for the durable one. Across Overwatch, Valorant, and Marvel Rivals the heroes that *stay* picked after the novelty window are the adult, morally complicated, silhouette-distinct ones — Reinhardt, Ana, Omen, Doctor Strange, Invisible Woman. The heroes that crater are the ones who share fantasy space with too many peers — brooding vigilantes, spy-girls-in-catsuits, flaming flyboys. Warcraft Rumble and Clash Royale confirm the corollary at small roster sizes: if you only get to ship a handful, make sure *no two share a silhouette*. Caveat: pick rate in a PvP shooter is not a perfect analog for Commander pick in a tower-defense-adjacent game — our pick is persistent identity, not per-match optimization — so we should weight *emotional durability* over *meta optimality* more heavily than these sources do.

---

## 2. Per-commander attributes (observed)

Compressed table of the most-picked / most-durable figures across the mined rosters. Pick-rate columns only populated where Tier 1/2 data exists.

| Game | Character | Fantasy label | Gender / age band | Power trope | Tonal register | Pick-rate signal |
|------|-----------|---------------|-------------------|-------------|----------------|------------------|
| OW2 | Reinhardt | Old knight | M / 60s | Shield + hammer | Earnest, bombastic | Durable top-tier tank, all seasons |
| OW2 | Ana | Sniper-grandmother | F / 60s | Biotic rifle | Weary, wry | Top support in QP S18 |
| OW2 | Mercy | Angel-medic | F / 30s | Heal beam + flight | Earnest, tragic | Casual-skewed top |
| OW2 | Kiriko | Fox-spirit healer | F / 20s | Heal + dash + kunai | Playful, confident | Top-2 support competitive |
| OW2 | Wuyang | Cloud-summoner support | M / adult | Water/wind | Serene | ~56% novelty pick S18 |
| Valorant | Omen | Wraith / regretful phantom | M-coded / indeterminate | Shadow/teleport | Grim, poetic | 74–86% VCT Stage 2 |
| Valorant | Viper | Embittered chemist | F / 40s | Poison/area denial | Cynical, cold | #2 in Americas/Pacific |
| Valorant | Sova | Hunter-tracker | M / 30s | Recon arrows | Earnest-stoic | #2 EMEA/China |
| Rivals | Cloak & Dagger | Paired-duality healer | M+F / 20s | Light/dark combined | Romantic, melancholic | Top competitive |
| Rivals | Invisible Woman | Maternal force-field | F / 40s | Barriers, invisibility | Matriarch, composed | Top competitive |
| Rivals | Doctor Strange | Sorcerer-scholar | M / 40s | Portals, wards | Arrogant, burdened | Top competitive |
| Rivals | Jeff | Tiny absurd beast | Animal | Swallow/heal | Comedic | Top QP |
| Hades II | Melinoë | Witch-princess | F / young adult | Witchcraft, arcana | Disciplined, studious | N/A, single-PC |
| Rumble | Tirion Fordring | Paladin-king | M / old | Holy warrior | Solemn, messianic | Community top tier |
| Rumble | Maiev Shadowsong | Obsessed warden | F / old (night elf) | Glaive, stealth | Vengeful, cold | Community top tier |
| Rumble | Baron Rivendare | Undead lord | Undead M | Necromancy | Grim camp | Community top tier |
| Rumble | Cairne Bloodhoof | Tauren elder | M / very old | Nature, totem | Dignified, warm | Community top tier |

Patterns that jump out:

- **Age skews older than marketing does.** The durable top tiers are disproportionately characters aged 40+, with many explicitly elderly (Reinhardt, Ana, Cairne, Tirion).
- **Duality and burden appear repeatedly.** Cloak & Dagger, Omen, Doctor Strange, Melinoë, Maiev — characters carry something. "Cheerful chosen one" is rare at the top.
- **Comedic / absurd silhouettes carry casual modes.** Jeff, Lucio, the Goblin-family Clash evolutions. Do not under-ship at least one.
- **"Anime sword girl" is missing from the durable-picks column almost everywhere.** The ones that exist (Yone, Yasuo, Genji-adjacent) are high-novelty, polarizing picks — loud floor but not durable ceiling.

---

## 3. Over-represented archetypes to AVOID

These are the silhouettes every hero-based game ships and every hero-based game's tail-end heroes embody. If we ship one, it should be *heavily* differentiated on at least two axes (age, species, lineage tilt, or tonal register).

1. **The gritty male soldier (Sinew-default).** Present in every hero shooter since Team Fortress 2. Soldier 76, Brimstone, The Punisher, Gragas-with-a-gun. Marvel Rivals' launch roster's least-picked list leans on exactly this silhouette *(MitchCactus pick-rate data, 2025)*. Pattern: audiences *respect* the archetype and do not *adopt* it as identity.
2. **The anime swordmaiden / twin-blade duelist.** Valorant has no agent in its top-3 durable picks who fits this mold; Rivals' Psylocke and Magik underperform the average; League's Fiora-shaped niche is sustained but small. "Cute girl with sword" is a saturated fantasy *(sentiment, Reddit/YouTube discourse; Tier 3 — treat as direction, not verdict)*.
3. **The chosen-one orphan youth.** Overused across JRPGs and gacha. Players report trope fatigue; no durable top-tier character in the mined multiplayer rosters actually is one. Novelty heroes that lean chosen-one (various LoL releases 2022–2023) have underperformed Riot's internal stickiness bar *(freshness flag — inferred from release cadence shift toward Mel/Ambessa; Tier 2/3 hybrid)*.
4. **The scruffy scoundrel / space cowboy.** Cassidy, Chamber, Star-Lord, half of every indie rogue-like protagonist. Individually some are fine; *collectively* they are the default male-ranged archetype. Ship at most one, and only if he carries on an additional axis.
5. **The edgy cloaked assassin man.** Reaper, Yoru, Moon Knight, every ninja in every game. Consistent bottom-half pick rate in Rivals (Deadpool / Blade cluster).
6. **The "sexy elf ranger."** Evelynn-shaped. Ships constantly, sells skins, does not become anyone's persistent identity.

### So-what for this game

**Loop 3 synthesis.** Avoid-lists are easier to write than to hold. The honest steelman is that these tropes are over-represented *because* they work — a gritty soldier and a ninja and a cowboy will each reliably fill a niche and can be differentiated at the kit level. The aggressive critique is that at a 5-Commander starter roster we literally cannot afford any slot to be filled by "fine." Synthesis: we treat this list as a **silhouette-exclusion filter, not a content-exclusion filter**. The archetype can reappear if and only if it's transformed on two axes — e.g., the "gritty soldier" fantasy can live on our Sinew slot only if the commander is, say, a 60-year-old farming matriarch who once led a siege, not a jawlined sergeant. Caveat: this is easier to assert than to execute; we will drift back to defaults under schedule pressure unless the exclusion filter is written into the character brief template.

---

## 4. Under-represented archetypes with APPETITE

Where is the appetite the saturated roster isn't feeding?

1. **Older protagonists (40+, 60+, grandparent-coded).** God of War (2018) Kratos, RDR2 Arthur Morgan, TLoU Joel — the stoic-older-man pattern has been the most critically and commercially durable narrative archetype of the last decade *(GameRant, "Arthur Morgan, Kratos, and Geralt... Common Ancestor", retrieved 2026-04; Tier 2)*. Multiplayer has under-served this — Ana, Reinhardt, Invisible Woman each prove the appetite is *there* in ensemble formats too. The female-elder slot (Ana-type) is unusually empty.
2. **Queer leads — explicit, not coded.** GLAAD's 2024 Gaming Report: under 2% of console releases have LGBTQ content despite 17% of active players identifying as queer; LGBTQ players are **4–5× more likely** to buy a game because of a queer lead; 72% of LGBTQ players (78% of 13–17-year-olds) report seeing queer characters improves wellbeing *(GLAAD, "2024 GLAAD Gaming Report: The State of LGBTQ Inclusion in Video Games", retrieved 2026-04; Variety coverage of same report; Tier 1/2)*. Business case is unusually clear-cut. Riot explicitly cites K'Sante as a representation milestone.
3. **Parent-figures (not orphan-figures).** Kratos-as-father, Joel-as-father, Ellie-as-protector. Invisible Woman in Rivals. Ana in OW2. Reinhardt-as-mentor. A Commander who is explicitly *someone's mother / teacher / grandparent* is rare in strategy rosters and stickier than expected when it lands.
4. **Non-human commanders that aren't cute mascots.** Warcraft Rumble's undead Baron, tauren elder, and arachnid Gazlowe-adjacent picks all reach top tier *(Dot Esports leaders tier list, retrieved 2026-04)*. Jeff proves cute-beast works, but there's a second axis — *dignified non-human elder* — that is strikingly empty across the mined rosters.
5. **Bureaucrats, scholars, clerks, accountants in fantasy clothing.** The Forge lineage almost begs for this. Doctor Strange's durable appeal is partly that he reads as an academic in armor. Almost no multiplayer roster ships a "logistics officer as hero" and those who try (Brigitte-as-engineer, Rampart in Apex) land surprisingly well.
6. **Absurd-but-earnest characters.** Jeff is the canonical case. One per roster. Don't ship zero.

### So-what for this game

**Loop 3 synthesis.** The market gaps are wide enough that *playing to them is the safer move than playing against them*. Aggressive critique first: "appetite" data from GLAAD is attitudinal, and stated preference doesn't always translate to revealed preference in a tower-defense game where Commander pick is downstream of lineage mechanics, not identity marketing. Steelman: the Ana / Reinhardt / Invisible Woman / Kratos evidence is *revealed* preference at the largest available scale, and our Commander-as-persistent-identity design makes identity resonance more load-bearing than in a PvP shooter, not less. Synthesis: deliberately seed the starter roster with (a) at least one commander 50+, (b) at least one explicitly queer commander, (c) at least one non-human-but-dignified commander, (d) one absurd-earnest commander. These are not quotas; they are exclusion *from* the default. Caveat: execution matters — tokenized older/queer/non-human characters are worse than shipping fewer commanders well. Character briefs must write identity into behavior, not into bio-text.

---

## 5. Archetype × lineage matrix

Scoring is 1–5 on each axis. **Market** = evidence of appetite from §1–4. **Fit** = how cleanly the fantasy reads as that lineage's tilt (Sinew/Ember/Forge/Crown/Veil per CONCEPT §5.4). **Diversity** = contribution to roster diversity *assuming one commander per lineage*. Candidates are intentionally over-generated — this is a selection menu, not a shortlist.

| # | Candidate archetype (placeholder) | Lineage tilt | Market | Fit | Diversity | Notes |
|---|---|---|---|---|---|---|
| A1 | Warmother — 60-year-old former siege-captain, grandmother, still carries the hammer | Sinew | 5 | 5 | 5 | Ana+Reinhardt composite. Anchor pick. |
| A2 | Gritty-male-soldier (default) | Sinew | 2 | 4 | 1 | Avoid per §3. |
| A3 | Farm-boy orphan-hero | Sinew | 2 | 3 | 1 | Avoid per §3. |
| A4 | Tauren-coded elder (non-human, dignified) | Sinew | 4 | 4 | 5 | Rumble evidence strong. Ships as alternative to A1. |
| B1 | Scholar-exile — middle-aged academic, arcane specialty, burdened | Ember | 5 | 5 | 4 | Doctor-Strange-shaped. Ember's anchor. |
| B2 | Chosen-child prodigy mage | Ember | 2 | 4 | 1 | Avoid per §3. |
| B3 | Queer inventor-technologist, 30s, cheerful | Ember | 4 | 4 | 5 | Pairs with B1 as alternative, not both. |
| B4 | Anime swordmaiden "battle-mage" | Ember | 2 | 2 | 1 | Avoid per §3. |
| C1 | Guild-master — logistics officer in fantasy clothing, 40s, parental | Forge | 4 | 5 | 4 | Invisible-Woman-shaped, bureaucrat-as-hero. Forge anchor. |
| C2 | Scruffy merchant-scoundrel | Forge | 2 | 3 | 2 | Partial avoid per §3. |
| C3 | Dwarven foundry-master, non-human, queer-coded | Forge | 4 | 5 | 5 | Alternative to C1. |
| C4 | Child-inventor prodigy | Forge | 2 | 3 | 2 | Trope-adjacent. |
| D1 | Paladin-king — older, messianic, burdened | Crown | 5 | 5 | 3 | Tirion-shaped. Crown anchor. |
| D2 | Teenage princess prodigy | Crown | 2 | 3 | 1 | Avoid per §3. |
| D3 | Saint-matron — older female religious leader | Crown | 5 | 5 | 5 | Pairs as Crown alternative; gender-flips D1 which is the stronger lean. |
| D4 | Warlord-conqueror (Ambessa-shaped) | Crown | 4 | 4 | 4 | Works if not overlapped with A1. |
| E1 | Trickster-courier — queer, 30s, charming, non-lethal toolkit | Veil | 5 | 5 | 5 | Omen+Cloak&Dagger composite. Veil anchor. |
| E2 | Edgy cloaked assassin man | Veil | 1 | 4 | 1 | Avoid per §3. |
| E3 | Fox-spirit trickster (non-human, mischievous) | Veil | 4 | 5 | 4 | Kiriko+Jeff-adjacent. Charm pick. |
| E4 | Haunted phantom, morally grey | Veil | 5 | 5 | 3 | Omen-shaped. Strong but overlaps with B1's burden tone. |

Per-lineage anchor recommendations (top scorer × diversity tiebreak):

- **Sinew:** A1 (warmother).
- **Ember:** B1 (scholar-exile).
- **Forge:** C1 or C3 (guild-master or dwarven foundry-master); C3 scores higher on diversity.
- **Crown:** D1 (paladin-king) or D3 (saint-matron) — these are near-tied; pick one to avoid two "older religious figure" slots on roster.
- **Veil:** E1 (trickster-courier).

If the PM wants the absurd-earnest slot (Jeff-shaped), E3 (fox-spirit trickster) is the cleanest home for it — Veil tilts playful naturally.

---

## 6. Roster-size recommendation — 3 / 5 / 8

**[PROPOSAL — not locked. Requires PM ratification before Stage 01 drafts.]**

Evidence:

- **Launch-roster benchmarks.** Apex shipped 8. Overwatch shipped 21. Marvel Rivals shipped 33. Clash Royale's *champion* rarity — the closest structural analog to our Commander tier — sits at 7 after four years *(Clash Royale Wiki champion cards, retrieved 2026-04)*. Warcraft Rumble launched with ~8 viable leaders. Mechabellum launched with a handful of commander units *(freshness flag, Tier 3 coverage)*.
- **Two-dev content budget.** Each Commander needs: silhouette art, portrait variants, voice lines, a kit that integrates cleanly with Sinew/Ember/Forge/Crown/Veil, balance passes every patch, a Stage 08 meta-progression tree, and Stage 01 readability. Realistic one-Commander content cost at our staffing is weeks, not days.
- **First-pick cognitive load.** Overwatch research and Riot champion-select studies both repeatedly surface "new player overwhelm" at rosters above ~8 for a *first* pick *(sentiment + internal-post references; Tier 3 — treat as direction)*. At 3 the choice is trivial; at 5 it is a readable wheel; at 8 it starts to require filtering UI.
- **One-per-lineage cleanliness.** We have 5 lineages. 5 Commanders maps perfectly. 3 forces three lineages to share Commanders or go un-headed. 8 forces some lineages to have duplicates at launch, creating a "my Sinew is better than your Sinew" balance problem out of the gate.

**Proposal: 5 at launch, one per lineage. Grow to 8–10 over the first two content seasons.** This is the option where launch identity is cleanest, content budget is achievable, cognitive load for first pick is manageable, and the diversity recommendations from §4 can *all* be seeded into the starter five rather than deferred to later patches.

**Reversibility.** This is a structurally reversible choice in both directions, but asymmetrically:

- *Adding* Commanders post-launch is the standard live-service motion. Low reversal cost. We expect to do this regardless.
- *Removing* Commanders post-launch is extremely painful — players who have progressed Stage 08 trees for a commander treat deletion as theft. High reversal cost.
- Implication: err toward **shipping fewer, not more**. If we are uncertain between 5 and 6 at launch, ship 5.
- Structurally, picking 5 now does not foreclose 3 or 8 later — 3 is a subset of 5, and 8 is an additive expansion of 5. Picking 8 now and trying to retreat to 5 is the only materially one-way decision.

**Named caveats the PM should weigh before ratifying:**

1. Five forces us to commit one commander per lineage. If Forge's best candidate in playtest is much weaker than Sinew's, we cannot compensate by just shipping two Sinews. This is a feature (clean identity) but is also a constraint (no balance-through-quantity).
2. The "one absurd-earnest" recommendation (§4.6) competes for a slot. At five, this probably means Veil carries it (E3), meaning we do not also get a Veil-anchor Omen-shape (E1). Trade-off.
3. Marvel Rivals' 33-at-launch success is partly IP leverage — "all your favorite Marvel heroes" — which we do not have. Five unknown commanders is a *bigger* ask than five Marvel ones; shipping more to compensate goes the wrong direction (more unknowns, not fewer).
4. If Stage 01 ends up supporting "no commander / classic mode" as a default, the pressure on commander diversity drops and 3 becomes more defensible. This is cross-dependent on Stage 01 that hasn't been drafted yet.

---

## Deliverables

### Archetype matrix table

See §5. Anchor per lineage: A1 Sinew, B1 Ember, C3 (or C1) Forge, D1 (or D3) Crown, E1 (or E3) Veil.

### Starter roster recommendation — 5 slots [PROPOSAL]

No final names per [CONCEPT §5.4](../CONCEPT.md). Fantasy labels are placeholder-descriptive.

| Slot | Lineage tilt | Fantasy label (placeholder) | Age band | Representation axis | Why this slot |
|------|---|---|---|---|---|
| 1 | Sinew | Warmother — former siege-captain | 60s | Elder female frontline | §4.1 + §4.3 appetite; avoids §3.1 default |
| 2 | Ember | Scholar-exile — academic, burdened, arcane specialty | 40s | Older male scholar (or gender-flip OK) | Doctor-Strange-shaped durable anchor |
| 3 | Forge | Foundry-master — dwarven, queer, pragmatic | middle-aged non-human | Queer + non-human | §4.2 + §4.4; fills Forge economy identity |
| 4 | Crown | Paladin-king OR Saint-matron — messianic, weary | elder | Age + weight of burden | Anchors aura/influence fantasy; Tirion-shaped |
| 5 | Veil | Trickster-courier — queer, charming, non-lethal toolkit | 30s | Queer + charm + absurd-adjacent | Omen+Jeff hybrid; carries the playful slot |

Recommend the PM lock exactly one of Slot 4's two alternatives (paladin-king *or* saint-matron, not both). Recommend Slot 3 remain non-human to avoid all five slots reading human.

### Explicit "we are NOT shipping these archetypes" list

At launch, and preferably through the first two seasons:

1. Gritty male soldier (jawlined, tactical gear, ranged rifle, stoic one-liner).
2. Anime swordmaiden / twin-blade duelist.
3. Chosen-one orphan youth (of any gender).
4. Scruffy scoundrel / space-cowboy rogue.
5. Edgy cloaked male assassin / ninja.
6. Sexy-elf-ranger.
7. Teenage prodigy mage-girl.
8. Generic dwarven drunk.

If a candidate Commander in later development drifts toward this list, treat as a **character-brief failure**, not a "ship it and iterate" case. Drift back to defaults is the failure mode we are designing against.

---

## Working-notes appendix — sourcing gaps and debt

Places where I could not reach Tier 1/2 evidence and leaned on Tier 3 sentiment, flagged for future replacement:

- Archetype-fatigue claims in §3 (anime swordmaiden saturation, cloaked-assassin underperformance) are partially Tier 3 / sentiment. The Rivals pick-rate data is Tier 2 and supports the directional claim, but the *causal* attribution ("players are fatigued with this trope") is inferred, not surveyed.
- Cognitive-load claim for first-pick rosters >8 in §6 is sentiment-tier; I could not find a Tier 1 published study. Riot internal posts referenced are trade-press summaries.
- Pick-rate data for Mechabellum, Stormgate, Deadlock was not sufficiently public at Tier 1/2 to include; these are excluded rather than downgraded.
- Melinoë reception (§1) blends Tier 2 reviews with Tier 3 Steam-forum sentiment; directional only.
- Hero-shooter launch-roster budget comparison (§6) leans on public launch counts (Tier 1) but the *cost-per-hero* implication is inferred, not directly sourced — no developer post-mortem surfaced in the methodology-compliant search window gave a clean per-hero content-cost figure.

Replacing any of these with a Tier 1/2 source during later passes should not change the synthesis in §1, §4, or §6. It would strengthen §3.

---

*End of draft. Next review: after PM ratification of roster size, or on receipt of Stage 01 first draft.*
