# Known Issues and Verification Concerns

This register separates current production/repository risks from historical defect reports, planned work, and remaining verification. Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Repository/control records

### PC-001 — Complete production validation path was previously absent from `main`

- Severity: Historical High
- Evidence basis: **Verified against production repository / GitHub Actions**
- Lifecycle: **Resolved repository-control gap; historical context preserved**
- Original baseline: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Validation branch/ref: `validation/issue-6-test-baseline` at `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Production PR: `R3C4LL4L1F3/RT-study-lab#1` — merged
- Merged production ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Historical finding: production `main` originally used a fixed five-file `npm test` path.
- Resolution: Issue #6 established the complete recursive `tests/**/*.test.mjs` validation path, locked npm install, lint, build, dedicated Ventilator P1 regression and diagnostic artifact upload.
- Current state: the complete validation path is on production `main` and remains part of the automatic production workflow.

### PC-002 — GitHub CI was previously not automatic on production `main`

- Severity: Historical High
- Evidence basis: **Verified against production repository / GitHub Actions**
- Lifecycle: **Resolved repository-control gap; historical context preserved**
- Historical finding: the original production baseline had no source-controlled validation workflow and the first validation workflow did not yet run automatically after `main` pushes.
- Resolution: production PR #1 added `Production Validation`; production PR #2 added automatic `main` push/merge validation.
- Current production ref: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Current automatic validation evidence: Actions run `31311314980` — **PASS** for locked install, lint, build, complete source-controlled suite, dedicated Ventilator P1 regression and diagnostic artifact upload.
- Current state: **production CI is green and automatic on `main`**.

### PC-003 — Live ChatGPT Sites deployment correspondence remains unverified — Issue #8

- Priority: P2 High
- Risk: Tier 1
- Evidence basis: Project-control verified + production-source verified boundary
- Lifecycle: **Current verification gap / BLOCKED**
- Finding: GitHub source and source-controlled Sites/Vinext integration are known, but no authoritative evidence yet proves which Git commit corresponds to the active live ChatGPT Sites deployment.
- Blocker: private Sites saved/deployed-version metadata.
- Impact: a passing GitHub commit cannot automatically be called the validated live deployment.
- Resolution target: complete Issue #8 without redeploying merely to manufacture evidence.

### PC-004 — npm/pnpm repository artifacts require a deployment-aware cleanup decision

- Priority: P2
- Severity: Medium
- Evidence basis: **Verified against production repository**
- Lifecycle: Current repository-hygiene concern / **DEFERRED**
- Finding: npm + maintained `package-lock.json` is the canonical reproducible repository-validation path. `pnpm-lock.yaml` and `pnpm-workspace.yaml` remain because their role in ChatGPT Sites/Vinext has not been proven safe to remove.
- Resolution target: investigate platform/deployment requirements first.
- Execution boundary: do not delete, regenerate or rewrite pnpm artifacts during unrelated work.

### PC-005 — Production README remains largely starter-oriented

- Priority: P2
- Severity: Low
- Evidence basis: **Verified against production repository**
- Lifecycle: Planned documentation improvement / **DEFERRED**
- Finding: production testing documentation is improved, but the production README still primarily presents a Vinext starter rather than the full RT Study Lab architecture.
- Resolution target: focused production documentation change after higher-order validation/governance work.

### PC-006 — Production `main` is not branch-protected

- Priority: P2 High
- Risk: Tier 1
- Evidence basis: **Verified against GitHub repository state**
- Lifecycle: Current repository-governance gap; approved policy work under Issue #12
- Current state: automatic CI is green, but `main` reports `protected: false`.
- Execution boundary: branch protection is **not authorized for execution during the project-control synchronization pass**.
- Resolution target: define/review the production branch-control policy under Issue #12, then execute at its approved sequence point.

### PC-007 — No production Git tag / GitHub Release convention is active

- Priority: P2
- Risk: Tier 1
- Evidence basis: **Verified against GitHub repository state**
- Lifecycle: Planned release-governance work under Issue #12
- Current state: no Git tags and no GitHub Releases exist in the production repository.
- Dependency: Issue #8 must establish authoritative deployment-to-Git correspondence before a release/tag record can reliably identify the live release.
- Execution boundary: do not create a tag or GitHub Release merely to fill this gap.

## Ventilator Waveform Lab — historical P1 reports

Issue #3 is the active validation record. These historical reports originated as **Confirmed from project history** and now have source-level and executable automated regression evidence supporting resolution at that layer. Browser/manual learner-facing verification remains open.

### VENT-P1-001 — Double-trigger / unintended triple stacking and minute ventilation

