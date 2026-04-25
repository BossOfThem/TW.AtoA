# UI verification sweep — Phase A (static analysis)

**Date:** 2026-05-05 (filed against branch `session/2026-04-25-q2-world-pitch`)
**Source:** `prototype/index.html` @ `e964cf5` (3,586 lines) + `prototype/data/*.json`
**Method:** read code path end-to-end per scene; Grep-then-targeted-Read; no in-browser verification this phase.
**Status legend:** OK = verified by code path / (Test) = ambiguous, conditional, or runtime-state-dependent / NEEDS-FIX = broken, dead, regressed, or contradicts intended spec.

Phase B (live in-browser via Claude-in-Chrome / preview MCP) will augment (Test) → OK or (Test) → NEEDS-FIX, fix small NEEDS-FIX inline, queue medium/large to AskUserQuestion.

---

## Scene 1 — Splash (`#scene-splash`, lines 415-420)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `◆` diamond + "ASH TO ALTAR" glyph row | `buildSplashGlyphs` ln 960; per-char animation delays unless reduce-motion | OK | Reduce-motion path collapses delays (ln 965, 971). |
| 3s auto-advance | `setTimeout(dismissSplash, 3000)` ln 976; reduce-motion → 300ms | OK | `dismissSplash` early-returns if scene already left. |
| Click-to-dismiss | `#scene-splash` click → `dismissSplash` ln 959 | OK | Post-splash-fix (`90f6f1c` `CODEX_DATA` rename) wiring restored. |
| Any-key-to-dismiss | global `keydown` ln 951 → `dismissSplash` while `currentScene==="splash"` | OK | Includes Escape implicitly. |
| `dismissSplash` route | → `menu` if `Profile.currentUser()`, else `login` | OK | First-run → login; returning → menu. |

## Scene 2 — Login (`#scene-login`, lines 425-439)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `applyLoginCopy` returning-vs-new branch | ln 983 — heading "Welcome back" + name when `Profile.load()` has username, else "Ash to Altar" + "Name your Commander" | OK | `goto("login")` triggers it (ln 920). |
| `#login-username` input | maxlength 24, autocomplete off, autofocused after 30ms | OK | Autofocus via `setTimeout(input.focus, 30)`. |
| `#login-go` Enter button | ln 1025 → `doLogin` ln 1007 → toast + `goto("menu")` | OK | Empty-name path toasts "Enter a name." |
| `#login-clear` Logout/clear | ln 1026 → `doLogout` ln 1016 → `goto("login")` | OK | |
| Enter key in input | ln 1027 → `doLogin` | OK | |
| `Profile.login` write | ln 838; persists `atoA.profile.v1` localStorage | OK | New-user shape includes settings, commanderProgress (5 commanders L1), saves={}, lastMode=null. |
| Existing-profile detect | `applyLoginCopy` reads via `Profile.load()` | OK | |

## Scene 3 — Menu (`#scene-menu`, lines 444-462)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#menu-greeting` reflects username | `refreshMenu` ln 1034 — "Welcome back, {name}." else "Welcome, Commander." | OK | Triggered by `goto("menu")` ln 918. |
| `#menu-user-label` footer | "— signed in as: {name} —" or "— not signed in —" | OK | |
| `#menu-continue` (Continue) | shown only if `isReturning && hasSave`; calls `menuContinue` ln 1062 → `startMode(last)` | (Test) | `Profile.hasSave` returns true for `skirmish` only if a save row exists, but `writeMatchSave` ln 879 *only persists for campaign* (skirmish/horde never autosave per save-model.md). So Continue→skirmish path will start a fresh skirmish, not resume. UX lie risk — confirm in browser whether Continue ever appears for a skirmish-only player. |
| `#menu-new` (New game) | `menuNewGame` → `goto("commander-pick")` | OK | |
| `#menu-play` (Play) | `menuPlay` → `goto("mode-select")` | OK | Visibility flips with `isReturning`. |
| Commander button (inline `onclick`) | `goto('commander-pick')` | OK | |
| Profile button | `goto('profile')` | OK | |
| Options button | `openOptions('menu')` ln 3422 → `goto("options")` | OK | |
| Logout button | `doLogout` → `goto("login")` | OK | |
| `Quit` footer link | `confirmQuit` ln 1121 → `window.close()` after confirm | (Test) | `window.close()` is a no-op for tabs not opened by script in modern browsers. Verify in-browser whether it produces any visible behavior; mark NEEDS-FIX if silently dead. |
| `#menu-last` last-played label | "Last played: {civ or lineage} · {mode}" | OK | **Phase B fix landed:** ln 1049-1056 now resolves via `COMMANDERS.roster[cid].civ` when present (legacy `commander-a..e` map preserved as fallback). Verified live: Leonidas → "Last played: greek · campaign". |

