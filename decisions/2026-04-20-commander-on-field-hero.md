# Decision — Commander-as-Hero-Unit-on-Field (SC/WC3/HoMM DNA)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Medium
**Affects:** `prototype/index.html` (`initMatch`, `effectiveTowerStats`, `commanderAuraEffectOn`, `moveCommanderTo`, `fireCommanderSignature`, `startWave` reset, commander draw block, Q/C key handlers, `buildSnapshot`, `applyGuestSnapshot`, guest `commander-move`/`commander-sig` receivers)

---

## Decision

Spawn a single **Commander Avatar** on the board at match start, seeded at the grass cell nearest the home anchor. Render as a 1.4× silhouette primitive (`renderSilhouette(kind, …, 1.4)`) tinted by the commander's lineage color, with a laurel ring + cooldown arc. A 2-cell dashed aura ring surrounds the avatar; towers inside the aura receive a lineage-flavored passive buff (Sinew +15% dmg, Ember −10% cd, Forge +10% dmg, Crown +15% range, Veil +8% dmg). Movement: **Shift+click** (or `C`-toggle then click) relocates the commander onto any empty build cell, capped at one move per wave — the cap is reset by `startWave()`. Signature ability on `Q` (60s CD, 8s duration) stacks a global aura empowerment (+20% dmg, −15% cd) on top of the passive for every tower inside the aura — fires a lineage-flavored VO feed message. The avatar is **non-destructible**; any enemy overlap triggers a knock-back toward home (30px step, prototype cheat for simplicity). Co-op: additive snapshot field `commander: {x, y, lineage, cd, sigActiveTtl, auraCells}` + two additive messages `{type:'commander-move', x, y}` and `{type:'commander-sig'}` broadcast host→guest; guests without the field/receivers degrade gracefully.

## Context

PM explicitly invoked WC3/SC2 commander presence and HoMM hero-as-army-anchor when expanding the Phase 10.1 concept-demo DNA pass beyond the 6 filed rails. Prior state: commander was metadata only — name, lineage tilt, passive string, VO lines — never *read* in-match. [commander-identity-floor.md](2026-04-20-commander-identity-floor.md:18) already shaped the signature schema (`stats.signature`), 20-level XP ladder, and cosmetic-slot scaffolding, so the identity data layer was ready; the gap was on-field embodiment.

## Alternatives considered

- **Option A — Keep commander as global passive (+15% to lineage, match-wide).** Why not: AoE-style global bonuses read nowhere on the board; the "commander" remains an invisible stat chip. Fails the WC3/SC2/HoMM "hero you can see" evocation the PM asked for.
- **Option B — Full RTS hero with HP, auto-attack, death-and-revive, multiple abilities, leveling mid-match.** Why not: explodes scope (~1 strand of 9) and risks turning TW pacing into an RTS micro loop. The "commander dies → game over" pattern also destabilizes co-op (one player's bad click loses both).
- **Option C — On-field avatar with aura-scoped passive, 1 move/wave cap, 1 signature on cooldown, non-destructible with knock-back.** (Chosen.) Reads visibly, gives the player a presence to attend to, stays within prototype budget, and doesn't upend the TW "build-then-wave" rhythm.

## Reason chosen

**Loop 1 — aggressive critique.** Aura-only passives *underpower* the commander if the player builds towers far from home: at wave 6 with a sprawled layout, the aura might cover <40% of towers — worse than a global passive. 1 move/wave is too miserly if the path changes (it doesn't in prototype, but still). Shift+click as the relocate gesture conflicts with nothing now but could collide with future multi-select. Knock-back on overlap hides a real vulnerability window during dense late waves. Signature Q-key clash with browser default? None currently.

**Loop 2 — steelman.** The aura-vs-sprawl risk is the *point*: aura ties commander placement to build planning — that's the WC3/SC2 "where you park the hero" decision surface. The balance watchpoint is explicit: if wave-6 median coverage <40%, auto-widen to 3 cells — a stop-gap documented here, wired in a follow-up if playtest warrants. 1 move/wave is TW-pacing-safe; players can still plan placement *before* wave begins. Shift+click is discoverable via the C-toggle fallback + toast on first click. Knock-back is explicitly "prototype cheat for simplicity" per plan; destructible-commander is a future PvP-only feature flag.

**Loop 3 — synthesis.** Ship as-coded. Add an explicit `C` toggle so keyboard-only players have a non-modifier path. Keep the signature generic (+20% dmg, −15% cd) for all lineages on v1 — per-lineage signatures populate later when playtest surfaces a balance read. Calibrate via the auraCells field (per-commander override lives in the commander object), so a future balance pass can tune without code churn. Coverage stop-gap lives in Follow-ups, not in code yet — document, don't pre-optimize.

## Reversibility note

Medium. Removing the avatar means: remove the draw block, remove `commanderAuraEffectOn` call from `effectiveTowerStats` (one line), remove the Q/C handlers, strip the snapshot commander field (additive — guests tolerate its absence), and null `game.commander` in `initMatch`. ~60 lines to surgically remove. No data-file changes required. `commanders.json.stats.signature` string format is untouched.

## Follow-ups

- Strand 6 (this pass): verification + click-budget audit.
- Post-Step-5: if coverage <40% at wave-6 median, bump default `auraCells` to 3 for that lineage; or expose `commander.auraCells` per-commander in `commanders.json`.
- Populate per-commander signatures: Sinew=Warcry (aura +fire-rate), Ember=Kindling (free tier on next build), Forge=Quartermaster (−20% build cost aura), Crown=Rally (+tier-damage aura), Veil=Phantom (slow all enemies in view). Currently commanders share the generic effect; the string on each `stats.signature` already carries the per-commander fantasy copy.
- Port note: Godot → avatar as `CharacterBody2D` + `Sprite2D` with `Area2D` aura child; `move_commander.rpc(to_host)` host-authoritative; signature as `Timer` with `_on_timeout` → lineage `Modulate` shader. Knock-back = `move_and_collide` with home-direction vector. Non-destructibility = layer mask excluding enemy layer.
