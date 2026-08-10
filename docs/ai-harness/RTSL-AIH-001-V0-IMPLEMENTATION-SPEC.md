# RTSL-AIH-001 — V0 Implementation Specification

**Priority:** P2  
**Risk:** Tier 1  
**Architecture:** frozen v1.1  
**Implementation option:** Option A  
**Runtime:** plain Python / standard library  
**Runtime AI:** none  
**Incremental AI-service cost:** $0  
**Implementation branch:** `feature/rtsl-aih-v0-harness`

## Vertical slice

V0 is a local offline deterministic evaluator:

`local JSON snapshot → schema validation → deterministic rules → transition/gate/approval/finding evaluation → deterministic recommendation → canonical audit + SHA-256 → mandatory final policy recheck → local read-only result artifacts`

The evaluator exposes one operation:

```text
python -m tools.ai_harness evaluate path/to/task.json --output-dir path/to/output
```

It does not mutate the input task or any repository/project state.

## Bounded scope

Implemented:

- canonical task/actor/gate/approval/finding structures;
- P0–P3 and Tier 0–3 validation;
- canonical work-state validation;
- frozen transition matrix;
- PAUSED/BLOCKED contracts;
- mandatory gate enforcement;
- no-gate-downgrade checks;
- approval-authority checks;
- QA actor-independence checks;
- validation-gap vs confirmed-defect separation;
- `RTSL-AIH-QA-004` evidence-producer/classifier separation;
- `RTSL-CANONICAL-RECORD-1`;
- SHA-256 input/findings/output/audit identity;
- substantive final deterministic policy recheck;
- disabled/read-only GitHub adapter extension point.

Not implemented:

- AI/model calls;
- GitHub network integration;
- GitHub write capability;
- project-state mutation;
- production app changes;
- multiple concurrent tasks;
- cross-task registry/persistence;
- duplicate-task-ID detection.

`RTSL-AIH-IMP-001` explicitly defers duplicate-task-ID detection beyond the initial isolated-task V0 slice.

## Kernel identity

The V0 config identifies `RT Study Lab Project Operating Kernel` version `V1.0`. The durable Kernel source revision and content hash are currently represented as `UNAVAILABLE`; the harness does not fabricate them.

## Exit behavior

- `0` evaluation completed, including deterministic denial/incomplete result;
- `2` invalid input/schema;
- `3` contradictory authoritative state;
- `4` unknown/untrusted Kernel profile/version;
- `5` internal final-policy-recheck failure;
- `6` unexpected internal harness error.

No evaluation result authorizes a project transition by itself. Project authority remains external.
