# RT Study Lab — Project Control

This repository is the durable project-control and documentation home for **RT Study Lab**.

The production application source is maintained separately in the private repository `R3C4LL4L1F3/RT-study-lab`. This project-control repository preserves development history, current status, roadmap, known issues, architecture decisions, validation records, and the AI-assisted development workflow without duplicating the application source.

## Repository boundary

This repository should answer:

- What is RT Study Lab trying to accomplish?
- What is confirmed from project history?
- What has been verified against current production source?
- What remains unresolved or requires runtime/clinical/accessibility/deployment verification?
- What architectural or workflow decisions have been made?
- What should be worked on next?

It should not become a substitute for the production application repository.

## Production source baseline

- Production repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility: Private
- Default branch: `main`
- Baseline verification ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Baseline commit message: `Redesign Shock visual teaching page`

The GitHub production source is now directly inspectable. Current synchronization between that GitHub ref and the live ChatGPT Sites deployment is **not yet verified** and must be tracked separately.

## Evidence and work-state vocabulary

Material claims should separate **where the evidence comes from** from **what the work currently means**.

### Evidence basis

- **Project-control verified** — directly observable in this repository, such as branches, pull requests, issues, documentation, or artifacts stored here. This does not imply application behavior was verified.
- **Confirmed from project history** — preserved from prior RT Study Lab development records or maintainer-provided history, but not necessarily reconciled against current production source.
- **Verified against production repository** — confirmed by inspecting `R3C4LL4L1F3/RT-study-lab` at a recorded ref/commit and, where relevant, associated source-controlled tests/assets/configuration.
- **Needs verification against production repository** — a claim cannot yet be established from current source.
- **Unknown** — information has not been established.

Historical tables may still use **Reported** as shorthand for project-history information. A Reported item is not automatically a current production fact.

### Lifecycle / disposition

- **Current known issue** — reproduced or otherwise confirmed with current evidence.
- **Resolved in current source; runtime re-execution required** — current implementation and regression source address a historical defect, but the relevant current test/runtime evidence has not yet been executed/retained.
- **Planned work** — intended future work; not an implementation claim.
- **Historical / possibly superseded** — retained because it matters to project history or verification, but it may no longer describe the current product.

Clinical validation, test pass state, deployment state, accessibility conformance, defect resolution, version numbers, and dates must not be promoted beyond their evidence.

## Current repository state

- Default branch: `main`
- Working branch for the project-control foundation/baseline: `setup/project-control-foundation`
- Draft PR: #1 into `main`; do not merge until reviewed
- Production application source: **identified and source-baselined**
- Production GitHub CI: no `.github/workflows` workflow identified at the baseline ref
- Project-control CI: none identified
- Current highest-priority repository risk: canonical `npm test` executes only a subset of the source-controlled test inventory

## Documentation index

- [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) — current project/module status
- [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md) — sequence-oriented development record
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — priorities, dependencies, and next work
- [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md) — confirmed risks, historical defect dispositions, and verification concerns
- [`docs/VALIDATION_REGISTER.md`](docs/VALIDATION_REGISTER.md) — current/historical validation and test evidence
- [`docs/ARCHITECTURE_DECISIONS.md`](docs/ARCHITECTURE_DECISIONS.md) — project and architecture decision log
- [`docs/AI_DEVELOPMENT_WORKFLOW.md`](docs/AI_DEVELOPMENT_WORKFLOW.md) — guardrails for AI-assisted development
- [`docs/PRODUCTION_REPOSITORY_VERIFICATION.md`](docs/PRODUCTION_REPOSITORY_VERIFICATION.md) — source-backed production baseline and remaining verification work

## Change workflow

1. Inspect production source and relevant project records before editing.
2. Do not make meaningful application changes directly on production `main`; use focused branches and PRs.
3. Do not make project-control changes directly on this repository's `main`.
4. Preserve evidence state: source inspection is not equivalent to runtime execution or clinical validation.
5. Update affected project-control records when production evidence changes project status.
6. Keep secrets, credentials, PHI, private filesystem paths, and private personal data out of repositories.
7. Use draft PRs for meaningful changes and review diffs before merge.

## Immediate control objective

The source-discovery baseline is established. The next highest-value phase is **Reproducible Production Validation**:

1. decide/document the canonical package manager;
2. make the canonical test command cover the intended current suite, including high-risk regression tests;
3. execute build/lint/full tests at a recorded source ref;
4. add durable GitHub CI around the proven commands;
5. then continue clinical, accessibility, deployment, and 3D mechanical/visual verification as separate evidence tracks.
