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

Approvals are explicit records. Free text never creates approval.

Confirmed-defect findings preserve evidence-producer identity separately from authoritative classification identity.
