# Development History

This history preserves the **reported sequence** of major RT Study Lab work from prior project records. Unless a row explicitly says otherwise, these entries are not independently verified from production source or CI in this repository.

## Reported development sequence

| Area | Reported milestone | Evidence state |
|---|---|---|
| Ventilator Waveform Lab | Continuous A/C VC and PC waveform lab with historical breath navigation, playback/window controls, annotations, and selected-breath details | Reported |
| Ventilator Waveform Lab | Session 3.5 audit identified four P1 issues affecting double triggering, dynamic compliance during effort, historical mode labeling, and expiratory-hold scheduling | Reported |
| ECG Rhythm Lab | Initial rhythm-learning engine with Learn Mode, ECG measurement controls, calibration, and a core rhythm library | Reported |
| ECG Rhythm Lab | Rhythm library expanded with ectopy, SVT, polymorphic VT, torsades, and additional practice behavior | Reported |
| ECG Rhythm Lab | Final Phase 1 audit refined measurement references, calipers, long-window behavior, rhythm-specific controls, and accessibility/performance behavior | Reported |
| ECG Rhythm Lab | Optional ECG landmark snapping added for measurement workflows | Reported |
| ECG / ACLS | Independent patient-state engine added to classify pulse, perfusion, breathing, mental status, shock, heart failure, arrest, and pathway state | Reported |
| ECG / ACLS | Clinical Practice and Examination modes added with seeded cases, scoring, timing, review, and local history | Reported |
| ECG / ACLS | Guideline/pathway engine added separately from waveform and patient-state engines | Reported |
| ECG / ACLS | Treatment engine added with medication/electrical actions, reassessment, deterministic state transitions, timeline replay, and sequence-aware scoring | Reported |
| Interactive Equipment | Macintosh laryngoscope modeling/refinement workflow established | Reported |
| Interactive Equipment | Shiley-style cuffed tracheostomy tube model developed with modular outer cannula, removable inner cannula, obturator, cuff/pilot-line, and iterative animation/model revisions | Reported |
| Project control | Dedicated GitHub project-control repository initialized | Repository-verified |
| Project control | `setup/project-control-foundation` branch created for first-pass documentation | Repository-verified |

## History policy

Future entries should include, when available:

- date or release identifier
- feature/change summary
- production commit or pull request
- deployment reference
- validation/test reference
- known regressions introduced or resolved
- evidence state

Do not assign precise dates retrospectively unless a source establishes them.
