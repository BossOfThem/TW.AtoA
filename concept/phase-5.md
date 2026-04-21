---
**Status:** Draft
**Last reviewed:** 2026-04-21
---

# Phase 5 — Implementation planning

*What gets built, in what order, to prove the vision before investing in content.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-4.md](phase-4.md). Next: [phase-6.md](phase-6.md).

## 5.1 MVP slice

The smallest playable thing that answers: *"Does the commander + tier + lineage combination produce a game that a Tower Wars fan wants to keep playing?"*

Under the [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md), **the MVP and the launch roster converge** — 3 is already the lean-launch floor per `concept/phase-3.md §3.2`, so MVP is the full roster, not a strict subset. Prior MVP spec (2 commanders / 2 lineages / 5 ages / 1 hybrid) is superseded by this decision.

- **Three commanders** (A / B / C — Ash-leaning / Nature-leaning / Prayer-leaning per §3.2). Full launch roster.
- **Three lineages fully built** (Ash, Nature, Prayer) — full lineage surface.
- **Three tiers** (Dust → Form → Apotheosis) under the Ash→Altar dungeon-cosmology arc per §3.5. Three tiers is the committed depth *and* the minimum depth for tier-persistence to emerge — the prior "five-age minimum" concern dissolves because three tiers is the ratified shape.
- **Two hybrids** — one Ash×Nature, one Ash×Prayer (per §4.3). Nature×Prayer does not hybridize.
- **One mode**: Solo vs AI on one map.
- **Basic UI**: unit picker, health bar, economy display, tier gate.
- **No divergence forks at MVP.** Fork pool is rescoped OPEN per §4.2 under the 2-tier-transition model; ratification can add the Dust→Form fork to MVP if it lands before MVP lock.
- **No meta progression** (no commander XP, no backpack, no battle pass).
- **No multiplayer yet.**
- **MVP commanders honor the §4.1 identity floor.** All three MVP commanders ship with the full [PROPOSAL] floor (portrait + variant, silhouette + variant, 12 voice lines, signature, passive, tilt, 20-level ladder, 3 cosmetic slot types with 1 default item each). Without the floor, the identity-promise validation (see Phase 6) is unfalsifiable.

If the MVP is fun, the vision works. If it is not fun, no amount of content added on top will save it.

## 5.2 Build phases after MVP

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

## 5.3 Art and tone direction

Three candidates:
- **Stylized vector / painted flat** — Kingdom Rush reference.
- **Isometric diorama** — Bloons TD 6 reference.
- **Silhouette-forward mythic** — cheapest, most distinctive. *Leading choice — now **load-bearing** under the dungeon-cosmology aesthetic locked 2026-04-21.*

Per the [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md), the PM locked the world aesthetic as *"dungeon-like and mysterious"* and the match arc as a 3-tier Ash→Altar descent (§3.5). That upstream frame is incompatible with bright stylized-vector or chipper isometric-diorama directions — silhouette-forward mythic is no longer merely leading, it is the only candidate consistent with Phase 1/3. Reverting to either alternative now requires a Phase 1/3 reopen, not a Phase 5 adjustment.

Silhouette-forward mythic requires strong art direction to avoid feeling underbuilt. Contract an art director *before* vertical slice work begins, not during.

## 5.4 Naming conventions (LOCKED at Phase 5)

Duplicated in the [CONCEPT.md hub](../CONCEPT.md) for cross-reference; canonical location is here.

- **Game title:** TBD. Current working title is placeholder.
- **Commanders:** evocative titles, may be first-name + epithet. Never generic.
- **Lineages:** one-syllable, ancient-feeling nouns (pattern: Sinew, Ember, Forge, Crown, Veil).
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
