# Development History

This history preserves major RT Study Lab project records and distinguishes historical claims from milestones now verified against production source.

## Development sequence

| Area | Milestone / record | Evidence basis |
|---|---|---|
| Ventilator Waveform Lab | Continuous A/C VC and PC waveform lab with historical navigation/playback/window/annotation work | Confirmed from project history; current implementation now source-verified |
| Ventilator Waveform Lab | Historical audit reported P1 concerns involving double triggering/minute ventilation, dynamic compliance during effort, historical mode labeling, and expiratory-hold scheduling | Confirmed from project history |
| Ventilator Waveform Lab | Current source contains dedicated Session 3.5.2 regression coverage and implementation paths addressing the historical P1 concerns | Verified against production repository at `a0495e9...`; runtime re-execution required |
| ECG Rhythm Lab | Initial rhythm engine, Learn/Practice behavior, measurement controls and expanding rhythm library | Confirmed from project history; current architecture now source-verified |
| ECG Rhythm Lab | Optional landmark snapping and guided measurement workflow | Confirmed from project history; current source verifies caliper-snapping implementation |
| ECG / ACLS | Patient-state, Clinical Practice/Exam, pathway, treatment, arrest and post-arrest learning architecture | Confirmed from project history; current source verifies the distinct engine/module architecture |
| ECG / ACLS | Current source verifies 500 Hz internal ECG generation and 19 rhythm definitions | Verified against production repository at `a0495e9...` |
| ECG / ACLS | Current pathway/treatment source carries AHA 2025 guideline metadata and educational/non-endorsement boundaries | Verified against production repository at `a0495e9...` |
| Shock | Course-aligned Shock disease module and later visual-teaching redesign | Verified from production commit history and source |
| Shock / Oxygen Transport | Current production source explicitly leaves the oxygen-transport simulation as a future integration boundary; no simulation runs on the page | Verified against production repository at `a0495e9...` |
| Interactive Equipment | Macintosh laryngoscope and Shiley-style cuffed tracheostomy Blender/model refinement work | Confirmed from project history; not identified as production-integrated at the baseline ref |
| Equipment catalog | Interactive image/HTML equipment lessons with device content, safety scenarios and source/license metadata | Verified against production repository at `a0495e9...` |
| Chest Trauma 3D | HRA respiratory and BodyParts3D thorax assets integrated into a React Three Fiber/Three.js visual lab with desktop/mobile variants | Verified against production repository and commit history |
| PFT | Reconstructed PFT report/loop learning system with 12 report-specific datasets and source-controlled validation contracts | Verified against production repository at `a0495e9...` |
| ABG | 25-case ABG interpretation lab | Verified against production repository at `a0495e9...` |
| Disease content | Generic disease library plus specialized Shock, Stroke, Burns, Chest Trauma, TBI/trauma modules | Verified against production repository at `a0495e9...` |
| Pharmacology | Structured respiratory medication monographs linked to shared source registry | Verified against production repository at `a0495e9...` |
| Project control | Dedicated GitHub project-control repository initialized | Project-control verified |
| Project control | `setup/project-control-foundation` branch created and Draft PR #1 opened | Project-control verified |
| Project control | Evidence/lifecycle vocabulary, roadmap, known-issue, validation and production-verification framework established | Project-control verified |
| Project control | Issues #2–#5 created as a small verification backlog | Project-control verified |
| Source control | Canonical private GitHub production repository established as `R3C4LL4L1F3/RT-study-lab` while preserving the pre-existing Sites source history | Verified against production repository/project workflow |
| Production baseline | Source ref `a0495e9fa4e5437d8a027312b618b5c1c389ef94` audited and mapped into project-control records | Project-control verified + Verified against production repository |
| Production baseline | Canonical `npm test` found to execute only a subset of the source-controlled test inventory; no GitHub Actions workflow identified | Verified against production repository |

## Historical test/validation policy

Historical numeric test counts and multidisciplinary review scores remain preserved in `VALIDATION_REGISTER.md`. Current source correspondence may confirm that engines/tests exist, but historical pass counts do not become current pass results until a current suite is executed with durable evidence.

## History policy

Future entries should include, when available:

- date/release identifier established by evidence
- feature/change summary
- production repository path and exact commit/PR
- deployment reference where established
- validation/test reference
- known regressions introduced/resolved
- evidence basis and lifecycle/disposition

Do not assign precise dates, deployment states, pass results, clinical validation, accessibility conformance, or defect-resolution status retrospectively without evidence.
