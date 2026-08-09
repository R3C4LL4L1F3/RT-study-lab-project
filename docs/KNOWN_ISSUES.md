# Known Issues and Verification Concerns

This register distinguishes confirmed current repository/control risks from historical application defects and unresolved validation work.

## Current known issues / risks

### PC-001 — Canonical production test command does not cover the full current test inventory

- Severity: High
- Evidence basis: **Verified against production repository**
- Lifecycle: **Current known issue**
- Source ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Evidence: `package.json` runs only five selected test files after build, while the production tree contains many additional ECG/ACLS, Ventilator, Shock, Stroke, trauma/chest-trauma 3D, and UX/clinical test files.
- Important example: `tests/ventilator-session352.test.mjs`, which contains regressions for the historical Ventilator P1 concerns, is not included in `npm test`.
- Impact: a successful default test command would not establish that the full current source-controlled regression suite passed.
- Resolution target: define a canonical full-suite command, make exclusions deliberate/explicit, execute it at a recorded source ref, and retain durable results.

### PC-002 — No source-controlled GitHub CI baseline

- Severity: High
- Evidence basis: **Verified against production repository**
- Lifecycle: **Current known issue**
- Evidence: no `.github/workflows` configuration was identified in the production baseline tree.
- Impact: future source changes lack an automatic GitHub build/lint/full-test gate and durable per-commit result trail.
- Resolution target: add a conservative CI workflow only after the canonical install/package-manager and full-test command are resolved.

### PC-003 — Live deployment synchronization is not verified

- Severity: Medium
- Evidence basis: Project-control verified + production-source verified boundary
- Lifecycle: **Current known issue (project control)**
- Evidence: the GitHub source repository is now identified, and Sites/Vinext hosting configuration exists, but this audit did not prove that the live ChatGPT Sites deployment is built from GitHub `main` at the recorded ref.
- Impact: GitHub source state must not automatically be called live deployment state.
- Resolution target: record a non-secret deployment verification procedure/ref and source-to-deployment relationship.

### PC-004 — Package-manager state is ambiguous

- Severity: Medium
- Evidence basis: **Verified against production repository**
- Lifecycle: **Current known issue (repository hygiene)**
- Evidence: `package-lock.json`, `pnpm-lock.yaml`, and `pnpm-workspace.yaml` coexist; README/scripts are npm-oriented.
- Impact: fresh-environment reproducibility and CI setup can diverge if tools resolve different lockfiles.
- Resolution target: select/document the canonical package manager and remove only demonstrably stale lock/workspace files through a reviewed application-repository PR.

### PC-005 — Production README is stale/generic

- Severity: Low
- Evidence basis: **Verified against production repository**
- Lifecycle: **Current known issue (repository documentation)**
- Evidence: the production README still describes the generic Vinext starter rather than RT Study Lab modules, architecture, verification commands, and GitHub/Sites relationship.
- Resolution target: revise through a focused production-repository documentation PR after test/package-manager conventions are decided.

## Ventilator Waveform Lab — historical P1 reports

These defects are **Confirmed from project history**, and current production source contains explicit implementation/regression evidence that addresses them. Because the current suites were not executed in this audit, the disposition is **Resolved in current source; runtime re-execution required**, not a fresh passing validation result.

### VENT-P1-001 — Double-trigger triple stacking / minute ventilation

- Historical priority: P1
- Current source disposition: **Resolved in current source; runtime re-execution required**
- Evidence: `tests/ventilator-session352.test.mjs` requires exactly two-breath stacked clusters, rejects three-breath clusters, and verifies minute ventilation over the declared completed-breath interval.
- Remaining action: execute the regression at a recorded source ref. Also add this file to the canonical test baseline.

### VENT-P1-002 — Dynamic compliance during patient effort

