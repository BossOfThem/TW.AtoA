# Stage 02 — Mode Select

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design)
**Upstream deps:** [Stage 01 — commander pick](01-commander-pick.md), [CONCEPT §3.6 Game modes](../CONCEPT.md)
**Downstream impact:** [Stage 03 — match setup](03-match-setup.md)
**Open questions:** See below.
**Research backing:** [01-genre-pulse.md](../research/01-genre-pulse.md), [05-demographics-platform.md](../research/05-demographics-platform.md)
**Last reviewed:** 2026-04-19

---

## Scope

Launch mode roster (Campaign, Solo vs AI, Co-op Horde, Lane Wars 1v1, Lane Wars 2v2, Custom Lobby), mode-select UX, matchmaking and lobby surfaces, unlock gating by commander level or campaign progress.

## To be written (Phase C pass)

Content will draw on [01-genre-pulse.md](../research/01-genre-pulse.md) to answer: is the audience mostly solo (skew Campaign/Skirmish) or PvP (skew Lane Wars)? That shapes which mode gets default cursor position and marketing weight.

## Open questions (seed list)

- Default cursor on the mode-select screen (Campaign vs Skirmish vs Lane Wars).
- Matchmaking rank visibility — show during placement or hide until placed.
- Party system UX — invites, voice, size limits per mode.
- Which modes are offline-capable (leading: Campaign + Solo vs AI).
- Mode-unlock gating — all modes from day 1 or earn-them-in?

## Alternatives considered

To be populated.

## Verification

- Median time from menu to in-match countdown ≤ 60 seconds (solo modes).
- 1v1 queue finds match in ≤ 60 seconds during active hours; <5% disconnect.
