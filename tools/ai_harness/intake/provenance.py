from __future__ import annotations

from typing import Any, Iterable

from ..github_readonly.provider import EvidenceRecord


def evidence_envelope(record: EvidenceRecord) -> dict[str, Any]:
    return {
        "provider": "AIH_002_GITHUB_READ_ONLY",
        "original_evidence_state": record.evidence_state.value,
        "collection_completeness": record.collection_completeness.value if record.collection_completeness else None,
        "evidence_ref": f"github:{record.provider}:{record.operation}:{record.subject}:{record.payload_sha256}",
        "audit": dict(record.audit),
    }


def evidence_snapshot(records: Iterable[EvidenceRecord]) -> list[dict[str, Any]]:
    return [evidence_envelope(record) for record in records]
