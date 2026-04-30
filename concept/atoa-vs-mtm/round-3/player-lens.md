# Round 3 — Player-Lens Analysis

**Agent:** R3 Player-Lens thinker | **Date:** 2026-04-28 | **Inputs:** R1 turn-in, DA pass, R2 Arguer A (defend pivot), R2 Arguer B (defend paid-EA), Swarmer-A and Swarmer-B evidence packages.

---

## 1. Player-lens framing

This lens privileges the felt experience of one human discovering, deciding-on, installing, opening, and continuing-to-play a game. It reads each path through the pupil of someone whose attention budget is six minutes on a Steam page and whose trust budget is one broken promise. It asks what the trailer says, what the storefront page promises, what the install delivers, what the first lobby feels like, what the third night returning feels like, what the player tells a friend at lunch the next day. It privileges signal over architecture: a player does not see the wishlist-conversion bet, the substrate-pivot-vs-identity-pivot taxonomy, or the two-product hand-off — they see *a thing they want to play*, or they don't.

What this lens cannot see: studio-economics runway, solo-dev career-capital depletion curves, engine-port labor pricing, Phase-5 timeline arithmetic, and the difference between substrate and identity pivots from inside the dev's chair. It cannot adjudicate whether the dev *can ship* either path — only whether each path, *if shipped*, lands as a thing a player wants to live with. PM-lens findings are needed alongside; the player lens is one column of the table, not the table.

A specific honesty: this lens distrusts the entire "free Steam SKU as audience funnel for paid sequel" frame because the player-experience inside that frame is "I downloaded this random TW game, played it, liked it, and now you're telling me the *real* one costs $30 and is a different download." That sentence is the experience the architecture produces, regardless of how the dev frames it internally. The lens has to surface this even when prior rounds have not foregrounded it.

---

## 2. Findings

### FINDING-3PL-1: The paid-EA Steam page tells a single coherent story; the two-product architecture tells two stories that contradict each other at the moment of contact

- **CLAIM:** A player on Steam reads the storefront as the contract. Paid-EA's page says "this is an unfinished game, here is what works today, here is the roadmap, you pay $15 to ride along." That sentence parses as one promise. The two-product pivot's storefront-pair says "AtoA is free and complete enough to play forever" *and* "MtM is the real version you should buy in 18 months" — and a player reading both pages cannot reconcile them without concluding either (a) AtoA is the lesser version and they should wait, depressing AtoA's player base before MtM ships, or (b) AtoA is enough and MtM is upsell, depressing MtM's conversion. The architecture forces the player to resolve a contradiction the dev has not resolved.
- **SOURCE:** Player-experience inference from R1 Player Complaint Atlas Bucket 5 (incompleteness vs broken-completeness-promise); R2 Arguer-B FINDING-2B-05 (reversal-of-promise as dominant anger pattern); R2 Arguer-A concession (a) (wishlist-conversion is the load-bearing assumption).
- **STRENGTH:** high
- **CONFIDENCE:** high
- **COUNTER-EVIDENCE:** Vampire Survivors maintained a free itch.io version *and* a paid Steam version (Swarmer-A FINDING-2WA-1) without the contradiction collapsing the franchise — the free was framed as a "demo" and the audience accepted the framing. The contradiction is real but not necessarily fatal if framing is disciplined.
- **PROMISE-1 RELEVANCE (0-5):** 4
- **PROMISE-2 RELEVANCE (0-5):** 3
- **PROMISE-3 RELEVANCE (0-5):** 4
- **RELEVANCE NOTE:** The first-contact promise is the foundation of all three north-star promises; an incoherent storefront pair undercuts every downstream commitment because the player never trusts the next claim after detecting the first inconsistency.

### FINDING-3PL-2: For TW-genre veterans, "free standalone TW on Steam" pattern-matches to the Tower-Wars-2012 / Defenders-of-Ardania / dead-mod-port reference class, not the WC3-customs reference class