## Scene 4 — Profile (`#scene-profile`, lines 467-484)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#profile-header` username + joined date + last mode | `renderProfileScene` ln 1075 | OK | Triggered via `goto("profile")` ln 919. |
| `#profile-roster` commander rows | sources from `COMMANDERS.roster` filter `playable:true`; civ commanders with civ-derived tilt; legacy fallback retained | OK | **Phase B fix landed (`<commit>`):** ln 1086-1099 now iterates `Object.entries(COMMANDERS.roster).filter([_,c]=>c.playable)` → civ commanders Leonidas/Montezuma II/Ragnar surface with tilt Greek/Aztec/Norse. Active commander marked `last`. Falls back to legacy 5-lineage shape if `COMMANDERS` is absent. Verified live (3 rows render, all L1/20). |
| XP bar fill | `pct = Math.min(100, Math.round(100 * xp / xpToNext))` | OK | |
| Cosmetic-slot count | `unlockedCosmetics + " / 3 cosmetics"` | OK | |
| Settings summary block | renders Master vol / UI scale / Reduce motion / Colorblind / Subtitles / Tutorial-on-new | OK | |
| `Back` button | `goto('menu')` | OK | |
| `Logout` button | `confirmLogout` ln 1022 — confirms then `doLogout` | OK | |
| Profile-clear | conflated with Logout (clears localStorage) | (Test) | HANDOFF mentions "profile-clear option" — only path is via Logout. Confirm PM expectation (separate clear-without-logout?). |

## Scene 5 — Mode-select (`#scene-mode-select`, lines 489-520)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| Solo Skirmish card | `startMode('skirmish')` → `MATCH_WAVES=3` + `goto("match")` | OK | Enter-key alternative wired. |
| Tutorial card | `startMode('tutorial')` → `goto("tutorial")` | OK | |
| Co-op Horde card | `startMode('horde')` → `goto("lobby-coop")` | OK | Tag still says "Phase 10.3 — lobby opens, match not yet wired" (ln 508). |
| Solo Campaign card | `disabled` class, `aria-disabled`, no onclick | OK | Tag "Phase 10.2 — stub". By design. |
| `Back` button | `goto('menu')` | OK | |
| Esc key | global handler ln 956 → `goto("menu")` | OK | |
| Hover state | CSS-driven via `.mode-card:hover` (presumed) | (Test) | Visual confirmation in Phase B. |

