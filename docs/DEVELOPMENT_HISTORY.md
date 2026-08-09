# Development History

This history preserves the sequence of major RT Study Lab work while distinguishing project-history claims from production-verified milestones.

Unless explicitly promoted by current evidence, older application-development entries remain **Confirmed from project history** rather than current production claims.

## Development sequence

| Area | Milestone / record | Evidence basis |
|---|---|---|
| Ventilator Waveform Lab | Continuous A/C VC and PC waveform lab with historical breath navigation, playback/window controls, annotations, and selected-breath details | Confirmed from project history; current implementation later verified against production source |
| Ventilator Waveform Lab | Session 3.5 audit identified historical concerns affecting double triggering/minute ventilation, dynamic compliance during effort, historical mode labeling, and expiratory-hold scheduling | Confirmed from project history |
| ECG Rhythm Lab | Initial rhythm-learning engine with Learn Mode, ECG measurement controls, calibration, and core rhythm library | Confirmed from project history; current architecture later verified against production source |
| ECG Rhythm Lab | Rhythm library expanded with ectopy, SVT, polymorphic VT, torsades, and additional practice behavior | Confirmed from project history |
| ECG Rhythm Lab | Final Phase 1 audit refined measurement references, calipers, long-window behavior, rhythm-specific controls, and accessibility/performance behavior | Confirmed from project history |
| ECG Rhythm Lab | Optional ECG landmark snapping added for measurement workflows | Confirmed from project history |
| ECG / ACLS | Independent patient-state engine reported for pulse, perfusion, breathing, mental status, shock, heart failure, arrest, and pathway state | Confirmed from project history; architecture verified in current production source |
| ECG / ACLS | Clinical Practice and Examination modes reported with seeded cases, scoring, timing, review, and local history | Confirmed from project history; corresponding current source verified |
| ECG / ACLS | Guideline/pathway engine reported separately from waveform and patient-state engines | Confirmed from project history; current separate pathway source verified |
| ECG / ACLS | Treatment engine reported with medication/electrical actions, reassessment, deterministic state transitions, timeline replay, and sequence-aware scoring | Confirmed from project history; current separate treatment source verified |
| Shock / Oxygen Transport | Project history identified a need to reconcile a reduced circulation implementation with a broader oxygen-transport model | Confirmed from project history; **Historical / superseded** at current production ref because no Shock physiology simulation is present |
| Interactive Equipment | Macintosh laryngoscope modeling/refinement workflow established | Confirmed from project history; not production-integrated at current ref |
| Interactive Equipment | Shiley-style cuffed tracheostomy model developed with modular outer cannula, removable inner cannula, obturator, cuff/pilot-line, and iterative animation/model revisions | Confirmed from project history; not production-integrated at current ref |
| Project control | Dedicated GitHub project-control repository initialized | Project-control verified |
| Project control | `setup/project-control-foundation` branch created for first-pass documentation | Project-control verified |
| Project control | Draft project-control PR #1 opened | Project-control verified |
| Project control | Evidence/lifecycle vocabulary and production-verification framework established | Project-control verified |
| Project control | Issues #2–#5 created as the initial verification backlog | Project-control verified |
| Production source | Existing RT Study Lab Git repository recovered and preserved in private GitHub repository `R3C4LL4L1F3/RT-study-lab` without replacing its existing Sites remote | Verified against production repository / migration evidence |
| Production verification | Baseline production source established at `a0495e9fa4e5437d8a027312b618b5c1c389ef94` (`Redesign Shock visual teaching page`) | Verified against production repository |
| Production verification | ECG/ACLS, Ventilator, Shock, equipment/chest-trauma 3D, PFT, ABG, disease, and medication modules mapped against current source | Verified against production repository |
| Production verification | Shock future lab confirmed as an explicit nonimplemented integration boundary; historical reduced-circulation reconciliation concern superseded | Verified against production repository |
| Production verification | Historical Shiley Blender model confirmed not production-integrated; chest-trauma 3D identified as current integrated Three.js/R3F 3D implementation | Verified against production repository |
| Project control | Issue #2 closed after production-source baseline completion; Issue #4 closed after Shock reconciliation; Issue #6 created for complete automated validation/CI | Project-control verified |
| Validation / Issue #6 | Production branch `validation/issue-6-test-baseline` and draft production PR #1 created from baseline `main`; no application/clinical code changes included | Verified against production repository/GitHub |
| Validation / Issue #6 | npm selected as canonical reproducible validation package manager; maintained `package-lock.json` used for CI while pnpm artifacts retained pending Sites/Vinext verification | Verified against production repository; project decision recorded |
| Validation / Issue #6 | Canonical `npm test` redesigned to build then recursively execute the complete `tests/**/*.test.mjs` inventory instead of a fixed five-file subset | Verified against production draft PR |
| Validation / Issue #6 | Initial CI investigation exposed Node 22.13 direct `.ts` import failures (`ERR_UNKNOWN_FILE_EXTENSION`); validation runner updated to use Node `--experimental-strip-types` without modifying production application source | Verified against GitHub Actions failure annotations and production draft PR |
| Validation / Issue #6 | Final production PR ref `96b5535f9228c7b01c709386e050ce53e68f14d4` passed `npm ci`, lint, build, complete 28-file suite, dedicated Ventilator historical-P1 regression, and diagnostic artifact upload in Actions run `31309995943` | **Verified executable automated evidence** |
| Ventilator verification | Historical P1 concerns now have passing automated regression evidence at production PR ref `96b5535...`; browser presentation/control verification remains | Verified automated evidence; runtime/browser verification still open |
| Chest-trauma 3D verification | `chest-trauma-3d.test.mjs` and `chest-trauma-visual.test.mjs` passed as part of the Issue #6 complete suite; manual visual/mechanical browser review remains | Verified automated evidence; manual verification still open |

## Current merge boundary

The Issue #6 validation implementation is on **draft production PR #1** and is not merged. Production `main` remains at the pre-validation baseline until explicit maintainer authorization is given.

Project-control PR #1 also remains draft and unmerged.

## History policy

Future entries should include, when available:

- date or release identifier established by evidence;
- production repository path and commit/pull request;
- deployment reference;
- validation/test reference;
- regressions introduced or resolved;
- evidence basis;
- lifecycle/disposition;
- explicit distinction between automated, clinical, accessibility, deployment, and manual visual/mechanical evidence.

Do not assign precise dates, versions, implementation states, resolution states, or architecture details retrospectively unless a source establishes them.
