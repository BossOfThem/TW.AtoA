# Swarmer — Round 3 — Promise 1 Evidence Pack

Role: Web-Swarmer feeding Round-3 superalignment cycle.
Date gathered: 2026-04-28.
Question: **Can a solo dev ship feature-, polish-, art-complete coverage of every TW-genre mode-type (Tower / Line / Hero / Horde / Custom / PVE-Campaign / PVP-Co-op) plus full AtoA scope (3 civs, full ladder, 9 Fusion Gods, 3 commanders)? On which path — two-product free→premium, or paid-EA single-product — is it more reachable?**

Honest-negative-results clause: superalignment requires evidence cuts both ways. Findings below include solo-dev shippers AND ceiling cases (Stormgate, Battle Aces) where many-million-dollar funded teams could not land equivalent scope.

---

## Question framing

The Promise-1 scope is unusually large for a solo dev: seven distinct mode-types, each of which is itself a recognized sub-genre with its own balance, AI, UX, and content requirements, layered on top of three asymmetric civs, a competitive ladder, nine Fusion-God overlay systems, and three commander identities. The relevant base rate is **how long do solo devs actually take to ship multi-mode-type or simulation-class scope, and what do they cut?** The two AtoA paths under contention differ in *when* the scope must be feature-complete: a free-prototype-then-premium-port path defers that bill until the engine port; a paid-EA single-product path forces it onto the same codebase from day one but lets you ship cuts as 1.0 and patch later. Findings below collect base rates from solo or near-solo TW-adjacent / RTS-adjacent / multi-mode-type shippers, and reference ceilings from well-funded-but-failed attempts.

---

## Findings

FINDING-3WP1-1:
  CLAIM: Caves of Qud took **15+ years from 2007 first commit to December 2024 1.0 release**, with the founding pair (Bucklew + Grinblat) only growing past two devs after 2015 Steam EA — and still only reached ~6-person scrum team for the final push. The game ships ONE mode-type (single-player roguelike), not seven.
  SOURCE: https://en.wikipedia.org/wiki/Caves_of_Qud ; https://www.gamespot.com/articles/caves-of-qud-finally-launches-today-after-15-years-of-development/1100-6528256/ ; https://www.cavesofqud.com/press-kit/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Qud's scope (deep simulation, hand-written lore) is arguably *deeper per mode-type* than AtoA's seven shallow mode-types; depth-vs-breadth not directly comparable.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Anchor data point for "two-dev simulation game" timeline — 15 years to 1.0 with one mode-type. AtoA targets seven mode-types solo; even at 1/3 the per-mode depth this implies a multi-decade ceiling unless mode-types are radically thin.

FINDING-3WP1-2:
  CLAIM: Dwarf Fortress took **20+ years of solo programming by Tarn Adams** (full-time from 2006) before the 2022 Steam Premium release that finally added pixel-art graphics, tutorials, and a real UI — and even that art/UX layer was outsourced to modders Mayday and Meph rather than produced by Adams himself. The "free-then-premium" port took 16 years to materialize, sold 160K in 24h and 1M+ by 2025, but the premium port did NOT add new mode-types — it ported the existing one with art bolted on.
  SOURCE: https://stackoverflow.blog/2021/12/31/700000-lines-of-code-20-years-and-one-developer-how-dwarf-fortress-is-built/ ; https://en.wikipedia.org/wiki/Dwarf_Fortress ; https://en.wikipedia.org/wiki/Tarn_Adams
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Dwarf Fortress is an extreme outlier in simulation depth and Tarn Adams is not seeking feature-completeness in the AtoA sense — DF is explicitly "never finished." Also: the *art* layer being outsourced is precisely the model AtoA could use.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Strongest case study for the free→premium-successor pattern. Two takeaways: (a) the prototype absolutely de-risked the design (1M sales prove it), (b) the engine port did NOT reset the clock because Tarn kept the same C++ codebase and added a rendering layer — but he also did not add mode-types. AtoA's plan to add mode-types DURING port multiplies risk.

