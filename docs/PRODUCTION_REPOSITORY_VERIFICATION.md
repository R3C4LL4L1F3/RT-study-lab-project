# Production Repository Verification

## Purpose

This document converts RT Study Lab project-history claims into facts traceable to production source and executable evidence. Source inspection, automated execution, clinical review, accessibility review, deployment verification, and manual mechanical/visual review are intentionally distinct evidence categories.

## Canonical production source

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility: Private
- Default branch: `main`
- Baseline `main` ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Baseline commit: `Redesign Shock visual teaching page`
- Source evidence state: **Verified against production repository**

The live ChatGPT Sites deployment relationship is not yet fully verified. Source-controlled Sites/Vinext/Cloudflare configuration exists, but no durable record currently proves which GitHub commit produced the live site. Do not equate GitHub source state with live deployment state without deployment evidence.

## Issue #6 executable validation ref

Complete repository validation was implemented on a production review branch rather than directly on `main`:

- Branch: `validation/issue-6-test-baseline`
- Production draft PR: `R3C4LL4L1F3/RT-study-lab#1`
- Validated PR head: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- GitHub Actions run: `31309995943`
- Job conclusion: **SUCCESS**
- Node: `22.13.0`
- Validation package manager: **npm**

Successful automated checks at that ref:

- `npm ci` — PASS
- `npm run lint` — PASS
- `npm run build` — PASS
- complete recursive 28-file `tests/**/*.test.mjs` inventory — PASS
- dedicated `tests/ventilator-session352.test.mjs` historical-P1 regression — PASS
- validation diagnostic artifact upload — PASS

This is executable automated evidence for the draft PR ref. It is **not yet evidence that production `main` contains the new validation workflow**, because the PR is intentionally unmerged pending explicit maintainer authorization.

### Test-harness architecture established by Issue #6

Several existing `.test.mjs` files import application `.ts` modules directly. At the declared minimum Node version, raw Node 22.13.0 test execution fails those imports with `ERR_UNKNOWN_FILE_EXTENSION`. The complete test runner therefore executes each test file sequentially with:

`node --experimental-strip-types --test <file>`

This is validation-harness configuration only; it does not modify production application code.

The runner recursively discovers every `*.test.mjs` file under `tests/`, so later conforming test files cannot silently fall outside the canonical command as they did under the previous fixed five-file script.

## Repository architecture observed

### Runtime/build

- Node engine: `>=22.13.0`
- Next.js `16.2.6`
- React/ReactDOM `19.2.6`
- TypeScript `5.9.3`
- Vinext `0.0.50`
- Vite `8.0.13`
- Cloudflare Vite plugin and Wrangler present
- Three.js, React Three Fiber and Drei actively used by chest-trauma 3D
- Drizzle ORM/tooling present; baseline schema intentionally empty
- static/educational assets primarily under `public/`

### Package-management disposition

Production contains `package-lock.json`, `pnpm-lock.yaml`, and `pnpm-workspace.yaml`.

Issue #6 established **npm as the canonical reproducible validation package manager** because:

- repository scripts are npm-oriented;
- the maintained npm lockfile includes later production dependencies such as chest-trauma 3D runtime packages;
- the pnpm lockfile has not tracked those later dependency changes.

The pnpm artifacts are intentionally retained. Their relationship to the ChatGPT Sites/Vinext environment has not been proven safe to remove or regenerate.

## Module verification register

### ECG Rhythm / ACLS Lab

- Production path: `app/acls/ecg-lab/`
- Route: `/acls/ecg-lab`
- Implementation: **Verified against production repository — implemented**
- Observed architecture:
  - deterministic ECG engine with 500 Hz internal sampling;
  - 19 source-defined rhythms;
  - caliper/landmark snapping assistance;
  - Learn, Practice and Exam logic;
  - independent patient-state/clinical-scenario layer;
  - pathway and treatment engines/training layers;
  - arrest and post-arrest engines.
- Current automated evidence: ECG/ACLS source-controlled test files were included in the Issue #6 complete suite and **passed at PR ref `96b5535...`**.
- Clinical evidence: guideline/source metadata exists, including AHA pathway/treatment references, but passing software tests are not independent current clinical validation.
- Accessibility evidence: keyboard/focus/announcement/semantic structures and accessibility-adjacent tests exist; no comprehensive current WCAG/manual assistive-technology artifact is established.

Historical architecture claims about the separate ECG/patient-state/pathway/treatment layers are substantially confirmed by production source. Historical numeric test-count milestones remain history rather than current suite counts.

### Ventilator Waveform Lab