- Historical priority: P1
- Current source disposition: **Resolved in current source; runtime re-execution required**
- Evidence: dedicated regression requires passive dynamic-compliance estimation and contaminated/null output with explanatory reason for effort/leak-related scenarios.
- Remaining action: execute the regression and confirm the UI communicates validity status as intended in a browser review.

### VENT-P1-003 — Historical VC data relabeled as PC after mode change

- Historical priority: P1
- Current source disposition: **Resolved in current source; runtime re-execution required**
- Evidence: `LiveVentilatorSession` stores per-breath configuration provenance; regression coverage exercises VC→PC→VC transitions and retained provenance.
- Remaining action: execute regression and visually inspect historical-breath labeling in the production UI.

### VENT-P1-004 — Expiratory hold not reschedulable after breath 3

- Historical priority: P1
- Current source disposition: **Resolved in current source; runtime re-execution required**
- Evidence: hold state dynamically targets the next breath and supports arm/repeat/cancel/invalid states; regression coverage repeats holds after arbitrary breath numbers.
- Remaining action: execute regression and browser-check control behavior.

## Shock / Oxygen Transport — reconciled state

### SHOCK-VERIFY-001 — Prior reduced-circulation-model reconciliation claim

- Evidence basis: **Verified against production repository**
- Lifecycle: **Historical / superseded at baseline ref**
- Current source: `ShockInteractiveLabSlot.tsx` explicitly states that the interactive Shock/Oxygen Transport lab is not implemented and is an integration boundary only.
- Disposition: there is no current reduced circulation engine to compare with the intended broader model at `a0495e9...`.

### SHOCK-PLAN-001 — Intended oxygen-transport simulation remains unimplemented

- Evidence basis: **Verified against production repository**
- Lifecycle: **Planned work**, not a defect
- Current source boundary: future concepts name circulating blood, cardiac output, oxygen delivery/extraction, SvO2/DO2/VO2, tissue reserve, and oxygen debt, while explicitly stating that no synthetic patient, pressure trace, cardiac-output model, treatment response, or simulation runs.
- Guardrail: do not claim Hb→CaO2→DO2→VO2→CvO2/SvO2 coupling, conservation, or numerical stability until an actual engine is implemented and reviewed.

## Interactive Equipment / 3D — verification concerns

### EQUIP-VERIFY-001 — External Shiley-style 3D work is not production-integrated

- Evidence basis: **Verified against production repository** plus Confirmed from project history
- Lifecycle: **Planned/integration work; mechanical verification still outstanding**
- Current production state: the tracheostomy equipment lesson uses a static equipment photograph with HTML hotspots. No Shiley-specific GLB/runtime/snap-lock implementation was identified in the production tree.
- Historical Blender/model work must not be described as deployed until deliberately integrated or separately version-controlled.

### 3D-VERIFY-001 — Chest-trauma 3D source contracts exist but current browser/mechanical validation is not executed

- Evidence basis: **Verified against production repository**
- Lifecycle: **Needs runtime/mechanical verification**
- Current production state: integrated Three.js/R3F chest-trauma module with desktop/mobile GLBs, morph targets, anatomical registration, source-controlled model-contract tests, and license/attribution records.
- Remaining action: execute model tests and perform browser visual/mechanical review for clipping, progression, controls, responsive behavior, reduced motion, and performance.

## Clinical and accessibility validation gaps

These are not automatically software defects.

- Source references and educational boundaries exist across major clinical modules, but no current end-to-end independent clinical-validation artifact was established for the baseline ref.
- ECG/ACLS, PFT, Shock and 3D code contain accessibility-oriented semantics/keyboard/reduced-motion behaviors and related tests, but no comprehensive current WCAG/manual assistive-technology report was identified.
- ABG, medication and equipment content have no dedicated test files identified in the current test inventory.

## Defect-state rule

A source-level fix plus a regression-test file is strong evidence of a resolved implementation path, but it is not equivalent to a freshly executed passing result. Historical defects above should only become **Verified resolved** after the relevant tests/runtime behavior are executed against a recorded production ref.
