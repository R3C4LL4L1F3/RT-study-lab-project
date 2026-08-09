# Validation Register

This register preserves historical validation claims while recording current executable evidence separately. **Tests present**, **tests executed**, **clinical validation**, **accessibility validation**, **deployment correspondence**, and **manual visual/mechanical/browser review** are distinct evidence states.

## Authoritative current validation summary

| Area | Current evidence state | Disposition |
|---|---|---|
| Production CI | Automatic `main` validation on `d64bde34...` passed install, lint, build, complete source-controlled suite, Ventilator P1 regression and artifact upload | **GREEN** |
| Ventilator historical P1 software regression | Dedicated and full-suite automated evidence passes | **Automated evidence complete** |
| Ventilator browser/manual P1 closure | Learner-facing behavior under Issue #3 not yet manually closed | **INCOMPLETE / IN VALIDATION** |
| Ventilator independent clinical validation | No current independent contemporary module sign-off established | **INCOMPLETE** |
| Chest-trauma 3D automated contracts | Source/model/visual contract tests pass | **Automated evidence complete** |
| Chest-trauma 3D runtime/manual QA | Browser/mechanical/visual/performance review under Issue #5 remains open | **INCOMPLETE / IN VALIDATION** |
| ECG / ACLS software validation | Substantial source-controlled engine/workflow tests pass in canonical suite | **Substantial automated evidence** |
| ECG / ACLS independent contemporary clinical validation | No current independent end-to-end clinical sign-off tied to current production `main` | **INCOMPLETE** |
| Accessibility | Accessibility-oriented code/tests exist; no comprehensive manual/WCAG/AT baseline | **INCOMPLETE** |
| Deployment correspondence | Source-side Sites linkage known; active deployed Git SHA requires authoritative Sites metadata under Issue #8 | **INCOMPLETE / BLOCKED** |
| Interactive Models & Simulation Lab | No reusable numerical physiology framework or Shock/O₂ simulation currently implemented | **Architecture/model contract pending under Issue #9** |

Validation gaps above are **not automatically confirmed defects**.

