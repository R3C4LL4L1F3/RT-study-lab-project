# Phase 2 Roadmap Coverage and Project Membership Audit

```text
PHASE COVERAGE: 2 OF 3
PROJECT CHAT COVERAGE: PARTIAL
GLOBAL RECONCILIATION: NOT COMPLETE
GLOBAL AUDIT: NOT COMPLETE
CODEX-READY GLOBAL BASELINE: NOT ESTABLISHED
```

## Audit rule

Each normalized significant entity was classified once as roadmap-worthy or documentation-only. Roadmap-worthy entities were mapped to one canonical Project representation. Existing items were retained where they already owned the decision, validation, gate, blocker, or parent relationship. New items were created only for the three evidenced historical milestones. A PR, chat, model version, or view was not made into a duplicate roadmap item merely because it appeared in more than one source.

This matrix is the report-time Phase 2 checkpoint audit at 17 Project items. The later explicit user-directed re-addition of production PR #3 as Project item #18, IN PROGRESS under Interactive Models, is recorded in [`PHASE-2-POST-CHECKPOINT-AMENDMENT.md`](PHASE-2-POST-CHECKPOINT-AMENDMENT.md) and supersedes the live Project membership statement for the post-checkpoint state without rewriting this historical audit.

## Significant-entity matrix

| # | Normalized entity | Source chat / entity type | State; priority / risk | Owner | Roadmap-worthy? | Existing issue / final Project item | Membership and disposition |
|---:|---|---|---|---|:---:|---|---|
| 1 | `P2-SITE-MIL-001` Shock learning module and visual-teaching release | SITE; historical milestone | Source implementation complete; priority/risk not assigned | SITE CHAT (RT_study) | YES | New #35 | Member verified. COMPLETE; Site / Platform; Milestone; Historical. |
| 2 | `P2-3D-MIL-001` Chest Trauma 3D pilot and licensed asset integration | SITE + 3D; historical milestone | Source integration complete; manual/runtime QA remains open; priority/risk not assigned | 3D Modeling Chat | YES | New #36 | Member verified. COMPLETE; 3D; Milestone; Historical. |
| 3 | `P2-VENT-MIL-001` Ventilator Session 3.5 stabilization lineage | Ventilator; historical milestone | Source implementation complete; validation remains open; priority/risk not assigned | Ventilator Waveform Chat | YES | New #37 | Member verified. COMPLETE; Ventilator; Milestone; Historical. |
| 4 | `P2-SITE-GATE-001` Sites deployment-to-Git correspondence | SITE; blocker / gate | BLOCKED; P2 / Tier 1 | GitHub PR and Documentation / MASTER routing | YES | #8 | Existing member verified; retained BLOCKED. |
| 5 | `P2-IM-FUT-001` Shock / oxygen numerical-lab future boundary | SITE + Interactive; future architecture dependency | Proposed, not authorized; P1 / Tier 3 boundary inherited from #9 | Interactive Models & Simulation Lab | YES | #9 | Represented by canonical #9; no separate future item. |
| 6 | `P2-SITE-HIST-001` Prior private Sites versions and deployment reports | SITE; historical deployment evidence | Chat claim; live SHA unknown | SITE CHAT (RT_study) | NO | None | Documentation-only under #8 boundary; no live deployment claim. |
| 7 | `P2-SITE-HIST-002` ECG teaching-page implementation history | SITE; historical feature lineage | Historical source context | SITE CHAT (RT_study) | NO | None | Documentation-only; no duplicate ECG item. |
| 8 | `P2-SITE-HIST-003` Ventilator UI redesign history | SITE; historical feature lineage | Historical source context | SITE CHAT (RT_study) | NO | #3 context | Documentation-only under existing Ventilator validation record. |
| 9 | `P2-VENT-CAP-001` Ventilator engine and Session 3.5 capability lineage | Ventilator; subsystem capability | Source-present; current validation not closed; P1 / Tier 3 parent boundary | Ventilator Waveform Chat | YES | #37 + #3 | Represented by milestone #37 and validation #3; no third implementation item. |
| 10 | `P2-VENT-VAL-001` Latest Ventilator P1 correctness concerns | Ventilator; validation / follow-up | IN VALIDATION; P1 / Tier 3 | QA - Regression & Release with Ventilator owner | YES | #3 | Existing member verified; retained IN VALIDATION; current retest required. |
| 11 | `P2-VENT-VAL-002` Browser/manual residuals and event-state concerns | Ventilator; validation gate | IN VALIDATION; P1 / Tier 3 | QA - Regression & Release | YES | #3 | Existing member verified; no separate defect item. |
| 12 | `P2-VENT-FUT-001` Graphical redesign / authoritative board-review readiness | Ventilator; future proposal | Not approved; priority/risk not assigned | Ventilator Waveform Chat | NO | None | Future discussion only; not a Project item. |
| 13 | `P2-ECG-OWNER-001` ECG/ACLS ownership and Tier 3 subsystem boundary | ECG; ownership record | Current routing record; not a defect or validation result | ECG & ACLS Lab Subsystems | NO | #10 context | Documentation-only; ownership does not itself create roadmap work. |
| 14 | `P2-ECG-CAP-001` ECG/ACLS implementation and test lineage | ECG + SITE; source/history | Source-present; clinical result not claimed | ECG & ACLS Lab Subsystems | NO | #10 context | Documentation-only until independent validation establishes a disposition. |
| 15 | `P2-ECG-VAL-001` ECG/ACLS independent clinical-validation sequence | ECG; validation gate | APPROVED; P2 / Tier 3 | Clinical Validation & Sources / QA | YES | #10 | Existing member verified; retained APPROVED. |
| 16 | `P2-ECG-FUT-001` Learn / Practice / Clinical Practice / Examination expansion | ECG; future scope | Future, unapproved; priority/risk not assigned | ECG & ACLS Lab Subsystems | NO | None | Documentation-only future scope; no item invented. |
| 17 | `P2-IM-ARCH-001` Interactive Models architecture/model contract | Interactive; architecture initiative | APPROVED for specification; implementation not approved; P1 / Tier 3 | Interactive Models & Simulation Lab | YES | #9 | Existing member verified; retained APPROVED. |
| 18 | `P2-IM-RENDER-001` Oxygen transport renderer PR #3 / Batches 1-6 | Interactive; implementation dependency | Draft/open, unmerged; gate-dependent; P1 / Tier 3 parent | Interactive Models & Simulation Lab | YES | #9; production PR #3 | Represented by #9. PR #3 intentionally not a separate Project member. |
| 19 | `P2-IM-QA-001` Renderer visual anatomy and independent-QA gate | Interactive; QA / validation gate | Independent QA not approved; P1 / Tier 3 parent | QA - Regression & Release | YES | #9 | Represented by #9 architecture and validation gates; no PASS claim. |
| 20 | `P2-IM-HIST-001` Standalone 2.5D and HTML physiology prototypes | Interactive; historical prototype | Historical / superseded context | Interactive Models & Simulation Lab | NO | None | Documentation-only; outside production `main`. |
| 21 | `P2-3D-CAP-001` Chest Trauma 3D production integration | 3D + SITE; subsystem capability | Source-integrated; manual/runtime QA open; P2 / Tier 2 under #5 | 3D Modeling Chat | YES | #36 + #5 | Represented by milestone #36 and validation #5. |
| 22 | `P2-3D-ASSET-001` BodyParts3D thorax v1 provenance | 3D; asset provenance | Source/attribution evidence; clinical/mechanical claims not made | 3D Modeling Chat | NO | #36 context | Documentation-only under #36; no item per derivative. |
| 23 | `P2-3D-ASSET-002` Respiratory v2 provenance and alignment correction | 3D; asset provenance | Source/attribution evidence; QA remains under #5 | 3D Modeling Chat | NO | #36 / #5 context | Documentation-only; local package hash is not a production commit claim. |
| 24 | `P2-3D-VAL-001` 3D runtime, mechanical, visual, and browser QA | 3D; validation gate | IN VALIDATION; P2 / Tier 2 | QA - Regression & Release / 3D Modeling | YES | #5 | Existing member verified; retained IN VALIDATION. |
| 25 | `P2-3D-HIST-001` Shiley model and animation workflow lineage | 3D; historical workflow | Historical, not production-integrated | 3D Modeling Chat | NO | None | Documentation-only; no production-ready claim. |
| 26 | `P2-3D-WF-001` Deterministic 3D implementation workflow conventions | 3D workflow; governance/documentation | Historical workflow; Blender runtime validation incomplete | 3D Model Implementation Workflow | NO | None | Documentation-only; routed to existing owner boundaries. |
| 27 | `P2-CROSS-ACC-001` Accessibility validation baseline | SITE + Ventilator + Interactive; validation framework | APPROVED; P2 / Tier 1 | Design System / QA | YES | #11 | Existing member verified; retained APPROVED. |

