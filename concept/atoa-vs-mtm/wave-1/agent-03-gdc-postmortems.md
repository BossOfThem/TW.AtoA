# Agent-03 — GDC + Dev Postmortem Lens (Wave 1)

## Summary

Public dev-side postmortems and design retrospectives from the TW/TD/LW space converge on a small set of recurring lessons: (a) launch scope must match a tightly-defined core competency — Sanctum 2 explicitly cut RPG and ambitious mazing systems to focus on "FPS + TD"; (b) "single-player-tested" mechanics break in multiplayer in non-obvious ways (Sanctum 2's resource-share); (c) console ports without first-party promotional support are commonly a net negative in dev-time ROI (Sanctum 2: ~33% of dev-time on console for ~5% of revenue); (d) premium / buy-to-play with steady free content updates retains better than season-pass commitments locked in pre-launch; and (e) the **moddability + custom-lobby lineage from Warcraft 3** is what Legion TD 2's authors explicitly credit as the reason WC3 outlived League of Legends-style closed clients in their players' rotation. None of the developers consulted name a "killer feature" — they name **a focused core loop plus durable post-launch cadence + community tools** as what actually retains.

---

## Findings

```
FINDING-1-03-1:
  CLAIM: Sanctum 2 devs explicitly cut RPG mechanics and abandoned a complex mazing system after six months to keep launch scope to "FPS + Tower Defense" core competency.
  SOURCE: "Postmortem: Sanctum 2", Coffee Stain Studios (Johannes Aspeby), gamedeveloper.com
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 5
  PROMISE-2 RELEVANCE (0-5): 2
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: Direct dev evidence that mode-coverage breadth at launch must be paired with explicit cuts of adjacent systems, not stacked on top.
```

```
FINDING-1-03-2:
  CLAIM: Sanctum 2's pre-committed Season Pass became a monetization trap — the studio could not discount or restructure DLC after sales disappointed without breaking promises to early purchasers.
  SOURCE: "Postmortem: Sanctum 2", gamedeveloper.com
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 0
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Battle Pass / Ranked Progression layered on a base game must preserve flexibility — pre-committing a fixed schedule is a named-by-dev failure mode.
```

```
FINDING-1-03-3:
  CLAIM: Sanctum 2's resource-sharing mechanic worked in office playtests but failed online with strangers — players grabbed first instead of cooperating, forcing a post-launch redesign.
  SOURCE: "Postmortem: Sanctum 2", gamedeveloper.com
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 3
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: Co-op / shared-economy systems in PVP-Co-op and Custom modes need stranger-pool playtesting, not friend-group testing.
```

```
FINDING-1-03-4:
  CLAIM: Sanctum 2 sold 95% on PC vs 5% on console despite ~33% of dev-time on console ports — devs publicly stated they would not pursue day-one console parity again.
  SOURCE: "Postmortem: Sanctum 2", gamedeveloper.com
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 0
  RELEVANCE NOTE: Steam-shippable-first is dev-validated for this genre; console parity is a downstream-only concern.
```

```
FINDING-1-03-5:
  CLAIM: Legion TD 2's creators (Brent Batas, Julian Gari) explicitly credit the Warcraft 3 World Editor's accessibility — not its raw power — as what kept WC3 alive for 12+ years and what they are deliberately rebuilding inside Legion TD 2.
  SOURCE: "Legion TD 2's creators on the return of a classic Warcraft custom game", PC Gamer interview
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 5
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: Direct dev confirmation of Promise-2 thesis: SC1/WC3 custom-lobby recognizability is a moddability story, not just a UI story.
```

```
FINDING-1-03-6:
  CLAIM: AutoAttack Games chose to focus development priorities on bug-fixing, balance, new legions, and features rather than skin/cosmetic monetization decisions, framed as a deliberate values choice.
  SOURCE: AutoAttack Games dev statements (collected via legiontd2.com beta + Sketchfab community blog)
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Game does sell cosmetic/legion content; statement is values-framing not absolute purity.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 2
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: A successful WC3-lineage TW survivor explicitly de-prioritizes monetization-design churn — supports the "Battle Pass layered without compromising regular play" framing in Promise-3.
```

```
FINDING-1-03-7:
  CLAIM: Ninja Kiwi sustains Bloons TD 6 retention via weekly dev blogs answering ~10 fan questions plus regular content updates (new heroes, maps, modes), not via FOMO-event spikes.
  SOURCE: Ninja Kiwi support hub + ninjakiwi.com update video archive (2024-2025 update cadence)
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: BTD6 also runs in-game events and has $42M (~47% of 2023 revenue) from microtransactions — the public-facing cadence narrative coexists with strong IAP monetization.
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: Premium-priced TD with sustained free content cadence + IAP layer is a working post-launch model adjacent to ATOA's Promise-3.
```

```
FINDING-1-03-8:
  CLAIM: Kingdom Rush campaign retention relies on focused per-level concept introduction, deliberate breather levels, and reserving the most distinctive towers for late-game — not on raw content volume.
  SOURCE: "Kingdom Rush — the wonderful Campaign level design", gamedeveloper.com
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Article is third-party design analysis, not first-party Ironhide postmortem; no GDC talk located.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: PVE-Campaign mode-type at launch needs concept-pacing discipline; full-coverage breadth ≠ retention by itself.
```

```
FINDING-1-03-9:
  CLAIM: Sanctum 2 devs cite hiring external TCR/TRC compliance testers as the single highest-ROI QA decision — internal teams missed compliance failures the externals caught immediately.
  SOURCE: "Postmortem: Sanctum 2", gamedeveloper.com
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 0
  PROMISE-3 RELEVANCE (0-5): 0
  RELEVANCE NOTE: Steam-shippable launch quality bar is achievable for small teams via outsourced compliance — relevant to "polish-complete" promise.
```

```
FINDING-1-03-10:
  CLAIM: Sanctum 2 devs identify their own key failure as ignoring beta gameplay feedback while obsessing over bug-fixing — "we had our noses stuck up in our rear ends and didn't acknowledge the feedback."
  SOURCE: "Postmortem: Sanctum 2", gamedeveloper.com (Johannes Aspeby quote)
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 2
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: Direct dev confession: bug-triage cadence can mask gameplay rot; relevant to ATOA's Phase-5+ playtest posture.
```

---

## Open questions for the PM

1. ATOA promises seven mode-types polish-complete at launch. Sanctum 2's named lesson is to **cut adjacent systems, not stack them** — does ATOA have a written equivalent of "what we will not ship" to prevent the same trap, or is mode-coverage itself the cut already made?
2. Promise-3 names Battle Pass + Ranked Progression as launch features. Sanctum 2's Season Pass became a flexibility-killer — has the design considered explicitly **leaving the season-N+1 contents undefined** at launch so post-launch can absorb feedback without breaking promises?
3. Legion TD 2 devs treat "WC3-style modding inside our client" as the durable retention engine. Is Promise-2's "customizability and recognizability of SC1/WC3 custom lobbies" intended to extend to **player-authored content surface** (script-level modding), or is it a curated-tools model?
4. Kingdom Rush's design strength is per-level concept pacing, not breadth. With 3 civs × full ladder × 9 Fusion Gods × 3 commanders × 7 mode-types, where does the **per-mode concept-pacing budget** live in the spine docs — does each mode-type get its own intro-curve owner, or is that downstream of Phase 5?
5. BTD6 sustains a weekly community-answer cadence post-launch as a retention pillar. Has ATOA scoped a **post-launch communications cadence as a launch-day deliverable** the way Ninja Kiwi treats it, or is community ops assumed to be built ad-hoc post-ship?
