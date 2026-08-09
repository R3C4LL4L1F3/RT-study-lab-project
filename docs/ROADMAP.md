# Roadmap

This roadmap distinguishes verified project-control work, production-source work, deployment verification, validation work, and future product development.

## Completed infrastructure baseline

### Issue #6 — Complete production validation path

Completed and merged.

Production `main` now contains:

- npm as the canonical reproducible validation package manager;
- locked install with `npm ci`;
- lint;
- Vinext production build;
- recursive discovery/execution of the complete source-controlled `tests/**/*.test.mjs` inventory;
- dedicated Ventilator historical-P1 regression;
- diagnostic validation artifact upload;
- GitHub Actions `Production Validation` workflow.

### Issue #7 — Automatic validation after merges to main

Completed and merged.

Current production `main`:

- `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- `Run production validation on main pushes (#2)`

The Issue #7 merge automatically triggered `Production Validation` on `main` as Actions run `31311314980`, and the complete validation path passed.

## P0 — Establish source-to-live deployment correspondence — Issue #8

GitHub now provides a durable production-source repository with repeatable CI, but the live ChatGPT Sites deployment is not yet tied to an exact GitHub commit through durable evidence.

### Verified mechanism

Production source contains `.openai/hosting.json`, linking the local source project to a provisioned Sites project. The private project identifier must not be copied into public project-control records.

Current official ChatGPT Sites documentation establishes that:

- a Sites project links local source to Sites hosting;
- publishing separates **save version** from **deploy version**;
- a saved local-source Site version is associated with the Git commit used for its build;
- saved versions can be listed/inspected;
- deployment publishes a selected saved version rather than occurring automatically from GitHub changes.

### Required work

- open the RT Study Lab Site in ChatGPT Sites management;
- list/inspect saved versions;
- identify the version currently deployed;
- record the associated Git commit without exposing private Site identifiers;
- verify that commit exists in `R3C4LL4L1F3/RT-study-lab`;
- compare the deployed commit with current GitHub `main`;
- if they differ, classify the difference before any deployment action;
- define the release rule: validated Git commit -> saved Sites version -> reviewed candidate -> explicit deploy -> post-deploy verification.

**Exit criterion:** a maintainer can identify the Git commit associated with the active Site deployment and can describe how a reviewed GitHub revision becomes a saved/reviewed/deployed Sites version.

Do not redeploy simply to manufacture correlation evidence.

## P1 — Complete targeted runtime/browser verification

### Ventilator Waveform Lab — Issue #3

Automated source-level and regression verification is established and repeatedly passing. Remaining browser checks:

- historical VC/PC breath labels after mode transitions;
- expiratory-hold controls across later breaths;
- dynamic-compliance contaminated/invalid messaging;
- double-trigger visual behavior and learner-facing minute-ventilation display.

If browser checks agree with the passing regressions, Issue #3 can be closed with evidence. If they disagree, create a narrowly scoped current defect.

### Interactive Equipment / chest-trauma 3D — Issue #5

Automated chest-trauma 3D/model/visual source tests pass. Remaining manual/browser checks:

- clipping and intersections;
- morph/progression visual fidelity;
- camera controls and labels;
- mobile/responsive behavior;
- reduced motion;
- performance/runtime stability;
- educational/anatomical visual review.

Historical Shiley Blender work remains outside production. If integration is pursued, first version-control the actual model/source assets, provenance/license, snap-lock acceptance criteria, and browser implementation plan.

## P1 — Clinical and accessibility evidence program

Automated software validation is reproducible; the remaining non-software evidence gaps are therefore explicit.

Prioritize:

- clinically meaningful calculations and safety-sensitive pathway/treatment assumptions;
- ECG/ACLS guideline-source reconciliation and clinical review;
- Ventilator mechanics/measurement teaching assumptions;
- PFT interpretation boundaries;
- disease/pharmacology high-risk statements;
- accessibility review of major interactive labs using keyboard and assistive-technology workflows.

Do not treat passing CI as clinical or accessibility validation.

## P1 — Shock / Oxygen Transport future simulation

Current production evidence establishes that the planned Shock/Oxygen Transport simulation is **not implemented**. The historical reduced-model reconciliation concern is superseded.

Before implementation:

1. define the educational and clinical model contract;
2. distinguish calculated, derived, approximated and illustrative variables;
3. define Hb/CaO2/DO2/VO2/CvO2-SvO2/extraction/oxygen-debt relationships from verified sources;
4. define numerical/conservation acceptance criteria;
5. write an architecture decision before adding the simulation engine.

This is planned feature work, not repair of an existing production engine.

## P2 — Production repository documentation and hygiene

After the deployment contract is settled:

- replace the starter-oriented production README with an RT Study Lab architecture/contributor overview;
- decide whether retained pnpm artifacts are required by Sites/Vinext before deleting or regenerating them;
- add issue/PR templates when repeated use justifies them;
- add release/deployment records keyed to the verified Sites saved-version/Git-commit model;
- add durable clinical/accessibility/manual-validation templates.

## P2 — Product stabilization and expansion

Use production evidence to prioritize future work rather than historical assumptions. Candidate workstreams include:

- ECG/ACLS refinement after current clinical/browser review;
- Ventilator feature refinement after Issue #3 closure;
- chest-trauma 3D refinement after Issue #5 closure;
- PFT/ABG improvements based on current source/test gaps;
- disease-process content improvements;
- respiratory pharmacology validation/expansion;
- equipment/oxygen-device interactive development;
- deliberate integration of external 3D equipment models where educational value justifies it.

## Deferred / evidence-sensitive claims

Do not claim completion without corresponding evidence for:

- exact live-site deployment synchronization until Issue #8 is complete;
- independent current clinical validation;
- comprehensive accessibility conformance;
- manual mechanical/visual 3D validation;
- production integration of the Shiley model.
