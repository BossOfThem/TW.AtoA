# Agent 8 — Player Complaint Atlas (Wave 1)

**Role:** Dedicated mining of PLAYER-VOICE complaint sources across the TW/TD genre and adjacent multiplayer-strategy titles. Creator-side complaints are Agent 9's scope and are not duplicated here.

**Date:** 2026-04-27
**Sources surveyed:** Steam negative-review aggregators (Legion TD 2, Bloons TD 6, Element TD 2, They Are Billions, Stormgate, Kingdom Rush 5), Steam Community discussion threads, Hive Workshop forums, Blizzard official forums (WC3 Reforged, SC2), ResetEra, EA forums (PvZ), pcgamer / gamerant / massivelyop post-mortems, Quarter-to-Three.

---

## Landscape paragraph (what players complain about most across the genre)

Across TW/TD-adjacent multiplayer-strategy games, the dominant player grievance is not a single mechanical flaw but a *trust* failure: games launch incomplete or pivot mid-life, balance becomes a meta treadmill that punishes the players who already invested, and monetization gradually annexes content that was previously free or progressionally earned. In multiplayer-skewed TDs (Legion TD 2, Direct Strike, Element TD 2 co-op) the loudest complaints cluster around matchmaking smurfing, toxic global chat, and content droughts. In single-player-skewed TDs (Bloons TD 6, Kingdom Rush, Plants vs. Zombies) the loudest complaints cluster around post-launch monetization creep, power-creep balance churn, and grind-fueled "F2P-mobile-feel" progression bolted onto premium games. In the heritage WC3/SC2 custom-map space, the dominant grievance is *abandonment*: copyright land-grabs (Reforged), platform rot, host-bot fragility, and the death of the lobby-browser model. RTS-genre onboarding ("dumps 40 mechanics on you, 15 hotkeys in the tutorial") is a near-universal secondary complaint and a primary churn vector for new players. Battle-pass FOMO-treadmills are widely loathed by casual cohorts even when defenders concede they are "skippable."

---

## Player-Complaint Taxonomy (frequency-rank ordered)

| Rank | Bucket | Frequency | Severity (player-voice intensity) | Genre prevalence |
|---|---|---|---|---|
| 1 | **Balance / power-creep / meta treadmill** | Very High | High | Universal — every TD, every patch cycle |
| 2 | **Monetization creep on previously-free content** | Very High | Very High (anger) | Especially Bloons TD 6, PvZ2, Stormgate, Underlords |
| 3 | **Matchmaking / smurfs / toxic lobbies** | High | Very High | Multiplayer TDs (Legion TD 2 acute), WC3/SC2 custom, RTS |
| 4 | **Endgame / content cliff / repetition** | High | Medium-High | Especially They Are Billions, Kingdom Rush 5, BTD6 freeplay |
| 5 | **Scope: launched feeling incomplete / half-baked modes** | High | High | Stormgate flagship, Reforged, MTM speculation |
| 6 | **Onboarding too steep / tutorial dumps everything** | High | Medium | RTS-wide, Element TD 2 ("too complex"), Legion TD 2 |
| 7 | **Customization deficit (no map editor, locked progression, shallow lobby settings)** | Medium-High | High in heritage cohort | WC3 Reforged copyright land-grab, Stormgate map editor delayed |
| 8 | **Bug rot / engine rot / abandoned support** | Medium-High | High | WC3 Reforged, SC2 arcade hacking, Underlords abandoned |
| 9 | **UX / UI / accessibility (colorblind, readability, audio mix)** | Medium | Medium | Stormgate combat audio, generic TD colorblind issues |
| 10 | **Battle-pass FOMO / treadmill obligation** | Medium-High | High in casual cohort | Genre-wide live-service; Underlords S2 acute |
| 11 | **Pricing vs. content delivered (premium + MTX double-dip)** | Medium | High | Stormgate $12.99 commander vs SC2 $6.25, BTD6 |
| 12 | **Other: retroactive account deletion, IP land-grab, save-system absence** | Low-Medium | Very High when triggered | Legion TD 2 180-day deletion, Reforged EULA, Stormgate no-save |

---

## Findings

