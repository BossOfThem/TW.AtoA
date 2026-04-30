# R1-C turn-in — Mindustry + Path of Achra + They Are Billions

**Date:** 2026-04-29 | **Bucket:** substrate-modding-and-solo-dev-and-RTS-hybrid triad | **Status:** R1 turn-in

Charter: [`CHARTER.md`](CHARTER.md) §3 (9 axes) × this bucket (3 comparators) = 27-cell matrix. Concept-only; non-instructional; copyright-respectful (short factual quotes only).

---

## §1 — Key data points (per comparator)

**Mindustry** — Steam app 1127400. Solo developer Anuken (Anuke). Price $9.99 base; also free on itch.io. Steam reviews ~25,000+ Overwhelmingly Positive (~96% positive). Open-source codebase. Full Steam Workshop integration for maps + mods; native modding via Java/JSON content. Mode roster: campaign sectors, custom games, PvP teams, co-op survival — all on the same factory-tower-defense substrate. Owners 1M-2M per SteamSpy. `[web-validated]`

**Path of Achra** — Steam app 2128270. Solo developer Ulfsire. Price $9.99 (regularly $4.99 on sale). Steam reviews ~3,000 Overwhelmingly Positive (~98% positive). Roguelike, not TD-adjacent — but the load-bearing data point is depth-per-dollar from a single dev: 1000+ culture × class × religion combinations, 50+ elementally-aligned powers, broken-build sandbox identity. No modding surface; no multiplayer; no observer. Single mode (run-based roguelike), authored very deep. `[web-validated]`

**They Are Billions** — Steam app 644930. Numantian Games (small team, not solo). Price $29.99 base. Steam reviews ~18,700, ~80% positive (Mostly Positive). Survival mode shipped December 2017 EA; "New Empire" campaign (40-50 hour hand-crafted) shipped at 1.0 on June 18, 2019. **Canonical post-EA mode-add cost data point: ~18 months elapsed from EA launch to campaign shipping**, and Numantian publicly extended production time when they expanded campaign scope mid-development. `[web-validated]`

---

## §2 — 9 × 3 axis matrix

| Axis | Mindustry | Path of Achra | They Are Billions |
|---|---|---|---|
| **1. Units** | Small mobile-unit roster (factory-built drones, mech tiers, naval, air); units are produced by factories not directly micro'd in classical RTS sense. `[web-validated]` | No mobile-unit roster — single hero with deep ability stack instead. The "unit" is the player character. `[web-validated]` | Worker + ~7 combat units (Ranger, Soldier, Sniper, Lucifer, Thanatos, Titan, Harpy etc.); roster is small but each unit is highly load-bearing in late-game composition. `[inference-from-reputation]` |
| **2. Structures** | Hundreds of buildable blocks across factory + defense (turrets, conveyors, drills, power, liquid). Tower roster alone is 20+ across vanilla. Identity-density: each block a single mechanical role; combinatorics emerge from layout. `[web-validated]` | No structures — roguelike has no base-building. `[web-validated]` | Tower + city-builder hybrid: walls, ballista, executor, shocking tower, plus full city-economy buildings (sawmill, foundry, market, bank). Tier ladder is shallow per category but broad across categories. `[inference-from-reputation]` |
| **3. Tiers** | Tech-tree gated by sector progression; tier-up via research currency. Tier payoff curves shaped around resource-throughput unlocks rather than pure power scaling. `[web-validated]` | Powers tier via stacking and synergy — no formal "tier" ladder, instead horizontal build-space at fixed power band. `[web-validated]` | Two-tier-ish tower progression (basic → upgraded). Population/tech progression through Town Hall ranks gates building access. Tier-up payoff is breadth-unlock not depth-spike. `[inference-from-reputation]` |
| **4. Progression** | Campaign sector unlocks; research tree per planet; no commander-leveling or persistent meta currency analogous to Fusion/Tribute. `[inference-from-reputation]` | Run-based meta-progression: unlocks for cultures/classes/religions persist; depth lives in the build-permutation space, not in numerical power-creep. `[web-validated]` | Per-mission campaign progression (skill points spent on Empire upgrades) + survival has no meta. Campaign adds RPG-flavored Empire metalayer absent at EA launch. `[web-validated]` |
| **5. Lobby / multiplayer** | Cross-platform PvP + co-op with custom servers + dedicated server hosting; no formal matchmaking; lobby-substrate is community-server based. No observer mode native. `[web-validated]` | None. Strictly single-player. `[web-validated]` | None. Strictly single-player. No multiplayer at any point in lifecycle. `[web-validated]` |
| **6. Monetization** | $9.99 one-time; also fully free on itch.io; no IAP; no BP; no cosmetics monetization. Open-source. As anti-P2W as it gets. `[web-validated]` | $9.99 one-time; no IAP; no DLC ecosystem at last-known. Cosmetic-only stance is moot — there are no cosmetics. `[web-validated]` | $29.99 one-time; no IAP; campaign was free update to existing owners (the canonical "huge content drop = price ceiling" play). `[web-validated]` |
| **7. Replay / observer** | No formal replay system in vanilla; no in-game observer. Community streaming substitutes. `[inference-from-reputation]` | No replay/observer (single-player). `[inference-from-reputation]` | No replay/observer; community uses video capture. Survival run sharing is anecdotal. `[inference-from-reputation]` |
| **8. Modding / custom-game surface** | **Best-in-bucket.** Steam Workshop, native Java/JSON content mods, open-source repo, custom map editor, scripting via Mindustry Logic (in-game programmable processors). The substrate-and-modding case par excellence. `[web-validated]` | None. No editor, no workshop, no mod API. `[web-validated]` | Map editor for survival maps shipped post-launch; no scripting layer; no Workshop on the same scale as Mindustry. `[inference-from-reputation]` |
| **9. Mode-roster breadth × depth** | ~4 mode-types (campaign / custom / PvP / co-op survival) all sharing the same substrate; depth is from substrate richness not mode-authoring. High depth-per-dollar via modding extension. `[web-validated]` | **1 mode-type, very deep.** Roguelike runs only. The exemplar of solo-dev depth-over-breadth: 98% positive, 3000+ reviews, ~$10, one mode authored to extreme depth. `[web-validated]` | 2 mode-types (Survival at EA, Campaign at 1.0). **Adding the second mode took ~18 months of dev time from a small team and required extending the publicly-committed production timeline.** This is the canonical "post-EA mode-add cost" data point referenced in CHARTER §2. `[web-validated]` |