- **CLAIM:** The player who clicks AtoA-free is a TW-veteran whose pattern library includes Wintermaul, SC2 Squadron TD, Element TD 2, Bloons, Cursed Treasure, Tower Wars (Steam 2012 — 71% positive, dead matchmaking pool per Finding 1-06-4), and Defenders of Ardania (cautionary tombstone per 1-05-08). The reference class for "free standalone TW on Steam, polish-ambitious, solo-dev" in their head is *empty of survivors*. A player encountering AtoA-free reads it through that priors set and concludes "another one of these" before they install. Paid-EA at $15-20 by contrast pattern-matches to Legion TD 2 ($20 paid-EA, 87% positive, 6+ years of monthly updates per FINDING-2WB-2) and to the Hades / Manor Lords / They Are Billions reference class — the genre's living shipped survivors. The same player applies the *correct* prior to a paid-EA listing and gives it a real chance.
- **SOURCE:** R1 Findings 1-06-4 (Tower Wars 2012), 1-05-08 (DoA), 1-02-3 (Legion TD 2 floor); R2WB FINDING-2WB-2 (LTD2 direct comp); player priors inference.
- **STRENGTH:** high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** TW-veterans are not the only audience; a player new to the genre has no priors and treats the storefront naively. But TW-veterans are *exactly* the audience Promise 2 (SC1/WC3 recognizability) is built for — the cohort whose priors the pivot is most exposed to is the cohort the design is most courting.
- **PROMISE-1 RELEVANCE (0-5):** 4
- **PROMISE-2 RELEVANCE (0-5):** 5
- **PROMISE-3 RELEVANCE (0-5):** 2
- **RELEVANCE NOTE:** Promise 2's audience (TW-genre veterans, WC3-customs nostalgic cohort) carries priors that punish free-standalone-TW posture and reward paid-EA posture — the lens favors the path the target audience's priors favor.

### FINDING-3PL-3: The price tag is the trust signal — $0 reads as "low confidence in own product" to the very players Promise 2 targets

- **CLAIM:** A player who has paid $20 for Legion TD 2, $15 for Vampire Survivors, $30 for Dwarf Fortress (Swarmer-B FINDING-2WB-3), and $40 for Manor Lords has internalized that price-as-confidence-signal: the dev who charges $0 for a feature-complete-claimed product is either (a) building toward a different revenue event the player is being recruited into without consent, or (b) does not believe the product clears the price bar. Both readings are corrosive. A player paying $15 for paid-EA AtoA is not asked to wonder where the trick is — the trick is the price, and it is fair, and the contract is closed. The free product carries an ambient *what's the catch* that the paid product does not.
- **SOURCE:** Steam pricing-priors inference; R1 Finding 1-08-15 (Stormgate $12.99 cash-shop hero on launch day did more reputational damage than gameplay shortfalls — pricing-optics-as-trust-signal); Player Complaint Atlas Rank 11.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** F2P games successfully converted millions of players who do not read free-as-low-confidence (Fortnite, Apex, Marvel Rivals). The free-as-low-confidence prior is most operative for the boomer-Steam-strategy-game cohort (32-42 with 90 minutes a week per DA A-6) — which, again, is the Promise-2 target audience.
- **PROMISE-1 RELEVANCE (0-5):** 3
- **PROMISE-2 RELEVANCE (0-5):** 4
- **PROMISE-3 RELEVANCE (0-5):** 4
- **RELEVANCE NOTE:** Promise 3's day-1-visible Battle Pass is double-corrosive on a free-base product (the player asks "wait, the game is free *and* there's a BP?") but harmonious on a paid-base product ("I paid $15, the BP is optional cosmetic flavor on top"). Pricing posture and BP posture have to be consistent for trust.

### FINDING-3PL-4: Friction-to-fun is structurally lower in paid-EA than in the two-product pivot from a player's wall-clock perspective