## Scene 6 — Lobby-coop (`#scene-lobby-coop`, lines 525-546)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `Host match` button | `coopHost` ln 1295 → `Net.host` ln 1157 (PeerJS) | OK | Code-side; runtime depends on `peerjs.com` broker reachability. |
| `#lobby-host-id` invite-code box | populated in `peer.on("open")` ln 1165 with id + `?join=<id>` link | OK | `user-select: all` for click-to-copy. |
| Join input + button | `coopJoin` ln 1296 reads `#lobby-join-code` → `Net.join` ln 1177 | OK | Empty-code path toasts "Paste an invite code." |
| `?join=<peerID>` URL auto-dial | IIFE ln 3570 — waits past splash/login then `goto("lobby-coop")` + `Net.join` | OK | 600ms initial poll, 400ms re-poll until past gate scenes. |
| `#lobby-status` text | updated through Net lifecycle (broker-contact / waiting / dialing / connected / error) | OK | |
| `Back` button | `goto('mode-select')` | OK | |
| 10s reconnect window on disconnect | per PROGRESS 10.3 — abort-and-return-to-menu | (Test) | Code presence not verified in this pass — Phase B should pull-the-cord. |
| Chat 100-char limit | `sendChat` ln 1368 `.slice(0,100)`; input also `maxlength=100` (ln 648) | OK | Lives in match scene, not lobby — confirmed. |
| `Net.host` PeerJS error handling | ln 1172 — surfaces `err.type` to status text; falls back to "Try again in 5 min or self-host." | OK | |

## Scene 7 — Commander-pick (`#scene-commander-pick`, lines 551-588)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#cmdr-roster` chips row | `renderCommanderRoster` ln 1559; chips from `COMMANDERS.roster` filter `playable:true` | OK | Click chip → `selectCommanderId` ln 1578. |
| `#cmdr-portrait` initial-letter silhouette | `applyCommanderCard` ln 1638 | OK | |
| Stats block (civ / passive / short / signature) | `applyCommanderCard` populates from `c.stats` | OK | |
| XP ladder + L5/L10/L15 ticks | static SVG-style markup; values from `c.progression` | OK | |
| Cosmetic locks | static text per slot; unlocked classes from progression | (Test) | Cosmetic slot DOM ids `cmdr-slot-skin/-frame/-tint` exist; verify whether `applyCommanderCard` actually toggles `unlocked` class — Phase B grep + visual. |
| `Back to menu` | `goto('menu')` | OK | |
| `Take the field` | `selectCommander` ln 1752 → `Profile.data.commanderId = COMMANDERS.active` + `Profile.save()` + `goto("menu")` + toast | OK | Toast: "Commander set. Play → Solo Skirmish to begin." |
| `?silhouette-test=1` | `applySilhouetteTest` ln 1692 → adds `silhouette-test` class | OK | Boots in `Profile.load()` flow ln 3563. |
| Shift+S toggle | global keydown ln 1696 — only commander-pick / profile scenes | OK | |
| Esc → menu | global handler ln 956 — includes `commander-pick` | OK | |
| Caption preview `#cmdr-caption-preview` | populated by `applyCommanderCard` (presumed) | (Test) | Confirm displays current commander VO sample in Phase B. |
| Back-compat `#scene-pick` stub | hidden div ln 591; `goto('pick')` redirected to `commander-pick` ln 909 | OK | Defensive alias. |

## Scene 8 — Tutorial (`#scene-tutorial`, lines 596-619)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| HUD: Gold / Tribute / Divinity / Lives | `updateHUD` ln 1906 with `hudPrefix="t-"` | OK | Tribute mirrors gold (alongside; ln 1911). |
| Step indicator `#t-step` | populated in `setTutorialStep` (downstream) | (Test) | Verify "1 / 5" → "5 / 5" progression in browser. |
| `#t-btn-fusion` ⚡ Fusion | `openFusionMenu` ln 1958 — disabled until `divinity ≥ 2` per `updateHUD` ln 1923 | OK | Tutorial unlikely to grant Divinity — button should remain disabled. |
| `#t-btn-codex` 📖 Codex | `openCodex` ln 2034 → 7×5 RPS matrix from `CODEX_DATA` | OK | Post-splash-fix `CODEX_DATA` rename verified ln 2039-2056. |
| `Skip` button | `skipTutorial` ln 1892 → `game.playing=false` + `goto("menu")` | OK | |
| `#narrator` step body + CTA | populated by `setTutorialStep` | (Test) | Phase B: walk steps 1→5; verify glow affordance + CTA copy. |
| Build-glow affordance | per debt entry (`2026-04-19-tutorial-cell-affordance`) — was flagged "too subtle" | (Test) | Phase B grayscale-screenshot check. |
| Esc in tutorial | global ln 956 — now covers tutorial → `goto("menu")` | OK | **Phase B fix landed:** ln 956 condition extended. Verified live: Esc in tutorial returns to menu. |
| Space / 1-5 keys | match-scene-only handler ln 3546 short-circuits unless `currentScene==="match"` | OK | By design — tutorial drives placement via narrator. |
| Tutorial → match handoff | `tutorialCTA(5)` ln 2310 sets skirmish + `goto("match")` | OK | |

