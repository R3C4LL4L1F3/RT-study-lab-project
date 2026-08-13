# Phase 2 Subsystem Records

```text
PHASE COVERAGE: 2 OF 3
PROJECT CHAT COVERAGE: PARTIAL
GLOBAL RECONCILIATION: NOT COMPLETE
GLOBAL AUDIT: NOT COMPLETE
CODEX-READY GLOBAL BASELINE: NOT ESTABLISHED
```

These records normalize chronology and current disposition without moving authority between chats. They cover only the six assigned Phase 2 chats.

## SITE CHAT (RT_study)

- Record: `019f720f-15ca-70c2-bd2f-9b72510e2844`; 7 pages / 62 turns.
- Role preserved: site/platform integration, educational page history, deployment context, and source-to-live boundary.
- Historical-to-current sequence: Shock page creation, source-locked teaching redesign, quiz/objective/reveal-case additions, production-source verification, and prior private Sites deployment reports. Chest Trauma 3D progressed through opt-in R3F/Drei/Three.js pilot work, BodyParts3D thorax v1, Respiratory v2 asset integration, orientation correction, and visual-acceptance correction.
- Verified repository result: the Shock route/files/tests and Chest Trauma 3D v1/v2 assets are present in the fetched production `main` tree at `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`.
- Boundary: the chat reports Sites version 66 and other private deployment events, but the active deployed Git SHA is not verified. Issue #8 remains the authority for that blocker.
- Project result: #35 records the Shock historical milestone; #36 records the Chest Trauma 3D historical milestone. ECG teaching-page and Ventilator UI history remain documentation evidence rather than duplicate Project items.

## Ventilator Waveform Chat

- Record: `019f8976-212b-7f93-ba5f-f4530a8c688d`; 1 page / 2 turns.
- Role preserved: Ventilator-specific mechanics, waveform behavior, implementation validation, and defect/retest evidence.
- Historical-to-current sequence: A/C VC and PC, equation-of-motion behavior, timing and I:E, auto-PEEP, leak balance, auto-trigger and ineffective effort, flow-starvation morphology, inspiratory hold/Pplat, and later validation of preset and mode-transition behavior.
- Current assigned-chat result: four P1 concerns remain in the latest report: triple-stacked double-trigger clusters, dynamic compliance displayed during active effort, VC history relabeled after a mode change, and expiratory hold constrained by a hard-coded breath-3 event. Additional P2 partials concern resistance isolation, selected-breath summaries, and setting-transition contamination.
- Reconciliation: existing #3 remains P1 / Tier 3 / IN VALIDATION. Its durable issue body records the historical automated layer as resolved while the latest assigned report identifies current P1/manual concerns. This is recorded as an unresolved evidence conflict requiring independent current source/browser retest; no state downgrade or duplicate defect was created.
- Project result: #37 records the evidenced Session 3.5 source milestone; #3 remains the active validation record.

## ECG & ACLS Lab Subsystems

- Record: `6a786482-1e5c-83ea-a27a-0e122b120fb8`; 1 page / 3 turns.
- Role preserved: Tier 3 subsystem owner for rhythm morphology, measurements/calipers, rhythm library, patient state, ACLS classification/pathways, treatment/scoring, and Learn/Practice/Clinical Practice/Examination modes.
- Chronology available from the assigned record: ownership and boundary definition. The assigned chat does not by itself establish a current clinical-validation result or a new defect.
- Repository reconciliation: the fetched production `main` tree contains the ECG/ACLS implementation and test families referenced by the broader project history. This confirms source presence, not clinical correctness or independent validation.
- Project result: #10 remains the canonical independent clinical-validation framework with ECG/ACLS in the initial sequence. No separate ECG milestone, defect, or validation item was invented from an ownership record alone.

## Interactive Models & Simulation Lab

- Record: `019fe35c-e3d2-73e0-9310-d790e0f50376`; 10 pages / 95 turns.
- Role preserved: reusable physiology/model framework and the oxygen-transport renderer boundary; model-specific clinical behavior remains bounded.
- Historical-to-current sequence: standalone HTML and 2.5D prototypes, renderer-shell planning, Batch 1-6 implementation, canonical anchors, vessel network, bounded oxygen particles, regional perfusion, heart mechanics, camera and visibility fixes, free HuBMAP/CCF anatomy asset integration, provenance diagnostics, reduced-motion and DOM fallback behavior.
- Repository/PR reconciliation: the durable implementation is on production PR #3, which is draft/open, unmerged, has no reviews, and is not in the canonical Project. Its final commits and body preserve the implementation and gate boundary. No oxygen-renderer files are present on verified production `main`.
- QA boundary: an earlier independent browser review found that the anatomy view did not yet meet the educational traceability objective. Later implementation-owner reports describe revisions, but independent QA approval remains absent. The conflict is retained as an evidence/retest dependency, not silently resolved by chat agreement.
- Project result: #9 remains the canonical architecture/model-contract item. PR #3 and its batches are represented under #9 rather than re-added as a competing Project item.

## 3D Modeling Chat

- Record: `019fe258-ff0d-7852-9ee4-01753e743d47`; 2 pages / 12 turns.
- Role preserved: Blender/device-model geometry, mechanics, animation, asset provenance, licensing, GLB/export, and visual/mechanical QA.
- Historical-to-current sequence: BodyParts3D thorax v1, Respiratory v2 package, alignment audit, provenance/licensing records, corrected asset packages, and historical Shiley model/animation work.
- Repository reconciliation: the production tree contains the Chest Trauma 3D v1/v2 asset families, attribution, manifests, and source/tests. The Shiley-style model and workflow remain historical/local evidence and are not claimed as production-integrated.
- QA boundary: independent browser, runtime, mechanical, and visual QA remains under #5. Asset hashes and local package sizes from the chat are retained as provenance evidence, not promoted into a production commit claim.
- Project result: #36 is the historical source-integration milestone; #5 remains the validation item. No item per model version was created.

## 3D Model Implementation Workflow

- Record: `6a5ca154-aacc-83ea-9b5f-82fee60f3bff`; 13 pages / 128 turns.
- Role preserved: historical model-building and rigging workflow, later routed as a persistent Interactive Models workflow owner while device-specific behavior remains with 3D Modeling.
- Historical-to-current sequence: Shiley-style v13.1/v13.2/v13.3 model and rigging iterations, broad-continuous centerline, deterministic naming/cleanup, model-only versus animation-rig separation, exploded-layout/debug-camera conventions, accessory-motion audits, and script-level corrections.
- Validation boundary: Blender-specific runtime execution was not fully available in the collection environment. The workflow does not claim animation-ready status, manufacturing accuracy, or production integration.
- Project result: documentation-only Phase 2 history. The durable Project representation remains #5 for current 3D validation and #9 for the general Interactive Models architecture boundary; no duplicate workflow item was created.
