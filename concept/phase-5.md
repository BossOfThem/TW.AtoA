---
**Status:** Draft
**Last reviewed:** 2026-04-26
---

# Phase 5 — Implementation planning

*What gets built, in what order, to prove the vision before investing in content.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-4.md](phase-4.md). Next: [phase-6.md](phase-6.md).

---

**Amendment banner — 2026-04-26 real-cultures frame cascade (§5.2 follow-on turn).** Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md), prior cascade turn rewrote §5.1 + §5.3. This turn rewrites **§5.2 (build phases)** to the real-cultures frame. **§5.4 (naming conventions) is [LOCKED] and is NOT touched by this turn or by the 2026-04-25 ratification** — only specific names flex; the conventions stay. Attack-type surfaces reference [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md).

---

## 5.1 MVP slice

The smallest playable thing that answers: *"Does the commander + civilization + tier-ladder + Fusion-to-Gods combination produce a game that a Tower Wars fan wants to keep playing?"*

Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md), **the MVP and the launch roster converge** — the locked launch skeleton is already the lean-launch floor, so MVP is the full roster, not a strict subset. Prior MVP specs (2 commanders / 2 lineages / 5 ages / 1 hybrid, and later 3 commanders / 3 lineages / 3 tiers / 2 hybrids under 2026-04-21 tightening) are **superseded**.

