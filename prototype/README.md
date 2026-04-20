# Prototype — Design Validation Slice (v1)

A single-file, zero-dependency, browser-based clickable prototype of *Ash to Altar*. **Throwaway.** Not the game engine.

> See [`decisions/2026-04-19-design-prototype-scope.md`](../decisions/2026-04-19-design-prototype-scope.md) for the scope rules. Port **findings**, not code.

## What this is

A playable slice that exercises the concept end-to-end so the PM can *feel* the design rather than only read about it. One commander, one tutorial, one match, one end screen. Five minutes cover-to-cover.

## What this is NOT

- Not the game engine (Godot 4 is leaning, but unlocked until Phase 4 exits).
- Not production code. Balance numbers, art, copy are all placeholder.
- Not canonical. If this prototype disagrees with `CONCEPT.md`, `CONCEPT.md` wins.
- Not to be ported line-for-line. When Phase 5 begins, this folder archives.

## How to run it

Two modes:

- **Data-driven (recommended):** double-click [`start.bat`](start.bat). It serves this folder over `http://localhost:8765/` via Python's built-in server and opens the prototype in your default browser. Needed to load `data/*.json` at runtime. Close the console window to stop the server.
- **Fallback (no server):** double-click [`index.html`](index.html) directly. Browsers block `fetch` on `file://` (CORS), so the prototype silently falls back to the inline defaults baked into `index.html`. Plays identically, but `data/*.json` becomes documentation-only until you use `start.bat`.

Check the browser console: `[atoA] data loaded from prototype/data/*.json` means data-driven mode is live; `[atoA] data load failed ...` means fallback mode.

Requires Python 3 on your PATH for `start.bat` (tested on 3.14). If `py --version` fails, use the fallback mode.

## The slice (concept-demo build after 2026-04-20 pivot)

| Scene | What happens |
|-------|--------------|
| **Splash** | "◆ ASH TO ALTAR" fade (3s, skippable). Respects reduce-motion setting. |
| **Login** | Enter a Commander name. Stored in `localStorage` (`atoA.profile.v1`). No server. |
| **Main menu** | Continue (if save exists), Play, Commander, Options, Logout. |
| **Mode select** | Solo Skirmish (3 waves), Tutorial, Co-op Horde (11 waves), Solo Campaign (stub). |
| **Commander pick** | 5 playable commanders (A–E), one per lineage. Lineage-colored initial-letter portrait, XP ladder, 3 cosmetic slots. |
| **Tutorial** | 5-step narrator — skippable. Returns to menu when done. |
| **Match** | 5 lineages (Sinew / Ember / Forge / Crown / Veil) + adjacent hybrid. Age progression (11 ages in Campaign/Horde, 3 in Skirmish). Send-Wave button disabled during active wave + "Wave N in progress" indicator. Esc → Pause overlay. |
| **Co-op Horde** | Host / Join via PeerJS (WebRTC DataChannel). Host-authoritative sim, 10Hz snapshots. Shared gold/knowledge. Chat panel. 10s reconnect window. |
| **Options** | 5 tabs — Audio / Input / Video / Accessibility / Gameplay. Saves to profile. |
| **End** | Victory/Defeat stats. XP awarded to active commander. |

## Login / Logout

- First run: splash → Login scene. Enter any name; local profile is created.
- Returning run: username is pre-filled. Press Enter or click **Enter**.
- From the menu, **Logout** clears the profile and returns you to Login.

## Co-op Horde (playing with a friend)

