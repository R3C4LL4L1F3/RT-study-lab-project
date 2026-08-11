from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any

from .errors import SchemaError, UnknownKernelError


class Priority(str, Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"


class RiskTier(str, Enum):
    TIER_0 = "TIER_0"
    TIER_1 = "TIER_1"
    TIER_2 = "TIER_2"
    TIER_3 = "TIER_3"


class WorkState(str, Enum):
    PROPOSED = "PROPOSED"
    APPROVED = "APPROVED"
    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    IN_VALIDATION = "IN_VALIDATION"
    READY_FOR_RELEASE = "READY_FOR_RELEASE"
    COMPLETE = "COMPLETE"
    PAUSED = "PAUSED"
    BLOCKED = "BLOCKED"
    DEFERRED = "DEFERRED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"


class ActorType(str, Enum):
    HUMAN = "HUMAN"
    VERIFIED_TOOL = "VERIFIED_TOOL"
    AI_ADVISORY = "AI_ADVISORY"
    VERIFIED_GOVERNED_SYSTEM = "VERIFIED_GOVERNED_SYSTEM"


class GateState(str, Enum):
    NOT_REQUIRED = "NOT_REQUIRED"
    REQUIRED_PENDING = "REQUIRED_PENDING"
    IN_REVIEW = "IN_REVIEW"
    PASS = "PASS"
    FAIL = "FAIL"
    BLOCKED = "BLOCKED"


CANONICAL_GATES = {
    "CLINICAL_EVIDENCE", "ARCHITECTURE", "IMPLEMENTATION",
    "INDEPENDENT_REVIEW", "QA", "GITHUB_PROVENANCE", "RELEASE",
}

FINDING_TYPES = {
    "VALIDATION_GAP", "CONFIRMED_DEFECT", "OBSERVATION", "UNRESOLVED",
}

REQUIRED_TASK_FIELDS = {
    "task_id", "title", "priority", "risk_tier", "work_state", "routing",
    "gates", "approvals", "findings", "kernel",
}


@dataclass(frozen=True)
class Config:
    roles: dict[str, Any]
    gates: dict[str, Any]
    transitions: dict[str, Any]
    kernel_profile: dict[str, Any]
    autonomy: dict[str, Any]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SchemaError(f"cannot load JSON {path}: {exc}") from exc


def load_config(repo_root: Path) -> Config:
    base = repo_root / "config" / "ai_harness"
    return Config(
        roles=load_json(base / "roles.v1.json"),
        gates=load_json(base / "gates.v1.json"),
        transitions=load_json(base / "transition-matrix.v1.json"),
        kernel_profile=load_json(base / "kernel-profile.v1.json"),
        autonomy=load_json(base / "autonomy.v1.json"),
    )


def _require_mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaError(f"{field} must be an object")
    return value


def _require_list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise SchemaError(f"{field} must be an array")
    return value


def validate_actor(actor: Any, field: str = "actor") -> dict[str, Any]:
    actor = _require_mapping(actor, field)
    actor_id = actor.get("actor_id")
    if not isinstance(actor_id, str) or not actor_id.strip():
        raise SchemaError(f"{field}.actor_id is required")
    try:
        ActorType(actor.get("actor_type"))
    except ValueError as exc:
        raise SchemaError(f"{field}.actor_type is invalid") from exc
    role = actor.get("authority_role")
    if role is not None and not isinstance(role, str):
        raise SchemaError(f"{field}.authority_role must be a string or null")
    return actor


def validate_gate(gate: Any, index: int) -> dict[str, Any]:
    field = f"gates[{index}]"
    gate = _require_mapping(gate, field)
    if gate.get("gate_id") not in CANONICAL_GATES:
        raise SchemaError(f"{field}.gate_id is invalid")
    obligation = _require_mapping(gate.get("obligation"), f"{field}.obligation")
    if not isinstance(obligation.get("required"), bool):
        raise SchemaError(f"{field}.obligation.required must be boolean")
    execution = _require_mapping(gate.get("execution"), f"{field}.execution")
    try:
        GateState(execution.get("state"))
    except ValueError as exc:
        raise SchemaError(f"{field}.execution.state is invalid") from exc
    if gate.get("authority") is not None:
        _require_mapping(gate["authority"], f"{field}.authority")
    disposition = gate.get("disposition")
    if disposition is not None:
        disposition = _require_mapping(disposition, f"{field}.disposition")
        if disposition.get("actor") is not None:
            validate_actor(disposition["actor"], f"{field}.disposition.actor")
        _require_list(disposition.get("evidence_refs", []), f"{field}.disposition.evidence_refs")
    return gate


def validate_approval(approval: Any, index: int) -> dict[str, Any]:
    field = f"approvals[{index}]"
    approval = _require_mapping(approval, field)
    for name in ("approval_id", "approval_type", "decision"):
        if not isinstance(approval.get(name), str) or not approval[name]:
            raise SchemaError(f"{field}.{name} is required")
    validate_actor(approval.get("actor"), f"{field}.actor")
    if approval.get("timestamp") is not None and not isinstance(approval.get("timestamp"), str):
        raise SchemaError(f"{field}.timestamp must be string")
    return approval


def validate_finding(finding: Any, index: int) -> dict[str, Any]:
    field = f"findings[{index}]"
    finding = _require_mapping(finding, field)
    if not isinstance(finding.get("finding_id"), str) or not finding["finding_id"]:
        raise SchemaError(f"{field}.finding_id is required")
    if finding.get("type") not in FINDING_TYPES:
        raise SchemaError(f"{field}.type is invalid")
    evidence = finding.get("evidence")
    if evidence is not None:
        evidence = _require_mapping(evidence, f"{field}.evidence")
        _require_list(evidence.get("evidence_refs", []), f"{field}.evidence.evidence_refs")
        if evidence.get("produced_by") is not None:
            validate_actor(evidence["produced_by"], f"{field}.evidence.produced_by")
    classification = finding.get("classification")
    if classification is not None:
        classification = _require_mapping(classification, f"{field}.classification")
        if classification.get("classified_by") is not None:
            validate_actor(classification["classified_by"], f"{field}.classification.classified_by")
    return finding


def validate_task(raw: Any, config: Config) -> dict[str, Any]:
    task = _require_mapping(raw, "task")
    missing = sorted(REQUIRED_TASK_FIELDS.difference(task))
    if missing:
        raise SchemaError(f"missing required fields: {', '.join(missing)}")
    if not isinstance(task["task_id"], str) or not task["task_id"].strip():
        raise SchemaError("task_id is required")
    if not isinstance(task["title"], str) or not task["title"].strip():
        raise SchemaError("title is required")
    try:
        Priority(task["priority"])
    except ValueError as exc:
        raise SchemaError("priority is invalid") from exc
    try:
        RiskTier(task["risk_tier"])
    except ValueError as exc:
        raise SchemaError("risk_tier is invalid") from exc
    try:
        WorkState(task["work_state"])
    except ValueError as exc:
        raise SchemaError("work_state is invalid") from exc

    routing = _require_mapping(task["routing"], "routing")
    for name in ("coordinating_owner", "primary_owner"):
        if routing.get(name) not in config.roles["roles"]:
            raise SchemaError(f"routing.{name} is not a canonical role")
    supporting = _require_list(routing.get("supporting_owners", []), "routing.supporting_owners")
    unknown_support = [r for r in supporting if r not in config.roles["roles"]]
    if unknown_support:
        raise SchemaError(f"unknown supporting owner(s): {unknown_support}")

    gate_ids = set()
    for idx, gate in enumerate(_require_list(task["gates"], "gates")):
        validate_gate(gate, idx)
        authority = gate.get("authority") or {}
        owner_role = authority.get("owner_role")
        if owner_role is not None and owner_role not in config.roles["roles"]:
            raise SchemaError(f"gates[{idx}].authority.owner_role is not a canonical role")
        if gate["gate_id"] in gate_ids:
            raise SchemaError(f"duplicate gate_id in task snapshot: {gate['gate_id']}")
        gate_ids.add(gate["gate_id"])

    for idx, approval in enumerate(_require_list(task["approvals"], "approvals")):
        validate_approval(approval, idx)
        if approval["approval_type"] not in config.roles["approval_authority"]:
            raise SchemaError(f"approvals[{idx}].approval_type is invalid")
        if approval["decision"] not in {"APPROVED", "REVISE", "REJECTED", "BLOCKED"}:
            raise SchemaError(f"approvals[{idx}].decision is invalid")
    for idx, finding in enumerate(_require_list(task["findings"], "findings")):
        validate_finding(finding, idx)

    requested = task.get("requested_transition")
    if requested is not None:
        try:
            WorkState(requested)
        except ValueError as exc:
            raise SchemaError("requested_transition is invalid") from exc

    completion_scope = task.get("completion_scope", "BOUNDED_TASK")
    if completion_scope not in {"BOUNDED_TASK", "PROJECT_RELEASE", "PROJECT_CLOSURE"}:
        raise SchemaError("completion_scope is invalid")

    governance = task.get("governance")
    if governance is not None:
        governance = _require_mapping(governance, "governance")
        handoff_required = governance.get("handoff_required")
        if handoff_required is not None and not isinstance(handoff_required, bool):
            raise SchemaError("governance.handoff_required must be boolean")
        pr_state = governance.get("pr_state")
        if pr_state is not None and pr_state not in {"NOT_OPEN", "OPEN", "APPROVED", "MERGED"}:
            raise SchemaError("governance.pr_state is invalid")
        independence = governance.get("independent_review")
        if independence is not None:
            independence = _require_mapping(independence, "governance.independent_review")
            decision = independence.get("decision")
            if decision not in {"REQUIRED", "NOT_REQUIRED"}:
                raise SchemaError("governance.independent_review.decision is invalid")
            if decision == "NOT_REQUIRED":
                if independence.get("basis") != "AUTHORITATIVE_CONTRACT":
                    raise SchemaError("NOT_REQUIRED independent review requires AUTHORITATIVE_CONTRACT basis")
                contract_ref = independence.get("contract_ref")
                if not isinstance(contract_ref, str) or not contract_ref.startswith("project-control://"):
                    raise SchemaError("authoritative independent-review contract_ref is invalid")
                if not isinstance(independence.get("contract_revision"), str) or not independence["contract_revision"].strip():
                    raise SchemaError("authoritative independent-review contract_revision is required")
                authority = _require_mapping(independence.get("authority"), "governance.independent_review.authority")
                validate_actor(authority, "governance.independent_review.authority")
                if authority.get("actor_type") != "HUMAN" or authority.get("authority_role") != "MASTER_PROJECT_CONTROL":
                    raise SchemaError("conditional independent-review authority must be MASTER_PROJECT_CONTROL human")

    kernel = _require_mapping(task["kernel"], "kernel")
    if not isinstance(kernel.get("profile_id"), str) or not kernel["profile_id"]:
        raise SchemaError("kernel.profile_id is required")
    if not isinstance(kernel.get("version_ref"), str) or not kernel["version_ref"]:
        raise SchemaError("kernel.version_ref is required")
    profile = config.kernel_profile
    if kernel["profile_id"] != profile["profile_id"] or kernel["version_ref"] != profile["version_ref"]:
        raise UnknownKernelError(
            f"unrecognized kernel profile/version: {kernel['profile_id']} / {kernel['version_ref']}"
        )

    if task.get("pause") is not None:
        pause = _require_mapping(task["pause"], "pause")
        if "resume_condition_satisfied" in pause and not isinstance(pause["resume_condition_satisfied"], bool):
            raise SchemaError("pause.resume_condition_satisfied must be boolean")
        if "resume_evidence_refs" in pause:
            _require_list(pause["resume_evidence_refs"], "pause.resume_evidence_refs")
    if task.get("blocker") is not None:
        blocker = _require_mapping(task["blocker"], "blocker")
        if "unblock_condition_satisfied" in blocker and not isinstance(blocker["unblock_condition_satisfied"], bool):
            raise SchemaError("blocker.unblock_condition_satisfied must be boolean")
        if "unblock_evidence_refs" in blocker:
            _require_list(blocker["unblock_evidence_refs"], "blocker.unblock_evidence_refs")
    if task.get("provenance") is not None:
        _require_mapping(task["provenance"], "provenance")
    return task
