# RTSL-AIH-001 — PR #16 Independent-QA Bounded Correction Record

**Task:** `RTSL-AIH-001 — RT Study Lab AI Development Harness`  
**Priority / risk:** P2 / Tier 1  
**Repository:** `R3C4LL4L1F3/RT-study-lab-project`  
**PR:** #16 — `Implement RTSL-AIH-001 offline deterministic V0 harness`  
**Implementation branch:** `feature/rtsl-aih-v0-harness`  
**Independent QA disposition received:** **FAIL — FIX REQUIRED**  
**Correction state:** **IMPLEMENTED — INDEPENDENT QA RETEST REQUIRED**

## Authority boundary

This record preserves the independent QA failure and the implementation-owner correction evidence. It does not convert QA's failed disposition into a pass. QA — Regression & Release remains the authority for independent retest disposition.

## Confirmed QA findings addressed

### RTSL-AIH-V0-QA-001
Risk-required gates could be present while represented as non-required.

**Bounded correction:** risk-minimum gate evaluation now fails closed when a gate required by the current risk tier has `obligation.required: false`.

### RTSL-AIH-V0-QA-002
A required gate could omit its authority owner.

**Bounded correction:** every gate with `obligation.required: true` must identify `authority.owner_role`; omission fails closed.

### RTSL-AIH-V0-QA-003
`PROPOSED -> APPROVED` could proceed without the frozen required approval.

**Bounded correction:** the source-controlled transition matrix now declares an explicit `MASTER / APPROVED` prerequisite and deterministic rule `AIH-V0-R054` requires a qualifying human MASTER approval before that transition is permitted.

### RTSL-AIH-V0-QA-004
PAUSED/BLOCKED resume behavior could rely on arbitrary `previous_state` data or unsatisfied resume/unblock conditions.

**Bounded correction:** `previous_state` must be a legal predecessor under the frozen transition matrix. Resuming to that prior state additionally requires explicit `*_condition_satisfied: true` plus non-empty evidence references. Cross-state PAUSED/BLOCKED/CANCELLED transitions remain limited to the frozen matrix.

### RTSL-AIH-V0-QA-005 — P2
Existing audit/evaluation output could be overwritten.

**Bounded correction:** `evaluation.json` and `audit.json` are create-only. Existing targets cause refusal before write; exclusive file creation also prevents direct overwrite at persistence time.

### RTSL-AIH-V0-QA-006 — P2
The implemented finding vocabulary omitted frozen values.

**Bounded correction:** schema now accepts exactly `VALIDATION_GAP`, `CONFIRMED_DEFECT`, `OBSERVATION`, and `UNRESOLVED`. Observation/unresolved findings remain distinct and are not automatically promoted to confirmed defects.

## Regression evidence — implementation owner

Executed after the bounded corrections:

```text
python -m unittest discover -s tests/ai_harness -p 'test_*.py' -v
python -m compileall -q tools tests
```

Result:

- focused V0 test suite: **55/55 PASS**;
- Python compilation: **PASS**;
- additional direct QA-001..006 scenario check: **19/19 PASS**.

These are implementation-owner results only.

## Preserved constraints

Unchanged:

- Option A;
- plain Python / standard-library-first offline V0;
- no runtime AI/model service;
- no paid API/platform/vector/observability dependency;
- `AIH-GH-RO-001` read-only GitHub boundary;
- no live GitHub integration or write path in the initial slice;
- `RTSL-AIH-QA-004` evidence-producer / authoritative-classifier separation;
- `RTSL-AIH-IMP-001` duplicate-task-ID detection deferral;
- no production repository/application change;
- no release/deployment action.

## Current disposition

**IN VALIDATION — CORRECTED PR HEAD PENDING INDEPENDENT QA RETEST.**

Do not merge PR #16 until QA independently retests the corrected head and returns the required disposition.