- **CLAIM:** Counterintuitive but specific: a player who pays $15 for paid-EA is *playing the actual product* in minute 6 (download → install → tutorial → first match). A player who downloads free AtoA is playing AtoA in minute 6, but is implicitly told that the "real" product is 18 months away — so the wall-clock to *the thing they're being recruited into* is 18 months + 6 minutes, not 6 minutes. The pivot's free product front-loads zero-friction install but back-loads the actual customer journey by a year-plus. From the player's lived time-budget, the free path is *slower* to the destination than the paid path. The Friction-to-fun metric, properly accounting for what the "fun" is supposed to be, favors paid-EA decisively.
- **SOURCE:** Player wall-clock inference; R2 Arguer-A FINDING-2A-12 ("Go big at AtoA's launch, not MtM's") arguably acknowledges this by trying to make AtoA *be* the destination — but R2 Arguer-A concession (a) (wishlist conversion to MtM is load-bearing) reveals MtM is in fact the destination.
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** If AtoA-free is genuinely a complete game in its own right and the player never feels any pressure to convert to MtM, this finding collapses — the player is playing the destination from minute 6. Whether AtoA-free is genuinely the destination or covertly the funnel is the unresolved tension Arguer A's concession (a) names.
- **PROMISE-1 RELEVANCE (0-5):** 5
- **PROMISE-2 RELEVANCE (0-5):** 3
- **PROMISE-3 RELEVANCE (0-5):** 2
- **RELEVANCE NOTE:** Promise 1's "complete at launch" lands in the player's wall-clock perception only if the launch product is *the* product, not the funnel for a future product. Paid-EA naturally satisfies this; the pivot only satisfies it if AtoA's completeness is genuine and not framed as preparatory.

### FINDING-3PL-5: Word-of-mouth ignites on paid-EA's "I bought into something interesting" frame; free products fail to generate the recommendation moment

