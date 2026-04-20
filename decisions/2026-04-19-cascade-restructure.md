# Decision — Cascade Restructure: Player-Journey-Ordered Docs + Deep-Dive Research

**Date:** 2026-04-19
**Status:** Accepted
**Reversibility:** Medium (restructuring back is possible but would require re-flattening 15+ docs)
**Affects:** [README.md](../README.md), [CLAUDE.md](../CLAUDE.md), [CONCEPT.md](../CONCEPT.md), [PLAYER-JOURNEY.md](../PLAYER-JOURNEY.md), new [CASCADE.md](../CASCADE.md), [stages/](../stages/), [research/](../research/)

---

## Decision

Reorganize the project from two flat design docs (`CONCEPT.md` + `PLAYER-JOURNEY.md`) into a waterfall/cascade of 200–600-line MDs structured around the player journey, with a deep-dive market research cascade feeding into stage decisions and a dated decision log. Consolidate to root `C:\TW.AtoA\`; archive `tw-commanders-starter\`. Work stages in strict downstream order: session start → commander pick → mode select → match setup → in-match core → age evolution → hybrids → match end → meta.

## Context

The previous structure was:

- Flat — two long files, no per-stage drill-down.
- Duplicated — same `CONCEPT.md` in two places.
- Research-thin — no evidence base; major claims asserted, not tested.
- Not built to grow — no navigation spine for future Claude sessions to pick up where prior sessions left off.

The user (PM/research hat) wants to pressure-test the concept against 2024–2026 market reality *before* any engine or code decisions. This required:

1. A doc structure that grows gracefully.
2. A research backbone that produces evidence, not vibes.
3. A discipline that works one stage at a time, starting from login.

## Alternatives considered

- **Option A — keep the flat two-doc structure and add a third "research.md."** Rejected: does not scale, does not let per-stage work be isolated, research would become a monolith.
- **Option B — per-topic docs (one per lineage, one per age, etc.).** Rejected: topic-sharding does not map to how the user experiences the game; makes player-journey review hard; encourages content-first rather than UX-first thinking.
- **Option C (chosen) — player-journey cascade + research cascade + decisions log + consolidated root.** Maps 1:1 to the user's experience, scales, isolates work, preserves cascade discipline from [CLAUDE.md](../CLAUDE.md).

## Reason chosen

Matches the user's stated mental model ("one at a time starting with when the user logs in"). Preserves the waterfall discipline already established in `CONCEPT.md`. Creates a navigation spine (`CASCADE.md`) that future sessions can read to orient in < 2 minutes. Isolates deep-dive research into its own cascade so stages don't bloat. Keeps the decision log honest.

3x debug loop synthesis:

- **Loop 1 critique:** "15 files is overhead for a two-dev team; will drift."
- **Loop 2 steelman:** "Status fields + last-reviewed dates + single index make drift visible; the overhead is paid by every future Claude session saving hours of hunting."
- **Loop 3 synthesis:** adopt with strict enforcement of the Stage doc standard header and CASCADE.md as single source of truth for "what exists and where." Drift becomes a housekeeping task, not an invisible rot.

## Reversibility note

Medium. To reverse, content would need to be re-flattened into two monoliths. Cross-links would all break. Decision log entries would become orphans. Not destructive — original content is preserved in the archived starter folder. But undoing costs several hours of rework.

## Follow-ups

- [ ] Phase A complete: all stubs present, CASCADE.md populated, README + CLAUDE updated, starter archived.
- [ ] Phase B first docs: `research/00-methodology.md`, `research/03-commander-archetypes.md`.
- [ ] Phase C first pass: `stages/00-session-start.md`, `stages/01-commander-pick.md`.
- [ ] Checkpoint review with PM after Stage 01 lands.