1. Both players open the prototype (either via `start.bat` or a deployed URL).
2. Player A: **Play → Co-op Horde → Host match**. Wait for the invite code.
3. Player A shares either the **invite code** (paste into friend's lobby) or the full **link** (which auto-dials on open).
4. Player B: opens link OR goes to **Co-op Horde → Join** and pastes the code.
5. On handshake, both are thrown into a shared 11-wave match.
6. Host runs the authoritative sim; guest sends input intents (place, send-wave, age-up, chat).
7. Guest-owned towers render with a dashed border.
8. Chat panel on the right; 100-char limit.
9. If either peer disconnects, a 10s reconnect window runs. If it expires, the match aborts.

PeerJS uses the free cloud broker at `peerjs.com`. If it's unreachable, the lobby will show a broker error — try again in ~5 min or stand up a local broker.

### Known limitation — broker SLA

The public `peerjs.com` broker has no SLA. If it's down at playtest time, neither host nor join works and the lobby surfaces a broker error. **This is a prototype-only limitation** — the Godot port will use a self-hosted broker or Steam networking (see `PORT-NOTES.md`). If a playtest is blocked by this, reschedule rather than patching around it.

## What to watch for when playtesting

The prototype exists to surface design questions. As you play, flag:

- **Identity moment.** Does the Commander B splash actually make you feel like "this commander." Or does it feel like a generic card?
- **Tutorial pacing.** Does the 5-step narrator hand-hold too much? Too little? Is the hybrid teaser (step 3) meaningful or glossed?
- **Economy feel.** Gold vs. Knowledge split — does spending knowledge on Age feel like a real tradeoff, or a tax?
- **Age progression.** Does the power jump between Primal → Mudbrick → Iron *feel* like a civilization leap, or a damage-number bump?
- **Hybrid unlock.** Placing Sinew + Ember adjacent to enable Tank Corps — does that moment land, or is it easy to miss?
- **Wave pacing.** Do the 3 waves escalate on a curve you'd want to repeat? Too easy, too hard, or "just one more run"?
- **End screen.** Is the stat summary something you'd want to compare between runs, or forgettable?
- **Upgrade mechanic [PROPOSAL].** Right-click any placed tower → Upgrade (L1→L2→L3). Do in-age upgrades deepen the choice space, or feel redundant with age-up? If redundant, we pull the mechanic. See [decisions/2026-04-20-prototype-interaction-layer.md](../decisions/2026-04-20-prototype-interaction-layer.md).
- **Hover info.** Tower buttons, placed towers, enemies, age-up, and hybrid button all show hover tooltips. Is the info load right, overloaded, or underloaded?
- **Ghost preview.** When a tower is selected and you hover an empty cell, a ghost silhouette + range circle appears (green=afford / red=can't). Does this speed placement or clutter the board?
- **Reference panel.** Press `I` (or click **Info**) for a readonly tier list — current age highlighted. Does it get used, or does hover alone cover it?
- **Right-click discoverability.** Right-click on a placed tower opens a Sell / Upgrade menu. Test with someone who hasn't played Tower Wars — do they find it without prompting? If not, that's a first-run-prompt debt.
- **Silhouette read.** Can you tell a swarmer from a heavy from a ranged enemy at a glance, without reading labels? If not, the archetype silhouette shapes need more differentiation. Covers the stage 01 §silhouette-read-test protocol.
- **Damage-number density.** Do rising hit numbers help you track which towers are carrying the wave, or do they clutter? If the white numbers are overwhelming, we'll threshold them to hits ≥1 base damage.
- **Status feedback.** Do you feel the Veil slow / Ember burn / Forge mark effects changing the fight? Or do they blend into the wave? If blended, lineage mechanical distinctness (§3.3) may need bigger knobs.
- **Threat bar.** Does the red-pulse under an enemy's HP bar (when it's <15% to exit) change your response? If you ignore it, either the pulse needs more punch or a tower-priority UI should replace it.
- **Next-wave telegraph.** Before pressing Send-Wave, does the mini-silhouette strip tell you enough to plan? Too much info, too little, or about right?
- **Combat feed.** Top-right event log (kill/leak/hybrid/upgrade). Is it useful history or noise? Does a leak message make you look down at your lives?

### In-match controls cheat-sheet

| Input | Action |
|-------|--------|
| `1`–`5` | Select Sinew / Ember / Forge / Crown / Veil |
| `6` | Select Hybrid (if adjacency satisfied) |
| `Space` | Begin next wave |
| `A` | Age-up (if 50 knowledge) |
| `I` | Open / close tier-reference panel |
| `U` | Upgrade hovered tower (while hovering it) |
| `X` | Sell hovered tower (while hovering it) |
| `Right-click` (on tower) | Open Sell / Upgrade menu |
| `Esc` | Pause (or close reference / context menu) |

Log findings in `decisions/YYYY-MM-DD-<slug>.md` — one per meaningful finding. They inform Phase B research and Phase C stage content.

## Tech notes

- `index.html` is self-contained. No external JS/CSS files. ~1100 lines.
- Canvas 2D for the game board; DOM for HUD, menus, splash.
- Cinzel (Google Fonts) for display type; system sans for UI.
- State is an object on `window`; there's no state persistence across reloads (intentional — every run is fresh).

## Related docs

- [CASCADE.md](../CASCADE.md) — navigation spine.
- [CONCEPT.md](../CONCEPT.md) — vision anchor.
- [admin/](../admin/) — the PM concept-map editor (sibling tool, different purpose).
- [decisions/2026-04-19-design-prototype-scope.md](../decisions/2026-04-19-design-prototype-scope.md) — scope decision.

## Changelog

- **v4 (2026-04-20)** — Meta-UI concept-fidelity + TW/HoMM/AoE/SC-WC3 DNA-injection pass (9 strands, 7 new decisions). **Shell:** splash glyph build-in; login first-time/returning branch; menu branching w/ last-played hint; Profile scene w/ XP + settings + Logout; mode-aware pause (Campaign hard+save / Skirmish hard / Horde host-vote 10s / LaneWars read-only). **Options 5 tabs real:** 5-bus audio + ducking + light WebAudio preview on Master/UI; input rebind capture; UI-scale/subtitle-scale/fullscreen; reduce-flash/reduce-effects/subtitle density; threat-bar/damage-numbers/feed/ghost/hybrid-hint/auto-age-up — all persisted to `profile.settings`. **Commander-pick:** 5 SVG lineage silhouettes; 20-level XP ladder w/ L5/L10/L15 cosmetic lock chips; `?silhouette-test=1` or `Shift+S` grayscale audit. **First-run prompts:** right-click / I-key / hover with permanent dismiss. **DNA:** age-gate cinematic banner from `ages.json` (reduce-motion 400ms) + Campaign autosave per SAVE-01; `data/mapmods.json` (6 biomes [PROPOSAL]); `data/events.json` (8 events [PROPOSAL] — LCG seeded by matchStartMs for co-op determinism, 25% probability, weighted pool, boons + mild downsides); **on-field Commander Avatar** — 1.4× SVG silhouette + 2-cell dashed aura + lineage-flavored passive for towers in aura + **Shift+click** or `C`-toggle move (1/wave cap) + **Q** signature (60s CD / 8s +20% dmg −15% cd aura-wide) + non-destructible knock-back. Co-op snapshot + messages all additive. Click-budget audit: **4 first-time / 2 returning** (targets ≤6/≤3 met); see [`CLICK-BUDGET.md`](CLICK-BUDGET.md).
- **v3 (2026-04-20)** — Visuals overhaul + insight layer ([decisions/2026-04-20-visuals-insight-pass.md](../decisions/2026-04-20-visuals-insight-pass.md)). Enemies now render as archetype silhouettes (swarmer/infantry/heavy/ranged/elite/boss) instead of flat circles, using the `kind`/`color`/`accent` fields already present in `enemies.json`. Towers render as hex + unicode glyph + level-crown chevrons; per-lineage projectile shapes (Sinew dart / Ember spark+trail / Forge hex-bolt / Crown chevron-pair / Veil wavy-bezier / Hybrid split). Insight HUD added: muzzle flash on shots, floating damage numbers (white/gold/grey), status-icon stack above HP bar (slow/burn/marked; Veil towers slow ×0.7 for 60 ticks, Ember towers burn -0.2/tick for 45 ticks, Forge towers mark for 90 ticks), threat bar below HP pulses red <15% to exit, next-wave telegraph strip above Send-Wave, combat feed top-right logs kill/leak/hybrid/upgrade/wave events with 4s fade (reduce-motion aware). Co-op snapshot schema extended additively — no breakage.
- **v2 (2026-04-20)** — Concept-demo pivot ([decisions/2026-04-20-prototype-concept-demo-pivot.md](../decisions/2026-04-20-prototype-concept-demo-pivot.md)). Added: Splash / Login / Menu / Mode Select / Options (5 tabs) / Pause overlay / Commander-pick identity floor (XP ladder + cosmetic slots) / 5 lineages × 11 ages / 5 adjacent hybrids / 11 per-age enemies / Send-Wave input guard / keyboard shortcuts / subtitle captions. Co-op Horde via PeerJS (host-authoritative, 10Hz snapshots, chat, 10s reconnect, URL auto-join). Profile persists in `localStorage`.
- **v1 (2026-04-19)** — Initial throwaway prototype. Commander B slice. Title → pick → tutorial → Lane Wars (3 waves) → end. Placeholder numbers, placeholder copy, silhouette aesthetic.