FINDING-3WP1-3:
  CLAIM: Cogmind solo dev Josh Ge logged **~8,000 hours over 4 years of full-time work** (2017 EA) on a single-mode-type roguelike, outsourcing only tileset and trailer score; full release still pending as of 2026. This is the closest "solo-dev does everything except art" base rate available.
  SOURCE: https://www.gamedeveloper.com/design/-play-87-interview-with-josh-ge-creator-of-cogmind ; https://en.wikipedia.org/wiki/Cogmind ; https://www.gridsagegames.com/cogmind/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Cogmind's scope is again single-mode-type; not a multi-mode-type test.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: 8,000 hours = ~4 person-years for one polished mode-type with outsourced art. Naive multiplication: 7 mode-types × 4 person-years ≈ 28 person-years — clearly infeasible. Argues for radical cuts on either path.

FINDING-3WP1-4:
  CLAIM: Path of Achra (Ulfsire) is the *fastest* successful solo-dev multi-system roguelike on record I could find: **early 2021 start → May 2023 EA → May 2024 1.0** = ~3.3 years total, single mode-type, 20 areas, Hungarian-chef-turned-coder learning from scratch. Notable for tight scope discipline (one mode, deep build variety) — the opposite of AtoA's mode-type breadth.
  SOURCE: https://www.pcgamer.com/games/roguelike/path-of-achra-is-a-bite-size-old-school-dungeon-crawling-dark-fantasy-treat/ ; https://store.steampowered.com/app/2128270/Path_of_Achra/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Achra ships with deliberately retro ASCII-grade art and minimal audio — "polish-complete" by AtoA's standard would not apply. Also genre is much smaller in surface area than RTS.
  PROMISE-1 RELEVANCE (0-5): 4
  RELEVANCE NOTE: This is the lower bound — ~3 years solo, *one* mode-type, polish deliberately constrained. AtoA cannot beat this lower bound while adding 6× more mode-types, 3 civs, and god-overlay systems.

FINDING-3WP1-5:
  CLAIM: Vampire Survivors is the canonical "free HTML5 prototype → premium successor" pattern AtoA emulates: poncle solo, **~1 year HTML5 dev (2020 → March 2021 itch free)**, then **8 months to Steam EA Dec 2021**, full release Oct 2022. BUT: the scope was deliberately micro — one screen, one mode-type, auto-attacks, 8-bit aesthetic. Poncle had to bring on more devs immediately post-success and now operates a multi-studio org with 15+ projects.
  SOURCE: https://en.wikipedia.org/wiki/Vampire_Survivors ; https://wccftech.com/vampire-survivors-developer-poncle-has-over-15-games-in-development-two-original-ips/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Direct precedent for the free→premium path *working fast* — but only because scope was extreme-minimum. The success funded the scaling, not the other way around.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Validates the path *if* scope at premium-port time matches the prototype 1:1. Negative for AtoA if the AtoA-free product is a slim TD prototype but the MtM-premium successor must add 6 more mode-types — that bill comes due in the port and there is no precedent for a solo dev paying it.

FINDING-3WP1-6:
  CLAIM: Stormgate is the ceiling reference: **$35-40M raised** (Kakao, Riot, Kickstarter $2.8M, equity crowdfund $1.2M) by ex-Blizzard SC2/WC3 leads at Frost Giant, targeting *exactly the AtoA mode-type spread* (1v1 ladder, 3v3, co-op missions, campaign), shipped Aug 2024 EA → **50% Steam reviews, 1,000 CCU at launch (down from 5K in EA), studio facing closure 2025-2026**. Cited critic complaints: short campaign, no offline skirmish, no mod support, weak art direction, broken Kickstarter promises.
  SOURCE: https://en.wikipedia.org/wiki/Stormgate ; https://www.gamesradar.com/games/real-time-strategy/stormgate-the-rts-from-ex-starcraft-and-warcraft-devs-launches-out-of-steam-early-access-with-perfect-balance-by-which-i-mean-with-50-percent-positive-user-reviews-we-plan-to-be-in-active-development-for-a-long-time/ ; https://www.gamedeveloper.com/business/frost-giant-ceo-tim-morten-says-layoffs-are-possible-after-stormgate-underperforms ; https://esportsinsider.com/what-happened-to-stormgate
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Stormgate's failures may be design/execution-specific (art, writing, F2P monetization confusion) rather than pure scope-impossibility. Possible some future team could nail the same mode-type spread with the same budget.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: This is the ceiling that matters. ~$40M and ex-Blizzard RTS leads could not deliver a feature-complete multi-mode-type RTS that satisfied players. AtoA's Promise-1 implies a solo dev clears a bar Frost Giant could not at 100× the budget. Strong negative evidence on either AtoA path.

