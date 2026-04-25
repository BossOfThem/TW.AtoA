---
**Status:** Draft
**Last reviewed:** 2026-05-05
---

# Phase 7 — Iteration

*What stays open. What gets revisited. How the doc keeps living.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-6.md](phase-6.md). Next: — (end of cascade).

---

**Amendment banner — 2026-04-26 real-cultures frame cascade (phase-7 consumer turn).** Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility **Hard**) — the 3-lineage Ash/Nature/Prayer + Dust/Form/Apotheosis shape is superseded by 3 civilizations (Greek/Aztec/Norse) + the 4-tier T1→T4+Fusion ladder. Open questions, refinement queue, and notes-to-future-self retargeted accordingly. Attack-type surfaces reference [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md).

---

## 7.1 Open questions (resolution targets noted)

1. **Mobile unit control model** (waypoint + mode flags confirmed, specifics) — resolved by Phase 4 exit.
2. **Enemy direction under real-cultures frame** (leaning Option C hybrid — civ-matched bosses at 5/10/15/20/25/30 + shared cross-cultural regular-wave pool per `concept/phase-4.md §4.7`) — resolved by Phase 4 exit. Supersedes prior "leaning B-dominant hybrid" question under the superseded dungeon-cosmology frame.
3. **Monetization model specifics** (leaning DRG-style premium + free BP + cosmetic DLC) — resolved by Phase 4 exit.
4. **Engine choice** (leaning Godot 4) — resolved by Phase 4 exit.
5. **Commander launch roster size** — **CLOSED at 3** (Leonidas / Montezuma II / Ragnar Lothbrok — one per launch civilization). Under the 2026-04-25 ratification the 3 is driven by the 3-civ structure; patch-1 adds one more per civ (2026-04-25 Follow-up #6). Not cascade-blocked.
6. **Hybrid discovery mechanic** — **CLOSED 2026-04-25**. Superseded by the Fusion system: menu-driven, not positional; 9 locked recipes visible in a codex from the Commander pick screen and from the in-match Fusion menu per `concept/phase-4.md §4.3`.
7. **Cultural-sensitivity pass** — **MANDATORY GATE** before MVP content-lock (2026-04-25 Follow-up #5). External consultation for Aztec representation; 300-movie-ideology audit for Leonidas; TV-show-vs-history framing for Ragnar.
8. **Game title** — resolved by Phase 5. The "Ash to Altar" working title is no longer thematically load-bearing under the real-cultures frame (2026-04-24 reopen). Title-lock still deferred; working-only until Phase 5.
9. **T4 Demigod-tier forms per commander/civilization** — resolved during T4 design per the locked 18-Demigod roster from 2026-04-25 (supersedes prior "Apotheosis (tier 3) forms per commander/lineage" framing).
10. **Civilization role differentiation under real-cultures frame** — each civ must have a legible thematic and mechanical identity distinct from the others (Greek defensive-anchor + divine-heavy endgame, Aztec ritual + priest-warrior + poison/fire, Norse raider + berserker-fury + slashing-heavy). Attack-type-coverage gaps per civ (Greek lacks Slashing/Poison, Aztec lacks Crushing, Norse lacks Poison/Divine) are intentional and tell the player what to counter-pick. Supersedes prior "Prayer drift / Ash mandatory-not-mandatory / 3-lineage differentiation" open question.
11. **Foresight-coin cross-civ borrowing mechanic** (2026-04-25 Follow-up #7) — deferred to post-launch. Specifies how a Greek commander might reach an Aztec tower.
12. **PvE campaign + AGES + leveling + attributes** (2026-04-25 Follow-up #8) — deferred; may reopen §4.7 enemy direction and §3.5 tier pacing per chapter.
13. **Patch-1 commanders per civilization** (2026-04-25 Follow-up #6) — TBD; one additional historical / mythic commander per civ.
14. **Mobile platform plan** — deferred to post-launch.
15. **Ranked mode design** — deferred to post-launch.
16. **Modding support** — deferred, but flagged as highest-leverage long-term retention feature.
17. **Naming pass** — the commander / tower / unit / Demigod / God names from the 2026-04-25 ratification are locked content-skeleton placeholders (mundane historic / high-school-recognizable-mythic). They are already §5.4-compliant in kind (Commanders = first-name + epithet or historic figure; Towers = mundane job-like building; Gods = named mythic proper nouns). Future decision may either ratify the current set as final or pick §5.4-compliant alternatives. Conventions in §5.4 remain **[LOCKED]** and untouched throughout.
18. **Phase 1 exit formal one-page write-up** (2026-04-25 Follow-up #11) — rubric substantively answered by the 2026-04-25 ratification + 2026-04-26 cascade; only the formal one-pager is still owed.

## 7.2 Decision log policy

Every major design decision recorded in `decisions/` with:
- Date
- Decision
- Alternatives considered
- Reason chosen
- Reversibility note (easy / medium / hard)

Decisions can be reversed, but only with a written reason in the same log.

## 7.3 Refinement priority queue

Order in which open items get addressed, assuming no new emergencies:

1. ~~Commander roster decision~~ — **CLOSED at 3** (locked launch trio per 2026-04-25).
2. ~~Hybrid discovery mechanic~~ — **CLOSED 2026-04-25** (menu-driven Fusion; 9 locked recipes).
3. Per-civilization mechanical identity (one-page writeup each — 3 civilizations: Greek / Aztec / Norse, covering 6 towers + 5 units + 6 T4 Demigods + 3 Gods + attack-type coverage).
4. Per-commander mechanical spec (one-page writeup each — Leonidas / Montezuma II / Ragnar Lothbrok) under the §4.1 identity floor, with full 3-ability kit numerics and cultural-sensitivity pass noted.
5. Fusion recipe balance pass — 9 locked recipes; verify no God is dominant / skippable; check the 2-type-damage inheritance plays fairly against the 5-armor matrix.
6. Tier Gate UX specification (T1→T2, T2→T3, T3→T4 + the Fusion event — supersedes the superseded Age Gate / Dust/Form/Apotheosis Tier Gate framing).
7. Cultural-sensitivity pass (2026-04-25 Follow-up #5) — hard gate before content-lock.
8. Onboarding + tutorial design (including the "mundane outside, myth inside" reveal pacing).
9. Scope reduction pass (what gets cut if timeline pressures rise).
10. Competitive differentiation statement (one paragraph: what makes this not just another TW game — the Fusion-to-Gods endgame is the lead differentiator).
11. Engine choice lock.
12. Monetization model lock.

## 7.4 Notes to future self

- Resist designing content before mechanics are locked. Three civilizations that feel mechanically distinct are worth more than fifty towers that feel mechanically same.
- The "almost infinite options" promise is carried by divergence forks and the **Fusion endgame**, not tower count. Nine locked Gods via nine locked recipes is not a small number when each is a 2-type damage source with locked armor-tag interactions.
- **The Commander is the user.** Protect the "Commander = player identity" promise — do not let Commander become just a skin with a stat modifier. Commander should have voice, story, progression, and signature ability that make the player feel *seen*. Under real-cultures the Commander is also a legendary historical leader — the voice + story inherits that weight.
- **"Mundane names outside, myth inside."** A Phalanx stays a Phalanx at T1-T3; when it fuses into Zeus, the trailer beat is earned. Don't surface the mythic layer too early; don't hide it at the endgame either.
- The **civilization-persistence callback** is the core delighter — a Greek match feels Greek from first wave to final fusion. Protect it.
- If a mechanic doesn't make the T1 tower placement (minute-1 choice) matter more, question whether it belongs.
- **Cascade discipline:** if you find yourself editing a Phase 2 constraint because a Phase 5 decision is inconvenient, stop. Reopen Phase 2 properly or change the Phase 5 decision.
- **Solo mode must be fully great on its own.** Multiplayer is additive, not required. Do not let multiplayer cold-start risk kill the launch.
- **Battle pass + cosmetic store works only with strict no-pay-to-win.** One misstep burns audience trust permanently. This is not a marketing concern. This is an identity constraint.
- **Live-service ops is a permanent state, not a project.** Scope content cadence realistically for a two-dev team. Seasonal content means *seasonal*, not *monthly*.
- **Cultural sensitivity is not optional.** Real-world cultures come with real-world responsibilities. Aztec representation in particular must clear external review before any content lock. Leonidas visual must not replay the 300-movie ideology. Ragnar must not flatten into the TV-show character. This is a hard gate, not a polish pass.
- The game title deserves the same discipline as every other naming convention. Don't ship with a placeholder.
- **Go big at launch (non-negotiable).** MVP ships the full locked content skeleton — 3 civilizations × (6 T1–T3 towers + 5 units + 6 T4 Demigods) + 3 Gods via the 9 locked Fusion recipes (per 2026-04-25 ratification). No MVP truncation to "1 civ + 2 commanders + 1 God." The validation rubric (`phase-6.md §6.4`) is built on the full arc, the trailer beat is the Fusion endgame, and the civilization-persistence callback only emerges if all three civs are present to compare against each other. Cutting scope at MVP saves weeks and loses the product. If timeline pressure forces a cut, cut **post-launch** content (patch-1 commanders, post-launch Gods, modes 7+) — never the launch skeleton.
