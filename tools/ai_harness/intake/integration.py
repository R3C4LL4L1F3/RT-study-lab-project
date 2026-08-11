from __future__ import annotations

from pathlib import Path
from typing import Any, Sequence

from ..errors import SchemaError
from ..github_readonly.integration import evaluate_snapshot_with_evidence
from ..github_readonly.provider import EvidenceRecord
from .schema import AssemblyStatus


def evaluate_assembled_v0(
    assembled_snapshot: dict[str, Any],
    v0_task: dict[str, Any],
    *,
    evidence: Sequence[EvidenceRecord],
    repo_root: Path,
) -> dict[str, Any]:
    """Send an explicitly supplied, safe V0 projection through the existing AIH-002 seam.

    AIH-004 does not construct or authorize a V0 record here. It only verifies that
    governance values copied into the caller-supplied V0 task were authoritative in
    the assembly, then delegates evidence binding and the final deterministic
    recheck to the unchanged AIH-002/AIH-001 integration.
    """
    payload = assembled_snapshot.get("canonical_payload", assembled_snapshot)
    fields = payload.get("assembled_fields", {})
    for name in ("priority", "risk_tier", "work_state"):
        if name in v0_task and fields.get(name, {}).get("status") != AssemblyStatus.AUTHORITATIVE.value:
            raise SchemaError(f"non-authoritative assembled field cannot populate V0: {name}")
    return evaluate_snapshot_with_evidence(v0_task, evidence=evidence, repo_root=repo_root)
