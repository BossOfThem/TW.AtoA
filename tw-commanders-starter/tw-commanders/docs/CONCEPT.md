# TW-COMMANDERS — Concept Cascade

**Working title only.** A tower wars game where every match is a compressed arc of civilizational evolution, fought between Commanders who each embody a distinct lineage path — and whose starting choice at minute 1 still matters when the final-age forms enter the field at minute 20.

This document is structured as a **waterfall cascade**: seven sequential phases, each with an explicit exit condition that hands off to the next. You do not skip ahead. A phase does not begin until the one above it is signed off. The point of the cascade is that Phase 7 decisions are constrained by Phase 1 decisions, and you can trace every late choice back to an early one.

## Placeholder names

All names in this document — commanders, factions, legions, ages, towers, units, hybrids, heirlooms, currencies, modes, enemies — are **placeholder / conceptual**. They will be revised once mechanics are locked and identity work begins. Do not treat them as final. When a name is finalized, it will be marked `[LOCKED]`.

The only locked decisions about naming are the *conventions* themselves in §5.4, not the specific names.

## The Commander is the user

Throughout this document, "the Commander" refers to the player's persistent avatar in the game. The player chooses a Commander at first login. The Commander carries across matches, levels up, unlocks content, and can be deployed as a Hero Unit on the battle map in modes that support it. The Commander is the player's identity in the game world. When in doubt about perspective, assume first-person player.

---

## Phase 1 — Discovery

*What are we building, for whom, and why.*

### 1.1 Vision statement

A tower wars game where every match plays through an accelerated arc of civilizational evolution. Players command a lineage through the ages, defending their lane and pressuring opponents' lanes. The tower you place in minute 1 still matters in minute 20 — it has evolved past recognition but carries your early choice forward. The Commander you chose at login is a living identity across every match you play, with their own story, unlocks, and hero-mode signature ability.

### 1.2 Target player

A strategy-game player who has finished *Kingdom Rush*, *Bloons TD 6*, and/or *Legion TD 2*. Comfortable with build-optimization loops and counter-picking. Interested in competitive multiplayer but also enjoys solo and co-op play. Values tight session length (5–25 minutes per match). Looking for a modern, polished take on the Warcraft 3 tower wars custom-map tradition with real single-player depth.

### 1.3 Core promise to the player

Three things, in order of importance:

1. **Commander identity.** The Commander you choose is yours. Across every match, your Commander's story, unlocks, and progression are visible and meaningful. You are not a generic avatar — you are a specific character with specific powers.
2. **Age persistence in-match.** The lineage you favor in minute 1 still feels like the same lineage in minute 20 — even though every tower name, model, and mechanic has evolved through the ages during the match.
3. **Multiple ways to play.** Solo vs AI, co-op horde, competitive lane wars, and commander-driven campaign — all built on one shared engine. No mode feels like an afterthought.

### 1.4 Success criteria for the vision

- Can be explained in one sentence to a Tower Wars fan and they nod.
- Solo mode is complete and enjoyable on its own, without any multiplayer.
- Has at least three unique mechanics no existing Tower Wars game ships with.
- Retains a player for ≥50 matches before content feels exhausted.
- Commander choice feels meaningful both mechanically and narratively.

### 1.5 Exit condition for Phase 1

Vision and promise are specific enough that any team member could restate them without looking at this doc. No further discovery work is needed to move on.

→ **Hand off to Phase 2.**

---

## Phase 2 — Analysis

*What constrains the design before we design anything.*

### 2.1 Competitive landscape

- **Legion TD 2** — the direct genre competitor. We learn from their mechanics (legions, mythium, merc-sending, mastermind drafting); we beat them on polish, single-player depth, and commander-driven identity.
- **Kingdom Rush / Bloons TD 6** — the production quality bar. Kingdom Rush reference for solo TD polish; Bloons for replay depth.
- **Warcraft 3 custom maps** (Element TD, Green TD, Castle Fight, Hero Line Wars) — the genre origin. Our reference for variety, community-driven mode expansion, and the idea that tower wars can host many sub-genres.
- **Clash Royale** — reference for commander/persistent-progression in a multiplayer strategy loop. We borrow structure, not gacha.
- **Deep Rock Galactic** — reference model for fair monetization: premium price + free earnable battle pass + cosmetic DLC, zero pay-to-win.
- **Hades** — reference for meta-progression that respects the player and doesn't gate fun behind grind.
- **Civilization / Humankind** — thematic inspiration only. We are NOT a 4X.
- **Plague Inc. Evolved** — reference for "evolution as mechanic."