## Scene 9 — Match (`#scene-match`, lines 624-670; modals 673-702)

### HUD row

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#m-cmdr` silhouette + name | `initMatch` ln 1859 sets initial; falls back to last-letter regex | OK | Color via `commanderSilhouetteColor`. |
| `#m-mode-label` | "Skirmish" / "Co-op Horde" / "Campaign" via `initMatch` ln 1856 | OK | |
| Gold / Tribute / Divinity pips / Lives | `updateHUD` ln 1906 prefix `m-`; pips are 6 spans toggled `filled` | OK | Tribute alongside gold (ln 1911). |
| `#m-wave` X / Y | ln 1927 | OK | |
| `#m-btn-fusion` | `openFusionMenu`; disabled while `divinity < 2` | OK | |
| `#m-btn-codex` | `openCodex` | OK | |
| `⏸ Pause` button | `togglePause` ln 2388 | OK | Match-only guard ln 2389 (`game.mode !== "match"` early-return). Tutorial pause not supported by design. |

### Board + overlays

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#board-match` canvas | `bindCanvas` ln 1894 — click / mousemove / mouseleave / contextmenu | OK | Click → `onBoardClick` ln 2116 → `placeTower` ln 2170. |
| Right-click context menu | `onBoardContext` (downstream); `#ctx-menu` div ln 805 | (Test) | Sell / Upgrade entries. Phase B walk. |
| Range ring on placement | per `2026-04-20-prototype-interaction-layer` decision | (Test) | Phase B visual. |
| Merge-preview ghost | regression-watch carried | (Test) | Phase B confirm T1+T1 ghost shows pre-merge preview. |
| `#combat-feed` | `renderCombatFeedDOM` ln 2846; gated on `gp.combatFeed` setting | OK | |
| `#next-wave-strip` | `renderNextWaveTelegraph` ln 2861 | (Test) | Phase B visual. |
| `#net-status` | `updateNetStatus` ln 1289 | OK | Coop-only on. |
| `#event-banner` | `showEventBanner` ln 2377 | OK | Spontaneity events; gated `gp.spontaneity`. |
| `#chat-panel` | toggled `on` only when `isCoop` ln 1849 | OK | Hidden in solo. |
| Chat form submit | `sendChat` ln 1368 | OK | 100-char slice. |

### Cast Bar (`#cast-bar`, lines 653-660)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| Passive button (`#cast-passive`) | `disabled` in HTML; populated by `renderCastBar` ln 2068 | OK | Display-only by spec (passive = always-on aura). |
| Short-CD button | `castAbility('short')` ln 2083 — 8s CD, fires VO + toast + cast-emerge state | OK | Cooldown class `cooling` for 8s; `CAST_DURATIONS.short = 72` frames. |
| Long-CD / Signature button | `castAbility('long')` — 18s CD; uses signature CAST_DURATION 270 only via `tier="signature"` mapping line 2097 | OK | **Phase B fix landed:** dead `CAST_DURATIONS.long = 168` key removed (ln 2082 now `{ short: 72, signature: 270 }`). Code paths read `.short` and `.signature` only. |
| Cast bar visibility | `bar.classList.add("on")` only when active commander has `c.civ && c.stats` ln 2073 | OK | Legacy commanders (commander-a..e) have no civ → bar hidden. |
| Targeting model | "Targeting TBD · §4.1" inline text ln 659 | OK | Per spec (post-2026-04-27 amendment). |

