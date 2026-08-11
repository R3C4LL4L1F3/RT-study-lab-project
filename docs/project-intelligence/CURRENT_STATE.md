# Phase 1 Current-State Snapshot

> PHASE COVERAGE: 1 OF 3
> PROJECT CHAT COVERAGE: PARTIAL
> GLOBAL PROJECT RECONCILIATION: NOT YET COMPLETE
> CODEX-READY GLOBAL BASELINE: NOT YET ESTABLISHED

**Snapshot date:** 2026-08-11
**Scope:** six assigned chats, project-control repository, production repository, and the existing GitHub Project
**Status semantics:** live evidence below is separated from older chat claims and stale documentation.

## Executive state

| Surface | Verified current state | Evidence boundary |
|---|---|---|
| Project-control repository | `R3C4LL4L1F3/RT-study-lab-project`, public, default `main` at `e97a83b984f96d51dc7c3a29789eee2be7e52a9f`; PR #30 merged; no open PRs; 16 branches; 0 tags | Repository and GitHub page |
| Production repository | `R3C4LL4L1F3/RT-study-lab`, private, default `main` at `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`; 5 branches; 1 open draft PR (#3); main is not protected; 0 tags/releases | Repository and GitHub page |
| Production CI | `Production Validation` run `31311314980` for `d64bde3` on `main`: `Success`; one artifact; warnings are present | GitHub Actions run page |
| Existing GitHub Project | `RT Study Lab - Development Roadmap & Control`, owner `R3C4LL4L1F3`, private, Project #1 | GitHub Project |
| Phase 1 bridge | Bounded six-chat checkpoint in this directory; no global baseline | This Phase 1 record |

The project-control `main` ref is newer than the older local working branch and older README status lines. Future Codex sessions must use the live ref plus the reconciliation notes rather than treating those older lines as current.

## Existing Project configuration

The current Project has **13 items**, **13 named views**, and **5 enabled workflows**. No new Project item was created for this bridge; existing records were corrected only where an explicit current issue/closure record supplied the state.

### Current roadmap items

| Item | Current Project status | Supporting current record |
|---|---|---|
| #3 Verify Ventilator Waveform Lab historical P1 correctness concerns | `IN VALIDATION` | Issue #3; manual/browser validation remains open |
| #5 Verify Interactive Equipment Lab fidelity and browser readiness | `IN VALIDATION` | Issue #5; manual/runtime validation remains open |
| #8 Establish ChatGPT Sites deployment-to-Git commit correspondence | `BLOCKED` | Issue #8; authoritative Sites metadata remains required |
| #9 Establish Interactive Models & Simulation Lab architecture/model contract | `APPROVED` | Issue #9; production implementation is not implied |
| #10 Establish independent clinical-validation framework | `APPROVED` | Issue #10; approved, not executed |
| #11 Establish accessibility-validation baseline | `APPROVED` | Issue #11; approved, not executed |
| #12 Define production branch and release control policy | `DEFERRED` | Issue #12; later dependency/gate required |
| #14 RTSL-AIH-001 - AI Development Harness V0 | `COMPLETE` | Closed issue #14 and project-control records |
| #19 RTSL-AIH-002 - GitHub Read-Only Evidence Integration V0.x | `COMPLETE` | Closed issue #19 and project-control records |
| #26 [DEFERRED] RTSL-AIH-003 - AI Development Harness pilot specification | `DEFERRED` | Explicit current disposition in issue #26 |
| #27 [APPROVED] RTSL-WF-001 - Project response and handoff workflow optimization | `APPROVED` | Explicit current disposition in issue #27 |
| #28 RTSL-AIH-004 - Task Intake & Context Assembly | `COMPLETE` | Explicit MASTER closure in issue #28; PR #30 merged |
| #32 RTSL-QA-MODEL-001 - Risk-Based QA Operating Model Migration | `APPROVED` | Explicit current work state in issue #32; policy edits not yet authorized |

The four bottom-of-queue corrections were made during this Phase 1 cycle: #26 `PROPOSED -> DEFERRED`, #27 `PROPOSED -> APPROVED`, #28 `PROPOSED -> COMPLETE`, and #32 `PROPOSED -> APPROVED`. No other Project item was changed.

### Named views

`MAIN - Work State`, `Executive Roadmap`, `Active Development`, `Future Roadmap`, `Historical Milestones`, `By Workstream`, `By Owner`, `High-Risk Work`, `Validation Queue`, `Blocked / Paused`, `Infrastructure & Governance`, `Roadmap / Timeline`, and `Gate Review`.

### Enabled workflows

1. `Auto-add sub-issues to project`: when an item has sub-issues, add the sub-issues.
2. `Auto-add to project`: when the filter matches a new or updated item, add the item; current filter is `RT-study-lab-project`.
3. `Auto-close issue`: when status is `COMPLETE`, close the issue.
4. `Item added to project`: when an issue or pull request is added, set `Status: PROPOSED`.
5. `Pull request linked to issue`: when a pull request is linked to an issue, set `Status: IN PROGRESS`.

The current enabled list does not show a closed-issue-to-`COMPLETE` or merged-PR-to-`COMPLETE` workflow. The current `Auto-close issue` direction is the reverse: Project status `COMPLETE` closes the issue.

## Live repository facts

### Project-control repository

- `main` currently points to merge commit `e97a83b984f96d51dc7c3a29789eee2be7e52a9f` from PR #30.
- The resulting tree is recorded in PR #30 as `ba5c0f3be77d3c5b607a461348b7c2533bb1f4a5`.
- PR #29 (Three.js circulation renderer planning) is merged; it is documentation/planning only and does not authorize production implementation.
- PR #31 (autonomy migration) is merged into the AIH-004 feature branch, not directly into `main`; its effect is included in the PR #30 merge.
- Current GitHub pull-request list shows 0 open and 14 closed project-control PRs.
- Current GitHub branch list shows 16 branches and 0 tags.

### Production repository

- `main` currently points to `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`.
- `Production Validation` run `31311314980` succeeded for that ref. The run is repository-validation evidence only; it is not independent clinical, accessibility, live-deployment, or release evidence.
- Draft PR #3, `M1 Three.js oxygen transport renderer shell`, is open and not mergeable while draft. Its body reports focused contract tests `3/3` and a local full-build/typecheck limitation; GitHub currently shows one successful validation check, which still does not authorize integration or clinical claims.
- The production repository has no tags or GitHub Releases and its `main` branch is not protected.
- Issue #8 remains blocked on authoritative ChatGPT Sites deployed-commit metadata.

## Current gates and limitations

- #3 and #5 remain in validation; manual/browser/runtime evidence is not replaced by repository presence or CI.
- #10 clinical-validation framework is approved but not executed; no new clinical disposition was created by Phase 1.
- #11 accessibility baseline is approved but not executed.
- #12 and #26 remain deferred.
- #9 and PR #29 establish planning evidence only; production PR #3 remains a draft.
- The current repository contains an explicit PR #30 comment activating `RTSL-KERNEL-AUTONOMY-001`, while the durable adoption record on `main` still says `NOT YET ACTIVE`. This is recorded as an unresolved contradiction in [`RECONCILIATION.md`](RECONCILIATION.md); Phase 1 does not decide which record to rewrite.

## Not established by this snapshot

This file does not establish a global project baseline, complete clinical validation, release readiness, live Sites correspondence, universal current status for unprocessed chats, or a replacement for MASTER/Architecture/Clinical/QA/GitHub authority.
