# Production Repository Verification

## Purpose

This document is the control framework for converting RT Study Lab project-history claims into facts verified against the actual production implementation.

It is intentionally a **verification framework**, not a claim that verification has already occurred.

## Current dependency

The canonical production RT Study Lab source repository has **not been identified through the current GitHub connection**. Relevant installed-repository searches surfaced this project-control repository, but no separate production repository was identified.

Until the canonical production source is available, module implementation status, current defects, architecture, tests, deployment state, accessibility evidence, and clinical-validation evidence remain **Needs verification against production repository** unless another durable source is explicitly recorded.

Do not guess the production repository name, path, branch, deployment environment, or architecture.

## Verification standard

For each major module, record all of the following before declaring the module production-verified:

- production repository and repository path
- source ref/commit used for verification
- implementation status observed in source
- relevant source files/directories
- architecture observed in code
- tests present and what they actually cover
- known defects reproduced or confirmed
- historical claims confirmed, refuted, or superseded
- clinical-validation evidence, if applicable
- accessibility evidence, if applicable
- deployment evidence, when relevant
- last verification point
- unresolved verification questions

A module can be partially verified. Each field should retain its own evidence state rather than forcing an all-or-nothing module status.

## Module verification register

### ECG Rhythm / ACLS Lab

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Confirmed from project history; needs production verification**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Confirmed from project history only; needs production verification**
- Known defects confirmed: **None established from current production source**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Historical claims exist; needs production verification**
- Accessibility evidence: **Historical claims exist; needs production verification**
- Last verification point: **None against production repository**
- Unresolved questions:
  - Which source files implement waveform generation, measurement/calipers, patient state, pathway logic, treatment logic, scoring, and UI rendering?
  - Are those engines still independently separable in current source?
  - What automated tests currently exist and what clinical behaviors do they cover?
  - What guideline/reference metadata is actually present in current source?

### Ventilator Waveform Lab

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Confirmed from project history; needs production verification**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Historical test/validation claims exist; needs production verification**
- Known defects confirmed: **None established as Current known issues from production source**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Historical multidisciplinary scores exist; needs production verification**
- Accessibility evidence: **Historical review claims exist; needs production verification**
- Last verification point: **None against production repository**
- Required verification questions:
  - Does the double-trigger scenario still permit unintended triple stacking or incorrect minute-ventilation behavior?
  - Is dynamic compliance calculated/displayed appropriately during patient effort?
  - Does historical breath data preserve the mode identity active when each breath was generated, rather than being relabeled after VC/PC mode changes?
  - Can expiratory holds be scheduled/rescheduled correctly beyond the historically reported breath-3 limitation?

### Shock / Oxygen Transport Lab

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Confirmed from project history at a high level; needs production verification**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **None established as Current known issues from production source**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Required verification questions:
  - How does the current reduced circulation implementation compare with the intended broader physiology model?
  - Are Hb → CaO2 → DO2 → VO2 → CvO2/SvO2 → extraction → oxygen-debt relationships actually coupled in the implementation, and how?
  - Do the implemented calculations conserve quantities and remain numerically stable across supported scenarios?
  - Which intended subsystems are absent, simplified, or disconnected?
  - Which displayed values are calculated, derived, approximated, or purely illustrative?

### Interactive Respiratory Equipment Lab

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Confirmed from project history; needs production verification**
- Relevant source files/assets: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **None established as Current known issues from production source**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical/mechanical validation evidence: **Historical review activity exists; current evidence unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Required verification questions:
  - Are model geometry and proportions sufficiently faithful for the stated educational purpose?
  - Are mechanical interactions and animation paths realistic and internally consistent?
  - Are there clipping, self-intersection, or device-part intersection problems in supported interactions?
  - Does the Shiley-style inner cannula use snap-lock behavior without an invented twist-lock motion?
  - Are asset provenance/license records complete for externally sourced assets?
  - Are models, textures, animation data, and browser runtime behavior optimized sufficiently for supported devices?

### PFT Lab

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Unknown in this repository**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **Unknown**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Unresolved questions: identify current scope, location, interaction model, calculations/interpretation logic, tests, and deployment state.

### Disease-Process Modules

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Unknown at repository level**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **Unknown**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Unresolved questions: inventory disease-process modules, identify shared components/content systems, and determine which modules are production-ready, experimental, or historical.

### ABG / Hemodynamics

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Unknown at repository level**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **Unknown**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Unresolved questions: identify implemented calculations, units, reference ranges, interpretation logic, scenario engines, and validation coverage without assuming equations or clinical rules that are not present in source.

### Respiratory Pharmacology

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Unknown at repository level**
- Relevant source files/content stores: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **Unknown**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Unresolved questions: identify current content scope, data model, references, interaction patterns, validation process, and update strategy.

### Oxygen-Delivery / Equipment Content

- Production repository/path: **Needs verification against production repository**
- Implementation status: **Unknown at repository level**
- Relevant source files/content/assets: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **Unknown**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Unresolved questions: inventory oxygen devices/equipment pages, determine image/3D/interactive asset sources, verify stated operating principles and educational scope, and identify overlap with the Interactive Respiratory Equipment Lab.

### Future Interactive Clinical Simulations

- Production repository/path: **Not applicable until implemented; verify any existing experimental source before changing this status**
- Implementation status: **Planned work unless production evidence proves otherwise**
- Relevant source files: **Unknown**
- Architecture observed in code: **Unknown**
- Tests present: **Unknown**
- Known defects confirmed: **Not applicable until implementation is identified**
- Historical claims confirmed/refuted: **Not yet reconciled**
- Clinical-validation evidence: **Unknown**
- Accessibility evidence: **Unknown**
- Last verification point: **None against production repository**
- Unresolved questions: identify whether any simulation framework already exists before designing or documenting a new one.

## Verification workflow

For each module:

1. Identify the canonical production repository and exact source ref.
2. Locate the module entry points and relevant files.
3. Record architecture from observed source rather than historical assumptions.
4. Inventory existing tests before running or changing them.
5. Reproduce high-risk historical defects where applicable.
6. Compare observed implementation with project-history claims.
7. Record confirmed, refuted, superseded, and still-unknown claims separately.
8. Inspect validation evidence and accessibility evidence without treating automated tests as clinical validation.
9. Update `PROJECT_STATUS.md`, `KNOWN_ISSUES.md`, `VALIDATION_REGISTER.md`, and `DEVELOPMENT_HISTORY.md` with traceable evidence.
10. Only then promote applicable records to **Verified against production repository** or **Current known issue**.

## Completion criteria for this phase

Production Repository Verification is complete only when:

- the canonical production repository is identified and linked safely
- each major module has a recorded source path/ref
- implementation status is based on current source
- high-risk historical defects have been reconciled
- relevant tests and validation evidence are inventoried
- historical claims are marked confirmed, refuted, superseded, or still unverified
- unresolved verification questions remain visible rather than being guessed away
