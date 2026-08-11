"""Stage-1 fixture-backed, read-only GitHub evidence provider boundary."""

from .provider import (
    CollectionCompleteness,
    CredentialCapability,
    DisabledEvidenceProvider,
    EvidenceProvider,
    EvidenceRecord,
    EvidenceRequest,
    EvidenceState,
    FixtureTransport,
    GitHubReadOnlyEvidenceProvider,
    Operation,
    StaticCredentialSource,
    TransportResponse,
)
from .integration import evaluate_snapshot_with_evidence, item_evidence_ref, record_evidence_ref

__all__ = [
    "CollectionCompleteness", "CredentialCapability", "DisabledEvidenceProvider",
    "EvidenceProvider", "EvidenceRecord", "EvidenceRequest", "EvidenceState",
    "FixtureTransport", "GitHubReadOnlyEvidenceProvider", "Operation",
    "StaticCredentialSource", "TransportResponse", "evaluate_snapshot_with_evidence",
    "item_evidence_ref", "record_evidence_ref",
]
