# Project Status

## Purpose

This document separates project-control facts, production-source facts, executable validation evidence, and historical claims. Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Project-control verified status

- This repository is the RT Study Lab project-control/documentation repository.
- `main` is the default branch.
- `setup/project-control-foundation` is the active project-control branch.
- Project-control PR #1 remains open, draft, and unmerged.
- The production repository is `R3C4LL4L1F3/RT-study-lab` and remains private.
- Production PR #1 was merged as part of Issue #6 completion.
- Production PR #2 was merged as part of Issue #7 completion.

## Production source baseline

The original source-backed application baseline was:

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Branch: `main`
- Ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Commit: `Redesign Shock visual teaching page`

After Issue #6, production `main` advanced to:

- Ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Commit: `Establish complete production validation baseline (#1)`

After Issue #7, current production `main` is:

- Ref: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Commit: `Run production validation on main pushes (#2)`
- Merge method: squash

The live ChatGPT Sites deployment has **not** been proven to correspond exactly to this GitHub ref. Source state and deployment state remain separate evidence categories.

## Automated validation baseline

Issue #6 established and merged the complete repository validation path using:

- Node `22.13.0`
- npm + maintained `package-lock.json`
- `npm ci`
- `npm run lint`
- `npm run build`
- recursive 28-file source-controlled test discovery
- dedicated Ventilator historical-P1 regression
- diagnostic artifact upload

Issue #6 pre-merge run `31309995943` passed at PR ref `96b5535f9228c7b01c709386e050ce53e68f14d4`.

Issue #6 exact-commit post-merge verification run `31310610948` passed at production ref `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`.

Issue #7 then added automatic `push: main` validation through production PR #2. The merge to `main` automatically started Actions run `31311314980` on exact commit `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`. That run passed:

- locked dependency installation — **PASS**
- lint — **PASS**
- build — **PASS**
- complete source-controlled test suite — **PASS**
- dedicated Ventilator historical-P1 regression — **PASS**
- diagnostic artifact upload — **PASS**
- overall job — **PASS**

The runner uses Node 22.13.0 with explicit `--experimental-strip-types` because several existing `.test.mjs` files import application `.ts` modules directly. Earlier CI failures caused by `ERR_UNKNOWN_FILE_EXTENSION` were test-harness loader failures, not application or clinical regressions.

## Major workstream status

| Workstream | Production-source status | Current executable / verification state |
|---|---|---|
| ECG Rhythm / ACLS Lab | Implemented under `app/acls/ecg-lab/` | Current source-controlled ECG/ACLS suites pass within the complete production validation suite; current clinical/accessibility review remains separate |
| Ventilator Waveform Lab | Implemented under `app/visual-lab/` | Full Ventilator suite and dedicated Session 3.5.2 P1 regression pass; browser verification remains under #3 |
| Shock / Oxygen Transport | Shock learning page implemented; simulation explicitly not implemented | `shock-page.test.mjs` passes; planned physiology engine remains future work, not a current defect |
| Equipment catalog | Image/HTML interactive lessons implemented | No dedicated equipment-catalog suite identified; historical Shiley 3D remains non-integrated |
| Chest-trauma 3D | Integrated R3F/Three.js module | 3D/model and visual source-controlled test files pass; manual browser/mechanical/visual review remains under #5 |
| PFT | Interactive reconstructed report/loop system implemented | PFT loop-data test passes in full suite |
| Disease-process modules | Generic disease library plus specialized Shock/Stroke/Burns/Chest Trauma/TBI/trauma modules present | Selected specialized module tests pass; comprehensive generic disease coverage not established |
| ABG / Hemodynamics | 25-case ABG lab; qualitative Shock hemodynamics | No dedicated ABG test file/general hemodynamic engine identified |
| Respiratory Pharmacology | Structured medication monographs/source registry implemented | Dedicated medication tests not identified; reference presence is not clinical validation |
| Oxygen/equipment content | Device lessons and licensed/static assets implemented | No manufacturer-specific mechanical simulation implied |

## Ventilator historical P1 disposition

Automated regression evidence now repeatedly passes for:

1. double-trigger/triple-stacking prevention and minute-ventilation behavior;
2. dynamic-compliance validity during effort/contamination;
3. immutable VC/PC historical breath provenance;
4. expiratory-hold scheduling/rescheduling behavior.

These items are **resolved in current source with passing automated regression evidence**. Issue #3 remains open for learner-facing browser verification of history labels, hold controls, and dynamic-compliance validity messaging.

## Current repository/project risks

1. **Live deployment synchronization is unknown.** GitHub validation does not prove the live ChatGPT Sites deployment matches the reviewed commit.
2. **pnpm artifacts remain unresolved for deployment hygiene.** npm is canonical for validation; pnpm files are intentionally retained until Sites/Vinext requirements are understood.
3. **Clinical validation remains distinct.** Passing tests do not establish independent current clinical review.
4. **Accessibility validation remains incomplete.** Accessibility-oriented code/tests exist, but comprehensive current WCAG/manual assistive-technology evidence is absent.
5. **Manual 3D/browser validation remains incomplete.** Chest-trauma automated source/model contracts pass, but visual/mechanical/runtime review remains.
6. **Production README remains starter-oriented.** Validation/testing documentation has been improved, but a broader project-specific README rewrite remains optional future cleanup.

## Issue tracking

- #2 — Production-repository source baseline: **Closed / completed**.
- #3 — Ventilator P1 verification: automated regression complete; **browser verification remains open**.
- #4 — Shock/Oxygen Transport reconciliation: **Closed / completed**; no current physiology simulation exists.
- #5 — Interactive Equipment / 3D verification: automated chest-trauma contracts executed; **manual/browser/mechanical work remains open**.
- #6 — Complete production test baseline and CI: **Closed / completed**.
- #7 — Automatic validation after merges to `main`: **Closed / completed**; automatic `main` run `31311314980` passed on `d64bde34...`.

## Next status transition

Repository validation infrastructure is now established and automatic on both PRs targeting `main` and pushes/merges to `main`.

The next priorities are:

1. establish GitHub-to-live-Sites deployment correspondence;
2. complete learner-facing Ventilator browser verification under Issue #3;
3. complete chest-trauma/equipment manual browser/mechanical verification under Issue #5;
4. keep clinical, accessibility, deployment, and visual/mechanical evidence separate from automated CI results.
