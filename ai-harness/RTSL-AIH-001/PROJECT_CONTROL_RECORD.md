# RTSL-AIH-001 — RT Study Lab AI Development Harness

## Durable Project-Control Record

**Task ID:** `RTSL-AIH-001`  
**Name:** RT Study Lab AI Development Harness  
**Project authority:** MASTER PROJECT CONTROL  
**Architecture owner:** `(PLANNING_ARCHITECTURE)`  
**Priority:** **P2 — Platform / Reusable Infrastructure**  
**Risk:** **Tier 1**  
**Current work state:** **APPROVED — IMPLEMENTATION AUTHORIZED**  
**Implementation option:** **Option A**  
**Implementation status at record creation:** **NOT STARTED**  
**Baseline cost requirement:** **$0 incremental AI-service expenditure**

## Repository identity

- Project-control / authorized V0 implementation repository: `R3C4LL4L1F3/RT-study-lab-project`
- Verified `main` baseline used for setup: `12d8879f21008178fca61934405b5564da5c75a3`
- Canonical GitHub task issue: `#14 — RTSL-AIH-001 — RT Study Lab AI Development Harness V0`
- Dedicated implementation branch: `feature/rtsl-aih-v0-harness`
- Project-control record branch: `docs/rtsl-aih-001-project-control`

The implementation branch was created from the verified `main` baseline above. No harness code or implementation files were added as part of the project-control setup step.

## Authority and evidence boundary

This record preserves approved project decisions and supporting-owner dispositions. GitHub records and links those decisions; it does not independently replace MASTER PROJECT CONTROL, `(PLANNING_ARCHITECTURE)`, Clinical Validation & Sources, or QA — Regression & Release as the authority for their respective domains.

## Frozen architecture

**Architecture:** `RTSL-AIH-001 — V0/V1 Requirements & Architecture Specification — Pre-Freeze Architecture Candidate v1.1`  
**Disposition:** **FROZEN / APPROVED BY MASTER PROJECT CONTROL**

The frozen architecture preserves the following controlling constraints:

- Project Operating Kernel remains authoritative;
- V0/V1 remains read-only/advisory;
- deterministic policy controls mandatory machine-enforceable rules;
- advisory AI cannot override deterministic failures;
- human approvals remain bounded by authority role;
- Tier 2/3 clinical gates fail closed when required evidence/disposition is unavailable;
- independent-review identity must be distinguishable where independence is mandatory;
- canonical audit serialization and SHA-256 content hashing are required;
- GitHub/project control remains durable provenance truth;
- no production writes, autonomous release, or autonomous clinical decisions are authorized by the harness;
- paid/API-dependent future capabilities remain optional and outside the V0 baseline.

## QA pre-freeze disposition

**Disposition:** **PASS**

Pre-freeze QA findings were closed before requirements freeze, including `RTSL-AIH-QA-004`.

### RTSL-AIH-QA-004

Tool-produced evidence may support defect assessment, but evidence production and authoritative defect classification are separate responsibilities.

A `VERIFIED_TOOL` result may be reliable evidence; it does **not** by itself establish an authoritative `CONFIRMED_DEFECT` where project governance requires an authorized classifier/disposition.

This correction is part of the frozen Architecture v1.1 requirements.

## Clinical supporting-owner review

**Owner:** Clinical Validation & Sources  
**Disposition:** **PASS**

The supporting review confirmed the harness does not acquire clinical authority. Clinical truth, evidence, equations, physiology, treatment rules, and implementation-ready clinical specifications remain outside harness authority. AI synthesis cannot itself satisfy an authoritative clinical gate, and required Tier 2/3 clinical evidence gates fail closed when the required external disposition is unavailable.

## GitHub / provenance supporting-owner review

**Owner:** GitHub PR and Documentation  
**Disposition:** **PASS**

The review confirmed compatibility of:

- project-control repository placement;
- production/project-control separation;
- Kernel version/revision/hash identity;
- canonical audit serialization and SHA-256 persistence;
- project-scoped actor-ID persistence;
- immutable provenance references;
- approval-to-artifact/revision binding;
- the read-only/advisory V0/V1 repository boundary.