- Production paths: `app/visual-lab/VentilatorWaveformLab.tsx`, `app/visual-lab/ventilator/`
- Implementation: **Verified against production repository — implemented**
- Observed architecture includes deterministic waveform/breath logic, breath records, monitoring calculations, triggering/neural clock, patient profiles, scenario/configuration state, renderer, provenance helpers and bounded-history `LiveVentilatorSession`.
- Tests: engine, Session 3, Session 3.5 and Session 3.5.2 source-controlled suites.
- Current automated evidence: broader Ventilator tests and dedicated Session 3.5.2 P1 command **passed** at Issue #6 PR ref `96b5535...`.

Historical concern dispositions:

1. double-trigger / unintended triple stacking and associated minute-ventilation behavior — **resolved in current source with passing automated regression evidence**;
2. dynamic compliance during patient effort/contamination — **resolved in current source with passing automated regression evidence**;
3. historical VC/PC relabeling — **resolved in current source with passing automated regression evidence**;
4. expiratory-hold scheduling/rescheduling — **resolved in current source with passing automated regression evidence**.

Issue #3 remains open for browser verification of learner-facing history labels, hold controls, dynamic-compliance validity messaging and double-trigger presentation. Historical multidisciplinary scores remain historical manual evidence rather than current CI results.

### Shock / Oxygen Transport

- Production path: `app/disease-processes/cardiovascular/shock/`
- Route: `/disease-processes/cardiovascular/shock`
- Status: **Shock learning page implemented; physiology simulation not implemented**
- `ShockInteractiveLabSlot.tsx` explicitly states `Not implemented · integration boundary only` and states that no synthetic patient, pressure trace, cardiac-output model, treatment response or simulation runs on the page.
- Current hemodynamics: qualitative/educational course trend data and comparison/quiz logic, not a coupled circulation engine.
- Hb→CaO2→DO2→VO2→CvO2/SvO2→extraction→oxygen-debt simulation: **absent at this ref**.
- Automated evidence: `tests/shock-page.test.mjs` **passed** within the Issue #6 full suite.
- Historical reduced-circulation reconciliation concern: **Historical / superseded at this production ref**.

A future Shock/Oxygen Transport simulation is planned work and should begin from an explicit clinical/educational model contract rather than a repair assumption.

### Equipment catalog

- Production paths: `app/equipment-lab/`, `public/equipment/`
- Status: **implemented as image/HTML-overlay interactive lessons**
- Behavior includes zoom/pan/fullscreen, keyboard controls, hotspots, flow diagrams, setup comparison, simplified assembly ordering, troubleshooting and scenario questions.
- `equipment-data.ts` stores device teaching content plus creator/source/license/accessed/alteration metadata.
- Tracheostomy lesson: static cuffed-tracheostomy photograph + HTML hotspots.
- Shiley-specific 3D runtime/snap-lock animation: **not identified in production source**.
- Dedicated equipment-catalog automated suite: not identified.

Historical Blender/Shiley work is therefore **Confirmed from project history but not production-integrated**.

### Chest-trauma 3D

- Production paths: `app/disease-processes/trauma/chest-trauma-3d/`, `public/visual-labs/chest-trauma/`
- Status: **integrated production 3D module**
- Architecture: React Three Fiber/Drei/Three.js; desktop/mobile respiratory and thorax GLBs; canonical node/morph lookup; geometry-derived runtime bounds/landmarks; camera controls; 2D-default lazy/opt-in 3D boundary; visibility/reduced-motion/runtime safeguards.
- Provenance: source-controlled HuBMAP HRA CC BY 4.0 attribution/derivative documentation and related asset manifests/license records.
- Automated evidence: `tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs` **passed** within the Issue #6 complete suite.
- Remaining verification: browser clipping/intersections, morph visual quality, controls, responsive behavior, performance, reduced-motion behavior and manual anatomical/educational visual fidelity.

### PFT

- Production paths: `app/pft-reports/`, `public/pft-images/`
- Status: **implemented**
- Current behavior: reconstructed educational reports, hidden diagnosis/reveal, metric inspection, keyboard-accessible view controls, stepwise interpretation, report-specific loop exploration, local review status and knowledge checks.
- Source-controlled data/test contract: 12 reports and 12 report-specific loop datasets with internal arithmetic/interpretive safeguards.
- Automated evidence: PFT loop-data tests **passed** in the Issue #6 complete suite.
- Clinical boundary: author-created educational reconstructions/no patient data; source references exist, but independent current human clinical validation remains separate.

### ABG / Hemodynamics

- Production paths: `app/abg-lab/`; qualitative Shock hemodynamics under the Shock module.
- Status: **25-case ABG learning lab implemented; no general hemodynamic calculation engine identified**.
- ABG interface: fixed authored case values, filtering, multiple choice, interpretation/compensation/oxygenation/cause/action feedback.
- Dedicated ABG automated file: not identified.
- No general user-entered hemodynamic/circulation calculation engine was established in this baseline.

### Disease-process modules

Generic dynamic disease records include:

