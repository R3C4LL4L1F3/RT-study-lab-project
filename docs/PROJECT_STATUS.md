# Project Status

## Purpose of this status record

This document separates repository-observable facts from historical implementation claims that have not yet been independently verified from production source, CI, or deployment artifacts.

## Repository-verified status

- This repository is a project-control/documentation repository.
- `main` is the default branch.
- `setup/project-control-foundation` is the current documentation foundation branch.
- Before this foundation work, the repository contained only a short `README.md`.
- No GitHub issues or pull requests were present when this foundation was inspected.
- No CI configuration or validation artifacts were present in this repository at that time.
- The production application source repository is not identified in this repository.

## Reported RT Study Lab status

The following items are preserved from prior development records. They are **Reported**, not independently re-run or verified from this repository.

### Ventilator Waveform Lab

Reported capabilities include an A/C volume-control and pressure-control waveform lab with continuous waveform history, breath navigation, selected-breath detail, controls for playback/window/history, annotations, and responsive learning controls.

A prior validation summary reported the following scores:

- Clinical: 82/100
- Engineering: 76/100
- Educational: 79/100
- Mechanics: 88/100
- Realism: 84/100
- Measurement: 78/100

The browser/clinical audit was reported as **PARTIAL PASS**, with four unresolved P1 issues retained in `KNOWN_ISSUES.md`.

### ECG Rhythm / ACLS Lab

Prior development records report a staged ECG/ACLS learning system including:

- ECG waveform generation and measurement tools
- Learn Mode and Practice Mode
- Expanded rhythm library
- Digital calipers and optional landmark snapping
- Patient-state modeling
- Clinical Practice and Examination modes
- Guideline/pathway logic
- Treatment sequencing, reassessment, and timeline replay

Reported test milestones are preserved in `VALIDATION_REGISTER.md`. They remain **Reported** until reproduced or supported with archived evidence.

### Interactive Respiratory Equipment Lab

Prior development records report work on interactive 3D respiratory-equipment content, including:

- Macintosh laryngoscope modeling
- Shiley-style cuffed tracheostomy tube modeling
- Inner-cannula, obturator, cuff/pilot-line, and animation work
- Blender/Python-based refinement workflows

Current production integration state, source location, validation status, and deployment state are **Unknown** in this repository.

## Current control gaps

1. Production application repository/location is not linked.
2. No build, test, or deployment evidence has been imported.
3. Historical validation claims are not yet backed by reproducible artifacts here.
4. Known application issues are documented from prior records but are not represented as GitHub issues yet.
5. Architecture decisions from prior work have not been reconstructed beyond the initial control decisions in this repository.

## Next status transition

The highest-value next step is to identify the production source repository and deployment target, then audit the current application directly. That audit should establish a new baseline for implementation status, tests, validation evidence, and open defects.
