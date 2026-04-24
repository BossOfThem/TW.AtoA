# Decision — Phase 1 vision reopen: synthetic mythic-history braid

**Date:** 2026-04-24
**Status:** Accepted
**Reversibility:** Hard
**Affects:** `CONCEPT.md` Phase 1 (vision / world / theme / shape), Phase 3 (hybrid topology — reopened for re-evaluation), Phase 4 (age model — deferred pending world), project title (working title "Ash to Altar" de-anchored), `CASCADE.md` current work pointer, `PROGRESS.md` queue. Does **not** touch: `concept/phase-5.md §5.4` naming conventions [LOCKED], `concept/phase-2.md §2.4a` accessibility floor [LOCKED], core mechanics contract (tower-defense + merge + debuff + magic).

---

## Decision

Phase 1 is reopened in full. The prior 2026-04-21 direction — a 3/3/3 lineage-count, dungeon-cosmology framing, and "Ash as enabler" motif, informally ratified but never filed as a decision entry — is **superseded**. Vision, theme, world shape, hybrid topology, and the working title "Ash to Altar" are all back on the table. The thematic direction for the reopen is a **synthetic mythic-history braid**: a single invented world whose raw material is drawn jointly from real-world history, comparative religion, mythology, and philosophy — not a remix of any one source, and not a pastiche of all four side-by-side, but a deliberately braided synthesis that reads as its own cosmology. The age model (within-match vs. seasonal vs. campaign-chapter) is **deferred** and will not be decided until the world, story, and background have enough shape to constrain the choice. Mechanics (TD / merge / debuff / magic) remain fixed. §2.4a accessibility floor and §5.4 naming conventions remain locked. Prototype is frozen against concept edits until the reopen ratifies; the Step 5 playtest gate and Step B prototype-reshape plan are downstream of this decision, not priorities.

## Context

Two playtest-adjacent pressures converged. First, the PM read the cumulative 2026-04-20 DNA-injection pass (TW / HoMM / AoE / SC-WC3 lineage, commander-on-field, age-as-civ-history, spontaneity events) against the 2026-04-21 informal direction and judged that the world/theme floor was load-bearing but under-specified — the 3/3/3 + dungeon-cosmology + Ash-enabler framing was sketched at the roster/mechanics layer but had never been stress-tested as a *world*. Second, the thematic ambition has widened: rather than a single inspirational spine (e.g., ash-to-altar ritual arc), the PM wants a world whose texture reads as the product of historical, religious, mythological, and philosophical sediment at once. That ambition does not fit inside the prior framing without silent edits to Phase 1, which CLAUDE.md forbids. The correct move is a proper reopen.

The 2026-04-21 direction is treated as superseded even though it was never filed. Informal ratifications lose to dated decision entries, which is why this one exists.

## Alternatives considered

- **Option A — Narrow reopen (theme only).** Keep vision, shape, hybrid topology, and title locked; reopen only the thematic surface. Rejected: the PM's "synthetic mythic-history braid" is not a surface reskin. It implies cosmology, age-model semantics, and potentially hybrid topology (e.g., whether lineages are civilizations, pantheons, philosophical schools, or something braided across all three). Holding shape and topology frozen while theme rewrites underneath them would force exactly the kind of silent upstream edit the cascade forbids.
- **Option B — Full reopen including mechanics.** Reopen Phase 1 *and* the TD/merge/debuff/magic mechanics contract. Rejected: mechanics are the most externally validated part of the concept — they survived two playtests and the DNA pass. Reopening them would throw away stable ground to solve a problem that lives upstream of mechanics. Mechanics are the constraint the world must fit, not the variable.
- **Option C — Full Phase 1 reopen; mechanics + [LOCKED] items preserved; age model deferred.** (Chosen.) Vision, theme, world shape, hybrid topology, and working title reopened together because they are mutually constraining. Mechanics, §2.4a, and §5.4 preserved because they are externally stable or explicitly locked. Age model deferred because it is downstream of world/story — deciding it before the world is pitched would force the world to fit a mechanical schedule rather than the other way around.

## Reason chosen

Option C is the only choice that honors cascade discipline (no silent edits to Phase 1 from downstream theme ambition), preserves earned ground (mechanics, locked items), and refuses premature commitment (age model).

**3x debug loop.**