- Historical priority: P1
- Current evidence: implementation + `tests/ventilator-session352.test.mjs`
- Automated disposition: **Resolved at source/regression layer; browser/manual verification remains**
- Remaining validation: confirm learner-facing double-trigger stacking and minute-ventilation behavior in browser under Issue #3.

### VENT-P1-002 — Dynamic compliance during patient effort

- Historical priority: P1
- Current evidence: validity-aware implementation and regression coverage for passive vs effort/leak-contaminated measurements
- Automated disposition: **Resolved at source/regression layer; browser/manual verification remains**
- Remaining validation: confirm invalid/contaminated messaging and presentation in browser.

### VENT-P1-003 — Historical VC/PC breath relabeling

- Historical priority: P1
- Current evidence: per-breath configuration provenance + transition regression coverage
- Automated disposition: **Resolved at source/regression layer; browser/manual verification remains**

### VENT-P1-004 — Expiratory-hold scheduling/rescheduling

- Historical priority: P1
- Current evidence: dynamic next-breath targeting + repeat/complete/cancel/invalid-state regression coverage
- Automated disposition: **Resolved at source/regression layer; browser/manual verification remains**

**Do not create a Ventilator production fix branch solely because Issue #3 remains open.** A current defect must be reproduced during manual/runtime validation first.

## Interactive Models & Simulation Lab

### IM-PLAN-001 — Reusable model contract + Shock / Circulation / Oxygen Transport foundation — Issue #9

- Priority: P1
- Risk: Tier 3
- Subsystem: **Interactive Models & Simulation Lab**
- Model/feature: reusable model contract + Shock / Circulation / Oxygen Transport foundation
- Owning chat: Planning / Architecture
- Lifecycle: **Approved for specification; implementation not approved**
- Dependency: approved clinical model contract
- Current production state: Shock learning page exists, but **no numerical physiology framework or Shock/Oxygen Transport simulation is implemented**.
- Historical disposition: closed Issue #4 remains the reconciliation record establishing that the former reduced-circulation concern is superseded at current production source.
- Mandatory gate: clinical evidence/model definition → architecture/model contract → reusable framework implementation → first Shock/O₂ validation → later model expansion.
- Execution boundary: no Interactive Models production implementation branch until the clinical contract and architecture decision are approved.

Future V/Q, gas-exchange, pulmonary-circulation, PE physiology, ARDS physiology, heart-failure physiology and similar models remain framework-dependent/deferred.

## 3D Equipment Lab

### EQUIP-VERIFY-001 — Chest-trauma 3D browser/mechanical/visual validation remains incomplete — Issue #5

- Priority: P2
- Risk: Tier 2
- Evidence basis: **Verified against production repository** for implementation and automated source/model contracts
- Lifecycle: **IN VALIDATION**
- Current implementation: integrated R3F/Drei/Three.js chest-trauma 3D module with desktop/mobile GLBs, morph targets, geometry-derived runtime landmarks, lazy/opt-in boundary, and source-controlled license/provenance records.
- Automated evidence: chest-trauma source/model/visual tests pass in the canonical production suite.
- Remaining verification:
  - browser clipping and self/intersection review
  - morph/progression visual review
  - camera/control behavior
  - responsive/mobile behavior
  - reduced-motion behavior
  - runtime performance/stability
  - educational/anatomical visual fidelity review
- Execution boundary: do not create a production fix branch until manual/runtime QA establishes a current defect.

### EQUIP-VERIFY-002 — Historical Shiley 3D work is not production-integrated

- Evidence basis: production repository + project history
- Lifecycle: Historical external work / planned integration only if later approved
- Current state: production tracheostomy lesson is a static equipment photograph with HTML hotspots. No Shiley-specific GLB, snap-lock runtime interaction, or 3D tracheostomy animation is in production.
- Requirement before future integration: version-control source model/assets, provenance/license, snap-lock acceptance criteria, animation/mechanical review evidence, and browser-runtime plan.

## Cross-project validation gaps

These are validation gaps, not confirmed defects:

- independent contemporary ECG/ACLS clinical validation — P1 approved;
- independent Ventilator clinical validation — P1 approved;
- repeatable project-wide clinical-validation framework — Issue #10, P2 approved;
- comprehensive accessibility-validation baseline — Issue #11, P2 approved;
- manual Ventilator learner-facing browser verification — Issue #3;
- manual chest-trauma 3D runtime/mechanical/visual review — Issue #5;
- live ChatGPT Sites deployment equivalence — Issue #8;
- dedicated automated coverage for ABG, medication content, equipment catalog and comprehensive generic disease records — P2 deferred candidates.

Passing production CI must not be substituted for any of these evidence layers.
