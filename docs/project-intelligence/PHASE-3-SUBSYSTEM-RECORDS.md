# Phase 3 Normalized Subsystem and Capability Records

This record preserves the useful project intelligence from the six assigned Phase 3 chats without copying their transcripts. Repeated references across chats are consolidated into one entity with multiple provenance sources.

## Tools Chat

### Tooling capability catalog - documentation-only reference

The chat contains a broad capability catalog covering bundled ChatGPT/Codex use, GitHub/project records, local deterministic execution, browser/manual validation tools, specialized 3D tooling, automation possibilities, rejected paid/API approaches, and watch-list capabilities. Individual tools and exploratory comparisons are not separate Project items. The catalog remains useful context for Codex, but it has no independent state, owner, gate, or lifecycle that requires a card.

### `RTSL-AGENT-EXP-001` - workflow-agent feasibility

The final feasibility report supports a useful zero-incremental-cost Workflow Agent V0 as a human-triggered advisory/coordinating surface using existing ChatGPT Plus/Codex capabilities, GitHub/project records, bounded tools, and deterministic harness enforcement. It does not support a continuously running custom autonomous service. Discovery is complete; architecture and implementation are not authorized. The canonical Project representation is new row #24 / Issue #44, marked `COMPLETE`, `AI / Development Infrastructure`, `Milestone`, and `Historical`.

### `RTSL-AGENT-COST-001` / `AIH-COST-001` - hard cost constraint

Phase 1/V0 must incur $0 incremental AI-service expenditure beyond the existing ChatGPT Plus subscription. Paid API inference, paid agent hosting, paid vector databases, paid observability, and paid orchestration are prohibited by default. This is a binding requirement of the workflow-agent and harness initiatives, not a separate implementation project. It is represented through the workflow-agent milestone (Project row #24), the existing AI-harness rows #8 and #9, and the future slices #19-#23.

### AIH V0 tooling recommendation

The recommended V0 implementation direction is a plain deterministic Python core, with no agent framework required; a local Ollama adviser is an optional future V1 possibility. ChatGPT/Codex are advisory/development surfaces rather than runtime dependencies. LangGraph, n8n, paid APIs, hosted agents, and unrestricted RAG are not V0 requirements. The decision is represented through the existing AIH-001/AIH-002 records and the future AIH-005 through AIH-009 Project items.

### `AIH-GH-RO-001` - read-only GitHub boundary

The GitHub evidence boundary is GET-only, allowlisted, fail-closed, and technically enforced rather than prompt-only. Positive evidence states remain distinct from `MISSING`, `STALE`, `UNVERIFIED`, and `CONTRADICTORY`. This requirement is represented through the existing AIH-001 and AIH-002 Project items; no duplicate read-only card is warranted.

## AI Harness Integration

The canonical lineage is:

```text
RTSL-AIH-001 deterministic V0 governance foundation
→ RTSL-AIH-002 read-only GitHub evidence
→ RTSL-AIH-004 task/context assembly
→ future RTSL-AIH-005 unified command
→ future RTSL-AIH-006 MASTER integration
→ deferred RTSL-AIH-003 operational pilot
→ future RTSL-AIH-007 advisory interpretation and RTSL-AIH-008 context compiler
→ future RTSL-AIH-009 implementation work packages
```

Current repository evidence confirms that AIH-004 was initially blocked by unavailable normative artifacts, then resumed after the v1.1 specification and fixtures became available. PR #30 merged the bounded implementation. The initial blocker is historical; it is not a current blocker on Issue #28.

The future AIH-005 through AIH-009 records remain `PROPOSED` and `Later`. Their issue bodies record dependencies, acceptance boundaries, and explicit non-goals. Project rows #19-#23 are standalone because each has an independently manageable capability, dependency, and future lifecycle.

## Agent-workflow chronology

Explore Agent Workflow introduced the workflow-agent question and the `RTSL-AGENT-EXP-001` discovery handoff. Tools Chat produced the feasibility and cost recommendation. Continue agent workflow exploration carried the AIH-004 and governance-migration implementation chronology, including a local-only QA migration attempt. The local branch is not remote/default-main evidence and was not promoted. AIH-004 remains represented by Issue #28 / Project row #12; the current live governance activation remains documented in the repository, while Issue #32 retains its own `APPROVED` work state.

These chats describe one workflow-agent initiative, not multiple competing agents. The agent remains subordinate to deterministic harness rules, MASTER authority, clinical authority, independent QA, and human approvals.

## `RTSL-QA-MODEL-001` and `RTSL-KERNEL-AUTONOMY-001`

Continue agent workflow exploration contains implementation-owner history for the risk-based QA migration and governance activation. Current GitHub evidence is stronger than the local branch claim: the governance migration activation is recorded as active in project-control main, but Issue #32's own current record remains `APPROVED` and says implementation/policy edits are not yet authorized by that issue. No Project status was silently promoted. The existing Project row #13 remains the canonical QA/gate representation.

## Design System & UI/UX

The chat establishes persistent ownership of shared visual language, interaction patterns, responsive behavior, accessibility requirements, visualization conventions, and educational UX. Decisions include educational clarity over decorative complexity, reusable patterns over one-off modules, 390px responsive acceptance, accessibility as an acceptance criterion, and immutable clinical behavior unless the feature owner changes the specification.

The current project-control queue already contains a separate deferred `Design-system durable record`. Existing Issue #11 is the accessibility-validation baseline, not the whole shared design-system architecture. Phase 3 therefore created one separate future Project item, row #25 / Issue #45, with no invented task ID, `DEFERRED`, P2, Tier 1, `Design System`, and `Later`. It does not authorize a production UI redesign.
