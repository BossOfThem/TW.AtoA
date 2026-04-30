# concept/atoa-vs-mtm/ — Product-shape swarm cascade

**Status:** Proposed (charter draft) — not yet launched
**Created:** 2026-04-28
**Reversibility:** Easy (entire folder is non-breaking; delete to revert)
**Affects:** Nothing in the spine until findings are separately ratified. This folder is a research container ("juice"), not part of the bootstrap chain.

---

## Purpose

A 4-round superaligned agent swarm exploring whether the current AtoA pivot proposal ([`decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md`](../../decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md), Status: Proposed) is the right product shape — or whether the swarm surfaces a better path. The pivot proposal is **untouched** by this cascade; the swarm produces refinement material that the PM may later use to ratify, modify, or replace the pivot.

Core PM question that triggered the swarm:
> *"How much progress do we lose if we move off HTML? What can we use this HTML and other files for without losing too much progress?"*

Supporting context (PM commitment, not a swarm conclusion): the math, tiers, units, commanders, and concept logic developed for Ash to Altar are believed to be 100% transferable across implementation paths and may be improvable when re-implemented. Agents may treat this as PM-stated context but are not required to accept it as load-bearing — challenging it with evidence is welcome.

## North-star statement (PM-signed, frozen at swarm launch)

Every agent in every round receives this verbatim. Every turn-in sheet ends with a self-rated alignment score per promise (1–5), with rationale. Three numbered promises become three explicit alignment-score axes — alignment-check agents measure mechanically, not interpretively.

> **A solo-first, Steam-shippable game that delivers three promises at launch: (1) feature-, polish-, and art-complete coverage of every TW-genre mode-type — Tower / Line / Hero / Horde / Custom / PVE-Campaign / PVP-Co-op — with the full Ash to Altar scope (3 civs, full ladder, 9 Fusion Gods, 3 commanders); (2) the customizability and recognizability of SC1 / WC3 custom lobbies that no standalone TW has reproduced; (3) optional Battle Pass and Ranked Progression for grind-oriented players, layered without compromising regular play.**

If a finding does not connect to at least one of these three promises, it does not belong in a turn-in sheet.

## Shared finding template

All R1 web/audit agents (and R2/R3 web-swarmers) report findings in this exact structure. Synthesizers and arguers may reference findings by **ID** without re-paraphrasing.

```
FINDING-<round>-<agent>-<n>:
  CLAIM: <one sentence>
  SOURCE: <URL / file-path / GDC talk title / etc.>
  STRENGTH: high / medium / low
  CONFIDENCE: high / medium / low
  COUNTER-EVIDENCE: <if any, else "none">
  PROMISE-1 RELEVANCE (0-5): <score>   # full-scope coverage
  PROMISE-2 RELEVANCE (0-5): <score>   # SC1/WC3 customizability + novelty
  PROMISE-3 RELEVANCE (0-5): <score>   # ranked/BP layered without compromising
  RELEVANCE NOTE: <one sentence on which promise(s) it advances and how>
```

A score of 0 means "not relevant to this promise" (legitimate — most findings advance one or two promises, not all three). A finding that scores 0 on all three promises does not belong in the turn-in sheet.

## Non-instructional rule (with enforcement)

Every turn-in sheet is **conceptual / refinement / educate / ask / repeat** — never instructional. No "do X, then Y." Each agent self-checks output before submission: imperative verbs are flagged and rewritten as questions or concepts. The inter-round alignment-check agent verifies compliance.

## Round structure

### Pre-flight
- PM signs the north-star above. Frozen for the entire swarm. Mid-swarm changes invalidate prior rounds.
- Charter (this file) is the only context-sharing artifact agents see beyond their own prompts and prior turn-in sheets.

### Round 1 — Foundational research (12 agents in 3 waves + alignment check)

R1 runs in three sequenced waves so the Devil's Advocate has findings to attack and the synthesizer has both findings + counter-arguments to reconcile.

**Wave 1 — Production (10 agents parallel):**

