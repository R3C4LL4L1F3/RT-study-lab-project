# RTSL-AIH-002 — GitHub Read-Only Evidence Integration

## Final Closure Status — 2026-08-11

**Task ID:** `RTSL-AIH-002`  
**Priority / Risk:** **P2 / Tier 1**  
**Current work state:** **COMPLETE**  
**Stage 1 independent QA:** **PASS / SATISFIED**  
**Stage 2 live read-only validation:** **PASS / SATISFIED**  
**Open confirmed defects:** **0**  
**Open validation gaps:** **0**  
**GitHub / provenance gate:** **SATISFIED**  
**Verified read-only credential boundary:** **SATISFIED — repository-scoped GitHub App installation token, read-only permission ceiling, `VERIFIED_READ_ONLY` preflight**  
**QA-validated implementation SHA:** `0e023ed79d0d7f13d19a830637e4376266259604`  
**Implementation PR:** `#22 — RTSL-AIH-002 Stage 1 GitHub read-only evidence provider` — **MERGED**  
**Implementation merge / resulting main SHA:** `d0e15589c62511c8b50c4118db0cb6497af0a90a`  
**Validated / merged tree SHA:** `5b49c077c7948d04ba1b598396cb74f672d527a1`

### Final validation provenance

Stage 1 independently validated the exact implementation head `0e023ed79d0d7f13d19a830637e4376266259604` with zero open Stage-1 defects and zero open Stage-1 validation gaps.

Stage 2 live validation used the approved repository-scoped GitHub App credential boundary against `R3C4LL4L1F3/RT-study-lab-project` only. The live credential capability resolved to `VERIFIED_READ_ONLY`; the frozen read permission ceiling was preserved; all nine frozen GET-only evidence operations were exercised successfully; collection completeness was established where applicable; secret non-serialization passed; no network write attempt occurred; and the final deterministic policy recheck executed and passed.

Stage 2 validation provenance:

- validation-only PR `#24` — **CLOSED UNMERGED**;
- GitHub Actions run `31460434475` — **SUCCESS**;
- job `93682699283 — validate-live-readonly` — **SUCCESS**;
- API version `2026-03-10`;
- repository identity `1328584202` / `R_kgDOTzCWCg`;
- repository scope: `R3C4LL4L1F3/RT-study-lab-project` only;
- requested permission ceiling: Metadata read, Contents read, Pull requests read, Checks read;
- credential capability: `VERIFIED_READ_ONLY`;
- network write attempts: `0`;
- secret serialization check: `PASS`;
- final deterministic policy recheck: performed and passed;
- full exact-head regression: `108/108 PASS`;
- `python3 -m compileall -q tools tests`: `PASS`.

### Merge / content provenance

PR #22 was marked ready for review without moving its head and was merged with the expected-head-SHA guard set to:

`0e023ed79d0d7f13d19a830637e4376266259604`

The resulting squash-merge commit is:

`d0e15589c62511c8b50c4118db0cb6497af0a90a`

The exact validated implementation head and the squash-merge commit both resolve to tree:

`5b49c077c7948d04ba1b598396cb74f672d527a1`

Therefore the implementation content merged to `main` is content-identical to the exact independently validated implementation head.

### Historical-state preservation

The prior project-control record is preserved below as historical state. Its earlier work-state, authorization, and sequencing statements describe the project at those earlier points and do not override the final closure status above.

---

# RTSL-AIH-002 — GitHub Read-Only Evidence Integration

## Durable Project-Control Record

**Task ID:** `RTSL-AIH-002`  
**Subsystem:** Shared Development / Governance Infrastructure  
**Model / feature:** `GitHubReadOnlyEvidenceProvider`  
**Project authority:** MASTER PROJECT CONTROL  
**Architecture owner:** `(PLANNING_ARCHITECTURE)`  
**Priority:** **P2 — Platform / Reusable Infrastructure**  
**Risk:** **Tier 1**  
**Current work state:** **APPROVED — IMPLEMENTATION AUTHORIZED / PROJECT-CONTROL SETUP IN PROGRESS**  
**Implementation stage authorized:** **Stage 1 mocked / fixture-backed adapter implementation only**  
**Live credential creation:** **NOT AUTHORIZED**