- **CLAIM:** The recommendation a player gives a friend has a recognizable shape: "dude I bought this thing, it's $15, you have to try it, it's like Legion TD 2 but with [X]." The price tag is not a deterrent in the recommendation — it is *part of the recommendation*, because it certifies the recommender's commitment and signals the friend that this is a real product worth trying. Free recommendations carry the opposite charge: "it's free, try it I guess" lands as low-confidence-from-the-recommender. The Hades / Vampire Survivors / Manor Lords / Dwarf Fortress word-of-mouth pattern is a paid-product pattern — Swarmer-A FINDING-2WA-1 even concedes Vampire Survivors' Steam release is the *paid* successor, and the word-of-mouth spike was on the paid version. Free products in this reference class do not generate the recommendation moment that compounds discoverability.
- **SOURCE:** Word-of-mouth pattern inference; R2WA FINDING-2WA-1 (VS itch.io free → Steam paid, paid version is the cultural moment); R1 Finding 1-09-6 (creator audience-economics debuff on free TW); R1 Finding 1-04-4 (BTD6's content-surface story is told about a paid product in the IP).
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** F2P/free games do generate word-of-mouth in the live-service / battle-royale reference class (Fortnite, Marvel Rivals, Apex). The recommendation pattern there is "log on with me tonight" rather than "buy this" — which is a different kind of recommendation requiring a specific game-shape (low-friction, social-graph-bound) AtoA-free does not have. AtoA-free occupies the recommendation gap between premium-buy and live-service-join, which is the dead zone for word-of-mouth.
- **PROMISE-1 RELEVANCE (0-5):** 3
- **PROMISE-2 RELEVANCE (0-5):** 4
- **PROMISE-3 RELEVANCE (0-5):** 3
- **RELEVANCE NOTE:** Promise 2's lobby-recognizability requires a steady inflow of new players for the lobby population to feel populated. Word-of-mouth is the discovery mechanism for that genre. The path that generates better word-of-mouth wins Promise 2 even if its raw install count is lower.

### FINDING-3PL-6: Post-launch loyalty depends on the ranked / progression / cosmetic loop the player can *invest* in; paid-EA carries that loop natively, the pivot defers it

- **CLAIM:** A player at month-3 returning to a TW-genre game returns because their progression is there — their ranked rating, their commander unlocks, their cosmetic shelf, their replay collection, their friends list of regular opponents. This is the core mechanism by which Legion TD 2 holds 800 DAU for six years (R1 FINDING-1-02-3) and BTD6 holds 97% sentiment over 13 years (R1 FINDING-1-02-1). Paid-EA at $15-20 ships this loop on day one — the player who buys in invests in a progression substrate that is durable, paid-for, and version-stable. The pivot's free-AtoA defers Promise 3's BP/Ranked architecture to MtM by construction (Arguer-A FINDING-2A-4 explicitly names this routing), meaning the AtoA-free player builds progression in a substrate the dev has already telegraphed will be replaced. The month-3 return is structurally weakened — the player knows their AtoA-free progression is vestigial.
- **SOURCE:** R1 FINDING-1-02-3 (Legion TD 2 ranked-progression niche); R1 FINDING-1-05-09 (BTD6 meta-progression on frozen rule-set); R2A FINDING-2A-4 (Promise 3 routes to MtM); player retention pattern inference.
- **STRENGTH:** high
- **CONFIDENCE:** medium-high
- **COUNTER-EVIDENCE:** Arguer-A could counter that AtoA-free's lack of progression is a deliberate Promise-3-anti-pattern-avoidance (no BP, no monetization, no progression-anger) — and a player returning to AtoA-free is returning for the gameplay itself, not for sunk progression cost. This is coherent but it abandons the month-3 retention mechanism that genre comps actually use.
- **PROMISE-1 RELEVANCE (0-5):** 3
- **PROMISE-2 RELEVANCE (0-5):** 4
- **PROMISE-3 RELEVANCE (0-5):** 5
- **RELEVANCE NOTE:** Promise 3's "without compromising regular play" requires the BP/Ranked layer to *exist on the product the player plays* — routing it to a separate future product means the player's regular play has no Promise-3 layer for the pivot's first 18+ months.

### FINDING-3PL-7: The "I am a beta-tester for the real game" perception is the single most toxic player-lens reading of the two-product pivot, and the architecture invites it

- **CLAIM:** The moment a player realizes AtoA-free is the *prototype-substrate* and MtM is the *paid-substrate*, they read AtoA-free as a beta program they were enrolled in without consent. This is the worst possible player-lens reading because it casts every flaw, every spec gap (R1 reconciled HTML — fusion-execution stub, ability-targeting unspecified, cosmetic-unlocks-dead-end), every iteration as evidence the player is unpaid QA. The pivot's structural honesty — "we are testing the design here before building the real version" — is the *exact* sentence that triggers Bucket-5 Player Complaint Atlas anger ("launched feeling incomplete / half-baked"). Paid-EA inverts this: the player paid to be in the iteration room, the iteration is the product, and every flaw is "the EA we signed up for." Same flaws, opposite valence, depending on whether money changed hands at the door.
- **SOURCE:** R1 Player Complaint Atlas Bucket 5; R1 reconciled HTML deliverable-logic figure (50-55%, with named stubs); R2A FINDING-2A-2 (frames the 50-55% as enough for free-product-proof — but a player does not read "concept-validation surface" as a feature, they read it as a not-yet-real product); R2B FINDING-2B-05 (reversal-of-promise as dominant anger).
- **STRENGTH:** high
- **CONFIDENCE:** high
- **COUNTER-EVIDENCE:** If AtoA-free is framed disciplinedly as a *complete game in its own right* with no roadmap to MtM visible at launch, the beta-tester perception does not arise — the player plays AtoA-free as if it is the only product. But this framing requires the dev to *not* market MtM during AtoA's lifecycle, which contradicts the wishlist-conversion mechanism (Arguer-A concession a) the pivot depends on commercially.
- **PROMISE-1 RELEVANCE (0-5):** 5
- **PROMISE-2 RELEVANCE (0-5):** 4
- **PROMISE-3 RELEVANCE (0-5):** 4
- **RELEVANCE NOTE:** Every promise lands worse if the player believes they are unpaid QA for a future version. This is the player-lens equivalent of the Reforged EULA betrayal (R1 FINDING-1-09-2) — same architecture-of-broken-trust, different vector.

### FINDING-3PL-8: SC1/WC3-customs muscle memory is a *hosting* memory — the player who returns expects to host a custom lobby on day one of contact, and paid-EA's funded substrate ships that capability sooner

- **CLAIM:** The Promise-2-target-audience does not just remember WC3 customs as gameplay; they remember the *lobby browser, the host button, the chat that filled with "/r open" requests, the friend who hosted Wintermaul Wars every Thursday*. The customizability promise lands at the moment a player can *host their own lobby with their own ruleset and have someone join*. The pivot defers this hosting capability to MtM — Arguer-A FINDING-2A-5 explicitly names that AtoA-free runs the substrate at "low-cost (Steam Lobby APIs, P2P-host-driven, no central server) at a scale that proves demand," and MtM funds the engineered version. This means the recognizability moment Promise 2 promises does not *arrive* in AtoA-free at the polish level the player remembers — they get a sketch of the lobby substrate, not the lobby substrate. Paid-EA's revenue from day one funds the substrate engineering directly (Arguer-B FINDING-2B-11), shipping the recognizability moment within the EA window rather than across a product boundary.
- **SOURCE:** R1 Promise-2 convergence findings (1-02-2, 1-04-2, 1-05-01, 1-09-1); R1 FINDING-1-06-8 (Blizzard-subsidized substrate); R2A FINDING-2A-5 (two-shot substrate operationalization); R2B FINDING-2B-11 (paid-EA funds substrate from day one).
- **STRENGTH:** medium-high
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** A "sketch" lobby substrate that just works (Steam Lobby + P2P, browse, host, join, friend invite) might be fully sufficient for the recognizability moment — the player does not actually need the engineered version, they need the *experience* of hosting, which is software-cheap if scoped right. If true, AtoA-free can deliver Promise 2 at HTML-deliverable quality and the engineered MtM substrate is incremental polish, not load-bearing recognizability.
- **PROMISE-1 RELEVANCE (0-5):** 2
- **PROMISE-2 RELEVANCE (0-5):** 5
- **PROMISE-3 RELEVANCE (0-5):** 1
- **RELEVANCE NOTE:** Promise 2's player-felt moment is "I hosted a custom lobby and someone joined." Both paths can deliver this; the pivot delivers it twice (sketch then engineered) at the cost of the player perceiving the first one as the prototype. Paid-EA delivers it once, framed as the real thing.

### FINDING-3PL-9: The price-anchor reset asymmetry — once a player plays AtoA-free, MtM at $30 reads as "I'm being charged for what I already had"

- **CLAIM:** Price perception is set by the first product in the franchise the player encounters. A player whose first AtoA-experience is a free Steam SKU has anchored AtoA-as-IP at $0. When MtM ships at $20-30 18 months later, the player reads it not as "fairly priced premium TW" but as "the same game I already played, with better graphics, for $30." This is the exact PvZ2 anger pattern (R1 FINDING-1-08-12: 95%+ negative-sentiment progression retrofit) and the Underlords S2 paywall pattern (R1 FINDING-1-08-11). Paid-EA at $15-20 day-one anchors AtoA-as-IP at $15-20, and the 1.0 release at $20-25 reads as "fair price for the finished version" — same dollars, totally different felt deal. The pivot inadvertently engineers the worst possible price-anchor for MtM.
- **SOURCE:** R1 Findings 1-08-11 (Underlords paywall), 1-08-12 (PvZ2 retrofit), 1-08-23 (anger keyed to change from free baseline); price-anchoring behavioral inference.
- **STRENGTH:** high
- **CONFIDENCE:** high
- **COUNTER-EVIDENCE:** If AtoA-free is framed as *demonstrably distinct* from MtM (different art, different scope, different name even — "Ash to Altar" vs "Made to Mythologize"), the anchor transfer might not happen. But the pivot doc explicitly names MtM as inheriting AtoA verbatim and only Phase 5 being fresh — the products are designed to be the same game, which is exactly the condition under which the anchor transfers most violently.
- **PROMISE-1 RELEVANCE (0-5):** 3
- **PROMISE-2 RELEVANCE (0-5):** 2
- **PROMISE-3 RELEVANCE (0-5):** 5
- **RELEVANCE NOTE:** Promise 3's BP-without-trust-breach lands on a foundation of fair-price perception for the base product. If MtM's base price already reads as unfair due to anchor reset, the BP-on-top reads as compounding offense — and Promise 3 collapses regardless of how the BP itself is designed.

### FINDING-3PL-10: The "creator IP stewardship + custom-game EULA" moment is a single-event high-leverage trust signal that paid-EA can deliver once, the pivot has to deliver twice

- **CLAIM:** R1 Creator Complaint Atlas Bucket 1 (Reforged EULA betrayal) and Bucket 8 (publisher betraying creator/player covenant) name the IP-stewardship public commitment as a near-zero-engineering, high-creator-trust differentiator. Paid-EA ships one EULA at one moment and the trust signal is delivered once, durably. The pivot's two-product architecture means either the trust signal is delivered at AtoA-free's launch (and MtM has to re-deliver it under fresh scrutiny, with any deviation read as betrayal — the Underlords/DD2 broken-promise pattern, R1 FINDING-1-06-7) or it is delivered at MtM's launch (and AtoA-free's interim creator scene is uncovenanted and at risk). The pivot doubles the EULA / IP-stewardship surface; paid-EA contains it.
- **SOURCE:** R1 Findings 1-09-1 (custom-lobby grief), 1-09-2 (Reforged EULA), 1-06-7 (DD2 reversed no-MTX promise), Creator Complaint Atlas Buckets 1 and 8.
- **STRENGTH:** medium
- **CONFIDENCE:** medium
- **COUNTER-EVIDENCE:** A single dated `decisions/` entry committing to creator-IP stewardship across both products simultaneously could resolve this — the pivot is not structurally exposed if the commitment is structured to be product-agnostic. But the pivot doc has not yet made this commitment and the player does not read decision-folder commits.
- **PROMISE-1 RELEVANCE (0-5):** 1
- **PROMISE-2 RELEVANCE (0-5):** 5
- **PROMISE-3 RELEVANCE (0-5):** 3
- **RELEVANCE NOTE:** Promise 2's creator-trust foundation is a public-commitment artifact. The path with fewer moments-of-recommitment carries less Promise-2 risk.