| # | Agent | Role | Tool |
|---|-------|------|------|
| 1 | HTML auditor | Full audit of `prototype/`. Produces "what's built / what's stub / what ports to engine / what's HTML-specific" matrix using shared template. | `Explore` |
| 2 | Web — Reddit + Steam (general) | General Reddit + Steam reviews across TW/LW/Hero/Horde games (broad lens; Agents 8 and 9 own complaint-specific mining) | `general-purpose` + WebSearch/WebFetch |
| 3 | Web — GDC + dev postmortems | Retention curves, what worked/failed from the dev side | `general-purpose` + WebSearch/WebFetch |
| 4 | Web — YouTube longform + creators | Novelty/customization gap critiques (general; Agent 9 owns creator-complaint-specific mining) | `general-purpose` + WebSearch/WebFetch |
| 5 | Web — Competitor design teardowns | WC3/SC1 customs, Bloons, KR, Legion TD, Element TD, Cursed Treasure | `general-purpose` + WebSearch/WebFetch |
| 6 | Web — Failed-TW tombstones (independent) | Dead/abandoned TWs, cause-of-death patterns | `general-purpose` + WebSearch/WebFetch |
| 7 | HTML bias-checker | Reviews Agent 1's matrix for blindspots, missed features, optimistic-vs-pessimistic skew (narrow scope: HTML matrix only) | `general-purpose` |
| 8 | **Player Complaint Atlas** | Player-side complaint-specific mining: Steam negative-review pulls on TWs with mixed/negative ratings, r/TowerDefense + r/WC3 + r/StarCraft complaint threads, "why I quit X" longform, abandoned-game forum post-mortems by players. Builds a player-complaint taxonomy (root-cause categorized: balance / monetization / endgame / customization-deficit / matchmaking / bug-rot / etc.). PM-flagged this vein as "gold." | `general-purpose` + WebSearch/WebFetch |
| 9 | **Creator Complaint Atlas** | Creator-side complaint-specific mining: Twitch VOD complaints mid-stream from TW/LW streamers, YouTube creator rants on TW genre stagnation, podcast hosts (Three Moves Ahead, etc.) airing genre grievances, dev-creator social-media beefs, "creators who quit covering this game" patterns. Separate output from Agent 8 — keep player vs creator complaint streams distinctly legible. | `general-purpose` + WebSearch/WebFetch |
| 10 | **R2-alternative scout** | Dedicated agent searching for alternative product-paths to the AtoA pivot \(single-product, web-only, mobile-first, F2P-with-cosmetics, premium-launch, episodic, etc.\). Surveys adjacent markets and recent indie launches for shapes the swarm hasn't yet considered. Output feeds R2 Arguer B with real ammunition. | `general-purpose` + WebSearch/WebFetch |

**Wave 2 — Cross-cutting Devil's Advocate (1 agent, sequential after Wave 1):**

| # | Agent | Role | Tool |
|---|-------|------|------|
| 11 | **Devil's Advocate** (cross-cutting) | Reads ALL Wave 1 outputs (findings from agents 1-10). Produces: (a) counter-arguments to each high-strength / high-confidence finding, (b) steel-mans of opposing positions, (c) "what if this entire finding is biased / unrepresentative / cherry-picked / sample-skewed" attacks, (d) cross-finding contradiction surfacing (where do agents disagree without realizing it?). Output is `da-pass.md` written into `concept/atoa-vs-mtm/`. Synthesizer is required to reckon with each DA challenge, not silently bury. | `general-purpose` |

**Wave 3 — Synthesis (1 agent, sequential after Wave 2):**

| # | Agent | Role | Tool |
|---|-------|------|------|
| 12 | Wide-scope synthesizer | Digests Wave 1 (agents 1-10 findings) + Wave 2 (DA challenges) into `round-1-turn-in.md`. **Required:** preserves Agent 8 (player) and Agent 9 (creator) complaint taxonomies as separate, legible sections — do not merge into general findings. **Required:** integrates Agent 10's alternative-path nominations as a "Strongest Alternative Paths" section so R2 Arguer B inherits real ammunition. **Required:** for each DA challenge, either accepts the challenge (downgrades the original finding) or rebuts with reasoning — never ignores. | `general-purpose` |

→ **Alignment-check 1** (lightweight agent) reads `round-1-turn-in.md` against the north-star, flags drift / contradictions / vocabulary collisions / missing counter-evidence. Writes `alignment-check-1.md`.
→ **PM gate.** PM reviews both files, redirects if needed, approves R2 launch.

