# Master Project Queue

This document is the durable project-control queue approved by MASTER PROJECT CONTROL for the current RT Study Lab engineering state.

It records approved sequencing, priority, ownership, dependencies and execution gates. **Recording a future item does not authorize executing it before its sequence/dependency gates are satisfied.**

## Canonical execution sequence

1. **Durable project-control baseline**
2. **Close existing Tier 3 validation**
3. **Establish independent clinical validation**
4. **Strengthen production/release controls**
5. **Specify Interactive Models architecture**
6. **Implement the first validated reusable physiology model**
7. **Expand only after the framework proves stable**

## Queue status vocabulary

- **ACTIVE** — currently being executed in the approved sequence.
- **APPROVED** — approved and durable, but execution may still be waiting on sequence/dependencies.
- **IN VALIDATION** — implementation/evidence exists; a defined validation layer remains open.
- **BLOCKED** — an explicit dependency/evidence source prevents completion.
- **DEFERRED** — intentionally held until a preceding gate is satisfied.

## P0

**None currently established.**

## P1

| Item | Risk | Subsystem | Model / feature | Owning chat | Status | Dependency / gate |
|---|---|---|---|---|---|---|
| ECG/ACLS independent clinical validation | Tier 3 | ECG / ACLS Lab | Current guideline-sensitive ECG/ACLS behavior | Clinical Validation & Sources | **APPROVED** | Independent clinical-validation method + authoritative source set; no code fix unless discrepancy is established |
| Ventilator browser/manual historical-P1 closure — #3 | Tier 3 | Ventilator Waveform Lab | Browser/manual regression closure | QA — Regression & Release | **IN VALIDATION** | Runtime/browser access; manual pass or reproducible current defect |
| Ventilator independent clinical validation | Tier 3 | Ventilator Waveform Lab | Mechanics/measurement/effort/asynchrony teaching assumptions | Clinical Validation & Sources | **APPROVED** | Independent clinical-validation method + source set; no code fix unless discrepancy is established |
| Interactive Models architecture/model contract — #9 | Tier 3 | Interactive Models & Simulation Lab | Reusable model contract + Shock / Circulation / Oxygen Transport foundation | Planning / Architecture | **APPROVED FOR SPECIFICATION — IMPLEMENTATION NOT APPROVED** | Approved clinical/model contract + reviewed architecture decision |

## P2

| Item | Priority detail | Risk | Owning chat / area | Status | Execution boundary |
|---|---|---|---|---|---|
| Project-control foundation — PR #1 | P2 High | Tier 0 | GitHub — PR / Documentation | **ACTIVE** | Merge requires explicit maintainer authorization |
| Production branch-control policy — #12 | P2 High | Tier 1 | GitHub — PR / Documentation | **APPROVED / DEFERRED EXECUTION** | Do not change branch protection during synchronization |
| Deployment-to-Git correspondence — #8 | P2 High | Tier 1 | Site / Platform | **BLOCKED** | Requires authoritative private Sites saved/deployed-version metadata |
| Release/tag convention — #12 | P2 | Tier 1 | GitHub — PR / Documentation + Site / Platform | **APPROVED / BLOCKED BY #8** | Do not create a tag or GitHub Release yet |
| Chest-trauma 3D manual/runtime QA — #5 | P2 | Tier 2 | QA — Regression & Release + 3D Equipment Lab | **IN VALIDATION** | Do not create fix branch without reproduced current defect |
| Clinical-validation framework — #10 | P2 | Tier 3 | Clinical Validation & Sources | **APPROVED** | Initial module-specific P1 validation begins with ECG/ACLS and Ventilator |
| Accessibility-validation framework — #11 | P2 | Tier 1 | Design System & UI/UX | **APPROVED** | Manual/keyboard/AT protocol required; no redesign implied by issue creation |
| Missing module automated coverage | P2 | Up to Tier 3 by module | QA — Regression & Release + subsystem owner | **DEFERRED** | Gaps are not defects; add targeted tests only through approved work |
| pnpm artifact investigation — PC-004 | P2 | Tier 1 | Site / Platform + GitHub | **DEFERRED** | Do not delete/regenerate pnpm files without Sites/Vinext evidence |
| Design-system durable record | P2 | Tier 1 | Design System & UI/UX | **DEFERRED** | Record architecture after higher-order validation/control work as sequenced |
| Production README modernization — PC-005 | P2 | Tier 0 | GitHub — PR / Documentation | **DEFERRED** | Do not rewrite production README during this synchronization pass |
| Validation-branch lifecycle cleanup | P2 | Tier 0 | GitHub — PR / Documentation | **DEFERRED / cleanup candidates only** | Do not delete retained validation branches during synchronization |

