# Production Repository Verification

## Purpose

This document converts RT Study Lab project-history claims into facts traceable to the production source repository. It records source structure and source-controlled evidence separately from runtime execution, clinical review, accessibility review, deployment health, and mechanical/visual review.

## Baseline source

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility at verification: Private
- Default branch: `main`
- Baseline source ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Commit message: `Redesign Shock visual teaching page`
- Evidence state: **Verified against production repository**

The source repository is now linked and inspectable. The live ChatGPT Sites deployment relationship is only partially established: source-controlled Sites/Vinext/Cloudflare configuration is present, but this audit did not verify that the live deployment is currently built from the GitHub `main` ref. Do not equate GitHub source state with deployment state without deployment evidence.

## Repository architecture observed

### Runtime and build

- Node engine requirement: `>=22.13.0`
- Next.js `16.2.6`, React/ReactDOM `19.2.6`, TypeScript `5.9.3`
- Vinext `0.0.50` and Vite `8.0.13`
- Cloudflare Vite plugin and Wrangler are present for the Sites runtime
- Three.js `^0.185.1`, React Three Fiber, and Drei are present and are actively used by the chest-trauma 3D module
- Drizzle ORM/tooling is present, but `db/schema.ts` is intentionally empty at this ref and `.openai/hosting.json` has no D1/R2 binding configured
- Static/educational assets are primarily under `public/`

### Package-management state

The repository contains `package-lock.json`, `pnpm-lock.yaml`, and `pnpm-workspace.yaml`. The README and package scripts are npm-oriented. The intended canonical package manager therefore needs a maintainer decision; the coexistence of multiple lockfiles is a repository-hygiene ambiguity rather than evidence of a runtime defect.

### Test execution boundary

The repository contains a broader test inventory than the canonical `npm test` script executes. `npm test` currently builds the app and runs only:

- `tests/rendered-html.test.mjs`
- `tests/pft-loop-data.test.mjs`
- `tests/ventilator-engine.test.mjs`
- `tests/ventilator-session3.test.mjs`
- `tests/ventilator-session35.test.mjs`

Additional source-controlled suites exist for ECG/ACLS, Ventilator Session 3.5.2 regressions, Shock, Stroke, trauma/chest-trauma 3D, and related UX/clinical logic. No `.github/workflows` CI configuration was identified in the baseline tree. This audit inspected tests but did **not** execute them, so test presence must not be presented as a passing result.

## Module verification register

### ECG Rhythm / ACLS Lab

- Production path: `app/acls/ecg-lab/`
- Entry route/component: `app/acls/ecg-lab/page.tsx`, `ECGRhythmLab.tsx`
- Implementation status: **Verified against production repository — implemented**
- Architecture observed:
  - `engine.ts` — deterministic ECG event/waveform engine with internal 500 Hz sample rate
  - `rhythms.ts` — 19 rhythm definitions
  - `caliperSnapping.ts` — event/landmark-aware measurement assistance
  - `practice.ts`, `exam.ts` — rhythm practice and examination logic
  - `patientState.ts`, `clinicalScenarios.ts`, `clinicalTraining.ts` — independent patient/clinical-state layer
  - `pathwayEngine.ts`, `pathwayTraining.ts` — ACLS pathway classification/training layer
  - `treatmentEngine.ts`, `treatmentTraining.ts` — treatment selection, parameter validation, deterministic patient/ECG response, reassessment, timeline, and scoring structures
  - `arrestEngine.ts` and `postArrestEngine.ts` — arrest and post-ROSC learning engines
- Source-backed historical claims confirmed:
  - 500 Hz internal ECG engine
  - 19-rhythm library
  - Learn, Practice, Exam, and Clinical modes
  - caliper/landmark assistance
  - independent clinical patient-state/pathway/treatment architecture
  - AHA 2025 guideline metadata in pathway/treatment source
  - treatment engine version metadata `phase-2b-2-v1`
- Tests present: multiple ECG engine, caliper, practice, exam, clinical-reasoning, pathway, treatment, arrest/post-arrest, and UX test files are source-controlled
- Current test execution: **Not executed during this GitHub-only audit**; ECG suites are not included in the current canonical `npm test` command
- Clinical evidence: source contains guideline identifiers/URLs and explicit educational-adaptation boundaries; this is reference evidence, not independent clinical validation
- Accessibility evidence: source and UX tests contain semantic labels, announcements/focus handling, keyboard/caliper guidance, responsive behavior, and explicit ECG-vs-patient-state safety language; no comprehensive WCAG/manual accessibility audit artifact was identified
- Current known defects confirmed: none from static source inspection
- Remaining verification: execute the full ECG suite at the baseline ref and perform current clinical/accessibility review before calling the module clinically or accessibility validated