### 2.2 Design constraints

- **Match length:** 5–25 minutes depending on mode. Solo TD target ~15min, lane wars ~20min, horde ~25min, quick-match ~8min.
- **Platform:** PC primary. Mobile is a post-launch consideration, not a launch requirement. Competitive multiplayer on mobile is a separate UX problem we are not solving at launch.
- **Team size:** two developers using AI-assisted workflows. Content must be data-driven and generable, not hand-sculpted per unit.
- **Art budget:** unknown at concept stage. Assume silhouette-forward stylized until proven otherwise. Contract an art director in Phase 4 or early Phase 5.
- **Netcode:** user-hosted games + Steam networking for launch. No dedicated server infrastructure required at launch. Dedicated servers for ranked later, maybe.

### 2.3 Known risks

- **Content explosion.** Commanders × lineages × ages × forks × hybrids = combinatorial content. Must be scoped aggressively. Data-driven pipeline is non-negotiable.
- **Lineage balance.** Five lineages must feel mechanically distinct, not just cosmetically. If two converge on the same playstyle, the system fails. Multi-way balance is notoriously hard.
- **Onboarding cliff.** Commander + ages + lineages + economy + send/defend + modes is a lot for a first-time player. Tutorial design is a real UX risk and gets its own Phase 5 attention.
- **Multiplayer cold-start.** If ranked lobbies don't fill, competitive play dies. Solo mode must carry the game independently. See §2.4.
- **Live-service ops commitment.** Battle pass + store + seasonal content requires ongoing team capacity. A two-dev team cannot run AAA-scale live ops. Content cadence must be realistic.
- **Monetization model tension.** Battle pass + cosmetic store works *only* with strict no-pay-to-win discipline. One misstep burns audience trust permanently. This is not a marketing concern; it is an identity constraint.
- **Commander over-promise.** If commanders are visually distinct but mechanically identical, the identity promise fails. Each commander must feel different to play.

### 2.4 Constraints we are choosing to accept

- **Solo mode is first-class.** Fully playable, fully polished, complete on its own. Multiplayer is additive, not required.
- **PC-first, desktop-quality UX.** Mobile later or never.
- **Premium + cosmetic monetization.** Target price point $5–15. Free seasonal battle pass earnable through play. Optional cosmetic DLC. NEVER pay-to-win. NEVER gacha. NEVER gameplay advantage sold.
- **English-first.** Localization is post-launch.
- **User-hosted multiplayer.** No dedicated server ops at launch. Accept peer/host trust model for small-lobby play.

### 2.5 Open question flagged here — OPEN

Monetization model specifics: premium price point, battle pass structure, cosmetic store scope. Leading model: Deep Rock Galactic (premium price + free earnable battle pass + optional cosmetic DLC). Must be resolved before Phase 5 exit. Tagged as blocker.

### 2.6 Exit condition for Phase 2

The design team can list, from memory, the top three risks and the top three constraints. Nothing in Phase 3 may violate a Phase 2 constraint without a written override in the decision log.

→ **Hand off to Phase 3.**

---

## Phase 3 — Design

*The shape of the game. High-level, not detailed.*

### 3.1 Core match loop (shared across all modes)

A match proceeds through multiple **ages** in sequence. In PvE modes, ages advance on a wave timer or wave count. In PvP modes, ages advance on a match timer or triggered event.

Between ages, an **Age Gate** pauses play and offers:
- Automatic advancement of existing towers to the next age's form.
- A **Divergence Fork** at certain gates, presenting 2–3 path choices that re-skin future ages.
- A marketplace of new towers/units unlocked by the advancing age.

Combat within an age uses standard tower wars mechanics: towers defend your lane, units attack enemy lanes (in PvP), economy drives everything.

What makes this game different is what happens *between* ages, and the fact that your starting Commander choice persists as a visible identity through the entire arc.

### 3.2 The Commander system (central feature)

