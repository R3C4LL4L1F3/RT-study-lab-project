# AI-Assisted Development Workflow

RT Study Lab uses AI extensively for planning, implementation support, validation design, 3D/model workflows, documentation, and review. This process must preserve traceability and prevent unverified output from becoming project fact.

Use the evidence/lifecycle vocabulary defined in the repository `README.md` and the production audit fields in `PRODUCTION_REPOSITORY_VERIFICATION.md`.

## Core rules

1. **Inspect before changing.** Review the current source, issue, PR, validation record, or artifact before proposing edits.
2. **Do not work directly on `main`.** Use a purpose-specific branch.
3. **Do not fabricate state.** Unknown implementation, validation, deployment, test, clinical, architecture, version, defect-resolution, or date information remains unknown.
4. **Separate project history from production verification.** Historical chat/project records may be **Confirmed from project history** but still **Need verification against production repository**.
5. **Separate evidence from lifecycle.** A historical defect report is not automatically a **Current known issue**, and a prior fix claim is not automatically **Resolved**.
6. **Keep changes reversible.** Avoid destructive edits when a branch, backup, or additive migration is available.
7. **Prefer narrow changes.** Do not combine unrelated refactors, clinical-rule changes, and visual redesigns in one review unit unless there is a documented reason.
8. **Record validation with the change.** A feature is not complete merely because code was generated.
9. **Protect public-repository boundaries.** Do not commit credentials, secrets, patient information, private filesystem paths, or personal/private data.

## Recommended work cycle

### 1. Define the change

Record:

- problem being solved
- affected subsystem
- clinical/educational intent
- technical scope
- explicit non-goals
- acceptance criteria
- known safety/accuracy constraints

### 2. Establish baseline

Before implementation, capture:

- relevant current behavior
- current production repository/path/ref when available
- relevant current source files
- existing tests
- existing defects or limitations
- screenshots/video/data where behavior is visual or interactive
- which statements are project history versus production-verified facts

### 3. Implement on a branch

Use a branch name that describes the work. Keep commits understandable and avoid silently rewriting unrelated project history.

### 4. Validate in layers

Depending on the subsystem, validation may include:

- unit/integration/regression tests
- deterministic scenario tests
- state-machine/pathway tests
- measurement/math verification
- browser/responsive/accessibility review
- visual/mechanical review
- clinical plausibility/correctness review
- educational usability review

The validation record should distinguish automated results from expert/manual review and should state the production source ref to which the evidence applies.

### 5. Reconcile history with source

When the work involves an existing RT Study Lab module:

- locate the implementation in the production repository
- inspect architecture rather than assuming it from prior chat history
- compare historical claims with current source
- classify each material claim as confirmed, refuted, superseded, still unverified, or newly observed
- reproduce high-risk historical defect reports where feasible
- do not mark a defect Current or Resolved without current evidence

Use `PRODUCTION_REPOSITORY_VERIFICATION.md` for the module-level record.

### 6. Document evidence

Update the relevant project-control records:

- `PROJECT_STATUS.md`
- `PRODUCTION_REPOSITORY_VERIFICATION.md`
- `DEVELOPMENT_HISTORY.md`
- `KNOWN_ISSUES.md`
- `VALIDATION_REGISTER.md`
- `ARCHITECTURE_DECISIONS.md` when a durable decision changed
- `ROADMAP.md` when priorities or dependencies changed

### 7. Open a draft PR

A draft PR should contain:

- concise change summary
- rationale
- files/subsystems affected
- source ref or baseline used
- validation performed
- validation not performed
- unresolved issues
- screenshots/artifacts where relevant
- clinical/reference notes where relevant

### 8. Review before merge

Do not merge because an AI agent says the work is complete. Review the actual diff, test evidence, unresolved comments, production-source traceability, and any clinical assumptions.

## Clinical-content guardrails

For clinically relevant behavior:

- identify the source guideline/reference and version when available and actually verified
- distinguish guideline facts from implementation choices
- do not invent equations, thresholds, medication values, or clinical rules to fill missing source information
- do not treat visual plausibility as clinical validation
- do not treat passing unit tests as clinical validation
- record uncertainty and scope limits
- require re-review when guideline logic or clinically meaningful calculations change

## 3D / interactive-equipment guardrails

For medical-device models and animations:

- record source/provenance and license for external assets
- preserve original source assets when possible
- distinguish geometry accuracy from animation accuracy
- distinguish educational simplification from device-realistic behavior
- use consistent anatomical/device orientation terminology
- retain review renders or comparable evidence for major revisions
- verify clipping/intersections and mechanical constraints rather than relying on a single viewing angle
- verify browser/runtime suitability separately from Blender/source-asset quality

## Prompt and conversation retention

Important prompts and AI-generated decisions should be converted into durable repository records when they affect:

- architecture
- clinical behavior
- acceptance criteria
- validation methodology
- known defects
- roadmap priorities

Chat history alone should not be the only durable record for a consequential project decision.

## Completion standard

A work item is ready to move out of draft review only when its implementation state, evidence basis, lifecycle/disposition, unresolved risks, and documentation agree with one another.
