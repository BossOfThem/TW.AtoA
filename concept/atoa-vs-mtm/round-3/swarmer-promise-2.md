# Web-Swarmer — Round 3, Promise 2 (lobby substrate funding mechanism)

Role: Web-Swarmer in superaligned swarm Round 3.
Date gathered: 2026-04-28.
Promise under examination: "the customizability and recognizability of SC1 / WC3 custom lobbies that no standalone TW has reproduced."
Question: which product-shape (free→premium two-product vs. paid-EA single-product) actually pays for the lobby substrate?

---

## 1. Question framing — what "lobby substrate" actually decomposes into

"Lobby substrate" is not one feature; it's a stack of five distinct engineering investments, each with its own cost curve and historically distinct cut-points in indie / mid-budget development:

1. **Map/terrain editor** — an in-engine WYSIWYG tool with brush-painting, doodad placement, trigger-region authoring. Cheapest of the five if the engine already exposes a level format.
2. **Data/unit editor + scripting layer** — the real expense. Galaxy Editor and the WC3 World Editor are powerful precisely because they expose nearly every unit/ability data field plus a Turing-complete scripting language (JASS, Galaxy Script). This is the ceiling that almost every indie cuts.
3. **Hosting / matchmaking / lobby-server infrastructure** — the persistent room metaphor: chat channels, public lobby browser, host-migration, regional servers, anti-cheat. The "Battle.net 1.0 chat-room" feel is here, not in the editor.
4. **Custom-game discovery & distribution** — Workshop integration, popularity ranking, search, "play" button piping a custom mod into a runnable session for someone who doesn't own the editor.
5. **Replay / observer / streamer-mode** — deterministic-replay record/playback, multi-camera spectator UI, casting overlays, delay/fog-of-war controls. Often punted to post-launch even by AAA.

These five are usually conflated in marketing as "the editor," but they're orthogonal in budget terms — and the historical record below shows clear patterns about which get cut first.

---

## 2. Findings

FINDING-3WP2-1:
  CLAIM: Frost Giant raised ~$34.7M in venture funding (Riot, BITKRAFT, Kakao) plus $2.38M on Kickstarter — by far the best-capitalised standalone-TW-genre attempt of the past decade — and *still* shipped 1.0 (Aug 2025) without a full custom-game editor; only a Terrain Editor alpha (no data, no triggers) was available, with the deeper editor and Arcade-style discovery slipped to undated post-launch milestones.
  SOURCE: https://www.pcgamer.com/stormgate-kickstarter-funding/ ; https://playstormgate.com/news/the-stormgate-roadmap ; https://playstormgate.com/news/terrain-editor-alpha
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Frost Giant's failure modes are multi-causal (player retention, F2P-monetization tuning, COVID-era investor dry-up); editor-cost alone didn't sink them, so attributing the editor-cut to budget rather than priority is partially inferential.
  PROMISE-2 RELEVANCE: 5
  RELEVANCE NOTE: This is the *control case*. If $37M and ex-Blizzard SC2 leadership cannot deliver the full lobby substrate with 1.0, no realistic indie/solo budget can. Validates that the substrate is the most-cut feature in the genre.

FINDING-3WP2-2:
  CLAIM: Frost Giant publicly chose free-to-play specifically because CEO Tim Morten argued the RTS genre needed an F2P entry to "break down barriers" of paid friction — i.e., even the best-funded TW-genre attempt's leadership concluded a free product-shape was prerequisite to reaching the audience the lobby substrate is built for.
  SOURCE: https://www.nme.com/features/gaming-features/frost-giant-studios-ceo-tim-morten-on-stormgate-the-rts-genres-best-days-are-ahead-3252433 ; https://playstormgate.com/news/frost-giant-business-faq
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Stormgate's F2P launch underperformed (~1K CCU at 1.0 vs. 5K in EA) — so the F2P decision didn't *pay off*, which is at least suggestive that "free shape" alone isn't sufficient; product quality and retention dominated. The financial outcome doesn't validate F2P as a funding mechanism for the editor.
  PROMISE-2 RELEVANCE: 5
  RELEVANCE NOTE: Strongest expert-leadership signal that the lobby-substrate audience requires a free entry point — but also a cautionary tale that "free" without a converting paid layer doesn't fund the substrate either.

FINDING-3WP2-3:
  CLAIM: SC2's Battle.net 2.0 / Arcade was widely criticised for *technically* having the substrate (Galaxy Editor is functionally a superset of the WC3 World Editor) but failing on the *social-discovery* layer — replacing Bnet 1.0's chat-room model with a popularity-ranked list crushed long-tail custom-game visibility, demonstrating that having the editor is necessary but not sufficient; the lobby/chat/discovery layer is a separate cost-and-design problem.
  SOURCE: https://www.neogaf.com/threads/interface-battle-dota-2-custom-games-vs-starcraft-2-arcade-vs-bnet-1-0.1109969/ ; https://us.forums.blizzard.com/en/sc2/t/suggestions-for-improving-the-custom-arcade-lobby/31853
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: SC2 Arcade did host hits (Squadron TD, Direct Strike) — the substrate worked for top-N maps; "failure" of long-tail is qualitative and contested.
  PROMISE-2 RELEVANCE: 5
  RELEVANCE NOTE: Decomposes the promise: SC1/WC3 *recognizability* is the chat-room/discovery layer, not the editor. AtoA must replicate the social shape, not just ship a tool.

