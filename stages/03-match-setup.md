# Stage 03 — Match Setup

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design) / 4 (Specification — economy spec)
**Upstream deps:** [Stage 02 — mode select](02-mode-select.md), [CONCEPT §3.1 Core match loop](../CONCEPT.md), [CONCEPT §4.6 Economy](../CONCEPT.md)
**Downstream impact:** [Stage 04 — in-match core](04-in-match-core.md)
**Open questions:** See below.
**Research backing:** [02-theme-era.md](../research/02-theme-era.md) — era spine decision lands here.
**Last reviewed:** 2026-04-26

---

## Amendment 2026-04-26 (stub-level — real-cultures frame cascade)

Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility **Hard**) + [`decisions/2026-04-26-phase-1-exit-one-pager.md`](../decisions/2026-04-26-phase-1-exit-one-pager.md) — the Scope §"Starting economy (gold, knowledge, influence starting pools)" is **superseded**. Under the current frame the launch currencies are **Tribute** (primary; historic-name replacement for gold/mineral; earned per wave + per kill) and **Divinity** (mythic token; 6-per-match cap; earned 1 per boss round at waves 5/10/15/20/25/30). Knowledge/Influence are retired. Starting pools are a Tribute pool only — Divinity is zero at match start and earned in-match.

The era-spine framing under "To be written" is **constrained** by the 2026-04-25 ratification: map visual identity + tonal framing follow the civilization the player chose at Commander pick (Greek / Aztec / Norse). "Starting age" reframes to **starting tier** (T1 by default). The `ages.json` → `tiers.json` data rename is part of the Proposed [prototype reshape plan](../decisions/2026-04-26-prototype-reshape-plan.md) (Step C1).

Commander banner reveal + signature voice line inherit the 2026-04-25 locked Commander roster (Leonidas / Montezuma II / Ragnar Lothbrok); specific voice-line text per commander is post-launch / post-cultural-sensitivity-pass scope.

§5.4 naming conventions **[LOCKED]** untouched. §2.4a accessibility floor **[LOCKED]** untouched. Body below preserved for traceability; dedicated Stage-03 rewrite deferred to a dedicated reopen pass.

---

## Scope

Everything between mode select and the first wave spawning:

- Map pick / map assignment.
- Lane assignment (PvP).
- Starting economy (gold, knowledge, influence starting pools).
- Pre-wave build phase — first tower placements.
- Commander banner reveal with signature voice line.
- Camera intro sweep, if any.
- Opponent/teammate reveal (PvP/co-op).

## To be written (Phase C pass)

First stage where the era-spine decision from [02-theme-era.md](../research/02-theme-era.md) materially shows up — map visual identity, starting age, tonal framing.

## Open questions (seed list)

- Map variety at launch (count, biomes, tied to era spine).
- Pre-wave timer length — enough to build, not enough to stall.
- Draft/ban phase in PvP — yes, no, or optional toggle.
- Lane asymmetry — always mirror, or can maps be asymmetric.

## Verification

To be populated. Goal: the player feels "I know what match I'm about to play, I know who I am, I'm ready to build."
