from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Sequence

from tools.ai_harness.evaluator import evaluate_snapshot
from .provider import EvidenceRecord, EvidenceState

GITHUB_REF_PREFIXES = ("github:", "github-item:")
POSITIVE_SUPPORT_STATES = {EvidenceState.VERIFIED}


def _hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def record_evidence_ref(record: EvidenceRecord) -> str:
    return f"github:{record.provider}:{record.operation}:{record.subject}:{record.payload_sha256}"


def item_evidence_ref(record: EvidenceRecord, item: dict[str, Any]) -> str:
    return f"github-item:{record.provider}:{record.operation}:{record.subject}:{_hash(item)}"


def _available_refs(evidence: Sequence[EvidenceRecord]) -> set[str]:
    """Return GitHub refs eligible to satisfy positive evidence-reference requirements.

    Only VERIFIED evidence is positive support. MISSING is authoritative absence, not
    positive evidence; STALE, UNVERIFIED, and CONTRADICTORY likewise cannot satisfy a
    positive non-empty evidence requirement. All states remain available in provenance.
    """
    available: set[str] = set()
    for record in evidence:
        if record.evidence_state in POSITIVE_SUPPORT_STATES:
            available.add(record_evidence_ref(record))
        payload = record.payload
        if isinstance(payload, dict) and isinstance(payload.get("items"), list):
            for item in payload["items"]:
                if not isinstance(item, dict):
                    continue
                try:
                    state = EvidenceState(item.get("evidence_state"))
                except (TypeError, ValueError):
                    continue
                if state in POSITIVE_SUPPORT_STATES:
                    available.add(item_evidence_ref(record, item))
    return available


def _bind_refs(values: Iterable[Any], available: set[str]) -> list[Any]:
    """Validate only GitHub-provider refs; preserve other evidence authorities untouched."""
    bound: list[Any] = []
    for value in values:
        if isinstance(value, str) and value.startswith(GITHUB_REF_PREFIXES):
            if value in available:
                bound.append(value)
        else:
            bound.append(value)
    return bound


def _bind_evidence_before_policy(raw_task: dict[str, Any], evidence: Sequence[EvidenceRecord]) -> dict[str, Any]:
    """Bind normalized positive GitHub support to existing V0 evidence-reference inputs.

    This does not create approvals, gate PASS states, clinical evidence, QA disposition,
    classifications, or work-state transitions. It only validates GitHub-prefixed
    positive evidence references already asserted by the task snapshot before V0 policy runs.
    """
    task = deepcopy(raw_task)
    available = _available_refs(evidence)

    for finding in task.get("findings", []):
        evidence_block = finding.get("evidence") if isinstance(finding, dict) else None
        if isinstance(evidence_block, dict) and isinstance(evidence_block.get("evidence_refs"), list):
            evidence_block["evidence_refs"] = _bind_refs(evidence_block["evidence_refs"], available)

    pause = task.get("pause")
    if isinstance(pause, dict) and isinstance(pause.get("resume_evidence_refs"), list):
        pause["resume_evidence_refs"] = _bind_refs(pause["resume_evidence_refs"], available)

    blocker = task.get("blocker")
    if isinstance(blocker, dict) and isinstance(blocker.get("unblock_evidence_refs"), list):
        blocker["unblock_evidence_refs"] = _bind_refs(blocker["unblock_evidence_refs"], available)

    for gate in task.get("gates", []):
        if not isinstance(gate, dict) or gate.get("gate_id") != "GITHUB_PROVENANCE":
            continue
        disposition = gate.get("disposition")
        if isinstance(disposition, dict) and isinstance(disposition.get("evidence_refs"), list):
            disposition["evidence_refs"] = _bind_refs(disposition["evidence_refs"], available)

    provenance = task.get("provenance")
    if isinstance(provenance, dict) and isinstance(provenance.get("evidence_refs"), list):
        provenance["evidence_refs"] = _bind_refs(provenance["evidence_refs"], available)

    return task


def evaluate_snapshot_with_evidence(
    raw_task: dict[str, Any],
    *,
    evidence: Sequence[EvidenceRecord],
    repo_root: Path,
) -> dict[str, Any]:
    """Bind normalized positive evidence first, then run unchanged V0 evaluator/recheck."""
    for record in evidence:
        if not isinstance(record, EvidenceRecord):
            raise TypeError("only normalized EvidenceRecord inputs are accepted")

    bound_task = _bind_evidence_before_policy(raw_task, evidence)
    result = evaluate_snapshot(bound_task, repo_root=repo_root)
    if not result.get("final_policy_recheck", {}).get("performed"):
        raise RuntimeError("mandatory final deterministic policy recheck was not performed")

    output = dict(result)
    output["evidence_binding"] = {
        "performed_before_deterministic_evaluation": True,
        "positive_support_states": sorted(state.value for state in POSITIVE_SUPPORT_STATES),
        "available_github_refs": sorted(_available_refs(evidence)),
    }
    output["evidence_provenance"] = [
        {
            "provider": record.provider,
            "repository_alias": record.repository_alias,
            "operation": record.operation,
            "subject": record.subject,
            "ref": record.ref,
            "evidence_state": record.evidence_state.value,
            "collection_completeness": record.collection_completeness.value if record.collection_completeness else None,
            "payload_sha256": record.payload_sha256,
            "audit": dict(record.audit),
        }
        for record in evidence
    ]
    return output