FINDING-3WP2-4:
  CLAIM: Beyond All Reason — the closest live free standalone-TW analog (Spring/Recoil engine, free, open-source, 150+ contributors) — explicitly states they "don't support full moddability and customization" because "we simply don't have the developer time"; modders can write widgets but full mod support is deferred. A free, volunteer-funded shape did NOT pay for the deep substrate.
  SOURCE: https://www.beyondallreason.info/faq ; https://en.wikipedia.org/wiki/Beyond_All_Reason
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: BAR is alpha and pre-revenue; this is "not yet" rather than "never." They inherited the SpringRTS engine's existing moddability for free, which is a hidden subsidy not available to AtoA.
  PROMISE-2 RELEVANCE: 5
  RELEVANCE NOTE: Direct counterexample to "free shape funds the substrate" — pure-free, no-monetization shapes punt the deep editor indefinitely. Suggests AtoA's pivot needs a paid successor specifically to fund Tier-2 (data/scripting).

FINDING-3WP2-5:
  CLAIM: Zero-K — another free open-source Spring-engine RTS — DOES ship a mission editor, custom modes, mutators, and a working lobby — but has been in development since 2010 (15+ years) sustained by volunteer labour, not a commercial funding model. The lobby substrate exists but the funding mechanism is "decade-plus of unpaid contributors," which doesn't generalize.
  SOURCE: https://zero-k.info/ ; https://en.wikipedia.org/wiki/Zero-K ; https://github.com/ZeroK-RTS/Zero-K
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Zero-K's substrate quality vs. SC2 Arcade is debatable; it serves a niche, not "recognizable" mass market. Also leans heavily on inherited Spring engine.
  PROMISE-2 RELEVANCE: 4
  RELEVANCE NOTE: Demonstrates the substrate is achievable on $0 budget *if* you trade money for time at decade-scale — not a model AtoA can adopt with any commercial timeline.

FINDING-3WP2-6:
  CLAIM: Stardew Valley (paid premium, single dev) shipped 1.0 in 2016 with NO official mod support; the entire mod scene runs on community-built SMAPI loader. ConcernedApe only added first-party mod awareness in 1.6 (2024), eight years post-launch — a documented case of "paid-EA / paid-premium single-product" deferring substrate work for nearly a decade.
  SOURCE: https://github.com/Pathoschild/SMAPI ; https://stardewvalleywiki.com/Modding:Player_Guide/Getting_Started
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Stardew is a singleplayer game; lobby substrate isn't comparable to multiplayer-RTS scope. The community-loader pattern *did* produce a thriving mod scene without dev cost — arguably a feature, not a failure.
  PROMISE-2 RELEVANCE: 3
  RELEVANCE NOTE: Paid-premium single-product evidence: solo devs with paid revenue still cut official modding tools at launch, leaning on community to build the loader. AtoA's promise to ship the substrate at launch is unprecedented at this budget tier.

FINDING-3WP2-7:
  CLAIM: Caves of Qud (paid Early Access from 2015, full release Dec 2024) added Steam Workshop mod support during EA but the *deep* modding hooks (XML, Lua scripts, asset replacement) were rolled out incrementally over a 9-year EA window — paid-EA model funded the substrate piecewise, not at-launch.
  SOURCE: https://wiki.cavesofqud.com/wiki/Modding:Overview ; https://steamcommunity.com/workshop/about/?appid=333640
  STRENGTH: medium
  CONFIDENCE: medium
  COUNTER-EVIDENCE: Search didn't surface a precise milestone date for Workshop integration; the 9-year claim is directional, not exact.
  PROMISE-2 RELEVANCE: 3
  RELEVANCE NOTE: Strongest positive case for paid-EA: a long EA window (years) lets revenue trickle in to fund substrate piecewise. AtoA's pivot timeline likely doesn't grant this much runway.

FINDING-3WP2-8:
  CLAIM: Terraria's modding substrate is *entirely community-built* (tModLoader, open-source, free), shipped as a free Steam DLC alongside the paid base game. Re-Logic did not build it themselves; they sanctioned it post-hoc. This is the dominant indie pattern: paid base game + free community-built loader.
  SOURCE: https://store.steampowered.com/app/1281930/tModLoader/ ; https://github.com/tModLoader/tModLoader
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Terraria is single/coop, not lobby-driven multiplayer; the discovery / matchmaking layer is absent from its scope.
  PROMISE-2 RELEVANCE: 3
  RELEVANCE NOTE: Paid-premium games typically *don't pay for* the substrate themselves — the community does, free, after launch. Forces the question whether AtoA can lean on a community loader rather than first-party engineering.

