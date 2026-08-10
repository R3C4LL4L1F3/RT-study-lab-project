# RTSL-AIH-001 — RT Study Lab AI Development Harness

## Durable Project-Control Record

**Task ID:** `RTSL-AIH-001`  
**Name:** RT Study Lab AI Development Harness  
**Project authority:** MASTER PROJECT CONTROL  
**Architecture owner:** `(PLANNING_ARCHITECTURE)`  
**Priority:** **P2 — Platform / Reusable Infrastructure**  
**Risk:** **Tier 1**  
**Current work state:** **IN VALIDATION — IMPLEMENTATION EXISTS / INDEPENDENT REVIEW PENDING**  
**Implementation option:** **Option A**  
**Implementation status at record creation:** **NOT STARTED**  
**Current implementation status:** **V0 IMPLEMENTED ON AUTHORIZED BRANCH — NOT MERGED / NOT QA-ACCEPTED**  
**Baseline cost requirement:** **$0 incremental AI-service expenditure**

## Repository identity

- Project-control / authorized V0 implementation repository: `R3C4LL4L1F3/RT-study-lab-project`
- Verified `main` baseline used for initial setup: `12d8879f21008178fca61934405b5564da5c75a3`
- Verified implementation-start baseline after project-control PR #15: `dea4ac45ef5eecb2344c047abccc56ebb9b41363`
- Canonical GitHub task issue: `#14 — RTSL-AIH-001 — RT Study Lab AI Development Harness V0`
- Dedicated implementation branch: `feature/rtsl-aih-v0-harness`
- Project-control setup branch: `docs/rtsl-aih-001-project-control`
- Project-control setup PR: `#15 — merged`
- V0 implementation commit: `9dff56d58b7c15aa84cc089d9864d3b7eb0a8293`
- V0 implementation PR: `#16 — Implement RTSL-AIH-001 offline deterministic V0 harness`

The implementation branch was originally prepared without harness code, then fast-forwarded to the merged project-control baseline before V0 implementation began. V0 implementation now exists only on the dedicated implementation branch / PR and is not merged into `main`.

## Authority and evidence boundary

This record preserves approved project decisions and supporting-owner dispositions. GitHub records and links those decisions; it does not independently replace MASTER PROJECT CONTROL, `(PLANNING_ARCHITECTURE)`, Clinical Validation & Sources, or QA — Regression & Release as the authority for their respective domains.

Implementation-owner test results are engineering evidence. They are not independent QA acceptance and do not by themselves authorize merge, release, or project closure.

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

**Disposition:** **PASS — IMPLEMENTATION AUTHORIZED AND EXECUTED FOR THE BOUNDED OFFLINE SLICE**

The approved implementation plan defines a bounded first vertical slice centered on the offline deterministic policy core. The first slice is intended to prove the frozen governance contracts through deterministic fixtures and audit output before adding optional integrations.

The implementation handoff required the frozen Architecture v1.1, the bounded QA correction including `RTSL-AIH-QA-004`, `AIH-GH-RO-001`, MASTER Option A selection, the V0 vertical-slice specification, frozen role/gate/Kernel-profile configuration, and the approved repository/branch identity.

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

## V0 implementation execution

**Implementation branch:** `feature/rtsl-aih-v0-harness`  
**Implementation-start baseline:** `dea4ac45ef5eecb2344c047abccc56ebb9b41363`  
**Implementation commit:** `9dff56d58b7c15aa84cc089d9864d3b7eb0a8293`  
**Implementation PR:** `#16`  
**Merge state:** **NOT MERGED**

Implemented bounded surfaces:

- `tools/ai_harness/` — offline deterministic evaluator;
- `config/ai_harness/` — frozen V0 roles/gates/transitions/Kernel profile;
- `tests/ai_harness/` — deterministic focused tests and fixtures;
- `docs/ai-harness/` — schema, rule, audit and read-only contracts.

Explicitly not implemented:

- runtime AI/model calls;
- paid AI/model APIs;
- agent framework;
- live GitHub integration;
- GitHub write capability;
- production application changes;
- deployment/release operations;
- cross-task persistence / duplicate-task-ID detection.

### Implementation-owner validation evidence

Executed locally against the implementation content before PR handoff:

- `python -m unittest discover -s tests/ai_harness -p 'test_*.py' -v` — **35/35 PASS**;
- `python -m compileall -q tools tests` — **PASS**;
- focused validation includes canonical schema/vocabulary, frozen state transitions, PAUSED/BLOCKED contracts, mandatory gates, no-gate-downgrade, approval authority, QA independence, `RTSL-AIH-QA-004`, canonical serialization/hash determinism, input non-mutation, disabled/read-only GitHub boundary, CLI artifact behavior, and `TEST-AIH-V0-FINAL-RECHECK-001`.

**Evidence boundary:** this is implementation-owner validation only. Independent QA / supporting review remains mandatory before merge/closure.

## Historical setup boundary

The initial project-control setup step created the canonical GitHub task record, durable source-controlled project-control record, and dedicated implementation branch. No harness code existed at that point. That historical fact remains preserved by PR #15 / its merge history.

## Current validation / closure boundary

Current state is **IN VALIDATION**.

Remaining before this V0 implementation can be treated as accepted/complete:

- independent QA / appropriate supporting review of PR #16 against frozen Architecture v1.1 and the V0 vertical-slice specification;
- disposition of any reproduced defects or validation gaps;
- verified PR merge only after required review/authorization;
- durable post-merge provenance/closure update as required by MASTER PROJECT CONTROL.

No GitHub read-only adapter enablement, V0.x expansion, framework selection change, or duplicate-task-ID implementation is authorized by this validation state.
