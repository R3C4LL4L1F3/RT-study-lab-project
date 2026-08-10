from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import hashlib
import json
import re
from typing import Any, Mapping, Protocol, Sequence
from urllib.parse import unquote

GITHUB_API_VERSION = "2026-03-10"
PROVIDER_ID = "github-readonly-v1"
PROJECT_CONTROL_ALIAS = "PROJECT_CONTROL"
EXPECTED_REPOSITORY = "R3C4LL4L1F3/RT-study-lab-project"
EXPECTED_REPOSITORY_ID = 1328584202
EXPECTED_NODE_ID = "R_kgDOTzCWCg"
EXPECTED_DEFAULT_BRANCH = "main"


class EvidenceState(str, Enum):
    VERIFIED = "VERIFIED"
    MISSING = "MISSING"
    STALE = "STALE"
    UNVERIFIED = "UNVERIFIED"
    CONTRADICTORY = "CONTRADICTORY"


EVIDENCE_PRECEDENCE: tuple[EvidenceState, ...] = (
    EvidenceState.CONTRADICTORY,
    EvidenceState.UNVERIFIED,
    EvidenceState.STALE,
    EvidenceState.MISSING,
    EvidenceState.VERIFIED,
)


class CollectionCompleteness(str, Enum):
    COMPLETE = "COMPLETE"
    INCOMPLETE = "INCOMPLETE"
    UNVERIFIED = "UNVERIFIED"


class CredentialCapability(str, Enum):
    NOT_CONFIGURED = "NOT_CONFIGURED"
    UNVERIFIED = "UNVERIFIED"
    INVALID = "INVALID"
    OVERPRIVILEGED = "OVERPRIVILEGED"
    VERIFIED_READ_ONLY = "VERIFIED_READ_ONLY"


class Operation(str, Enum):
    REPO_GET = "GH-OP-REPO-GET"
    COMMIT_GET = "GH-OP-COMMIT-GET"
    CONTENT_GET = "GH-OP-CONTENT-GET"
    PR_GET = "GH-OP-PR-GET"
    PR_COMMITS_LIST = "GH-OP-PR-COMMITS-LIST"
    PR_FILES_LIST = "GH-OP-PR-FILES-LIST"
    PR_REVIEWS_LIST = "GH-OP-PR-REVIEWS-LIST"
    PR_MERGED_CHECK = "GH-OP-PR-MERGED-CHECK"
    CHECK_RUNS_LIST = "GH-OP-CHECK-RUNS-LIST"


ALLOWED_OPERATIONS = frozenset(Operation)
COLLECTION_OPERATIONS = frozenset(
    {
        Operation.PR_COMMITS_LIST,
        Operation.PR_FILES_LIST,
        Operation.PR_REVIEWS_LIST,
        Operation.CHECK_RUNS_LIST,
    }
)
CONTENT_PREFIXES = (
    "ai-harness/RTSL-AIH-001/",
    "ai-harness/RTSL-AIH-002/",
    "docs/ai-harness/",
    "config/ai_harness/",
)
READ_ONLY_PERMISSION_CEILING = {
    "metadata": "read",
    "contents": "read",
    "pull_requests": "read",
    "checks": "read",
}
SECRET_HEADER_NAMES = frozenset({"authorization", "proxy-authorization", "x-github-token"})


class EvidenceProvider(Protocol):
    enabled: bool

    def retrieve(self, request: "EvidenceRequest") -> "EvidenceRecord": ...


class CredentialSource(Protocol):
    def capability(self, repository_alias: str) -> CredentialCapability: ...

    def request_headers(self, repository_alias: str) -> Mapping[str, str]: ...


class ReadOnlyTransport(Protocol):
    def get(
        self,
        *,
        operation: Operation,
        repository: str,
        subject: str,
        headers: Mapping[str, str],
        page: int | None = None,
    ) -> "TransportResponse": ...


@dataclass(frozen=True)
class EvidenceRequest:
    repository_alias: str
    operation: Operation
    subject: str
    ref: str | None = None
    path: str | None = None
    observed_states: tuple[EvidenceState, ...] = ()
    absence_eligible: bool = False


@dataclass(frozen=True)
class TransportResponse:
    status_code: int
    payload: Any = None
    next_page: int | None = None
    endpoint_supports_absence: bool = False
    request_headers: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class EvidenceRecord:
    provider: str
    repository_alias: str
    repository_id: int | None
    repository_node_id: str | None
    operation: str
    subject: str
    ref: str | None
    api_version: str
    evidence_state: EvidenceState
    credential_capability: CredentialCapability
    collection_completeness: CollectionCompleteness | None
    payload: Any
    payload_sha256: str
    audit: Mapping[str, Any]