A **Commander** is the player's persistent identity in the game world. At first login, the player chooses a Commander from a starter roster. Each Commander has:

- A distinctive visual identity (portrait, silhouette, color accent, voice).
- A thematic backstory, usable as solo campaign framing.
- A **lineage affinity** — a +X% tilt toward one of the core lineages. Not a cage; player can still build other lineages heavily.
- A **passive buff** — small mechanical bonus that persists across matches.
- A **signature ability** — unlocks at a commander level threshold. Deployable as a Hero Unit on the battle map in supported modes.
- A **progression track** — XP, levels, unlocked cosmetics, voice lines, portrait frames.

Commanders level up through play. Towers in a match start at age 1 (Primal) and progress through ages during that match. Commander progression is match-to-match meta. Age progression is within-match tactical. These are two distinct progression systems operating at different timescales.

**Starter commander roster (placeholder names, all subject to revision):**
- Commander A — Sinew-leaning frontline specialist
- Commander B — Ember-leaning tech specialist
- Commander C — Forge-leaning economy specialist
- Commander D — Crown-leaning aura specialist
- Commander E — Veil-leaning trickster

Launch roster size: TBD. Leading options are 3 (lean launch), 5 (one per lineage), or 8 (Legion TD 2 parity). Decision deferred to Phase 5.

**"Tilt, not cage" principle:** a Sinew-leaning Commander can still build Ember-heavy mid-game. They just don't get the Sinew affinity bonus. This preserves player agency.

### 3.3 The five lineages (mechanical identity within a match)

Each lineage fills a mechanical role that the other four cannot fill. Lineages are the *unit categories* within a match, independent of Commander choice.

- **Sinew** — the front line. High HP, high damage, low range. Takes hits, deals hits. Includes mobile melee units that can push lanes.
- **Ember** — the tech accelerator. Weak alone. Unlocks techs that buff the whole board. Tower-based but outputs are board-wide buffs, not direct damage.
- **Forge** — the economy. Generates gold, produces buffs, feeds adjacent towers.
- **Crown** — the multiplier. Aura towers. Do not kill enemies; make other towers kill them harder.
- **Veil** — the wild card. Time, terrain, debuff, reality-bend. Weird by design. Includes most of the "special effect" category units.

A player who ignores any one lineage will struggle. A player who specializes narrowly will excel in that narrow domain and fail broadly. The game is built to reward balanced lineage use, not maxed lineage use.

**Open issue:** Veil's "weird by design" role has a known failure mode of being "the one nobody picks." Specification must resolve this in Phase 4.

### 3.4 Unit categories (cross-cutting, not lineage-exclusive)

Units come in three categories:

- **Towers** — static placements. Attack within their range. Most tower-wars units are towers. Evolve through the ages.
- **Mobile units** — active units placed on the board that move along paths or patrol routes. Include melee front-liners (Sinew), skirmishers, and hero-class units. Can be directed with waypoint-style commands, not full RTS micro.
- **Special effect units** — timed abilities, temporary zones, consumables, debuff fields. Predominantly Veil lineage. Limited in placement count per match to avoid spam.

The Commander, when deployed via signature ability, acts as a Hero Unit — a special high-value mobile unit with abilities. Only one Commander Hero per player on the map at a time.

### 3.5 The eleven ages (in-match tower evolution tiers)

The structural backbone. Each age re-skins every lineage's towers and units. The count (eleven) is conceptual and may change. Names are placeholder.

1. Primal
2. Mudbrick
3. Iron
4. Spires
5. Alchemical
6. Steamheart
7. Atomic
8. Signal
9. Synthetic
10. Stellar
11. Ascendant

Not every match reaches all eleven ages. Match length and mode determine max age reached. Solo TD missions may cap at age 6–8. Ranked lane wars may cap at age 9–10. Special endgame modes unlock ages 10–11. This is a design lever, not a bug.

Early ages are short and brutal. Late ages are longer and more strategic. Total playtime stays within mode target.

### 3.6 Game modes (launch roster)

