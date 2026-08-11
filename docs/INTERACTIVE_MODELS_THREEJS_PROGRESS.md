# Interactive Models — Three.js Planning Progress

**Workstream state:** PROPOSED / IN PROGRESS — planning only

**Branch:** `agent/threejs-planning-architecture`

**Repository:** `R3C4LL4L1F3/RT-study-lab-project`

**Related queue item:** Issue #9

## Verified baseline

- The project-control repository is the durable home for this planning record.
- The current project-control queue gates Interactive Models production expansion behind clinical/model and architecture approval.
- The existing Oxygen Transport & Regional Perfusion Lab prototype is outside this repository’s production source and is not yet a production implementation claim.
- The current visual direction is an SVG circulation viewport with a deterministic physiology engine and bounded runtime work already present in the prototype.

## Current planning deliverables

- Three.js 2.5D roadmap.
- Renderer and physiology architecture contract.
- Validation and evidence plan.
- ADR-012 documenting the proposed renderer decision.

## Not yet verified

- Approved clinical/model contract for the Oxygen Transport & Regional Perfusion Lab.
- Approved anatomical asset, scale reference, topology, and license.
- Production repository implementation branch.
- WebGL/browser support matrix.
- Independent visual QA.
- Independent clinical-educational review.
- GitHub Actions evidence for any Three.js implementation.

## Next actions

1. Review this planning package through project-control/architecture ownership.
2. Confirm the clinical/model specification and visual teaching limits.
3. Assign an anatomical asset owner and provenance reviewer.
4. Approve the renderer frame contract.
5. Build an isolated Three.js renderer spike without changing production behavior.
6. Record prototype screenshots and parity results.

## Non-goals for this branch

- No production renderer implementation.
- No change to the current production site.
- No new shock categories or treatment content.
- No full 3D migration.
- No claim of clinical validation or release readiness.