## Production source baseline

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Original production baseline: `a0495e9fa4e5437d8a027312b618b5c1c389ef94` — `Redesign Shock visual teaching page`
- Current production `main`: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6` — `Run production validation on main pushes (#2)`

The original source-baseline audit did not itself execute tests/build/lint. Issues #6 and #7 subsequently established executable validation and automatic post-merge `main` validation.

## Current production validation infrastructure

Canonical repository validation uses:

- Node `22.13.0`
- npm + maintained `package-lock.json`
- `npm ci`
- `npm run lint`
- `npm run build`
- recursive `tests/**/*.test.mjs` discovery
- sequential isolated Node test processes
- explicit `--experimental-strip-types` for existing tests that import `.ts` source directly
- dedicated `npm run test:p1:ventilator`
- retained diagnostic report artifact

The full runner currently discovers **28 source-controlled `*.test.mjs` files**.

### Issue #6 baseline evidence

Pre-merge production PR #1 validation:

- validated ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Actions run: `31309995943`
- install — **PASS**
- lint — **PASS**
- build — **PASS**
- complete 28-file suite — **PASS**
- dedicated Ventilator P1 regression — **PASS**
- diagnostic artifact — **PASS**
- overall job — **PASS**

Post-merge exact-commit verification:

- merged production ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Actions run: `31310610948`
- validation path — **PASS**

### Issue #7 automatic-main evidence

Production PR #2 added automatic validation on pushes/merges to `main`.

Current production `main`:

- `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`

Automatic `main` run:

- Actions run `31311314980`
- event: `push`
- branch: `main`
- overall result: **PASS**

| Check | Result |
|---|---|
| Locked dependency installation (`npm ci`) | **PASS** |
| Repository lint | **PASS** |
| Vinext production build | **PASS** |
| Complete source-controlled test inventory | **PASS** |
| Dedicated Ventilator historical-P1 regression | **PASS** |
| Diagnostic report artifact upload | **PASS** |
| Overall job | **PASS** |

## Node/TypeScript test-harness finding

Several existing `.test.mjs` files import application `.ts` modules directly. Raw Node 22.13.0 rejects those imports without the configured support.

The validation harness therefore invokes test files with:

`node --experimental-strip-types --test <test-file>`

Earlier Issue #6 red runs caused by `ERR_UNKNOWN_FILE_EXTENSION` are **test-harness loader failures**, not application or clinical regressions.

## Ventilator Waveform Lab

### Historical multidisciplinary record

These scores remain **Confirmed from project history** and are not replaced by CI:

| Dimension | Historical score | Evidence basis |
|---|---:|---|
| Clinical | 82/100 | Confirmed from project history |
| Engineering | 76/100 | Confirmed from project history |
| Educational | 79/100 | Confirmed from project history |
| Mechanics | 88/100 | Confirmed from project history |
| Realism | 84/100 | Confirmed from project history |
| Measurement | 78/100 | Confirmed from project history |

Historical browser/clinical disposition: **PARTIAL PASS**.

### Current automated evidence

`tests/ventilator-session352.test.mjs` directly covers the historical high-risk concerns:

- exactly two-breath double-trigger clusters / rejection of unintended triple stacking;
- minute ventilation derived from completed delivered volumes over the declared interval;
- dynamic-compliance validity/contamination behavior;
- immutable VC/PC breath provenance across mode transitions;
- diagnostic hold arm/repeat/complete/cancel/invalid-state behavior after arbitrary breath numbers.

The dedicated P1 regression also passed on current production `main` in Actions run `31311314980`.

**Automated historical-P1 regression evidence: complete.**

**Browser/manual closure: incomplete under Issue #3.**

**Independent contemporary Ventilator clinical validation: incomplete.**

Do not create a production fix branch unless manual validation reproduces a current defect. Automated pass status is not clinical validation.

## ECG / ACLS Lab

Historical automated milestones remain historical records and are not converted into current test totals.

Current source-controlled ECG/ACLS tests covering waveform engine, calipers, practice/exam, clinical reasoning/UX, patient-state, pathways, treatment, arrest and post-arrest behavior are included in the complete production suite and passed in current automatic production validation.

**Current software-test evidence: substantial.**

**Independent contemporary clinical validation: incomplete.**

Initial P1 independent clinical-validation work is approved to begin through the Clinical Validation & Sources workflow after the approved project sequence reaches that stage. Do not create a production fix branch unless that validation establishes an implementation discrepancy.

## Interactive Models & Simulation Lab — Shock / Circulation / Oxygen Transport

Current production Shock content is a learning module with qualitative hemodynamic teaching and an explicit future-lab boundary.

- No synthetic circulation state engine is implemented.
- No numerical Hb→CaO₂→DO₂→VO₂→CvO₂/SvO₂→extraction→oxygen-debt engine is implemented.
- No reusable physiology model clock/state/invariant framework is implemented.
- No long-run numerical/conservation validation is applicable to a nonexistent engine.

`tests/shock-page.test.mjs` passes in the current canonical production suite, but that test validates page/content/boundary contracts rather than a numerical physiology simulation.

Current forward state:

- Issue #9 — **P1, Tier 3, APPROVED FOR SPECIFICATION; implementation not approved**.
- Required gate: approved clinical/model contract + approved reusable architecture/model contract before production implementation.
- Required future architecture validation includes independent review, deterministic cases, invariants, boundary behavior, long-run expectations, reset/replay, seed behavior and serialization expectations.

Future V/Q, gas-exchange, pulmonary-circulation, PE, ARDS-physiology, heart-failure-physiology and related models remain framework-dependent/deferred.

## Chest-trauma 3D

`tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs` cover source/model contracts including canonical nodes/morphs, desktop/mobile assets, geometry budgets, coordinate registration, geometry-derived landmarks/camera fitting, lazy/opt-in boundaries, interaction safeguards and provenance expectations.

Both pass in canonical production validation.

**Automated source/model/visual contract evidence: complete.**

**Manual runtime/browser/mechanical/visual validation: incomplete under Issue #5.**

Remaining evidence includes clipping/intersection review, morph visual fidelity, responsive behavior, camera/control behavior, reduced-motion behavior, performance/runtime stability and educational/anatomical fidelity.

Historical external Shiley Blender work remains outside production integration unless deliberately version-controlled and integrated.

## PFT

`tests/pft-loop-data.test.mjs` defines source-controlled contracts for reconstructed reports/loop datasets, arithmetic consistency, ratio/TLC safeguards, bronchodilator-response math, distinct physiologic trace sets and accessibility descriptions/boundaries.

Current production validation passes this test. Independent clinical review remains separate.

## ABG, medications, equipment catalog and broader disease content

- ABG: 25 authored cases present; no dedicated ABG automated test file identified.
- Medications: structured monographs/source IDs present; no dedicated medication automated test file identified.
- Equipment catalog: structured lessons, safety content and source/license metadata present; no dedicated equipment-catalog automated test file identified.
- Disease content: selected specialized tests exist, but comprehensive generic disease-record coverage is not established.

These are **coverage/validation gaps**, not confirmed defects.

## Independent clinical-validation framework — Issue #10

- Priority: P2
- Risk: Tier 3
- Owner: Clinical Validation & Sources
- Support: QA — Regression & Release
- Status: **APPROVED — not yet completed**

The framework must preserve source/version traceability, production-ref traceability, explicit clinical assumptions/simplifications, independent disposition, uncertainty/conflict handling and re-review triggers.

Initial P1 module validation begins with ECG/ACLS and Ventilator. Neither module is clinically validated merely because the framework record exists.

## Accessibility-validation baseline — Issue #11

- Priority: P2
- Risk: Tier 1
- Owner: Design System & UI/UX
- Support: QA — Regression & Release
- Status: **APPROVED — baseline incomplete**

Required project-level evidence includes, as applicable:

- keyboard operation;
- focus behavior;
- semantic structure/control naming;
- status/error/feedback announcements;
- responsive behavior;
- reduced motion;
- manual accessibility review;
- assistive-technology review where practical;
- production-ref traceability.

Existing ARIA/live regions, focus handling, responsive CSS and accessibility-adjacent tests do not by themselves establish comprehensive conformance.

## Deployment correspondence — Issue #8

Source-side Sites integration is verified. The active deployed Git ref remains **unknown** until authoritative private Sites saved/deployed-version metadata is inspected.

Current disposition: **INCOMPLETE / BLOCKED**.

Do not infer live deployment equivalence from GitHub `main` or green CI. Do not redeploy simply to generate evidence.

## Validation policy going forward

1. Use npm + maintained `package-lock.json` for canonical production-repository validation unless a documented decision changes that convention.
2. Preserve automatic validation on review refs and production `main`.
3. Retain exact run/ref evidence for material validation decisions.
4. Keep complete recursive test discovery rather than returning to a fixed subset.
5. Keep automated, clinical, accessibility, deployment and manual visual/mechanical evidence distinct.
6. Do not promote a validation gap to a current defect without supporting evidence.
7. Do not delete/regenerate pnpm artifacts until their Sites/Vinext role is verified.
8. For Interactive Models, do not begin production implementation until the clinical/model contract and reusable architecture decision are approved.
