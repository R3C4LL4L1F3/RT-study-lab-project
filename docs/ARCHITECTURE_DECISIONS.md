# Architecture and Project Decisions

This file is the lightweight decision register for RT Study Lab project-control decisions. It is not a substitute for detailed ADRs when a decision has significant technical consequences.

Decision **status** and evidence **basis** are separate concepts. Use the vocabulary defined in the repository `README.md`.

## DEC-001 — Keep project control separate from production application source

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Use this repository as the durable source for project control, development history, roadmap, known issues, validation records, architecture decisions, and AI-development workflow. Do not assume it is the production application source repository.

### Rationale

The project needs a stable control plane that survives individual chats, experiments, model revisions, and application implementation changes.

### Consequences

- Production implementation claims require links or evidence from the actual source/deployment environment.
- Documentation changes can proceed independently of production code.
- This repository must clearly distinguish project-control evidence from production verification.

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
- **Planned work**
- **Historical / possibly superseded**

Historical tables may retain **Reported** as shorthand for project-history information, but Reported does not establish current production behavior.

### Rationale

A fact can be well supported as project history while still being unverified in current production. Likewise, a historical defect report should not automatically become a Current known issue.

### Consequences

- Historical feature/test records can be preserved without being overstated.
- Production status requires direct production-source or durable production evidence.
- Unknown information is recorded as unknown rather than inferred.
- Defect lifecycle is separated from the evidence source used to describe it.

## DEC-003 — Use branch-and-draft-PR review for project-control changes

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Do not make project-control changes directly to `main`. Use a purpose-specific branch and open a draft pull request for review.

### Rationale

This provides a reviewable change history and reduces accidental corruption of the project-control record.

## DEC-004 — Preserve validation dimensions as distinct concerns

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

Future validation records should separate, as applicable:

- clinical plausibility/correctness
- engineering/software correctness
- mechanics/simulation behavior
- measurement correctness
- educational clarity/effectiveness
- accessibility
- visual/interaction realism

### Rationale

A passing software test does not establish clinical correctness, and a clinically plausible visualization does not establish software robustness.

## DEC-005 — Keep major learning engines independently reviewable where source supports it

- Status: Proposed
- Evidence basis: Confirmed from project history; needs verification against production repository

### Decision

Where the production implementation supports it, preserve separable concerns for systems such as ECG waveform generation, patient-state modeling, pathway logic, treatment logic, scoring, and UI rendering.

### Rationale

Independent engines are easier to test, audit, and clinically review than tightly coupled behavior.

### Verification needed

Inspect the production source and convert this entry to Accepted only if the current architecture supports the reported pattern and the decision remains appropriate.

## DEC-006 — Require production evidence before current-defect or resolved status

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

A historical application defect report must not be labeled **Current known issue** or **Resolved** solely from chat history, prior summaries, or this project-control repository. Current production evidence is required for either status.

GitHub issues may track verification tasks before production access exists, but issue creation alone does not confirm the defect.

### Rationale

This prevents stale historical findings from being mistaken for current behavior and prevents unsupported claims that a safety- or correctness-relevant problem has been fixed.

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
