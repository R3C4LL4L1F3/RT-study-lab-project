# Validation Register

This register preserves historical validation claims while recording current executable evidence separately. **Tests present**, **tests executed**, **clinical validation**, **accessibility validation**, and **manual visual/mechanical review** are distinct evidence states.

## Production source baseline

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Production `main` baseline ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Baseline commit: `Redesign Shock visual teaching page`
- Initial audit type: GitHub source inspection

The original source-baseline audit did not execute tests, build, or lint. That limitation is preserved as historical context; Issue #6 subsequently established executable evidence on a dedicated production validation branch and draft PR.

## Issue #6 executable automated-validation baseline

Validation implementation:

- Production branch: `validation/issue-6-test-baseline`
- Production draft PR: `R3C4LL4L1F3/RT-study-lab#1` — `Establish complete production validation baseline`
- Validated PR ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- GitHub Actions workflow: `Production Validation`
- Successful run ID: `31309995943`
- Job: `Lint, build, and complete tests`
- Runner: GitHub-hosted `ubuntu-latest`
- Application Node version: `22.13.0`
- Dependency install: `npm ci`
- Validation package manager: **npm**

### Successful executable results

At production PR ref `96b5535f9228c7b01c709386e050ce53e68f14d4`:

| Check | Result |
|---|---|
| Locked dependency installation (`npm ci`) | **PASS** |
| Repository lint (`npm run lint`) | **PASS** |
| Vinext production build (`npm run build`) | **PASS** |
| Complete source-controlled test inventory (`npm run test:all`) | **PASS** |
| Dedicated Ventilator historical-P1 regression (`npm run test:p1:ventilator`) | **PASS** |
| Full-suite diagnostic report artifact upload | **PASS** |
| Overall GitHub Actions job | **PASS** |

The complete runner discovers **28 source-controlled `*.test.mjs` files** under `tests/` and executes each file sequentially in its own Node test-runner process.

### Node/TypeScript test-harness finding

Several existing `.test.mjs` files import application `.ts` modules directly. At the repository's declared minimum Node version, Node 22.13.0 rejects those imports under raw `node --test` with `ERR_UNKNOWN_FILE_EXTENSION`.

The validation harness therefore invokes each test file with:

`node --experimental-strip-types --test <test-file>`

This is a test-runner configuration requirement; it does not modify or transpile production application source. Earlier red Issue #6 runs that showed this loader error are **not application or clinical regressions**.

### Current merge boundary

The successful validation is attached to the **draft production PR**, not production `main`. Until PR #1 is explicitly authorized and merged:

- production `main` still contains the older five-file `npm test` command;
- production `main` still lacks the proposed GitHub Actions workflow;
- the new test runner and `TESTING.md` remain branch/PR changes.

Do not describe this validation infrastructure as deployed to production `main` until merge evidence exists.

## Complete current automated-test inventory

The validated full-suite runner includes the 28 source-controlled test files covering:

- chest-trauma 3D model/runtime contracts
- chest-trauma visual contracts
- ECG engine, calipers, practice, exam, patient-state, clinical reasoning/UX, pathways, treatment, arrest and post-arrest logic
- PFT report/loop-data contracts
- rendered HTML
- Shock page/content boundaries
- Stroke page and visual interactions
- trauma page
- Ventilator engine and Sessions 3, 3.5 and 3.5.2

The runner uses recursive `tests/**/*.test.mjs` discovery, so new test files following that convention enter the canonical validation path automatically rather than requiring manual editing of a fixed file list.

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

At production PR ref `96b5535f9228c7b01c709386e050ce53e68f14d4`, the dedicated P1 regression command **passed**, and the broader Ventilator tests also passed as part of the complete suite.

**Current disposition:** automated regression verification is complete on the draft PR. Browser presentation/control verification remains required before Issue #3 is fully complete. Automated pass status is not independent clinical validation.

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

Current source-controlled ECG/ACLS files covering engine, calipers, practice/exam, clinical reasoning/UX, pathways, treatment, arrest and post-arrest behavior were included in the complete Issue #6 suite and **passed at PR ref `96b5535...`**.

This does not independently establish current AHA clinical validation or comprehensive accessibility conformance.

## Shock / Oxygen Transport

The current Shock page is a learning module with qualitative hemodynamic teaching and an explicit future-lab boundary. The oxygen-transport simulation is not implemented.

`tests/shock-page.test.mjs` was included in the Issue #6 full suite and **passed at PR ref `96b5535...`**. No circulation-engine numerical/conservation validation is applicable because that simulation engine is absent.

## PFT

`tests/pft-loop-data.test.mjs` defines source-controlled contracts for 12 reconstructed reports/loop datasets, internal arithmetic consistency, ratio/TLC safeguards, bronchodilator-response math, distinct physiologic trace sets, and accessibility descriptions/boundaries.

The PFT test file was included in the Issue #6 full suite and **passed at PR ref `96b5535...`**.

## Chest-trauma 3D

`tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs` cover source/model contracts including canonical nodes/morphs, desktop/mobile assets, geometry budgets, coordinate registration, geometry-derived landmarks/camera fitting, lazy/opt-in boundaries, interaction safeguards, and provenance expectations.

Both files were included in the Issue #6 full suite and **passed at PR ref `96b5535...`**.

This establishes automated source/model-contract evidence only. Browser rendering, clipping/intersection review, morph visual quality, performance, reduced-motion behavior in real browsers, and mechanical/visual fidelity still require manual/runtime review under Issue #5.

## ABG, medications, equipment catalog, and broader disease content

- ABG: 25 authored cases are present; no dedicated ABG automated test file was identified.
- Medications: structured monographs and source IDs are present; no dedicated medication automated test file was identified.
- Equipment catalog: structured lessons, safety content and source/license metadata are present; no dedicated equipment-lab automated test file was identified.
- Disease content: dedicated tests exist for selected specialized modules such as Shock, Stroke and trauma/chest-trauma, but comprehensive generic disease-record coverage is not established.

## Clinical-validation inventory

Production source contains substantial reference evidence, including the shared source registry and module-specific guideline/source metadata.

**No current independent end-to-end clinical validation artifact tied to the Issue #6 validated PR ref was established.** Automated CI must not be substituted for clinician review, guideline reconciliation, or clinical plausibility/correctness review.

## Accessibility-validation inventory

Source evidence includes ARIA labels/live regions, focus handling, keyboard interaction, responsive styles, reduced-motion handling, and accessibility-adjacent tests in several major modules.

**No comprehensive current WCAG conformance artifact or documented manual assistive-technology review was established.**

## Mechanical / 3D validation inventory

Automated chest-trauma 3D source/model tests now have passing executable evidence at the Issue #6 PR ref. Manual visual/mechanical browser validation remains separate and incomplete.

Historical external equipment-model work, including Shiley Blender assets, remains outside the production integration baseline unless deliberately version-controlled and integrated.

## Validation policy going forward

For future production changes:

1. use npm and the maintained `package-lock.json` for repository validation unless a documented architecture decision changes that convention;
2. run the canonical build/lint/full-suite path at the exact review ref;
3. retain CI/run evidence with the PR or project-control record;
4. keep the complete test discovery convention rather than returning to a manually curated subset;
5. keep automated results separate from clinical, accessibility, deployment, and visual/mechanical evidence;
6. do not delete or regenerate the retained pnpm files until their ChatGPT Sites/Vinext role is verified.
