# Stage 08 — Meta Progression

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design) / 5 (Implementation planning — monetization lock)
**Upstream deps:** [Stage 01 — commander pick](01-commander-pick.md), [Stage 07 — match end](07-match-end.md), [CONCEPT §3.7 Meta systems](../CONCEPT.md), [PLAYER-JOURNEY §Commander/Backpack/BP/Store surfaces](../PLAYER-JOURNEY.md)
**Downstream impact:** Cycles back to [Stage 00 — session start](00-session-start.md) (returning-player state)
**Open questions:** See below.
**Research backing:** [04-monetization-liveops.md](../research/04-monetization-liveops.md)
**Last reviewed:** 2026-04-19

---

## Scope

Between-match persistence:

- **Commander progression** — XP, levels, cosmetics, voice lines, signature-ability tiers, portrait frames.
- **Backpack** — evolution components, cosmetic items, commander-specific items, consumables (if any), gifts.
- **Battle Pass** — free track + premium track, seasonal theme, 10–12 week length placeholder.
- **Cosmetic Store** — skins, voice packs, tints, emotes, bundles. Zero pay-to-win.
- **Account-wide** vs **per-commander** persistence policy.

## To be written (Phase C pass)

Content backed by [04-monetization-liveops.md](../research/04-monetization-liveops.md). This stage is where the "realistic live-ops envelope for a two-dev team" gets enforced in UX — season length, content-drop cadence, store refresh rate.

## Open questions (seed list)

- Progression policy: per-commander XP + account-wide cosmetics (leading) vs shared-everything.
- Season length — 10–12 weeks, or longer.
- Battle pass premium price — to be set after monetization research.
- Pay-to-skip — NO at launch (confirmed by principle); revisit post-launch.
- Consumables — in or out of scope.
- Premium cosmetic rarity tiers — how many, how signaled.

## Verification

- Day-2 return rate ≥ 40% in alpha.
- Zero in-store items provide gameplay advantage (enforced by design review per [CLAUDE.md](../CLAUDE.md)).
- Season cadence survivable by a two-dev team for ≥ 3 consecutive seasons without crunch.
