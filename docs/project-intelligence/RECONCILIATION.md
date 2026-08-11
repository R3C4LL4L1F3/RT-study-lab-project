# Phase 1 Normalization and Reconciliation

> PHASE COVERAGE: 1 OF 3
> PROJECT CHAT COVERAGE: PARTIAL
> GLOBAL PROJECT RECONCILIATION: NOT YET COMPLETE
> CODEX-READY GLOBAL BASELINE: NOT YET ESTABLISHED

## Method

The six assigned project chats were collected through their accessible app records, including pagination. Claims were normalized into work items, decisions, milestones, validation events, architecture/clinical requirements, dependencies, blockers, future initiatives, repository events, and state transitions. No identifier, date, owner, priority, risk, gate, or completion state was invented.

The reconciliation order was: explicit authority and source provenance; current GitHub repository, issue, PR, branch, commit, and Actions evidence; current Project item, view, field, and workflow evidence; historical chat claims retained as claims unless confirmed; and explicit conflict recording with owner and evidence needed.

## Source register

| Source | Record ID | Collection result | Main contribution |
|---|---|---:|---|
| MASTER PROJECT CONTROL | `6a786390-94a4-83ea-b9ec-2fb410d9aee3` | 8 pages / 77 turns | authority model, queue, governance activation/closure claims, issue-state decisions |
| (PLANNING_ARCHITECTURE) | `6a60717e-b014-83ea-9f4f-d09610a70707` | 25 pages / 247 turns | AIH-004 architecture, QA gate conflict disposition, Three.js planning and architecture claims |
| Clinical Validation & Sources | `6a7863d2-798c-83ea-ab01-788248c2451e` | 1 page / 4 turns | clinical authority boundary and AIH-001 clinical-gate exclusion review |
| QA - Regression & Release | `6a786440-20c0-83ea-a52c-3dd6de11cf5e` | 6 pages / 54 turns | AIH-004 QA corrections, QA retest, risk-/contract-based QA model |
| ROADMAP (GitHub) | `019fef59-e6a4-70d0-b39e-13548f35a9ff` | 1 page / 3 turns | Project creation/import/schema/view/workflow implementation record |
| GitHub PR and Documentation | `6a784402-36e8-83ea-8444-341624a5a9c4` | 7 pages / 69 turns | repository setup, PR/branch/merge/validation provenance claims, project-control durability |

`sources/` contained zero synchronized files at inspection time. Direct chat records are therefore the collection source for this bounded phase; the repository and GitHub Project are the current-state evidence sources.

## Normalized entity register

