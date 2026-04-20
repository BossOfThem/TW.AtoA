# Decision — Options: make all 5 tabs real

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (opts-panel markup 619–670, `syncOptsUI`/`saveOptsAndClose`/`applyUISettings` JS, new `beginRebind`/`playTestTone`/`toggleFullscreen`), `Profile.login` default settings

---

## Decision

Replace placeholder sliders/toggles/remaps with real behavior across all five Options tabs. Audio: 5-bus sliders + ducking threshold/ratio/release + focus-loss select per mode + WebAudio test-tone for Master and UI. Input: 13 action rows with real Rebind-capture (keydown listener that writes `profile.settings.input.binds[action] = e.code`), Escape cancels. Video: fullscreen toggle via browser API, UI scale 75–150%, subtitle scale 75–200% (independent), subtitle-speaker-labels toggle. Accessibility: colorblind/reduce-motion/reduce-flash/reduce-effects/subtitles + density select + README#accessibility anchor. Gameplay: threat-bar, damage-density, combat-feed, ghost-preview, hybrid-adjacency-hint, auto-age-up, spontaneity, auto-send-wave, tutorial-on-new. All writes go through `Profile.updateSetting()` and `applyUISettings()` propagates class toggles for reduce-motion/reduce-flash/reduce-effects/colorblind and CSS variables for UI scale and subtitle scale.

## Context

[audio-architecture.md](2026-04-20-audio-architecture.md) specifies the 5-bus mixer + ducking + focus-loss behavior. [accessibility-floor.md](2026-04-20-accessibility-floor.md) locks WCAG 2.3.1 (reduce-flash) and 2.3.3 (reduce-motion). [meta-ui-envelope.md](2026-04-20-meta-ui-envelope.md) defines Options as the single surface for all persistent tuning. Prior HTML had placeholder `remapStub()` and partial audio/a11y/gameplay rows — this strand instantiates them.

## Alternatives considered

- **Option A — Godot-side AudioServer + InputMap.** Why not: engine code forbidden until Phase 5.
- **Option B — Full WebAudio mixer graph in prototype.** Why not: scope creep; prototype port-findings-not-code. Light Master+UI test-tone covers the UX question.
- **Option C — Declarative `[data-opt]` attributes + Profile-backed persistence + per-action rebind capture.** (Chosen.) Matches existing prototype pattern; adds no deps; maps 1:1 to `InputMap.action_erase_events` + `InputMap.action_add_event` in Godot.

## Reason chosen

**Loop 1 — aggressive critique.** 13 action rebinds let a player lock themselves out (e.g. bind Esc to a conflict). The focus-loss select defaults differ (solo=mute, pvp=keep) but only honor on next focus-change — no live preview. WebAudio test-tone triggers on-click but the user's *system volume* might be 0 and they'll think the slider is broken.

**Loop 2 — steelman.** Lockout risk is mitigated by Escape-cancels-rebind; the binding is local-only so worst case the user logs out and re-enters (clears profile). Focus-loss is a boundary behavior; live preview is unnecessary. Test-tone is 200ms at 30% amplitude — audible on any working system; if it's silent, the *system* is the culprit, which is a legitimate signal.

**Loop 3 — synthesis.** Ship as-coded. Add a note in PORT-NOTES: Godot `InputMap` needs a "restore defaults" helper; prototype defaults are hardcoded in `Profile.login()`. No CONCEPT change needed.

## Reversibility note

Easy. Removing the expanded opts-panel markup + reverting `syncOptsUI`/`saveOptsAndClose`/`applyUISettings` returns to the placeholder state. Profile settings keys are additive; stale keys in old profiles are ignored by `setting()` fallback.

## Follow-ups

- Strand 4: commander-pick silhouette + XP ladder.
- Port note: Godot `ConfigFile` → `InputMap` restoration on load; `AudioServer.set_bus_volume_db(bus_index, linear_to_db(v))` for bus sliders.
