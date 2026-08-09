# Validation Register

This register preserves historical validation claims while recording current executable evidence separately. **Tests present**, **tests executed**, **clinical validation**, **accessibility validation**, and **manual visual/mechanical review** are distinct evidence states.

## Production source baseline

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Original production baseline ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Original baseline commit: `Redesign Shock visual teaching page`
- Initial audit type: GitHub source inspection

The original source-baseline audit did not execute tests, build, or lint. Issues #6 and #7 subsequently established executable CI evidence and automatic post-merge validation.

## Current production validation infrastructure

Current production `main` ref:

- `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- `Run production validation on main pushes (#2)`

Canonical repository validation uses:

- Node `22.13.0`
- npm + maintained `package-lock.json`
- `npm ci`
- `npm run lint`
- `npm run build`
- recursive `tests/**/*.test.mjs` discovery
- sequential isolated Node test processes
- explicit `--experimental-strip-types` for existing tests that directly import `.ts` source
- dedicated `npm run test:p1:ventilator`
- retained diagnostic report artifact

The full runner discovers **28 source-controlled `*.test.mjs` files** under `tests/`.

### Issue #6 baseline evidence

Pre-merge production PR #1 validation:

- ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Actions run: `31309995943`
- install — **PASS**
- lint — **PASS**
- build — **PASS**
- complete 28-file suite — **PASS**
- dedicated Ventilator P1 regression — **PASS**
- diagnostic artifact — **PASS**
- overall job — **PASS**

Post-merge exact-commit verification for production PR #1:

- production ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Actions run: `31310610948`
- all validation steps — **PASS**

### Issue #7 automatic-main validation evidence

Production PR #2 changed only `.github/workflows/production-validation.yml` to add `main` to the existing `push` branch filter.

PR/branch validation at ref `586314ab8e252dba0a479c062a9ade9c96c5d1e6`:

- branch-push Actions run `31310866155` — **PASS**
- pull-request Actions run `31310877109` — **PASS**

After authorized squash merge, production `main` advanced to:

- `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`

The merge itself automatically started `Production Validation` as Actions run `31311314980` with event `push` and branch `main`.

Post-merge automatic-main result:

| Check | Result |
|---|---|
| Locked dependency installation (`npm ci`) | **PASS** |
| Repository lint (`npm run lint`) | **PASS** |
| Vinext production build (`npm run build`) | **PASS** |
| Complete source-controlled test inventory (`npm run test:all`) | **PASS** |
| Dedicated Ventilator historical-P1 regression (`npm run test:p1:ventilator`) | **PASS** |
| Full-suite diagnostic report artifact upload | **PASS** |
| Overall GitHub Actions job | **PASS** |

**Current disposition:** automatic repository validation is now established for pull requests targeting `main` and pushes/merges to `main`.

## Node/TypeScript test-harness finding

Several existing `.test.mjs` files import application `.ts` modules directly. At the repository's declared minimum Node version, raw Node 22.13.0 rejects those imports with `ERR_UNKNOWN_FILE_EXTENSION`.

The validation harness therefore invokes each test file with:

`node --experimental-strip-types --test <test-file>`

This is a test-runner configuration requirement; it does not modify production application source. Earlier Issue #6 red runs caused by this loader behavior are **not application or clinical regressions**.

## Complete current automated-test inventory

The complete runner includes source-controlled tests covering:

- chest-trauma 3D model/runtime contracts
- chest-trauma visual contracts
- ECG engine, calipers, practice, exam, patient-state, clinical reasoning/UX, pathways, treatment, arrest and post-arrest logic
- PFT report/loop-data contracts
- rendered HTML
- Shock page/content boundaries
- Stroke page and visual interactions
- trauma page
- Ventilator engine and Sessions 3, 3.5 and 3.5.2

New files following `tests/**/*.test.mjs` enter the canonical validation path automatically.

## Ventilator Waveform Lab

### Historical multidisciplinary validation summary

These remain **Confirmed from project history** and are not replaced by automated CI:

| Dimension | Historical score | Evidence basis |
|---|---:|---|
| Clinical | 82/100 | Confirmed from project history |
| Engineering | 76/100 | Confirmed from project history |
| Educational | 79/100 | Confirmed from project history |
| Mechanics | 88/100 | Confirmed from project history |
| Realism | 84/100 | Confirmed from project history |
| Measurement | 78/100 | Confirmed from project history |

Historical browser/clinical result: **PARTIAL PASS**.

### Current executable regression evidence

`tests/ventilator-session352.test.mjs` directly covers the historical high-risk concerns:

- double-trigger clusters must contain exactly two breaths; unintended triple stacking is rejected;
- minute ventilation is derived from completed delivered volumes over the declared interval;
- dynamic compliance is validity-aware and contaminated in effort/leak-related scenarios;
- historical breaths retain immutable VC/PC provenance across mode transitions;
- diagnostic holds can arm after arbitrary breath numbers, repeat, complete, cancel, and invalidate under incompatible conditions.

The dedicated P1 regression has passed repeatedly, including the automatic production-`main` run `31311314980` at `d64bde34...`.

**Current disposition:** automated regression verification is complete. Browser presentation/control verification remains required before Issue #3 is fully complete. Automated pass status is not independent clinical validation.

## ECG Rhythm / ACLS Lab

### Historical automated-test milestones

These counts remain historical records and are not converted into current suite counts:

| Milestone | Historical result | Evidence basis |
|---|---|---|
| Phase 1A | ECG tests 12/12; site tests 97/97 | Confirmed from project history |
| Final Phase 1 audit | ECG tests 33/33; site tests 118/118 | Confirmed from project history |
| Version 27 landmark snapping | ECG tests 40/40; site tests 125/125 | Confirmed from project history |
| Phase 2A-1 patient-state engine | Patient-state tests 8/8 | Confirmed from project history |
| Phase 2A-2 clinical practice/exam | Patient-state tests 19/19; ECG tests 59/59; complete suite 144 | Confirmed from project history |
| Phase 2B-2 treatment engine | Treatment tests 18/18; complete suite 175/175 | Confirmed from project history |

### Current executable evidence

Current source-controlled ECG/ACLS tests covering engine, calipers, practice/exam, clinical reasoning/UX, pathways, treatment, arrest and post-arrest behavior are included in the complete production validation suite and passed in automatic `main` run `31311314980`.

This does not independently establish current AHA clinical validation or comprehensive accessibility conformance.

## Shock / Oxygen Transport

The current Shock page is a learning module with qualitative hemodynamic teaching and an explicit future-lab boundary. The oxygen-transport simulation is not implemented.

`tests/shock-page.test.mjs` is included in the complete suite and passed in automatic `main` run `31311314980`. No circulation-engine numerical/conservation validation is applicable because that simulation engine is absent.

## PFT

`tests/pft-loop-data.test.mjs` defines source-controlled contracts for 12 reconstructed reports/loop datasets, internal arithmetic consistency, ratio/TLC safeguards, bronchodilator-response math, distinct physiologic trace sets, and accessibility descriptions/boundaries.

The PFT test passed in automatic `main` run `31311314980`.

## Chest-trauma 3D

`tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs` cover source/model contracts including canonical nodes/morphs, desktop/mobile assets, geometry budgets, coordinate registration, geometry-derived landmarks/camera fitting, lazy/opt-in boundaries, interaction safeguards, and provenance expectations.

Both passed in automatic `main` run `31311314980`.

This establishes automated source/model-contract evidence only. Browser rendering, clipping/intersection review, morph visual quality, performance, reduced-motion behavior in real browsers, and mechanical/visual fidelity still require manual/runtime review under Issue #5.

## ABG, medications, equipment catalog, and broader disease content

- ABG: 25 authored cases are present; no dedicated ABG automated test file was identified.
- Medications: structured monographs and source IDs are present; no dedicated medication automated test file was identified.
- Equipment catalog: structured lessons, safety content and source/license metadata are present; no dedicated equipment-lab automated test file was identified.
- Disease content: dedicated tests exist for selected specialized modules such as Shock, Stroke and trauma/chest-trauma, but comprehensive generic disease-record coverage is not established.

## Clinical-validation inventory

Production source contains substantial reference evidence, including the shared source registry and module-specific guideline/source metadata.

**No current independent end-to-end clinical validation artifact tied to current production `main` was established.** Automated CI must not be substituted for clinician review, guideline reconciliation, or clinical plausibility/correctness review.

## Accessibility-validation inventory

Source evidence includes ARIA labels/live regions, focus handling, keyboard interaction, responsive styles, reduced-motion handling, and accessibility-adjacent tests in several major modules.

**No comprehensive current WCAG conformance artifact or documented manual assistive-technology review was established.**

## Mechanical / 3D validation inventory

Automated chest-trauma 3D source/model tests have passing executable evidence on current production `main`. Manual visual/mechanical browser validation remains separate and incomplete.

Historical external equipment-model work, including Shiley Blender assets, remains outside the production integration baseline unless deliberately version-controlled and integrated.

## Validation policy going forward

For future production changes:

1. use npm and the maintained `package-lock.json` for repository validation unless a documented architecture decision changes that convention;
2. require the canonical validation path on review refs and preserve automatic validation after merges to `main`;
3. retain CI/run evidence with the PR or project-control record when it is material to a verification decision;
4. keep complete recursive test discovery rather than returning to a manually curated subset;
5. keep automated results separate from clinical, accessibility, deployment, and visual/mechanical evidence;
6. do not delete or regenerate the retained pnpm files until their ChatGPT Sites/Vinext role is verified.
