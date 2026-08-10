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

__all__ = [
    "CollectionCompleteness",
    "CredentialCapability",
    "DisabledEvidenceProvider",
    "EvidenceProvider",
    "EvidenceRecord",
    "EvidenceRequest",
    "EvidenceState",
    "FixtureTransport",
    "GitHubReadOnlyEvidenceProvider",
    "Operation",
    "StaticCredentialSource",
    "TransportResponse",
]
