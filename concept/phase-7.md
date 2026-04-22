---
**Status:** Draft
**Last reviewed:** 2026-04-21
---

# Phase 7 — Iteration

*What stays open. What gets revisited. How the doc keeps living.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-6.md](phase-6.md). Next: — (end of cascade).

## 7.1 Open questions (resolution targets noted)

1. **Hybrid discovery mechanic** (accept/randomness/gating) — resolved by Phase 4 exit.
2. **Mobile unit control model** (waypoint+mode flags confirmed, specifics) — resolved by Phase 4 exit.
3. **Enemy direction** (leaning B-dominant hybrid) — resolved by Phase 4 exit.
4. **Monetization model specifics** (leaning DRG-style premium + free BP + cosmetic DLC) — resolved by Phase 4 exit.
5. **Engine choice** (leaning Godot 4) — resolved by Phase 4 exit.
6. **Commander launch roster size** — **CLOSED 2026-04-21 at 3** per [concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md). 3 is a lean-launch floor; expansion not cascade-blocked.
7. **Game title** — resolved by Phase 5. "Ash to Altar" is thematically load-bearing (arc, not string); title-lock remains deferred.
8. **Final Apotheosis (tier 3) forms per commander/lineage** — resolved during Apotheosis-tier design. (Supersedes prior "Ascendant age 11" framing — retired by 2026-04-21 concept tightening.)
9. **Lineage role differentiation under 3-lineage shape** — Prayer cannot drift into "less-good Nature"; Ash must feel essential without becoming mandatory. Supersedes prior "Veil-not-being-the-weird-one" and "Crown-not-being-boring" questions, both retired by 2026-04-21 concept tightening.
10. **Mobile platform plan** — deferred to post-launch.
11. **Ranked mode design** — deferred to post-launch.
12. **Modding support** — deferred, but flagged as highest-leverage long-term retention feature.
13. **Naming pass** (lineage placeholders Ash/Nature/Prayer + tier placeholders Dust/Form/Apotheosis vs. §5.4 [LOCKED] conventions) — deferred 2026-04-21. Future decision either reopens §5.4 or picks §5.4-compliant placeholders.

## 7.2 Decision log policy

Every major design decision recorded in `decisions/` with:
- Date
- Decision
- Alternatives considered
- Reason chosen
- Reversibility note (easy / medium / hard)

Decisions can be reversed, but only with a written reason in the same log.

## 7.3 Refinement priority queue

Order in which open items get addressed, assuming no new emergencies:

1. ~~Commander roster decision~~ — **CLOSED 2026-04-21 at 3** per concept tightening.
2. Per-lineage mechanical identity (one-page writeup each — 3 lineages: Ash / Nature / Prayer).
3. Per-commander mechanical spec (one-page writeup each — 3 launch commanders A / B / C).
4. Hybrid table (4–8 items under Ash-enabler model: Ash×Nature and Ash×Prayer families; supersedes prior 20–30-item target).
5. Tier Gate UX specification (Dust→Form, Form→Apotheosis — supersedes prior Age Gate framing).
6. Onboarding + tutorial design.
7. Scope reduction pass (what gets cut if timeline pressures rise).
8. Competitive differentiation statement (one paragraph: what makes this not just another TW game).
9. Engine choice lock.
10. Monetization model lock.

## 7.4 Notes to future self

- Resist designing content before mechanics are locked. Three lineages that feel mechanically distinct are worth more than fifty towers that feel mechanically same.
- The "almost infinite options" promise is carried by forks and hybrids, not tower count.
- **The Commander is the user.** Protect the "Commander = player identity" promise — do not let Commander become just a skin with a stat modifier. Commander should have voice, story, progression, and signature ability that make the player feel *seen*.
- The tier-persistence callback is the core delighter. Protect it.
- If a mechanic doesn't make the Dust tier (minute-1 choice) matter more, question whether it belongs.
- **Cascade discipline:** if you find yourself editing a Phase 2 constraint because a Phase 5 decision is inconvenient, stop. Reopen Phase 2 properly or change the Phase 5 decision.
- **Solo mode must be fully great on its own.** Multiplayer is additive, not required. Do not let multiplayer cold-start risk kill the launch.
- **Battle pass + cosmetic store works only with strict no-pay-to-win.** One misstep burns audience trust permanently. This is not a marketing concern. This is an identity constraint.
- **Live-service ops is a permanent state, not a project.** Scope content cadence realistically for a two-dev team. Seasonal content means *seasonal*, not *monthly*.
- The game title deserves the same discipline as every other naming convention. Don't ship with a placeholder.
