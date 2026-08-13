# RT Study Lab - Project Intelligence / Codex Context Bridge

> PHASE COVERAGE: 3 OF 3
> PROJECT CHAT COVERAGE: COMPLETE FOR THE THREE BOUNDED INGESTION BATCHES
> GLOBAL PROJECT RECONCILIATION: NOT COMPLETE
> CODEX-READY GLOBAL BASELINE: NOT ESTABLISHED

This directory contains the bounded Phase 1, Phase 2, and Phase 3 navigation and reconciliation layers for the RT Study Lab project. Each phase retains its own coverage boundary; Phase 2 and Phase 3 are separate additive checkpoints. Together they make the processed project-chat context usable by a future Codex session with GitHub access while preserving the existing project-control documents as the broader authority system.

It is not a transcript archive, a replacement governance system, a clinical evidence repository, or a claim that all RT Study Lab chats have been reconciled.

## Read order

1. [`PHASE-3-README.md`](PHASE-3-README.md) - Phase 3 scope, assigned chats, and representation model.
2. [`PHASE-3-CURRENT-STATE.md`](PHASE-3-CURRENT-STATE.md) - current live repository, Project, and Phase 3 field snapshot.
3. [`PHASE-3-SUBSYSTEM-RECORDS.md`](PHASE-3-SUBSYSTEM-RECORDS.md) - normalized tooling, AI-harness, agent-workflow, and design-system records.
4. [`PHASE-3-RECONCILIATION.md`](PHASE-3-RECONCILIATION.md) - collection, normalization, cross-phase reconciliation, conflicts, and dependencies.
5. [`PHASE-3-ROADMAP-COVERAGE.md`](PHASE-3-ROADMAP-COVERAGE.md) - three-level entity-to-Project coverage matrix and membership audit.
6. [`PHASE-3-MANIFEST.yml`](PHASE-3-MANIFEST.yml) - machine-readable Phase 3 manifest.
7. [`PHASE-3-CHECKPOINT.md`](PHASE-3-CHECKPOINT.md) - bounded Phase 3 checkpoint and global-status boundary.
8. [`PHASE-2-README.md`](PHASE-2-README.md) and its linked records - separately bounded Phase 2 checkpoint and amendment.
9. [`PHASE-1-CHECKPOINT.md`](PHASE-1-CHECKPOINT.md) and its linked records - separately bounded Phase 1 checkpoint.
10. [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`RECONCILIATION.md`](RECONCILIATION.md) - earlier canonical baseline/provenance records retained for historical continuity.
11. Existing canonical records linked from the repository root README, especially `docs/MASTER_PROJECT_QUEUE.md`, `docs/PROJECT_STATUS.md`, `docs/DEVELOPMENT_HISTORY.md`, `docs/VALIDATION_REGISTER.md`, and `docs/ARCHITECTURE_DECISIONS.md`.

Current-state records are authoritative for the verified live refs and explicit decisions. Older PR #1 and pre-activation adoption/handoff/deviation statements remain available as historical provenance only; the C-001/C-002 resolution details and exact evidence are in `RECONCILIATION.md`.

## Assigned chat collection

The Phase 1 assigned project chats were read from their accessible project records on 2026-08-11. The synchronized `sources/` directory was present but contained no files, so it was not treated as a source of evidence. Phase 2 and Phase 3 collection details are recorded in their respective phase indexes.

| Assigned chat | Chat record | Accessible collection | Authority preserved |
|---|---|---:|---|
| MASTER PROJECT CONTROL | `6a786390-94a4-83ea-b9ec-2fb410d9aee3` | 8 pages / 77 turns | priority, sequence, routing, dependencies, risk, state, blockers, release, closure, governance exceptions |
| (PLANNING_ARCHITECTURE) | `6a60717e-b014-83ea-9f4f-d09610a70707` | 25 pages / 247 turns | architecture, contracts, state models, reusable boundaries, ADRs |
| Clinical Validation & Sources | `6a7863d2-798c-83ea-ab01-788248c2451e` | 1 page / 4 turns | clinical evidence, clinical authority, source trace, clinical disposition |
| QA - Regression & Release | `6a786440-20c0-83ea-a52c-3dd6de11cf5e` | 6 pages / 54 turns | independent validation, regression, defects, retest, release validation |
| ROADMAP (GitHub) | `019fef59-e6a4-70d0-b39e-13548f35a9ff` | 1 page / 3 turns | roadmap representation, Project fields/views, work-state records |
| GitHub PR and Documentation | `6a784402-36e8-83ea-8444-341624a5a9c4` | 7 pages / 69 turns | repository, issue, branch, PR, commit, merge, CI, and documentation provenance |

Collection counts are an inspection snapshot, not permanent identifiers for future chat history. Each significant normalized record retains the chat title, record ID, approximate chronological location, entity, claim/event, evidence class, authority domain, confidence, and supersession note where applicable.

## Evidence vocabulary

- `VERIFIED REPOSITORY FACT` - observed directly in current GitHub or the fetched repository ref.
- `CHAT CLAIM` - preserved from an assigned chat; not current until independently confirmed.
- `DURABLE PROJECT-CONTROL RECORD` - current repository documentation or issue/PR record; authority still depends on domain and recency.
- `AUTHORITY DECISION` - explicit decision by the domain owner, preserved with its source.
- `SOURCE-GROUNDED` - supported by the Clinical Validation & Sources record or an authoritative source trace.
- `INFERRED` - not used to assign priority, owner, risk, gates, work state, release, or closure.
- `UNVERIFIED` - observed or claimed but not sufficiently confirmed.
- `CONTRADICTORY` - relevant current claims disagree; the checkpoint records the conflict and owner instead of choosing silently.

The following distinctions remain mandatory:

```text
AI agreement != clinical evidence
green CI != clinical validation
PR approval != QA PASS
merge != release or project closure
repository presence != authority for every domain
```

## Scope boundary

Each phase processes only its explicitly assigned chats. The Phase 3 batch processed only Tools Chat, AI Harness Integration, Explore Agent Workflow, Continue agent workflow exploration, Implement RTSL-AIH-004 intake, and Design System & UI/UX. The bridge does not recursively discover unassigned chats, redesign the website, change clinical behavior, change production code, rewrite governance, invent task IDs or dates, delete history, or establish a global baseline.

The current project-control repository remains the durable documentation home. Phase 1, Phase 2, and Phase 3 records are canonical only for their bounded processed scopes and checkpoints. Together they cover the processed three-batch chat scope, but they do not establish a global baseline for the entire project.