---

## 3. First-contact walkthrough

### Path A — Player discovers AtoA-free (the pivot)

Minute 0 — Player sees a TW recommendation on Reddit / from a creator / on Steam. Clicks the AtoA Steam page.

Minute 1 — Storefront page loads. Genre: Tower Defense / Strategy / Multiplayer. Price: Free. Trailer plays — three civs, fusion gods, custom lobby, ranked. Looks ambitious. Player's first internal question: *"Why is this free?"* Scans the page for the catch. Sees no IAP, no ads. Reads the description: "Solo-developed, complete TW experience." A small voice asks: *who funded this and why*. The player has been trained by Stormgate, Reforged, and twenty failed F2P TWs to ask this question.

Minute 2 — Player clicks recent reviews. Mixed bag — some "great free game!" (5 hours played), some "feels unfinished" (12 hours), some "if it's free, why is it broken?" (2 hours). Player's framework now: *this is either a hidden gem or a half-built thing*. Hits Install because the friction is zero.

Minute 4 — Game opens. Title screen. Mode select. Player sees seven mode-types listed. Clicks Tower mode first because it's familiar. Tutorial dumps. First match.

Minute 12 — Match feels good. Math is tight. Three civs distinct. The player notes the HTML-feel — works fine, doesn't sing. Tries to host a custom lobby. Lobby browser is functional but sparse — 11 lobbies up, 4 of them empty. Joins one. Match starts after 90 seconds.

