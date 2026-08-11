# ADR-012 — Three.js 2.5D Circulation Renderer

**Status:** Proposed

**Date:** 2026-08-11

**Decision owner:** Interactive Models & Simulation Lab — Shock / Circulation

**Reviewers required:** Planning / Architecture; Clinical Validation & Sources; Design System & UI/UX; QA — Regression & Release; 3D Modeling Chat

## Context

The Oxygen Transport & Regional Perfusion Lab currently uses an SVG-based circulation viewport. It contains useful physiology, bounded parcel pools, persistent parcel state, pulmonary source-of-truth behavior, cardiac mechanics, canonical routing work, tissue oxygen accounting, curves, accessibility output, and validation scenarios.

The current viewport remains visually inadequate for the intended teaching task. The same 2D path layer is responsible for anatomical proportion, vessel branching, chamber mechanics, pulmonary exchange, route tracing, particle movement, labels, and regional delivery. Zoom is implemented as viewport cropping, which creates clipping and loss of orientation. The renderer therefore needs a different presentation architecture without replacing the validated physiology source of truth.

## Decision

Adopt a Three.js 2.5D renderer using an orthographic camera and a documented GLB/glTF anatomical asset pipeline. Keep the deterministic physiology engine, controls, charts, accessible DOM summaries, and validation modules outside the renderer.

Implement the new renderer initially as an isolated prototype beside the SVG renderer. The fallback may only be removed after independent visual, accessibility, runtime, topology, and physiology-parity evidence passes.

## Alternatives considered

### Continue expanding SVG

Rejected as the primary direction. SVG remains useful as a fallback and for overlays, but it is poorly suited to conveying depth, volumetric chambers, tubular vessels, and instanced transport at the required clarity.

### Full 3D game-engine migration

Rejected for this phase. Unity or Unreal would introduce deployment and integration complexity not justified by the current desktop web lab. Full 3D remains deferred.

### Spline or design-first 3D tooling

Rejected as the simulation renderer. Design-first tools may help with visual prototyping but do not provide the required direct state-driven parcel, valve, pulmonary, and validation integration.

### AI-generated anatomy as production asset

Rejected as an authoritative source. It may support concept exploration, but production anatomy requires named meshes, reviewable topology, provenance, licensing, and stable segment mapping.

## Consequences

### Positive

- Anatomical scale and camera behavior can be separated from viewport cropping.
- Heart chambers, valves, lungs, vessels, and parcels can be rendered as spatial objects.
- Instancing can support bounded repeated blood and oxygen objects.
- Canonical segment IDs can drive geometry, routing, labels, and validation together.
- The existing physiology model can remain independently testable.

### Negative

- A new asset pipeline is required.
- WebGL failure and fallback behavior must be designed and tested.
- Visual QA becomes more important and more expensive.
- Anatomical asset provenance and licensing become release requirements.
- Three.js does not provide clinical truth; it only renders the resolved model state.

## Reversibility

The decision is reversible during the prototype phase because the SVG renderer remains available behind a renderer adapter/fallback. It becomes a production migration only after the release gate in `docs/INTERACTIVE_MODELS_THREEJS_VALIDATION_PLAN.md` passes.

## Resolutions for the M1 renderer-shell gate

The following decisions resolve the technical questions for the isolated M1 prototype without claiming that the production anatomical asset or clinical reference set is approved:

- **M1 anatomy asset:** use clearly labeled procedural placeholder geometry only. Do not treat it as production anatomy. A reviewed Blender-authored GLB remains an M2 dependency.
- **Production asset and license:** defer selection to the 3D Modeling Chat and Clinical Validation & Sources owners. The asset must have documented source, license, scale basis, mesh names, and review evidence before M2.
- **Scale and landmarks:** M1 uses normalized scene coordinates and named camera anchors. M2 must bind those anchors to an approved anatomical reference set.
- **Heart deformation:** prefer authored morph targets for production chamber deformation, with deterministic procedural transforms allowed for the M1 shell. Both must be driven by the same renderer frame contract.
- **Browser target:** M1 must run in the existing supported desktop browser validation environment and record the actual browser/graphics capability observed. The final support matrix remains a release-gate decision.
- **Labels:** essential values and accessibility text remain in the DOM overlay. The Three.js scene may display concise anatomical labels, but no clinical meaning may exist only in WebGL.
- **Manual QA owner:** QA — Regression & Release owns independent visual, interaction, accessibility, and runtime review, with Clinical Validation & Sources reviewing clinical teaching mappings.

The following questions remain evidence-bound and are intentionally not guessed in this planning PR:

- the final production anatomical asset and license;
- the approved proportional reference set;
- the final browser/WebGL support matrix;
- the final clinical-educational disposition of the visual encodings.

## Related records

- `docs/INTERACTIVE_MODELS_THREEJS_ROADMAP.md`
- `docs/INTERACTIVE_MODELS_THREEJS_ARCHITECTURE.md`
- `docs/INTERACTIVE_MODELS_THREEJS_VALIDATION_PLAN.md`
- `docs/ARCHITECTURE_DECISIONS.md` DEC-009 and DEC-010
- `docs/ROADMAP.md` Issue #9
