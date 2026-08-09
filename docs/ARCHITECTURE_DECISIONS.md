# Architecture and Project Decisions

This file is the lightweight decision register for RT Study Lab project-control decisions. It is not a substitute for detailed ADRs when a decision has significant technical consequences.

## DEC-001 — Keep project control separate from production application source

- Status: Accepted
- Evidence state: Repository-verified

### Decision

Use this repository as the durable source for project control, development history, roadmap, known issues, validation records, architecture decisions, and AI-development workflow. Do not assume it is the production application source repository.

### Rationale

The project needs a stable control plane that survives individual chats, experiments, model revisions, and application implementation changes.

### Consequences

- Production implementation claims require links or evidence from the actual source/deployment environment.
- Documentation changes can proceed independently of production code.
- This repository must clearly distinguish evidence states.

## DEC-002 — Use evidence states for implementation and validation claims

- Status: Accepted
- Evidence state: Repository-verified

### Decision

Classify material project claims as **Repository-verified**, **Reported**, **Proposed**, or **Unknown**.

### Rationale

RT Study Lab includes clinical education, simulation behavior, automated tests, and AI-assisted development. Treating historical conversation output as equivalent to reproducible validation would create false confidence.

### Consequences

- Historical feature/test records can be preserved without being overstated.
- Validation records require traceable evidence before promotion to repository-verified status.
- Unknown information is recorded as unknown rather than inferred.

## DEC-003 — Use branch-and-draft-PR review for project-control changes

- Status: Accepted
- Evidence state: Repository-verified

### Decision

Do not make project-control changes directly to `main`. Use a purpose-specific branch and open a draft pull request for review.

### Rationale

This provides a reviewable change history and reduces accidental corruption of the project-control record.

## DEC-004 — Preserve clinical, engineering, and educational validation as distinct concerns

- Status: Accepted
- Evidence state: Proposed control standard based on project needs

### Decision

Future validation records should separate:

- clinical plausibility/correctness
- engineering/software correctness
- mechanics/simulation behavior
- measurement correctness
- educational clarity/effectiveness
- visual/interaction realism where relevant

### Rationale

A passing software test does not establish clinical correctness, and a clinically plausible visualization does not establish software robustness.

## DEC-005 — Keep major learning engines independently reviewable

- Status: Proposed
- Evidence state: Reported architecture pattern, pending source verification

### Decision

Where the production implementation supports it, preserve separable concerns for systems such as ECG waveform generation, patient-state modeling, pathway logic, treatment logic, scoring, and UI rendering.

### Rationale

Independent engines are easier to test, audit, and clinically review than tightly coupled behavior.

### Verification needed

Inspect the production source and convert this entry to Accepted/Repository-verified only if the current architecture supports the reported pattern.

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
