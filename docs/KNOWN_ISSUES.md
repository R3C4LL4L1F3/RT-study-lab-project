# Known Issues and Verification Concerns

This register separates current production/repository risks from historical defect reports and remaining verification work. Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Current repository/control issues

### PC-001 — Complete validation path is not yet on production `main`

- Severity: High
- Evidence basis: **Verified against production repository**
- Lifecycle: Current known repository issue; remediation validated on draft PR
- Baseline production `main`: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Remediation branch: `validation/issue-6-test-baseline`
- Validated remediation ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Production PR: `R3C4LL4L1F3/RT-study-lab#1` (draft, unmerged)
- Finding: production `main` still uses the older fixed five-file `npm test` command. The draft PR replaces that path with recursive discovery/execution of the complete 28-file source-controlled test inventory.
- Validation: GitHub Actions run `31309995943` passed locked install, lint, build, complete suite, and the dedicated Ventilator P1 regression.
- Resolution target: explicit maintainer review/authorization and merge of the validated production PR. Do not describe the new path as present on `main` until merge evidence exists.

### PC-002 — GitHub CI is validated on a draft PR but not yet established on production `main`

- Severity: High
- Evidence basis: **Verified against production repository / GitHub Actions**
- Lifecycle: Current known repository issue; remediation validated on draft PR
- Finding: baseline `main` had no `.github/workflows` validation workflow. Production PR #1 adds a conservative read-only-source validation workflow with no deployment credentials.
- Validated checks: `npm ci`, lint, build, complete tests, dedicated Ventilator P1 regression, diagnostic artifact upload.
- Resolution target: merge the validated production PR only after explicit maintainer authorization.

### PC-003 — Live ChatGPT Sites deployment correspondence remains unverified

- Severity: High
- Evidence basis: Project-control verified + production-source verified boundary
- Lifecycle: Current known verification gap
- Finding: GitHub source and source-controlled Sites/Vinext/Cloudflare integration are known, but no durable evidence currently proves which GitHub commit corresponds to the live ChatGPT Sites deployment.
- Impact: a passing GitHub PR cannot automatically be called a validated live deployment.
- Resolution target: establish a safe deployment/source synchronization record without exposing internal credentials or private deployment tokens.

### PC-004 — npm/pnpm repository artifacts require a deployment-aware cleanup decision

- Severity: Medium
- Evidence basis: **Verified against production repository**
- Lifecycle: Current known repository-hygiene concern; validation convention resolved
- Finding: Issue #6 established **npm** as the canonical reproducible validation package manager because the maintained `package-lock.json` tracks later production dependencies while `pnpm-lock.yaml` has not tracked those updates.
- Remaining concern: `pnpm-lock.yaml` and `pnpm-workspace.yaml` are retained because their role in ChatGPT Sites/Vinext has not been proven safe to remove.
- Resolution target: do not delete/regenerate pnpm artifacts until the Sites build/deployment contract is verified.

### PC-005 — Production README remains largely starter-oriented

- Severity: Low
- Evidence basis: **Verified against production repository**
- Lifecycle: Planned repository documentation improvement
- Finding: Issue #6 adds testing/validation guidance and links `TESTING.md`, but the production README still primarily describes the Vinext starter rather than the full RT Study Lab architecture.
- Resolution target: update the production README in a separate focused documentation change after the validation PR is settled.

## Ventilator Waveform Lab — historical P1 reports

These records originated as **Confirmed from project history**. Current source plus executable automated regression evidence now supports a stronger disposition, while browser/UI verification remains open.

### VENT-P1-001 — Double-trigger / unintended triple stacking and minute ventilation

- Historical priority: P1
- Current evidence: source implementation + `tests/ventilator-session352.test.mjs`
- Executable evidence: dedicated P1 command and full suite **passed** at production PR ref `96b5535f9228c7b01c709386e050ce53e68f14d4`, Actions run `31309995943`
- Lifecycle: **Resolved in current source with passing automated regression; browser verification remains**
- Remaining verification: confirm learner-facing waveform/history behavior in a browser before closing Issue #3.

