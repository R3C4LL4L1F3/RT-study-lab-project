# Roadmap

This roadmap distinguishes **control work required to establish reliable project state** from proposed product development. Priorities may change after the production source repository is identified and audited.

## P0 — Production Repository Verification

This is the next highest-value project-control phase. Use `PRODUCTION_REPOSITORY_VERIFICATION.md` as the working framework.

### 1. Identify the canonical production source and deployment evidence

- Identify the production application source repository.
- Record the canonical deployment target and environment(s), if available.
- Record the relationship between production source, this project-control repository, and any asset/model repositories.
- Add links/references without copying secrets, credentials, private filesystem paths, or personal/private data.

**Current dependency:** relevant searches through the current GitHub connection have identified this project-control repository but have not identified a separate production RT Study Lab repository.

**Exit criterion:** a maintainer can move from this repository to the exact production source and deployment evidence without relying on chat history.

### 2. Verify each major workstream against current source

For each module, record production path/ref, implementation status, relevant source files, architecture observed in code, tests present, known defects confirmed, historical claims confirmed/refuted/superseded, clinical-validation evidence, accessibility evidence, last verification point, and unresolved questions.

Required coverage:

- ECG Rhythm / ACLS Lab
- Ventilator Waveform Lab
- Shock / Oxygen Transport Lab
- Interactive Respiratory Equipment Lab
- PFT Lab
- disease-process modules
- ABG / hemodynamics
- respiratory pharmacology
- oxygen-delivery/equipment content
- future interactive clinical simulations or any existing experimental simulation framework

**Exit criterion:** every major workstream has a production-source status record or an explicit documented reason it cannot yet be verified.

### 3. Establish a reproducible validation baseline

- Inspect the production test suite before changing it.
- Run or retrieve current test results when the source/build environment is available.
- Record source ref, test command/procedure, environment/tool versions, and durable result evidence.
- Separate automated tests from clinical, educational, accessibility, visual, and mechanical review.
- Reconcile historical test counts rather than assuming they remain current.

**Exit criterion:** current test and validation claims can be traced to reproducible evidence.

### 4. Reconcile historical defect reports into current issue state

Prioritize high-risk correctness concerns.

#### Ventilator Waveform Lab

Verify whether the following historical P1 concerns still exist:

1. double-trigger breath stacking/minute-ventilation behavior
2. dynamic-compliance behavior during patient effort
3. historical VC/PC breath labeling across mode changes
4. expiratory-hold scheduling/rescheduling behavior

Do not mark any of these **Current known issue** or **Resolved** without current production evidence.

#### Shock / Oxygen Transport Lab

- reconcile the current reduced circulation implementation with the intended broader physiology model
- inspect Hb → CaO2 → DO2 → VO2 → CvO2/SvO2 → extraction → oxygen-debt coupling as actually implemented
- test conservation and numerical stability
- identify absent, simplified, or disconnected subsystems

#### Interactive Respiratory Equipment Lab

- verify geometry fidelity and intended educational accuracy
- verify mechanical realism and animation paths
- check clipping/intersections
- verify Shiley-style snap-lock inner-cannula behavior
- verify asset provenance/license records
- evaluate browser optimization and interaction performance

**Exit criterion:** each historical high-risk concern is classified as confirmed current defect, resolved, superseded, not reproducible, or still unverified, with evidence.

## P1 — Stabilize production-verified learning systems

Only move work into this phase after the relevant module has a current source baseline.

### Ventilator Waveform Lab

If current verification confirms the historical concerns, fix them in production source and re-run the appropriate engineering, clinical, mechanics, measurement, realism, educational, accessibility, and regression checks.

### ECG Rhythm / ACLS Lab

- verify waveform generation and measurement behavior
- verify patient-state, pathway, treatment, scoring, and UI concerns independently where the source architecture supports that separation
- confirm current guideline/reference metadata from source and authoritative references
- re-run deterministic scenario and safety-critical sequence tests where present
- record clinically reviewed assumptions and limitations

### Shock / Oxygen Transport Lab

After architecture verification, correct only source-observed discrepancies or explicitly approved model gaps. Preserve a traceable distinction between bedside physiology, educational simplification, and software implementation choices.

### Interactive Respiratory Equipment Lab

After source/asset inventory, prioritize correctness before visual refinement: device geometry, mechanics, animation constraints, clipping/intersections, provenance, and browser/runtime suitability.

### Other learning/content systems

For PFT, disease-process, ABG/hemodynamics, pharmacology, oxygen-delivery/equipment, and future clinical simulations, derive stabilization priorities from the production verification findings rather than from assumptions in project history.

## P2 — Improve documentation durability

- Add a lightweight ADR format for substantive architecture decisions.
- Add issue/PR templates for defects, clinical review, and feature work when repeated use justifies them.
- Add validation-report templates.
- Add release/deployment records once production versioning is known.
- Add a glossary for project-specific terminology and evidence states if the repository vocabulary becomes difficult to maintain from the README alone.

## Deferred until evidence is available

The following should not be asserted or scheduled as completed work without further evidence:

- production release/version numbers
- current deployment health
- current CI pass/fail state
- current clinical-validation status
- exact current production test counts
- exact production architecture details
- resolved status of historical defects
- exact ownership/assignees for product subsystems
