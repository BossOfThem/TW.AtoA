---
**Status:** Draft
**Last reviewed:** 2026-04-21
---

# Phase 6 — Validation

*How we know the game is working before we commit to finishing it.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-5.md](phase-5.md). Next: [phase-7.md](phase-7.md).

## 6.1 Primary question for the MVP

Does the commander + tier + lineage combination produce moment-to-moment fun, AND does the tier-persistence feeling emerge by the end of Form (tier 2) at the latest?

If yes, the vision is viable. If no, the vision is wrong and Phase 1 must be reopened.

Three tiers in the MVP is deliberate under the [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md): the full Ash→Altar arc (Dust → Form → Apotheosis) is the ratified shape, so MVP validates the full arc rather than a truncated slice. Prior "five ages is the minimum" framing is superseded — under the 3-tier arc, the validation bar is tier-persistence emerging by end of Form, not a linear-age count.

## 6.2 Secondary questions (in order)

- Do new players understand commanders and lineages within their first match?
- Do players re-pick the same commander on match 2 or try another? (Indicates whether commander identity is sticky or shallow.)
- Does the tier-persistence callback feel earned by the end of Form (tier 2)?
- Is match length right, too long, or too short?
- Which lineage gets picked least, and is that a bug or a feature?
- Does solo TD hold attention without multiplayer? (Critical — solo must carry the game independently.)
- Do hybrids feel discovered or feel hidden?

## 6.3 Playtesting approach

- **Internal playtesting** with the two-person dev team through MVP completion.
- **Closed alpha** with 5–10 external playtesters (TD/TW fans) for the first post-MVP expansion (full 3/3/3 roster already in MVP per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md); closed-alpha milestone adds one PvP mode + both hybrid families Ash×Nature and Ash×Prayer live).
- **Open alpha** after multiplayer is stable and all commanders exist, to catch late-game balance and cold-start matchmaking issues.

## 6.4 Success metrics per build phase

Under the [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md), MVP converges with the full 3/3/3 launch roster — the prior "Post-five-lineages" and "Post-eleven-ages" milestones are obsolete (MVP already has all 3 lineages and all 3 tiers). Remaining milestones:

- **MVP:** 70%+ of playtesters say they would play a second match. 50%+ report the **tier-persistence** feeling by end of Form. Median session length ≥ 15 minutes. No lineage picked less than 20% of the time across tracked runs (tighter than the prior 10% under a 5-lineage shape — with only 3 lineages, a lineage at <20% pick rate is a real design failure). **Commander re-pick on match 2 ≥ 40%** (measures whether the §4.1 identity floor produces stickiness; promoted from §6.2 secondary via [2026-04-20 commander identity floor](../decisions/2026-04-20-commander-identity-floor.md) — rebased by 2026-04-21).
- **Post-hybrid-families:** both Ash×Nature and Ash×Prayer families discoverable in ≥ 60% of tracked runs by match 3.
- **Post-multiplayer:** Median ranked match finds opponent in <60 seconds during active hours. <5% disconnect rate.
- **Alpha:** Average session length ≥ 30 minutes. Day-2 return rate ≥ 40%.

## 6.5 Exit condition for Phase 6

A validation plan exists for every build phase. Success metrics are defined in advance, not defined after the data comes in. The team knows what would make them cancel the project.

→ **Hand off to [Phase 7](phase-7.md).**
