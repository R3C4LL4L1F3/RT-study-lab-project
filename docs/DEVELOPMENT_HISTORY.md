# Development History

This history preserves the sequence of major RT Study Lab work while distinguishing project-history claims from production-verified milestones.

Unless explicitly promoted by current evidence, older application-development entries remain **Confirmed from project history** rather than current production claims.

## Development sequence

| Area | Milestone / record | Evidence basis |
|---|---|---|
| Ventilator Waveform Lab | Continuous A/C VC and PC waveform lab with historical breath navigation, playback/window controls, annotations and selected-breath details | Confirmed from project history; current implementation later verified against production source |
| Ventilator Waveform Lab | Session 3.5 audit identified historical concerns affecting double triggering/minute ventilation, dynamic compliance during effort, historical mode labeling and expiratory-hold scheduling | Confirmed from project history |
| ECG Rhythm Lab | Initial rhythm-learning engine with Learn Mode, ECG measurement controls, calibration and core rhythm library | Confirmed from project history; current architecture later verified against production source |
| ECG Rhythm Lab | Rhythm library expanded with ectopy, SVT, polymorphic VT, torsades and additional practice behavior | Confirmed from project history |
| ECG Rhythm Lab | Phase 1 refinement improved measurement references, calipers, long-window behavior, rhythm-specific controls and accessibility/performance behavior | Confirmed from project history |
| ECG Rhythm Lab | Optional ECG landmark snapping added for measurement workflows | Confirmed from project history |
| ECG / ACLS | Independent patient-state engine reported for pulse, perfusion, breathing, mental status, shock, heart failure, arrest and pathway state | Confirmed from project history; architecture verified in production source |
| ECG / ACLS | Clinical Practice and Examination modes reported with seeded cases, scoring, timing, review and local history | Confirmed from project history; corresponding current source verified |
| ECG / ACLS | Guideline/pathway engine reported separately from waveform and patient-state engines | Confirmed from project history; current separate pathway source verified |
| ECG / ACLS | Treatment engine reported with medication/electrical actions, reassessment, deterministic state transitions, timeline replay and sequence-aware scoring | Confirmed from project history; current separate treatment source verified |
| Shock / Oxygen Transport | Project history identified a need to reconcile a reduced circulation implementation with a broader oxygen-transport model | Confirmed from project history; **Historical / superseded** because current production has no Shock numerical physiology simulation |
| Interactive Equipment | Macintosh laryngoscope modeling/refinement workflow established | Confirmed from project history; not production-integrated at current ref |
| Interactive Equipment | Shiley-style cuffed tracheostomy model developed with modular outer cannula, removable inner cannula, obturator, cuff/pilot-line and iterative animation/model revisions | Confirmed from project history; not production-integrated at current ref |
| Project control | Dedicated GitHub project-control repository initialized | Project-control verified |
| Project control | `setup/project-control-foundation` branch created and project-control PR #1 opened | Project-control verified |
| Project control | Project-control PR #1 merged into `main`; the historical foundation milestone is represented by issue #34 | Verified current project-control history; historical milestone, not active work |
| Project control | Evidence/lifecycle vocabulary and production-verification framework established | Project-control verified |
| Production source | Existing RT Study Lab Git repository recovered and preserved in private GitHub repository `R3C4LL4L1F3/RT-study-lab` without replacing its existing Sites remote | Verified against production repository / migration evidence |
| Production verification | Baseline production source established at `a0495e9fa4e5437d8a027312b618b5c1c389ef94` (`Redesign Shock visual teaching page`) | Verified against production repository |
| Production verification | ECG/ACLS, Ventilator, Shock, equipment/chest-trauma 3D, PFT, ABG, disease and medication modules mapped against source | Verified against production repository |
| Production verification | Shock future lab confirmed as an explicit nonimplemented integration boundary; historical reduced-circulation reconciliation concern superseded | Verified against production repository |
| Production verification | Historical Shiley Blender model confirmed not production-integrated; chest-trauma 3D identified as current integrated Three.js/R3F implementation | Verified against production repository |
| Project control | Issues #2–#5 established the initial production-verification backlog; #2 and #4 later closed after their verification questions were answered | Project-control verified |
| Validation / Issue #6 | Production branch `validation/issue-6-test-baseline` and production PR #1 created from baseline `main` for validation/configuration changes | Verified against production repository/GitHub |
| Validation / Issue #6 | npm selected as canonical reproducible validation package manager; maintained `package-lock.json` used for CI while pnpm artifacts retained pending Sites/Vinext verification | Verified against production repository; project decision recorded |
| Validation / Issue #6 | Canonical `npm test` redesigned to build then recursively execute the complete `tests/**/*.test.mjs` inventory instead of a fixed five-file subset | Verified against production source/PR |
| Validation / Issue #6 | Initial CI investigation exposed Node 22.13 direct `.ts` import failures (`ERR_UNKNOWN_FILE_EXTENSION`); validation runner updated to use `--experimental-strip-types` without changing application behavior | Verified against GitHub Actions and production PR |
| Validation / Issue #6 | Final PR ref `96b5535f9228c7b01c709386e050ce53e68f14d4` passed locked install, lint, build, complete 28-file suite, dedicated Ventilator P1 regression and diagnostic artifact upload in run `31309995943` | Verified executable automated evidence |
| Validation / Issue #6 | Production PR #1 merged as `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`; exact-commit validation run `31310610948` passed | Verified against production GitHub/Actions |
| Validation / Issue #7 | Production PR #2 added automatic validation after pushes/merges to `main` without application/clinical/deployment behavior changes | Verified against production PR |
| Validation / Issue #7 | Production `main` advanced to `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`; automatic run `31311314980` passed | Verified against production GitHub/Actions |
| Ventilator verification | Historical P1 concerns have passing automated regression evidence on current production validation; learner-facing browser/manual verification remains under Issue #3 | Verified automated evidence; runtime/browser verification open |
| Chest-trauma 3D verification | Chest-trauma 3D source/model/visual contract tests pass in canonical production validation; manual visual/mechanical/runtime review remains under Issue #5 | Verified automated evidence; manual verification open |
| Deployment verification | Issue #8 established the source-side Sites linkage/deployment evidence model; active deployed Git ref remains blocked on authoritative Sites version metadata | Project-control + production-source verified boundary |
| Project structure | Active standalone Shock circulation-simulator chat ownership replaced by **Interactive Models & Simulation Lab — Shock / Circulation** for forward work; historical terminology preserved in chronology | Approved MASTER PROJECT CONTROL policy |
| Project control | Issue #9 created for the reusable Interactive Models architecture/model contract; specification approved, implementation not approved | Project-control verified |
| Project control | Issue #10 created for independent clinical-validation framework; initial P1 module validation begins with ECG/ACLS and Ventilator | Project-control verified |
| Project control | Issue #11 created for project-wide accessibility-validation baseline | Project-control verified |
| Project control | Issue #12 created for future production branch/release control policy; execution explicitly deferred | Project-control verified |