- **Three commanders** — Leonidas (Greek), Montezuma II (Aztec), Ragnar Lothbrok (Norse). Each shipping with the full §4.1 identity floor + the locked 3-ability kit from `concept/phase-3.md §3.2`.
- **Three civilizations fully built** — Greek, Aztec, Norse. 18 T1-T3 towers total (6 per civ), 15 units (5 per civ), 18 T4 Demigods/Heroes (6 per civ). All names locked per 2026-04-25 ratification.
- **Four-tier ladder + Fusion endgame**: T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero → Fusion → God. 9 Gods total (3 per civ) via 9 locked fusion recipes per `concept/phase-4.md §4.3`.
- **Attack-type system fully wired**: 7 damage types (Piercing / Slashing / Crushing / Fire / Poison / Arcane / Divine) + 5 armor tags + RPS matrix + status procs per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md). All 18 T1-T3 towers and 18 T4 Demigods carry their locked primary type; all 9 Gods carry their inherited 2-type damage.
- **Economy: Tribute (primary) + Divinity (mythic token)**. 30-round match cap. Mini-boss at 5/15/25, main-boss at 10/20/30. 6 Divinity cap per match. 2 Divinity to unlock Fusion menu + 1 per fusion.
- **One mode**: Solo vs AI on one map, lane-wars shape.
- **Basic UI**: unit picker, health bar, economy display (Tribute + Divinity), Fusion menu, type/armor tooltips.
- **No meta progression** (no commander XP, no backpack, no battle pass).
- **No multiplayer yet.**
- **MVP commanders honor the §4.1 identity floor.** All three MVP commanders ship with the full [PROPOSAL] floor (portrait + variant, silhouette + variant, 12 voice lines, 3-ability kit, civ affinity to own roster, 20-level ladder, 3 cosmetic slot types with 1 default item each). Without the floor, the identity-promise validation (see Phase 6) is unfalsifiable.
- **Cultural-sensitivity pass passed** (2026-04-25 Follow-up #5) before MVP content lock — mandatory gate.

If the MVP is fun, the vision works. If it is not fun, no amount of content added on top will save it.

## 5.2 Build phases after MVP

Under the 2026-04-25 real-cultures ratification, MVP converges with the full launch roster (§5.1: 3 commanders, 3 civs, 18 T1-T3 towers, 15 units, 18 T4 Demigods, 9 Gods via 9 locked Fusion recipes, Tribute + Divinity economy, 7-type × 5-armor combat). The prior 3/3/3 Ash-enabler-hybrid-family build list (2026-04-21 tightening) and the earlier 5-lineage × 11-age × 4-fork list are both **obsolete**. New sequence:

1. Add **Divergence Forks** at the two tier transitions (T2→T3 and T3→T4 per §4.2) — themes OPEN; fork ratification is a PM-input gate.
2. Add **enemy roster under the ratified §4.7 direction** (leading placeholder: Option C hybrid — civ-matched bosses at rounds 5 / 10 / 15 / 20 / 25 / 30 + shared cross-cultural regular-wave pool). Cultural-sensitivity pass (2026-04-25 Follow-up #5) gates any Aztec myth-creature content lock.
3. Add multiplayer netcode + Lane Wars 1v1 mode. Mythium PvP-only third currency wired here per §4.6.
4. Add Co-op Horde mode. Resolve mixed-civ enemy-pool matchmaking under the ratified §4.7 direction.
5. Add Commander meta progression (XP, 20-level ladder per §4.1, cosmetic / voice / portrait-frame unlocks — no gameplay-power gates).
6. Add Solo Campaign for the 3 launch commanders (Leonidas / Montezuma II / Ragnar Lothbrok). Commander-storyline outline from §4.1 one-pagers; full script under cultural-sensitivity-pass guardrails.
7. Add Backpack + Battle Pass + Cosmetic Store. Non-negotiable: no-pay-to-win; cosmetic-only.
8. Add Lane Wars 2v2.
9. Add **patch-1 commander per civilization** (2026-04-25 Follow-up #6, requires PM direction) — one additional historical / mythic commander per civ; expands commander choice from 3 to 6 without changing civ roster size.
10. Expose **Foresight-coin cross-civ borrowing mechanic** (2026-04-25 Follow-up #7) — first controlled multi-civ play, still constrained by per-civ identity.
11. Polish pass: art, sound, UX, onboarding, accessibility (§2.4a floor validation + WCAG 2.3.1 re-audit).

Each phase has its own validation gate. See Phase 6. PvE campaign scope (the deferred AGES concept per 2026-04-25 Follow-up #8) may insert between phases 6 and 7 once PM-ratified — it can reopen §4.7 enemy direction per-chapter and §3.5 tier pacing.

## 5.3 Art and tone direction

Per the 2026-04-25 real-cultures ratification, the world aesthetic is now **"mundane names outside, myth inside" — real-world cultures rendered at high legibility with native myth revealed through tier progression and Fusion endgame**. Candidates:

- **Stylized vector / painted flat** — Kingdom Rush reference. Legibility-forward; per-civ palette (Greek blue/white, Aztec red/gold/green, Norse grey/steel/deep-green) carries civ identity. Handles the "high-school recognizable" discipline well because iconic tower silhouettes (Pyramid, Phalanx shield, Longhouse gable) render cleanly at any zoom.
- **Isometric diorama** — Bloons TD 6 reference. Heavier art burden; dioramic civ-districts are marketable but multiply art pipeline.
- **Silhouette-forward mythic** — cheapest, most distinctive. The Fusion-to-Gods endgame (mortal Demigod → named God, e.g., Hercules + Jason → **Zeus**) benefits from dramatic silhouette-forward staging; the Gods should read as *silhouette events* on the board.

**Leading direction (placeholder, not ratified): hybrid — stylized vector for T1-T3 tower bodies (civ palette + iconic silhouette cues), silhouette-forward mythic treatment for T4 Demigods and Gods.** This matches "mundane outside, myth inside": mundane tower bodies read civ-legibly at gameplay speed; Demigods and Gods get trailer-moment treatment.

The prior "silhouette-forward mythic is the only candidate" framing (2026-04-21 dungeon-cosmology) is **superseded** by real-cultures: civ-coded visual identity needs more color + iconography than pure silhouette. Silhouette-forward mythic remains a load-bearing *ingredient* at the T4/God layer, not the whole style.

Cultural-sensitivity pass (2026-04-25 Follow-up #5) is a **mandatory gate before any art lock** — especially Aztec visual representation (avoid caricature), 300-movie-ideology audit for Leonidas visual direction, and TV-show-vs-history framing for Ragnar's visual direction.

Art director contract discipline unchanged: contract *before* vertical slice work begins, not during.

## 5.4 Naming conventions (LOCKED at Phase 5)

**Amendment banner — 2026-04-28 Lineages-row deletion + Civilizations-row addition.** Per [`decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md`](../decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) (closes Follow-up #10 from [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](../decisions/2026-04-27-commander-as-summoned-ability-avatar.md)). The Lineages convention (one-syllable kenning: Sinew / Ember / Forge / Crown / Veil) was orphaned by the 2026-04-25 real-cultures ratification and is removed. A Civilizations convention is added in its place. Original Lineages row text archived verbatim in [`CASCADE-history.md`](../CASCADE-history.md). No other §5.4 row is touched.

Duplicated in the [CONCEPT.md hub](../CONCEPT.md) for cross-reference; canonical location is here.

- **Game title:** TBD. Current working title is placeholder.
- **Commanders:** evocative titles, may be first-name + epithet. Never generic.
- **Civilizations:** real-culture proper nouns; the culture names itself. No invented placeholders. Launch roster: Greek / Aztec / Norse. Expansions follow the same pattern (real cultures only; no synthetic-myth coinages).
- **Ages:** evocative compound nouns, not dates (pattern: The Mudbrick Era).
- **Towers/Units:** job titles, never proper nouns (pattern: Warhost, Spirebinder).
- **Hybrids:** compound or hyphenated (pattern: Tank Corps, Rune-Smiths).
- **Enemies:** single-word kenning (pattern: Thornback, Nullspawn, Ashwake).
- **Heirlooms / inventory items:** mythic-fragment style (pattern: The Last Spear of Heidelberg).
- **Modes:** direct, muscular (pattern: Lane Wars, Horde, Campaign). Not florid.

## 5.5 Engine choice

**Leading choice:** Godot 4, 3D scene with angled orthographic camera (StarCraft/Warcraft III style). GDScript for most game logic, C# for performance-critical paths if needed.

**Alternatives considered:**
- Unity — larger ecosystem, more middleware, more tutorials. Cons: licensing, corporate drift.
- Unreal — overkill for this genre. Cons: C++ or Blueprints overhead, royalty structure, heavy build pipeline.

**Locked at:** end of Phase 4.

## 5.6 Exit condition for Phase 5

MVP scope agreed. Build order sequenced. Art direction picked. Naming conventions locked. Engine locked. Art director contracted. Initial sprint plan sequenced.

→ **Hand off to [Phase 6](phase-6.md).**