```
FINDING-1-08-1:
  CLAIM: Legion TD 2's most-upvoted negative reviews cluster around three themes — pervasive global-chat racism/toxicity, smurf-driven matchmaking, and a steep paywall-adjacent learning curve — not gameplay quality itself.
  SOURCE: https://steamcommunity.com/app/469600/negativereviews/?p=1&browsefilter=toprated
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Game retains "Very Positive" overall (~86% positive of ~13.5k reviews); core gameplay is widely praised.
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: AtoA's PVP-Co-op promise inherits Legion TD 2's matchmaking-toxicity attack surface unless lobby/chat moderation is part of shippable scope.
```

```
FINDING-1-08-2:
  CLAIM: Bloons TD 6 players report deep anger at retroactive monetization — features previously unlocked via leveling were re-gated behind Monkey Money currency years after launch — with verbatim accusations that "Ninja Kiwi [is] slowly becoming EA."
  SOURCE: https://steamcommunity.com/app/960090/discussions/0/1742265315848334933/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Defenders note Monkey Money is farmable; game retains "Overwhelmingly Positive."
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Direct precedent for AtoA's optional-Battle-Pass promise — players will detect ANY post-launch shift of formerly-free systems behind currency and react with disproportionate fury.
```

```
FINDING-1-08-3:
  CLAIM: Stormgate launched into early access with an explicitly incomplete feature set — no 3v3 mode, no map editor, no manual save in campaign, sub-par AI — and Frost Giant later admitted "we released far too early."
  SOURCE: https://www.pcgamer.com/games/rts/starcraft-2-spiritual-successor-stormgate-launches-to-a-mixed-rating-on-steam-but-frost-giant-is-undaunted-mixed-reviews-are-to-be-expected-at-this-stage/
  STRENGTH: very high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none — developer self-confirmed.
  PROMISE-1 RELEVANCE (0-5): 5
  PROMISE-2 RELEVANCE (0-5): 5
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: Strongest cautionary precedent for AtoA Promise 1 (feature-/polish-/art-complete coverage of every mode-type at launch). The market punished the alternative.
```

```
FINDING-1-08-4:
  CLAIM: Stormgate's map editor — repeatedly cited as one of the heritage features that kept WC3/SC2 alive — was delayed past launch into "next year" promises, drawing direct comparisons to Reforged's custom-game neglect.
  SOURCE: https://massivelyop.com/2025/07/23/multiplayer-rts-stormgate-will-leave-early-access-without-achieving-1-0-or-finishing-core-game-modes/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 5
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: Direct evidence that customization tooling MUST be in launch scope to credibly claim Promise 2; deferred map editors poison community trust.
```

```
FINDING-1-08-5:
  CLAIM: Warcraft 3 Reforged's EULA change claimed Activision-Blizzard as sole IP owner of any custom maps created in Reforged, which players and creators identified as a core driver of the custom-game scene's collapse.
  SOURCE: https://massivelyop.com/2020/01/30/blizzard-limits-warcraft-iii-reforgeds-custom-game-scene-as-players-complain-over-missing-features/
  STRENGTH: very high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 5
  PROMISE-3 RELEVANCE (0-5): 0
  RELEVANCE NOTE: AtoA's Promise 2 (recreate SC1/WC3 custom-lobby recognizability) requires creator-IP-friendly terms; this is the negative space the genre has not filled.
```

```
FINDING-1-08-6:
  CLAIM: Element TD 2 co-op players hit a balance "cliff" at waves 63-65 where the Cheese-element boss heals/shields make progression near-impossible even with full T3/T4 fills, plus persistent desync bugs where one player hits 0 HP while teammate retains full HP.
  SOURCE: https://steamcommunity.com/app/1018830/discussions/0/6852856365575066352/
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Devs released hotfixes and have continued co-op content roadmap.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: Co-op-mode polish at the late-game cliff is a recurring failure mode AtoA's PVE-Campaign + PVP-Co-op promise must directly address.
```

```
FINDING-1-08-7:
  CLAIM: Legion TD 2 ranked complaints describe a "smurf-paired-with-noob vs. legend-tier premade" matchmaking pattern, with high-ranked players openly running 5+ smurf accounts to dodge MMR.
  SOURCE: https://steamcommunity.com/app/469600/discussions/0/3124928124063586373/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Devs have published rating-convergence accelerators (+40 / doubled change first 20 games).
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Ranked Progression promise is exposed; smurf-resistance must be designed in, not patched after.
```