| Entity | Type / ID status | Normalized state or disposition | Authority and evidence |
|---|---|---|---|
| RTSL-AIH-001 | Work item; ID verified from chat and issue #14 | `COMPLETE` in current Project and closed issue; deterministic V0 harness baseline is present in project-control `main` | MASTER/GitHub; Clinical chat supplied a bounded authority-boundary `PASS`, not clinical content validation |
| RTSL-AIH-002 | Work item; ID verified from chat and issue #19 | `COMPLETE` in current Project and closed issue; read-only evidence boundary remains a repository contract | GitHub/Documentation and current repository; no write authority inferred |
| RTSL-AIH-003 | Work item; ID verified from chat and issue #26 | `DEFERRED`; fixtures, goldens, corpus admission, and pilot execution remain unauthorized | MASTER issue #26; exact resume conditions retained |
| RTSL-WF-001 | Work item; ID verified from issue #27 | `APPROVED`; response/handoff optimization does not change clinical, architecture, QA, or release authority | MASTER issue #27; Project status corrected |
| RTSL-AIH-004 | Work item; ID verified from chat and issue #28 | Explicit MASTER closure `COMPLETE`; PR #30 merged to project-control `main`; independent implementation QA PASS is not claimed | Issue #28, PR #30, commit `e97a83b`; governance deviation remains separate from QA PASS |
| RTSL-QA-MODEL-001 | Work item; ID verified from issue #32 | `APPROVED` requirements/contract migration; QA chat says contract complete, policy/configuration edits not authorized by the record | Issue #32 and QA chat; Project status corrected |
| RTSL-QA-MODEL-ARCH-001 | Architecture decision; ID verified from Planning/QA records | `RESOLVED`: Tier 2 `INDEPENDENT_REVIEW` and `QA` are conditional and independently triggerable; no policy edit authorization | Planning authority and QA supporting review; not a repository policy change |
| RTSL-KERNEL-AUTONOMY-001 | Governance decision; ID verified from chat/PR #31/PR #30 | `ACTIVE` effective `2026-08-11T12:56:49Z` by the explicit MASTER activation decision recorded after PR #30 merged; the adoption record's earlier `NOT YET ACTIVE` wording is preserved historical preparation state | MASTER authority decision plus GitHub durable PR #30 comment, merge, and adoption-record chronology; C-001 resolved |
| Issue #3 | Defect/validation work item; task ID missing | `IN VALIDATION`; Ventilator historical P1/browser/manual validation remains open | Current Project/issue; `ID_STATUS: MISSING / NEEDS NORMALIZATION` |
| Issue #5 | Validation work item; task ID missing | `IN VALIDATION`; 3D equipment fidelity/browser/runtime validation remains open | Current Project/issue; `ID_STATUS: MISSING / NEEDS NORMALIZATION` |
| Issue #8 | Blocker/work item; task ID missing | `BLOCKED`; authoritative Sites deployed Git commit metadata is required | Current Project/issue; exact unblock condition retained |
| Issue #9 | Architecture/work item; task ID missing | `APPROVED`; Interactive Models architecture/model contract is approved; no production implementation authorization | Current Project/issue, PR #29 planning merge, Three.js docs |
| Issue #10 | Validation framework/work item; task ID missing | `APPROVED`; independent clinical-validation framework is not executed | Current Project/issue |
| Issue #11 | Validation framework/work item; task ID missing | `APPROVED`; accessibility-validation baseline is not executed | Current Project/issue |
| Issue #12 | Governance/release work item; task ID missing | `DEFERRED`; branch/release controls await approved dependency/sequence | Current Project/issue |
| PR #29 | Repository event; GitHub ID verified | Merged documentation-only Three.js planning package; no production renderer authorization | Current GitHub PR and `main` history |
| PR #30 | Repository event; GitHub ID verified | Merged AIH-004 plus stacked migration recovery; resulting `main` `e97a83b`; 0 checks on PR page | Current GitHub PR, commit, tree, and issue #28 |
| PR #31 | Repository event; GitHub ID verified | Merged into the AIH-004 feature branch, then included in PR #30; original PR body retained `NOT ACTIVE` boundary | Current GitHub PR |
| Production PR #3 | Repository event; GitHub ID verified | Draft, open, 5 commits, focused contract tests reported `3/3`, full build/typecheck pending in checkout; not production-integrated | Current production GitHub PR |
| Production run `31311314980` | Validation event; run ID verified | `Success` on production `main` at `d64bde3`; CI warnings present; not clinical/accessibility/release proof | Current GitHub Actions |

## Roadmap coverage correction

The strict entity-to-Project audit is recorded in [`PHASE-1-ROADMAP-COVERAGE.md`](PHASE-1-ROADMAP-COVERAGE.md). It reviewed 26 significant Phase 1 entities and assigned each exactly one disposition. The live Project remains a single surface and now has 14 items, 13 named views, and 5 enabled workflows.

The audit found no missing active, approved-future, validation/gate, or infrastructure/governance work item that could be created without inventing authority, state, priority, risk, owner, or gate data. It did find one materially useful historical milestone absent from the Historical Milestones view: the merged PR #1 project-control documentation foundation. Issue #34 was created from verified PR evidence, auto-added once by the existing Project workflow, and set to `COMPLETE`, `Documentation / Governance`, `Milestone`, and `Historical`; the issue is now closed by the existing `COMPLETE -> close issue` workflow.

Existing item field corrections made in the live Project were deliberately limited to evidence-supported view/state representation:

- #26: `DEFERRED`, `AI / Development Infrastructure`, `Later`.
- #27: `APPROVED`, `Documentation / Governance`, `Near-Term`.
- #28: `COMPLETE`, `AI / Development Infrastructure`, `Historical`.
- #32: `APPROVED`, `QA / Release`, `Near-Term`.

Priority, risk tier, owner, target date, release/version, clinical gate, architecture gate, and QA gate values were not inferred or populated. C-001 and C-002 are resolved documentation-only/non-card dispositions. No Project item was required because the authoritative activation decision and the current-vs-historical repository status were corrected in durable records; creating a separate card would duplicate documentation reconciliation rather than represent authorized project work.

## Important normalized decisions and requirements

### Authority separation

The six chats consistently preserve these domain boundaries: MASTER controls project priority/sequence/state/release/closure; Planning controls architecture; Clinical controls clinical truth; QA controls independent validation when required; GitHub/Documentation controls repository and provenance facts; ROADMAP represents the Project surface. A chat claim cannot overwrite another domain.

