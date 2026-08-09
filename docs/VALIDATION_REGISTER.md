# Validation Register

This register preserves historical validation claims while recording what is now directly observable in production source. **Tests present** and **tests passing** are deliberately different states.

## Baseline verification point

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Source ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Audit type: GitHub production-source inspection
- Tests executed during this audit: **None**
- Build executed during this audit: **None**
- Lint executed during this audit: **None**
- CI evidence: no `.github/workflows` source-controlled workflow identified

## Current automated-test inventory

The production repository contains a broad Node test inventory spanning ECG/ACLS, Ventilator, PFT, Shock, Stroke, trauma/chest-trauma 3D, rendered HTML, and UX/clinical logic.

The canonical package script is narrower:

`npm test` = build +

- `tests/rendered-html.test.mjs`
- `tests/pft-loop-data.test.mjs`
- `tests/ventilator-engine.test.mjs`
- `tests/ventilator-session3.test.mjs`
- `tests/ventilator-session35.test.mjs`

Therefore, the default command does **not** currently provide a complete full-suite baseline. Notably excluded are the ECG/ACLS suites, `tests/ventilator-session352.test.mjs`, `tests/shock-page.test.mjs`, and chest-trauma 3D suites.

## Ventilator Waveform Lab

### Historical multidisciplinary validation summary

These remain historical results; current source does not prove the scores remain valid.

| Dimension | Historical score | Evidence basis |
|---|---:|---|
| Clinical | 82/100 | Confirmed from project history |
| Engineering | 76/100 | Confirmed from project history |
| Educational | 79/100 | Confirmed from project history |
| Mechanics | 88/100 | Confirmed from project history |
| Realism | 84/100 | Confirmed from project history |
| Measurement | 78/100 | Confirmed from project history |

Historical browser/clinical result: **PARTIAL PASS**.

### Current source-controlled regression evidence

`tests/ventilator-session352.test.mjs` directly covers the historical high-risk concerns:

- double-trigger clusters must contain exactly two breaths; unintended triple stacking is rejected
- minute ventilation is derived from completed delivered volumes over its declared interval
- dynamic compliance is validity-aware and contaminated in effort/leak-related scenarios
- historical breaths retain immutable VC/PC provenance across mode transitions
- diagnostic holds can arm after arbitrary breath numbers, repeat, complete, cancel, and invalidate under incompatible effort conditions

`app/visual-lab/ventilator/liveSession.ts` contains corresponding per-breath provenance, configuration transition, bounded history, and dynamic hold-state implementation.

**Current disposition:** source indicates the historical P1 defects are addressed, but the regression file was not executed during this audit and is not in canonical `npm test`. Do not call them freshly “passing” until executed.

## ECG Rhythm / ACLS Lab

### Historical automated-test milestones

These counts remain historical records only.

| Milestone | Historical result | Evidence basis |
|---|---|---|
| Phase 1A | ECG tests 12/12; site tests 97/97 | Confirmed from project history |
| Final Phase 1 audit | ECG tests 33/33; site tests 118/118 | Confirmed from project history |
| Version 27 landmark snapping | ECG tests 40/40; site tests 125/125 | Confirmed from project history |
| Phase 2A-1 patient-state engine | Patient-state tests 8/8 | Confirmed from project history |
| Phase 2A-2 clinical practice/exam | Patient-state tests 19/19; ECG tests 59/59; complete suite 144 | Confirmed from project history |
| Phase 2B-2 treatment engine | Treatment tests 18/18; complete suite 175/175 | Confirmed from project history |

### Current source evidence

Current source verifies:

- 500 Hz internal ECG engine
- 19 rhythm definitions
- Learn, Practice, Exam, Clinical modes
- caliper snapping/measurement assistance
- independent patient state, clinical scenarios, pathway, treatment, arrest and post-arrest modules
- pathway/treatment AHA 2025 guideline metadata and educational/non-endorsement boundaries
- source-controlled ECG test files covering engine, calipers, practice/exam, clinical reasoning/UX, pathways, treatment, arrest and post-arrest behavior