- ARDS
- COPD exacerbation
- status asthmaticus
- pneumonia
- acute pulmonary edema
- pulmonary embolism
- pulmonary fibrosis
- cystic fibrosis
- neuromuscular respiratory failure
- bronchiectasis

Specialized source modules include Shock, Stroke, Burns, Chest Trauma, traumatic brain injury and trauma landing/general content.

Selected specialized tests including Shock, Stroke and trauma/chest-trauma were included in the complete Issue #6 suite and passed. Comprehensive automated coverage of every generic disease record is not established.

### Respiratory pharmacology

- Production path: `app/medications/`
- Status: **implemented**
- Structured monographs include mechanisms, indications, response, administration/device considerations, ventilator aerosol considerations, adverse effects, precautions/interactions, monitoring, failure cues, education, cases, traps, source IDs and review fields.
- Shared source registry includes AARC, ATS/ERS, GOLD, GINA, DailyMed, CFF, SCCM, AHA, CDC and other references.
- Dedicated medication automated suite: not identified.
- Reference presence is not independent clinical validation.

### Oxygen-delivery / equipment content

Source-verified device lessons cover oxygen, aerosol, airway and ventilation/emergency equipment using static/openly licensed imagery, diagrams, flow/setup teaching, troubleshooting and scenarios. Manufacturer-specific mechanical simulation is not implied.

### Other/future interactive systems

Current source contains several different interactive categories:

1. engine-backed physiologic/clinical systems — ECG/ACLS and Ventilator;
2. reconstructed-data/case teaching — PFT, ABG and equipment lessons;
3. 3D anatomy/pathology visualization — chest-trauma 3D.

The planned Shock/Oxygen Transport simulation remains an explicit integration boundary only. No separate general-purpose future simulation framework should be treated as production-ready.

## Automated validation inventory

### Baseline `main`

At `a0495e9...`, the canonical `npm test` script names only five selected test files and there is no source-controlled GitHub Actions workflow.

### Validated Issue #6 draft PR

At `96b5535...`, the proposed canonical path:

- uses npm + maintained `package-lock.json`;
- builds before testing;
- recursively discovers the complete source-controlled `tests/**/*.test.mjs` set;
- executes test files sequentially with Node 22.13 explicit type stripping;
- runs the Ventilator historical-P1 regression explicitly;
- uploads a durable per-file diagnostic report;
- contains no deployment credentials and does not deploy.

GitHub Actions run `31309995943` completed successfully.

## Clinical validation inventory

Production source contains substantial guideline/source evidence and educational boundaries. No current independent end-to-end clinical validation artifact tied to either baseline `main` or the Issue #6 PR ref has been established.

Automated pass results must not be called clinical validation.

## Accessibility validation inventory

Source includes ARIA/live regions, focus/keyboard behavior, semantic structures, responsive code, reduced-motion handling and accessibility-adjacent tests in major modules.

No comprehensive current WCAG conformance report or documented manual assistive-technology review is established.

## Mechanical / 3D validation inventory

Chest-trauma automated model/source contracts now have passing executable evidence on the Issue #6 PR ref. Manual browser/mechanical/visual validation remains open under Issue #5.

External Blender equipment-model review remains project-history evidence unless the relevant assets/runtime are version-controlled in production.

## Security and repository hygiene

Positive source controls include:

- `.env*`, `node_modules`, runtime/build state and PEM files ignored;
- no tracked environment file identified in the current production tree;
- `.openai/hosting.json` contains project/deployment metadata but no credential was observed during baseline inspection;
- dependency/build output such as `node_modules` is not source-controlled;
- third-party chest-trauma asset attribution is source-controlled;
- Issue #6 GitHub Actions uses `contents: read` and no deployment credentials.

Current hygiene items:

- pnpm artifacts remain pending deployment-aware disposition;
- production README remains largely starter-oriented;
- live-source deployment mapping remains undocumented.

## Current unresolved verification questions

1. Which GitHub ref corresponds to the current live ChatGPT Sites deployment?
2. After production PR #1 is merged, does the new validation workflow also pass from `main`?
3. Do Ventilator learner-facing browser behaviors agree with the now-passing automated P1 regressions?
4. Does chest-trauma 3D pass current manual browser/mechanical/visual review across supported devices?
5. What independent clinical-review cadence/evidence should govern safety-sensitive modules?
6. What comprehensive accessibility-validation workflow should be adopted?
7. Are the retained pnpm files required by the Sites/Vinext development/deployment environment?

## Baseline completion status

The **production source baseline is complete** and Issue #2 is closed.

The **automated validation baseline is successfully implemented and executed on draft production PR #1**. It is not yet landed on `main`; Issue #6 therefore remains open pending explicit merge authorization and post-merge verification.

Runtime/browser, clinical, accessibility, live-deployment and manual 3D validation remain separate follow-on evidence categories.