### VENT-P1-002 — Dynamic compliance during patient effort

- Historical priority: P1
- Current evidence: validity-aware implementation and regression coverage for passive vs effort/leak-contaminated measurements
- Executable evidence: dedicated P1 command and full suite **passed** at production PR ref `96b5535...`
- Lifecycle: **Resolved in current source with passing automated regression; browser messaging verification remains**
- Remaining verification: confirm contaminated/invalid measurement messaging and interaction presentation in the browser.

### VENT-P1-003 — Historical VC/PC breath relabeling

- Historical priority: P1
- Current evidence: per-breath configuration provenance in `LiveVentilatorSession` plus transition regression coverage
- Executable evidence: **PASS** at production PR ref `96b5535...`
- Lifecycle: **Resolved in current source with passing automated regression; browser history-label verification remains**

### VENT-P1-004 — Expiratory-hold scheduling/rescheduling

- Historical priority: P1
- Current evidence: dynamic next-breath hold targeting and repeat/complete/cancel/invalid-state regression coverage
- Executable evidence: **PASS** at production PR ref `96b5535...`
- Lifecycle: **Resolved in current source with passing automated regression; browser control verification remains**

## Shock / Oxygen Transport

### SHOCK-PLAN-001 — Planned oxygen-transport simulation is not implemented

- Evidence basis: **Verified against production repository**
- Lifecycle: Planned work, not a defect
- Current state: `ShockInteractiveLabSlot.tsx` explicitly defines a simulation-free integration boundary. No synthetic patient, circulation model, pressure trace, cardiac-output engine, treatment response, or Hb→CaO2→DO2→VO2→CvO2/SvO2→extraction→oxygen-debt engine is present.
- Historical disposition: the prior reduced-circulation reconciliation concern is **Historical / superseded** at the baseline source ref.
- Automated evidence: `tests/shock-page.test.mjs` passed as part of Issue #6 full-suite validation at PR ref `96b5535...`.
- Future requirement: any simulation implementation should begin with an explicit clinical/educational model contract and architecture decision rather than assuming a pre-existing circulation engine.

## Interactive Respiratory Equipment / 3D

### EQUIP-VERIFY-001 — Chest-trauma 3D browser/mechanical/visual validation remains incomplete

- Evidence basis: **Verified against production repository** for implementation and automated source/model contracts
- Lifecycle: Current verification concern
- Current implementation: integrated R3F/Drei/Three.js chest-trauma 3D module with desktop/mobile GLBs, morph targets, geometry-derived runtime landmarks, lazy/opt-in boundary, and source-controlled license/provenance records.
- Automated evidence: `tests/chest-trauma-3d.test.mjs` and `tests/chest-trauma-visual.test.mjs` **passed** in the Issue #6 full suite at PR ref `96b5535...`.
- Remaining verification:
  - browser clipping and self/intersection review
  - morph/progression visual review
  - camera/control behavior
  - responsive/mobile behavior
  - reduced-motion behavior
  - runtime performance
  - educational/anatomical visual fidelity review

### EQUIP-VERIFY-002 — Historical Shiley 3D work is not production-integrated

- Evidence basis: production repository + project history
- Lifecycle: Historical external work / planned integration if pursued
- Current state: the production tracheostomy lesson is a static equipment photograph with HTML hotspots. No Shiley-specific GLB, snap-lock runtime interaction, or 3D tracheostomy animation is in the production tree.
- Requirement before future integration: version-control the actual source model/assets, provenance/license, snap-lock acceptance criteria, animation/mechanical review evidence, and browser-runtime plan.

## Evidence boundaries that remain open

Passing Issue #6 CI does **not** establish:

- independent clinical validation;
- comprehensive accessibility/WCAG conformance;
- manual browser verification of Ventilator learner-facing behavior;
- live ChatGPT Sites deployment equivalence;
- manual 3D mechanical/visual fidelity;
- production integration of external Blender/Shiley assets.

Those concerns remain explicit rather than being inferred from automated test results.
