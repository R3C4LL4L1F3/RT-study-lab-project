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
| RTSL-KERNEL-AUTONOMY-001 | Governance decision; ID verified from chat/PR #31/PR #30 | Migration merged and explicit activation comment exists, but the adoption record still says `NOT YET ACTIVE`; effective state is `CONTRADICTORY` pending owner reconciliation | MASTER authority claim plus GitHub durable records; conflict C-001 |
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
| Earlier project-control foundation | Initial project-control branch/PR #1 and production validation PRs were created and merged in prior history | Historical; older README/status lines still reference these states |
| AIH-001 / AIH-002 | Deterministic V0 and read-only evidence foundations were implemented and closed | Current Project #14/#19 and current repository artifacts |
| AIH-003 | Pilot-specification work underwent bounded QA corrections, then was explicitly deferred | Current issue #26; no pilot execution inferred |
| AIH-004 | Architecture, QA/GitHub supporting reviews, implementation, stacked governance migration, conflict recovery, and merge were recorded | Current issue #28, PR #30, and main `e97a83b`; QA deviation is not QA PASS |
| Three.js planning | PR #29 merged documentation-only renderer planning; production PR #3 remains draft | Current project-control and production GitHub |
| QA model | Issue #32 is approved for contract migration; implementation/configuration edits remain unauthorized by that issue | Current issue #32 and corrected Project item |

## Conflict register

### C-001 - Autonomy activation versus adoption-record state

- **Classification:** authority / repository-document conflict.
- **Claim A:** PR #30 contains an explicit MASTER PROJECT CONTROL activation comment for `RTSL-KERNEL-AUTONOMY-001` effective from `main = e97a83b`.
- **Claim B:** `docs/governance/RTSL-KERNEL-AUTONOMY-001-ADOPTION-RECORD.md` on the same current `main` says `Activation state: NOT YET ACTIVE` and the existing Kernel remains authoritative until a future activation condition.
- **Why unsafe to choose silently:** one is an explicit authority decision; the other is the durable canonical adoption record and activation boundary. Future automation must not treat the target policy as active while its governing record says otherwise.
- **Owner:** MASTER PROJECT CONTROL, with GitHub PR and Documentation preserving the corrected durable record.
- **Evidence needed:** an explicit update or supersession record in the adoption document and related current-status docs, or a durable reversal/clarification of the activation comment.
- **Phase 1 disposition:** unresolved and preserved; no policy or governance record was rewritten.

### C-002 - Historical repository status text versus live repository state

- **Classification:** historical supersession / documentation drift.
- **Claims:** current `main` is `e97a83b`, PR #30 is merged, and no project-control PR is open; older `README.md`, `PROJECT_STATUS.md`, `MASTER_PROJECT_QUEUE.md`, and related records still describe PR #1 as the active/open foundation boundary.
- **Why unsafe to choose silently:** these documents remain navigational and can misroute future work.
- **Owner:** GitHub PR and Documentation, routed through MASTER for any queue/state changes.
- **Evidence needed:** a bounded current-status documentation correction against the live `main` history, preserving the historical PR #1 record.
- **Phase 1 disposition:** unresolved; this bridge points to live evidence but does not rewrite the broader canonical documents.

### C-003 - Chat/project state lag for corrected roadmap items

- **Classification:** roadmap-state normalization; resolved in the existing Project.
- **Claims:** issues #26, #27, #28, and #32 each contain explicit current dispositions that differed from their auto-added Project `PROPOSED` value.
- **Correction:** Project statuses were updated to `DEFERRED`, `APPROVED`, `COMPLETE`, and `APPROVED` respectively.
- **Disposition:** resolved and rechecked; no new roadmap item was created.

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
- PR #29: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/29`
- PR #30: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/30`
- PR #31: `https://github.com/R3C4LL4L1F3/RT-study-lab-project/pull/31`
- Production PR #3: `https://github.com/R3C4LL4L1F3/RT-study-lab/pull/3`
- Production run: `https://github.com/R3C4LL4L1F3/RT-study-lab/actions/runs/31311314980`