## Verified repository setup baseline

- Repository: `R3C4LL4L1F3/RT-study-lab-project`
- Verified `main` baseline for `RTSL-AIH-002-GH-SETUP-01`: `b6f062b79260c627856d9c0b1ece94631d25f887`
- Canonical task issue: `#19 — RTSL-AIH-002 — GitHub Read-Only Evidence Integration V0.x`
- Project-control documentation branch: `docs/rtsl-aih-002-project-control`
- Dedicated implementation branch: `feature/rtsl-aih-002-github-readonly-evidence`

Both branches were created from the verified setup baseline. No adapter code or credential configuration is part of this setup record.

## Completed baseline — RTSL-AIH-001

`RTSL-AIH-001 — RT Study Lab AI Development Harness V0` is **COMPLETE**.

The completed V0 provides the offline deterministic core that remains authoritative for policy evaluation. `RTSL-AIH-002` adds only an evidence-acquisition input path and must not change existing deterministic V0 semantics.

## Frozen AIH-GH-RO-001

`AIH-GH-RO-001` remains controlling for connected GitHub evidence:

- GitHub integration is evidence-only;
- repository mutation capability is prohibited;
- technical read-only capability must be verified rather than assumed from prompt instructions;
- unverified read-only capability fails closed or uses supplied/offline evidence;
- repository facts do not themselves establish project approval, QA acceptance, clinical truth, or work-state transitions.

## Frozen RTSL-AIH-002 architecture

The approved V0.x architecture is:

```text
allowlisted GitHub read facts
        ↓
GitHubReadOnlyEvidenceProvider
        ↓
provider-neutral normalized evidence records
        ↓
existing V0 deterministic core
        ↓
mandatory final deterministic policy recheck
```

The evidence provider must not move GitHub-specific response structures into policy functions and must not acquire project authority.

Preserved exclusions:

- runtime AI;
- agent framework;
- RAG;
- GitHub writes;
- autonomous task mutation;
- cross-task persistence;
- duplicate-task-ID detection;
- production repository/application changes;
- V0 policy-semantic changes.

## QA architecture correction history

QA initially identified four bounded architecture findings:

- `RTSL-AIH-002-QA-001` — deterministic 404 / `MISSING` eligibility;
- `RTSL-AIH-002-QA-002` — credential-capability preflight;
- `RTSL-AIH-002-QA-003` — evidence-state precedence;
- `RTSL-AIH-002-QA-004` — pagination / collection completeness.

The bounded corrections were independently retested by QA.

**QA bounded retest disposition:** **PASS / SATISFIED**  
**Open QA architecture findings:** **0**

QA accepts:

- deterministic `404 → MISSING` eligibility;
- credential-capability states and fail-closed preflight;
- evidence-state precedence;
- collection completeness / pagination semantics;
- mandatory golden architecture tests `GH-031` through `GH-040`.

Implementation QA remains pending and is separate from architecture QA.

## GitHub / Project-Control supporting review

**Review ID:** `RTSL-AIH-002-GH-ARCH-01`  
**Disposition:** **PASS / SATISFIED**

GitHub / Project-Control found no architecture-reopening correction and approved the candidate for architecture / endpoint / permission-manifest freeze.

## Frozen repository allowlist

Initial repository alias:

```text
PROJECT_CONTROL
→ R3C4LL4L1F3/RT-study-lab-project
```

Frozen expected identity:

- repository ID: `1328584202`
- node ID: `R_kgDOTzCWCg`
- default branch: `main`

No production repository, arbitrary owner/repository input, fork traversal as an evidence source, organization-wide discovery, or broad repository crawl is authorized in the initial slice.

## Frozen read-operation allowlist

Only these GitHub evidence operations are approved:

1. `GH-OP-REPO-GET` — repository identity/default-branch metadata;
2. `GH-OP-COMMIT-GET` — immutable commit lookup and branch-head lookup by explicit ref;
3. `GH-OP-CONTENT-GET` — explicit allowed file at explicit ref;
4. `GH-OP-PR-GET` — PR identity/head/base/state;
5. `GH-OP-PR-COMMITS-LIST` — PR commit membership collection;
6. `GH-OP-PR-FILES-LIST` — PR changed-file collection;
7. `GH-OP-PR-REVIEWS-LIST` — PR review collection;
8. `GH-OP-PR-MERGED-CHECK` — read-only merged-state fact;
9. `GH-OP-CHECK-RUNS-LIST` — check runs for explicit ref.

The provider must expose no generic authenticated HTTP request surface. Only the approved evidence operations may reach transport.

## Frozen authenticated permission ceiling

For the connected authenticated profile, the maximum approved repository permissions are:

- **Metadata: read**
- **Contents: read**
- **Pull requests: read**
- **Checks: read**

Any write capability is `OVERPRIVILEGED` and connected authoritative evidence retrieval must be refused.

## Credential architecture

Selected connected-mode credential architecture:

**repository-scoped GitHub App installation access token**

The credential/bootstrap boundary is external to the GET-only evidence provider. The provider receives only token/capability material required for the current process and must never serialize secret material into normalized evidence, audit output, logs, exceptions, or advisory output.

Before authoritative connected retrieval, capability preflight must establish `VERIFIED_READ_ONLY` for the approved repository and permission ceiling.

Non-authoritative states include:

- `NOT_CONFIGURED`
- `UNVERIFIED`
- `INVALID`
- `OVERPRIVILEGED`

If credential capability is not `VERIFIED_READ_ONLY`, connected retrieval cannot produce authoritative `VERIFIED` or `MISSING` evidence.

### Credential sequencing boundary

**Live GitHub App creation, installation, private key/token creation, and credential configuration are NOT AUTHORIZED during Stage 1.**

Stage 1 must use mocked / fixture-backed credential and transport behavior only.

## Frozen content-read allowlist

`GH-OP-CONTENT-GET` is restricted to:

- `ai-harness/RTSL-AIH-001/**`
- `ai-harness/RTSL-AIH-002/**`
- `docs/ai-harness/**`
- `config/ai_harness/**`

The implementation must reject path traversal, absolute paths, encoded traversal, normalization escapes, unexpected reference/symlink policy bypass, and arbitrary user/AI paths outside the governed allowlist.

PR-file listing may report paths outside these patterns for bounded change-scope evidence; that does not authorize content retrieval for those paths.

## Frozen GitHub REST API version

```text
X-GitHub-Api-Version: 2026-03-10
```

The implementation must pin this version explicitly. Future API-version changes require deliberate compatibility/permission/regression review; silent floating is prohibited.

## Corrected 404 / MISSING contract

A general HTTP 404 does not automatically mean `MISSING`.

`MISSING` is available only when deterministic prerequisites establish that the request used:

- the approved repository identity;
- an approved operation;
- `VERIFIED_READ_ONLY` credential capability;
- a valid current-run access/preflight state;
- endpoint semantics that support authoritative absence;
- no permission, transport, pagination, or completeness ambiguity.

Otherwise a 404 fails closed as `UNVERIFIED`.

For the dedicated PR merged-state operation, after PR existence/identity has already been authoritatively established:

- `204` → `VERIFIED { merged: true }`
- `404` → `VERIFIED { merged: false }`

## Evidence-state precedence

Frozen deterministic precedence:

```text
CONTRADICTORY
>
UNVERIFIED
>
STALE
>
MISSING
>
VERIFIED
```

These are evidence states only. They do not replace gate states, work states, QA disposition, or MASTER authority.

## Pagination / collection completeness

Collection completeness is distinct from individual observed evidence.

Frozen collection states:

- `COMPLETE`
- `INCOMPLETE`
- `UNVERIFIED`

If collection knowledge is not `COMPLETE`, the evaluator/provider may preserve positively observed items but may not establish authoritative absence or exhaustiveness from the incomplete collection.

This contract applies to PR commits, PR files, PR reviews, and check runs.

