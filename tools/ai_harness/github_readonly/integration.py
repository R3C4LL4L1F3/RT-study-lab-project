from __future__ import annotations

from pathlib import Path
from typing import Any, Sequence

from tools.ai_harness.evaluator import evaluate_snapshot
from .provider import EvidenceRecord


def evaluate_snapshot_with_evidence(
    raw_task: dict[str, Any],
    *,
    evidence: Sequence[EvidenceRecord],
    repo_root: Path,
) -> dict[str, Any]:
    """Run the unchanged V0 evaluator and attach normalized evidence provenance only.

    Evidence is repository-fact input. It does not mutate the task snapshot, establish
    approval/QA authority, or bypass the mandatory final deterministic policy recheck.
    """
    for record in evidence:
        if not isinstance(record, EvidenceRecord):
            raise TypeError("only normalized EvidenceRecord inputs are accepted")

    result = evaluate_snapshot(raw_task, repo_root=repo_root)
    if not result.get("final_policy_recheck", {}).get("performed"):
        raise RuntimeError("mandatory final deterministic policy recheck was not performed")

    output = dict(result)
    output["evidence_provenance"] = [
        {
            "provider": record.provider,
            "repository_alias": record.repository_alias,
            "operation": record.operation,
            "subject": record.subject,
            "ref": record.ref,
            "evidence_state": record.evidence_state.value,
            "payload_sha256": record.payload_sha256,
            "audit": dict(record.audit),
        }
        for record in evidence
    ]
    return output
