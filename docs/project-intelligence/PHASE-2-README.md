# RT Study Lab - Project Intelligence / Codex Context Bridge - Phase 2

```text
PHASE COVERAGE: 2 OF 3
PROJECT CHAT COVERAGE: PARTIAL
GLOBAL RECONCILIATION: NOT COMPLETE
GLOBAL AUDIT: NOT COMPLETE
CODEX-READY GLOBAL BASELINE: NOT ESTABLISHED
```

This is the durable index for the bounded Phase 2 project-intelligence pass and its later post-checkpoint roadmap amendment. It processes only the six assigned project chats listed below. It does not establish a global project baseline, ingest Phase 3 chats, redesign the site, change clinical behavior, or replace the authority model.

## Read order

1. [`PHASE-2-CURRENT-STATE.md`](PHASE-2-CURRENT-STATE.md) - report-time repository, production, Project, and evidence snapshot.
2. [`PHASE-2-SUBSYSTEM-RECORDS.md`](PHASE-2-SUBSYSTEM-RECORDS.md) - normalized histories for the six assigned chats.
3. [`PHASE-2-RECONCILIATION.md`](PHASE-2-RECONCILIATION.md) - collection, normalization, repository reconciliation, conflicts, and dependencies.
4. [`PHASE-2-ROADMAP-COVERAGE.md`](PHASE-2-ROADMAP-COVERAGE.md) - significant-entity matrix, canonical Project representation, and membership audit.
5. [`PHASE-2-MANIFEST.yml`](PHASE-2-MANIFEST.yml) - machine-readable phase manifest.
6. [`PHASE-2-CHECKPOINT.md`](PHASE-2-CHECKPOINT.md) - bounded checkpoint, disposition, limitations, and next-batch boundary.
7. [`PHASE-2-POST-CHECKPOINT-AMENDMENT.md`](PHASE-2-POST-CHECKPOINT-AMENDMENT.md) - user-directed current Project membership/status amendment after the bounded checkpoint.
8. Phase 1 records in this directory, especially [`PHASE-1-CHECKPOINT.md`](PHASE-1-CHECKPOINT.md), remain the authority for the separately bounded Phase 1 scope.

## Assigned chats only

| Chat | Record ID | Collection result |
|---|---|---|
| SITE CHAT (RT_study) | `019f720f-15ca-70c2-bd2f-9b72510e2844` | 7 pages / 62 turns |
| Ventilator Waveform Chat | `019f8976-212b-7f93-ba5f-f4530a8c688d` | 1 page / 2 turns |
| ECG & ACLS Lab Subsystems | `6a786482-1e5c-83ea-a27a-0e122b120fb8` | 1 page / 3 turns |
| Interactive Models & Simulation Lab | `019fe35c-e3d2-73e0-9310-d790e0f50376` | 10 pages / 95 turns |
| 3D Modeling Chat | `019fe258-ff0d-7852-9ee4-01753e743d47` | 2 pages / 12 turns |
| 3D Model Implementation Workflow | `6a5ca154-aacc-83ea-9b5f-82fee60f3bff` | 13 pages / 128 turns |

The synchronized local `sources/` directory was not treated as evidence. Repository, issue, Project, PR, and current production-source claims are separately labeled in the Phase 2 records.

## Authority and evidence boundary

Phase 1 authority boundaries remain in force. MASTER PROJECT CONTROL owns project-level priority, sequencing, routing, states, gates, blockers, and closure. Clinical truth remains with authoritative evidence and Clinical Validation & Sources. Architecture and contracts remain with the architecture owner and approved specifications. QA and release claims remain independent. GitHub repository and Project state are verified at report time, not inferred from chat agreement.

```text
AI agreement != clinical evidence
green CI != clinical validation
merge != QA PASS, release, or project closure
repository presence != authority for every domain
```

Phase 2 is canonical only for the processed Phase 1 plus Phase 2 bounded scope once its checkpoint is accepted. It is not canonical for the entire RT Study Lab project.