1. **Solo Campaign** — story missions tied to each Commander. Progresses through ages. Introduces mechanics gradually. Non-negotiable at launch. This is how the solo promise is kept.
2. **Solo vs AI (Skirmish)** — pick map, difficulty, lineage restrictions. Quick game against AI.
3. **Co-op Horde** — 2–4 players defend shared lanes against escalating waves. User-hosted or matchmade.
4. **Lane Wars 1v1** — classic competitive tower wars PvP.
5. **Lane Wars 2v2** — team PvP, matchmaking or party.

**Post-launch expansion (not at launch):**
- **Hero Line Wars** — hero-controllable extended mode. Builds on the signature ability system.
- **Ranked** — competitive laddered play with seasons.
- **Custom modes** — community-driven, tied to modding support if we add it.
- **Roguelite TD** — single-player run-based mode that borrows TTA concept ideas.

### 3.7 Meta systems (between-match progression)

1. **Commander progression** — XP, levels, unlocks (cosmetics, voice lines, commander passive tiers, signature ability tiers).
2. **Backpack / Inventory** — gifts, evolution components, consumables, cosmetic items. Earned through play or events. Inventory UI in main menu.
3. **Battle Pass** — seasonal progression track. Free tier earnable by playing. Premium tier unlocked by purchase, rewarding cosmetics only (never gameplay power).
4. **Cosmetic Store** — skins, emotes, commander voice packs, map tints. Never sells gameplay advantage.

### 3.8 Exit condition for Phase 3

The shape of the game can be drawn on a whiteboard in five minutes: commanders, five lineages, eleven ages, three unit categories, five launch modes, four meta systems. Nothing in Phase 4 introduces a new system that contradicts Phase 3.

→ **Hand off to Phase 4.**

---

## Phase 4 — Specification

*Detailed system design. This is where the game actually becomes a game.*

### 4.1 Commander mechanical spec (OPEN — needs full writeup)

Each Commander needs documented:
- Lineage tilt magnitude (leading: +15% to affinity lineage outputs).
- Passive buff description (small, persistent, not match-winning).
- Signature ability for hero mode deployment (cooldown, duration, effect, visual).
- Unlock path for cosmetics and voice lines (by commander level).
- Solo campaign storyline (outline only at Phase 4; full script in Phase 5 polish).

Each Commander gets a one-page mechanical writeup before Phase 4 exits.

### 4.2 Divergence system

At specific ages, the player picks a fork that re-skins every lineage's expression for that age and all future ages of the match. The fork does not change the lineage's mechanical role — it changes how that role is expressed visually and subtly mechanically (damage types, tempo, etc.).

Placeholder fork pool:
- **Steamheart fork (age 6):** Steam / Electric / Æther
- **Atomic fork (age 7):** Nuclear / Biotech / Chemical
- **Synthetic fork (age 9):** Cybernetic / Organic / Mystic
- **Stellar fork (age 10):** Colonist / Warborn / Transcendent

Run variety: 3 × 3 × 3 × 3 = 81 possible fork paths per match when all forks apply. Each produces a visibly and mechanically distinct late game.

### 4.3 Hybrid system

When two lineages are placed adjacent on the board and held adjacent for a threshold duration, a hybrid evolution unlocks in the tech tree. The player can then build the hybrid unit.

Adjacent-lineage hybrids are common. Opposite-lineage hybrids are rare and high-payoff.

Starter hybrid table (placeholder names, not final):

| Pair | Age unlocked | Hybrid (placeholder) |
|------|--------------|----------------------|
| Sinew + Ember | Steamheart | Tank Corps |
| Forge + Crown | Iron | The Tribute Hall |
| Ember + Veil | Synthetic | Mindshards |
| Crown + Sinew | Spires | Holy Order |
| Forge + Veil | Mudbrick | Rune-Smiths |

Target count: 20–30 hybrids across all age × pair combinations. Full table is a Phase 4 deliverable.

**OPEN BLOCKER — hybrid discovery mechanic:** Unlock via adjacency creates rote placement once players learn the pairings. Wikis will publish the full table week 1, and the "discovery" feeling breaks. Resolution options:
1. Accept it. Discovery is a first-run experience; rote placement is fine for veterans.
2. Add randomness. Hybrids have a probabilistic unlock on adjacency, with heirloom/meta boosts.
3. Gate knowledge. Hybrid knowledge is per-commander or per-account, unlocked through play. Wikis help advanced players but entry-level players still discover.

