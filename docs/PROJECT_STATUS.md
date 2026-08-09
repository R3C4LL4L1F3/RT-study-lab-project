# Project Status

## Purpose

This document records current RT Study Lab project state while keeping project-control facts, production-source facts, executable validation evidence, deployment evidence, and historical claims distinct.

## Overall state

**Stable, but not yet release-mature.**

No current **P0** work item is established by MASTER PROJECT CONTROL.

Current project emphasis is:

1. make the project-control baseline durable;
2. close existing Tier 3 validation;
3. establish independent clinical-validation capability;
4. strengthen production/release governance;
5. specify the Interactive Models & Simulation Lab architecture/model contract before any reusable physiology implementation;
6. defer broad Tier 3 expansion until the reusable framework proves stable.

## Current repository state

### Project-control repository

- Repository: `R3C4LL4L1F3/RT-study-lab-project`
- Default branch: `main`
- Foundation branch: `setup/project-control-foundation`
- PR #1: open review vehicle for the durable foundation; merge requires explicit maintainer authorization
- Current project-control issues in active/future queue include #3, #5, #8, #9, #10, #11 and #12

### Production repository

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility: Private
- Default branch: `main`
- Current ref: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Commit: `Run production validation on main pushes (#2)`
- Automatic `Production Validation` on current `main`: **PASS** — Actions run `31311314980`
- Open production PRs: none at synchronization inspection
- Open production issues: none at synchronization inspection
- `main` branch protection: **not enabled**
- Git tags: none
- GitHub Releases: none

Green production CI does not establish clinical validation, comprehensive accessibility validation, manual 3D/browser validation, or live deployment equivalence.

## Deployment correspondence

Issue #8 tracks the unresolved source-to-live ChatGPT Sites correspondence.

Source-side linkage is verified, but the Git commit associated with the active Sites deployment remains **unknown pending authoritative private Sites saved/deployed-version metadata**.

Current status: **BLOCKED**.

Do not infer the live ref from GitHub `main`, commit dates, or the existence of `.openai/hosting.json`. Do not redeploy merely to manufacture correlation evidence.

## Major workstream status

| Workstream | Current production / record state | Queue state |
|---|---|---|
| ECG / ACLS Lab | Implemented; substantial source-controlled tests pass | **P1 APPROVED** for independent contemporary clinical validation; no fix branch unless validation finds a discrepancy |
| Ventilator Waveform Lab | Implemented; historical-P1 automated regression evidence passes | **P1 IN VALIDATION** under #3 for browser/manual closure; independent clinical validation is also P1 approved |
| Interactive Models & Simulation Lab — Shock / Circulation / O₂ | Shock learning page exists; no numerical physiology framework/simulation is implemented | **P1 APPROVED FOR SPECIFICATION** under #9; implementation not approved |
| 3D Equipment Lab — chest-trauma 3D | Integrated; automated model/source contracts pass | **P2 IN VALIDATION** under #5 for runtime/manual QA |
| Clinical-validation framework | No repeatable independent project-wide baseline completed | **P2 APPROVED** under #10 |
| Accessibility-validation framework | Accessibility-adjacent implementation/tests exist; no comprehensive current baseline | **P2 APPROVED** under #11 |
| Production branch/release controls | CI green; `main` unprotected; no tags/releases | **P2 APPROVED / EXECUTION DEFERRED** under #12 |
| Deployment-to-Git correspondence | Source-side mechanism known; deployed SHA unknown | **P2 High BLOCKED** under #8 |
| PFT | Implemented; loop-data test passes | No current defect record; independent clinical review remains separate |
| ABG | 25-case learning lab implemented | Missing dedicated automated coverage remains P2 queue candidate |
| Respiratory pharmacology | Structured monographs/source registry implemented | Dedicated automated coverage and independent clinical review remain incomplete |
| Equipment catalog | Image/HTML interactive lessons implemented | Dedicated catalog automated coverage not established; historical Shiley 3D is not production-integrated |

## Interactive Models ownership change

Active project routing now uses:

**Interactive Models & Simulation Lab — Shock / Circulation**

for Shock-related forward planning/specification.

The prior standalone Shock circulation-simulator chat terminology may remain in historical chronology where needed. Ventilator Waveform Lab, ECG & ACLS Lab, and 3D Equipment Lab remain separate subsystem owners.

## Canonical priority state

### P0

None currently established.

### P1

- ECG/ACLS independent clinical validation — **APPROVED**
- Ventilator browser/manual historical-P1 closure — **IN VALIDATION**, Issue #3
- Ventilator independent clinical validation — **APPROVED**
- Interactive Models architecture/model contract — **APPROVED FOR SPECIFICATION**, Issue #9; implementation not approved

### P2

- project-control foundation — **ACTIVE** through PR #1
- production branch-control policy — **APPROVED / DEFERRED EXECUTION**, Issue #12
- deployment correspondence — **BLOCKED**, Issue #8
- release/tag convention — **APPROVED / BLOCKED BY #8**, Issue #12
- chest-trauma 3D manual QA — **IN VALIDATION**, Issue #5
- clinical-validation framework — **APPROVED**, Issue #10
- accessibility-validation framework — **APPROVED**, Issue #11
- missing module test coverage — **DEFERRED**
- pnpm artifact investigation — **DEFERRED**
- design-system durable record — **DEFERRED**
- production README modernization — **DEFERRED**
- validation-branch lifecycle cleanup — **DEFERRED / cleanup candidates only**

### P3

Framework-dependent content/model expansion. No broad Interactive Models production expansion is authorized before the approved clinical/model and architecture gates are satisfied.

## Existing issue disposition

- #3 — Ventilator historical-P1 browser/manual closure: **open / IN VALIDATION**
- #5 — chest-trauma 3D runtime/manual verification: **open / IN VALIDATION**
- #8 — deployment-to-Git correspondence: **open / BLOCKED**
- #9 — Interactive Models architecture/model contract: **open / APPROVED FOR SPECIFICATION**
- #10 — independent clinical-validation framework: **open / APPROVED**
- #11 — accessibility-validation baseline: **open / APPROVED**
- #12 — production branch/release control policy: **open / APPROVED, execution deferred**

Closed Issue #4 remains the historical Shock reconciliation record and should not be reopened merely to represent future Interactive Models architecture work.

## Immediate next operational task

Once the project-control foundation is approved for merge and made durable on project-control `main`, the next operational owner is normally:

**QA — Regression & Release**
→ complete Ventilator browser/manual historical-P1 verification under Issue #3.

If new repository evidence materially changes the state before that handoff, return to MASTER PROJECT CONTROL rather than silently reprioritizing.
