# RT Study Lab - Project Intelligence / Codex Context Bridge

> PHASE COVERAGE: 1 OF 3
> PROJECT CHAT COVERAGE: PARTIAL
> GLOBAL PROJECT RECONCILIATION: NOT YET COMPLETE
> CODEX-READY GLOBAL BASELINE: NOT YET ESTABLISHED

This directory contains the bounded Phase 1 and Phase 2 navigation and reconciliation layers for the RT Study Lab project. The Phase 1 records retain their original Phase 1 coverage boundary; the Phase 2 records are a separate, additive checkpoint. Together they make the processed project-chat context usable by a future Codex session with GitHub access while preserving the existing project-control documents as the broader authority system.

It is not a transcript archive, a replacement governance system, a clinical evidence repository, or a claim that all RT Study Lab chats have been reconciled.

## Read order

1. [`CURRENT_STATE.md`](CURRENT_STATE.md) - current live repository, Project, roadmap, and validation snapshot.
2. [`RECONCILIATION.md`](RECONCILIATION.md) - normalized entities, provenance, chronology, claims, verified facts, and conflicts.
3. [`PHASE-1-ROADMAP-COVERAGE.md`](PHASE-1-ROADMAP-COVERAGE.md) - strict entity-to-Project coverage matrix and re-audit result.
4. [`PHASE-1-MANIFEST.yml`](PHASE-1-MANIFEST.yml) - machine-readable phase and coverage manifest.
5. [`PHASE-1-CHECKPOINT.md`](PHASE-1-CHECKPOINT.md) - audit result, coverage boundary, limitations, and next batch.
6. [`PHASE-2-README.md`](PHASE-2-README.md) - Phase 2 scope, exact coverage banner, and read order.
7. [`PHASE-2-CURRENT-STATE.md`](PHASE-2-CURRENT-STATE.md) - Phase 2 current-state snapshot and evidence boundaries.
8. [`PHASE-2-SUBSYSTEM-RECORDS.md`](PHASE-2-SUBSYSTEM-RECORDS.md) - six assigned subsystem histories and current disposition.
9. [`PHASE-2-RECONCILIATION.md`](PHASE-2-RECONCILIATION.md) - collection, normalization, repository reconciliation, conflicts, and dependencies.
10. [`PHASE-2-ROADMAP-COVERAGE.md`](PHASE-2-ROADMAP-COVERAGE.md) - Phase 2 entity-to-Project coverage matrix and membership audit.
11. [`PHASE-2-MANIFEST.yml`](PHASE-2-MANIFEST.yml) - machine-readable Phase 2 manifest.
12. [`PHASE-2-CHECKPOINT.md`](PHASE-2-CHECKPOINT.md) - bounded Phase 2 checkpoint and next-batch boundary.
13. Existing canonical records linked from the repository root README, especially `docs/MASTER_PROJECT_QUEUE.md`, `docs/PROJECT_STATUS.md`, `docs/DEVELOPMENT_HISTORY.md`, `docs/VALIDATION_REGISTER.md`, and `docs/ARCHITECTURE_DECISIONS.md`.

Current-state records are authoritative for the verified live refs and explicit decisions. Older PR #1 and pre-activation adoption/handoff/deviation statements remain available as historical provenance only; the C-001/C-002 resolution details and exact evidence are in `RECONCILIATION.md`.

## Assigned chat collection

The six assigned project chats were read from their accessible project records on 2026-08-11. The synchronized `sources/` directory was present but contained no files, so it was not treated as a source of evidence.

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

Phase 1 processes only the six chats above. It does not ingest other persistent chats, recursively discover unassigned chats, redesign the website, change clinical behavior, change production code, rewrite governance, invent task IDs or dates, delete history, or establish a global baseline.

The current project-control repository remains the durable documentation home. The Phase 1 records are canonical only for their bounded processed scope; the Phase 2 records are canonical only for the six-chat Phase 2 scope and its checkpoint. Neither phase establishes a global baseline for the entire project.