Decision required before Phase 5 begins.

### 4.4 Mobile hero units specification

Mobile units need:
- Movement speed per unit tier.
- Pathing mode (patrol, follow lane, direct to waypoint, attack-move).
- Engagement rules (auto-engage, hold, fall back).
- Control complexity: waypoint + mode flags, NOT full RTS per-unit micro.

**OPEN ISSUE:** Exact control model. Full RTS per-unit micro is scope-blowing and wrong genre. Waypoint + mode flags is achievable. Attack-Move command is useful. Must resolve before unit spec work starts.

Commander Hero Units (signature ability deployments) have richer control — direct movement + 2–3 abilities + return-to-base. One active Commander Hero per player per match.

### 4.5 Special effect units specification

Special effect units are limited in placement count per match to avoid spam. Examples:
- Timed zones (debuff aura for 20 seconds).
- Consumables (one-shot damage bursts, healing pulses).
- Terrain modifiers (Veil: create a tar pit, destroy it next age).

Each special effect has a cooldown, a cost, and a visible indicator on the map. Specification per-item is a Phase 5 task; Phase 4 locks the *framework* only.

### 4.6 Economy specification

Three in-match currencies, one per primary lineage pillar:
- **Gold** — generated by Forge towers and wave kills. Spent on tower placement and tower upgrades.
- **Knowledge** — generated by Ember towers. Spent on tech unlocks that buff the board.
- **Influence** — generated by Crown towers. Spent on aura upgrades and fork choices.

Sinew and Veil do not generate primary currency. They spend the other three. This is intentional: every build must touch at least one economy lineage.

**Multiplayer-only fourth currency:**
- **Mythium** (placeholder) — time-based income from workers (Legion TD 2 pattern). Spent on sending creeps/mercenaries to opponent lanes.

Sinew and Veil are pure consumers. Forge/Ember/Crown are producers. The bookkeeping is standard; the balance work is extensive.

### 4.7 Enemy system (PvE modes)

Two directions:
- **A — Parallel evolution.** Enemies march through the ages alongside the player. Stone beasts → bronze raiders → iron barbarians → etc.
- **B — The Left Behind.** Enemies are what humanity abandoned at each age. Beasts we displaced. Plagues we outgrew. Gods we stopped believing in. Machines we discarded. Finally: past versions of ourselves.

**Leading direction: hybrid — B-dominant with A as wave-variety baseline.** Regular waves use Direction A patterns (parallel evolution, easier to art and balance). Age bosses and special waves use Direction B (thematically rich, marketing-heavy). This gets you the trailer moments without tripling the art burden.

Decision required before Phase 5 begins.

### 4.8 Exit condition for Phase 4

- Commander spec complete (one-page per commander).
- Hybrid discovery mechanic resolved.
- Mobile unit control model resolved.
- Enemy direction locked.
- Economy balanced on paper (spreadsheet with currencies, costs, income curves).
- Monetization model specifics resolved.
- Engine choice locked.
- Art director engaged or scoped.

→ **Hand off to Phase 5.**

---

## Phase 5 — Implementation planning

*What gets built, in what order, to prove the vision before investing in content.*

### 5.1 MVP slice

The smallest playable thing that answers: *"Does the commander + ages + lineage combination produce a game that a Tower Wars fan wants to keep playing?"*

- **Two commanders** (one Sinew-leaning, one Ember-leaning).
- **Two lineages fully built** (Sinew and Ember). No Forge, Crown, or Veil yet.
- **Five ages** (Primal → Mudbrick → Iron → Spires → Alchemical). Five ages is the minimum depth that lets the age-persistence feeling emerge. Three ages (as in earlier TTA MVP spec) is too short.
- **One hybrid** (Sinew + Ember → Tank Corps).
- **One mode**: Solo vs AI on one map.
- **Basic UI**: unit picker, health bar, economy display, age gate.
- **No divergence forks yet.**
- **No meta progression** (no commander XP, no backpack, no battle pass).
- **No multiplayer yet.**

If the MVP is fun, the vision works. If it is not fun, no amount of content added on top will save it.

### 5.2 Build phases after MVP