Minute 30 — Player has played one Tower match, one custom lobby, opened the cosmetic shelf, found it stub-clickable (R1 reconciled HTML stub catalogue). Player opens the Steam store page in alt-tab. Sees a small banner: *"Check out our upcoming premium engine release: Made to Mythologize — wishlist now!"* Player feels the floor shift. *Oh. So this is the demo.* The free-Steam thing is the prototype. The real game is 18 months away. Player closes the alt-tab. Plays one more match. Doesn't return for two months.

Day 60 — Player tries to remember why they uninstalled. Vaguely recalls "felt like a beta for something." Doesn't wishlist MtM. Doesn't think about it again.

### Path B — Player discovers AtoA paid-EA at $15

Minute 0 — Same Reddit recommendation. Clicks Steam page.

Minute 1 — Storefront page. Genre: Tower Defense / Strategy / Multiplayer. Price: $14.99. Early Access. Trailer plays — three civs, fusion gods, custom lobby, ranked. Looks ambitious. EA badge near the price says *"Currently in Early Access — see roadmap below."* Player scrolls. Roadmap is explicit: *Tower, PvP-Co-op shipping at EA launch. Hero, Horde, Custom, PVE-Campaign rolling in over the next 12 months. 1.0 target: Q2 2027.*

Minute 2 — Player thinks: *"$15. Solo dev. Direct comp to Legion TD 2. EA with public roadmap. Reasonable bet."* Reads recent reviews. 86% positive — Hades-shaped EA review profile (R2WA FINDING-2WA-1 reference class). Most reviews say variations of "what's there is good, looking forward to the rest." Player buys.