```
FINDING-1-08-8:
  CLAIM: Tower-defense Steam reviews repeatedly cite "F2P-mobile-feel" grind — replaying earlier levels to farm currency to brute-force later levels — as the single most off-putting design pattern for premium-Steam audiences.
  SOURCE: https://steamcommunity.com/curator/44794427-Tower-Defense-games-rated/?snr=1_1050_curatorsreviewing_
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Mobile-port titles continue to sell despite this complaint.
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: AtoA's "Battle Pass + Ranked layered without compromising regular play" promise lives or dies on whether the regular-play loop never feels grind-gated.
```

```
FINDING-1-08-9:
  CLAIM: Bloons TD 6 community has explicitly acknowledged power-creep as a recurring quality-of-life problem; Ninja Kiwi published a public commitment to "more targeted nerfs and fewer buff changes" in response to player feedback.
  SOURCE: https://bloons.fandom.com/wiki/Bloons_TD_6/Balance_changes
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none — developer public statement.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: Power-creep is the long-tail cost of perpetual balance churn; AtoA with 9 Fusion Gods + 3 commanders has a wide combinatorial surface for this failure mode.
```

```
FINDING-1-08-10:
  CLAIM: They Are Billions players cite endgame tedium ("repeating the same patterns over and over after 50%"), absence of mid-mission save/restart, and pointless hero-mission detours as the dominant negative-review themes despite an 80%+ positive overall score.
  SOURCE: https://steamcommunity.com/app/644930/discussions/0/4772128648795382062/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: 83% recent / 80% all-time positive — complaints are minority but loud.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: PVE-Campaign promise must avoid the "compelling first half, treadmill second half" trap that dominates this bucket of negative reviews.
```

```
FINDING-1-08-11:
  CLAIM: Dota Underlords lost its core audience after Season 2 locked two additional starting hero choices behind a paid Battle Pass — a textbook "compromise regular play with the Battle Pass" failure mode — followed by Valve effectively abandoning the title.
  SOURCE: https://www.resetera.com/threads/so-whats-the-status-of-the-auto-chess-genre.633809/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Direct cautionary precedent for AtoA's Promise 3 — Battle Pass that "compromises regular play" is the documented genre-killer.
```

```
FINDING-1-08-12:
  CLAIM: Plants vs. Zombies 2 international-version progression is described by 95%+ of core-community survey respondents as "absurd" and "the worst, most grind-heavy, and most pay-to-win design" in the franchise — driven by a level/mastery system retrofit onto a previously-loved premium IP.
  SOURCE: https://forums.ea.com/discussions/plants-vs-zombies-2-en/dear-development-team-of-plants-vs-zombies-2-international-version--players/12234698
  STRENGTH: medium-high
  CONFIDENCE: medium (% claim is community-self-reported)
  COUNTER-EVIDENCE: PvZ2 remains commercially active.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 0
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Most-cited cautionary tale for "monetization grafted onto established premium gameplay loop" — Promise 3's optional-layer constraint is exactly the design discipline this case violates.
```

```
FINDING-1-08-13:
  CLAIM: Battle-pass FOMO complaints are dominated by *casual* players who feel obligation-pressure to log in, with the loudest grievance being shortened seasons (3 months → 8 weeks) coupled with growing reward tiers — i.e. the time-budget squeeze is the predatory vector, not the price.
  SOURCE: https://gamerant.com/live-service-battle-pass-seasons-fomo-wow-overwatch-2-diablo-4-bad/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Some studios (per metrocareservicesmn coverage) have begun lengthening seasons / removing time-gates in response.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 0
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: AtoA Promise 3 wording "without compromising regular play" should likely be operationalized as "no time-gated FOMO loop" specifically, since that is the casual-cohort grievance vector.
```

```
FINDING-1-08-14:
  CLAIM: RTS onboarding is widely perceived as broken — "modern games dump 40 mechanics on you, 15 hotkeys in the tutorial, new players close the game" — with the heritage-campaign-as-tutorial model identified as the missing element.
  SOURCE: https://criticalmovesforum.com/threads/are-rts-games-too-complex-for-new-players.37/
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: AoE4 / Stormgate campaigns attempt this; mixed reception.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 2
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: AtoA's PVE-Campaign mode is a natural onboarding vector — explicitly designing it as the tutorial-by-stealth answers a known genre wound.
```

```
FINDING-1-08-15:
  CLAIM: Stormgate's $12.99 co-op-commander pricing — vs. SC2's $6.25 equivalent — was singled out by community as "very expensive" and was specifically called out as souring day-one supporters when a Hero appeared in the cash shop on launch day.
  SOURCE: https://massivelyop.com/2024/08/02/not-so-massively-stormgate-was-not-ready-for-early-access/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Pricing optics matter — the *visible* cash-shop hero on launch day did more reputational damage than the underlying gameplay shortfalls; AtoA Battle Pass storefront is exposed to the same optics risk.
```

