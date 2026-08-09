# Development History

This history preserves the **reported sequence** of major RT Study Lab work from prior project records alongside project-control milestones that are directly observable in this repository.

Unless a row explicitly says otherwise, application-development entries are **Confirmed from project history** and **Need verification against production repository**. Their order is retained from project records; precise dates are not assigned retrospectively without source evidence.

## Development sequence

| Area | Milestone / historical record | Evidence basis |
|---|---|---|
| Ventilator Waveform Lab | Continuous A/C VC and PC waveform lab with historical breath navigation, playback/window controls, annotations, and selected-breath details | Confirmed from project history; needs production verification |
| Ventilator Waveform Lab | Session 3.5 audit identified four P1 concerns affecting double triggering, dynamic compliance during effort, historical mode labeling, and expiratory-hold scheduling | Confirmed from project history; historical / possibly superseded until production verification |
| ECG Rhythm Lab | Initial rhythm-learning engine with Learn Mode, ECG measurement controls, calibration, and a core rhythm library | Confirmed from project history; needs production verification |
| ECG Rhythm Lab | Rhythm library expanded with ectopy, SVT, polymorphic VT, torsades, and additional practice behavior | Confirmed from project history; needs production verification |
| ECG Rhythm Lab | Final Phase 1 audit refined measurement references, calipers, long-window behavior, rhythm-specific controls, and accessibility/performance behavior | Confirmed from project history; needs production verification |
| ECG Rhythm Lab | Optional ECG landmark snapping added for measurement workflows | Confirmed from project history; needs production verification |
| ECG / ACLS | Independent patient-state engine reported for pulse, perfusion, breathing, mental status, shock, heart failure, arrest, and pathway state | Confirmed from project history; needs production verification |
| ECG / ACLS | Clinical Practice and Examination modes reported with seeded cases, scoring, timing, review, and local history | Confirmed from project history; needs production verification |
| ECG / ACLS | Guideline/pathway engine reported separately from waveform and patient-state engines | Confirmed from project history; needs production verification |
| ECG / ACLS | Treatment engine reported with medication/electrical actions, reassessment, deterministic state transitions, timeline replay, and sequence-aware scoring | Confirmed from project history; needs production verification |
| Shock / Oxygen Transport | Project history identifies a need to reconcile a reduced circulation implementation with a broader intended oxygen-transport/physiology model | Confirmed from project history; needs production verification |
| Interactive Equipment | Macintosh laryngoscope modeling/refinement workflow established | Confirmed from project history; needs production verification |
| Interactive Equipment | Shiley-style cuffed tracheostomy tube model developed with modular outer cannula, removable inner cannula, obturator, cuff/pilot-line, and iterative animation/model revisions | Confirmed from project history; needs production verification |
| Project control | Dedicated GitHub project-control repository initialized | Project-control verified |
| Project control | `setup/project-control-foundation` branch created for first-pass documentation | Project-control verified |
| Project control | Draft PR #1 opened to establish the documentation foundation | Project-control verified |
| Project control | PR #1 audited; evidence/lifecycle vocabulary clarified and major workstream verification coverage expanded | Project-control verified |
| Project control | `PRODUCTION_REPOSITORY_VERIFICATION.md` added as the framework for the next control phase | Project-control verified |
| Project control | Issues #2–#5 created as a deliberately small verification backlog for production baseline, Ventilator, Shock/Oxygen Transport, and Interactive Equipment | Project-control verified |

## History policy

Future entries should include, when available:

- date or release identifier established by evidence
- feature/change summary
- production repository path and commit or pull request
- deployment reference
- validation/test reference
- known regressions introduced or resolved
- evidence basis
- lifecycle/disposition where relevant

Do not assign precise dates, versions, implementation states, resolution states, or architecture details retrospectively unless a source establishes them.
