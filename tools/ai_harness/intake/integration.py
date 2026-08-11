from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Sequence

from ..errors import SchemaError
from ..github_readonly.integration import evaluate_snapshot_with_evidence
from ..github_readonly.provider import EvidenceRecord
from .schema import AssemblyStatus


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
    return {
        "task_id": fields["task_id"]["value"], "title": fields["title"]["value"],
        "priority": fields["priority"]["value"], "risk_tier": fields["risk_tier"]["value"],
        "work_state": fields["work_state"]["value"],
        "routing": {"coordinating_owner": "MASTER_PROJECT_CONTROL", "primary_owner": owner["value"], "supporting_owners": []},
        "requested_transition": None,
        "gates": payload.get("gates", {}).get("gates", []), "approvals": [], "findings": [],
        "pause": None, "blocker": None,
        "kernel": {"profile_id": kernel["profile_id"], "version_ref": kernel["version_ref"]},
        "provenance": {"evidence_refs": [item["evidence_ref"] for item in payload.get("evidence_snapshot", [])]},
    }


def evaluate_assembled_v0(
    assembled_snapshot: dict[str, Any],
    v0_task: dict[str, Any] | None = None,
    *,
    evidence: Sequence[EvidenceRecord],
    repo_root: Path,
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
    return evaluate_snapshot_with_evidence(v0_task, evidence=evidence, repo_root=repo_root)