Minute 6 — Game opens. Same title screen, same mode select, same first match. Same mechanics quality. Match feels good. Player notes it's clearly a real product. Looks up at the cosmetic shelf — sees 12 cosmetics, 4 unlockable through play, 8 in a paid Battle Pass on the side ($5, 12-week, all earned through play, no FOMO). Player reads the BP description: "Optional. Layered without compromising regular play. Cosmetic-only." Believes the framing because the base price already paid for the actual game.

Minute 30 — Player has played two Tower matches and one PvP-Co-op match, hosted a custom lobby that filled (lobby pool feels healthier because everyone in it paid to be there, filtering for high-intent players per R1 FINDING-1-10-1's selection-confounding-as-feature-not-bug reading). Joins the Discord posted on the storefront. Subscribes to dev devlog.

Day 60 — Player has played 18 hours. Has a ranked rating. Has an opinion about civ balance. Is back on the Steam page reviewing patch notes. Tells a friend at lunch: *"$15, you should try this, it's like Legion TD 2 but with custom-mode breadth."* Friend buys.

### Side-by-side contrast

The same player, same gameplay, same mechanics, two paths. Path A: 30 minutes of play, 0 emotional commitment, 0 word-of-mouth, churn at day 1, vague unease about the architecture. Path B: 30 minutes of play, $15 emotional commitment (the magnitude that produces real engagement, per R1 FINDING-1-10-1), word-of-mouth at day 60, friend-acquisition compounding. The mechanics are identical; the framing changes everything about what the player feels.

The pivot's defenders will argue Path A is misframed — that with disciplined marketing AtoA-free is read as "the real game" and not as "the prototype-for-MtM." This is true in principle and unlikely in practice: the wishlist-conversion mechanism the pivot's commercial logic depends on requires *some* visibility of MtM to AtoA-free players. The moment that visibility exists, Path A's minute-30 reframing happens.

---

## 4. Player-lens verdict

**The player lens favors paid-EA at $15-20 single-product, decisively.**

The verdict rests on six convergent player-felt asymmetries: (1) coherent storefront narrative vs incoherent two-product story, (2) reference-class pattern-match to Legion TD 2 / Hades vs to Tower-Wars-2012 / DoA, (3) price-as-trust-signal aligned with confidence vs free-as-low-confidence with target audience, (4) shorter wall-clock to the destination product, (5) better word-of-mouth recommendation shape, (6) durable progression substrate from day one rather than after a product transition. The Promise-2 substrate question (does paid-EA fund the lobby engineering?) and the Promise-3 BP-without-anger question both resolve more cleanly under paid-EA than under the pivot at the moment of player contact.

**Blind spots this lens cannot adjudicate:**

- *Solo-dev resource feasibility.* The lens cannot tell whether the dev can ship paid-EA to a quality bar that survives the review-velocity guillotine (R2 Arguer-A FINDING-2A-6, Arguer-B concession 1). This is the dominant PM-lens question; if the answer is "the dev cannot clear the paid-EA quality bar at first contact," the player-lens preference is moot. The lens flags that the *upper bound* of paid-EA's player-felt experience is dramatically higher than the pivot's, but the floor — a paid-EA product that ships at 60% Steam review score — is dramatically lower. The pivot's free-shell is a softer landing pad on the bottom.
- *Marketing-burden week-one floor.* Paid-EA with no audience and no marketing budget sells ~50 copies week 1 (Arguer-B concession 3). The lens cannot price the multi-month devlog runway needed to clear that floor before launch.
- *HTML sunk-cost.* The lens does not weigh the rendering/transport/UI work in `prototype/` that paid-EA strands. R2WA FINDING-2WA-7 in Swarmer-A's package notes the math/balance work survives any substrate decision; only the rendering layer is lost. The lens treats this as PM-lens domain.
- *The "AtoA-free as a complete game in its own right" framing.* If the pivot's discipline holds and AtoA-free is genuinely the destination (not the funnel), much of this lens's objection collapses. The lens is forced to treat the pivot as it is *commercially* structured (free-funnel-to-paid-MtM, per Arguer-A concession a), not as the most charitable framing of it.

**Recommended elevation for R3 synthesis:** the player-lens conclusion is that the strongest version of the pivot — discipline-perfect, AtoA-as-destination, no MtM marketing during AtoA's lifecycle, two genuinely independent products — produces roughly equal player experience to paid-EA at a much higher dev-discipline cost. The probable version of the pivot — wishlist-funnel architecture with MtM visibility — produces materially worse player experience than paid-EA on every axis the lens reads. The synthesis question is whether the dev can hold the discipline for 18+ months under solo-dev career-capital pressure, or whether the funnel architecture asserts itself the moment AtoA-free hits a slow week. If the latter is the realistic prediction, paid-EA is the more honest path on the player-experience lens. **A specific R4 question worth asking: would the dev's monetization discipline survive AtoA-free's week-12 install-curve flattening, or would the temptation to surface MtM in-product be the moment the pivot's player-experience story fails?**

---

### Self-rated alignment scores

**Promise 1 — coverage of all TW mode-types at launch: 4/5.** Friction-to-fun (3PL-4), reference-class pattern-match (3PL-2), and beta-tester-perception (3PL-7) all engage Promise 1 directly and surface that paid-EA's framing better honors the "complete at launch" promise from the player's perceived-time perspective. One point withheld because the lens cannot adjudicate whether either path *can* deliver the seven-mode-types polish bar at solo scope — that is PM-lens territory.

**Promise 2 — SC1/WC3 customizability + recognizability: 5/5.** Findings 3PL-2, 3PL-5, 3PL-8, 3PL-10 collectively converge on the audience-priors story, the word-of-mouth story, the hosting-moment story, and the EULA-trust story — all four of which the lens reads as harder under the pivot than under paid-EA. The convergence is the densest in this analysis.

**Promise 3 — optional BP + Ranked layered without compromising regular play: 5/5.** Findings 3PL-3, 3PL-6, 3PL-9 attack the pivot's Promise-3 architecture from three angles (price-as-trust-signal, progression-routing-to-MtM, price-anchor-reset) that R2 Arguer-A's defense (FINDING-2A-4) does not address from the player's lived perspective. Arguer-A's "Promise-3 routes cleanly to MtM" is structurally true and player-experientially incoherent; this lens surfaces the gap.

---

*End of player-lens turn-in. Output: `C:\TW.AtoA\concept\atoa-vs-mtm\round-3\player-lens.md`. Conceptual / refinement / educate / ask / repeat.*