FINDING-3WP1-7:
  CLAIM: Battle Aces (Uncapped Games, Tencent-backed, led by SC2 lead designer David Kim) was **cancelled May 2025 after April 2025 beta** — even with deliberately *narrow* scope (single 10-min PvP mode, no campaign, no co-op). "Returns from early testing not strong enough to support continued development." Funded studio with a top RTS designer could not even get *one* mode-type past the player-retention bar.
  SOURCE: https://www.gamespot.com/articles/this-exhilarating-rts-was-abruptly-canceled-by-its-developers-before-release/1100-6531818/ ; https://www.pcgamesn.com/battle-aces/shut-down-rts-game ; https://www.allkeyshop.com/blog/battle-aces-shut-down-uncapped-games-cancelled-rts-project-news-r/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Cancellation was retention-driven, not scope-driven; the team *could* have shipped, they chose not to. AtoA could ship a similarly narrow product without retention-test cancellation pressure since solo dev has no investors to satisfy.
  PROMISE-1 RELEVANCE (0-5): 4
  RELEVANCE NOTE: Reinforces the genre-difficulty signal even at zero scope. The TW-adjacent / RTS market is brutal even for *narrow* scope; solo-dev attempting 7 mode-types broad-scope is fighting two wars at once.

FINDING-3WP1-8:
  CLAIM: They Are Billions (Numantian Games, small team — not strictly solo but small) entered **EA Dec 2017 with survival mode only**, shipped 1.0 with the campaign **18 months later (June 2019)**. The campaign ("New Empire") was widely judged underwhelming and was the slowest, most-cut part of the 1.0 push. This is the closest analog of "ship one mode in EA, add a second mode for 1.0" — and it took 18 months for a small team for ONE additional mode-type, with quality compromises.
  SOURCE: https://en.wikipedia.org/wiki/They_Are_Billions ; https://www.vice.com/en/article/they-are-billions-gets-the-single-player-campaign-nobody-needed/ ; https://store.steampowered.com/app/644930/They_Are_Billions/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Numantian had > 1 person and was not solo; also they wrote a custom 20K-unit engine which inflated time. AtoA could pick a turnkey engine.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Best apples-to-apples for "add one new mode-type post-EA" cost: ~18 small-team-months. Multiply for 6 additional mode-types: 9 small-team-years. Solo dev → 18+ years on naive math. Hard ceiling on Promise-1.

FINDING-3WP1-9:
  CLAIM: Solo-dev shipper *with broad mode coverage* base rate is essentially zero. Successful solo or 1-person-shop shippers (Brotato/Blobfish, Dome Keeper/Bippinbits 2-person, Path of Achra/Ulfsire, Vampire Survivors/poncle, Cogmind/Ge) all share **ONE mode-type with depth variation** (build variety, biome variety, character variety) rather than mode-type breadth. Brotato added local co-op via DLC ~2 years post-1.0; online co-op was publicly declined as too costly. Bippinbits (2 devs) added 1 expansion since 2022 1.0.
  SOURCE: https://en.wikipedia.org/wiki/Brotato ; https://store.steampowered.com/app/1942280/Brotato/ ; https://en.wikipedia.org/wiki/Dome_Keeper ; https://howtomarketagame.com/2022/10/17/how-dome-keeper-achieved-a-million-dollar-launch/ ; https://steamcommunity.com/app/1942280/discussions/0/4696784170963208867/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Absence of evidence isn't evidence of absence; perhaps no one has *tried* the multi-mode-type solo approach because it is unfashionable rather than impossible.
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Strongest Bayesian prior available. Across the entire successful-solo-dev population I could find, none ship 7 mode-types — all converge on one mode + variety. This argues AtoA must either (a) cut to 1-2 mode-types on either path, or (b) accept that "feature-complete coverage" of all 7 is the unachievable promise, not a pivotable detail.