class StaticCredentialSource:
    """Fixture-backed capability source. It never creates or refreshes live credentials."""

    def __init__(
        self,
        capability: CredentialCapability = CredentialCapability.NOT_CONFIGURED,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        self._capability = capability
        self._headers = dict(headers or {})

    def capability(self, repository_alias: str) -> CredentialCapability:
        return self._capability

    def request_headers(self, repository_alias: str) -> Mapping[str, str]:
        return dict(self._headers)


class FixtureTransport:
    """Deterministic Stage-1 transport. Only GET semantics exist."""

    def __init__(self, responses: Sequence[TransportResponse]) -> None:
        self._responses = list(responses)
        self.calls: list[dict[str, Any]] = []

    def get(
        self,
        *,
        operation: Operation,
        repository: str,
        subject: str,
        headers: Mapping[str, str],
        page: int | None = None,
    ) -> TransportResponse:
        self.calls.append(
            {
                "method": "GET",
                "operation": operation.value,
                "repository": repository,
                "subject": subject,
                "page": page,
                "header_names": sorted(headers),
            }
        )
        if not self._responses:
            raise RuntimeError("fixture transport has no remaining response")
        return self._responses.pop(0)

    def request(self, method: str, **_: Any) -> TransportResponse:
        raise PermissionError(f"non-GET transport method rejected before network: {method.upper()}")


class DisabledEvidenceProvider:
    enabled = False

    def retrieve(self, request: EvidenceRequest) -> EvidenceRecord:
        capability = CredentialCapability.NOT_CONFIGURED
        return _record(
            request=request,
            state=EvidenceState.UNVERIFIED,
            capability=capability,
            completeness=(CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None),
            payload={"reason": "provider-disabled"},
        )


class GitHubReadOnlyEvidenceProvider:
    enabled = True

    def __init__(self, credentials: CredentialSource, transport: ReadOnlyTransport) -> None:
        self._credentials = credentials
        self._transport = transport

    def retrieve(self, request: EvidenceRequest) -> EvidenceRecord:
        _validate_request(request)
        capability = self._credentials.capability(request.repository_alias)
        if capability is not CredentialCapability.VERIFIED_READ_ONLY:
            return _record(
                request=request,
                state=resolve_evidence_state((*request.observed_states, EvidenceState.UNVERIFIED)),
                capability=capability,
                completeness=(CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None),
                payload={"reason": "credential-preflight-failed"},
            )

        headers = _safe_request_headers(self._credentials.request_headers(request.repository_alias))
        headers = {**headers, "X-GitHub-Api-Version": GITHUB_API_VERSION}
        if request.operation in COLLECTION_OPERATIONS:
            return self._retrieve_collection(request, capability, headers)
        return self._retrieve_scalar(request, capability, headers)

    def _retrieve_scalar(
        self,
        request: EvidenceRequest,
        capability: CredentialCapability,
        headers: Mapping[str, str],
    ) -> EvidenceRecord:
        response = self._transport.get(
            operation=request.operation,
            repository=EXPECTED_REPOSITORY,
            subject=request.subject,
            headers=headers,
        )
        state, payload = _scalar_state(request, response)
        state = resolve_evidence_state((*request.observed_states, state))
        return _record(request=request, state=state, capability=capability, completeness=None, payload=payload)

    def _retrieve_collection(
        self,
        request: EvidenceRequest,
        capability: CredentialCapability,
        headers: Mapping[str, str],
    ) -> EvidenceRecord:
        items: list[Any] = []
        page: int | None = 1
        completeness = CollectionCompleteness.COMPLETE
        while page is not None:
            try:
                response = self._transport.get(
                    operation=request.operation,
                    repository=EXPECTED_REPOSITORY,
                    subject=request.subject,
                    headers=headers,
                    page=page,
                )
            except Exception:
                completeness = CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED
                state = resolve_evidence_state((*request.observed_states, EvidenceState.UNVERIFIED))
                return _record(
                    request=request,
                    state=state,
                    capability=capability,
                    completeness=completeness,
                    payload={"items": items, "reason": "collection-retrieval-failed"},
                )
            if response.status_code != 200:
                completeness = CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED
                state = resolve_evidence_state((*request.observed_states, EvidenceState.UNVERIFIED))
                return _record(
                    request=request,
                    state=state,
                    capability=capability,
                    completeness=completeness,
                    payload={"items": items, "status_code": response.status_code},
                )
            if not isinstance(response.payload, list):
                completeness = CollectionCompleteness.UNVERIFIED
                return _record(
                    request=request,
                    state=EvidenceState.UNVERIFIED,
                    capability=capability,
                    completeness=completeness,
                    payload={"items": items, "reason": "non-list collection payload"},
                )
            items.extend(response.payload)
            page = response.next_page

        state = resolve_evidence_state((*request.observed_states, EvidenceState.VERIFIED))
        return _record(
            request=request,
            state=state,
            capability=capability,
            completeness=completeness,
            payload={"items": items, "exhaustive": True},
        )


def resolve_evidence_state(states: Sequence[EvidenceState]) -> EvidenceState:
    if not states:
        return EvidenceState.UNVERIFIED
    present = set(states)
    for state in EVIDENCE_PRECEDENCE:
        if state in present:
            return state
    return EvidenceState.UNVERIFIED


def validate_permission_manifest(permissions: Mapping[str, str]) -> CredentialCapability:
    normalized = {str(k).lower(): str(v).lower() for k, v in permissions.items()}
    if not normalized:
        return CredentialCapability.UNVERIFIED
    for required in READ_ONLY_PERMISSION_CEILING:
        if required not in normalized:
            return CredentialCapability.UNVERIFIED
    for name, value in normalized.items():
        if value not in {"read", "none"}:
            return CredentialCapability.OVERPRIVILEGED
        if name not in READ_ONLY_PERMISSION_CEILING and value != "none":
            return CredentialCapability.OVERPRIVILEGED
    for required, ceiling in READ_ONLY_PERMISSION_CEILING.items():
        if normalized.get(required) not in {ceiling, "none", None}:
            return CredentialCapability.OVERPRIVILEGED
    return CredentialCapability.VERIFIED_READ_ONLY


def validate_content_path(path: str) -> str:
    if not isinstance(path, str) or not path:
        raise ValueError("content path is required")
    decoded = path
    for _ in range(3):
        new = unquote(decoded)
        if new == decoded:
            break
        decoded = new
    decoded = decoded.replace("\\", "/")
    if decoded.startswith("/") or re.match(r"^[A-Za-z]:/", decoded):
        raise ValueError("absolute content paths are prohibited")
    segments = decoded.split("/")
    if any(segment in {"", ".", ".."} for segment in segments):
        raise ValueError("path traversal or normalization escape prohibited")
    normalized = "/".join(segments)
    if not any(normalized.startswith(prefix) for prefix in CONTENT_PREFIXES):
        raise ValueError("content path is outside the governed allowlist")
    return normalized


def _validate_request(request: EvidenceRequest) -> None:
    if request.repository_alias != PROJECT_CONTROL_ALIAS:
        raise ValueError("repository alias is not allowlisted")
    if request.operation not in ALLOWED_OPERATIONS:
        raise ValueError("operation is not allowlisted")
    if request.operation is Operation.CONTENT_GET:
        if request.path is None:
            raise ValueError("content operation requires an explicit path")
        validate_content_path(request.path)
        if not request.ref:
            raise ValueError("content operation requires an explicit ref")


def _safe_request_headers(headers: Mapping[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in headers.items():
        if key.lower() in SECRET_HEADER_NAMES:
            result[key] = value
        else:
            result[key] = value
    return result


def _scalar_state(request: EvidenceRequest, response: TransportResponse) -> tuple[EvidenceState, Any]:
    if request.operation is Operation.PR_MERGED_CHECK:
        if response.status_code == 204:
            return EvidenceState.VERIFIED, {"merged": True}
        if response.status_code == 404 and request.absence_eligible and response.endpoint_supports_absence:
            return EvidenceState.VERIFIED, {"merged": False}
        return EvidenceState.UNVERIFIED, {"status_code": response.status_code}

    if 200 <= response.status_code < 300:
        return EvidenceState.VERIFIED, response.payload
    if response.status_code == 404:
        if request.absence_eligible and response.endpoint_supports_absence:
            return EvidenceState.MISSING, {"missing": True}
        return EvidenceState.UNVERIFIED, {"status_code": 404, "reason": "ambiguous-not-found"}
    return EvidenceState.UNVERIFIED, {"status_code": response.status_code}


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _redact(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            lower = str(key).lower()
            if lower in SECRET_HEADER_NAMES or "token" in lower or "secret" in lower or "private_key" in lower:
                result[str(key)] = "[REDACTED]"
            else:
                result[str(key)] = _redact(item)
        return result
    if isinstance(value, list):
        return [_redact(v) for v in value]
    if isinstance(value, tuple):
        return tuple(_redact(v) for v in value)
    return value


def _record(
    *,
    request: EvidenceRequest,
    state: EvidenceState,
    capability: CredentialCapability,
    completeness: CollectionCompleteness | None,
    payload: Any,
) -> EvidenceRecord:
    sanitized = _redact(payload)
    payload_hash = _canonical_hash(sanitized)
    audit = {
        "provider": PROVIDER_ID,
        "repository_alias": request.repository_alias,
        "repository_id": EXPECTED_REPOSITORY_ID,
        "repository_node_id": EXPECTED_NODE_ID,
        "operation": request.operation.value,
        "subject": request.subject,
        "ref": request.ref,
        "github_api_version": GITHUB_API_VERSION,
        "evidence_state": state.value,
        "credential_capability": capability.value,
        "collection_completeness": completeness.value if completeness else None,
        "payload_sha256": payload_hash,
    }
    return EvidenceRecord(
        provider=PROVIDER_ID,
        repository_alias=request.repository_alias,
        repository_id=EXPECTED_REPOSITORY_ID,
        repository_node_id=EXPECTED_NODE_ID,
        operation=request.operation.value,
        subject=request.subject,
        ref=request.ref,
        api_version=GITHUB_API_VERSION,
        evidence_state=state,
        credential_capability=capability,
        collection_completeness=completeness,
        payload=sanitized,
        payload_sha256=payload_hash,
        audit=audit,
    )