### Clinical authority

The Clinical chat's bounded AIH-001 review is a source/authority-boundary review. It records that the harness may inspect whether an authorized clinical disposition exists but may not create clinical truth, approve evidence, or satisfy a clinical gate by AI synthesis. This does not validate any medical rule, equation, treatment, device behavior, or physiology model.

### AIH-004 architecture and QA corrections

Planning and QA records establish the following bounded contracts: proposals are not authority; non-authoritative values cannot populate authoritative V0 fields; authority-source claims require deterministic validation; AIH-002 evidence state and collection completeness remain distinct; and the assembler cannot create clinical truth. The implementation merged in PR #30 is repository evidence, while the reported `56/56`, `164/164`, and `9/9` results remain preserved as implementation-owner/PR evidence, not independent QA evidence.

### Risk-based QA model

The resolved architecture decision says Tier 2 gates are contract-triggered rather than universally required merely from the risk tier. This target model must not be treated as current executable truth without reconciling the adoption record, issue #32, and the actual machine-readable configuration. Tier 3 mandatory independent clinical/safety validation remains fail-closed.

## Significant chronology

| Approximate order | Event | Current evidence / disposition |
|---|---|---|
| Earlier project-control foundation | Initial project-control branch/PR #1 and production validation PRs were created and merged in prior history | Historical; original status wording is preserved in repository history, while current records are corrected |
| AIH-001 / AIH-002 | Deterministic V0 and read-only evidence foundations were implemented and closed | Current Project #14/#19 and current repository artifacts |
| AIH-003 | Pilot-specification work underwent bounded QA corrections, then was explicitly deferred | Current issue #26; no pilot execution inferred |
| AIH-004 | Architecture, QA/GitHub supporting reviews, implementation, stacked governance migration, conflict recovery, and merge were recorded | Current issue #28, PR #30, and main `e97a83b`; QA deviation is not QA PASS |
| Project-control status reconciliation | PR #1 foundation was verified as historical/merged; PR #30 merged at `e97a83b`; the later explicit MASTER activation decision was recorded at `2026-08-11T12:56:49Z`; Phase 1 corrections remain in draft/open PR #33 | Current GitHub evidence; C-001 and C-002 resolved in this bounded pass |
| Three.js planning | PR #29 merged documentation-only renderer planning; production PR #3 remains draft | Current project-control and production GitHub |
| QA model | Issue #32 is approved for contract migration; implementation/configuration edits remain unauthorized by that issue | Current issue #32 and corrected Project item |

## Conflict register

### C-001 - Autonomy activation versus adoption-record state

- **Conflict ID:** `C-001`.
- **Original:** PR #30 contained an explicit MASTER PROJECT CONTROL activation comment while the adoption record stated `NOT YET ACTIVE`.
- **Disposition:** **RESOLVED** on `2026-08-11`.
- **Root cause:** the adoption record was committed at `17798cc8c6b6cc97da3bd66752b261c683c9f281` at `2026-08-11T08:38:31-04:00`, before PR #30 merged at `2026-08-11T08:50:57-04:00`; the owner-authored activation decision was recorded later as a distinct authority event.
- **Authoritative current state:** `RTSL-KERNEL-AUTONOMY-001` is **ACTIVE**, effective `2026-08-11T12:56:49Z` (`8:56 AM EDT`), by the explicit `MASTER PROJECT CONTROL ACTIVATION DECISION` in PR #30 comment [`#issuecomment-5253465946`](https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/30#issuecomment-5253465946), against verified merged `main` `e97a83b984f96d51dc7c3a29789eee2be7e52a9f`.
- **Historical preserved:** the adoption record, independent-QA handoff, and temporary-QA-deviation record retain their pre-activation `NOT YET ACTIVE` state and are labeled as historical; no source wording was deleted.
- **Evidence:** PR #30 merge chronology and the exact owner-authored comment; adoption-record commit history; corrected durable governance records.
- **Files corrected:** `docs/governance/RTSL-KERNEL-AUTONOMY-001-ADOPTION-RECORD.md`, `docs/governance/RTSL-KERNEL-AUTONOMY-001-INDEPENDENT-QA-HANDOFF.md`, `docs/governance/RTSL-KERNEL-AUTONOMY-001-TEMPORARY-QA-DEVIATION.md`, `docs/governance/RTSL-KERNEL-AUTONOMY-001-CONFLICT-MIGRATION-REGISTER.md`, `docs/AI_DEVELOPMENT_WORKFLOW.md`, and the Phase 1 records listed in the checkpoint.
- **Project items corrected:** **NONE**. C-001 did not warrant a separate Project card.
- **Remaining limitation:** the decision is not a QA PASS, clinical validation, release, project closure, or waiver of Tier 3 independent validation/no-gate-downgrade controls.

