# RTSL AI Harness V0 Schema

V0 accepts one JSON object with required fields:

- `task_id`, `title`
- `priority`: `P0|P1|P2|P3`
- `risk_tier`: `TIER_0|TIER_1|TIER_2|TIER_3`
- `work_state`
- `routing`
- `gates`
- `approvals`
- `findings`
- `kernel.profile_id`
- `kernel.version_ref`

Canonical work states:

`PROPOSED`, `APPROVED`, `READY`, `IN_PROGRESS`, `IN_VALIDATION`, `READY_FOR_RELEASE`, `COMPLETE`, `PAUSED`, `BLOCKED`, `DEFERRED`, `REJECTED`, `CANCELLED`.

Gate states:

`NOT_REQUIRED`, `REQUIRED_PENDING`, `IN_REVIEW`, `PASS`, `FAIL`, `BLOCKED`.

Actor types:

`HUMAN`, `VERIFIED_TOOL`, `AI_ADVISORY`, `VERIFIED_GOVERNED_SYSTEM`.

Frozen finding types:

`VALIDATION_GAP`, `CONFIRMED_DEFECT`, `OBSERVATION`, `UNRESOLVED`.

Approvals are explicit records. Free text never creates approval. The frozen transition matrix requires an explicit authorized `MASTER / APPROVED` human approval for `PROPOSED -> APPROVED`.

Every gate whose `obligation.required` is true must identify `authority.owner_role`. A gate required by the task's risk tier cannot be represented as `required: false` merely because a gate record exists.

For a PAUSED/BLOCKED resume to `previous_state`, V0 requires both legal previous-state provenance and explicit satisfied-condition evidence:

- PAUSED: `resume_condition_satisfied: true` plus non-empty `resume_evidence_refs`;
- BLOCKED: `unblock_condition_satisfied: true` plus non-empty `unblock_evidence_refs`.

The `previous_state` must itself be a canonical state from which the frozen matrix legally permits entry into PAUSED/BLOCKED.

Confirmed-defect findings preserve evidence-producer identity separately from authoritative classification identity. `OBSERVATION` and `UNRESOLVED` are preserved as their own frozen finding types and are not silently promoted to `CONFIRMED_DEFECT`.

The controlled-adoption candidate may additionally carry `completion_scope` (`BOUNDED_TASK`, `PROJECT_RELEASE`, or `PROJECT_CLOSURE`) and a `governance.independent_review` contract. The contract may mark Tier 2 independence `NOT_REQUIRED` only with a `project-control://` reference, contract revision, and human `MASTER_PROJECT_CONTROL` authority. These fields are dormant until the controlled profile is explicitly selected; the current V0 profile remains the default.
