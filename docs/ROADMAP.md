# Roadmap

This roadmap distinguishes verified project-control work, production-source work, validation work, and future product development.

## P0 — Land the validated production verification path

Issue #6 has established and successfully executed a complete production validation path on a draft production PR.

### Current validated state

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Baseline `main`: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Validation branch: `validation/issue-6-test-baseline`
- Production draft PR: #1 — `Establish complete production validation baseline`
- Validated PR ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Successful Actions run: `31309995943`
- Canonical validation package manager: **npm**
- Locked install, lint, build, complete 28-file suite, dedicated Ventilator P1 regression and diagnostic artifact upload: **PASS**

### Remaining P0 action

- Review production PR #1.
- Merge it only after explicit maintainer authorization.
- After merge, confirm the workflow executes successfully from production `main`.

**Exit criterion:** the validated complete-suite command and GitHub CI are present on production `main` with a successful post-merge run.

## P0 — Establish source-to-live deployment correspondence

GitHub now provides a durable production-source repository, but the live ChatGPT Sites deployment has not been tied to an exact GitHub commit through durable evidence.

Required work:

- determine the safe/official relationship between the GitHub source copy and the ChatGPT Sites source/deployment path;
- establish how a reviewed GitHub change becomes a live Sites change;
- record the deployed source ref when that can be established without exposing internal credentials/tokens;
- keep source verification and live deployment verification separate until then.

**Exit criterion:** a maintainer can identify which source ref produced the live site and how reviewed changes move between GitHub and the deployment environment.

## P1 — Complete targeted runtime/browser verification

### Ventilator Waveform Lab — Issue #3

Automated source-level and regression verification is now established on the Issue #6 PR ref. Remaining browser checks:

- historical VC/PC breath labels after mode transitions;
- expiratory-hold controls across later breaths;
- dynamic-compliance contaminated/invalid messaging;
- double-trigger visual behavior and learner-facing minute-ventilation display.

If the browser checks agree with the passing regressions, Issue #3 can be closed with evidence. If they disagree, create a narrowly scoped current defect.

### Interactive Equipment / chest-trauma 3D — Issue #5

Automated chest-trauma 3D/model/visual source tests passed in the Issue #6 complete suite. Remaining manual/browser checks:

- clipping and intersections;
- morph/progression visual fidelity;
- camera controls and labels;
- mobile/responsive behavior;
- reduced motion;
- performance/runtime stability;
- educational/anatomical visual review.

Historical Shiley Blender work remains outside production. If integration is pursued, first version-control the actual model/source assets, provenance/license, snap-lock acceptance criteria, and browser implementation plan.

## P1 — Clinical and accessibility evidence program

Automated software validation is now reproducible; this makes the remaining non-software evidence gaps clearer.

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

After the validation PR and deployment contract are settled:

- replace the starter-oriented production README with an RT Study Lab architecture/contributor overview;
- decide whether retained pnpm artifacts are required by Sites/Vinext before deleting or regenerating them;
- add issue/PR templates when repeated use justifies them;
- add release/deployment records once deployment versioning is established;
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

- live-site deployment synchronization;
- independent current clinical validation;
- comprehensive accessibility conformance;
- manual mechanical/visual 3D validation;
- production integration of the Shiley model;
- post-merge CI on production `main` before the production PR is actually merged.
