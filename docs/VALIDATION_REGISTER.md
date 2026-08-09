# Validation Register

This register preserves known validation/test claims while keeping their evidence state explicit.

**Important:** historical values below are **Reported** from prior development records. They have not been independently re-run from source or CI in this repository.

## Ventilator Waveform Lab

### Reported multidisciplinary validation summary

| Dimension | Reported score | Evidence state |
|---|---:|---|
| Clinical | 82/100 | Reported |
| Engineering | 76/100 | Reported |
| Educational | 79/100 | Reported |
| Mechanics | 88/100 | Reported |
| Realism | 84/100 | Reported |
| Measurement | 78/100 | Reported |

Additional reported result:

- Browser/clinical validation outcome: **PARTIAL PASS**
- Four P1 issues remained open in the historical audit; see `KNOWN_ISSUES.md`.

## ECG Rhythm / ACLS Lab

### Reported automated-test milestones

| Milestone | Reported result | Evidence state |
|---|---|---|
| Phase 1A | ECG tests 12/12; site tests 97/97 | Reported |
| Final Phase 1 audit | ECG tests 33/33; site tests 118/118 | Reported |
| Version 27 landmark snapping | ECG tests 40/40; site tests 125/125 | Reported |
| Phase 2A-1 patient-state engine | Patient-state tests 8/8 | Reported |
| Phase 2A-2 clinical practice/exam | Patient-state tests 19/19; ECG tests 59/59; complete suite 144 | Reported |
| Phase 2B-2 treatment engine | Treatment tests 18/18; complete suite 175/175 | Reported |

## What is missing for repository verification

For any reported result to become **Repository-verified**, retain or link enough evidence to establish:

1. source commit or release under test
2. test command or validation procedure
3. environment/tool versions where relevant
4. raw or durable result artifact
5. reviewer identity/role for manual clinical or educational review where appropriate
6. date of the actual validation event
7. unresolved findings and disposition

## Clinical-validation policy

Automated tests are not equivalent to clinical validation. Clinical claims should identify:

- the clinical rule/assumption being evaluated
- source guideline/text/reference and version/date
- scope and known limitations
- reviewer qualifications when human clinical review is part of the evidence
- whether the result is educationally acceptable, clinically plausible, or intended to reproduce real bedside behavior

Until those elements are recorded, clinical statements should remain **Reported**, **Proposed**, or **Unknown** rather than being labeled validated.
