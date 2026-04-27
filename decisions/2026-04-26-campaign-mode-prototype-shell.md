# Decision — Campaign mode: enable playable shell with 3-act / 30-wave structure

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (mode menu card, `startMode("campaign")`, HUD `refreshModeLabel`), `PROGRESS.md` (Phase 10.2 advance)

---

## Decision

Solo Campaign in the prototype is no longer a disabled card. It now starts a 30-wave match (`BALANCE.MATCH_WAVES = 30`, up from the prior placeholder `11`) and the match HUD renders the active campaign act in the mode-label slot: "Campaign · Act I — Rising" through "Act III — Reckoning", with the act recomputed on every `updateHUD()`. Autosave between sessions is **not** included; that is C5/C6 (engine port) work and the card copy now states this explicitly. Tutorial, Skirmish, Horde paths are unchanged.

## Context

Long-distance-run Round-3/Round-4 swarm review reached zero P0/P1 issues. Per the user's locked answer ("Exit when zero P0/P1 issues remain, then build the highest-value missing prototype scene") the next move was to surface the most visible scene gap. The grayed-out "Phase 10.2 — stub" Solo Campaign card was the loudest. `startMode("campaign")` was already wired to `goto("match")` with a placeholder 11-wave count; the only blockers were the disabled card attribute and the absence of any UX signal that campaign differs from skirmish.

The 30-wave / 3-act structure is already ratified in `decisions/2026-04-25-q2-real-cultures-direction-ratified.md` and CONCEPT §4.7 R11. Wiring the prototype to that count is alignment, not new design.

## Alternatives considered

- **Option A — Leave disabled, defer to C5/C6.** Would keep the card honest about "not wired," but the card is in fact wired; the disabled attribute was the lie. Rejected.
- **Option B — Enable with 11-wave placeholder.** Cheap unlock, but plays identically to Skirmish-with-more-waves. The act structure is the design's identity for campaign; without it, "campaign" is just a long skirmish. Rejected as missing the value.
- **Option C — Enable with 30 waves + act-aware HUD label.** (Chosen.) Smallest code that makes campaign feel structurally different from skirmish. No content/balance changes — wave defs still come from `deriveWaveDefs(30)`. Acts are presentation only.
- **Option D — Add per-act enemy theming, autosave, antagonist boss spawn.** Real campaign content. Rejected as scope: this is C5/C6 + balance work, not a prototype scene wire-up.

## Reason chosen

Option C respects "Port findings, not code." The finding is: act-divided wave structure communicates campaign identity even without bespoke content per act. The engine port can later swap `CAMPAIGN_ACTS` for data-driven act definitions (per-act tile palette, music, antagonist trigger) — the prototype encodes only the shape.

3x debug loop:
- **Loop 1 (attack):** "30 waves of identical content is boring; players will quit at wave 12." — Counter: the prototype's job is to validate the *shell*, not to ship a campaign. The boredom is a balance problem the engine port owns. The HUD's act label tells the player the structure exists.
- **Loop 2 (steelman):** "Add at least an act-2 / act-3 difficulty bump to make it feel different." — Reasonable but `deriveWaveDefs` already scales linearly with wave index, so wave-25 is harder than wave-5. No additional balance work needed for the prototype.
- **Loop 3 (synthesis):** Ship the shell. Document that act content is C5/C6.

## Reversibility note

Easy. To revert: re-disable the card, drop `CAMPAIGN_ACTS` + `refreshModeLabel`, restore the old inline ternary, set MATCH_WAVES back to 11. No persistent state crosses session boundaries (autosave is explicitly out of scope), so reverting cannot strand any save data.

## Follow-ups

- C5/C6 (engine port) owns: act-keyed wave generators, antagonist boss spawn at wave 30, autosave, per-act music/palette swaps.
- PORT-NOTES.md: add a row noting that prototype's `CAMPAIGN_ACTS` constant is presentation-only — engine port should treat acts as content-driven entities, not HUD strings.
- PROGRESS.md: Phase 10.2 row advances from "stub" to "playable shell — content placeholder."
