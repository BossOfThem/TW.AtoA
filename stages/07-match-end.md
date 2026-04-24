# Stage 07 — Match End

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design) / 5 (Implementation planning — UX polish)
**Upstream deps:** [Stage 04 — in-match core](04-in-match-core.md), [Stage 05 — age evolution](05-age-evolution.md), [Stage 06 — hybrids & fusion](06-hybrids-fusion.md), [PLAYER-JOURNEY §Match end](../PLAYER-JOURNEY.md)
**Downstream impact:** [Stage 08 — meta progression](08-meta-progression.md)
**Open questions:** See below.
**Research backing:** [04-monetization-liveops.md](../research/04-monetization-liveops.md) (drop rates, battle-pass XP pacing)
**Last reviewed:** 2026-04-26

---

## Amendment 2026-04-26 (stub-level — real-cultures frame cascade)

Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility **Hard**) + [`decisions/2026-04-26-phase-1-exit-one-pager.md`](../decisions/2026-04-26-phase-1-exit-one-pager.md) — the Scope §"MVP lineage, final age reached" is **superseded**. Under the current frame the stats panel summary statistics should read:

- **MVP civilization** (Greek / Aztec / Norse) instead of "MVP lineage."
- **Final tier reached** (T1/T2/T3/T4) instead of "final age reached," plus **Fusion count** (0-3 Gods fused) and **named Gods fused** (from the 9 locked recipes).
- **Tribute earned / Tribute spent** + **Divinity earned / Fusions executed** replace any gold/knowledge/influence totals.
- Per-type damage breakdown per the 7-type × 5-armor RPS matrix ([`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md)) is an autonomy-safe addition once the prototype reshape plan ratifies.

Commander-specific voice-line copy (first-win / loss-streak / level-up) inherits the 2026-04-25 locked commander roster + must pass the cultural-sensitivity gate (Follow-up #5) before lock. Leonidas loss-line is particularly sensitive (no 300-adjacent jingoism); Montezuma II first-win line must avoid caricature; Ragnar lines should lean to saga-tradition not TV-show framing.

§5.4 naming conventions **[LOCKED]** untouched. §2.4a accessibility floor **[LOCKED]** untouched. Body below preserved for traceability; dedicated Stage-07 rewrite deferred to a dedicated reopen pass.

---

## Scope

From final wave resolution to return-to-menu. Covers:

- Victory / defeat screen — tone, pacing, skippability.
- Stats panel — waves survived, towers built, creeps sent, kills, MVP lineage, final age reached.
- XP award flow with level-progress bar.
- Battle pass progression award.
- Backpack drop check (evolution components, cosmetic shards, rarity rolls).
- Next-match nudge — Replay / Return to Menu / Queue Again.
- Level-up or new-unlock flourishes.

## To be written (Phase C pass)

Tight stage. Mostly UX intent + data surfaces. Drop-rate tuning is a Phase 5 polish concern; this stage fixes the *framework* only.

## Open questions (seed list)

- How aggressive is the "Queue Again" nudge — CTA prominence.
- Stats panel default view — summary vs detail.
- Loss framing — tone of defeat screen (harsh, supportive, neutral).
- Does the commander have unique voice lines for first-win, loss-streak, level-up.

## Verification

- Players return to menu or queue again within 30 seconds of match end in ≥ 70% of cases.
- Loss-screen sentiment in playtesting is "I want to try again," not "the game punished me."