### Ventilator Waveform Lab

- Production paths: `app/visual-lab/VentilatorWaveformLab.tsx`, `app/visual-lab/ventilator/`
- Implementation status: **Verified against production repository — implemented**
- Architecture observed includes deterministic engine, breath records, monitor calculations, triggering, neural clock, patient profiles, scenario/configuration state, waveform rendering, clinical revision/provenance helpers, and a stateful bounded-history `LiveVentilatorSession`.
- Tests present: `ventilator-engine`, `ventilator-session3`, `ventilator-session35`, and `ventilator-session352`
- Current test execution: **Not executed during this audit**

#### Historical P1 dispositions from current source

1. **Double-trigger / unintended triple stacking** — **Resolved in current source; runtime re-execution still required.** `ventilator-session352.test.mjs` explicitly requires two-breath stacked clusters and rejects three-breath clusters.
2. **Minute ventilation associated with double triggering** — **Resolved in current source; runtime re-execution still required.** The same regression suite recalculates minute ventilation over the declared completed-breath interval and explicitly guards the historical ultra-short-interval defect.
3. **Dynamic compliance during patient effort** — **Resolved in current source; runtime re-execution still required.** Regression coverage requires a usable passive estimate and contaminated/null output with a reason for effort/leak-related conditions.
4. **Historical VC/PC breath relabeling** — **Resolved in current source; runtime re-execution still required.** `LiveVentilatorSession` stores per-breath configuration provenance and the regression suite verifies immutable VC/PC provenance through mode transitions.
5. **Expiratory-hold scheduling/rescheduling** — **Resolved in current source; runtime re-execution still required.** `LiveVentilatorSession` dynamically targets the next breath and supports arm/repeat/cancel/invalid states; regression coverage exercises holds after arbitrary breath numbers.

Important validation gap: `tests/ventilator-session352.test.mjs`, which contains the dedicated P1 regressions, is **not** included in the current `npm test` script.

Historical multidisciplinary scores remain historical evidence only; current source does not itself prove those review scores remain valid.

### Shock / Oxygen Transport

- Production paths: `app/disease-processes/cardiovascular/shock/`
- Current route: `/disease-processes/cardiovascular/shock`
- Implementation status: **Verified against production repository — Shock learning page implemented; physiology simulation not implemented**
- `ShockInteractiveLabSlot.tsx` explicitly states: `Not implemented · integration boundary only.` It also states that no synthetic patient, pressure trace, cardiac-output model, treatment response, or simulation runs on the page.
- Current hemodynamics are educational/qualitative course trend data and interactive comparison/quiz content, not a coupled circulation engine.
- Hb → CaO2 → DO2 → VO2 → CvO2/SvO2 → extraction → oxygen-debt simulation coupling: **not implemented at this ref**
- Conservation/numerical-stability testing of a Shock circulation engine: **not applicable to the current source because that engine is absent**
- Tests present: `tests/shock-page.test.mjs` verifies route rendering, 34-objective/quiz mapping, qualitative hemodynamic trends, source/educational boundaries, future-lab nonimplementation, responsive behavior, and accessibility-adjacent markup
- Current test execution: **Not executed during this audit**; `shock-page.test.mjs` is not included in the current canonical `npm test`
- Historical claim disposition: the prior concern about reconciling a reduced circulation implementation is **Historical / superseded for this ref**. The current repository does not contain that simulation; the intended broader oxygen-transport lab remains planned work.

### Interactive Respiratory Equipment / 3D

Two distinct production states must be kept separate.

#### Equipment catalog

- Production paths: `app/equipment-lab/`, `public/equipment/`
- Implementation status: **Verified against production repository — implemented as image/HTML-overlay interactive lessons**
- `EquipmentExplorer.tsx` provides zoom/pan/fullscreen, keyboard controls, hotspots, flow diagrams, setup-error reveal, simplified assembly ordering, troubleshooting, and scenario questions.
- `equipment-data.ts` contains device-specific educational content plus creator/source/license/accessed/alterations metadata.
- The cuffed tracheostomy lesson currently uses a static openly sourced photograph and HTML hotspots. It is **not** the external Blender Shiley 3D model.

