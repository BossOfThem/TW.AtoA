---
**Status:** Draft
**Last reviewed:** 2026-05-05
---

# Phase 6 — Validation

*How we know the game is working before we commit to finishing it.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-5.md](phase-5.md). Next: [phase-7.md](phase-7.md).

---

**Amendment banner — 2026-04-26 real-cultures frame cascade (phase-6 consumer turn).** Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility **Hard**) — supersedes the 2026-04-21 3-tier Dust/Form/Apotheosis validation framing. This file retargets the validation rubric to the **4-tier ladder + Fusion endgame** (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero → Fusion → God) and the real-cultures content skeleton (3 civilizations, 3 launch commanders, 9 Gods via 9 locked Fusion recipes). Attack-type surfaces reference [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md) (Reversibility Medium).

---

## 6.1 Primary question for the MVP

Does the **commander + civilization + 4-tier-ladder + Fusion-to-Gods** combination produce moment-to-moment fun, AND does the **civilization-persistence feeling** (a Greek match that feels Greek from first wave to final fusion — same for Aztec, same for Norse) emerge by the end of T3 at the latest?

If yes, the vision is viable. If no, the vision is wrong and Phase 1 must be reopened.

Shipping the full locked content skeleton in MVP is deliberate under the 2026-04-25 ratification: the launch roster (3 civs × 6 T1-T3 + 5 units + 6 T4 + 3 Gods) is the lean-launch floor, so MVP validates the full arc rather than a truncated slice. Prior "tier-persistence emerging by end of Form" framing (2026-04-21) is **superseded** — under the 4-tier + Fusion frame, the validation bar is (a) civilization-persistence emerging by end of T3 and (b) the Fusion endgame producing at least one trailer-beat God moment per match.

## 6.2 Secondary questions (in order)

- Do new players understand commanders and civilizations within their first match?
- Do players re-pick the same commander on match 2 or try another? (Indicates whether commander identity is sticky or shallow.)
- Does the civilization-persistence callback feel earned by the end of T3?
- Is match length right, too long, or too short? (Target: 30-round cap fits the 5–25 min window from `concept/phase-1.md §1.2`.)
- Which civilization gets picked least, and is that a bug or a feature?
- Does solo TD hold attention without multiplayer? (Critical — solo must carry the game independently.)
- Do the **9 locked Fusion recipes feel learnable** without wiki-lookup, and does reaching a God feel earned rather than automatic?
- Does the **attack-type × armor-tag RPS matrix** land at gameplay speed — do players read "my Fire tower is strong into this Beast wave" without a tooltip?
- Is the **Tribute / Divinity split** legible — do players understand that Divinity is the mythic-endgame currency and not just "more Tribute"?

## 6.3 Playtesting approach

- **Internal playtesting** with the two-person dev team through MVP completion.
- **Cultural-sensitivity external review** (2026-04-25 Follow-up #5) — mandatory gate **before** any playtest exposes Aztec representation, Leonidas visual framing, or Ragnar TV-vs-history framing.
- **Closed alpha** with 5–10 external playtesters (TD/TW fans) after MVP — tests the full 3/3/3 roster + Fusion endgame in live play before any post-launch expansion.
- **Open alpha** after multiplayer is stable and the patch-1 commanders are live (see `concept/phase-5.md §5.2` item 9), to catch late-game balance, Fusion-recipe meta stabilization, and cold-start matchmaking issues.

## 6.4 Success metrics per build phase

Under the 2026-04-25 real-cultures ratification, MVP converges with the full launch roster — the prior "Post-five-lineages," "Post-eleven-ages," and "Post-hybrid-families" milestones are obsolete (MVP already has all 3 civs, all 4 tiers, and the Fusion endgame). Remaining milestones:

- **MVP:** 70%+ of playtesters say they would play a second match. 50%+ report the **civilization-persistence** feeling by end of T3. **30%+ reach at least one Fusion (God summon) per match** — lower threshold than civ-persistence because Fusion is the trailer beat, not the baseline. Median session length ≥ 15 minutes (inside the 5–25 min target). No civilization picked less than **25% of the time** across tracked runs (with only 3 civilizations, a civ at <25% pick rate is a real design failure — tighter than the prior <20% under 3 lineages because the pool is smaller). **Commander re-pick on match 2 ≥ 40%** (measures whether the §4.1 identity floor produces stickiness; inherited from [2026-04-20 commander identity floor](../decisions/2026-04-20-commander-identity-floor.md) — re-rebased 2026-04-26 to the 2026-04-25 ratification).
- **Post-divergence-forks (after `concept/phase-5.md §5.2` item 1):** both T2→T3 and T3→T4 forks get picked across ≥ 60% of tracked runs; the T3→T4 fork demonstrably affects which Fusion recipe(s) the player reaches.
- **Post-enemy-roster (after §5.2 item 2):** armor-tag RPS reads at gameplay speed — ≥ 70% of playtesters can name the counter-type for a given armor tag after 3 matches, without the tooltip.
- **Post-multiplayer:** Median ranked match finds opponent in <60 seconds during active hours. <5% disconnect rate.
- **Post-patch-1-commanders:** no civilization's patch-1 commander picked <35% of their civ's match share (prevents the launch commander soft-dominating its civ forever).
- **Alpha:** Average session length ≥ 30 minutes. Day-2 return rate ≥ 40%.

## 6.5 Skill-bar telemetry (NEW 2026-05-05)

*Decision entry: [`2026-05-05 R9 skill-bar thresholds`](../decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) (Accepted; Reversibility Medium). Resolves the [`phase-4.md §4.11.8`](phase-4.md#4118-skill-bar-thresholds-per-k) forward-anchor. Engine-side gathering is a Phase 5 task; this section binds the measurement protocol.*

The 3 skill-bar axes (matchup-correctness / placement-coverage / ability-uptime) per `phase-4.md §4.10.5` carry per-(k) expert + novice thresholds in `§4.11.8`. Each axis is computed from gameplay events as follows:

- **Matchup-correctness** — for every kill event, log `effective_multiplier = 1.25` if the firing tower's attack-type RPS-counters the runner's armor-tag, `0.75` if RPS-countered, `1.0` otherwise (per [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md)). The axis value is `(count of 1.25-events) / (total kill events)` over the match. Hardcore expert target: 90%.
- **Placement-coverage** — for every active tower-second, log `engaged = 1` if any runner is within tower range during that second, else `0`. The axis value is `Σ engaged / Σ tower-seconds` across the match — i.e., the realized ε in §4.11.4. Hardcore expert target: 80%.
- **Ability-uptime** — for the commander active ability (and any aux-slot timed effect), log `cast_count` against `(match_duration / cooldown)`. The axis value is `cast_count / max_cast_count`. Signature ability is **excluded** per §4.10.5 lock. Hardcore expert target: 80%.

Realized DPS multiplier per match = product of the three axis values (Hardcore expert ≈ 0.576) — used by the validation rubric to detect "winning despite skill-bar fail" outliers (memorization meta) and "losing despite skill-bar pass" outliers (numerics drift). Both signal the §4.7 Round-11 mandate is needed.

The same telemetry feeds the §6.4 success-metric "civilization-persistence by end of T3" check: per-civ matchup-correctness should rise across T1→T3 as the player learns the civ's RPS coverage.

## 6.6 Exit condition for Phase 6

A validation plan exists for every build phase. Success metrics are defined in advance, not defined after the data comes in. The team knows what would make them cancel the project. The **cultural-sensitivity pass** is scheduled as a hard gate between MVP content-lock and any external playtest.

→ **Hand off to [Phase 7](phase-7.md).**
