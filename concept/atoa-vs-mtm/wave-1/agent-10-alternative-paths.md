# Agent 10 — Alternative Product-Shape Scout (Wave 1)

**Role:** R2-Alternative ammunition supplier. Hunts product-shapes that the current pivot (HTML/free AtoA → engine/premium MtM, sequential) might be foreclosing. Output feeds R2 Arguer B.

---

## The space of plausible alternative shapes

The current pivot — sequential two-product, free HTML AtoA first then premium engine MtM — is one point in a multi-dimensional shape space defined by (a) **distribution channel** (Steam / web / itch / mobile / multi), (b) **price model** (free / freemium / premium / Early Access / episodic / subscription), (c) **content commitment** (full-scope solo+MP / multiplayer-only / vertical slice / chapter), (d) **engine** (HTML / native / hybrid / parallel), and (e) **funding** (self / publisher / Patreon / KS / EA-as-funding). The pivot collapses several of those axes simultaneously — it picks free+HTML+Steam+full-scope+sequential at once. Any of these axes can be moved independently. Notably, several recent comparable launches (Stormgate, Battle Aces) failed precisely because they over-committed scope at premature distribution moments — which is exactly the risk that lurks in a free-Steam-first shape if "free" anchors expectations the engine successor can't escape. The space worth surveying is therefore not "free vs paid" but "which combination of these five axes survives a Stormgate-style scope shock?"

---

## Catalog of candidate alternative shapes

| # | Shape | 1-line | Promise-1 fit | Promise-2 fit | Promise-3 fit | Biggest risk |
|---|-------|--------|---|---|---|---|
| A | **Single-product premium launch** ($15–25, no free) | Skip free entirely; ship one paid Steam product | 4 | 3 | 3 | If quality bar misses, no on-ramp to recover |
| B | **F2P cosmetics-only single-product** | One product, F2P, cosmetics + BP only | 4 | 4 | 5 | F2P on Steam needs ARC-Raiders-tier polish or it's invisible |
| C | **Web-only / itch-only** | Skip Steam entirely | 1 | 5 | 1 | No discoverability engine; itch browser analytics weak |
| D | **Mobile-first** | Ship mobile TD/TW first, port up | 2 | 1 | 5 | TW-genre custom-lobby identity dies on touch UI |
| E | **Episodic / chapter** | Drip civs / modes / commanders as chapters | 3 | 2 | 4 | 7-mode-type commitment fights episodic structure |
| F | **Paid Early Access on Steam** | EA at $15, full launch later | 5 | 4 | 4 | EA expectation is a *path to 1.0*; Stormgate proved this hostile to incomplete mode rosters |
| G | **AtoA = free demo / vertical slice** (not full free product) | AtoA is a wishlist-driver demo, not the product | 3 | 3 | 2 | Loses the "AtoA ships first as a real game" anchor |
| H | **Parallel HTML+engine builds** | Both products developed simultaneously | 5 | 4 | 4 | Solo-first = roughly 2x scope at once; resource-fatal |
| I | **Patreon-funded ongoing development** | No launch event; fund rolling expansion | 2 | 4 | 5 | Requires existing audience AtoA does not have |
| J | **Multiplayer-only minimal SP** | Cut solo-first, ship MP-only | 0 | 3 | 4 | Violates north-star solo-first; Stormgate cautionary tale |
| K | **Hybrid premium + free benchmark mode** | One paid product, one free "lobby/sandbox" mode permanently free | 4 | 5 | 3 | Splits identity; requires careful firewall |
| L | **Publisher / Game Pass deal** | Sign with mid-tier publisher; day-one Game Pass | 4 | 3 | 3 | Loss of creative control; hard to land cold |

Findings that score 0 across all three promises were dropped. Shape J kept because it's a real industry pattern even though it fails P1.

---

## Deep dives — top 3 nominees for R2 Arguer B

### Nominee 1: Shape F — **Paid Early Access on Steam, single product**

The strongest case against the current pivot is that "free HTML first" optimizes for a problem (audience generation) the EA model arguably solves better while *also* solving the funding and feedback problems the current pivot leaves unsolved. EA contributed ~24% of successful 2024 indie titles and 23.67% of revenue; EA games posted higher median engagement (38.9h vs 27.1h playtime) and higher median review scores (86% vs 81%) than full releases. Crucially, EA *converts wishlist intent into paid commitment immediately*, where free-HTML-first deliberately defers monetization to a successor product that may never ship. Hades, Hades 2, Vampire Survivors, Palworld all used paid EA to fund completion while building community. The pivot's logic ("we need audience before we can charge") is what EA was invented to solve.

