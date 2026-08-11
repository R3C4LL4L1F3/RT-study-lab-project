# Interactive Models — Three.js 2.5D Circulation Roadmap

**Status:** PROPOSED / SPECIFICATION

**Priority:** P1

**Risk:** Tier 3 clinical-educational simulation and visualization

**Owner:** Interactive Models & Simulation Lab — Shock / Circulation

**Planning support:** Planning / Architecture; Clinical Validation & Sources; Design System & UI/UX; QA — Regression & Release; 3D Modeling Chat

**Related project-control item:** Issue #9 — Interactive Models architecture/model contract

**Scope boundary:** This roadmap covers a browser-based Three.js 2.5D renderer for the Oxygen Transport & Regional Perfusion Lab. It does not authorize broad physiology expansion, new shock categories, medications, full 3D, or production integration before the required gates pass.

## Objective

Replace the current SVG circulation viewport with a spatially coherent, anatomically proportioned, desktop-first 2.5D renderer while preserving the existing physiology engine and validation boundaries.

The renderer must make the following relationships visually legible:

- four-chamber cardiac filling, contraction, valve state, and ejection;
- pulmonary loading through bilateral low/normal/high V/Q compartments and shunt mixing;
- oxygenated and deoxygenated blood movement through canonical vascular segments;
- regional delivery and extraction at organ beds;
- Follow One Parcel route tracing;
- zoomed anatomy without clipping or loss of orientation.

## Non-goals

- Full 3D clinical anatomy or surgical visualization.
- New shock categories, medications, interventions, disease modules, or treatment recommendations.
- Replacing the physiology solver with Three.js logic.
- Treating an educational reserve index as a clinical outcome predictor.
- Using AI-generated anatomy as an authoritative clinical source.
- Treating automated tests as independent clinical validation.

## Gate sequence

Work must proceed through these states in order:

1. **PROPOSED** — planning package recorded; no renderer implementation authorized.
2. **ARCHITECTURE REVIEW** — architecture, model contract, asset contract, and accessibility contract reviewed.
3. **CLINICAL SPECIFICATION** — equations, assumptions, visual encodings, and teaching limits source-grounded.
4. **PROTOTYPE** — isolated renderer spike using representative geometry; no production replacement.
5. **IN VALIDATION** — prototype connected to a frozen state adapter and tested against the existing engine.
6. **READY FOR PRODUCTION IMPLEMENTATION** — independent review and QA gates pass.
7. **IMPLEMENTATION** — production branch/PR may replace the circulation viewport.
8. **RELEASE VALIDATION** — visual, interaction, accessibility, runtime, and clinical-educational evidence reviewed separately.

## Milestones

### M0 — Planning and contracts

- Approve the architecture record.
- Define the renderer-to-physiology frame contract.
- Define the anatomy asset naming and provenance contract.
- Define canonical segment-to-geometry mapping.
- Define camera presets and zoom invariants.
- Define visual encodings for oxygen content, flow, perfusion, valves, and tissue state.

**Exit evidence:** approved architecture record, model contract, asset contract, and validation plan.

### M1 — Renderer shell

- Add an isolated Three.js canvas adapter.
- Add an orthographic camera with whole-body, cardiopulmonary, heart, pulmonary, and selected-organ presets.
- Add smooth camera transitions and keyboard-compatible pan/zoom.
- Keep the current SVG renderer available as a fallback.
- Add a canvas failure and reduced-motion fallback path.

**Exit evidence:** no clipping at supported desktop sizes; camera preset screenshots; fallback behavior verified.

### M2 — Anatomical asset integration

- Import named GLB meshes for body, heart, lungs, major vessels, and organ beds.
- Confirm scale and anchor placement against an approved anatomical reference set.
- Separate chambers, valves, lungs, vessels, and organs into addressable nodes.
- Record source, license, version, scale, and modifications.

**Exit evidence:** asset manifest, provenance record, GLB validation, anchor mapping review, visual QA.

### M3 — Canonical vessel rendering

- Render canonical vascular segments as volumetric tubes or equivalent geometry.
- Use segment IDs from the solver and parcel routes.
- Connect flow, resistance, radius, opacity, and pulse emphasis to resolved state.
- Add portal and pulmonary routes without duplicating disconnected route lists.

**Exit evidence:** topology tests, route continuity tests, branch-frequency tests, visual route review.

### M4 — Heart and pulmonary mechanics

- Map chamber volume to visible fill level.
- Map pressure-derived valve state to leaflet state.
- Map ejected volume to aortic and pulmonary outflow.
- Show bilateral pulmonary compartments and content-weighted mixing.
- Preserve one animation clock and reduced-motion parity.

**Exit evidence:** chamber-volume reconciliation, valve-gate tests, pulmonary content conservation, timing review.

### M5 — Parcels and oxygen particles

- Replace independent SVG particles with bounded instanced objects.
- Keep physical parcel state separate from visual encoding.
- Show loading in assigned lung compartments and unloading in terminal beds.
- Preserve Follow One Parcel and Three Routes.

**Exit evidence:** bounded-resource peaks, route synchronization, parcel-lap completion, reduced-motion parity.

### M6 — Teaching and accessibility layer

- Keep charts and key values in accessible DOM/UI surfaces.
- Add concise anatomical labels anchored to scene objects.
- Add selected-organ and causal-change explanations.
- Add screen-reader summary and keyboard-equivalent camera controls.
- Verify visual meaning never depends on color alone.

**Exit evidence:** keyboard-only test, focus stability test, reduced-motion test, accessible state summary, manual desktop review.

### M7 — Independent QA and release decision

- Run production-engine validation.
- Run visual regression screenshots at all camera presets.
- Run accelerated long-runtime validation.
- Run independent clinical-educational review.
- Record limitations and unresolved risks.

**Exit evidence:** QA report, clinical review record, release decision, provenance record, and linked PR evidence.

## Progress record

| Milestone | State | Evidence | Owner | Next action |
|---|---|---|---|---|
| M0 Planning and contracts | IN PROGRESS | This planning package | Planning / Architecture | Review and approve contracts |
| M1 Renderer shell | DEFERRED | None | Interactive Models | Start only after M0 gate |
| M2 Anatomical asset integration | DEFERRED | None | 3D Modeling Chat | Define asset source and provenance |
| M3 Canonical vessel rendering | DEFERRED | None | Interactive Models | Implement after renderer shell |
| M4 Heart and pulmonary mechanics | DEFERRED | None | Interactive Models + Clinical Validation | Validate visual-to-state mapping |
| M5 Parcels and oxygen particles | DEFERRED | None | Interactive Models | Reuse bounded parcel contract |
| M6 Teaching and accessibility | DEFERRED | None | Design System + QA | Review after scene stabilizes |
| M7 Independent QA and release | DEFERRED | None | QA — Regression & Release | Requires completed M1–M6 |

## Completion definition

This roadmap is complete only when the renderer, physiology source of truth, canonical segment topology, anatomical asset provenance, accessibility output, and independent validation evidence are all linked to a reviewed production PR. A working prototype alone is not release evidence.
