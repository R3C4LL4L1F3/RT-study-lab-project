# Interactive Models — Three.js 2.5D Architecture

**Status:** PROPOSED / ARCHITECTURE REVIEW REQUIRED

**Decision scope:** Renderer architecture for the Oxygen Transport & Regional Perfusion Lab.

**Risk:** Tier 3 clinical-educational simulation and visualization.

## Architectural decision

Use a Three.js 2.5D renderer with an orthographic camera as a presentation layer over the existing deterministic physiology engine.

The physiology engine remains authoritative. Three.js consumes resolved state and produces visual output. No clinical equation, tissue solver, debt calculation, pulmonary mixing calculation, valve decision, or branch-flow calculation may be duplicated inside the renderer.

The current SVG viewport may remain as a fallback during migration and for environments where WebGL is unavailable.

## System boundary

```text
Inputs and controls
        |
        v
Deterministic physiology engine
        |
        +--> resolved arterial state
        +--> chamber and valve state
        +--> pulmonary compartment state
        +--> canonical vascular segments
        +--> persistent parcel state
        +--> tissue and debt state
        |
        v
Immutable renderer frame adapter
        |
        +--> Three.js scene
        +--> accessible DOM summary
        +--> route labels and explanations
        +--> validation probes
```

## Renderer frame contract

The adapter should expose a versioned, immutable frame:

```ts
type RendererFrame = {
  schemaVersion: 'oxygen-transport-renderer-v1';
  simulationTime: number;
  cardiac: {
    phase: 'filling' | 'atrial' | 'ejection' | 'relaxation';
    chambers: Record<ChamberId, {
      volumeMl: number;
      pressureMmHg: number;
      fillFraction: number;
      contractility: number;
    }>;
    valves: Record<ValveId, {
      open: boolean;
      upstreamPressureMmHg: number;
      downstreamPressureMmHg: number;
    }>;
    ejectedVolumeMl: number;
  };
  pulmonary: {
    compartments: PulmonaryCompartmentFrame[];
    bilateralPerfusion: { right: number; left: number };
    arterial: { po2: number; saturation: number; content: number };
  };
  segments: CanonicalSegmentFrame[];
  parcels: ParcelFrame[];
  tissues: TissueFrame[];
  cameraAnchors: Record<string, [number, number, number]>;
};
```

The adapter must copy or freeze values at frame creation. Scene objects must not retain mutable solver references.

## Scene graph

```text
Scene
├── anatomyContext
│   ├── bodySilhouette
│   ├── thoraxAndMediastinum
│   └── organMeshes
├── cardiopulmonary
│   ├── heart
│   │   ├── rightAtrium
│   │   ├── rightVentricle
│   │   ├── leftAtrium
│   │   ├── leftVentricle
│   │   └── valves
│   └── lungs
│       ├── rightLung
│       ├── leftLung
│       └── pulmonaryCompartments
├── vascularNetwork
│   ├── pulmonarySegments
│   ├── systemicSegments
│   ├── portalSegments
│   └── capillaryBeds
├── transport
│   ├── bloodParcels
│   └── oxygenParticles
├── routeHighlight
└── interactionTargets
```

## Projection and camera

Use an orthographic camera for the primary 2.5D view. Camera presets must be defined in normalized anatomical coordinates, not hard-coded SVG viewBox crops.

Required presets:

| Preset | Purpose | Required context |
|---|---|---|
| Whole Body | proportion and regional delivery | full body, heart/lungs in correct scale |
| Heart + Lungs | central transport | both lungs, four chambers, pulmonary vessels |
| Heart + Valves | mechanics teaching | chamber volume and valve states |
| Pulmonary Exchange | gas exchange | bilateral compartments and content mixing |
| Selected Organ | tissue delivery | organ bed, incoming/outgoing blood, reserve/debt |

Camera transitions must preserve orientation, avoid clipping, and respect reduced-motion mode.

## Geometry and asset contract

Production assets should be authored in Blender and exported as GLB/glTF. Every mesh must have a stable identifier and provenance entry.

Minimum asset metadata:

```json
{
  "assetId": "oxygen-transport-anatomy",
  "version": "0.1.0",
  "source": "documented source or authored asset",
  "license": "record exact license",
  "scaleBasis": "normalized anatomical coordinate system",
  "meshes": {
    "heart.leftVentricle": "node name",
    "heart.rightVentricle": "node name",
    "lung.right": "node name",
    "vessel.aorta": "node name"
  }
}
```

AI-generated anatomy may be used only for non-authoritative concept exploration. It must not be accepted as the production anatomical source without human anatomical review and documented provenance.

## Canonical segment contract

Every functional vessel or valve visible in the scene must map to one canonical segment ID.

```ts
type CanonicalSegmentFrame = {
  id: string;
  name: string;
  type: 'chamber' | 'valve' | 'arterial' | 'arteriolar' | 'capillary' | 'venous' | 'portal' | 'pulmonary';
  upstreamNode: string;
  downstreamNode: string;
  geometryReference: string;
  flowLMin: number;
  resistance: number;
  transitTimeS: number;
  visible: boolean;
  emphasis: number;
};
```

The solver, route builder, vessel geometry, pulse propagation, parcel traversal, route-progress text, validation probes, and accessibility labels must all consume these IDs.

## Heart rendering contract

The visual heart must be driven by resolved state:

- chamber fill level follows chamber volume;
- chamber wall deformation follows the declared visual mapping of pressure/activation;
- valve leaflets follow individual valve state;
- ejection animation is funded by resolved ejected volume;
- right and left ventricular timing remains paired;
- no visual-only contraction may alter physiology.

Mesh deformation may use authored shape keys/morph targets or bounded procedural transforms, but the mapping must be deterministic and documented.

## Pulmonary rendering contract

Each pulmonary compartment must expose visible but restrained evidence of:

- perfusion fraction;
- ventilation fraction;
- V/Q ratio;
- end-capillary oxygen content;
- bilateral assignment;
- true-shunt mixing.

The renderer must not average saturation or PO2 for display when the resolved state is content-weighted. Labels should explain that arterial PO2 and saturation are obtained after content mixing and inversion.

## Parcel and particle rendering

Use bounded instanced objects for repeated parcel and oxygen marks. Physical parcel state and visual particle occupancy remain separate.

Required renderer behavior:

- each active parcel has one canonical route;
- current segment and local progress are visible to Follow One Parcel;
- branch selection follows solved outgoing flows;
- oxygen loading/unloading uses resolved content deltas;
- no new parcel or particle allocation occurs per frame;
- all GPU resources are disposed when a scene is replaced.

## Accessibility and fallback

WebGL is a visual enhancement, not the only source of meaning.

Required fallback behavior:

- accessible DOM summary of cardiac phase, valve state, arterial state, selected route, and tissue state;
- keyboard camera controls;
- keyboard organ selection;
- reduced-motion parity;
- static SVG or text fallback when WebGL is unavailable;
- visible labels that do not depend on color alone;
- focus remains outside the canvas unless an explicit interaction target is selected.

## Performance contract

The renderer must keep:

- one animation clock;
- bounded parcel pool;
- bounded oxygen particle pool;
- bounded route-history buffer;
- bounded event log;
- one shared geometry cache;
- no per-frame DOM growth;
- no per-frame geometry reconstruction for unchanged segments.

Resource peaks must be reported during accelerated long-runtime tests.

## Migration rule

The first Three.js implementation must run beside the current SVG renderer behind a local renderer switch or isolated prototype harness. It must not remove the known-good fallback until visual, interaction, accessibility, and runtime gates pass.
