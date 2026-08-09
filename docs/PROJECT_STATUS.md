# Project Status

## Purpose

This document separates project-control facts, production-source facts, executable validation evidence, and historical claims. Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Project-control verified status

- This repository is the RT Study Lab project-control/documentation repository.
- `main` is the default branch.
- `setup/project-control-foundation` is the active project-control branch.
- Project-control PR #1 remains open, draft, and unmerged.
- The production repository is `R3C4LL4L1F3/RT-study-lab` and remains private.
- Production Issue #6 work is represented by production draft PR #1; production `main` has not been modified by this validation phase.

## Production source baseline

The source-backed application baseline remains:

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Branch: `main`
- Source ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Commit: `Redesign Shock visual teaching page`

The live ChatGPT Sites deployment has **not** been proven to correspond exactly to this GitHub ref. Source state and deployment state remain separate evidence categories.

## Issue #6 validation baseline

A complete repository-validation implementation now exists on:

- Production branch: `validation/issue-6-test-baseline`
- Production draft PR: `R3C4LL4L1F3/RT-study-lab#1`
- Validated PR head: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Successful GitHub Actions run: `31309995943`
- Node: `22.13.0`
- Canonical validation package manager: **npm**

The successful run established:

- `npm ci` — **PASS**
- `npm run lint` — **PASS**
- `npm run build` — **PASS**
- complete 28-file source-controlled test suite — **PASS**
- dedicated Ventilator historical-P1 regression — **PASS**
- diagnostic report artifact upload — **PASS**

The runner uses Node 22.13.0 with explicit `--experimental-strip-types` because several existing `.test.mjs` files import application `.ts` modules directly. Earlier CI failures caused by `ERR_UNKNOWN_FILE_EXTENSION` were test-harness loader failures, not application or clinical regressions.

**Important:** the validated scripts/workflow remain on the draft PR. Production `main` retains the old validation command until explicit merge authorization is given.

## Major workstream status

| Workstream | Production-source status | Current executable / verification state |
|---|---|---|
| ECG Rhythm / ACLS Lab | Implemented under `app/acls/ecg-lab/` | Current source-controlled ECG/ACLS suites passed within Issue #6 full-suite CI at PR ref `96b5535...`; current clinical/accessibility review still separate |
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

At Issue #6 production PR ref `96b5535...`, automated regression evidence passed for:

1. double-trigger/triple-stacking prevention and minute-ventilation behavior;
2. dynamic-compliance validity during effort/contamination;
3. immutable VC/PC historical breath provenance;
4. expiratory-hold scheduling/rescheduling behavior.

These items are now **resolved in current source with passing automated regression evidence**. Issue #3 remains open for learner-facing browser verification of history labels, hold controls, and dynamic-compliance validity messaging.

## Current repository/project risks

1. **Validated CI is not yet on production `main`.** Production PR #1 remains draft/unmerged.
2. **Live deployment synchronization is unknown.** GitHub validation does not prove the live ChatGPT Sites deployment matches the reviewed commit.
3. **pnpm artifacts remain unresolved for deployment hygiene.** npm is canonical for validation; pnpm files are intentionally retained until Sites/Vinext requirements are understood.
4. **Clinical validation remains distinct.** Passing tests do not establish independent current clinical review.
5. **Accessibility validation remains incomplete.** Accessibility-oriented code/tests exist, but comprehensive current WCAG/manual assistive-technology evidence is absent.
6. **Manual 3D/browser validation remains incomplete.** Chest-trauma automated source/model contracts pass, but visual/mechanical/runtime review remains.
7. **Production README remains starter-oriented.** Issue #6 only added the validation/testing information required for the current task.

## Issue tracking

- #2 — Production-repository source baseline: **Closed / completed**.
- #3 — Ventilator P1 verification: automated regression now complete; **browser verification remains open**.
- #4 — Shock/Oxygen Transport reconciliation: **Closed / completed**; no current physiology simulation exists.
- #5 — Interactive Equipment / 3D verification: automated chest-trauma contracts now executed; **manual/browser/mechanical work remains open**.
- #6 — Complete production test baseline and CI: **implementation + executable validation complete on production draft PR #1; awaiting explicit merge authorization**.

## Next status transition

The validation infrastructure itself is no longer the unknown. The next transition is:

1. maintainer review/authorization of production PR #1;
2. after merge, verify the CI path on production `main`;
3. establish GitHub-to-live-Sites deployment correspondence;
4. complete the targeted browser/manual verification still open in Issues #3 and #5.

No merge is authorized by this status record.