## Audit / provenance requirements

Normalized GitHub evidence must preserve, as applicable:

- provider identity;
- repository alias;
- repository ID/node ID;
- approved operation ID;
- subject/ref;
- request/retrieval timestamps;
- GitHub API version;
- evidence state;
- credential-capability state;
- collection completeness;
- canonical normalized payload hash.

Do not serialize credentials, Authorization headers, private keys, raw tokens, unnecessary response headers, or secret-bearing exception/log material.

A successful check run remains a repository evidence fact; it does not independently establish QA PASS. A GitHub reviewer identity likewise requires governed actor mapping before it can support canonical actor authority/independence checks.

## Negative-capability freeze

Write capability must be absent at all three layers:

### Credential

No permission above read. Any write grant is rejected as `OVERPRIVILEGED`.

### Provider API

No create/update/delete/merge/comment/review-submit/rerun/dispatch/push/release mutation methods.

### Transport

Only approved `GET` operations. `POST`, `PUT`, `PATCH`, and `DELETE` are rejected before network transmission.

Credential/bootstrap mechanics remain outside this GET-only evidence transport and are not authorized during Stage 1.

## Approved implementation plan

MASTER approved the `V0.x GitHub Evidence Adapter Implementation Plan` as the governing implementation specification for the bounded slice.

Authorized Stage 1 implementation includes:

- provider-neutral `EvidenceProvider`;
- `GitHubReadOnlyEvidenceProvider`;
- repository/operation/path allowlists;
- credential abstraction and preflight state machine;
- GET-only transport contract;
- approved scalar reads;
- pagination/completeness behavior;
- normalized evidence state resolution;
- audit integration;
- offline V0 preservation;
- golden tests `GH-001` through `GH-040`;
- negative-capability and secret-leakage tests.

## MASTER implementation authorization

**Disposition:** **AUTHORIZED — BOUNDED V0.x ADAPTER ONLY**

Stage 1 may begin after completion of `RTSL-AIH-002-GH-SETUP-01`.

The implementation owner must inspect the current V0 implementation before code changes, preserve current deterministic behavior, add only the approved evidence-provider slice, use mock/fixture-backed transport first, run focused regression, record the exact implementation SHA, prepare a PR, and hand the result to independent QA.

## Required implementation acceptance evidence

Before Stage 1 can advance beyond code QA, evidence must establish at minimum:

1. existing offline V0 regression remains green;
2. `GH-001` through `GH-040` pass;
3. no policy module imports GitHub-specific code;
4. all provider evidence operations are GET-only;
5. non-GET requests fail before network;
6. provider exposes no mutation methods;
7. repository/path allowlists fail closed;
8. ambiguous 404 → `UNVERIFIED`;
9. eligible authoritative 404 → `MISSING`;
10. incomplete collections cannot establish absence/exhaustiveness;
11. credential material cannot enter logs/audit/evidence;
12. reviewer/check evidence cannot independently establish QA PASS;
13. offline execution works with provider absent;
14. final deterministic policy recheck still executes.

## Implementation sequence

```text
Stage 1 — AUTHORIZED AFTER PROJECT-CONTROL SETUP
mocked / fixture-backed adapter implementation
        ↓
implementation-owner validation
        ↓
independent QA of code + negative capability
        ↓
return to MASTER

Stage 2 — NOT AUTHORIZED
live GitHub App bootstrap / credential configuration
        ↓
live read-only evidence validation
        ↓
independent QA
        ↓
merge authorization
```

## Current validation / closure boundary

Current project state remains **APPROVED — IMPLEMENTATION AUTHORIZED / PROJECT-CONTROL SETUP IN PROGRESS** until this documentation record is merged through the approved repository workflow.

No live credential bootstrap, repository mutation capability, production change, runtime AI, agent framework, RAG, cross-task persistence, duplicate-task-ID detection, or V0 policy-semantic expansion is authorized by this record.

Final project closure requires independently validated Stage 1 code, separately authorized and independently validated Stage 2 live read-only bootstrap, merged implementation, post-merge provenance verification, and MASTER closure.