### Action bar (`#action-bar`, lines 661-668)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#civ-tower-btns` build buttons | `renderActionBarBuildSet` ln 1590 — tower buttons populated per active commander civ | OK | |
| Wave-indicator `#wave-indicator` | `updateHUD` ln 1932 — "Ready" / "Wave N in progress" / "All waves complete" | OK | |
| `Info` button | `openReference` ln 3301 → `#reference-panel` modal with civ tower table | OK | |
| `Begin Wave N` (`#btn-wave`) | `startWave` ln 2319; disabled while `waveActive` per `updateHUD` ln 1930 | OK | Label flips per wave count. |
| Hover tooltips | `bindActionBarTooltips` ln 3350 — first-run prompt + range-ring tip | OK | |

### Modals

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| Fusion modal `#fusion-modal` | `openFusionMenu` ln 1958; populated `#fm-grid` | (Test) | Phase B: gain 2 Divinity in skirmish (boss-round wave % 5 === 0 path) and click-through. |
| Fusion close | `closeFusionMenu` ln 1987 + Esc handler ln 3542 | OK | |
| `#fusion-modal aria-hidden` | toggled in open/close (presumed by API contract) | (Test) | Phase B inspect. |
| Codex modal `#codex-modal` | `openCodex` ln 2034 — 7×5 grid + status-proc legend | OK | Post-fix `CODEX_DATA`. Click-outside closes via inline ln 687. |
| Codex Esc close | global keydown ln 3543 | OK | |
| Reference panel `#reference-panel` | `openReference` ln 3301; populated with active civ towers | OK | I-key handler ln 3553. Esc closes via ln 3540. |

### Match keyboard shortcuts (global keydown ln 3537)

| Key | Handler | Status | Note |
|-----|---------|--------|------|
| Space | `startWave` ln 3547 | NEEDS-FIX | **Hardcoded to literal `" "` — does not consult `Profile.setting("input.binds")["send-wave"]`.** Rebind UI in Options is decorative for this and all other match keys. Medium severity — touches input system. |
| 1-9 | `selectTower` via `data-tower` index ln 3548-3552 | NEEDS-FIX | Same hardcoding — Options "Tower slot 1..6" rebinds are dead. Medium. |
| I | `openReference` ln 3553 | NEEDS-FIX | Same hardcoding. Medium. |
| U (with hover) | `upgradeTower(hoverState.tower)` ln 3554 | NEEDS-FIX | Same. Medium. |
| X (with hover) | `sellTower(hoverState.tower)` ln 3555 | NEEDS-FIX | Same. Medium. |
| Q | (no handler) | OK | Inert post-C7.a. Options "Commander Q (signature)" rebind is decorative-only. |
| Esc in match | `togglePause` ln 954 | OK | Match-scene branch fires before mode-specific guard. |
| A (age-up) | **no handler in keydown listener** | NEEDS-FIX | HANDOFF + scene-checklist call out "A (age-up)" as a global match shortcut. Search of ln 3537-3556 shows no key === "a" branch. If age-up is intentionally retired (per Tribute kill-only economy revisit?), the scene-checklist needs amending; if intended, it's regressed. Queue for PM clarification. |

### Co-op specifics

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| Host snapshot 10Hz | `Net` snapshot timer (referenced ln 1147, broadcasts via `buildSnapshot` ln 1303) | OK | 40-shot cap, 32-builder cap. |
| Guest intent send | `Net.sendIntent` queued; `processRemoteIntents` drains host-side ln 2132 | OK | Place + send-wave intents. |
| Guest tower owner=`guest` | dashed-white border via render path | (Test) | Phase B visual. |
| Pause vote | host-authoritative ln 2400-2419 + 10s timeout | OK | |
| `match-end` broadcast | `Net.broadcastMatchEnd` from `endMatch` ln 3380 | OK | Sync end screen. |