FINDING-3WP2-9:
  CLAIM: A Hat in Time's "Creator DLC" model — paid-premium base game + community-authored mod packs curated and sold/distributed officially — is the cleanest example of a paid single-product paying for *integration* of a community-built substrate, but the editor itself ships with the base game (Unreal-based, leveraging engine tools), not built bespoke. Bespoke editor cost was ~zero because Unreal already had it.
  SOURCE: https://ahatintime.wiki.gg/wiki/Creator_DLC ; https://store.steampowered.com/news/app/253230/view/2907592728174327915
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Unreal Engine licensing is a hidden subsidy; an AtoA bespoke engine doesn't get this for free. Single-player-style platformer is also a far simpler substrate than RTS-lobby.
  PROMISE-2 RELEVANCE: 3
  RELEVANCE NOTE: Suggests engine choice (Unreal/Unity vs. bespoke) materially changes whether paid-EA can fund the substrate. AtoA's engine-lock decision in Phase 4 is load-bearing on Promise 2.

FINDING-3WP2-10:
  CLAIM: DotA's full graduation arc — free WC3 custom map → Valve-funded free-to-play standalone (Dota 2, 2013) → Auto Chess mod (2019) → multiple paid-tier successors (TFT, Underlords, standalone Auto Chess) — is the single best-documented case of a free custom-lobby substrate generating multiple downstream commercial products. The substrate's *value* is realised by spawning successors, not by monetizing the substrate itself.
  SOURCE: https://en.wikipedia.org/wiki/Defense_of_the_Ancients ; https://en.wikipedia.org/wiki/Dota_Auto_Chess
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: Every successor was funded by *external* studios (Valve, Riot, Drodo) — the original WC3 substrate didn't fund itself; Blizzard built it for ~$0 marginal return on the lobby layer. The funnel is real but the funder is always upstream.
  PROMISE-2 RELEVANCE: 5
  RELEVANCE NOTE: Pattern-matches AtoA→MtM precisely: free substrate produces validated genre slices, paid successor (MtM) captures the value. Strongest historical analog for the two-product pivot.

FINDING-3WP2-11:
  CLAIM: Replay/observer/spectator UI is consistently treated as a post-launch addition even by AAA — Riot publicly delayed LoL replays for years citing "backpatching" engineering complexity; Overwatch, Heroes of the Storm, and others all shipped without it and added it post-launch. This sub-layer of the substrate is the most universally cut for budget/scope reasons.
  SOURCE: https://esportsedition.com/league-of-legends/league-replay-system/ ; https://blizzpro.com/2014/10/07/heroes-features-custom-games-observer-mode-replays/
  STRENGTH: high
  CONFIDENCE: high
  COUNTER-EVIDENCE: SC1/WC3/SC2 all shipped replays at launch — so the "TW-genre baseline" is actually higher than other genres on this axis. Calling it routinely cut is genre-conditional.
  PROMISE-2 RELEVANCE: 4
  RELEVANCE NOTE: Within the five-tier decomposition, replay/observer is the most plausible deferral candidate even for AtoA — the genre baseline expects it but the engineering is non-trivial and routinely slips.

---

## 3. Funding-mechanism honest assessment

The cleanest read of the evidence is that **neither product-shape "pays for" the full lobby substrate at indie/solo budgets — both shapes cut it.** Stormgate cut it at $37M. BAR cut it on free/volunteer labour. Stardew deferred it 8 years on paid-premium. Terraria outsourced it to community labour. The historical pattern is: the substrate is *never* fully funded at launch by the product carrying it; it is either (a) inherited from an engine subsidy (Unreal, Spring), (b) outsourced to community loaders (SMAPI, tModLoader), (c) deferred to long EA tails (Caves of Qud), or (d) built by an upstream platform giant (Blizzard, Valve) and then *exploited* by downstream commercial products (DotA→Dota2, Auto Chess→TFT). Within that honest baseline, the AtoA→MtM two-product pivot has one structural advantage: it explicitly *names* the upstream/downstream pattern that has historically worked (Finding 10) — the free SKU plays the role of WC3, the paid MtM plays the role of Dota 2 / TFT. A paid-EA single-product attempt is forced to fund the substrate from its own revenue, which the Stormgate, Caves of Qud, and Stardew evidence suggests will result in either deep cuts or multi-year deferrals. **The pivot's funding mechanism is therefore not "the free product pays for the substrate" — it's "the free product validates the substrate cheaply enough that the paid successor can afford to finish it."** Caveats: (1) this assumes the free product can get away with a *thin* substrate (terrain editor + workshop + replay only, deferring data/scripting) — if Promise 2 demands the deep WC3-grade substrate at the free tier, no funding mechanism in the evidence base supports that; (2) the engine-lock decision (Phase 4) materially changes the calculus — leveraging Unreal/Godot as a substrate subsidy could halve the cost and make either shape viable; (3) the Stormgate F2P-launch failure is a live warning that "free shape" alone, without conversion economics, doesn't fund anything.