#### Chest-trauma 3D visual lab

- Production paths: `app/disease-processes/trauma/chest-trauma-3d/`, `public/visual-labs/chest-trauma/`
- Implementation status: **Verified against production repository — integrated 3D module**
- Architecture: React Three Fiber/Drei/Three.js, GLB loading, desktop/mobile respiratory and thorax assets, morph targets, camera controls, runtime anatomical bounds, reduced-motion/visibility safeguards, and 2D-default lazy opt-in boundary
- Tests present: `tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs` include source/model integrity, canonical nodes/morphs, triangle budgets, coordinate registration, runtime landmark checks, opt-in/lazy boundaries, and interaction safeguards
- Provenance: v2 respiratory assets have explicit HuBMAP HRA CC BY 4.0 attribution and derivative-modification documentation; v1 asset manifests/license files are also present
- Current test execution/mechanical visual review: **Not executed during this audit**

#### Shiley-style model status

No Shiley-specific `.glb`, snap-lock interaction implementation, or tracheostomy 3D runtime was identified in the production tree at this ref. The historical Blender/Shiley work is therefore **Confirmed from project history but not production-integrated**. Its geometry/mechanical fidelity remains outside the production-source baseline until the source asset/runtime is deliberately integrated or separately version-controlled.

### PFT Lab

- Production paths: `app/pft-reports/`, `public/pft-images/`
- Implementation status: **Verified against production repository — implemented**
- `PFTReportLab.tsx` provides reconstructed educational reports, hidden diagnosis, metric inspection, keyboard-accessible zoom/navigation, stepwise interpretation, knowledge checks, local review status, and report-specific loop exploration.
- `tests/pft-loop-data.test.mjs` establishes source-controlled contracts for 12 reports/12 loop datasets, internal report arithmetic, ratio/TLC safeguards, bronchodilator-response math, distinct physiologic trace sets, and accessibility descriptions/boundaries.
- Current test execution: not executed during this audit, although `pft-loop-data.test.mjs` is included in the canonical `npm test` command.
- Clinical boundary: author-created reconstructions explicitly state no patient data and require quality review before values; source registry includes ATS/ERS PFT references. This is not a substitute for current human clinical review.

### ABG / Hemodynamics

- Production paths: `app/abg-lab/`, with qualitative Shock hemodynamics under `app/disease-processes/cardiovascular/shock/`
- Implementation status: **Verified against production repository — ABG case lab implemented; no general hemodynamic calculation engine identified**
- ABG lab contains 25 authored cases with fixed gas values, interpretation/compensation/oxygenation/cause/action explanations, filtering, and multiple-choice feedback.
- Some case text includes derived clinical reasoning such as Winter estimate or P/F ratio, but the reviewed `ABGLab.tsx` is a case/answer interface rather than a user-entered calculation engine.
- Dedicated ABG automated test file was not identified in the current `tests/` inventory.
- Current clinical validation: source references exist, but a current module-specific clinical review artifact was not identified.

### Disease-process modules

- Generic disease content: `app/diseases/` with a dynamic `[slug]` route
- Source-verified generic disease records include ARDS, COPD exacerbation, status asthmaticus, pneumonia, acute pulmonary edema, pulmonary embolism, pulmonary fibrosis, cystic fibrosis, neuromuscular respiratory failure, and bronchiectasis.
- Specialized disease-process modules are source-controlled for:
  - cardiovascular: Shock
  - neurologic: Stroke
  - trauma: trauma landing/general, burns, chest trauma, traumatic brain injury
- Chest trauma contains the integrated 3D visual lab described above.
- Source references are present in disease records and the shared source registry.
- Test coverage is uneven: dedicated tests exist for Shock, Stroke, trauma/chest-trauma, while no claim of comprehensive disease-module coverage is made.
- Production-ready vs educational completeness still requires content-by-content clinical review; source presence alone is not a clinical validation status.

### Respiratory Pharmacology

- Production paths: `app/medications/`
- Implementation status: **Verified against production repository — implemented**
- `medication-data.ts` contains structured monographs with mechanism, indications, response, administration/device considerations, ventilator aerosol considerations, adverse effects, precautions/interactions, monitoring, failure cues, education, cases, traps, source IDs, and review date fields.
- Source IDs connect to `app/source-registry.ts`, which includes AARC, ATS/ERS, GOLD, GINA, DailyMed, CFF, SCCM, AHA, CDC, and other references.
- Dedicated medication automated tests were not identified in the current tests inventory.
- Reference presence and a source review date do not constitute independent current clinical validation.

