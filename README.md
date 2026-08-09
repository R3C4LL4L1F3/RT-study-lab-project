# RT Study Lab — Project Control

This repository is the durable project-control and documentation home for **RT Study Lab**.

It is intentionally separate from any production application source repository unless that source is explicitly added here later. Its purpose is to preserve development history, current status, roadmap, known issues, architecture decisions, validation records, and the AI-assisted development workflow.

## Repository boundary

This repository should answer:

- What is RT Study Lab trying to accomplish?
- What has been reported as implemented?
- What has actually been validated and with what evidence?
- What remains unresolved?
- What architectural or workflow decisions have been made?
- What should be worked on next?

It should **not** silently become a substitute for the production application repository.

## Evidence states

Project claims should use one of these states:

- **Repository-verified** — supported directly by content, commits, pull requests, issues, or validation artifacts in this repository.
- **Reported** — preserved from prior project/development records but not independently re-run or verified from this repository.
- **Proposed** — planned work or a recommended future state.
- **Unknown** — information has not yet been established.

Clinical validation, implementation status, test results, deployment status, and dates must not be promoted from **Reported** to **Repository-verified** without supporting evidence.

## Current repository state

As of the initial project-control setup:

- Default branch: `main`
- Working branch for this foundation: `setup/project-control-foundation`
- Production application source repository: **Unknown / not linked here yet**
- CI configuration in this repository: **None identified**
- Existing issue history before project-control setup: **None identified**
- Existing pull-request history before project-control setup: **None identified**

## Documentation index

- [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) — current verified and reported status
- [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md) — chronological/sequence-oriented development record
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — priorities, dependencies, and next work
- [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md) — unresolved defects, risks, and documentation gaps
- [`docs/VALIDATION_REGISTER.md`](docs/VALIDATION_REGISTER.md) — validation and test claims with evidence state
- [`docs/ARCHITECTURE_DECISIONS.md`](docs/ARCHITECTURE_DECISIONS.md) — project and architecture decision log
- [`docs/AI_DEVELOPMENT_WORKFLOW.md`](docs/AI_DEVELOPMENT_WORKFLOW.md) — guardrails for AI-assisted development

## Change workflow

1. Inspect the repository and relevant project records before editing.
2. Work on a purpose-specific branch; do not make project-control changes directly on `main`.
3. Preserve existing content unless a deliberate revision is documented.
4. Separate verified facts from reported history and proposals.
5. Update affected project-control documents in the same change set.
6. Open a **draft pull request** into `main` for review.
7. Do not merge until the documentation accurately reflects available evidence.

## Immediate control objective

The next control milestone is to connect this repository to the production source/deployment evidence and convert high-value **Reported** records into **Repository-verified** records through source inspection, reproducible validation, or archived artifacts.