## Scene 10 — End-of-match (`#scene-end`, lines 707-715)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| `#end-title` Victory / Defeat | `renderEnd` ln 3401 — toggles `defeat` class | OK | |
| `#end-sub` "The altar stands / fell to ash" | ln 3406 | OK | |
| `#end-stats` rows | waves / kills / gold / towers / lives — five rows | OK | **Phase B fix landed:** "Highest Age" row dropped from `renderEnd` ln 3411 (age system no longer tracked under Tribute/Divinity economy). Verified live: 5 rows render, no `undefined`. |
| `Play again` button | `restart` ln 3416 → `initMatch` + `goto("match")` | OK | |
| `Back to menu` button | `goto('menu')` | OK | |
| XP award | `endMatch` ln 3382: 40 win / 12 loss; auto-level-up toasts; persists to `Profile.data.commanderProgress[cid]` | OK | **Phase C fix landed:** `endMatch` ln 3390-3408 now syncs the in-memory mutation back to `Profile.data.commanderProgress[cid] = { level, xp, xpToNext, unlockedCosmetics }` and calls `Profile.save()`. Verified live: simulated win → `localStorage.atoA.profile.v1.commanderProgress.leonidas.xp = 40`; after reload, Profile scene XP bar reads 40%. |
| VO line on end | `endMatch` ln 3392 — picks from `c.vo.victory/defeat` pool index 0 | (Test) | Always pool[0] — not random. By design? |
| Co-op host broadcast | `Net.broadcastMatchEnd` ln 3380 (host only) | OK | |
| Play again / Back to menu | markup has two; checklist obsolete | OK | **Phase C ratification (2026-05-05):** PM ruled markup canonical. 2-button shape stands (Play again + Back to menu); "Continue" has no semantics until Campaign mode lands (currently stub). HANDOFF/scene-checklist references to a 3rd "Continue" button are obsolete and should be amended at next handoff prep. No prototype code change. |

## Scene 11 — Options (`#scene-options`, lines 720-786)

| Element | Handler / source | Status | Note |
|---------|------------------|--------|------|
| 5 tabs (Audio / Input / Video / Accessibility / Gameplay) | `selectOptsTab` ln 3424 — toggles `.opts-tab.active` + `.opts-panel.active` | OK | |
| `syncOptsUI` on enter | ln 3428 — populates each `[data-opt]` from `Profile.setting`; bind labels via `prettyKey` | OK | |
| Audio sliders (master / music / sfx / ui / voice / duck-thresh / duck-ratio / duck-rel) | range inputs persisted via `saveOptsAndClose` ln 3445 | OK | |
| Audio test-tone buttons | `playTestTone('master' / 'ui')` ln 3489 — 440Hz / 880Hz | OK | Falls back to toast if AudioContext unavailable. |
| Focus-loss selects (solo / pvp) | `audio.focusSolo` / `audio.focusPvp` | OK | Persisted; not consumed in code (informational-only at prototype level). |
| Input rebind buttons (12 rows) | `beginRebind(action, btn)` ln 3464 — captures next keydown, persists `input.binds[action]` | OK (capture) / NEEDS-FIX (consumption) | **Captures and persists rebind input fine, but the in-match keydown handler ln 3537 ignores `input.binds` entirely.** See match-keyboard rows above. Single-source fix. |
| Video → Fullscreen toggle | `toggleFullscreen` ln 3502 | OK | Falls back to toast on failure. |
| UI scale slider 75-150% | `applyUISettings` ln 3520 sets `--ui-scale` | OK | |
| Subtitle scale 75-200% | `--sub-scale` | OK | |
| Subtitle speaker-labels checkbox | `video.subSpeakers` | (Test) | Persisted; consumption in caption render pipeline not verified this pass. |
| Reduce-motion (mirror in Video) | `a11y.reduceMotion` shared with A11y tab | OK | Both inputs share `data-opt` key — last-saved wins. Confirm Phase B that toggling one tab updates the other live (currently does not until reopen). |
| A11y: colorblind / reduce-motion / reduce-flash / reduce-effects / subtitles / sub-density | all persisted via `applyUISettings` body classes | OK | |
| A11y "Open README §Accessibility" link | `target="_blank"` static href | OK | |
| Gameplay toggles (threat-bar / dmg-density / combat-feed / ghost-preview / spontaneity / autowave-cd / tutorial-on-new) | persisted; `applyUISettings` toggles threat-bar + combat-feed visibility ln 3530-3531 | OK | `gp.dmgDensity` / `gp.ghostPreview` / `gp.autowaveCd` consumption in render path — Phase B. |
| `Cancel` (footer) | `closeOptions` ln 3423 | OK | Returns to origin (pause → match, otherwise menu). |
| `Save` (footer) | `saveOptsAndClose` ln 3445 — writes all `[data-opt]` to Profile + `applyUISettings()` + toast + close | OK | |
| Live-preview during drag | global `input` listener ln 3513 — updates `[data-for]` text live | OK | |
| Esc in options | global handler ln 955 → `closeOptions` | OK | |