```
FINDING-1-08-16:
  CLAIM: SC2 Arcade's most-popular custom (Direct Strike) has been intermittently exploited — infected map versions used to crash clients and "wipe data" — illustrating engine-rot / abandoned-platform risk in custom-map heritage scenes.
  SOURCE: https://us.forums.blizzard.com/en/sc2/t/arcade-being-hacked-again-direct-strike-games/30068
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Specific incidents have been patched; map remains active.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 0
  RELEVANCE NOTE: Promise 2 (custom-lobby ecosystem) inherits a security-rot attack surface that the WC3/SC2 platforms never solved.
```

```
FINDING-1-08-17:
  CLAIM: Wintermaul's long-running Warcraft 3 community singled out "killstealing whining" and "the only way to lose is to lag out" as the dominant social-toxicity and engine-fragility complaints — i.e. the social-design and netcode of a TD shape player perception of fairness.
  SOURCE: https://www.hiveworkshop.com/threads/wintermaul-redux-1-08g.121401/
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Map remains beloved; complaint is targeted at variants not the core.
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 3
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: Multi-lane TD social design (kill attribution, shared income, lag-loss) is a complaint surface that AtoA's Tower / Line / PVP-Co-op modes will inherit.
```

```
FINDING-1-08-18:
  CLAIM: Kingdom Rush 5 (the most recent franchise entry) saw its DLC Steam rating "plummet," with player complaints centered on encounter-reskinning, reused open arenas, and a procedural-content engine that "started feeling incredibly similar after about three runs."
  SOURCE: https://www.pcgamesn.com/kingdom-rush-5-alliance/dlc-feedback-colossal-dwarfare
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Devs publicly called for feedback and committed to iteration.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: Procedural / repetition-driven content is the cheapest way to fake "endgame depth" and is the most-detected fake-out in negative reviews.
```

```
FINDING-1-08-19:
  CLAIM: Element TD 2 negative discussion threads include "this tower defense game is TOO COMPLEX" as a recurring onboarding complaint — i.e. even within the TD niche, depth-first design cliffs new players unless tutorial scaffolding matches the surface area.
  SOURCE: https://steamcommunity.com/app/1018830/discussions/0/2959418921943947218/
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Same depth is praised by veteran cohort.
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 2
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: With 9 Fusion Gods + 3 civs + 3 commanders, AtoA's surface area exceeds Element TD 2's — onboarding pacing must be a Phase 4 / Phase 5 explicit deliverable.
```

```
FINDING-1-08-20:
  CLAIM: Legion TD 2 specifically warns players via in-product disclosure that "your account can be deleted after 180 [days] of inactivity" with no compensation for prior purchases — flagged in negative reviews as a betrayal-of-trust grievance distinct from gameplay or balance.
  SOURCE: https://steamcommunity.com/app/469600/negativereviews/?p=1&browsefilter=toprated
  STRENGTH: medium
  CONFIDENCE: medium (citation per WebFetch summary; primary text not directly quoted)
  COUNTER-EVIDENCE: Devs may have revised this policy; not verified current.
  PROMISE-1 RELEVANCE (0-5): 0
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: Account-policy footguns can poison Promise 3's monetization legitimacy regardless of in-game design — under-discussed but high-impact.
```

```
FINDING-1-08-21:
  CLAIM: Bloons TD 6 community contains a discrete cohort that explicitly asks "can I disable updates?" because frequent patches "keep ruining the experience" for casual players who rejoin to find the meta has shifted under them.
  SOURCE: https://steamcommunity.com/app/960090/discussions/0/6406956248960279272/
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Active player cohort generally welcomes patches.
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 3
  RELEVANCE NOTE: Under-discussed: patch-velocity itself is a complaint vector — ranked seasons that re-shuffle balance can alienate the lapsed-returner audience that solo-first AtoA implicitly targets.
```

