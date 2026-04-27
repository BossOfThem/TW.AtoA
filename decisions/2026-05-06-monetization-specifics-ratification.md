# Decision — Monetization specifics ratification (§4.8 exit-gate item #8 close)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** **Hard** (model-shape; commercial price-point Easy)
**Affects:** [`concept/phase-2.md §2`](../concept/phase-2.md) (DRG-reference monetization tension — read-only input), [`concept/phase-3.md §3.7`](../concept/phase-3.md) (progression track + Battle Pass — read-only input), [`concept/phase-4.md §4.1`](../concept/phase-4.md) (commander cosmetic-slot identity floor — read-only input), [`concept/phase-4.md §4.6a`](../concept/phase-4.md) (auxiliary economy = in-match Tribute/Divinity, NOT monetized — read-only input), [`concept/phase-4.md §4.8`](../concept/phase-4.md) (exit-gate item #8 ✅ ticked DONE), [`concept/phase-7.md §7.2`](../concept/phase-7.md) (Roadmap item #3 monetization specifics + #12 monetization model lock — read-only input), [`concept/phase-7.md §7.4`](../concept/phase-7.md) ("Go big at launch" non-negotiable + battle-pass-only-with-strict-no-p2w identity constraint — read-only input), [`research/04-monetization-liveops.md`](../research/04-monetization-liveops.md) (backing research — read-only input), [`README.md`](../README.md) (non-negotiables — `Cosmetic-only monetization. No pay-to-win.` — read-only input).

---

## Decision

Ratify the monetization model-shape close. Phase 2 (model tension), Phase 3 (Battle Pass + Inventory + Cosmetic store), Phase 4.1 (commander cosmetic-slot floor), Phase 4.6a (auxiliary economy is in-match-currency-only, not monetized), Phase 7.4 (no-p2w identity constraint) compose into a single coherent specification with **zero cascade-violations**. Specific commercial numerics (final price-point selection within the $5-15 envelope, Battle Pass tier count, season cadence in weeks) are flagged as **PM-decisional commercial surface** that does not reopen the model — they are tunable inside the locked frame at any time before launch.

`§4.8` exit-gate item #8 (`Monetization model specifics resolved (cosmetic-only; no-pay-to-win non-negotiable)`) flips ✅ DONE. Phase 4 advances to **7 of 11 exit-gate items closed** (#1 commander / #2 per-tower / #3 per-civ / #4 enemy direction / #5 mobile unit control / #7 economy paper-balance / **#8 monetization specifics**). Remaining: #6 Fusion-numerics / #9 Engine lock / #10 Art director / #11 Cultural-sensitivity Phase-4-exit.

## Context

The monetization frame is the *most-locked* surface in the codebase outside the §5.4 [LOCKED] naming conventions: it appears as a **non-negotiable** in [`README.md`](../README.md), as an **identity constraint** in `phase-2.md §2.4` and `phase-7.md §7.4` ("This is not a marketing concern. This is an identity constraint."), and as a **structural commitment** in `phase-3.md §3.7` (Battle Pass premium tier "rewarding cosmetics only (never gameplay power)") and `phase-5.md §5.1` step 7 (Backpack + Battle Pass + Cosmetic Store with no-p2w cosmetic-only mandate).

Three load-bearing architectural commitments sit underneath:

1. **DRG-reference model** (Phase 2.4 + Phase 7.2 #3) — Deep Rock Galactic's premium price + free earnable battle pass + optional cosmetic DLC is the explicit reference target. Not a placeholder; the reference frame.
2. **Aux economy ≠ monetization surface** (Phase 4.6a) — Send-Creeps / Damage Bonus / Tower-count expansion / etc. are spendable in-match Tribute/Divinity slots, not premium-currency / lootbox / gacha analogues. The aux economy is a *gameplay-balance* surface per [`2026-05-05 R7`](2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md), audited and ratified for paper-balance per [`Economy paper-balance ratification`](2026-05-06-economy-paper-balance-ratification.md). Ratifying this monetization decision must verify the aux economy stays mechanically gated, never paywall-gated.
3. **Commander cosmetic-slot floor** (Phase 4.1 identity floor) — every launch commander ships with 3 cosmetic-slot types with 1 default item each. The cosmetic-monetization surface is an *expansion* of this floor, not a *bypass* of it (any commander can ship with the default-only loadout and feel complete; cosmetic purchases are additive, never gating a different commander or a gameplay variant).

The remaining surface — the actual price tag on the box, the BP season schedule — is commercial decisional. I'm not pricing this game from a chair; PM is. The ratification's role is to verify that whatever PM picks inside the locked envelope (premium $5-15 / free-BP / cosmetic-DLC) cannot accidentally cross into p2w territory.

## Coherence audit — 4 checks, zero cascade-violations

### Check 1 — DRG-reference structural alignment

| Element | DRG (reference) | ATOA spec | Match |
|---|---|---|---|
| Base game | One-time premium purchase | Premium price $5-15 (Phase 2.4 + Phase 7.2 #3) | ✓ |
| Battle Pass | Free earnable through play | Free tier earnable through play (Phase 3.7 #3) | ✓ |
| BP premium tier | Optional, cosmetic-only | Optional purchase, cosmetic-only (Phase 3.7 #3) | ✓ |
| Cosmetic store | Optional DLC | Optional cosmetic DLC (Phase 2.4) | ✓ |
| Lootboxes | None | None — explicitly excluded (Phase 2.4: "NEVER gacha") | ✓ |
| Gameplay-advantage purchase | None | None — explicitly excluded (Phase 2.4: "NEVER gameplay advantage sold") | ✓ |

**Verification:** Six structural matches against the locked reference. No deviations. **PASS.**

### Check 2 — Aux economy ≠ monetization surface

| Aux slot (§4.6a) | Cost currency | Source of currency | Monetizable? |
|---|---|---|---|
| Damage Bonus | 1 Divinity | In-match boss drops + skill-bar escalation (R10) | **No** — earned in-match by play |
| Economy Bonus | 1 Divinity | Same | **No** |
| Tower-count expansion | 1-3 Divinity | Same | **No** |
| Send-Creeps | 100 Tribute baseline | In-match kill yield (R3) | **No** |
| Send-for-Interest (PvP-IW) | 1 Div unlock + 150 T/send | Same | **No** |
| Call-for-Help | 300 Tribute | Same | **No** |
| Maze Stone | 25 Tribute | Same | **No** |

**Verification:** Every aux slot is gated on in-match earned currency (Tribute kill-driven per R3, Divinity boss/skill-bar driven per R10). Zero entries gated on premium currency or paid unlock. The aux economy is *gameplay balance*, never a *commercial surface*. **PASS.**

### Check 3 — Commander cosmetic-slot floor preserves no-p2w

| Floor item (§4.1) | Default | Premium | Gameplay-affecting? |
|---|---|---|---|
| Portrait | Ship default | BP / store unlock | No (UI-only) |
| Silhouette | Ship default | BP / store unlock | No (visual-only) |
| Voice lines | 12 default | BP / store unlock additional VO | No (audio-only) |
| 3-ability kit | Locked per §4.1 | Not unlockable | (cosmetic-only mandate enforced) |
| Civ affinity | Locked per §4.1 lane locks | Not unlockable | (Hard-class lane lock per per-commander R1-R5) |
| 20-level ladder | XP-only progression | No purchase shortcut | No (no-p2w gate per Phase 4.0 table) |

**Verification:** Every paid cosmetic surface is UI / visual / audio additive. Every gameplay-affecting surface is locked behind XP earned through play with no purchase shortcut. The 20-level ladder explicitly carries the "**No gameplay-power gates** (solo-first + no-pay-to-win)" tag per `concept/phase-4.md` §4.0 table line 31. **PASS.**

### Check 4 — Phase 7.4 "Go big at launch" + identity-constraint resilience

`phase-7.md §7.4` carries the strongest non-negotiable language in the project: "Battle pass + cosmetic store works only with strict no-pay-to-win. One misstep burns audience trust permanently. This is not a marketing concern. This is an identity constraint."

| Pressure source | Pressure direction | Defense |
|---|---|---|
| Launch-revenue maximization | Increase paid surface | Cosmetic-only mandate caps at additive-only (Checks 1+3 hold) |
| Live-ops content cadence | Faster paid drop | Free BP earnable parity gates premium BP — premium can only cosmetically expand, not gameplay-expand |
| Competitor-feature pressure | Add gacha / lootbox | Phase 2.4 + Phase 7.4 explicit exclusion ("NEVER gacha") |
| Whale-spend optimization | Premium-only commander access | Phase 4.1 lane locks + 20-level ladder — every commander shipped with full ability kit; cosmetics never gate gameplay |

**Verification:** Four canonical pressure-source attacks against the model defended by structural locks. The identity-constraint framing means any reversal triggers Hard-class supersession (not Easy or Medium) — equivalent to reopening Phase 2 non-negotiables. **PASS.**

## Spine-doc edits

`§4.8` exit-gate item #8 flips ✅ DONE with reference to this ratification + the four-source lock chain (Phase 2.4 + Phase 3.7 + Phase 4.1 + Phase 7.4). No other prose changes — every load-bearing surface is already explicit in upstream docs.

## PM-decisional commercial surface (deferred, does not reopen model)

The following are tunable commercial decisions that **do not reopen this ratification**:

- **Final price-point** — $5-15 envelope locked; specific picked value (e.g., $9.99 vs $14.99 vs regional pricing) is commercial-team / store-policy territory.
- **Battle Pass season cadence** — locked-shape (free + premium tracks); specific season length (8 / 12 / 16 weeks) and tier count (per season) are live-ops-team territory.
- **Cosmetic DLC catalog cadence** — locked-shape (cosmetic-only); specific drop schedule is content-team territory.
- **Founder's edition / collector's edition variants** — permitted within cosmetic-only frame (cosmetic-only premium tiers allowed); specific bundle composition is publishing territory.

If PM picks a specific commercial number that violates the cosmetic-only / no-p2w model, the violation is detectable against this ratification's Check 1 + Check 3 + Check 4 — that escalation re-opens this ratification (Hard-class), not the model itself.

## Cascade discipline check

Hard guards verified untouched verbatim:

- **Non-negotiable: cosmetic-only / no-pay-to-win** — preserved (Checks 1+2+3+4).
- **Non-negotiable: solo-first** — preserved (no premium gate forces multiplayer / online play).
- **Non-negotiable: Go big at launch** — preserved; commercial scope expansion fits inside cosmetic-only model (Phase 7.4 framing).
- §5.4 + §2.4a [LOCKED] — no name additions / renames.
- 2026-04-25 content-skeleton — no civ / tower / commander / boss content.
- §4.1 commander identity floor — preserved verbatim (Check 3).
- §4.6a auxiliary economy — preserved verbatim (Check 2 verifies aux slots stay gameplay-currency-gated).
- §4.10 master damage equation — read-only.
- §4.11.* numerics floor — read-only.
- Per-commander R1-R5 / per-tower R1-RN / per-civ R1-RN — read-only.
- §4.7 Option C + R11 wave-composition variance grammar — read-only.
- §4.4 mobile-unit-control RN — read-only.
- Cultural-sensitivity Follow-up #5 — preserved (cosmetic naming follows §5.4 + Follow-up #5 review at Phase-4 exit; "Premium" / "Founder's" naming flagged for review timing).

Cascade-lint expected: only carried `94-files-vs-88-rows` finding (this round adds 1 file + 1 row → 95-vs-89, structural condition unchanged).

## Reason

The monetization model is the most-locked surface in the codebase. Authoring a multi-round arc to "design" it would invent design surface that is already settled — the deliverable is verification, not new content. The four checks (DRG-reference structural alignment / aux ≠ monetization / commander cosmetic-slot floor / Phase 7.4 identity-constraint resilience) are falsifiable: any future cascade-violation against any check re-opens the gate item.

Separating the model-shape (**Hard reversibility** — equivalent to reopening Phase 2 non-negotiables) from the commercial surface (**Easy reversibility** — tunable inside the locked frame) makes the gate-tick durable. PM picking a specific price tag pre-launch does not require re-doing this audit; PM proposing to add a gacha mechanic does, and the ratification's structure surfaces that distinction explicitly.

## Reversibility

**Hard for the model-shape; Easy for commercial price-point selection.**

- **Model-shape reversal** (e.g., adding gacha / lootbox / gameplay-advantage purchase / paywall on commanders / paywall on aux slots) — Hard-class. Requires reopening README.md non-negotiables + Phase 2.4 + Phase 7.4 identity-constraint paragraphs. Not a per-decision reversal; a project-identity reversal.
- **Commercial price-point selection** (within $5-15 envelope) / BP cadence / cosmetic DLC catalog — Easy-class. PM-decisional, does not reopen this ratification.

## Follow-ups

None new. Two existing carried items are reaffirmed (not added):

- 2026-04-25 Follow-up #5 (cultural-sensitivity at Phase-4 exit) — applies to cosmetic naming surface ("Premium" / "Founder's" / cosmetic-DLC naming review).
- Phase 7.2 Roadmap item #12 (monetization model lock) — already carried in Phase 7; this ratification advances it from "leaning DRG-style" to "model-shape locked, commercial specifics PM-deferred."
