# Project Status

## Purpose

This document separates project-control facts, production-source facts, runtime/validation evidence, and historical project claims. Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Project-control verified status

- This repository is the RT Study Lab project-control/documentation repository.
- `main` is the default branch.
- `setup/project-control-foundation` is the active documentation foundation branch.
- PR #1 remains an open draft into `main`; it has not been merged.
- The initial verification backlog was issues #2–#5; issue #6 was added after the production baseline exposed a current validation-path gap.
- The production repository is now identified as `R3C4LL4L1F3/RT-study-lab`.

## Production baseline

The current source-backed baseline uses:

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility: Private
- Branch: `main`
- Source ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Commit: `Redesign Shock visual teaching page`

See `PRODUCTION_REPOSITORY_VERIFICATION.md` for the module-by-module evidence record.

GitHub source is now directly inspectable, but the live ChatGPT Sites deployment has **not** been proven to be synchronized to this GitHub ref. Source state and deployment state must remain separate.

## Major workstream verification overview

| Workstream | Production-source status | Validation / current issue state |
|---|---|---|
| ECG Rhythm / ACLS Lab | **Verified against production repository — implemented** under `app/acls/ecg-lab/` | Extensive source-controlled tests and guideline metadata exist; current tests were not executed in this audit and ECG tests are outside canonical `npm test` |
| Ventilator Waveform Lab | **Verified against production repository — implemented** under `app/visual-lab/` | Historical P1 concerns appear resolved in current source with dedicated regression coverage; runtime re-execution still required |
| Shock / Oxygen Transport | Shock learning page implemented; **oxygen-transport simulation not implemented** | Current source explicitly defines an integration boundary only; prior reduced-model reconciliation concern is superseded at this ref |
| Interactive Equipment | Equipment catalog implemented as image/HTML interactive lessons | Historical Blender/Shiley 3D work is not production-integrated at this ref |
| Chest-trauma 3D | **Verified against production repository — integrated** | R3F/Three.js GLB runtime, model-contract tests, and source-controlled attribution exist; current browser/mechanical test execution still required |
| PFT | **Verified against production repository — implemented** | 12 reconstructed report/loop datasets have source-controlled tests; current execution not performed |
| Disease-process modules | Generic disease library plus specialized Shock, Stroke, Burns, Chest Trauma, TBI and trauma modules are present | Test/clinical-review coverage is uneven by module |
| ABG / Hemodynamics | 25-case ABG learning lab present; qualitative Shock hemodynamics present | No general hemodynamic calculation engine or dedicated ABG test file identified |
| Respiratory Pharmacology | Structured medication monographs and shared source registry present | Dedicated medication tests not identified; reference presence is not clinical validation |
| Oxygen-delivery / equipment content | Device lessons and licensed/static assets present | No manufacturer-specific mechanical simulation implied |
| Future interactive clinical simulations | ECG/Ventilator/chest-trauma are already distinct interactive systems; Shock simulation remains planned | No separate general-purpose future simulation framework identified |

## Production architecture summary

Current source is a Next.js/React/TypeScript application built through Vinext/Vite with Cloudflare/ChatGPT Sites integration. Three.js/React Three Fiber is actively used by chest-trauma 3D. Drizzle tooling exists but the production schema is intentionally empty and D1/R2 bindings are null at the baseline ref.

The current `npm test` command performs a build and runs only five selected test files, although the repository contains a much broader test inventory. No `.github/workflows` CI configuration was identified.

## Historical Ventilator P1 disposition

Production source now contains dedicated `tests/ventilator-session352.test.mjs` regressions and corresponding session/provenance/hold implementation for the historical concerns:

1. double-trigger unintended triple stacking — **Resolved in current source; runtime re-execution required**
2. minute-ventilation defect during double triggering — **Resolved in current source; runtime re-execution required**
3. dynamic compliance during effort/contamination — **Resolved in current source; runtime re-execution required**
4. VC/PC historical breath relabeling — **Resolved in current source; runtime re-execution required**
5. expiratory-hold rescheduling — **Resolved in current source; runtime re-execution required**

Because those regression tests are not currently part of canonical `npm test` and were not executed in this GitHub-only audit, these are source-level dispositions rather than fresh pass results.

## Current known project-control / repository risks

1. **Incomplete canonical test command:** the default test script excludes substantial current suites, including ECG/ACLS, Shock, chest-trauma 3D, and the dedicated Ventilator P1 regression file.
2. **No GitHub CI baseline:** no source-controlled GitHub Actions workflow was identified.
3. **No current full-suite/build/lint artifact:** source inspection established test presence, not passing execution.
4. **Deployment synchronization unknown:** GitHub source-to-live-Sites correspondence is not currently evidenced.
5. **Package-manager ambiguity:** npm and pnpm lock/workspace files coexist.
6. **Production README is stale/generic:** it does not describe RT Study Lab architecture or verification workflow.
7. **Clinical/accessibility validation incomplete:** source references, ARIA/keyboard structures, and tests exist, but comprehensive current review evidence is not established.

## Current verification tracking

- #2 — **Closed / completed:** production-repository source baseline established.
- #3 — **Open:** Ventilator P1 implementation/regression source indicates resolution; executable regression/browser evidence still required.
- #4 — **Closed / completed:** Shock reconciliation established that no oxygen-transport simulation exists at the baseline ref; future physiology engine is planned work.
- #5 — **Open:** equipment/chest-trauma source integration mapped; Shiley model is not production-integrated and current 3D browser/mechanical validation remains outstanding.
- #6 — **Open / P0:** establish a complete production test baseline and GitHub CI after package-manager/test-command semantics are resolved.

## Historical evidence retained

Historical multidisciplinary Ventilator scores and historical ECG test-count milestones remain preserved in `VALIDATION_REGISTER.md`. They are not converted into current pass results merely because related source/tests now exist.

## Next status transition

The source-discovery baseline is established. The highest-value next validation phase is issue #6: create and execute a **complete canonical production test baseline** that includes the intended full source-controlled suite and durable CI evidence, then use those results to finalize source-level defect dispositions and protect future development.
