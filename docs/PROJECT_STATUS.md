# Project Status

## Purpose of this status record

This document separates project-control facts from historical implementation claims and from facts that have actually been verified against the production source.

Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Project-control verified status

- This repository is the RT Study Lab project-control/documentation repository.
- `main` is the default branch.
- `setup/project-control-foundation` is the current documentation foundation branch.
- Before this foundation work, the repository contained only a short `README.md`.
- No GitHub issues were present when the current PR audit began.
- PR #1 exists as an open draft from `setup/project-control-foundation` into `main`.
- No CI configuration or validation artifacts have been identified in this project-control repository.
- The production application source repository is not identified in this repository.
- Relevant searches through the current GitHub connection identified this project-control repository but did not identify a separate production RT Study Lab repository.

These are **Project-control verified** statements only. They do not establish current production application behavior.

## Major workstream verification overview

| Workstream | Project-history state | Production verification | Current issue state |
|---|---|---|---|
| ECG Rhythm / ACLS Lab | Historical implementation and test milestones are recorded | Needs verification against production repository | No current production defect status established here |
| Ventilator Waveform Lab | Historical implementation plus four P1 defect reports are recorded | Needs verification against production repository | Historical / possibly superseded until reproduced |
| Shock / Oxygen Transport Lab | Project history identifies an implementation/physiology reconciliation need | Needs verification against production repository | Verification concern; not yet a Current known issue |
| Interactive Respiratory Equipment Lab | Historical 3D/modeling work is recorded | Needs verification against production repository | Verification concerns; not yet Current known issues |
| PFT Lab | Workstream identified | Needs verification against production repository | Unknown |
| Disease-Process Modules | Workstream identified | Needs verification against production repository | Unknown |
| ABG / Hemodynamics | Workstream identified | Needs verification against production repository | Unknown |
| Respiratory Pharmacology | Workstream identified | Needs verification against production repository | Unknown |
| Oxygen-Delivery / Equipment Content | Workstream identified | Needs verification against production repository | Unknown |
| Future Interactive Clinical Simulations | Planned work unless current source proves an existing implementation | Needs verification before any implementation claim | Planned work |

Detailed verification fields and questions are maintained in `PRODUCTION_REPOSITORY_VERIFICATION.md`.

## Current verification tracking

A deliberately small issue set tracks the next high-value verification work:

- #2 — Establish production-repository verification baseline
- #3 — Verify Ventilator Waveform Lab historical P1 correctness concerns
- #4 — Reconcile Shock / Oxygen Transport implementation with intended physiology model
- #5 — Verify Interactive Equipment Lab fidelity and browser readiness

Issues #3–#5 are verification tasks. Their existence does not prove that a historical application defect is currently present.

## Confirmed from project history

The following sections summarize retained history. They are **not** production-verified.

### Ventilator Waveform Lab

Project history records an A/C volume-control and pressure-control waveform lab with continuous waveform history, breath navigation, selected-breath detail, playback/window/history controls, annotations, and responsive learning controls.

A historical validation summary recorded:

- Clinical: 82/100
- Engineering: 76/100
- Educational: 79/100
- Mechanics: 88/100
- Realism: 84/100
- Measurement: 78/100

The historical browser/clinical audit recorded **PARTIAL PASS** and four P1 concerns. Those concerns are preserved in `KNOWN_ISSUES.md` but are not labeled **Current known issue** until reproduced against production source/current behavior.

### ECG Rhythm / ACLS Lab

Project history records a staged ECG/ACLS learning system including:

- ECG waveform generation and measurement tools
- Learn Mode and Practice Mode
- expanded rhythm library
- digital calipers and optional landmark snapping
- patient-state modeling
- Clinical Practice and Examination modes
- guideline/pathway logic
- treatment sequencing, reassessment, and timeline replay

Historical test milestones are preserved in `VALIDATION_REGISTER.md`. They need production-source and durable test-evidence reconciliation before being treated as current results.

### Shock / Oxygen Transport Lab

Project history identifies a need to reconcile the implemented circulation/transport model with the intended broader physiology architecture. Specific verification targets include transport-chain coupling, conservation/numerical stability, and missing or disconnected subsystems. No production implementation details are asserted here.

### Interactive Respiratory Equipment Lab

Project history records interactive 3D respiratory-equipment work including Macintosh laryngoscope and Shiley-style cuffed tracheostomy tube modeling, Blender/Python refinement, and device animation work.

Current production integration, geometry fidelity, mechanical realism, animation correctness, clipping/intersection status, Shiley snap-lock behavior, browser optimization, source location, and deployment state all need verification against production source/assets.

## Current project-control gaps

1. Canonical production application repository/location is not linked or otherwise identified through the current connection.
2. No build, test, or deployment evidence has been imported or linked here.
3. Historical validation claims are not yet backed by reproducible production-linked evidence.
4. Historical application concerns have not yet been reconciled into current defect status.
5. Architecture from production source has not yet been inventoried.
6. Several major workstreams have little or no durable implementation-status history in this repository.

## Next status transition

The highest-value next phase is **Production Repository Verification**. Once the canonical production source becomes accessible, use `PRODUCTION_REPOSITORY_VERIFICATION.md` to establish module paths, source files, observed architecture, tests, current defects, historical claim disposition, clinical/accessibility evidence, and unresolved verification questions.