Current ECG tests were **not executed** in this audit and are not part of the canonical `npm test` command.

## Shock / Oxygen Transport

Source verification establishes that the current Shock page is a learning module with qualitative hemodynamic teaching and an explicit future-lab boundary. The oxygen-transport simulation is not implemented.

`tests/shock-page.test.mjs` exists and covers route rendering, 34-objective/quiz mapping, qualitative hemodynamic trends, source/educational boundaries, future-lab nonimplementation, responsive behavior, and accessibility-adjacent markup.

Current execution: **not run**; this file is not included in canonical `npm test`.

No circulation-engine numerical/conservation validation is applicable at this ref because the simulation engine is absent.

## PFT

`tests/pft-loop-data.test.mjs` is source-controlled and included in canonical `npm test`. It defines contracts for:

- 12 reports and 12 report-specific loop datasets
- dataset validation and accessible descriptions/boundaries
- FEV1/FVC, RV/TLC, and VA×KCO internal arithmetic consistency
- obstruction/restriction safeguards using ratio/TLC
- bronchodilator-response calculation and distinct pre/post traces
- distinct restrictive/obstructive/quality teaching traces

Current execution: **not run during this audit**.

## Chest-trauma 3D

Source-controlled validation includes `tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs`.

Observed test contracts include:

- 2D-default and lazy/opt-in Three.js boundary
- canonical respiratory/thorax nodes and required morph targets
- desktop/mobile asset pairing and triangle budgets
- source-frame/anatomical registration
- geometry-derived runtime landmarks/camera fitting
- respiratory/thorax asset rollback pairing
- interaction/animation/reduced-motion/visibility safeguards
- model license/provenance expectations

Current execution: **not run during this audit** and not included in canonical `npm test`.

## ABG, medications, equipment catalog, and broader disease content

- ABG: 25 authored cases are present; no dedicated ABG automated test file was identified.
- Medications: structured monographs and source IDs are present; no dedicated medication automated test file was identified.
- Equipment catalog: structured lessons, safety content and source/license metadata are present; no dedicated equipment-lab automated test file was identified.
- Disease content: dedicated tests exist for selected specialized modules such as Shock, Stroke and trauma/chest-trauma, but comprehensive coverage of all generic disease records is not established.

## Clinical-validation inventory

Production source contains substantial reference evidence:

- shared `app/source-registry.ts`
- module-specific guideline/source URLs and identifiers
- AHA 2025 pathway/treatment metadata in ECG/ACLS
- ATS/ERS PFT references
- AARC, ATS, GOLD, GINA, DailyMed, CFF, SCCM, AHA, CDC and other records used by content modules
- educational boundaries such as “not clinical decision support,” source-limited/course-limited content, and non-endorsement statements

This is **not equivalent to independent clinical validation**. No current end-to-end human clinical-review artifact tied to `a0495e9...` was established in this audit.

## Accessibility-validation inventory

Source evidence includes:

- ARIA labels/live regions
- focus management and announcements
- keyboard-accessible ECG/PFT/equipment controls
- responsive CSS tests
- reduced-motion handling in Shock/chest-trauma 3D
- safety language separating ECG morphology from pulse/perfusion assessment

No comprehensive current WCAG conformance artifact, automated accessibility scan result, or documented manual assistive-technology review was established.

## Required next validation baseline

Before future implementation work is treated as safely regression-controlled:

1. select/document the canonical package manager
2. define a full canonical test command that intentionally includes the current source-controlled suites
3. run build, lint and full tests at a recorded source ref
4. add durable GitHub CI after local command semantics are proven
5. retain results separately from clinical, accessibility, visual and mechanical review
6. re-run the Ventilator P1 regressions and use executable evidence to finalize their resolved status

Automated passing results must never be substituted for clinical validation.
