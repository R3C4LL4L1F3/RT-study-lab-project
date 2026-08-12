# AI-Assisted Development Workflow

RT Study Lab uses AI extensively for planning, implementation support, validation design, 3D/model workflows, documentation and review. This process must preserve traceability and prevent unverified output from becoming project fact.

Use the evidence/lifecycle vocabulary defined in the repository `README.md`, the canonical queue in `MASTER_PROJECT_QUEUE.md`, and the production audit fields in `PRODUCTION_REPOSITORY_VERIFICATION.md`.

## Core rules

1. **Inspect before changing.** Review the current source, issue, PR, validation record or artifact before proposing edits.
2. **Do not work directly on `main`.** Use a purpose-specific branch/PR.
3. **Do not fabricate state.** Unknown implementation, validation, deployment, test, clinical, architecture, version, defect-resolution or date information remains unknown.
4. **Separate project history from production verification.** Historical chat/project records may be **Confirmed from project history** but still require production evidence for current claims.
5. **Separate evidence from lifecycle.** A historical defect report is not automatically a **Current known issue**, and a prior fix claim is not automatically **Resolved** across every validation layer.
6. **Keep changes reversible.** Avoid destructive edits when a branch, backup or additive migration is available.
7. **Prefer narrow changes.** Do not combine unrelated refactors, clinical-rule changes and visual redesigns without a documented reason.
8. **Record validation with the change.** A feature is not complete merely because code was generated.
9. **Protect public-repository boundaries.** Do not commit credentials, secrets, patient information, private filesystem paths, private Site identifiers/URLs unnecessarily, or personal/private data.
10. **Honor the canonical execution sequence.** Recording approved future work is not permission to execute it early.
11. **Route work to the correct subsystem owner.** Do not migrate specialized simulators into Interactive Models merely because they are interactive.

## Canonical execution sequence

1. Durable project-control baseline
2. Close existing Tier 3 validation
3. Establish independent clinical validation
4. Strengthen production/release controls
5. Specify Interactive Models architecture
6. Implement the first validated reusable physiology model
7. Expand only after the framework proves stable

If a later item is already recorded in GitHub, its issue/queue entry remains a planning artifact until its sequence/dependency gates are satisfied.

## Subsystem ownership / routing

### Interactive Models & Simulation Lab

Use for general physiology/pathophysiology simulations where the central problem is a changing clinical state or coupled physiologic variables.

Forward Shock routing:

**Interactive Models & Simulation Lab — Shock / Circulation**

Related future framework-dependent model classes may include oxygen transport, hemodynamics, V/Q, gas exchange, pulmonary circulation, PE physiology, ARDS physiology and heart-failure physiology.

The former standalone Shock circulation-simulator chat name may remain in historical records where needed for chronology.

### Keep these specialized systems separate

**Ventilator — Waveform Lab** owns:

- ventilator mechanics;
- pressure/flow/volume waveform generation;
- triggering/cycling;
- patient effort and ventilator asynchronies;
- ventilator-specific simulation.

**ECG & ACLS Lab** owns:

- ECG waveform engine/rhythms;
- ECG measurement/caliper behavior;
- patient-state engine for ACLS workflows;
- ACLS pathways/treatment/scoring.

**3D Equipment Lab** owns:

- device geometry;
- Blender/source-model workflows;
- GLB production;
- 3D equipment animation/mechanical interaction.

## Tier 3 Interactive Models gate

Issue #9 is **approved for specification; implementation is not approved**.

Do not begin production Interactive Models implementation until both are approved:

1. **Clinical/model contract** from Clinical Validation & Sources; and
2. **Reusable architecture/model contract** from Planning / Architecture with independent review.

Required architecture/specification evidence includes:

- deterministic cases;
- invariants;
- boundary/invalid-state behavior;
- long-run expectations;
- reset/replay behavior;
- seed/reproducibility behavior;
- serialization/snapshot expectations;
- explicit calculated/derived/approximated/illustrative variable classification;
- source-grounded clinical equations/assumptions.

The approved dependency chain is:

**Clinical evidence/model definition**
→ **Interactive Models architecture/model contract**
→ **reusable framework implementation**
→ **Shock / Circulation / Oxygen Transport first-model validation**
→ **additional physiology models**

Do not create an Interactive Models production branch during specification-only work.

## Recommended work cycle

### 1. Define the change

Record:

- problem being solved;
- affected subsystem and owning chat;
- queue priority/status/risk when established;
- clinical/educational intent;
- technical scope;
- explicit non-goals;
- dependencies/gates;
- acceptance criteria;
- safety/accuracy constraints.

### 2. Establish baseline

Before implementation or validation, capture:

- current production repository/path/ref;
- current behavior where relevant;
- relevant source files/tests;
- current CI state;
- existing defects/limitations/verification gaps;
- screenshots/video/data for visual or interactive behavior when needed;
- which statements are project history versus production-verified facts.

### 3. Confirm execution authorization

Before creating an implementation branch, verify that the queue state and dependency gates permit implementation.

Examples:

- An open validation issue does not automatically authorize a fix branch.
- A future policy issue does not authorize branch-protection changes.
- An Interactive Models architecture issue does not authorize production implementation.
- A clinical-validation discrepancy must be established before creating an ECG/ACLS or Ventilator fix branch.

### 4. Implement on a branch

Use a branch name that describes the approved work. Keep commits understandable and avoid silently rewriting unrelated project history.

### 5. Validate in layers

Depending on the subsystem, validation may include:

- unit/integration/regression tests;
- deterministic scenario tests;
- state-machine/pathway tests;
- measurement/math verification;
- invariant/boundary/long-run simulation tests;
- browser/responsive/accessibility review;
- visual/mechanical review;
- clinical plausibility/correctness review;
- educational usability review.

Record automated evidence separately from manual/expert evidence and tie material evidence to the applicable source ref.

### 6. Reconcile history with source

When work involves an existing module:

- locate implementation in production;
- inspect architecture rather than assuming it from chat history;
- compare historical claims with current source;
- classify material claims as confirmed, refuted, superseded, still unverified or newly observed;
- reproduce high-risk historical defect reports where feasible;
- do not mark a defect Current or fully Resolved without appropriate evidence.

### 7. Document evidence

Update affected project-control records:

- `MASTER_PROJECT_QUEUE.md`
- `PROJECT_STATUS.md`
- `PRODUCTION_REPOSITORY_VERIFICATION.md`
- `DEVELOPMENT_HISTORY.md`
- `KNOWN_ISSUES.md`
- `VALIDATION_REGISTER.md`
- `ARCHITECTURE_DECISIONS.md` when a durable decision changed
- `ROADMAP.md` when dependencies/sequence/status changed

### 8. Open a PR

A PR should contain:

- concise change summary;
- rationale;
- files/subsystems affected;
- source ref/baseline used;
- validation performed;
- validation not performed;
- unresolved issues;
- screenshots/artifacts where relevant;
- clinical/reference notes where relevant.

### 9. Review before merge

Do not merge because an AI agent says work is complete. Review the actual diff, executable evidence, unresolved comments, source traceability, clinical assumptions and project-control consistency.

## Clinical-content guardrails

For clinically relevant behavior:

- identify the authoritative source/guideline and version/date actually reviewed;
- distinguish clinical facts from implementation choices and educational simplifications;
- do not invent equations, thresholds, medication values or clinical rules to fill missing source information;
- do not treat visual plausibility or automated tests as independent clinical validation;
- record uncertainty/conflicts/scope limits;
- require re-review when clinically meaningful logic/calculations change.

Issue #10 owns the reusable independent clinical-validation framework. Initial P1 module validation begins with ECG/ACLS and Ventilator; neither is considered clinically validated merely because software tests pass.

## Accessibility guardrails

Issue #11 owns the reusable accessibility-validation baseline.

Where applicable, validate:

- keyboard operation;
- focus visibility/order/trapping/restoration;
- semantic structure/control names;
- status/error/feedback announcements;
- responsive behavior;
- reduced-motion behavior;
- manual accessibility review;
- assistive-technology review where practical.

Accessibility-oriented source/tests are evidence inputs, not comprehensive conformance by themselves.

## 3D / interactive-equipment guardrails

For medical-device models and animations:

- record source/provenance/license;
- preserve original source assets when possible;
- distinguish geometry accuracy from animation/mechanical accuracy;
- distinguish educational simplification from device-realistic behavior;
- use consistent anatomical/device orientation terminology;
- retain review renders/comparable evidence for major revisions;
- verify clipping/intersections/mechanical constraints;
- verify browser/runtime suitability separately from Blender/source-asset quality.

Issue #5 remains a validation issue. Do not create a 3D production fix branch until manual/runtime QA establishes a current defect.

## Repository/release guardrails

Issue #12 records approved future branch/release governance work.

During record-only synchronization or before the approved sequence point:

- do not enable/change production branch protection;
- do not create production tags or GitHub Releases;
- do not delete completed validation branches;
- do not alter deployment behavior;
- do not modify pnpm artifacts without platform evidence.

Issue #8 must establish authoritative deployment-to-Git correspondence before a release record can reliably identify the live deployment.

## Prompt and conversation retention

Important prompts and AI-generated decisions should be converted into durable repository records when they affect architecture, clinical behavior, acceptance criteria, validation methodology, known defects, roadmap/queue priorities, work ownership or execution gates.

Chat history alone should not be the only durable record for a consequential project decision.

## Completion standard

A work item is ready to leave draft/review only when its implementation state, queue state, evidence basis, lifecycle/disposition, unresolved risks and documentation agree.

A green automated suite is necessary evidence for many production changes, but RT Study Lab is not considered release-mature until applicable clinical, accessibility, manual/runtime and deployment/release-control evidence is also satisfied.

## Controlled governance migration overlay

`RTSL-KERNEL-AUTONOMY-001` is approved for controlled adoption and is **ACTIVE** by the explicit MASTER PROJECT CONTROL decision recorded in PR #30 comment [`#issuecomment-5253465946`](https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/30#issuecomment-5253465946) at `2026-08-11T12:56:49Z`, after verified merged `main` `e97a83b984f96d51dc7c3a29789eee2be7e52a9f`. The adoption record's earlier `NOT YET ACTIVE` wording is the preserved pre-activation preparation state. The existing Project Operating Kernel and current policy remain authoritative for controls not superseded by the amendment; activation does not make CI, merge, QA, clinical, release, or closure evidence automatic. The durable adoption record, source-inspected conflict register, operating-manual amendment, and role-contract amendment are under `docs/governance/`.

Within an already-authorized bounded task, the implementation owner may continue through ordinary inspection, edits, tests, branch, PR, CI, provenance, and documentation milestones without returning to MASTER for each internal milestone. `PR_OPEN` is not a handoff requirement; GitHub approval is not merge authority, independent QA, or activation authority. Tier 0–1 work is normally self-validation-sufficient, Tier 2 independence is conditional on an authoritative contract, and Tier 3 independence remains mandatory. Bounded-task `COMPLETE` does not mean project release or closure. Any PAUSED or BLOCKED record must carry one exact resume/unblock condition and evidence.