---

## Cross-cutting checks

| Concern | Status | Note |
|---------|--------|------|
| `Profile.hasSave('skirmish')` vs reality | OK | **Phase B fix landed:** `saveAndExit` ln 2444-2456 now branches three ways — campaign writes + toasts "Saved.", skirmish toasts "Skirmish does not autosave (§4.9).", co-op toasts horde line. Verified live: skirmish path no longer claims "Saved." |
| `data/civilizations.json` shape | (Test) | HANDOFF flag — verify in browser whether it actually contains commanders-shaped data; previously suspected curl-ordering artifact. |
| Console clean | (Test) | Phase B — no SyntaxError / unhandled rejections / fetch 404s (except known favicon). |
| Data fetches `loadData()` | (Test) | All 7 JSON files referenced in HANDOFF; locate `loadData()` and confirm endpoints match. |
| Mode-aware pause overlay | OK | Restart hidden for skirmish (ln 2433); Save-and-Exit hidden for non-campaign (ln 2431). Co-op horde uses host vote with 10s timeout. Lane-Wars uses read-only overlay (note: lane-wars mode never set in code path — dead branch / forward-compat). |
| Spontaneity events | OK | `rollSpontaneityEvent('wave-start')` ln 2337 + LCG seeded RNG ln 2349. Co-op host broadcasts via `event-roll`. |
| Right-click context menu hide | OK | Outside-click handler ln 3295. |
| Click-budget instrumentation | OK | Counts BUTTON clicks outside match/tutorial/options ln 1115. |
| Toast / caption / first-run-toast hosts | OK | All three present (`#toast`, `#caption`, `#first-run-toast`). |

---

## Prioritized fix queue (end of Phase A)

### NEEDS-FIX — small — ALL LANDED PHASE B (2026-05-05)

1. ~~**end scene "Highest Age" row shows `undefined`**~~ — **FIXED**: row dropped from `renderEnd` ln 3411. Verified live (5 rows, no `undefined`).
2. ~~**Tutorial Esc dead**~~ — **FIXED**: ln 956 condition extended to include `tutorial`. Verified live (Esc → menu).
3. ~~**`saveAndExit` toasts "Saved." for skirmish**~~ — **FIXED**: 3-branch `saveAndExit` ln 2444-2456 (campaign saves; skirmish + co-op explicitly do-not-autosave). Verified live.
4. ~~**`menu-last` lineage map stale**~~ — **FIXED**: ln 1049-1056 resolves civ via `COMMANDERS.roster[cid].civ`, legacy map preserved as fallback. Verified live (Leonidas → "greek").
5. ~~**`CAST_DURATIONS.long` dead**~~ — **FIXED**: dead key removed ln 2082. No regressions (consumers read `.short` / `.signature` only).

### NEEDS-FIX — medium (queue to AskUserQuestion)