FINDING-3WP1-10:
  CLAIM: Successful EA-to-1.0 shippers in adjacent genres (Slay the Spire 14mo, Dead Cells 15mo, Deep Rock Galactic 27mo, Factorio 54mo, Baldur's Gate 3 34mo) all shipped on **single-mode-type cores** with content/depth additions during EA. Over 50% of EA games never reach 1.0 at all. There is no precedent in the searched record for an EA game adding additional *mode-types* (vs. content/depth) during EA and shipping 1.0 successfully — the closest analog is They Are Billions adding campaign, with mixed reception.
  SOURCE: https://en.wikipedia.org/wiki/Early_access ; https://fictionhorizon.com/20-early-access-success-stories-that-stuck-the-landing/ ; https://www.wayline.io/blog/early-access-indie-savior-or-slow-death
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Survey is incomplete; Hades is sometimes cited as adding modes (heat / pact-of-punishment) but those are difficulty layers, not mode-types. ZeroSpace (Starlance, ~2026 EA) attempts the AtoA-style breadth at small-team scale and is too early to verify, but it's a flashing yellow signal — RPGCodex tagged it "Feature Creep: The RTS."
  PROMISE-1 RELEVANCE (0-5): 5
  RELEVANCE NOTE: EA convention is depth-during-EA, not breadth-during-EA. Paid-EA single-product path for AtoA assumes the *opposite* convention is fine; no precedent supports it.

FINDING-3WP1-11:
  CLAIM: Cataclysm: Dark Days Ahead — sometimes cited as a "one-dev" simulation — is actually maintained by **1000+ volunteer contributors over 13 years** since the 2013 fork; 50-100 active any given month, ~450 contributing to a single recent release. The deep-simulation TW/Qud-tier scope is sustainable only via open-source community labor, not solo effort.
  SOURCE: https://en.wikipedia.org/wiki/Cataclysm:_Dark_Days_Ahead ; https://github.com/CleverRaven/Cataclysm-DDA
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Open-source path is theoretically available to AtoA but explicitly not the chosen monetization path.
  PROMISE-1 RELEVANCE (0-5): 4
  RELEVANCE NOTE: Confirms that "deep multi-system game" + "solo" is essentially mutually exclusive at AtoA's claimed scope. Either the scope shrinks, the team grows, or the game opens its source.

---

## Reachability honest assessment

The searched evidence runs strongly negative on Promise-1 in its full-scope form on **either** path. Across the entire population of solo-dev success stories I could surface (Vampire Survivors, Brotato, Path of Achra, Dome Keeper, Cogmind, Caves of Qud, Dwarf Fortress), the consistent shape is **one mode-type with variety-depth, 3–15+ years to 1.0, art outsourced where present at all**. Nobody ships 7 mode-types solo, and the ceiling reference (Stormgate, $35-40M, ex-Blizzard RTS leads, exactly the AtoA mode-spread) demonstrates that even with two orders of magnitude more resource, a feature-complete multi-mode-type TW-genre product can fail to land. Of the two paths under contention, the **free→premium two-product path has the stronger precedent for the *prototype* step** (Vampire Survivors and Dwarf Fortress's premium port both validate the pattern) but no precedent for a solo dev *adding mode-types during the engine port* — Tarn kept his same one mode and bolted art on; poncle kept his same one mode and added platforms. The **paid-EA single-product path** has stronger genre-precedent for the EA→1.0 mechanism itself (Slay the Spire, Dead Cells, Factorio, BG3) but those all shipped single-mode-type cores; the only multi-mode-type EA→1.0 case (They Are Billions adding a campaign) took 18 months for a small team to add *one* mode at compromised quality. The honest read is that Promise-1 as currently scoped (7 mode-types feature-, polish-, and art-complete, 3 civs, full ladder, 9 Fusion Gods, 3 commanders) is **not reachable solo on either path** within any timeframe consistent with a viable indie career; reachability requires a mandatory written scope-cut (likely to 2–3 mode-types feature-complete + the rest as deferred / community / cut), and on that cut-scope basis the free→premium path inherits more validated precedent (the prototype de-risks; the port is a known shape) while the paid-EA path inherits more EA-economics precedent (paying customers fund the burn). Neither is a slam-dunk; both require the same scope cut to be honest. The biggest red flag in the data is that AtoA's Promise-1 implicitly claims to clear a bar that $40M and ex-Blizzard leads could not — and no narrative about the solo-dev path resolves that gap.