### AIH-GH-RO-001

`AIH-GH-RO-001` is incorporated into the frozen requirements.

V0/V1 GitHub access must be technically constrained to read-only access through credential-level least privilege and/or an allowlisted read-only adapter. A write-capable GitHub interface must not be exposed to the advisory/runtime layer merely with a prompt instruction not to mutate.

If the read-only boundary cannot be verified, repository-connected execution fails closed or uses supplied offline evidence. This requirement does not itself authorize changing repository permissions.

## MASTER Requirements Freeze

**Decision authority:** MASTER PROJECT CONTROL  
**Disposition:** **APPROVED / FROZEN**

MASTER approved and froze the V0/V1 requirements and Architecture v1.1 after QA and supporting-owner review. Framework choice remained downstream of the requirements freeze and implementation-option analysis.

## Option A selection

**Selected option:** **Option A**

Authorized V0 baseline:

- plain Python;
- standard-library-first;
- offline deterministic evaluator;
- project-control repository implementation;
- structured machine-readable inputs/outputs;
- deterministic policy/state/gate/approval/finding evaluation;
- canonical deterministic audit serialization and SHA-256 audit identity;
- mandatory final deterministic policy recheck;
- no runtime AI/agent framework requirement;
- no paid model API requirement;
- no GitHub write path in the initial V0 slice;
- no paid vector database;
- no paid observability platform.

A later GitHub evidence integration is limited by `AIH-GH-RO-001` to an allowlisted read-only adapter and is not part of the initial offline core.

## V0 Implementation Plan & Vertical-Slice Specification

**Disposition:** **PASS — READY FOR IMPLEMENTATION HANDOFF**

The approved implementation plan defines a bounded first vertical slice centered on the offline deterministic policy core. The first slice is intended to prove the frozen governance contracts through deterministic fixtures and audit output before adding optional integrations.

The implementation handoff requires the frozen Architecture v1.1, the bounded QA correction including `RTSL-AIH-QA-004`, `AIH-GH-RO-001`, MASTER Option A selection, the V0 vertical-slice specification, frozen role/gate/Kernel-profile configuration, and the approved repository/branch identity.

**Implementation sequence constraint:** implement only the offline core first.

## MASTER implementation authorization

**Decision authority:** MASTER PROJECT CONTROL  
**Disposition:** **IMPLEMENTATION AUTHORIZED**

Authorization applies only to the approved bounded V0 implementation plan and frozen requirements. It does not authorize scope expansion, paid-service adoption, production mutation, autonomous release, or framework substitution beyond the approved baseline.

## Bounded correction — RTSL-AIH-IMP-001

**ID:** `RTSL-AIH-IMP-001`  
**Disposition:** **APPROVED BOUNDED CORRECTION / SCOPE CLARIFICATION**

Duplicate-task-ID detection is **deferred beyond the initial isolated-task V0 slice**.

The initial V0 vertical slice evaluates an isolated task record and must not claim or imply cross-task duplicate-ID detection. Future duplicate-task-ID detection requires a later explicitly approved persistence/cross-record scope.

This deferral does not weaken any mandatory gate inside the isolated-task V0 scope.

## Initial implementation branch

`feature/rtsl-aih-v0-harness`

Branch baseline:

`12d8879f21008178fca61934405b5564da5c75a3`

At project-control setup, the branch contains no harness implementation change relative to that baseline.

## Implementation boundary for this setup step

Completed in this step:

- canonical GitHub task record created;
- durable source-controlled project-control record prepared through branch/PR workflow;
- dedicated V0 implementation branch created from verified `main`.

Not performed in this step:

- harness code implementation;
- framework substitution;
- GitHub permission changes;
- GitHub adapter integration;
- production application changes;
- release/tag operations.

## Next execution boundary

The next implementation action belongs on `feature/rtsl-aih-v0-harness` and must remain within the approved Option A V0 vertical-slice specification. The implementation owner must inspect this record and the frozen requirements before adding code.
