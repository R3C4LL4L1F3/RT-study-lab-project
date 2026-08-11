# RTSL-KERNEL-AUTONOMY-001 — Controlled Governance Migration

## Durable adoption record

**Amendment:** `RTSL-KERNEL-AUTONOMY-001 — Continuous Execution / Sole-Human Repository Governance Amendment`
**Adoption disposition:** **APPROVED FOR CONTROLLED ADOPTION**
**Activation state:** **NOT YET ACTIVE**
**Current governing policy:** Existing RT Study Lab Project Operating Kernel and `RTSL-AIH-V0-POLICY-1` remain authoritative until the activation condition below is satisfied.

This record is the durable project-control record for the approved migration. It records preparation and adoption of the amendment; it does not activate the amendment or authorize project-wide release/closure.

## Activation condition

Project-wide activation requires a separate explicit `MASTER_PROJECT_CONTROL` decision after:

1. the migration branch is reviewed and merged through the permitted GitHub workflow;
2. all required deterministic regression and provenance checks pass;
3. any required independent validation is recorded by an independent QA authority;
4. Tier 3 independence, no-gate-downgrade, clinical/architecture boundaries, and the AIH-001 final deterministic recheck are verified at the exact implementation head; and
5. no unresolved clinical, architecture, authority, mandatory-gate, or provenance conflict remains.

Until then, a prepared autonomy profile is a migration candidate only. A pull request being open, a GitHub review being present, or a CI check being green does not activate the amendment, authorize merge, satisfy independent QA, or authorize project release/closure.

## Preserved controls

- Tier 3 independent validation remains mandatory. The implementer cannot self-certify a Tier 3 independent gate.
- No-gate-downgrade remains mandatory. A previously established or explicitly required gate cannot be removed by this amendment.
- AIH-001 remains the deterministic policy/evaluator authority and retains legal transition checks, authority checks, PAUSED/BLOCKED contracts, canonical audit, and the final deterministic policy recheck.
- AIH-002 remains the evidence-only `EvidenceProvider` boundary. Evidence state and collection completeness remain separate and no GitHub write capability is introduced.
- The AI Harness receives no merge, approval, release, comment, push, credential, or project-state mutation authority.
- The migration introduces no runtime AI, agents, RAG/vector storage, persistence, autonomous clinical decisions, or paid runtime service.
- Incremental cost remains `$0`.

## Governance distinctions adopted for controlled preparation

- Continuous execution is permitted inside an already-authorized bounded task. It does not authorize a new task, a material scope change, a new priority/risk classification, a project-wide activation, a release, or project closure.
- `PR_OPEN` is a repository fact, not a handoff state. GitHub approval, merge authority, independent QA, and MASTER activation authority remain separate facts and authorities.
- Tier 0–1 work normally uses `SELF_VALIDATION_SUFFICIENT` unless an authoritative contract explicitly adds an independent gate.
- Tier 2 work is `CONDITIONAL`: independent validation is required when the authoritative task contract says so; an authoritative, recorded `NOT_REQUIRED` condition is required for the exception. Missing or unverified conditions fail closed.
- Tier 3 work is `INDEPENDENT_VALIDATION_REQUIRED`.
- `IN_VALIDATION → COMPLETE` is available only for a bounded task when no separate release gate is required. Project release and project closure remain separate decisions and cannot be inferred from bounded-task completion.
- `PAUSED` requires a reason, owner, exact resume condition, and satisfied-condition evidence before resumption. `BLOCKED` requires a blocker, owner, exact unblock condition, and satisfied-condition evidence before resumption.
- If the current authorized session can safely perform an ordinary in-scope operation, it performs that operation rather than asking the sole human to relay it. Human decisions remain required for authority, scope, activation, release, closure, and any required independent gate.

## Approved migration sequence

1. Establish this durable adoption record.
2. Source-inspect the current Kernel, manual, role archive, QA/GitHub contracts, AIH-001, AIH-002, and AIH-004 artifacts.
3. Record KEEP / CLARIFY / MODIFY / SUPERSEDE / NO_CHANGE dispositions in the migration register.
4. Add the smallest coherent governance and role-contract overlays while preserving unrelated wording.
5. Add the dormant controlled-adoption AIH-001 policy profile and deterministic semantics.
6. Reconcile AIH-004 only at the real gate-matrix seam; preserve its architecture, EvidenceProvider reuse, evidence semantics, and V0 final recheck.
7. Run `AUTONOMY-001` through `AUTONOMY-016` and the existing AIH-001/002/004 suite.
8. Review the exact diff, branch, PR, CI, and provenance state.
9. Route the result to independent QA where the governing contract requires it; do not self-certify that gate.
10. Return a consolidated activation package to MASTER and stop before project-wide activation.

## Source and baseline evidence

| Artifact | Source / status | Verified identity |
|---|---|---|
| AIH-004 v1.1 specification | User-supplied recovered normative source; complete `INTAKE-054`–`INTAKE-085`, QA-001–003, and GH-001–003 definitions present | SHA-256 `6DF0A7EFF3F6D3FD226DA57DF4F58BA6C0907E0EBB63118CC5F5E80606508EFA` |
| Operating Manual | Available external Version 2.6 Phase 1 working candidate; not labeled as an approved repository artifact | SHA-256 `C93E9E01E2468AFA4FBD16C34E39EBB5A00ADF017B3993AF3D67832B0F6EF41D` |
| Role archive inventory | Available external Version 2.6 Phase 1 inventory; missing prompts are explicitly marked unavailable | SHA-256 `B2107A6E52C9372F705CEB7C990FA9C6901A9F0F9493C5A179B7CC5A4285CD85` |
| Migration base | AIH-004 implementation head used as the migration starting point | `2f6d40fa995938b0089ad71690f7f5b7936d9ac9` |
| Migration implementation commit | Reviewed bounded migration implementation | `99df24b65acf9e7fd61f1984687e4fb5725e49d2` (exact commit before this provenance-only record update) |
| Remote main at inspection | Current project-control main after PR #29; not the migration branch | `f1b6f59322d5499a5fd180ed5741595df35cb872` |

## Affected durable artifacts

- This adoption record.
- `RTSL-KERNEL-AUTONOMY-001-CONFLICT-MIGRATION-REGISTER.md`.
- `RTSL-KERNEL-AUTONOMY-001-OPERATING-MANUAL-AMENDMENT.md`.
- `RTSL-KERNEL-AUTONOMY-001-ROLE-CONTRACT-AMENDMENT.md`.
- `RTSL-KERNEL-AUTONOMY-001-INDEPENDENT-QA-HANDOFF.md`.
- Dormant AIH-001 controlled-adoption configuration and deterministic policy tests.
- AIH-004 gate-derivation/V0 handoff seam, only where the conditional matrix is explicitly selected.
- Existing AIH-001/002/004 contracts and fixtures remain preserved; no second GitHub client or write path is added.

## Current migration disposition

**Controlled migration prepared; project-wide activation not performed.**

Implementation-owner validation currently records targeted autonomy/intake tests `56/56 PASS`, the complete repository suite `164/164 PASS`, unchanged default AIH-001 fixture outputs, and no independent QA disposition. The complete 25-item handoff is durable in `RTSL-KERNEL-AUTONOMY-001-INDEPENDENT-QA-HANDOFF.md`.

The exact resume condition for this record is: `MASTER_PROJECT_CONTROL` records an explicit activation decision after the exact migration head has passed all required regression, provenance, and independent-validation gates.
