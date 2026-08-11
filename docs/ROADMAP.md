# Roadmap

This roadmap is governed by the approved MASTER PROJECT CONTROL queue. It distinguishes current execution from approved future work and preserves dependency gates.

## Canonical execution sequence

1. **Durable project-control baseline**
2. **Close existing Tier 3 validation**
3. **Establish independent clinical validation**
4. **Strengthen production/release controls**
5. **Specify Interactive Models architecture**
6. **Implement the first validated reusable physiology model**
7. **Expand only after the framework proves stable**

A work item may be recorded before its sequence position is reached. Recording it does **not** authorize implementation or governance changes early.

## Completed production validation foundation

### Issue #6 — Complete production validation path

Completed and merged.

Production `main` contains:

- npm + maintained `package-lock.json` as canonical repository-validation path;
- locked install with `npm ci`;
- lint;
- Vinext production build;
- recursive discovery/execution of all source-controlled `tests/**/*.test.mjs` files;
- dedicated Ventilator historical-P1 regression;
- diagnostic artifact upload;
- GitHub Actions `Production Validation` workflow.

### Issue #7 — Automatic validation after `main` changes

Completed and merged.

Current production `main`:

- `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- `Run production validation on main pushes (#2)`

Automatic `Production Validation` run `31311314980` passed on that exact ref.

## P0

**None currently established.**

Do not promote deployment uncertainty, validation gaps, or planned feature work to P0 without new evidence and MASTER PROJECT CONTROL review.

## P1 — Approved high-value work

### ECG / ACLS independent clinical validation

- Status: **APPROVED**
- Risk: Tier 3
- Owner: Clinical Validation & Sources
- Support: ECG & ACLS Lab; QA — Regression & Release
- Dependency: repeatable clinical-validation method / authoritative source set
- Execution boundary: do not create a production fix branch unless validation establishes an implementation discrepancy.

### Ventilator browser/manual historical-P1 closure — Issue #3

- Status: **IN VALIDATION**
- Risk: Tier 3
- Owner: QA — Regression & Release
- Support: Ventilator — Waveform Lab
- Automated historical-P1 regression evidence is complete and passing.
- Remaining work is learner-facing browser/manual verification.
- A fix branch is not authorized unless manual QA reproduces a current defect.

### Ventilator independent clinical validation

- Status: **APPROVED**
- Risk: Tier 3
- Owner: Clinical Validation & Sources
- Support: Ventilator — Waveform Lab; QA — Regression & Release
- Scope: mechanics, measurement, patient-effort/asynchrony teaching assumptions and other clinically meaningful behavior.
- Automated tests do not satisfy this validation layer.

### Interactive Models architecture/model contract — Issue #9

- Status: **APPROVED FOR SPECIFICATION — IMPLEMENTATION NOT APPROVED**
- Risk: Tier 3
- Subsystem: Interactive Models & Simulation Lab
- Model/feature: reusable model contract + Shock / Circulation / Oxygen Transport foundation
- Owner: Planning / Architecture
- Support: Clinical Validation & Sources; Interactive Models & Simulation Lab; Design System & UI/UX; QA — Regression & Release
- Dependency: approved clinical model contract

#### Mandatory production-expansion gate

**Interactive Models production expansion requires an approved clinical/model contract and an approved reusable simulation architecture.**

Approved dependency chain:

**Clinical evidence/model definition**
→ **Interactive Models architecture/model contract**
→ **reusable framework implementation**
→ **Shock / Circulation / Oxygen Transport first-model validation**
→ **additional physiology models**

Do not create an implementation branch for the reusable Interactive Models core until the clinical contract and architecture decision are approved.

Future V/Q, gas-exchange, pulmonary-circulation, pulmonary-embolism physiology, ARDS physiology, heart-failure physiology and similar models remain **DEFERRED / framework-dependent**. They are not an approved speculative implementation backlog.

#### Three.js 2.5D circulation renderer planning package

- Status: **PROPOSED / SPECIFICATION — IMPLEMENTATION NOT APPROVED**
- Related records: `docs/INTERACTIVE_MODELS_THREEJS_ROADMAP.md`, `docs/INTERACTIVE_MODELS_THREEJS_ARCHITECTURE.md`, `docs/INTERACTIVE_MODELS_THREEJS_VALIDATION_PLAN.md`, `docs/ADR-012-threejs-2-5d-circulation-renderer.md`
- Scope: replace the circulation viewport presentation layer while preserving the deterministic physiology source of truth and accessible fallback.
- Gate: architecture/model contract, clinical teaching specification, asset provenance, independent QA, and validation evidence must pass before production implementation.
- Non-goals: full 3D, new shock categories, medications, interventions, or unreviewed AI-generated anatomy.

## P2 — Governance, validation infrastructure and stabilization

### Project-control foundation — PR #1

- Status: **ACTIVE**
- Risk: Tier 0
- Goal: make the two-repository governance, current production state, canonical queue, architecture decisions and validation boundaries durable on project-control `main`.
- Merge remains subject to explicit maintainer authorization.

### Production branch-control policy — Issue #12

- Status: **APPROVED / EXECUTION DEFERRED**
- Risk: Tier 1
- Current fact: production `main` is not branch-protected.
- Record policy now; do not change branch protection during project-control synchronization.

### Deployment correspondence — Issue #8

- Status: **BLOCKED**
- Priority detail: P2 High
- Risk: Tier 1
- Dependency: authoritative private ChatGPT Sites saved/deployed-version metadata.
- Do not redeploy merely to generate evidence.

### Release/tag convention — Issue #12

- Status: **APPROVED / BLOCKED BY DEPLOYMENT CORRESPONDENCE**
- Risk: Tier 1
- Current fact: production has no Git tags or GitHub Releases.
- Do not create either until deployment-to-Git correspondence and release policy are approved.

### Chest-trauma 3D manual/runtime QA — Issue #5

- Status: **IN VALIDATION**
- Risk: Tier 2
- Owners: QA — Regression & Release; 3D Equipment Lab
- Automated source/model contracts pass; manual/runtime/mechanical/visual review remains.
- Do not create a production fix branch without a reproduced current defect.

### Clinical-validation framework — Issue #10

- Status: **APPROVED**
- Risk: Tier 3
- Owner: Clinical Validation & Sources
- Support: QA — Regression & Release
- Initial module-specific P1 validation begins with ECG/ACLS and Ventilator.

### Accessibility-validation framework — Issue #11

- Status: **APPROVED**
- Risk: Tier 1
- Owner: Design System & UI/UX
- Support: QA — Regression & Release
- Required evidence includes keyboard, focus, semantics, status announcements, responsive behavior, reduced motion where applicable, manual review, and assistive-technology review where practical.

### Missing module automated coverage

- Status: **DEFERRED**
- Current known gaps include dedicated coverage for ABG, medication content, equipment catalog and comprehensive generic disease records.
- Test gaps are not confirmed production defects.

### pnpm artifact investigation — PC-004

- Status: **DEFERRED**
- npm is canonical for repository validation.
- Do not delete or regenerate `pnpm-lock.yaml` / `pnpm-workspace.yaml` until Sites/Vinext platform evidence establishes their role.

### Design-system durable record

- Status: **DEFERRED**
- Current UI/CSS implementation exists across the site, but a durable centralized design-system architecture record remains future work.

### Production README modernization — PC-005

- Status: **DEFERRED**
- The production README remains substantially Vinext-starter oriented.
- Do not rewrite it in this project-control synchronization pass.

### Validation-branch lifecycle cleanup

- Status: **DEFERRED / cleanup candidates only**
- Candidates:
  - `validation/issue-6-test-baseline`
  - `validation/issue-7-main-push`
  - `validation/post-merge-main-verification`
- Do not delete them during synchronization.

## P3 — Framework-dependent expansion

P3 contains product/content/model expansion whose safe implementation depends on the preceding validation/governance/framework work.

For Interactive Models, P3 expansion is explicitly gated by the successful specification, implementation and validation of the reusable framework and first Shock/O₂ model. Do not promote later physiology models into production implementation before that evidence exists.

## Specialized subsystem ownership boundary

Interactive Models & Simulation Lab does **not** absorb:

- Ventilator Waveform Lab mechanics/waveform simulation;
- ECG & ACLS waveform/patient-state/pathway/treatment systems;
- 3D Equipment Lab device geometry/GLB/mechanical interaction.

Forward Shock ownership is **Interactive Models & Simulation Lab — Shock / Circulation**. Historical records may retain older Shock-chat terminology where necessary for chronology.

## Evidence-sensitive claims

Do not claim completion without corresponding evidence for:

- exact live-site deployment synchronization until Issue #8 is complete;
- independent contemporary ECG/ACLS clinical validation;
- independent Ventilator clinical validation;
- comprehensive accessibility validation;
- manual chest-trauma 3D mechanical/visual/runtime validation;
- production integration of historical Shiley Blender work;
- existence of a reusable numerical Interactive Models physiology framework before Issue #9's architecture and subsequent implementation are actually approved and completed.
