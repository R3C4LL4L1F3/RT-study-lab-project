# RT Study Lab — Project Control

This repository is the durable project-control and documentation home for **RT Study Lab**.

It is intentionally separate from the private production application source repository:

`R3C4LL4L1F3/RT-study-lab`

This repository preserves development history, current status, roadmap, known issues, architecture decisions, validation records, and the AI-assisted development workflow. It should not silently become a substitute for the production application repository.

## Evidence and work-state vocabulary

### Evidence basis

- **Project-control verified** — directly observable in this repository.
- **Confirmed from project history** — preserved from prior development records but not necessarily current production fact.
- **Verified against production repository** — confirmed by inspecting the production source at a recorded ref and, where relevant, associated tests/evidence.
- **Needs verification against production repository** — cannot yet be confirmed from current production source.
- **Unknown** — not established.

### Lifecycle / disposition

- **Current known issue** — reproduced or otherwise confirmed with current evidence.
- **Planned work** — intended future work; not an implementation claim.
- **Historical / possibly superseded** — retained for project history but may no longer describe current production.

Clinical validation, implementation state, test results, deployment status, defect resolution, version numbers, and dates must not be promoted without supporting evidence.

## Current repository state

- Default branch: `main`
- Working project-control branch: `setup/project-control-foundation`
- Project-control PR #1: open, draft, unmerged
- Production source repository: `R3C4LL4L1F3/RT-study-lab`
- Production baseline ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Complete validation implementation: production draft PR #1 on `validation/issue-6-test-baseline`
- Validated production PR ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Successful GitHub Actions run: `31309995943`

Issue #6 established a passing automated validation path on the production draft PR: locked npm install, lint, build, complete 28-file source-controlled test suite, dedicated Ventilator P1 regression, and diagnostic artifact upload all passed. The production PR remains unmerged; production `main` is unchanged until explicit maintainer authorization.

## Documentation index

- [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) — current project and module status
- [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md) — sequence-oriented development history
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — priorities and next work
- [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md) — current risks, historical defects, and verification concerns
- [`docs/VALIDATION_REGISTER.md`](docs/VALIDATION_REGISTER.md) — automated/manual validation evidence and boundaries
- [`docs/ARCHITECTURE_DECISIONS.md`](docs/ARCHITECTURE_DECISIONS.md) — project and architecture decision register
- [`docs/AI_DEVELOPMENT_WORKFLOW.md`](docs/AI_DEVELOPMENT_WORKFLOW.md) — guardrails for AI-assisted development
- [`docs/PRODUCTION_REPOSITORY_VERIFICATION.md`](docs/PRODUCTION_REPOSITORY_VERIFICATION.md) — current production source/verification baseline

## Change workflow

1. Inspect current source and project-control evidence before editing.
2. Do not work directly on `main`; use a purpose-specific branch.
3. Preserve history and separate historical claims from current evidence.
4. Run the relevant production validation path for application changes once that workflow is on the reviewed branch/ref.
5. Keep automated, clinical, accessibility, deployment, and manual visual/mechanical evidence distinct.
6. Update affected project-control records in the same work cycle.
7. Use draft PRs for review.
8. Do not merge without explicit maintainer authorization.

## Immediate control objective

The production source baseline and draft-PR automated validation baseline are now established. The next control decisions are:

1. review and explicitly authorize or reject merge of the validated production PR #1;
2. after merge, confirm CI on production `main`;
3. establish GitHub-to-live-ChatGPT-Sites deployment correspondence;
4. complete the remaining browser/manual checks in Issues #3 and #5.