---

## §3 — Load-bearing finding for AtoA differentiation

This bucket teaches three things load-bearing for the differentiation thesis. **First, depth-over-breadth is the proven solo-and-small-team success path:** Path of Achra (98% positive, 3K+ reviews) shipped **one** mode authored to extreme combinatorial depth at $9.99 from a single developer — the exact shape AtoA's post-supersession Tower+PvP-Co-op (or Tower+Custom) cut implicitly commits to, and an existence-proof that two-mode-types-at-depth is a viable storefront posture rather than a deficit. **Second, the post-EA mode-add cost is empirically heavy:** They Are Billions, a non-solo small team with shipping experience, took ~18 months between EA-survival and 1.0-campaign and publicly extended timeline mid-build — direct numerical substantiation of the supersession's "breadth is unreachable" finding and a defensible Steam-page framing for AtoA's roadmap-stretch language on the five non-launch mode-types. **Third, modding surface is a load-bearing axis where AtoA will likely concede ground:** Mindustry's open-source-plus-Workshop-plus-Logic-scripting stack is the bucket's modding ceiling and is structurally out of reach for a solo-or-tiny-team paid-EA shop without explicit engine-time investment; per CHARTER §6 + RT-3, this finding feeds Phase F Steam-page framing as a "we are not trying to win on modding" honest concession rather than triggering substrate redesign. The differentiation play remains depth-per-dollar at the unit/structure/tier substrate (the audited 36/36 cross-coherence stack) plus Fusion-and-attack-type mechanic novelty — not modding breadth, not multi-mode-roster breadth, not RTS-hybrid scope.

---

*End R1-C turn-in. Output: `concept/atoa-vs-mtm/diff-swarm/r1-c-turn-in.md`. Non-instructional; copyright-respectful; no other files touched.*

**Sources:**
- [Mindustry on Steam](https://store.steampowered.com/app/1127400/Mindustry/)
- [Mindustry — Wikipedia](https://en.wikipedia.org/wiki/Mindustry)
- [Mindustry on SteamSpy](https://steamspy.com/app/1127400)
- [Mindustry on Overwhelmingly Positive](https://overwhelmingly-positive.com/game/Mindustry/)
- [Path of Achra on Steam](https://store.steampowered.com/app/2128270/Path_of_Achra/)
- [Path of Achra on SteamSpy](https://steamspy.com/app/2128270)
- [Path of Achra review — pixeldie.com](https://pixeldie.com/2024/06/12/path-of-achra-review-pc/)
- [They Are Billions on Steam](https://store.steampowered.com/app/644930/They_Are_Billions/)
- [They Are Billions — Wikipedia](https://en.wikipedia.org/wiki/They_Are_Billions)
- [They Are Billions leaves Early Access — PCGamesN](https://www.pcgamesn.com/they-are-billions/campaign)
- [They Are Billions campaign length — GamingBolt](https://gamingbolt.com/they-are-billions-campaign-will-be-40-50-hours-long-coming-at-launch)
- [They Are Billions campaign development update — Numantian](http://www.numantiangames.com/2018/09/27/they-are-billions-update-campaign-development-i/)
