# Known Issues and Verification Concerns

This register separates current project-control gaps from historical application defect reports and verification concerns that have **not** yet been confirmed against the current production implementation.

Use the evidence/lifecycle vocabulary defined in the repository `README.md`.

## Current project-control issues

### PC-001 — Production source repository is not linked or identified

- Severity: High
- Evidence basis: Project-control verified
- Lifecycle: Current known issue (project control)
- Impact: Implementation, test, CI, deployment, architecture, and defect-resolution claims cannot be independently reconciled from this repository.
- Resolution target: Record the canonical production source repository and deployment relationship without adding credentials or sensitive data.

### PC-002 — No reproducible production-linked validation evidence is stored or linked

- Severity: High
- Evidence basis: Project-control verified
- Lifecycle: Current known issue (project control)
- Impact: Historical test counts and validation summaries remain project-history claims rather than current verified results.
- Resolution target: Link or archive current automated-test results, validation reports, source refs, and environment information once the production repository is identified.

### PC-003 — Current application defect status has not been reconciled

- Severity: High
- Evidence basis: Project-control verified
- Lifecycle: Current known issue (project control)
- Impact: Historical defect reports cannot yet be classified as still present, resolved, regressed, or superseded.
- Resolution target: Perform Production Repository Verification and reproduce high-risk historical concerns against current source/build behavior.

## Ventilator Waveform Lab — historical defect reports

The four records below are **Confirmed from project history** and **Need verification against production repository**. They are deliberately **not** labeled Current known issues until current evidence confirms them.

### VENT-P1-001 — Double-trigger preset can produce triple stacking / incorrect minute ventilation

- Historical priority: P1
- Evidence basis: Confirmed from project history
- Lifecycle: Historical / possibly superseded
- Reported behavior: The double-trigger preset can produce triple-stacked breaths and/or minute-ventilation behavior inconsistent with the intended scenario.
- Required verification: Reproduce against the current production build/source and inspect event scheduling, breath generation, and minute-ventilation calculation behavior.

### VENT-P1-002 — Dynamic compliance during patient effort

- Historical priority: P1
- Evidence basis: Confirmed from project history
- Lifecycle: Historical / possibly superseded
- Reported behavior: Dynamic-compliance output during patient effort may be physiologically or mechanically misleading.
- Required verification: Confirm calculation and display semantics against the current waveform engine and intended teaching model; do not assume a formula that has not been observed in source.

### VENT-P1-003 — Mode change relabels historical VC data as PC

- Historical priority: P1
- Evidence basis: Confirmed from project history
- Lifecycle: Historical / possibly superseded
- Reported behavior: Historical volume-control waveform/breath data can be relabeled as pressure-control after a mode change.
- Required verification: Confirm that each historical breath retains the mode identity active when that breath was generated.

### VENT-P1-004 — Expiratory hold not reschedulable after breath 3

- Historical priority: P1
- Evidence basis: Confirmed from project history
- Lifecycle: Historical / possibly superseded
- Reported behavior: An expiratory-hold action may not schedule correctly after the third breath.
- Required verification: Reproduce against the current hold scheduler/state machine and document actual supported scheduling behavior.

## Shock / Oxygen Transport Lab — verification concerns

These are verification requirements, not confirmed production defects.

### SHOCK-VERIFY-001 — Reconcile implemented transport model with intended broader physiology model

- Evidence basis: Confirmed from project history
- Lifecycle: Needs verification against production repository
- Verification scope:
  - identify the circulation/transport model actually implemented
  - compare the current reduced circulation implementation with the intended broader physiology architecture
  - identify missing, simplified, or disconnected subsystems

### SHOCK-VERIFY-002 — Validate oxygen-transport coupling and numerical behavior

- Evidence basis: Confirmed from project history
- Lifecycle: Needs verification against production repository
- Verification scope:
  - inspect whether Hb → CaO2 → DO2 → VO2 → CvO2/SvO2 → extraction → oxygen-debt relationships are actually coupled in source
  - determine which values are calculated, derived, approximated, or illustrative
  - test conservation behavior and numerical stability across supported scenarios
  - do not document equations or clinical rules that are not verified from source/reference evidence

## Interactive Respiratory Equipment Lab — verification concerns

These are verification requirements, not confirmed production defects.

### EQUIP-VERIFY-001 — Verify geometry, mechanics, animation, and browser readiness

- Evidence basis: Confirmed from project history
- Lifecycle: Needs verification against production repository
- Verification scope:
  - geometry fidelity and proportions for the stated educational purpose
  - mechanical realism of moving/locking components
  - animation paths and device-part alignment
  - clipping, self-intersection, and part-to-part intersections
  - Shiley-style snap-lock inner-cannula behavior without invented twist-lock motion
  - asset provenance/license records for sourced assets
  - browser optimization for models, textures, animations, and interaction runtime

## Current production defect status

No application item in this file is currently labeled **Current known issue** based on production-source evidence because the canonical production repository has not yet been identified through the current GitHub connection.

GitHub issues may be created to track **verification work** before production access is available. The existence of a tracking issue must not be interpreted as proof that a historical defect still exists.
