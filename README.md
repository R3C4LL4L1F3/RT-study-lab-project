# RT Study Lab — Project Control

This repository is the durable project-control and documentation home for **RT Study Lab**.

It is intentionally separate from any production application source repository unless that source is explicitly linked here later. Its purpose is to preserve development history, current status, roadmap, known issues, architecture decisions, validation records, and the AI-assisted development workflow.

## Repository boundary

This repository should answer:

- What is RT Study Lab trying to accomplish?
- What is confirmed from project history?
- What has been verified against the current production source?
- What remains unresolved or needs production verification?
- What architectural or workflow decisions have been made?
- What should be worked on next?

It should **not** silently become a substitute for the production application repository.

## Evidence and work-state vocabulary

Material claims should separate **where the evidence comes from** from **what the work currently means**.

### Evidence basis

- **Project-control verified** — directly observable in this repository, such as branches, pull requests, issues, documentation, or artifacts stored here. This does **not** imply that production application behavior has been verified.
- **Confirmed from project history** — preserved from prior RT Study Lab development records or maintainer-provided history, but not yet reconciled against the current production repository.
- **Verified against production repository** — confirmed by inspecting the identified production source at a recorded ref/commit and, where relevant, associated tests or durable validation evidence.
- **Needs verification against production repository** — the claim, defect, architecture statement, or implementation status cannot yet be confirmed from current production source.
- **Unknown** — information has not been established.

Historical tables may still use **Reported** as shorthand for project-history information. A Reported item must not be treated as current production fact unless it is separately marked **Verified against production repository**.

### Lifecycle / disposition

- **Current known issue** — reproduced or otherwise confirmed against the current production implementation, with current evidence.
- **Planned work** — intended future work; not an implementation claim.
- **Historical / possibly superseded** — retained because it matters to project history or verification, but it may no longer describe the current product.

Clinical validation, implementation status, test results, deployment status, defect resolution, version numbers, and dates must not be promoted to production-verified status without supporting evidence.

## Current repository state

As of the project-control foundation audit:

- Default branch: `main`
- Working branch for this foundation: `setup/project-control-foundation`
- Production application source repository: **Needs verification against production repository / not identified through the current GitHub connection**
- CI configuration in this project-control repository: **None identified**
- Issue history before project-control setup: **None identified**
- Pull-request history before project-control setup: **None identified**

## Documentation index

- [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) — current project-control and module status
- [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md) — sequence-oriented historical development record
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — priorities, dependencies, and next work
- [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md) — current control gaps, historical defect reports, and verification concerns
- [`docs/VALIDATION_REGISTER.md`](docs/VALIDATION_REGISTER.md) — validation and test claims with evidence state
- [`docs/ARCHITECTURE_DECISIONS.md`](docs/ARCHITECTURE_DECISIONS.md) — project and architecture decision log
- [`docs/AI_DEVELOPMENT_WORKFLOW.md`](docs/AI_DEVELOPMENT_WORKFLOW.md) — guardrails for AI-assisted development
- [`docs/PRODUCTION_REPOSITORY_VERIFICATION.md`](docs/PRODUCTION_REPOSITORY_VERIFICATION.md) — framework for converting project-history claims into production-verified records

## Change workflow

1. Inspect the repository and relevant project records before editing.
2. Work on a purpose-specific branch; do not make project-control changes directly on `main`.
3. Preserve existing content unless a deliberate revision is documented.
4. Separate project-history evidence from production-repository verification.
5. Do not call a historical defect a **Current known issue** until current production evidence supports that status.
6. Update affected project-control documents in the same change set.
7. Open a **draft pull request** into `main` for review.
8. Do not merge until the documentation accurately reflects available evidence.

## Immediate control objective

The next control phase is **Production Repository Verification**. The goal is to identify the canonical production repository and systematically reconcile each major RT Study Lab workstream against current source, tests, validation evidence, accessibility evidence, and unresolved defects. The verification framework is prepared in `docs/PRODUCTION_REPOSITORY_VERIFICATION.md`; it is intentionally not marked complete while production source remains inaccessible or unidentified.