1. Add remaining three lineages (Forge, Crown, Veil) — completing the five.
2. Add ages 6–8 (Steamheart → Signal) and the first divergence fork (Steamheart fork).
3. Add multiplayer netcode + Lane Wars 1v1 mode.
4. Add Co-op Horde mode.
5. Add Commander meta progression (XP, levels, unlocks).
6. Add Solo Campaign for launch commanders.
7. Add ages 9–11 and remaining forks.
8. Add Backpack + Battle Pass + Cosmetic Store.
9. Add Lane Wars 2v2.
10. Polish pass: art, sound, UX, onboarding, accessibility.

Each phase has its own validation gate. See Phase 6.

### 5.3 Art and tone direction

Three candidates:
- **Stylized vector / painted flat** — Kingdom Rush reference.
- **Isometric diorama** — Bloons TD 6 reference.
- **Silhouette-forward mythic** — cheapest, most distinctive. *Leading choice.*

Silhouette-forward mythic requires strong art direction to avoid feeling underbuilt. Contract an art director *before* vertical slice work begins, not during.

### 5.4 Naming conventions (LOCKED at Phase 5)

- **Game title:** TBD. Current working title is placeholder.
- **Commanders:** evocative titles, may be first-name + epithet. Never generic.
- **Lineages:** one-syllable, ancient-feeling nouns (pattern: Sinew, Ember, Forge, Crown, Veil).
- **Ages:** evocative compound nouns, not dates (pattern: The Mudbrick Era).
- **Towers/Units:** job titles, never proper nouns (pattern: Warhost, Spirebinder).
- **Hybrids:** compound or hyphenated (pattern: Tank Corps, Rune-Smiths).
- **Enemies:** single-word kenning (pattern: Thornback, Nullspawn, Ashwake).
- **Heirlooms / inventory items:** mythic-fragment style (pattern: The Last Spear of Heidelberg).
- **Modes:** direct, muscular (pattern: Lane Wars, Horde, Campaign). Not florid.

### 5.5 Engine choice

**Leading choice:** Godot 4, 3D scene with angled orthographic camera (StarCraft/Warcraft III style). GDScript for most game logic, C# for performance-critical paths if needed.

**Alternatives considered:**
- Unity — larger ecosystem, more middleware, more tutorials. Cons: licensing, corporate drift.
- Unreal — overkill for this genre. Cons: C++ or Blueprints overhead, royalty structure, heavy build pipeline.

**Locked at:** end of Phase 4.

### 5.6 Exit condition for Phase 5

MVP scope agreed. Build order sequenced. Art direction picked. Naming conventions locked. Engine locked. Art director contracted. Initial sprint plan sequenced.

→ **Hand off to Phase 6.**

---

## Phase 6 — Validation

*How we know the game is working before we commit to finishing it.*

### 6.1 Primary question for the MVP

Does the commander + ages + lineage combination produce moment-to-moment fun, AND does the age-persistence feeling emerge by age 4 or 5?

If yes, the vision is viable. If no, the vision is wrong and Phase 1 must be reopened.

Five ages in the MVP is deliberate: three ages is too short for age-persistence to emerge, and eleven ages is too much content for an MVP. Five is the minimum that validates the core mechanic honestly.

### 6.2 Secondary questions (in order)

- Do new players understand commanders and lineages within their first match?
- Do players re-pick the same commander on match 2 or try another? (Indicates whether commander identity is sticky or shallow.)
- Does the age-persistence callback feel earned by age 5?
- Is match length right, too long, or too short?
- Which lineage gets picked least, and is that a bug or a feature?
- Does solo TD hold attention without multiplayer? (Critical — solo must carry the game independently.)
- Do hybrids feel discovered or feel hidden?

### 6.3 Playtesting approach

- **Internal playtesting** with the two-person dev team through MVP completion.
- **Closed alpha** with 5–10 external playtesters (TD/TW fans) for the first post-MVP expansion (all five lineages, 8 ages, one PvP mode).
- **Open alpha** after multiplayer is stable and all commanders exist, to catch late-game balance and cold-start matchmaking issues.

### 6.4 Success metrics per build phase