6. **Input rebind UI is decorative** — match keydown handler (ln 3537) hardcodes Space / 1-9 / I / U / X. Rebind UI captures + persists `input.binds` correctly, but no consumer. Touches input system; PM call: replace hardcoded keys with `binds[action]` lookup, or label rebind UI as "preview only" until input system lands properly. [scene-9 + scene-11] — **PENDING**
7. ~~**Profile scene roster hardcodes legacy commanders**~~ — **FIXED Phase B** (PM Recommended pick): `renderProfileScene` ln 1086-1099 now sources from `COMMANDERS.roster` filter `playable:true`; civ commanders surface with civ-derived tilt; legacy 5-lineage shape retained as fallback. Verified live.
8. ~~**End-screen XP doesn't persist**~~ — **FIXED Phase C**: `endMatch` ln 3390-3408 now writes `Profile.data.commanderProgress[cid] = { level, xp, xpToNext, unlockedCosmetics }` after the in-memory mutation and calls `Profile.save()`. Verified live (sim-win → localStorage XP=40 → reload → Profile scene reads 40%). [scene-10]

### NEEDS-FIX — large (queue to AskUserQuestion; do NOT fix without ratification)

9. **"A" (age-up) keyboard shortcut absent from match handler** — scene-checklist + HANDOFF list `A` as global; no branch in ln 3537-3556. Likely intent: either Tribute-economy retirement removed age-up (and checklist needs updating), or it regressed during a refactor. PM call before any fix. [scene-9]
10. ~~**End-screen Continue / Replay / Menu mismatch**~~ — **RESOLVED Phase C (2026-05-05)**: PM ratified markup as canonical (2 buttons: Play again + Back to menu). "Continue" has no semantics until Campaign mode lands; obsolete checklist references to be amended at next handoff prep. No prototype code change. [scene-10]

### (Test) carried into Phase B (not yet NEEDS-FIX)

- Mode-card hover state visual.
- Tutorial step copy + glow affordance + grayscale screenshot.
- Build-glow contrast under reduce-motion.
- Cosmetic-slot unlock class toggling on commander-pick.
- Caption preview on commander-pick.
- Right-click context menu sell/upgrade entries.
- Range-ring on placement / merge-preview ghost / next-wave telegraph.
- Reference-panel render in browser.
- `civilizations.json` shape integrity in browser.
- `loadData()` fetch path (404s, ordering, console).
- Reduce-motion / reduce-flash / colorblind / `gp.dmgDensity` / `gp.ghostPreview` consumption in render.
- Subtitle speaker-labels rendering.
- Reduce-motion mirror sync between Video tab and A11y tab.
- Pause overlay button visibility per mode (Save-and-Exit gated to campaign; Restart hidden for skirmish).
- Co-op snapshot apply / guest-tower dashed border / reconnect window.
- Continue button visibility for skirmish-only player (UX-lie risk).
- `window.close()` Quit footer behavior in supported browsers.
- Esc in tutorial (currently dead — see fix #2).
- Fusion menu walk with ≥2 Divinity.

---

## Phase A done — summary for handoff into Phase B

- **11 scenes walked.** All routing OK (`goto` ln 908 covers every scene + commander-pick alias).
- **5 small NEEDS-FIX** identified for inline fix during Phase B (per-3-fix commit batch).
- **3 medium NEEDS-FIX** queued for AskUserQuestion at end of Phase B.
- **2 large NEEDS-FIX** require PM ratification before any fix.
- **~25 (Test) rows** carried into Phase B for live confirmation.
- **No catastrophic findings** — running the prototype in browser is safe; splash-fix from `90f6f1c` holds.
- Regression-watch (Codex post-rename / Cast-bar / merge-preview / Promote-T4 / Aztec glyph / `logBalanceCurve` / `effectiveTowerStats` / snapshot) — code paths intact; visual confirmation deferred to Phase B.

Phase B should start Claude-in-Chrome / preview MCP against `http://localhost:8765/prototype/index.html` (via `prototype/start.bat`).
