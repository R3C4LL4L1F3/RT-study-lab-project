# Architecture and Project Decisions

This file is the lightweight decision register for RT Study Lab project-control and cross-repository engineering decisions. It is not a substitute for detailed ADRs when a decision has significant technical or clinical consequences.

Decision **status** and evidence **basis** are separate concepts. Use the vocabulary defined in the repository `README.md`.

## DEC-001 — Keep project control separate from production application source

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Use `R3C4LL4L1F3/RT-study-lab-project` as the durable project-control repository and `R3C4LL4L1F3/RT-study-lab` as the production source repository. Do not treat either repository as a substitute for the other.

Production owns application code, production tests/CI, implementation branches/PRs and eventual production tags/releases. Project control owns project-level issues, roadmap/queue, architecture decisions, validation/known-issues registers, project status and work-routing governance.

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

Queue state additionally distinguishes **ACTIVE**, **APPROVED**, **IN VALIDATION**, **BLOCKED** and **DEFERRED**.

## DEC-003 — Use branch-and-PR review for project-control changes

- Status: Accepted
- Evidence basis: Project-control verified

### Decision

Do not make project-control changes directly to `main`. Use a purpose-specific branch and pull request. PR #1 was the historical foundation review vehicle and is now merged into project-control `main`; current Phase 1 documentation corrections are being carried in draft/open PR #33 and are not merged by this pass.

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

## DEC-006 — Require production evidence before current-defect or resolved status

- Status: Accepted
- Evidence basis: Project-control verified control standard

### Decision

A historical application defect report must not be labeled **Current known issue** or **Resolved** solely from chat history. Current production evidence is required.

When source-level implementation plus executable automated regressions support resolution, record that exact scope. Do not infer browser, clinical, accessibility, deployment, or manual visual/mechanical validation from automated results.

## DEC-007 — Use npm as the canonical production repository validation package manager

- Status: Accepted and **implemented on production `main`**
- Evidence basis: Verified against production repository and executable GitHub Actions evidence
- Initial validated PR ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- Merged validation baseline: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- Current production `main`: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Current automatic `main` validation: Actions run `31311314980` — **PASS**

### Decision

Use **npm** and the maintained `package-lock.json` for reproducible production-repository installation and automated validation.

The canonical validation path:

1. installs with `npm ci`;
2. lints;
3. builds;
4. discovers the complete `tests/**/*.test.mjs` inventory recursively;
5. executes each test file in an isolated Node process;
6. supports existing direct TypeScript imports at Node 22.13.0 with `--experimental-strip-types`;
7. runs the dedicated Ventilator historical-P1 regression;
8. retains durable GitHub Actions evidence/diagnostics.

### Current consequence

The decision is no longer pending a production merge. Production PR #1 merged the complete validation path, production PR #2 added automatic `main` validation, and the current `main` run is green.

New conforming test files enter the canonical recursive suite automatically. A manually curated fixed subset must not become the default again without a deliberate validation/architecture decision.

### pnpm boundary

Do **not** delete or regenerate `pnpm-lock.yaml` or `pnpm-workspace.yaml` merely because npm is canonical for validation. Their possible ChatGPT Sites/Vinext role remains unresolved under PC-004.

## DEC-008 — Keep GitHub validation independent from deployment

- Status: Accepted
- Evidence basis: Production-source and deployment-boundary verification

### Decision

The production GitHub validation workflow must not deploy RT Study Lab or require deployment credentials unless a future separately reviewed deployment architecture explicitly requires it.

### Rationale

The current GitHub-to-ChatGPT-Sites deployed ref remains unknown under Issue #8. CI proves repository quality, not live deployment identity.

## DEC-009 — Define Interactive Models & Simulation Lab ownership without absorbing specialized simulators

- Status: Accepted project-structure decision
- Evidence basis: Approved MASTER PROJECT CONTROL policy

### Decision

Use **Interactive Models & Simulation Lab** as the persistent owner for general interactive physiology/pathophysiology modeling where the central problem is changing clinical state.

Shock forward work is routed as:

**Interactive Models & Simulation Lab — Shock / Circulation**

The following remain separate persistent subsystem owners:

- Ventilator — Waveform Lab
- ECG & ACLS Lab
- 3D Equipment Lab

Historical references to the former standalone Shock circulation-simulator chat may remain where necessary to preserve chronology.

## DEC-010 — Gate Interactive Models production expansion behind clinical and architecture approval

- Status: Accepted governance/architecture gate
- Evidence basis: Approved MASTER PROJECT CONTROL policy + current production verification that no numerical Shock/O₂ engine exists
- Related project-control issue: #9

### Decision

Interactive Models production expansion requires **both**:

1. an approved clinical/model contract; and
2. an approved reusable simulation architecture/model contract.

Approved dependency chain:

**Clinical evidence/model definition**
→ **Interactive Models architecture/model contract**
→ **reusable framework implementation**
→ **Shock / Circulation / Oxygen Transport first-model validation**
→ **additional physiology models**

### Required architecture/specification evidence

Before production implementation approval, define and independently review:

- deterministic reference cases;
- model invariants;
- boundary/invalid-state behavior;
- long-run expectations;
- reset/replay behavior;
- seed/reproducibility behavior;
- serialization/snapshot expectations;
- clinically meaningful equations/assumptions and their source basis;
- calculated/derived/approximated/illustrative variable distinctions.

### Consequence

Issue #9 is **approved for specification only**. No `feature/interactive-models-core` or equivalent production implementation branch is authorized until the gate is satisfied.

Future V/Q, gas-exchange, pulmonary-circulation, PE physiology, ARDS physiology, heart-failure physiology and related models remain framework-dependent/deferred.

## DEC-011 — Strengthen production branch/release controls through explicit policy before execution

- Status: Accepted governance direction; implementation deferred
- Evidence basis: Current GitHub repository state + approved MASTER PROJECT CONTROL sequencing
- Related issues: #8 and #12

### Decision

Record branch-protection, release/tag and deployment-correspondence requirements now, but execute them only at their approved sequence point.

Current production facts:

- `main` automatic CI is green;
- `main` is not branch-protected;
- no Git tags exist;
- no GitHub Releases exist;
- active Sites deployment Git ref remains unknown.

Do not enable branch protection, create a tag/Release, deploy, or delete validation branches as part of project-control synchronization.

## DEC-012 — Use a Three.js 2.5D renderer as a replaceable presentation layer

- Status: Proposed; architecture review required
- Evidence basis: Project-control planning package; current lab visual audit
- Related records: `docs/ADR-012-threejs-2-5d-circulation-renderer.md`, `docs/INTERACTIVE_MODELS_THREEJS_ARCHITECTURE.md`

### Decision

Plan a Three.js 2.5D renderer using an orthographic camera, documented GLB/glTF anatomy assets, canonical vascular segment IDs, bounded instanced parcels, and an immutable renderer frame adapter. Keep the existing deterministic physiology engine, accessible DOM summary, validation modules, and SVG/text fallback independent of the renderer.

### Gate

This decision authorizes specification and isolated prototyping only. It does not authorize production implementation until the clinical/model contract, asset provenance, independent QA, accessibility evidence, physiology-parity evidence, and runtime evidence pass.

## Future ADR threshold

Create a dedicated ADR when a decision materially changes one or more of the following:

- clinical model or guideline interpretation
- state-machine behavior
- simulation math
- reusable Interactive Models architecture
- data model/schema
- framework/runtime
- deployment architecture
- persistence/storage
- 3D asset pipeline
- accessibility architecture
- test/validation strategy
- package-management/dependency strategy
- production branch/release governance
