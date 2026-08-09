# Project Status

## Purpose

This document separates project-control facts, production-source facts, executable validation evidence, and historical claims. Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Project-control verified status

- This repository is the RT Study Lab project-control/documentation repository.
- `main` is the default branch.
- `setup/project-control-foundation` is the active project-control branch.
- Project-control PR #1 remains open, draft, and unmerged.
- The production repository is `R3C4LL4L1F3/RT-study-lab` and remains private.
- Production PR #1 has been merged into production `main` as part of Issue #6 completion.

## Production source baseline

The original source-backed application baseline was:

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Branch: `main`
- Ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Commit: `Redesign Shock visual teaching page`

After Issue #6, production `main` is now:

- Ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Commit: `Establish complete production validation baseline (#1)`
- Merge method: squash

The live ChatGPT Sites deployment has **not** been proven to correspond exactly to this GitHub ref. Source state and deployment state remain separate evidence categories.

## Issue #6 validation baseline

Issue #6 established and merged the repository validation path.

Validation implementation:

- Production branch: `validation/issue-6-test-baseline`
- Production PR: `R3C4LL4L1F3/RT-study-lab#1` — **merged**
- Validated PR head: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Successful pre-merge Actions run: `31309995943`
- Production `main` merge ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Post-merge exact-commit verification branch: `validation/post-merge-main-verification`
- Successful post-merge Actions run: `31310610948`
- Node: `22.13.0`
- Canonical validation package manager: **npm**

The post-merge verification branch points to the **exact same commit now on production `main`**. This was necessary because the merged workflow's current `push` trigger covers `validation/**` but not `main`.

The successful post-merge run established:

- `npm ci` — **PASS**
- `npm run lint` — **PASS**
- `npm run build` — **PASS**
- complete 28-file source-controlled test suite — **PASS**
- dedicated Ventilator historical-P1 regression — **PASS**
- diagnostic report artifact upload — **PASS**
- overall GitHub Actions job — **PASS**

The runner uses Node 22.13.0 with explicit `--experimental-strip-types` because several existing `.test.mjs` files import application `.ts` modules directly. Earlier CI failures caused by `ERR_UNKNOWN_FILE_EXTENSION` were test-harness loader failures, not application or clinical regressions.

## Major workstream status

| Workstream | Production-source status | Current executable / verification state |
|---|---|---|
| ECG Rhythm / ACLS Lab | Implemented under `app/acls/ecg-lab/` | Current source-controlled ECG/ACLS suites passed within the complete Issue #6 suite; current clinical/accessibility review remains separate |
| Ventilator Waveform Lab | Implemented under `app/visual-lab/` | Full Ventilator suite and dedicated Session 3.5.2 P1 regression passed; browser verification remains under #3 |
| Shock / Oxygen Transport | Shock learning page implemented; simulation explicitly not implemented | `shock-page.test.mjs` passed; planned physiology engine remains future work, not a current defect |
| Equipment catalog | Image/HTML interactive lessons implemented | No dedicated equipment-catalog suite identified; historical Shiley 3D remains non-integrated |
| Chest-trauma 3D | Integrated R3F/Three.js module | 3D/model and visual source-controlled test files passed; manual browser/mechanical/visual review remains under #5 |
| PFT | Interactive reconstructed report/loop system implemented | PFT loop-data test passed in full suite |
| Disease-process modules | Generic disease library plus specialized Shock/Stroke/Burns/Chest Trauma/TBI/trauma modules present | Selected specialized module tests passed; comprehensive generic disease coverage not established |
| ABG / Hemodynamics | 25-case ABG lab; qualitative Shock hemodynamics | No dedicated ABG test file/general hemodynamic engine identified |
| Respiratory Pharmacology | Structured medication monographs/source registry implemented | Dedicated medication tests not identified; reference presence is not clinical validation |
| Oxygen/equipment content | Device lessons and licensed/static assets implemented | No manufacturer-specific mechanical simulation implied |

## Ventilator historical P1 disposition

At both the validated PR ref and the exact merged production `main` commit, automated regression evidence passed for:

1. double-trigger/triple-stacking prevention and minute-ventilation behavior;
2. dynamic-compliance validity during effort/contamination;
3. immutable VC/PC historical breath provenance;
4. expiratory-hold scheduling/rescheduling behavior.

These items are now **resolved in current source with passing automated regression evidence**. Issue #3 remains open for learner-facing browser verification of history labels, hold controls, and dynamic-compliance validity messaging.

## Current repository/project risks

1. **Live deployment synchronization is unknown.** GitHub validation does not prove the live ChatGPT Sites deployment matches the reviewed commit.
2. **Automatic post-merge `main` validation is not yet configured.** PRs targeting `main` run CI, but the current `push` trigger only covers `validation/**`; Issue #6 used an exact-commit validation branch for post-merge evidence.
3. **pnpm artifacts remain unresolved for deployment hygiene.** npm is canonical for validation; pnpm files are intentionally retained until Sites/Vinext requirements are understood.
4. **Clinical validation remains distinct.** Passing tests do not establish independent current clinical review.
5. **Accessibility validation remains incomplete.** Accessibility-oriented code/tests exist, but comprehensive current WCAG/manual assistive-technology evidence is absent.
6. **Manual 3D/browser validation remains incomplete.** Chest-trauma automated source/model contracts pass, but visual/mechanical/runtime review remains.
7. **Production README remains starter-oriented.** Issue #6 added the validation/testing information required for the current task but did not perform a broader README rewrite.

## Issue tracking

- #2 — Production-repository source baseline: **Closed / completed**.
- #3 — Ventilator P1 verification: automated regression complete; **browser verification remains open**.
- #4 — Shock/Oxygen Transport reconciliation: **Closed / completed**; no current physiology simulation exists.
- #5 — Interactive Equipment / 3D verification: automated chest-trauma contracts executed; **manual/browser/mechanical work remains open**.
- #6 — Complete production test baseline and CI: **completed and merged; exact merged `main` commit passed post-merge validation**.

## Next status transition

The repository validation baseline is now established on production `main`. The next priorities are:

1. add a narrowly scoped automatic `push: main` post-merge validation trigger through a separate reviewed change;
2. establish GitHub-to-live-Sites deployment correspondence;
3. complete the targeted browser/manual verification still open in Issues #3 and #5;
4. keep clinical, accessibility, deployment, and visual/mechanical evidence separate from automated CI results.
