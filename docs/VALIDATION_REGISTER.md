# Validation Register

This register preserves known validation/test claims while keeping their evidence basis explicit.

**Important:** historical values below are **Confirmed from project history** but **Need verification against production repository**. They have not been independently re-run from current production source or CI through this project-control repository.

## Ventilator Waveform Lab

### Historical multidisciplinary validation summary

| Dimension | Historical score | Evidence basis |
|---|---:|---|
| Clinical | 82/100 | Confirmed from project history; needs production verification |
| Engineering | 76/100 | Confirmed from project history; needs production verification |
| Educational | 79/100 | Confirmed from project history; needs production verification |
| Mechanics | 88/100 | Confirmed from project history; needs production verification |
| Realism | 84/100 | Confirmed from project history; needs production verification |
| Measurement | 78/100 | Confirmed from project history; needs production verification |

Additional historical result:

- Browser/clinical validation outcome: **PARTIAL PASS**
- Four P1 concerns remained in the historical audit; see `KNOWN_ISSUES.md`.
- Those concerns are not Current known issues until reproduced or otherwise confirmed against current production evidence.

## ECG Rhythm / ACLS Lab

### Historical automated-test milestones

| Milestone | Historical result | Evidence basis |
|---|---|---|
| Phase 1A | ECG tests 12/12; site tests 97/97 | Confirmed from project history; needs production verification |
| Final Phase 1 audit | ECG tests 33/33; site tests 118/118 | Confirmed from project history; needs production verification |
| Version 27 landmark snapping | ECG tests 40/40; site tests 125/125 | Confirmed from project history; needs production verification |
| Phase 2A-1 patient-state engine | Patient-state tests 8/8 | Confirmed from project history; needs production verification |
| Phase 2A-2 clinical practice/exam | Patient-state tests 19/19; ECG tests 59/59; complete suite 144 | Confirmed from project history; needs production verification |
| Phase 2B-2 treatment engine | Treatment tests 18/18; complete suite 175/175 | Confirmed from project history; needs production verification |

These names, counts, and milestone identifiers are retained as historical records only. Do not infer that the same test files, version labels, suite size, or pass state exist in current production.

## Other major workstreams

The project-control repository does not yet contain durable validation evidence for the following workstreams:

- Shock / Oxygen Transport Lab
- Interactive Respiratory Equipment Lab
- PFT Lab
- disease-process modules
- ABG / hemodynamics
- respiratory pharmacology
- oxygen-delivery/equipment content
- future interactive clinical simulations

Their current validation status is **Needs verification against production repository** or **Unknown**, as detailed in `PRODUCTION_REPOSITORY_VERIFICATION.md`.

## Requirements for production verification

For a historical result to become **Verified against production repository**, retain or link enough evidence to establish:

1. canonical production repository and source commit/ref under test
2. test command or validation procedure
3. environment/tool versions where relevant
4. raw or durable result artifact
5. reviewer identity/role for manual clinical, mechanical, educational, visual, or accessibility review where appropriate
6. date of the actual validation event, when established by evidence
7. unresolved findings and disposition
8. the exact module/scope covered by the evidence

## Clinical-validation policy

Automated tests are not equivalent to clinical validation. Clinical claims should identify:

- the clinical rule/assumption being evaluated
- source guideline/text/reference and version/date when verified and relevant
- scope and known limitations
- reviewer qualifications when human clinical review is part of the evidence
- whether the result is educationally acceptable, clinically plausible, or intended to reproduce real bedside behavior

Until those elements are recorded, clinical statements should remain **Confirmed from project history**, **Needs verification against production repository**, **Planned work**, or **Unknown** rather than being labeled production-validated.
