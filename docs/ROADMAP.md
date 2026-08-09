# Roadmap

This roadmap distinguishes **control work required to establish reliable project state** from proposed product development. Priorities may change after the production source repository is identified and audited.

## P0 — Establish trustworthy project control

### 1. Link production source and deployment evidence

- Identify the production application source repository.
- Record the canonical deployment target and environment(s).
- Record the relationship between production source, this project-control repository, and any asset/model repositories.
- Add links/references without copying secrets or credentials.

**Exit criterion:** a maintainer can move from this repository to the exact production source and deployment evidence without relying on chat history.

### 2. Establish a reproducible validation baseline

- Inspect the production test suite.
- Run or retrieve current test results.
- Record environment/tooling versions needed to reproduce them.
- Separate automated tests from clinical/educational review.
- Archive or link validation evidence.

**Exit criterion:** current test and validation claims can be traced to reproducible evidence.

### 3. Convert known defects into tracked issues

Create GitHub issues for confirmed unresolved defects, starting with the reported Ventilator Waveform Lab P1 items in `KNOWN_ISSUES.md` after confirming they are still present in the current product.

**Exit criterion:** every confirmed P1 defect has an owner/state, reproduction steps, and acceptance criteria.

## P1 — Stabilize high-value learning systems

### Ventilator Waveform Lab

Proposed order after current-state verification:

1. Resolve double-trigger breath stacking/minute-ventilation behavior.
2. Correct dynamic-compliance behavior during patient effort.
3. Preserve historical mode identity across mode changes.
4. Fix expiratory-hold scheduling behavior.
5. Re-run clinical, engineering, mechanics, realism, measurement, and educational audits.

### ECG / ACLS Lab

- Reconcile the reported feature/test history with current production source.
- Verify rhythm-generation and measurement behavior.
- Verify patient-state and treatment engines independently.
- Confirm current guideline-source metadata.
- Re-run deterministic scenario and safety-critical sequence tests.
- Record clinically reviewed assumptions and limitations.

### Interactive Respiratory Equipment Lab

- Inventory production-ready vs experimental 3D assets.
- Record license/provenance for sourced assets.
- Establish model review criteria for anatomy/device geometry and animation.
- Define integration acceptance criteria for interactive equipment pages.
- Keep model geometry, animation logic, and educational annotations independently reviewable.

## P2 — Improve documentation durability

- Add a lightweight ADR format for substantive architecture decisions.
- Add issue/PR templates for defects, clinical review, and feature work.
- Add validation-report templates.
- Add release/deployment records once production versioning is known.
- Add a glossary for project-specific terminology and evidence states.

## Deferred until evidence is available

The following should not be asserted or scheduled as completed work without further evidence:

- production release/version numbers
- current deployment health
- current CI pass/fail state
- current clinical-validation status
- exact production test counts
- exact ownership/assignees for product subsystems