## P3

**Framework-dependent product/content/model expansion.**

P3 Interactive Models expansion is gated by successful completion of the clinical/model definition, reusable architecture, first framework implementation and first Shock/O₂ validation.

Future model classes already represented by approved project context include:

- V/Q relationships;
- gas exchange;
- pulmonary circulation;
- pulmonary embolism physiology;
- ARDS physiology;
- heart-failure physiology;
- related physiology/pathophysiology models that fit the Interactive Models ownership definition.

These are **not** individually authorized implementation tasks. Do not create a speculative large model backlog until the framework proves stable.

## Interactive Models & Simulation Lab gate

Forward Shock ownership is:

**Interactive Models & Simulation Lab — Shock / Circulation**

Historical references to the former standalone Shock circulation-simulator chat may remain for chronology.

The following specialized persistent owners remain separate:

- Ventilator — Waveform Lab;
- ECG & ACLS Lab;
- 3D Equipment Lab.

### Required dependency chain

**Clinical evidence/model definition**
→ **Interactive Models architecture/model contract**
→ **reusable framework implementation**
→ **Shock / Circulation / Oxygen Transport first-model validation**
→ **additional physiology models**

### Mandatory implementation gate

Do **not** begin production Interactive Models implementation until:

- the clinical/model contract is approved;
- the reusable architecture/model contract is approved;
- deterministic cases are defined;
- invariants are defined;
- boundary behavior is defined;
- long-run expectations are defined;
- reset/replay behavior is defined;
- seed/reproducibility behavior is defined;
- serialization/snapshot expectations are defined;
- independent review has occurred.

Issue #9 is a specification/architecture record, not implementation authorization.

## Existing validation issues to reuse

- **#3 — Ventilator historical-P1 browser/manual closure:** P1, Tier 3, IN VALIDATION.
- **#5 — Chest-trauma 3D runtime/manual verification:** P2, Tier 2, IN VALIDATION.
- **#8 — Deployment-to-Git correspondence:** P2 High, Tier 1, BLOCKED.

Do not create duplicate records for these scopes.

## New reusable project-control records

- **#9 — Establish Interactive Models & Simulation Lab architecture/model contract:** P1, Tier 3, APPROVED FOR SPECIFICATION; implementation not approved.
- **#10 — Establish independent clinical-validation framework:** P2, Tier 3, APPROVED.
- **#11 — Establish accessibility-validation baseline:** P2, Tier 1, APPROVED.
- **#12 — Define production branch and release control policy:** P2 High, Tier 1, APPROVED POLICY WORK; execution deferred.

## Explicit future actions recorded but not authorized for execution in the synchronization pass

Do not prematurely execute:

- production branch-protection changes;
- production Git tag creation;
- GitHub Release creation;
- site deployment/republication;
- `feature/interactive-models-core` or equivalent production implementation branch creation;
- Ventilator production fixes without a manual reproduced defect;
- ECG/ACLS production fixes without a clinical-validation discrepancy;
- 3D production fixes without manual/runtime defect evidence;
- deletion of `validation/issue-6-test-baseline`;
- deletion of `validation/issue-7-main-push`;
- deletion of `validation/post-merge-main-verification`;
- pnpm artifact deletion/modification;
- production README modernization during this synchronization pass.

## Next operational owner after project-control baseline merge

Unless new repository evidence requires MASTER PROJECT CONTROL reconsideration:

**QA — Regression & Release**
→ **Issue #3 — Complete Ventilator browser/manual historical-P1 verification**.