*Loop 1 — aggressive critique.* A full Phase 1 reopen at this point is expensive. Twenty-plus 2026-04-20 decision entries reference a concept surface that was implicitly the prior direction; reopening Phase 1 risks invalidating commander-on-field identity, age-history flavor banners, the biome `mapmods.json` sketch, and the commander-pick silhouette roster — all of which were written against an unstated world. "Synthetic mythic-history braid" is also dangerously underconstrained: four source domains (history, religion, mythology, philosophy) multiplied together produce an almost unbounded design space, and without a sharper rubric the reopen can drift for sessions. Deferring the age model sounds prudent but risks becoming permanent deferral — age-gate mechanics are the pivot the whole prototype turns on, and if the world never decides, the age model never decides, and prototype progress stalls. The title reopen specifically is low-value churn; "Ash to Altar" is explicitly placeholder per §5.4 and nothing in the repo depends on it being final. Finally, Reversibility Hard is correctly labeled but under-costed: if the reopen lands a world direction that later needs to reverse, every 2026-04-20 decision entry that name-drops commanders, ages, or biomes becomes a candidate for re-ratification.

*Loop 2 — steelman.* Loop 1 overweights sunk cost. The 2026-04-20 entries were written against a world that was never actually specified — they survive a Phase 1 reopen precisely because most of them are mechanical (meta-UI envelope, save model, audio architecture, accessibility floor, commander identity floor's *structural* half) rather than thematic. The thematic half of those entries (commander lore strings, age flavor banners, biome names in `mapmods.json`) was always labeled `[PROPOSAL]` and was always going to be rewritten once the world was pinned. Loop 1's worry about "unbounded design space" is real but is addressed by the rubric: *synthetic* rules out remix; *braided* rules out side-by-side; *one invented world* rules out multiverse. Those three constraints plus §5.4's naming conventions collapse the space fast. On the deferral risk: age model deferral is not indefinite — the reopen gates it on "world, story, background established," which is a reachable milestone, not a moving one. On the title: the title reopen is costless because nothing depends on it, and leaving it locked would implicitly constrain thematic direction (an "Ash to Altar" world pitch is narrower than a free one). On Reversibility Hard: the label is exactly what cascade discipline requires — it ensures any future sub-decision that contradicts this one must reopen Phase 1 again rather than silently edit.

*Loop 3 — synthesis.* Ratify the full reopen, but ship it with three stop-gaps against Loop 1's real concerns. (1) Scope fence: this decision reopens Phase 1 *only*; downstream phases re-evaluate only when Phase 1 exits and names a constraint they violate. 2026-04-20 mechanical decisions stay Accepted. 2026-04-20 thematic `[PROPOSAL]` content expects rewrite. (2) Completion rubric: Phase 1 exits when the PM can answer, in one page, *what the world is*, *what the player's role in it is*, and *what the hybrid topology expresses about the world* — these three answers together gate age-model reopening. (3) Pacing discipline: question-per-turn cadence as the PM specified, starting with the world pitch, then role, then topology, then age model. No batching into a single omnibus Phase 1 rewrite.

Option C with those three stop-gaps is the choice.

## Reversibility note

**Hard.** Undoing this reopen would require (a) restoring the 2026-04-21 informal direction as a filed decision entry, (b) rewriting or superseding every Phase 1 artifact this reopen produces, and (c) re-ratifying any downstream decisions that this reopen invalidated. The Hard label is the point: it raises the bar for future sub-decisions to contradict the reopened vision, which is exactly the cascade protection a Phase 1 change deserves.

Mechanical decisions filed 2026-04-20 remain Accepted and are not invalidated by this reopen. `[PROPOSAL]` thematic content in commanders, ages, and `mapmods.json` / `events.json` is expected to be rewritten and is not counted as reversal cost.

## Follow-ups

1. **Next turn (this session):** Q2 — world pitch. One question, PM drives pacing. Output is a candidate world-statement draft, not a ratification.
2. **Bump `CASCADE.md` current work pointer** to "Phase 1 reopen in flight — synthetic mythic-history braid" in a subsequent turn (pointer edit is its own step per one-file-per-turn cadence).
3. **Bump `PROGRESS.md`** with a 2026-04-24 session-log row and an explicit Step-5 parking note once the pointer bump lands.
4. **Defer:** age-model decision, `mapmods.json` biome rewrite, commander lore rewrite, working-title decision — all gated on Phase 1 exit.
5. **Stop-gap rubric (for Phase 1 exit):** PM answers in one page — what the world is, what the Commander's role in it is, what hybrid topology expresses about the world. Until that page exists, Phase 1 stays open.
6. **Prototype stays frozen** against concept edits until reopen ratifies. Step 5 playtest and Step B prototype-reshape plan remain downstream, not priorities.