### Oxygen-delivery / equipment content

- Production paths: `app/equipment-lab/`, `public/equipment/`, plus related generic learning/disease content
- Source-verified device lessons include oxygen, aerosol, airway, ventilation/emergency equipment; visible assets include HFNC, non-rebreather mask, small-volume jet nebulizer, MDI/spacer, cuffed tracheostomy tube, suction catheter, BVM, PAP interface, nasal cannula and other equipment images.
- Device lessons retain source/license/alteration metadata.
- Interactive behavior is HTML/image overlay and educational flow/setup/scenario logic, not manufacturer-specific mechanical simulation.
- Dedicated equipment-lab test coverage was not identified in the current tests inventory.

### Other / future interactive simulations

Current source already contains three materially different interactive categories:

1. engine-backed physiologic/clinical simulations — ECG/ACLS and Ventilator
2. interactive reconstructed-data teaching — PFT/ABG/equipment lessons
3. 3D anatomy/pathology visualization — chest-trauma 3D

The planned Shock/Oxygen Transport simulation remains an explicit integration boundary only. No separate general-purpose future simulation framework was identified that should be treated as production-ready.

## Validation inventory

### Automated software evidence

- Source-controlled test files: broad multi-module Node test inventory is present
- Canonical `npm test`: build + five selected test files only
- GitHub Actions/CI: no source-controlled workflow identified
- Tests executed in this audit: **none**
- Lint/build executed in this audit: **none**

### Clinical-content evidence

- Shared source registry and module-specific source metadata exist
- ECG pathway/treatment engines include AHA 2025 source metadata and educational/non-endorsement boundaries
- Disease/pharmacology/PFT/equipment content contains source references and educational boundaries
- No current independent end-to-end clinical validation artifact was established for the baseline ref

### Accessibility evidence

- Source contains ARIA labels/live regions, focus handling, keyboard interaction, semantic structures, responsive styles, reduced-motion handling, and accessibility-adjacent tests in several major modules
- No comprehensive WCAG conformance report, automated accessibility run artifact, or current manual assistive-technology review was identified

### Mechanical / 3D evidence

- Chest-trauma GLB structure/provenance and mechanical/anatomical source contracts are represented in source and tests
- Current visual/mechanical browser validation was not executed during this audit
- Historical external equipment-model fidelity work is not automatically production evidence

## Security and repository hygiene

### Positive controls observed

- `.gitignore` excludes `.env*`, `node_modules`, build/runtime state directories, `.wrangler`, and PEM files
- no environment file is present in the current tracked tree
- `.openai/hosting.json` contains a project ID and null D1/R2 binding values; no credential was observed there
- dependency/build output directories such as `node_modules` are not source-controlled in the GitHub tree
- chest-trauma third-party asset attribution is source-controlled

### Current hygiene gaps

1. **Canonical test command is incomplete relative to the source-controlled test inventory.** High-risk ECG and Ventilator P1 regressions are outside `npm test`.
2. **No source-controlled GitHub CI workflow was identified.** There is no durable GitHub baseline showing build/lint/full-suite status for each change.
3. **Multiple lockfiles/package-manager signals coexist.** `package-lock.json` plus pnpm lock/workspace files should be deliberately reconciled.
4. **Production README is still a generic Vinext starter README.** It does not describe RT Study Lab architecture, verification commands, module map, or GitHub/Sites relationship.
5. **Source-controlled Sites metadata exists.** It appears non-secret at this ref, but deployment ownership/synchronization must remain separately documented.

## Baseline completion status

The **production repository source baseline is complete** for source discovery and module mapping at `a0495e9fa4e5437d8a027312b618b5c1c389ef94`:

- canonical GitHub production repository identified
- exact source ref recorded
- major module paths and implementation states mapped
- historical Ventilator P1 concerns reconciled against current source
- Shock simulation status reconciled
- equipment-vs-chest-trauma-3D integration distinction established
- test inventory and canonical execution gap identified
- clinical/accessibility/mechanical evidence boundaries recorded

The following remain deliberately incomplete:

- runtime execution of the full current test suite
- current build/lint evidence
- live deployment-to-source synchronization proof
- comprehensive clinical validation
- comprehensive accessibility validation
- current browser/mechanical/visual validation of 3D behavior

These remaining items are follow-on validation work, not blockers to calling the **source baseline** established.