```
FINDING-1-08-22:
  CLAIM: Stormgate negative reviews flagged combat-audio mix problems ("combat audio has no weight," Simu Liu's hired-celebrity dialogue "inaudible") as a polish-tier complaint that disproportionately damaged launch reception relative to its dev-cost.
  SOURCE: https://www.pcgamer.com/games/rts/starcraft-2-spiritual-successor-stormgate-launches-to-a-mixed-rating-on-steam-but-frost-giant-is-undaunted-mixed-reviews-are-to-be-expected-at-this-stage/
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: none.
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 1
  RELEVANCE NOTE: Promise 1's "polish-complete" wording is load-bearing — audio mix is an under-budgeted polish dimension with outsized review-score impact.
```

```
FINDING-1-08-23:
  CLAIM: Across PvZ2, BTD6, and Underlords, the unifying player-anger pattern is not monetization-existence but monetization *introduced after* a free / earned baseline was established — players treat this as a breach of implicit contract more than as an economic transaction.
  SOURCE: https://www.isaelvega.com/blog-1/2019/2/13/plants-vs-zombies-monetization-in-video-games
  STRENGTH: high (synthesis across three titles)
  CONFIDENCE: high
  COUNTER-EVIDENCE: Some games (Path of Exile, Warframe) layer monetization gracefully onto established loops.
  PROMISE-1 RELEVANCE (0-5): 1
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Strongest cross-case finding — Promise 3's discipline must be "Battle Pass present from day 1, never grafted, never expanded into formerly-free space."
```

```
FINDING-1-08-24:
  CLAIM: A measurable subset of WC3 Reforged complaints centered on the 12-unit selection limit being preserved despite being a 2003-era constraint — a single legacy UX choice was a recurring negative-review touchstone independent of the larger Reforged failures.
  SOURCE: https://us.forums.blizzard.com/en/warcraft3/t/is-warcraft-reforged-worth-to-buy-for-the-custom-games/23378
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Some heritage players defend the 12-unit limit as identity-defining.
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 0
  RELEVANCE NOTE: Heritage-recognizability (Promise 2) does not require heritage *constraints* — players want the lobby/customization vibe, not the 2003 UX limits.
```

---

## Open questions for PM

1. **Exposure:** Of the twelve buckets above, which is AtoA's current design *most* exposed to? My read: Bucket 5 (Scope: launched-feeling-incomplete) given the ambitious 7-mode + 3-civ + 9-Fusion-God + 3-commander launch surface — but Bucket 3 (matchmaking/toxicity) is a near-tie because the PVP-Co-op promise inherits Legion-TD-2's known pathologies.

2. **Resolution:** Which bucket is AtoA's design *uniquely positioned to resolve*? My read: Bucket 7 (Customization deficit) — the explicit Promise 2 wording "customizability and recognizability of SC1/WC3 custom lobbies that no standalone TW has reproduced" is precisely the negative space the genre has left vacant since Reforged's IP land-grab. Is this also your read, or is the answer more about Bucket 1 (balance) via the Fusion-numerics paper-balance discipline already ratified in §4.8?

3. **Promise-3 operationalization:** Given the cross-case finding (FINDING-1-08-23) that monetization-anger is keyed to *change* rather than *existence*, should the Battle Pass be present and visible from EA day-1 (poison-pill commitment) rather than added at 1.0 or post-launch?

4. **Onboarding-as-campaign:** Does the PVE-Campaign mode get explicit framing as the onboarding-by-stealth answer to FINDING-1-08-14, or is it scoped as a pure content-mode and tutorial is a separate deliverable?

5. **Patch-velocity stance:** FINDING-1-08-21 surfaces a quiet but real complaint that frequent balance patches alienate lapsed-returner solo players. Is AtoA's solo-first principle compatible with a Ranked-Seasons cadence that necessarily churns the meta? Where is the seam?

6. **Smurf-resistance design budget:** Promise 3 (Ranked Progression) inherits Legion TD 2's documented matchmaking grievances. Is smurf-resistance / dual-account detection being scoped as engineering work in the Phase 5 plan, or is it being treated as a post-launch ops problem?

7. **The under-discussed risk:** FINDING-1-08-20 (account-deletion / inactivity policies) is rarely surfaced in design-doc discussions but reliably triggers Steam-review nukes when discovered. Should AtoA's Phase 4 exit gate include an explicit "no account-state footguns" review of monetization terms?

8. **Heritage-recognizability vs. heritage-constraints:** FINDING-1-08-24 suggests players want the lobby/custom-game *feel* but not the 2003 UX limits. How will Promise 2 distinguish "what to copy" from "what to modernize" — is there a written rubric, or is it case-by-case Phase 5 judgement?

---

*End of Agent 8 deliverable.*