## Final Project field audit for new items

| Item | Status | Workstream / Project Area | Initiative Type | Roadmap Level | Planning Horizon | Other fields |
|---|---|---|---|---|---|---|
| #35 Shock milestone | COMPLETE | Site / Platform | Unassigned - no Milestone option exists | Milestone | Historical | Priority, risk, owner, release, clinical, architecture, QA, block, resume, and target fields left blank where not evidenced. |
| #36 Chest Trauma 3D milestone | COMPLETE | 3D | Unassigned - no Milestone option exists | Milestone | Historical | Same conservative blank-field rule. |
| #37 Ventilator Session 3.5 milestone | COMPLETE | Ventilator | Unassigned - no Milestone option exists | Milestone | Historical | Same conservative blank-field rule. |

## Membership audit result

- Significant entities reviewed: **27**.
- Roadmap-worthy entities: **15**.
- Documentation-only / historical / future-not-authorized entities: **12**.
- Canonical Project representations used: **#3, #5, #8, #9, #10, #11, #35, #36, #37**.
- Roadmap-worthy entity membership: **15/15 represented and verified** through those canonical items.
- New Project items: **3** (#35, #36, #37).
- Existing Project items added to the Project: **0**.
- Existing Project items updated: **0**.
- Duplicate item per view: **none observed**.
- Project count after Phase 2: **17**; named views **13**; enabled workflows **5**.
- Membership blockers: **none for the roadmap-worthy entities**. The unresolved dependencies listed in the reconciliation record remain gates/evidence dependencies, not membership failures.
