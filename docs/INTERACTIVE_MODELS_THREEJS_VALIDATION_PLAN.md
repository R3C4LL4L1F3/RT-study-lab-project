# Interactive Models — Three.js 2.5D Validation Plan

**Status:** PROPOSED / VALIDATION DESIGN

**Risk:** Tier 3 clinical-educational simulation and visualization

This plan separates clinical correctness, software correctness, visual behavior, accessibility, performance, asset provenance, and deployment evidence. Passing one category does not establish the others.

## Evidence levels

### Level A — External fixed reference

Immutable expected values from published equations, independently hand-calculated cases, or approved external datasets.

### Level B — Independent implementation

Expected values calculated by a separate implementation that does not call the production solver or share mutable state.

### Level C — Internal invariant

Conservation, bounds, determinism, topology, synchronization, and resource-limit checks.

### Level D — Behavioral and visual test

Actual controls, camera presets, route following, labels, reduced motion, WebGL fallback, screenshots, and manual review.

## Required validation groups

### Physiology and model synchronization

- resolved arterial state is unchanged by renderer choice;
- chamber volume is conserved;
- ejected volume is funded by the left-ventricular state;
- valve visuals agree with pressure-derived valve states;
- pulmonary compartment content mixing is conserved;
- regional flow and oxygen delivery remain identical between SVG and Three.js renderers;
- debt repayment and reserve trajectories remain identical between renderers;
- presentation-only camera changes do not change physiology.

### Canonical topology

- every visible functional vessel maps to a segment ID;
- every parcel route uses existing segment IDs;
- adjacent route segments share nodes;
- no route skips valves, pulmonary compartments, or terminal capillaries;
- portal routes include portal vein and hepatic sinusoid;
- route highlight and accessible route text agree with actual parcel segment.

### Camera and anatomy

- Whole Body view preserves relative heart/lung/body scale;
- Heart + Lungs view shows both lungs and central vessels without clipping;
- Heart + Valves view keeps all four chambers and valve labels visible;
- Pulmonary Exchange view shows bilateral compartments and the content-mixing sequence;
- Selected Organ view retains orientation and surrounding context;
- camera transitions settle deterministically;
- labels remain readable at supported desktop widths;
- no preset creates an impossible arterial or venous overlap.

### Heart mechanics

- atrial filling increases atrial fill indicators;
- ventricular filling increases ventricular volume;
- AV valves open only in the declared filling window;
- semilunar valves open only in the declared ejection window;
- ventricular volume decreases during ejection;
- ejected volume equals the resolved stroke-volume accounting within tolerance;
- right and left chamber timing remains paired;
- reduced motion produces the same cardiac values without continuous motion.

### Parcel and particle behavior

- parcel count never exceeds the configured ceiling;
- oxygen particle count never exceeds its ceiling;
- no per-frame DOM growth occurs;
- branch frequencies converge on solved flow fractions;
- parcel loading uses assigned right/left pulmonary target;
- parcel unloading uses selected tissue exchange;
- Follow One Parcel highlights the actual route;
- full-motion and reduced-motion parcel physiology match.

### Accessibility and fallback

- keyboard controls operate camera presets, zoom, pan, organ selection, route following, and reduced motion;
- focus does not move unexpectedly after slider changes;
- screen-reader summary reports the current cardiac, pulmonary, parcel, and tissue states;
- visual meanings do not depend on color alone;
- WebGL-disabled fallback remains understandable;
- labels and status announcements are debounced and bounded.

### Performance and runtime

- one animation clock is observable;
- geometry is cached and reused;
- GPU resources are disposed on scene replacement;
- accelerated 60-minute run remains finite;
- active parcels, instanced particles, event history, and DOM node count remain bounded;
- maximum oxygen-conservation, chamber-volume, vascular-node, and route-sync errors are reported.

### Asset and provenance

- every GLB has a source and license record;
- mesh names match the asset manifest;
- segment-to-mesh mapping is complete;
- scale basis is recorded;
- animations are documented and deterministic;
- no unreviewed generated anatomy is treated as authoritative.

## Required test artifacts

```text
validation-records/interactive-models/
  threejs-camera-baselines.md
  threejs-physiology-parity.md
  threejs-topology-results.md
  threejs-accessibility-results.md
  threejs-runtime-results.md
  threejs-asset-provenance.md
  screenshots/
```

## Release gate

Three.js renderer work is not release-ready until:

1. the existing SVG or text fallback remains available;
2. physiology parity passes independently of visual screenshots;
3. visual/manual review passes all camera presets;
4. accessibility and reduced-motion evidence is recorded;
5. long-runtime resource limits are recorded;
6. asset provenance and licensing are complete;
7. QA — Regression & Release reviews the evidence independently;
8. the production PR is linked to the project-control decision and validation records.
