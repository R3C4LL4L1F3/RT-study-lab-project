# RTSL-KERNEL-AUTONOMY-001 — Operating Manual Amendment

## Status and source boundary

This is a controlled, additive amendment to the inspected RT Study Lab AI-Assisted Development Operating Manual Version 2.6 Phase 1 working candidate. It is a repository-durable migration overlay, not a claim that the external DOCX has been approved or replaced. Existing manual wording remains in force unless this amendment is explicitly activated by MASTER PROJECT CONTROL.

The amendment is deliberately written as a narrow overlay. It does not globally replace `review`, `QA`, `approval`, `merge`, `complete`, or `release` language.

## Controlled execution standard

Once a bounded task is authorized, the implementation owner continues through ordinary in-scope inspection, editing, testing, diff review, branch, PR, CI, and documentation milestones without returning to MASTER for each internal milestone. The owner stops and returns to MASTER for a material scope change, priority/risk change, failed mandatory gate that cannot be corrected within scope, unresolved clinical/architecture/authority conflict, true blocker, project release, project-wide activation, or project closure.

An open PR is a repository state. It is not a handoff requirement. GitHub approval is evidence from GitHub; it is not merge authority, independent QA, or project activation. Merge authority and project activation remain governed by the applicable MASTER and repository controls.

## Gate applicability matrix

| Work class | Classification | Rule |
|---|---|---|
| Tier 0 | `SELF_VALIDATION_SUFFICIENT` | The implementer may perform engineering self-validation when no independent gate is explicitly required. This is not independent QA and cannot authorize release. |
| Tier 1 | `SELF_VALIDATION_SUFFICIENT` by default | The implementer may self-validate ordinary bounded work unless an authoritative task contract explicitly requires independent review or QA. A gate that is already established remains protected by no-gate-downgrade. |
| Tier 2 | `CONDITIONAL` | Independent validation is required when the authoritative task contract requires it. A `NOT_REQUIRED` result is valid only with an authoritative contract reference, revision, and authority record. Missing or unverified conditions fail closed. |
| Tier 3 | `INDEPENDENT_VALIDATION_REQUIRED` | Independent review/QA remains mandatory. The implementation owner cannot self-certify, waive, or replace the independent gate. |

The matrix changes who must perform a gate, not the evidence standard. Clinical, architecture, QA, GitHub/provenance, and release authorities remain separate truth domains.

## State and completion distinction

- `IN_VALIDATION → COMPLETE` may be used for a bounded task only when no separate release gate is required and the deterministic policy profile permits the direct transition.
- Bounded-task `COMPLETE` means the authorized task scope and its applicable validation are complete. It does not mean the project release is approved, the PR is merged, the site is deployed, or the project is closed.
- Project release and project closure require their own authority, evidence, provenance, and gates. They remain MASTER PROJECT CONTROL decisions.

## PAUSED / BLOCKED contracts

`PAUSED` records must contain the pause reason, responsible owner, exact resume condition, `previous_state`, `resume_condition_satisfied: true`, and non-empty `resume_evidence_refs` before resuming to the previous state.

`BLOCKED` records must contain the blocker description, responsible owner, exact unblock condition, `previous_state`, `unblock_condition_satisfied: true`, and non-empty `unblock_evidence_refs` before resuming to the previous state.

An exact resume/unblock condition is a verifiable condition, not “continue later,” “user decides,” or an unbounded request for clarification. If the condition cannot be satisfied within the authorized scope, the task returns to MASTER with the exact condition required to resume.

## Sole-human interruption rule

The current authorized session performs ordinary safe in-scope repository inspection, file editing, testing, branch preparation, PR preparation, and evidence collation itself. It does not ask the sole human to relay an operation that the session can safely perform.

The session must still stop for decisions reserved to a human authority: material scope, priority/risk, clinical truth, architecture approval, required independent QA disposition, merge/release authority, project closure, or project-wide activation.

## Preserved guardrails

- No-gate-downgrade remains in force.
- Tier 3 independent validation remains mandatory.
- The AI Harness remains deterministic/read-only/advisory and cannot approve itself, merge, write to GitHub, activate governance, or make autonomous clinical decisions.
- The AIH-001 final deterministic recheck and canonical audit remain mandatory.
- AIH-002 evidence states and collection completeness remain unchanged.
- Incremental cost remains `$0`.

## Activation

This amendment becomes governing policy only when MASTER PROJECT CONTROL records explicit project-wide activation after the migration handoff has passed all applicable validation and provenance gates. Until then, the existing Operating Kernel and current manual remain authoritative.
