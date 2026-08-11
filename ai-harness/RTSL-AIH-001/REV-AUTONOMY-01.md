# RTSL-AIH-001-REV-AUTONOMY-01

## Revision disposition

**Revision:** `RTSL-AIH-001-REV-AUTONOMY-01`
**Amendment:** `RTSL-KERNEL-AUTONOMY-001`
**Disposition:** **PREPARED FOR CONTROLLED ADOPTION — NOT ACTIVE**
**Default behavior:** unchanged `RTSL-AIH-V0-POLICY-1` / current Kernel profile
**Activation authority:** MASTER PROJECT CONTROL only

## Bounded revision

This revision adds a dormant, explicitly selected policy profile. It does not change the default evaluator path and does not add a GitHub client, write method, credential, permission, agent, runtime AI, persistence, or project-state mutation.

The selected candidate profile provides deterministic support for:

- Tier 0–1 `SELF_VALIDATION_SUFFICIENT` unless an explicit independent gate is present;
- Tier 2 conditional independent review, with authoritative contract evidence required for `NOT_REQUIRED` and fail-closed behavior otherwise;
- mandatory Tier 3 independent review and distinct implementation/reviewer identities;
- canonical gate-authority ownership checks;
- direct bounded-task `IN_VALIDATION → COMPLETE` only when no required `RELEASE` gate exists;
- explicit `PROJECT_RELEASE` / `PROJECT_CLOSURE` completion scope requiring a PASS `RELEASE` gate;
- separation of PR-open state from handoff, merge, QA, and activation authority.

The following remain unchanged and are re-evaluated in the selected profile: no-gate-downgrade, transition legality, approval authority, PAUSED/BLOCKED resume evidence, contradiction handling, evidence-producer/classifier separation, canonical audit, read-only boundary, and the mandatory final deterministic policy recheck.

## Implementation surface

- `config/ai_harness/autonomy.v1.json`
- `config/ai_harness/gates.v1.json` canonical gate-authority map
- `config/ai_harness/roles.v1.json` non-authority `AI_HARNESS` execution role
- `tools/ai_harness/schemas.py`
- `tools/ai_harness/transitions.py`
- `tools/ai_harness/policy.py`
- `tools/ai_harness/evaluator.py`
- `tools/ai_harness/github_readonly/integration.py`
- `tools/ai_harness/intake/authority.py`
- `tools/ai_harness/intake/gates.py`
- `tools/ai_harness/intake/assembly.py`
- `tools/ai_harness/intake/integration.py`
- `tests/ai_harness/test_autonomy.py`
- bounded AIH-004 regression additions in `tests/ai_harness/test_intake.py`

## Validation contract

The revision is not complete for activation until the exact implementation head has passing `AUTONOMY-001` through `AUTONOMY-016`, the complete existing AIH-001/002/004 regression suite, canonical reproducibility checks, unchanged final-recheck checks, diff/provenance review, and any required independent QA disposition.

**Exact activation condition:** MASTER PROJECT CONTROL records project-wide activation after those gates pass and no unresolved scope, risk, clinical, architecture, authority, or provenance conflict remains.
