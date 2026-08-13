# RT Study Lab — Project Control

This repository is the durable project-control and documentation home for **RT Study Lab**.

It is intentionally separate from the private production application source repository:

`R3C4LL4L1F3/RT-study-lab`

This repository owns project status, roadmap/queue, known issues, architecture decisions, validation records, work routing, and AI-assisted development governance. The production repository owns application source, production tests/CI, implementation branches/PRs, and eventual production tags/releases.

## Evidence and work-state vocabulary

### Evidence basis

- **Project-control verified** — directly observable in this repository.
- **Confirmed from project history** — preserved from prior development records but not necessarily current production fact.
- **Verified against production repository** — confirmed by inspecting production source at a recorded ref and, where relevant, executable evidence.
- **Needs verification against production repository** — cannot yet be confirmed from current production source.
- **Unknown** — not established.

### Lifecycle / disposition

- **Current known issue** — reproduced or otherwise confirmed with current evidence.
- **Planned work** — intended future work; not an implementation claim.
- **Historical / possibly superseded** — retained for project history but may no longer describe current production.

### Queue status

- **ACTIVE** — current project-control work is being executed.
- **APPROVED** — approved work is recorded but execution may still be gated by sequence/dependencies.
- **IN VALIDATION** — implementation/evidence exists and a defined validation layer remains open.
- **BLOCKED** — an identified dependency/evidence source prevents completion.
- **DEFERRED** — intentionally held until an approved dependency/gate is satisfied.

Clinical validation, implementation state, test results, deployment status, defect resolution, version numbers, and dates must not be promoted without supporting evidence.

## Current repository / production state

Project-control:

- Default branch: `main`
- Current `main` ref at the Phase 3 inherited baseline: `382132f82b5f71d2b6d101b56e3b70dff5b557ee` (Phase 2 PR #38 merged)
- PR #1 is the historical project-control foundation milestone; it is merged and represented by issue #34.
- Phase 1 documentation corrections were merged by PR #33, and the Phase 2 checkpoint was merged by PR #38. Phase 3 records are being prepared on the purpose-specific branch for this bounded batch.

Production:

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Default branch: `main`
- Current ref: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Current automatic `Production Validation`: **PASS** — Actions run `31311314980`
- Production `main` branch protection: **not enabled** at the current repository state
- Git tags: **none**
- GitHub Releases: **none**
- Live ChatGPT Sites deployed Git ref: **Unknown / blocked on authoritative Sites version metadata** under Issue #8

Green CI is repository-validation evidence; it is not independent clinical validation, comprehensive accessibility validation, live-deployment equivalence, or release maturity.

## Approved project execution sequence

MASTER PROJECT CONTROL approved this sequence:

1. Durable project-control baseline
2. Close existing Tier 3 validation
3. Establish independent clinical validation
4. Strengthen production/release controls
5. Specify Interactive Models architecture
6. Implement the first validated reusable physiology model
7. Expand only after the framework proves stable

Recording a later step does **not** authorize executing it early.

## Subsystem routing

### Interactive Models & Simulation Lab

Owns general interactive physiology/pathophysiology models where the central problem is changing clinical state, including **Shock / Circulation / Oxygen Transport** and future framework-dependent V/Q, gas-exchange, pulmonary-circulation, PE, ARDS-physiology, and heart-failure-physiology models.

The former standalone active Shock circulation-simulator chat ownership has been replaced by **Interactive Models & Simulation Lab — Shock / Circulation**. Historical terminology may remain in chronological records.

The following remain separate persistent subsystem owners and must not be migrated under Interactive Models:

- **Ventilator — Waveform Lab**
- **ECG & ACLS Lab**
- **3D Equipment Lab**

## Documentation index

- [`docs/MASTER_PROJECT_QUEUE.md`](docs/MASTER_PROJECT_QUEUE.md) — approved canonical queue, sequence, ownership and execution gates
- [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) — current project and module status
- [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md) — sequence-oriented development history
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — roadmap dependencies and future gates
- [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md) — current risks, historical defects, and verification concerns
- [`docs/VALIDATION_REGISTER.md`](docs/VALIDATION_REGISTER.md) — automated/manual/clinical/accessibility validation evidence and boundaries
- [`docs/ARCHITECTURE_DECISIONS.md`](docs/ARCHITECTURE_DECISIONS.md) — project and architecture decision register
- [`docs/AI_DEVELOPMENT_WORKFLOW.md`](docs/AI_DEVELOPMENT_WORKFLOW.md) — guardrails and work-routing for AI-assisted development
- [`docs/governance/RTSL-KERNEL-AUTONOMY-001-ADOPTION-RECORD.md`](docs/governance/RTSL-KERNEL-AUTONOMY-001-ADOPTION-RECORD.md) — controlled governance migration adoption state and activation boundary
- [`docs/governance/RTSL-KERNEL-AUTONOMY-001-CONFLICT-MIGRATION-REGISTER.md`](docs/governance/RTSL-KERNEL-AUTONOMY-001-CONFLICT-MIGRATION-REGISTER.md) — source-inspected KEEP / CLARIFY / MODIFY register
- [`docs/governance/RTSL-KERNEL-AUTONOMY-001-INDEPENDENT-QA-HANDOFF.md`](docs/governance/RTSL-KERNEL-AUTONOMY-001-INDEPENDENT-QA-HANDOFF.md) — complete 25-item independent-QA handoff; implementation-owner evidence only
- [`docs/governance/RTSL-KERNEL-AUTONOMY-001-TEMPORARY-QA-DEVIATION.md`](docs/governance/RTSL-KERNEL-AUTONOMY-001-TEMPORARY-QA-DEVIATION.md) — temporary merge deviation; explicitly not a QA PASS
- [`docs/ADR-012-threejs-2-5d-circulation-renderer.md`](docs/ADR-012-threejs-2-5d-circulation-renderer.md) — proposed Three.js renderer decision
- [`docs/INTERACTIVE_MODELS_THREEJS_ROADMAP.md`](docs/INTERACTIVE_MODELS_THREEJS_ROADMAP.md) — Three.js 2.5D implementation roadmap and gates
- [`docs/INTERACTIVE_MODELS_THREEJS_ARCHITECTURE.md`](docs/INTERACTIVE_MODELS_THREEJS_ARCHITECTURE.md) — renderer, asset, segment, and state contracts
- [`docs/INTERACTIVE_MODELS_THREEJS_VALIDATION_PLAN.md`](docs/INTERACTIVE_MODELS_THREEJS_VALIDATION_PLAN.md) — evidence and release validation plan
- [`docs/INTERACTIVE_MODELS_THREEJS_PROGRESS.md`](docs/INTERACTIVE_MODELS_THREEJS_PROGRESS.md) — current workstream progress and next actions
- [`docs/PRODUCTION_REPOSITORY_VERIFICATION.md`](docs/PRODUCTION_REPOSITORY_VERIFICATION.md) — current production source/verification baseline

## Phase 1, Phase 2, and Phase 3 project-intelligence bridge

The bounded Phase 1, Phase 2, and Phase 3 Codex context bridges are indexed at [`docs/project-intelligence/README.md`](docs/project-intelligence/README.md). Phase 3 is additionally indexed at [`docs/project-intelligence/PHASE-3-README.md`](docs/project-intelligence/PHASE-3-README.md). These are bounded-scope evidence layers and do not replace the project-control queue, authority records, or final global reconciliation owned elsewhere in this repository.

## Change workflow

1. Inspect current source and project-control evidence before editing.
2. Do not work directly on `main`; use a purpose-specific branch/PR.
3. Preserve useful history and separate historical claims from current evidence.
4. Use the canonical production validation path for production changes.
5. Keep automated, clinical, accessibility, deployment, and manual visual/mechanical evidence distinct.
6. Update affected project-control records in the same work cycle.
7. Route consequential work to the owning subsystem/chat recorded in the queue.
8. Do not implement a later queue step merely because its future record exists.
9. Do not merge project-control or production PRs without the required maintainer authorization.

## Immediate control objective

The coherent project-control foundation is durable on project-control `main`. The next operational task is normally **QA — Regression & Release** for Ventilator browser/manual historical-P1 verification under Issue #3 unless MASTER PROJECT CONTROL changes the sequence based on new evidence.
