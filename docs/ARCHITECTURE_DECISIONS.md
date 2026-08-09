# Architecture and Project Decisions

This file is the lightweight decision register for RT Study Lab project-control and cross-repository engineering decisions. It is not a substitute for detailed ADRs when a decision has significant technical consequences.

Decision **status** and evidence **basis** are separate concepts. Use the vocabulary defined in the repository `README.md`.

## DEC-001 — Keep project control separate from production application source

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Use `R3C4LL4L1F3/RT-study-lab-project` as the durable project-control repository and `R3C4LL4L1F3/RT-study-lab` as the production source repository. Do not treat either repository as a substitute for the other.

### Rationale

The project needs a stable control plane that survives individual chats, experiments, model revisions, and application implementation changes while allowing implementation claims to be verified against actual source.

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

### Consequence

A historical defect can be preserved without being called current, and passing automated evidence can be recorded without being mislabeled clinical validation.

## DEC-003 — Use branch-and-draft-PR review for project-control changes

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Do not make project-control changes directly to `main`. Use a purpose-specific branch and draft pull request for review.

## DEC-004 — Preserve validation dimensions as distinct concerns

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

Separate, as applicable:

- clinical correctness/plausibility
- engineering/software correctness
- mechanics/simulation behavior
- measurement correctness
- educational clarity/effectiveness
- accessibility
- visual/interaction realism
- deployment/source correspondence

A passing automated suite does not establish the other categories.

## DEC-005 — Keep major learning engines independently reviewable where source supports it

- Status: Accepted
- Evidence basis: Verified against production repository for current ECG/ACLS and Ventilator architecture

### Decision

Preserve separable concerns where the implementation supports them, including ECG waveform generation, patient-state modeling, pathway logic, treatment logic, scoring, Ventilator engine/session behavior, and UI rendering.

### Rationale

Current production source confirms the reported separation in major learning engines, and independent layers are easier to test, audit, and clinically review.

## DEC-006 — Require production evidence before current-defect or resolved status

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

A historical application defect report must not be labeled **Current known issue** or **Resolved** solely from chat history. Current production evidence is required.

When source-level implementation plus executable automated regressions support resolution, record that exact scope. Do not infer browser, clinical, accessibility, or deployment validation from automated results.

## DEC-007 — Use npm as the canonical production repository validation package manager

- Status: Accepted for repository validation
- Evidence basis: Verified against production repository and Issue #6 executable evidence
- Validation ref: production draft PR #1 at `96b5535f9228c7b01c709386e050ce53e68f14d4`

### Decision

Use **npm** and the maintained `package-lock.json` for reproducible production-repository installation and automated validation.

The canonical validation path should:

1. install with `npm ci`;
2. lint;
3. build;
4. discover the complete `tests/**/*.test.mjs` inventory recursively;
5. execute each test file in an isolated Node process;
6. explicitly support direct TypeScript imports at the declared Node 22.13.0 minimum with `--experimental-strip-types`;
7. retain durable GitHub Actions evidence/diagnostics.

### Evidence

Issue #6 established that:

- the repository scripts are npm-oriented;
- `package-lock.json` includes later production dependencies that the older pnpm lockfile does not;
- GitHub Actions run `31309995943` passed `npm ci`, lint, build, the complete 28-file suite, the dedicated Ventilator P1 regression, and artifact upload at the validated PR ref.

### pnpm boundary

Do **not** delete or regenerate `pnpm-lock.yaml` or `pnpm-workspace.yaml` as part of this decision. Their potential role in the ChatGPT Sites/Vinext environment has not yet been verified. Validation-package-manager selection and deployment-tooling cleanup are separate decisions.

### Consequences

- New conforming `tests/**/*.test.mjs` files enter the canonical suite automatically.
- A manually curated fixed subset should not become the default validation path again without an explicit architecture/validation decision.
- Production `main` does not receive this decision's implementation until the draft production PR is explicitly authorized and merged.

## DEC-008 — Keep GitHub validation independent from deployment

- Status: Accepted
- Evidence basis: Production-source and deployment-boundary verification

### Decision

The production GitHub validation workflow must not deploy RT Study Lab or require deployment credentials unless a future, separately reviewed deployment architecture explicitly requires it.

### Rationale

The current GitHub-to-ChatGPT-Sites deployment correspondence is not yet fully established. CI should prove repository quality without silently changing the live site.

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
- package-management/dependency strategy