- **MVP:** 70%+ of playtesters say they would play a second match. 50%+ report the age-persistence feeling. Median session length ≥ 15 minutes.
- **Post-five-lineages:** No lineage picked less than 10% of the time across tracked runs.
- **Post-multiplayer:** Median ranked match finds opponent in <60 seconds during active hours. <5% disconnect rate.
- **Post-eleven-ages:** Median player reaches age 9+ within three matches.
- **Alpha:** Average session length ≥ 30 minutes. Day-2 return rate ≥ 40%.

### 6.5 Exit condition for Phase 6

A validation plan exists for every build phase. Success metrics are defined in advance, not defined after the data comes in. The team knows what would make them cancel the project.

→ **Hand off to Phase 7.**

---

## Phase 7 — Iteration

*What stays open. What gets revisited. How the doc keeps living.*

### 7.1 Open questions (resolution targets noted)

1. **Hybrid discovery mechanic** (accept/randomness/gating) — resolved by Phase 4 exit.
2. **Mobile unit control model** (waypoint+mode flags confirmed, specifics) — resolved by Phase 4 exit.
3. **Enemy direction** (leaning B-dominant hybrid) — resolved by Phase 4 exit.
4. **Monetization model specifics** (leaning DRG-style premium + free BP + cosmetic DLC) — resolved by Phase 4 exit.
5. **Engine choice** (leaning Godot 4) — resolved by Phase 4 exit.
6. **Commander launch roster size** (3 vs 5 vs 8) — resolved by Phase 5.
7. **Game title** — resolved by Phase 5.
8. **Final Ascendant (age 11) forms per commander/lineage** — resolved during age 11 design.
9. **Veil-not-being-the-weird-one-nobody-picks** — open, needs design resolution.
10. **Crown-not-being-boring** — open, needs design resolution.
11. **Mobile platform plan** — deferred to post-launch.
12. **Ranked mode design** — deferred to post-launch.
13. **Modding support** — deferred, but flagged as highest-leverage long-term retention feature.

### 7.2 Decision log policy

Every major design decision recorded in `decisions/` with:
- Date
- Decision
- Alternatives considered
- Reason chosen
- Reversibility note (easy / medium / hard)

Decisions can be reversed, but only with a written reason in the same log.

### 7.3 Refinement priority queue

Order in which open items get addressed, assuming no new emergencies:

1. Commander roster decision (3 / 5 / 8 at launch).
2. Per-lineage mechanical identity (one-page writeup each).
3. Per-commander mechanical spec (one-page writeup each).
4. Full hybrid table (20–30 items with adjacency rules).
5. Age Gate UX specification.
6. Onboarding + tutorial design.
7. Scope reduction pass (what gets cut if timeline pressures rise).
8. Competitive differentiation statement (one paragraph: what makes this not just another TW game).
9. Engine choice lock.
10. Monetization model lock.

### 7.4 Notes to future self

- Resist designing content before mechanics are locked. Five lineages that feel mechanically distinct are worth more than fifty towers that feel mechanically same.
- The "almost infinite options" promise is carried by forks and hybrids, not tower count.
- **The Commander is the user.** Protect the "Commander = player identity" promise — do not let Commander become just a skin with a stat modifier. Commander should have voice, story, progression, and signature ability that make the player feel *seen*.
- The age-persistence callback is the core delighter. Protect it.
- If a mechanic doesn't make age 1 matter more, question whether it belongs.
- **Cascade discipline:** if you find yourself editing a Phase 2 constraint because a Phase 5 decision is inconvenient, stop. Reopen Phase 2 properly or change the Phase 5 decision.
- **Solo mode must be fully great on its own.** Multiplayer is additive, not required. Do not let multiplayer cold-start risk kill the launch.
- **Battle pass + cosmetic store works only with strict no-pay-to-win.** One misstep burns audience trust permanently. This is not a marketing concern. This is an identity constraint.
- **Live-service ops is a permanent state, not a project.** Scope content cadence realistically for a two-dev team. Seasonal content means *seasonal*, not *monthly*.
- The game title deserves the same discipline as every other naming convention. Don't ship with a placeholder.

---

*Document version: 0.3 — TW pivot from earlier TTA concept. Preserves cascade discipline. No mechanics locked. No content committed. No names locked except naming conventions themselves (§5.4). Reopen any phase with discipline, not convenience.*