**Real successes (in/near genre):** Hades (paid EA $20 → 1.0 success); Vampire Survivors (paid EA → cultural phenomenon); Manor Lords (paid EA, RTS-adjacent, multi-million units); They Are Billions (paid EA, RTS+TD, very strong). **Failures:** Stormgate (free EA, wrong-pricing decision; <1k concurrent at launch); Sanctuary Shore-style EA bleeds where scope was wrong; many EAs that drop below 50 reviews and stall.

**Promise fit:** P1 = 5 (EA explicitly accommodates incomplete mode coverage as a known-state, not a broken-promise); P2 = 4 (custom-lobby identity ports cleanly to paid EA and EA players are exactly the modder/customizer demographic); P3 = 4 (BP/Ranked layer well to a paid EA → 1.0 transition).

**Biggest risk:** Stormgate proves EA can fail catastrophically when scope at launch is wrong even with massive funding ($36M+); the *pricing* of EA matters less than the *state* of the build at first impression.

### Nominee 2: Shape A — **Single-product premium launch ($15–20)**

The "$15–20 sweet spot + quality that exceeds expectations" finding from 2025 Steam data is the most underweighted signal in the current pivot. Hollow Knight Silksong ($20, $81.6M); Clair Obscur ($49.99, 4.6M units, 95% positive); Balatro ($14.99, multi-million units). The pivot assumes "free is the lowest-friction on-ramp," but Steam data shows under-$10 conversion is ~15% and $10+ is ~10% — meaning a $15–20 paid product converts *wishlists into dollars* nearly as efficiently as a $9.99 product converts them into installs. Free, by contrast, has no conversion event at all until MtM exists. The pivot's two-product architecture exists largely to dodge the premium-launch decision; if AtoA is good enough to ship, charging $15 for it skips the entire MtM-as-monetization-recovery dependency.

**Successes:** Hollow Knight ($15→Silksong $20); Balatro ($14.99); Slay the Spire ($25); Into the Breach ($14.99). **Failures:** dozens of $19.99 indie strategy games annually that vanish under 1k reviews — premium pricing punishes weak quality where free hides it.

**Promise fit:** P1 = 4 (forces tighter scope discipline, which may *help* hitting all 7 mode-types at quality); P2 = 3 (custom lobbies thrive on premium PC where modders converge); P3 = 3 (BP/Ranked still works on premium base — see Deep Rock Galactic).

**Biggest risk:** Premium with unknown IP and 7-mode-type promise is a quality-bar that's ~Clair-Obscur-level to clear; below that, total flop.

### Nominee 3: Shape H — **Parallel HTML+engine builds (not sequential)**

The sequential assumption in the current pivot has a hidden cost: AtoA must be feature-complete *before* MtM development meaningfully begins, which means the engine-product is gated on the success of a free product whose monetization may not fund it. Parallel development — even at 60/40 effort split — means MtM enters EA the moment AtoA hits 1.0, compressing the "cliff" between products. Crashlands shipped Steam+iOS+Android same-day; Unity 2024 data shows 71% increase in multiplatform indie titles. Two ports of the same design built in parallel is a known pattern; what's unusual here is that "HTML" and "engine" are not just ports but two *product tiers*. The sequential framing may be reasoning about resources that parallel development could partially share (data model, balance tables, art).

**Successes:** Crashlands (sim-launch); Stardew Valley (post-launch parallel ports); Dead Cells (multi-platform near-sim). **Failures:** Many studios that tried parallel and shipped nothing (most cited as "scope death"); No Man's Sky-style platform splits causing launch-state mismatches.