### Round 2 — Path-to-product disagreement (4 agents parallel + alignment check)

| # | Agent | Role |
|---|-------|------|
| 1 | Arguer A | Defends AtoA-first-sequential pivot (current proposal). Cites R1 findings by ID. |
| 2 | Arguer B | Argues the strongest alternative path nominated by R1 synthesizer. Cites R1 findings by ID. |
| 3 | Web-swarmer A | Deepens Arguer A's case with fresh research. New findings in shared template. |
| 4 | Web-swarmer B | Deepens Arguer B's case with fresh research. New findings in shared template. |

Output: `round-2-turn-in.md` — non-duplicative, opens with each agent's "what from R1 am I treating as load-bearing, and do I challenge any of it" coherence-diff paragraph.

→ **Alignment-check 2** runs same protocol. → **PM gate.**

### Round 3 — PM-lens vs Player-lens with synthesis (5 agents — 2 + 2 + 1)

| # | Agent | Role |
|---|-------|------|
| 1 | PM-lens thinker | Scope / timeline / dependency-risk / ship-readiness lens |
| 2 | Player-lens thinker | Fun / recognizable / novel / customizable lens. "What no TW captures from SC1/WC3 customs." |
| 3 | Web-swarmer A | Deepens PM-lens findings |
| 4 | Web-swarmer B | Deepens Player-lens findings |
| 5 | Synthesis agent | Merges 1-4 + **only the prior turn-in sheets** (not raw agent outputs — context-window discipline) into `round-3-turn-in.md`. Includes pre-emptive evolution proposals (Maze TW, Spiral TW, custom-lobby capture). |

→ **Alignment-check 3** runs same protocol. → **PM gate.**

### Round 4 — Convergence-detected question cycles (2 background agents)

- Two agents retain full swarm context and collaborate to generate 20-question batches via `AskUserQuestion`.
- Each cycle: 20 questions → PM answers → answers fold into context → next 20 generated.
- **Convergence rule:** when ≥18 of 20 newly-generated questions are reformulations of prior questions (semantic similarity), agents declare convergence and propose stop. PM confirms or extends.
- Output: one `round-4-cycles/cycle-N.md` per cycle, plus final `SYNTHESIS.md`.

## File index (created during swarm)

```
concept/atoa-vs-mtm/
├── README.md                  (this file — charter, frozen at launch)
├── round-1-turn-in.md
├── da-pass.md                 (Wave 2 cross-cutting Devil's Advocate output, R1 only)
├── alignment-check-1.md
├── round-2-turn-in.md
├── alignment-check-2.md
├── round-3-turn-in.md
├── alignment-check-3.md
├── round-4-cycles/
│   ├── cycle-1.md
│   ├── cycle-2.md
│   └── ...
└── SYNTHESIS.md               (final artifact)
```

## What the swarm will NOT do

- No edits to AtoA pivot doc, CONCEPT.md, phase docs, or any decision log outside this folder.
- No ratification — output is conceptual material; PM ratifies separately.
- No code changes to `prototype/`.
- No git commits during the swarm. PM commits at end if/when satisfied.
- No deviation from the north-star without explicit PM mid-swarm reset.

## Cost transparency

- R1: 12 agents in 3 waves. Wave 1: 10 parallel (1 codebase audit + 5 broad web + 1 player-complaint atlas + 1 creator-complaint atlas + 1 HTML bias-check + 1 R2-alternative-scout). Wave 2: 1 sequential (Devil's Advocate). Wave 3: 1 sequential (Synthesizer).
- R2: 4 agents parallel.
- R3: 5 agents (4 parallel + 1 sequential synthesis).
- R4: 2 background agents in N convergence cycles.
- 3 lightweight alignment-check agents (one between each round).
- Total: ~20 agent-runs + N R4 cycles.
- Material context spend. Documented so it's not a surprise.

## Reversibility

Easy. Delete `concept/atoa-vs-mtm/` to revert; nothing in the spine references this folder. The AtoA pivot doc is untouched. The bootstrap chain is untouched.

## PM go-state

- [ ] PM has read this charter
- [ ] PM has signed off on the north-star statement (verbatim, frozen)
- [ ] PM has issued explicit "go" for R1 launch

When all three are checked, R1 launches.
