# AI-Assisted Development Workflow

RT Study Lab uses AI extensively for planning, implementation support, validation design, 3D/model workflows, documentation, and review. This process must preserve traceability and prevent unverified output from becoming project fact.

## Core rules

1. **Inspect before changing.** Review the current source, issue, PR, validation record, or artifact before proposing edits.
2. **Do not work directly on `main`.** Use a purpose-specific branch.
3. **Do not fabricate state.** Unknown implementation, validation, deployment, test, clinical, or date information remains unknown.
4. **Separate evidence from inference.** Historical chat records are useful project evidence but should be labeled **Reported** until tied to reproducible source/artifacts.
5. **Keep changes reversible.** Avoid destructive edits when a branch, backup, or additive migration is available.
6. **Prefer narrow changes.** Do not combine unrelated refactors, clinical-rule changes, and visual redesigns in one review unit unless there is a documented reason.
7. **Record validation with the change.** A feature is not complete merely because code was generated.

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
- current source/ref/commit
- existing tests
- existing defects or limitations
- screenshots/video/data where behavior is visual or interactive

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
- clinical plausibility review
- educational usability review

The validation record should distinguish automated results from expert/manual review.

### 5. Document evidence

Update the relevant project-control records:

- `PROJECT_STATUS.md`
- `DEVELOPMENT_HISTORY.md`
- `KNOWN_ISSUES.md`
- `VALIDATION_REGISTER.md`
- `ARCHITECTURE_DECISIONS.md` when a durable decision changed
- `ROADMAP.md` when priorities or dependencies changed

### 6. Open a draft PR

A draft PR should contain:

- concise change summary
- rationale
- files/subsystems affected
- validation performed
- validation not performed
- unresolved issues
- screenshots/artifacts where relevant
- clinical/reference notes where relevant

### 7. Review before merge

Do not merge because an AI agent says the work is complete. Review the actual diff, test evidence, unresolved comments, and any clinical assumptions.

## Clinical-content guardrails

For clinically relevant behavior:

- identify the source guideline/reference and version when available
- distinguish guideline facts from implementation choices
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

A work item is ready to move out of draft review only when its implementation state, evidence, unresolved risks, and documentation agree with one another.
