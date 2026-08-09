# Known Issues

This register contains both project-control gaps and application defects preserved from prior development records.

## Evidence legend

- **Repository-verified** — directly observable in this repository.
- **Reported** — preserved from prior project records; current production behavior has not yet been independently re-verified here.

## Project-control issues

### PC-001 — Production source repository is not linked

- Severity: High
- Evidence: Repository-verified
- Impact: Implementation, test, CI, and deployment claims cannot be independently reconciled from this repository.
- Resolution target: Record the canonical production source repository and deployment relationship.

### PC-002 — No reproducible validation evidence is stored or linked

- Severity: High
- Evidence: Repository-verified
- Impact: Historical test counts and validation summaries remain reported claims.
- Resolution target: Link or archive current automated-test results, validation reports, and environment information.

### PC-003 — Historical defects are not represented as GitHub issues

- Severity: Medium
- Evidence: Repository-verified
- Impact: Defects lack issue lifecycle, ownership, reproduction steps, and closure evidence.
- Resolution target: After current-state verification, convert confirmed unresolved defects into GitHub issues.

## Reported application issues

### VENT-P1-001 — Double-trigger preset can produce triple stacking / incorrect minute ventilation

- Priority: P1
- Evidence: Reported
- Area: Ventilator Waveform Lab
- Reported behavior: The double-trigger preset can produce triple-stacked breaths and/or minute-ventilation behavior inconsistent with the intended scenario.
- Required verification: Reproduce against the current production build before opening a defect issue.

### VENT-P1-002 — Dynamic compliance during patient effort

- Priority: P1
- Evidence: Reported
- Area: Ventilator Waveform Lab
- Reported behavior: Dynamic-compliance output during patient effort may be physiologically or mechanically misleading.
- Required verification: Confirm calculation/measurement semantics against the current waveform engine and intended clinical teaching model.

### VENT-P1-003 — Mode change relabels historical VC data as PC

- Priority: P1
- Evidence: Reported
- Area: Ventilator Waveform Lab
- Reported behavior: Historical volume-control waveform/breath data can be relabeled as pressure-control after a mode change.
- Required verification: Confirm that historical records retain the mode identity active when each breath was generated.

### VENT-P1-004 — Expiratory hold not reschedulable after breath 3

- Priority: P1
- Evidence: Reported
- Area: Ventilator Waveform Lab
- Reported behavior: An expiratory-hold action may not schedule correctly after the third breath.
- Required verification: Reproduce using the current hold scheduler/state machine.

## Not yet promoted to issue status

The four Ventilator P1 items above are intentionally retained as **Reported** records rather than GitHub issues until the production implementation can be inspected and the behavior reproduced. This prevents stale historical findings from being treated as confirmed current defects.
