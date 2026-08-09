# Architecture and Project Decisions

This file is the lightweight decision register for RT Study Lab project-control decisions. It is not a substitute for detailed ADRs when a decision has significant technical consequences.

Decision **status** and evidence **basis** are separate concepts. Use the vocabulary defined in the repository `README.md`.

## DEC-001 — Keep project control separate from production application source

- Status: Accepted
- Evidence basis: Project-control verified; production boundary now source-verified

### Decision

Use `R3C4LL4L1F3/RT-study-lab-project` as the durable project-control repository and the private `R3C4LL4L1F3/RT-study-lab` repository as the durable production application source. Do not duplicate application source into the control repository.

### Rationale

The project needs a stable control plane that survives individual chats, experiments, model revisions, and application implementation changes while still allowing source-backed verification.

### Consequences

- Application implementation claims cite the production repository and a source ref.
- Project status/history/issues/validation are maintained here.
- GitHub source state and live ChatGPT Sites deployment state remain distinct until deployment evidence connects them.

## DEC-002 — Separate evidence basis from lifecycle/disposition

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Material project records should distinguish evidence basis from lifecycle/disposition.

Evidence basis includes:

- **Project-control verified**
- **Confirmed from project history**
- **Verified against production repository**
- **Needs verification against production repository**
- **Unknown**

Lifecycle/disposition includes, where relevant:

- **Current known issue**
- **Resolved in current source; runtime re-execution required**
- **Planned work**
- **Historical / possibly superseded**

Historical tables may retain **Reported** as shorthand for project-history information, but Reported does not establish current production behavior.

### Rationale

Source presence, runtime execution, historical evidence, clinical validation and deployment evidence are different kinds of proof.

## DEC-003 — Use branch-and-draft-PR review for project-control changes

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Do not make project-control changes directly to `main`. Use a purpose-specific branch and a draft pull request for review.

## DEC-004 — Preserve validation dimensions as distinct concerns

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

Future validation records should separate, as applicable:

- automated software correctness
- clinical plausibility/correctness
- mechanics/simulation behavior
- measurement correctness
- educational clarity/effectiveness
- accessibility
- visual/interaction realism
- deployment verification

A software test is not clinical validation; accessibility-oriented markup is not WCAG conformance; source state is not deployment state.

## DEC-005 — Keep major learning engines independently reviewable where source supports it

- Status: Accepted
- Evidence basis: **Verified against production repository** at `a0495e9fa4e5437d8a027312b618b5c1c389ef94`

### Decision

Preserve separable concerns for engine-backed learning systems where the current architecture already supports that separation.

### Production evidence

The ECG/ACLS source separates waveform generation, rhythm definitions, calipers, practice/exam, patient state, clinical scenarios, pathways, treatment, arrest/post-arrest and UX/workspace layers. The Ventilator source likewise separates engine, triggering, monitoring, patient profiles, scenario/configuration state, rendering, breath/provenance logic and live-session state.

### Rationale

Independent modules are easier to test, audit, clinically review and change without coupling unrelated behavior.

## DEC-006 — Require current evidence before current-defect or resolved status

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

A historical defect must not be labeled **Current known issue** or **Verified resolved** solely from project history. Current production evidence is required.

When source implementation plus dedicated regression source clearly addresses a historical defect but the regression has not been re-executed, use **Resolved in current source; runtime re-execution required**.

### Rationale

This prevents both stale defect claims and unsupported claims of passing resolution.

## DEC-007 — Establish reproducible full-suite validation before expanding CI

- Status: Accepted
- Evidence basis: **Verified against production repository** baseline

### Decision

Before adding GitHub CI as a gate, first establish the canonical package manager and a deliberate full-suite local test command that reflects the current source-controlled test inventory. CI should automate a proven command rather than codify an incomplete/default subset accidentally.

### Production evidence

At the baseline ref, `npm test` builds and runs only five selected test files while additional high-value ECG/ACLS, Ventilator Session 3.5.2, Shock and chest-trauma suites exist. No `.github/workflows` workflow was identified.

### Consequences

- Test-command reconciliation is the first production-repository implementation task after this source audit.
- CI design follows the command/package-manager decision.
- Ventilator historical P1s remain source-resolved but not freshly execution-verified until their regression file runs.

## DEC-008 — Treat Shock/Oxygen Transport simulation as a new feature boundary, not an existing engine repair

- Status: Accepted
- Evidence basis: **Verified against production repository** at `a0495e9...`

### Decision

The current Shock page is an educational learning module. Its `ShockInteractiveLabSlot` explicitly states that the physiology simulation is not implemented. Future oxygen-transport simulation work therefore requires a deliberate architecture/clinical-model decision rather than assuming an existing circulation engine should be repaired or extended.

### Consequences

Any future implementation should establish the educational contract, equations, simplifications, invariants, numerical-validation plan and clinical-review boundary before coding.

## Future ADR threshold

Create a dedicated ADR when a decision materially changes one or more of the following:

- clinical model or guideline interpretation
- state-machine behavior
- simulation math
- data model/schema
- framework/runtime
- deployment architecture
- persistence/storage
- 3D asset pipeline
- accessibility architecture
- test/validation strategy
