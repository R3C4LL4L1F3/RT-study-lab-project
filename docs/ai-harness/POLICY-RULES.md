# RTSL AI Harness V0 Frozen Rule Pack

Policy profile: `RTSL-AIH-V0-POLICY-1`.

Stable rule families implemented:

- Structural: `AIH-V0-R001`–`R005`
- PAUSED/BLOCKED: `R010`–`R011`
- Transitions: `R020`–`R023`
- Gates: `R030`–`R037`
- No-gate-downgrade: `R040`–`R042`
- Approvals: `R050`–`R054`
- QA / independence: `R060`–`R064`
- Validation gap / defect: `R070`–`R074`
- Contradictions: `R080`–`R082`
- Read-only boundary: `R090`

The evaluator is deterministic. Human approval cannot legalize a deterministic policy violation. Missing mandatory Tier 2/3 evidence/gates fail closed as incomplete rather than being invented or silently downgraded.

`RTSL-AIH-QA-004` remains implemented by `R073`/`R074`: verified tool evidence may support defect assessment, but it cannot alone establish an authoritative `CONFIRMED_DEFECT`.

The frozen normative transition matrix is source-controlled in `config/ai_harness/transition-matrix.v1.json`.

## PR #16 independent-QA bounded corrections

The following corrections preserve frozen Architecture v1.1 and do not expand V0 scope:

- `RTSL-AIH-V0-QA-001`: `R030` now fails when a risk-required gate is present but represented as `obligation.required: false`.
- `RTSL-AIH-V0-QA-002`: `R036` requires an authority owner for every explicitly required gate.
- `RTSL-AIH-V0-QA-003`: `R054` enforces the frozen explicit MASTER approval prerequisite for `PROPOSED -> APPROVED`.
- `RTSL-AIH-V0-QA-004`: `R010/R011/R020/R022/R023` validate PAUSED/BLOCKED previous-state provenance and require explicit satisfied-condition evidence before resuming to the prior state.
- `RTSL-AIH-V0-QA-005`: output artifacts are create-only; an existing `evaluation.json` or `audit.json` causes refusal rather than overwrite.
- `RTSL-AIH-V0-QA-006`: the frozen finding vocabulary includes `VALIDATION_GAP`, `CONFIRMED_DEFECT`, `OBSERVATION`, and `UNRESOLVED`.

`AIH-GH-RO-001`, Option A, and `RTSL-AIH-IMP-001` remain unchanged.

## RTSL-AIH-001-REV-AUTONOMY-01 — dormant controlled-adoption profile

The repository contains a dormant candidate profile for `RTSL-KERNEL-AUTONOMY-001`. It is not the default evaluator profile and does not activate the amendment. When explicitly selected for migration validation, it adds only these deterministic checks:

- Tier 0–1 independent review is `NOT_REQUIRED` unless an explicit gate exists;
- Tier 2 independent review is conditional on an authoritative contract and fails closed when the contract is absent, malformed, or unverified;
- Tier 3 independent review remains mandatory and the independent actor must be distinct from the implementation actor;
- required gate authority must match the canonical role map;
- project release/closure completion requires a required PASS `RELEASE` gate;
- bounded-task `IN_VALIDATION -> COMPLETE` is legal only when no release gate is required;
- the existing no-gate-downgrade, PAUSED/BLOCKED, canonical-audit, read-only, and final deterministic recheck rules remain in force.

This candidate profile does not create approval, QA, merge, release, activation, clinical, architecture, credential, GitHub-write, agent, or persistence authority for the Harness.
