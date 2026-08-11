from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Sequence

from ..errors import SchemaError
from ..github_readonly.integration import evaluate_snapshot_with_evidence
from ..github_readonly.provider import EvidenceRecord
from .schema import AssemblyStatus


def _v0_gate_records(gates_payload: dict[str, Any], *, risk_value: str) -> list[dict[str, Any]]:
    """Convert the assembly gate envelopes to the existing V0 gate shape."""
    result: list[dict[str, Any]] = []
    for source in gates_payload.get("gates", []):
        obligation = dict(source.get("obligation") or {})
        if "required" in obligation:
            v0_obligation = obligation
        else:
            condition = obligation.get("condition")
            v0_obligation = {
                "required": bool(obligation.get("value")),
                "origin": condition or {"type": "RISK_TIER", "ref": risk_value},
                "status": obligation.get("status"),
                "derivation_rule_ids": list(obligation.get("derivation_rule_ids", [])),
            }
        result.append({**source, "obligation": v0_obligation})
    return result


def build_v0_task(assembled_snapshot: dict[str, Any], *, repo_root: Path) -> dict[str, Any]:
    """Build a complete V0 record from validated assembled fields only."""
    payload = assembled_snapshot.get("canonical_payload", assembled_snapshot)
    fields = payload.get("assembled_fields", {})
    for name in ("task_id", "title"):
        if not fields.get(name, {}).get("value"):
            raise SchemaError(f"missing intake field for V0: {name}")
    for name in ("priority", "risk_tier", "work_state"):
        if fields.get(name, {}).get("status") != AssemblyStatus.AUTHORITATIVE.value:
            raise SchemaError(f"non-authoritative assembled field cannot populate V0: {name}")
    owner = fields.get("owner", {})
    if owner.get("status") != AssemblyStatus.AUTHORITATIVE.value:
        raise SchemaError("authoritative owner is required for V0 routing")
    kernel = json.loads((repo_root / "config" / "ai_harness" / "kernel-profile.v1.json").read_text(encoding="utf-8"))
    gates_payload = payload.get("gates", {})
    task = {
        "task_id": fields["task_id"]["value"], "title": fields["title"]["value"],
        "priority": fields["priority"]["value"], "risk_tier": fields["risk_tier"]["value"],
        "work_state": fields["work_state"]["value"],
        "routing": {"coordinating_owner": "MASTER_PROJECT_CONTROL", "primary_owner": owner["value"], "supporting_owners": []},
        "requested_transition": None,
        "gates": _v0_gate_records(gates_payload, risk_value=fields["risk_tier"]["value"]), "approvals": [], "findings": [],
        "pause": None, "blocker": None,
        "kernel": {"profile_id": kernel["profile_id"], "version_ref": kernel["version_ref"]},
        "provenance": {"evidence_refs": [item["evidence_ref"] for item in payload.get("evidence_snapshot", [])]},
    }
    completion_scope = fields.get("completion_scope", {})
    if completion_scope.get("status") == AssemblyStatus.AUTHORITATIVE.value:
        task["completion_scope"] = completion_scope["value"]
    independent = fields.get("independent_review_requirement", {})
    if independent.get("status") == AssemblyStatus.AUTHORITATIVE.value:
        source_refs = independent.get("source_refs") or []
        task["governance"] = {
            "independent_review": {
                "decision": "REQUIRED" if independent.get("value") is True else "NOT_REQUIRED",
                "basis": "AUTHORITATIVE_CONTRACT",
                "contract_ref": source_refs[0] if source_refs else "",
                "contract_revision": independent.get("source_revision", ""),
                "authority": {
                    "actor_id": independent.get("authority_actor_id", ""),
                    "actor_type": "HUMAN",
                    "authority_role": independent.get("authority_role"),
                },
            }
        }
    return task


def evaluate_assembled_v0(
    assembled_snapshot: dict[str, Any],
    v0_task: dict[str, Any] | None = None,
    *,
    evidence: Sequence[EvidenceRecord],
    repo_root: Path,
    governance_profile: str | None = None,
) -> dict[str, Any]:
    """Send a safe V0 projection through the existing AIH-002 seam.

    When no task is supplied, AIH-004 constructs one from authoritative assembled
    fields only. In both modes, evidence binding and the final deterministic
    recheck are delegated to the unchanged AIH-002/AIH-001 integration.
    """
    if v0_task is None:
        v0_task = build_v0_task(assembled_snapshot, repo_root=repo_root)
    payload = assembled_snapshot.get("canonical_payload", assembled_snapshot)
    fields = payload.get("assembled_fields", {})
    for name in ("priority", "risk_tier", "work_state"):
        if name in v0_task and fields.get(name, {}).get("status") != AssemblyStatus.AUTHORITATIVE.value:
            raise SchemaError(f"non-authoritative assembled field cannot populate V0: {name}")
    return evaluate_snapshot_with_evidence(
        v0_task,
        evidence=evidence,
        repo_root=repo_root,
        governance_profile=governance_profile,
    )
