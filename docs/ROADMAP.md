# Roadmap

This roadmap now starts from a source-backed production baseline rather than an unknown production repository.

## P0 — Establish reproducible production validation

The canonical production repository is `R3C4LL4L1F3/RT-study-lab`; the source baseline is recorded at `a0495e9fa4e5437d8a027312b618b5c1c389ef94` in `PRODUCTION_REPOSITORY_VERIFICATION.md`.

### 1. Make the canonical test command complete

Current evidence shows that `npm test` runs only five selected test files even though the production repository contains a broader ECG/ACLS, Ventilator, Shock, Stroke, trauma/chest-trauma 3D, and UX/clinical test inventory.

Priority actions:

- decide and document the canonical package manager
- create a deliberate full-suite test command
- include `tests/ventilator-session352.test.mjs` so the historical P1 regressions are part of the normal baseline
- include the current ECG/ACLS, Shock and chest-trauma 3D suites unless an evidence-backed reason requires a separate command
- run build, lint and full tests at a recorded source ref
- retain results without treating software tests as clinical validation

**Exit criterion:** a maintainer can run one documented baseline workflow and know which current source-controlled tests were executed.

### 2. Add durable GitHub CI after local semantics are proven

No `.github/workflows` CI configuration is present at the baseline ref.

After the canonical install/test commands are verified:

- add a conservative GitHub Actions workflow through a production-repository branch/PR
- run install/build/lint/full tests
- avoid adding secrets unless a workflow actually requires them
- keep deployment credentials and ChatGPT Sites internals out of the repository

**Exit criterion:** pull requests have durable automated evidence tied to commit SHAs.

### 3. Finalize Ventilator historical P1 dispositions with execution evidence

Current source and dedicated regression tests indicate that the historical issues are addressed:

1. double-trigger unintended triple stacking
2. minute-ventilation interval defect
3. dynamic compliance during effort/contamination
4. historical VC/PC breath relabeling
5. expiratory-hold rescheduling

Execute the relevant tests and browser behavior at a recorded ref before promoting the records from **Resolved in current source; runtime re-execution required** to **Verified resolved**.

### 4. Verify deployment synchronization

The GitHub repository is now the durable production-source repository, but current correspondence between GitHub `main` and the live ChatGPT Sites deployment is not yet evidenced.

Record a non-secret method to establish:

- source ref used for a deployment
- whether Sites remains an independent Git remote/deployment origin
- how future GitHub-reviewed changes reach the live site
- rollback expectations

**Exit criterion:** source state and deployed state can be distinguished without relying on chat history.

## P1 — Production documentation and repository hygiene

### Production README

Replace the generic Vinext starter README through a focused production-repository documentation PR. It should document:

- RT Study Lab purpose
- module map
- install/build/test/lint commands
- package-manager convention
- source vs deployment relationship
- contribution/branch/PR expectations
- clinical/educational validation boundaries

### Package-manager cleanup

Reconcile `package-lock.json`, `pnpm-lock.yaml`, and `pnpm-workspace.yaml` only after confirming which toolchain the Sites/local environment requires. Do not delete lockfiles speculatively.

### Validation records

Add durable validation artifacts or links for:

- full automated test baseline
- clinical review
- accessibility review
- chest-trauma 3D visual/mechanical review

## P1 — Module stabilization priorities

### ECG Rhythm / ACLS

Current production source confirms a substantial engine-backed system: 500 Hz ECG generation, 19 rhythms, Learn/Practice/Exam/Clinical modes, patient state, pathways, treatment, arrest and post-arrest engines.

Next stabilization work should be driven by full-suite execution and current clinical/accessibility review rather than historical test counts.

### Ventilator Waveform Lab

Do not reopen historical P1s merely because they existed historically. Current source addresses them. Use execution evidence to verify, then focus future work on any failures or browser/clinical-review findings actually observed.

### Shock / Oxygen Transport

Current Shock page is a production learning module; the planned oxygen-transport simulation does not exist at the baseline ref.

Treat the future lab as a feature/architecture project, not a bug fix. Before implementation, establish an explicit educational/physiology contract for the intended model, equations, simplifications, validation method, and numerical invariants.

### Interactive Equipment and chest-trauma 3D

Keep these scopes distinct:

- equipment catalog: image/HTML-overlay device lessons
- chest-trauma: integrated R3F/Three.js 3D anatomy/pathology module
- historical Shiley/laryngoscope Blender work: not production-integrated at this ref

Prioritize executable model tests and browser visual/mechanical review before further chest-trauma visual expansion. If Shiley integration is pursued, first version-control the actual source asset, provenance and mechanical acceptance criteria.

### PFT

Current source verifies 12 reconstructed report/loop datasets and test contracts. Next work should follow current test execution plus targeted clinical review of interpretation boundaries and reference assumptions.

### ABG / hemodynamics

ABG is currently a 25-case learning interface, not a general calculation engine. Add tests before substantial case/calculation expansion. Treat any future hemodynamic calculator or Shock physiology engine as a distinct architecture decision.

### Disease processes

Specialized Shock, Stroke, Burns, Chest Trauma, TBI and generic disease pages exist. Prioritize clinical-content review and test coverage based on educational risk rather than uniformly expanding every disease page.

### Respiratory pharmacology and equipment content

Structured source-backed content exists, but dedicated tests were not identified. Future work should emphasize source freshness, content validation, and regression coverage before adding broad new inventories.

## P2 — Documentation durability

- lightweight ADR format for substantive architecture decisions
- defect/clinical-review/feature issue templates once repetition justifies them
- validation-report templates
- deployment/release record after source-to-Sites workflow is established
- project terminology/evidence glossary if README vocabulary becomes insufficient

## Deferred / evidence required

Do not assert the following without new evidence:

- that current GitHub `main` is the exact live Sites deployment
- that the full current test suite passes
- that historical multidisciplinary validation scores remain current
- that source references equal clinical validation
- that accessibility-oriented markup/tests establish WCAG conformance
- that the historical Shiley Blender model is deployed
- that a Shock oxygen-transport engine exists

## Current highest-value next task

**Establish and execute the complete canonical automated test baseline, then add CI around the proven command.**

This has the highest leverage because every future code change depends on knowing whether ECG/ACLS, Ventilator P1 regressions, Shock, PFT and 3D contracts are actually protected by the normal verification path.