## Current merge / execution boundary

Production validation infrastructure is **merged and green on current production `main`** at `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`.

Project-control PR #1 is the historical foundation review vehicle and is merged into project-control `main`. The current verified `main` ref at the Phase 2 synchronization baseline is `53c5f1aebb52fc69e721fd9276d8668c0b8fdd71` after PR #33; issue #34 records the foundation milestone. Phase 2 records are carried on a purpose-specific branch and reviewed by a separate pull request.

Later approved work recorded in the queue does not authorize premature execution. In particular, project-control synchronization does not authorize:

- production branch-protection changes;
- production Git tags or GitHub Releases;
- Interactive Models implementation branches/code;
- Ventilator/ECG/3D fix branches without a demonstrated current discrepancy;
- deletion of completed validation branches;
- pnpm artifact deletion/modification;
- deployment/republication.

## History policy

Future entries should include, when available:

- date or release identifier established by evidence;
- production repository path and commit/pull request;
- deployment reference;
- validation/test reference;
- regressions introduced or resolved;
- evidence basis;
- lifecycle/disposition;
- queue status/ownership where material;
- explicit distinction between automated, clinical, accessibility, deployment and manual visual/mechanical evidence.

Do not assign precise dates, versions, implementation states, resolution states or architecture details retrospectively unless a source establishes them.