### C-002 - Historical repository status text versus live repository state

- **Conflict ID:** `C-002`.
- **Original:** current-status documents described PR #1 and `setup/project-control-foundation` as the active/open foundation boundary after that foundation had been superseded by merged history.
- **Disposition:** **RESOLVED** on `2026-08-11`.
- **Root cause:** current navigational prose was not updated after the PR #1 foundation merged and later project-control work advanced through PR #30; historical chronology and current status were not explicitly separated.
- **Authoritative current state:** project-control `main` is `e97a83b984f96d51dc7c3a29789eee2be7e52a9f` after merged PR #30; PR #1 is a historical merged foundation milestone represented by issue #34; PR #33 is the current draft/open Phase 1 documentation branch and is not merged.
- **Historical preserved:** the PR #1 branch/PR creation and merge history, issue #34 milestone, and historical development record remain intact.
- **Evidence:** verified current `main`, live PR #30 merge, live PR #33 draft/open state, issue #34, and the corrected current-status documents.
- **Files corrected:** `README.md`, `docs/PROJECT_STATUS.md`, `docs/MASTER_PROJECT_QUEUE.md`, `docs/ROADMAP.md`, `docs/ARCHITECTURE_DECISIONS.md`, and the current merge/execution boundary in `docs/DEVELOPMENT_HISTORY.md`.
- **Project items corrected:** **NONE**. C-002 was a documentation-state correction and did not warrant a new roadmap item.
- **Remaining limitation:** PR #33 remains a draft/open branch checkpoint until separately reviewed and authorized; this correction does not establish global project reconciliation or Phase 2/3 coverage.

### C-003 - Chat/project state lag for corrected roadmap items

- **Classification:** roadmap-state normalization; resolved in the existing Project.
- **Claims:** issues #26, #27, #28, and #32 each contain explicit current dispositions that differed from their auto-added Project `PROPOSED` value.
- **Correction:** Project statuses were updated to `DEFERRED`, `APPROVED`, `COMPLETE`, and `APPROVED` respectively.
- **Correction:** the same four items also received evidence-supported workstream/planning-horizon values so deferred, governance, historical, and QA work appears in the appropriate existing views.
- **Disposition:** resolved and rechecked; no duplicate normalization item was created.

### C-004 - Chat implementation/test claims versus independent validation

- **Classification:** validation authority boundary.
- **Claims:** assigned chats and PR #30 report implementation-owner test results; no independent implementation QA PASS is claimed, and the temporary deviation is explicitly not a QA PASS.
- **Disposition:** no conflict after normalization; implementation evidence remains implementation evidence, not QA or clinical validation.

## Future, deferred, and non-goal records

- **Committed/approved:** #9 architecture/model contract, #10 clinical-validation framework, #11 accessibility baseline, #32 QA contract migration, and the already-merged documentation/planning package in PR #29.
- **Deferred:** #12 production branch/release control and #26 AIH-003 pilot specification.
- **Blocked:** #8 Sites-to-Git correspondence until authoritative deployed-commit metadata exists.
- **Not authorized:** production Three.js integration from PR #3, AIH-003 pilot fixture/golden/corpus work, unapproved AIH-004 policy/configuration edits, and any new clinical behavior.
- **Not established:** global future roadmap, complete project-wide chronology, or a release plan for all subsystems.

## Provenance links

- Project: `https://github.com/users/R3C4LL4L1F3/projects/1`
- Project-control repository: `https://github.com/R3C4LL4L1F3/RT-study-lab-project`
- Production repository: `https://github.com/R3C4LL4L1F3/RT-study-lab`
- Historical milestone issue #34: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/issues/34`
- Phase 1 coverage PR #33: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/33`
- PR #29: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/29`
- PR #30: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/30`
- PR #30 activation decision: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/30#issuecomment-5253465946`
- PR #31: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/31`
- Production PR #3: `https://github.com/R3C4LL4L1F3/RT-study-lab/pull/3`
- Production run: `https://github.com/R3C4LL4L1F3/RT-study-lab/actions/runs/31311314980`
