# RTSL-KERNEL-AUTONOMY-001 - Temporary QA Governance Deviation

**Disposition:** TEMPORARY GOVERNANCE DEVIATION - NOT A QA PASS

**Recorded:** 2026-08-11

**Authority source:** The current MASTER-directed repository instruction supplied by the project owner explicitly authorizes bypassing the previously required independent-QA gate for this governance migration until the QA model is replaced. This record preserves that instruction as a temporary deviation; it does not convert implementation-owner validation into independent QA.

## Affected operation

This deviation is limited to merge recovery for PR #30, `RTSL-AIH-004 - Task Intake & Context Assembly`, after PR #31 was merged into the AIH-004 feature branch and the feature branch diverged from current `main`.

Verified pre-recovery state:

- AIH-004 feature head: `17798cc8c6b6cc97da3bd66752b261c683c9f281`.
- Current `main`: `f1b6f59322d5499a5fd180ed5741595df35cb872`.
- PR #30: open and non-mergeable before conflict recovery.

## Exact deviation

The prior independent-QA requirement may be bypassed for this one authorized migration merge after the exact conflict is resolved and all listed deterministic, regression, canonicalization, compilation, provenance, and post-merge checks pass. The bypass is a procedural governance exception only.

It does not:

- issue a QA PASS or independent validation disposition;
- waive Tier 3 mandatory independent clinical/safety validation;
- change AIH-001 deterministic policy semantics;
- remove no-gate-downgrade;
- grant the Harness approval, merge, release, activation, or GitHub-write authority;
- activate `RTSL-KERNEL-AUTONOMY-001` project-wide; or
- authorize unrelated scope, priority, risk, clinical, architecture, release, or closure changes.

## Required evidence before merge

The implementation owner must record the exact conflict files and resolution, pass AUTONOMY-001 through AUTONOMY-016, pass the targeted and full harness suites, pass JSON/compilation/canonicalization/reproducibility/final-recheck validation, push the resolved feature branch, verify PR #30 is mergeable, and verify the resulting `main` SHA and Git tree after merge.

## Expiry and non-reuse

This deviation applies only to the identified PR #30 recovery/merge. It expires after post-merge verification is recorded and cannot be reused for another task. The QA model replacement must establish a new authoritative QA contract before future governance work relies on a changed independence model.

**Historical pre-activation state:** `RTSL-KERNEL-AUTONOMY-001` was `NOT ACTIVE` until MASTER PROJECT CONTROL recorded a separate explicit project-wide activation decision. That decision is now recorded in PR #30 comment [`#issuecomment-5253465946`](https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/30#issuecomment-5253465946) at `2026-08-11T12:56:49Z`; the current activation state is `ACTIVE`. This does not convert the deviation into a QA PASS or waive Tier 3 independent validation.