**Promise fit:** P1 = 5 (full scope demonstrated *across both products* not deferred); P2 = 4 (custom-lobby identity tested twice); P3 = 4 (monetization layer on engine product doesn't wait for AtoA).

**Biggest risk:** Solo-first means one person; parallel = 2x active scope = highest probability of shipping nothing.

---

## Findings

```
FINDING-1-10-1:
  CLAIM: Paid Early Access on Steam outperformed free Early Access on every observable engagement metric in 2024 (38.9h median playtime vs 27.1h, 86% vs 81% review score, 23.67% of 2024 indie revenue).
  SOURCE: opgamemarketing.substack.com 2024 Indie Game Market analysis; gamedevreports.substack.com Steam Indie 2024
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: EA failure rate is still high in absolute terms; only ~25% of EA games reach 1.0
  PROMISE-1 RELEVANCE (0-5): 5
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: EA explicitly accommodates incomplete-state shipping (P1), attracts the modder/customizer audience (P2), and provides the funding bridge to BP/Ranked (P3).
```

```
FINDING-1-10-2:
  CLAIM: Stormgate's free Early Access launch with $36M+ funding peaked under 1,000 concurrent at "1.0" launch and is exiting EA without finishing core modes — directly comparable to a free AtoA shipping incomplete TW-mode coverage.
  SOURCE: pcgamer.com Stormgate coverage; massivelyop.com 2025/07/23
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Stormgate had specific design failures (visual style, faction identity) beyond pricing model
  PROMISE-1 RELEVANCE (0-5): 5
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: Free-first did NOT solve Stormgate's discoverability or scope problem; cautionary for the current pivot.
```

```
FINDING-1-10-3:
  CLAIM: $15–$20 premium pricing with quality-exceeds-expectations (Silksong $20→$81.6M, Clair Obscur $49.99→4.6M units, Balatro $14.99→multi-million) outperforms expected-quality $30 pricing in 2025 Steam data.
  SOURCE: SteamData Research 2025; alineaanalytics.substack.com top 2025 games
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Survivor bias — cited examples are top 0.1%; majority of $15–20 indies fail
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 3
  PROMISE-3 RELEVANCE (0-5): 3
  RELEVANCE NOTE: Premium pricing converts wishlists to dollars at rates comparable to free converting to installs, removing the need for a sequential MtM-as-monetization-recovery product.
```

```
FINDING-1-10-4:
  CLAIM: F2P on Steam in 2025 generated $378M+ across just two titles (ARC Raiders, Where Winds Meet) with $34+ ARPU — proving F2P-cosmetics works but only at AAA-polish thresholds AtoA cannot meet alone.
  SOURCE: SteamData Research 2025
  STRENGTH: high
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Most F2P Steam launches die in obscurity; the model has heavy survivorship bias
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: A single F2P-cosmetics-only product is a real alternative to two-product sequencing — but quality-bar is the binding constraint, same as premium.
```

```
FINDING-1-10-5:
  CLAIM: Steam Next Fest demos generate 2,000–10,000+ wishlists per appearance with higher buy-intent than trailer-only wishlists (29.5% of YAPYAP wishlisters had played the demo; 5.5% conversion at 23 days post-launch).
  SOURCE: alineaanalytics.substack.com wishlist conversion analysis; gamedevreports.substack.com
  STRENGTH: medium
  CONFIDENCE: high
  COUNTER-EVIDENCE: Demo strategy assumes a paid product to convert *to*
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 3
  PROMISE-3 RELEVANCE (0-5): 2
  RELEVANCE NOTE: The "AtoA as demo for MtM" shape is empirically supported as a wishlist-conversion engine, distinct from "AtoA as free full product."
```

```
FINDING-1-10-6:
  CLAIM: Patreon ongoing-development models can sustain $40k+/month (Paralives 8,511 patrons, $41,533/mo) but require pre-existing audience that AtoA does not have at zero.
  SOURCE: gamedeveloper.com Patreon analysis; growthhq.io crowdfunding strategy
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Cold-start Patreon is essentially zero revenue
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 4
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Patreon's content-drop cadence resembles the BP/seasonal layer the current pivot defers to MtM — could collapse the two-product split into one rolling product.
```

```
FINDING-1-10-7:
  CLAIM: Indie cross-platform sim-launches (Crashlands; Unity 2024 data: 71% increase in indie multiplatform titles) reduce marketing overhead and tipping-point cultural moments compared to staged rollouts.
  SOURCE: gamedeveloper.com Crashlands postmortem; Unity 2024 Gaming Report
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Sim-launch failures rarely written up; survivorship in this dataset is severe
  PROMISE-1 RELEVANCE (0-5): 4
  PROMISE-2 RELEVANCE (0-5): 3
  PROMISE-3 RELEVANCE (0-5): 4
  RELEVANCE NOTE: Sequential two-product is a *choice*, not a constraint; parallel is industry-trending.
```

```
FINDING-1-10-8:
  CLAIM: 20,282 games shipped on Steam in 2025 and only 608 cleared 1,000 reviews — discoverability is the binding constraint regardless of price model.
  SOURCE: gamesradar.com 2025 Steam release stats
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: none
  PROMISE-1 RELEVANCE (0-5): 3
  PROMISE-2 RELEVANCE (0-5): 3
  PROMISE-3 RELEVANCE (0-5): 3
  RELEVANCE NOTE: The pivot's "free for discoverability" logic is true in direction but Steam algorithm rewards *momentum signal*, not price — paid EA with strong review velocity beats free with weak signal.
```

```
FINDING-1-10-9:
  CLAIM: Mobile tower-defense F2P (Random Dice ~$80M Y1, Rush Royale, Bloons TD 6 mobile $0.99 + IAP) outperforms PC TD revenue by orders of magnitude — but the TW-genre custom-lobby identity (P2) does not transfer to mobile UX.
  SOURCE: askgptai.com 2025 mobile TD analysis; bloonswiki
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Mobile-first development cost and UA spend is far higher than indie PC
  PROMISE-1 RELEVANCE (0-5): 2
  PROMISE-2 RELEVANCE (0-5): 1
  PROMISE-3 RELEVANCE (0-5): 5
  RELEVANCE NOTE: Mobile is the highest-revenue alternative shape but kills the TW-custom-lobby promise; useful only as a downstream port shape, not a launch shape.
```

---

## Open questions for the PM

1. **Which alternative do you find hardest to dismiss out of hand?** (The mandated question; please be honest — even a "hard to dismiss but still rejecting" answer steers R2 Arguer B usefully.)
2. Has the pivot decision tested **Shape F (paid EA single-product)** specifically against the current sequential model? The Hades / Manor Lords / They Are Billions cluster suggests this is the closest-fit reference class for an unfinished-but-shippable TW-style game, and "free" foregoes the EA review-velocity signal that drives Steam's algorithm.
3. The **Stormgate failure mode** (free EA, $36M, peak <1k at launch, exits without finishing core modes) is uncomfortably close to the current pivot's risk profile. What does the pivot do differently that makes its outcome diverge from Stormgate's?
4. Is the **two-product split a feature or a workaround**? If MtM exists primarily because AtoA-as-free can't monetize, then Shape A (single premium product) or Shape F (paid EA → 1.0) collapses the split entirely. What does the second product *uniquely* deliver that one product at the right price+state could not?
5. What's the **resource budget assumption** behind sequential vs parallel (Shape H)? If it's "solo dev cannot do parallel," that's the binding constraint, not "sequential is optimal" — which is a different conversation.

---

## Sources

- [SteamData Research — Steam in 2025](https://medium.com/@research_86150/steam-in-2025-the-year-indie-games-ate-the-industry-alive-666abf04551f)
- [Alinea Analytics — Top 2025 games](https://alineaanalytics.substack.com/p/the-top-new-2025-games-by-players)
- [GamesRadar — 20,282 Steam games 2025](https://www.gamesradar.com/games/a-terrifying-20-282-games-were-released-on-steam-in-2025-and-just-608-managed-to-get-1-000-reviews-expert-finds-we-might-be-in-a-bit-of-an-indie-golden-age/)
- [OPGM 2024 Indie & AA Market](https://opgamemarketing.substack.com/p/the-2024-indie-and-aa-game-market)
- [Digital Trends — Early Access mainstream 2024](https://www.digitaltrends.com/gaming/early-access-gaming-2024-interview/)
- [PCGamer — Stormgate multiplayer loss](https://www.pcgamer.com/games/rts/stormgate-the-starcraft-like-rts-that-launched-last-summer-is-losing-online-multiplayer-support-because-its-server-partner-was-bought-by-an-ai-company/)
- [Massively Overpowered — Stormgate exits EA without 1.0](https://massivelyop.com/2025/07/23/multiplayer-rts-stormgate-will-leave-early-access-without-achieving-1-0-or-finishing-core-game-modes/)
- [Alinea — Wishlist-to-buyer conversions Next Fest](https://alineaanalytics.substack.com/p/wishlist-to-buyer-conversions-for)
- [GameDeveloper — Patreon for game dev](https://www.gamedeveloper.com/business/the-benefits-and-risks-of-using-patreon-to-crowdfund-games)
- [GameDeveloper — Crashlands cross-platform launch notes](https://www.gamedeveloper.com/business/notes-from-an-indie-cross-platform-launch)
- [AskGPTAI — Mobile TD market 2025](https://askgptai.com/mobile-tower-defense-games-market-analysis-2025/)
- [Notebookcheck — Indie 25% of Steam revenue 2025](https://www.notebookcheck.net/Indie-games-accounted-for-25-of-Steam-s-revenue-in-2025.1189429.0.html)
