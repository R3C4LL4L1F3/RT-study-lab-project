from __future__ import annotations

from dataclasses import dataclass
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
COLLECTION_OPERATIONS = frozenset({
    Operation.PR_COMMITS_LIST,
    Operation.PR_FILES_LIST,
    Operation.PR_REVIEWS_LIST,
    Operation.CHECK_RUNS_LIST,
})
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
    def permission_manifest(self, repository_alias: str) -> Mapping[str, str] | None: ...
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


@dataclass(frozen=True)
class TransportResponse:
    status_code: int
    payload: Any = None
    next_page: int | None = None
    endpoint_supports_absence: bool = False


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
    """Fixture-backed manifest/header source. It never creates or refreshes credentials."""

    def __init__(self, manifest: Mapping[str, str] | None = None, headers: Mapping[str, str] | None = None) -> None:
        self._manifest = None if manifest is None else dict(manifest)
        self._headers = dict(headers or {})

    def permission_manifest(self, repository_alias: str) -> Mapping[str, str] | None:
        return None if self._manifest is None else dict(self._manifest)

    def request_headers(self, repository_alias: str) -> Mapping[str, str]:
        return dict(self._headers)


class FixtureTransport:
    """Deterministic Stage-1 transport. Only GET semantics exist."""

    def __init__(self, responses: Sequence[TransportResponse]) -> None:
        self._responses = list(responses)
        self.calls: list[dict[str, Any]] = []

    def get(self, *, operation: Operation, repository: str, subject: str, headers: Mapping[str, str], page: int | None = None) -> TransportResponse:
        self.calls.append({
            "method": "GET",
            "operation": operation.value,
            "repository": repository,
            "subject": subject,
            "page": page,
            "header_names": sorted(headers),
        })
        if not self._responses:
            raise RuntimeError("fixture transport has no remaining response")
        return self._responses.pop(0)

    def request(self, method: str, **_: Any) -> TransportResponse:
        raise PermissionError(f"non-GET transport method rejected before network: {method.upper()}")


class DisabledEvidenceProvider:
    enabled = False

    def retrieve(self, request: EvidenceRequest) -> EvidenceRecord:
        return _record(
            request=request,
            state=EvidenceState.UNVERIFIED,
            capability=CredentialCapability.NOT_CONFIGURED,
            completeness=(CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None),
            payload={"reason": "provider-disabled"},
            repository_identity=None,
        )


class GitHubReadOnlyEvidenceProvider:
    enabled = True

    def __init__(self, credentials: CredentialSource, transport: ReadOnlyTransport) -> None:
        self._credentials = credentials
        self._transport = transport

    def retrieve(self, request: EvidenceRequest) -> EvidenceRecord:
        _validate_request(request)
        manifest = self._credentials.permission_manifest(request.repository_alias)
        capability = validate_permission_manifest(manifest)
        if capability is not CredentialCapability.VERIFIED_READ_ONLY:
            return _record(
                request=request,
                state=EvidenceState.UNVERIFIED,
                capability=capability,
                completeness=(CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None),
                payload={"reason": "credential-preflight-failed"},
                repository_identity=None,
            )

        headers = {**self._credentials.request_headers(request.repository_alias), "X-GitHub-Api-Version": GITHUB_API_VERSION}

        repo_response = self._transport.get(
            operation=Operation.REPO_GET,
            repository=EXPECTED_REPOSITORY,
            subject=EXPECTED_REPOSITORY,
            headers=headers,
        )
        repo_state, repo_identity, repo_payload = _normalize_repository(repo_response)
        if repo_state is not EvidenceState.VERIFIED:
            return _record(
                request=request,
                state=repo_state,
                capability=capability,
                completeness=(CollectionCompleteness.UNVERIFIED if request.operation in COLLECTION_OPERATIONS else None),
                payload={"repository": repo_payload, "reason": "repository-identity-preflight-failed"},
                repository_identity=repo_identity,
            )

        if request.operation is Operation.REPO_GET:
            return _record(
                request=request,
                state=EvidenceState.VERIFIED,
                capability=capability,
                completeness=None,
                payload=repo_payload,
                repository_identity=repo_identity,
            )

        if request.operation in COLLECTION_OPERATIONS:
            return self._retrieve_collection(request, capability, headers, repo_identity)
        return self._retrieve_scalar(request, capability, headers, repo_identity)

    def _retrieve_scalar(self, request: EvidenceRequest, capability: CredentialCapability, headers: Mapping[str, str], repository_identity: Mapping[str, Any]) -> EvidenceRecord:
        try:
            response = self._transport.get(
                operation=request.operation,
                repository=EXPECTED_REPOSITORY,
                subject=request.subject,
                headers=headers,
            )
        except Exception:
            return _record(
                request=request,
                state=EvidenceState.UNVERIFIED,
                capability=capability,
                completeness=None,
                payload={"reason": "operation-retrieval-failed"},
                repository_identity=repository_identity,
            )
        state, payload = _normalize_scalar(request, response, repository_identity)
        return _record(
            request=request,
            state=state,
            capability=capability,
            completeness=None,
            payload=payload,
            repository_identity=repository_identity,
        )

    def _retrieve_collection(self, request: EvidenceRequest, capability: CredentialCapability, headers: Mapping[str, str], repository_identity: Mapping[str, Any]) -> EvidenceRecord:
        items: list[Any] = []
        page: int | None = 1
        seen_pages: set[int] = set()
        while page is not None:
            if page in seen_pages:
                return _record(
                    request=request,
                    state=EvidenceState.UNVERIFIED,
                    capability=capability,
                    completeness=CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,
                    payload={"items": items, "reason": "pagination-cycle"},
                    repository_identity=repository_identity,
                )
            seen_pages.add(page)
            try:
                response = self._transport.get(
                    operation=request.operation,
                    repository=EXPECTED_REPOSITORY,
                    subject=request.subject,
                    headers=headers,
                    page=page,
                )
            except Exception:
                return _record(
                    request=request,
                    state=EvidenceState.UNVERIFIED,
                    capability=capability,
                    completeness=CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,
                    payload={"items": items, "reason": "collection-retrieval-failed"},
                    repository_identity=repository_identity,
                )
            if response.status_code != 200:
                return _record(
                    request=request,
                    state=EvidenceState.UNVERIFIED,
                    capability=capability,
                    completeness=CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,
                    payload={"items": items, "status_code": response.status_code},
                    repository_identity=repository_identity,
                )
            page_state, normalized_items = _normalize_collection_page(request.operation, response.payload)
            if page_state is not EvidenceState.VERIFIED:
                return _record(
                    request=request,
                    state=page_state,
                    capability=capability,
                    completeness=CollectionCompleteness.INCOMPLETE if items else CollectionCompleteness.UNVERIFIED,
                    payload={"items": items, "reason": "invalid-collection-page"},
                    repository_identity=repository_identity,
                )
            items.extend(normalized_items)
            page = response.next_page

        derived_state = _derive_collection_fact_state(request, items)
        return _record(
            request=request,
            state=derived_state,
            capability=capability,
            completeness=CollectionCompleteness.COMPLETE,
            payload={"items": items, "exhaustive": True},
            repository_identity=repository_identity,
        )


def resolve_evidence_state(states: Sequence[EvidenceState]) -> EvidenceState:
    if not states:
        return EvidenceState.UNVERIFIED
    present = set(states)
    for state in EVIDENCE_PRECEDENCE:
        if state in present:
            return state
    return EvidenceState.UNVERIFIED


def validate_permission_manifest(permissions: Mapping[str, str] | None) -> CredentialCapability:
    if permissions is None:
        return CredentialCapability.NOT_CONFIGURED
    normalized = {str(k).lower(): str(v).lower() for k, v in permissions.items()}
    if not normalized:
        return CredentialCapability.UNVERIFIED
    for required, required_value in READ_ONLY_PERMISSION_CEILING.items():
        if normalized.get(required) != required_value:
            return CredentialCapability.UNVERIFIED
    for name, value in normalized.items():
        if value not in {"read", "none"}:
            return CredentialCapability.OVERPRIVILEGED
        if name not in READ_ONLY_PERMISSION_CEILING and value != "none":
            return CredentialCapability.OVERPRIVILEGED
    return CredentialCapability.VERIFIED_READ_ONLY


def validate_content_path(path: str) -> str:
    if not isinstance(path, str) or not path:
        raise ValueError("content path is required")
    decoded = path
    for _ in range(3):
        newer = unquote(decoded)
        if newer == decoded:
            break
        decoded = newer
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


def _normalize_repository(response: TransportResponse) -> tuple[EvidenceState, Mapping[str, Any] | None, Any]:
    if response.status_code != 200 or not isinstance(response.payload, Mapping):
        return EvidenceState.UNVERIFIED, None, {"status_code": response.status_code}
    payload = dict(response.payload)
    required = {"id", "node_id", "full_name", "default_branch"}
    if not required.issubset(payload):
        return EvidenceState.UNVERIFIED, None, {"reason": "repository-required-field-missing"}
    identity = {
        "id": payload["id"],
        "node_id": payload["node_id"],
        "full_name": payload["full_name"],
        "default_branch": payload["default_branch"],
    }
    expected = {
        "id": EXPECTED_REPOSITORY_ID,
        "node_id": EXPECTED_NODE_ID,
        "full_name": EXPECTED_REPOSITORY,
        "default_branch": EXPECTED_DEFAULT_BRANCH,
    }
    if identity != expected:
        return EvidenceState.CONTRADICTORY, identity, _redact(payload)
    return EvidenceState.VERIFIED, identity, _redact(payload)


def _normalize_scalar(request: EvidenceRequest, response: TransportResponse, repository_identity: Mapping[str, Any]) -> tuple[EvidenceState, Any]:
    if request.operation is Operation.PR_MERGED_CHECK:
        if response.status_code == 204:
            return EvidenceState.VERIFIED, {"merged": True}
        if response.status_code == 404 and response.endpoint_supports_absence and _merged_absence_eligible(request):
            return EvidenceState.VERIFIED, {"merged": False}
        return EvidenceState.UNVERIFIED, {"status_code": response.status_code}

    if response.status_code == 404:
        if response.endpoint_supports_absence and _missing_eligible(request, repository_identity):
            return EvidenceState.MISSING, {"missing": True}
        return EvidenceState.UNVERIFIED, {"status_code": 404, "reason": "ambiguous-not-found"}
    if not (200 <= response.status_code < 300):
        return EvidenceState.UNVERIFIED, {"status_code": response.status_code}
    if not isinstance(response.payload, Mapping):
        return EvidenceState.UNVERIFIED, {"reason": "scalar-payload-not-object"}
    return _normalize_operation_payload(request, dict(response.payload))


def _normalize_operation_payload(request: EvidenceRequest, payload: Mapping[str, Any]) -> tuple[EvidenceState, Any]:
    op = request.operation
    if op is Operation.COMMIT_GET:
        if not isinstance(payload.get("sha"), str) or not payload["sha"]:
            return EvidenceState.UNVERIFIED, {"reason": "commit-sha-missing"}
        normalized = {"sha": payload["sha"]}
        if request.ref and re.fullmatch(r"[0-9a-fA-F]{40}", request.ref) and payload["sha"].lower() != request.ref.lower():
            return EvidenceState.STALE, normalized
        return EvidenceState.VERIFIED, normalized

    if op is Operation.CONTENT_GET:
        required = {"path", "sha"}
        if not required.issubset(payload) or not all(isinstance(payload[k], str) and payload[k] for k in required):
            return EvidenceState.UNVERIFIED, {"reason": "content-required-field-missing"}
        normalized_path = validate_content_path(payload["path"])
        if normalized_path != validate_content_path(request.path or ""):
            return EvidenceState.CONTRADICTORY, {"path": normalized_path, "sha": payload["sha"]}
        return EvidenceState.VERIFIED, {"path": normalized_path, "sha": payload["sha"]}

    if op is Operation.PR_GET:
        required = {"number", "state", "head", "base"}
        if not required.issubset(payload):
            return EvidenceState.UNVERIFIED, {"reason": "pr-required-field-missing"}
        try:
            requested_number = int(request.subject)
        except (TypeError, ValueError):
            return EvidenceState.UNVERIFIED, {"reason": "pr-subject-not-number"}
        if payload["number"] != requested_number:
            return EvidenceState.CONTRADICTORY, {"number": payload["number"]}
        if not isinstance(payload["head"], Mapping) or not isinstance(payload["base"], Mapping):
            return EvidenceState.UNVERIFIED, {"reason": "pr-head-base-invalid"}
        if not isinstance(payload["head"].get("sha"), str) or not isinstance(payload["base"].get("ref"), str):
            return EvidenceState.UNVERIFIED, {"reason": "pr-head-base-required-field-missing"}
        normalized = {
            "number": payload["number"],
            "state": payload["state"],
            "head_sha": payload["head"]["sha"],
            "base_ref": payload["base"]["ref"],
        }
        if request.ref and re.fullmatch(r"[0-9a-fA-F]{40}", request.ref) and normalized["head_sha"].lower() != request.ref.lower():
            return EvidenceState.STALE, normalized
        return EvidenceState.VERIFIED, normalized

    return EvidenceState.UNVERIFIED, {"reason": "unsupported-scalar-normalizer"}


def _normalize_collection_page(operation: Operation, payload: Any) -> tuple[EvidenceState, list[Any]]:
    if not isinstance(payload, list):
        return EvidenceState.UNVERIFIED, []
    normalized: list[Any] = []
    for item in payload:
        if not isinstance(item, Mapping):
            return EvidenceState.UNVERIFIED, []
        if operation is Operation.PR_COMMITS_LIST:
            sha = item.get("sha")
            if not isinstance(sha, str) or not sha:
                return EvidenceState.UNVERIFIED, []
            normalized.append({"sha": sha})
        elif operation is Operation.PR_FILES_LIST:
            filename, status = item.get("filename"), item.get("status")
            if not isinstance(filename, str) or not filename or not isinstance(status, str) or not status:
                return EvidenceState.UNVERIFIED, []
            normalized.append({"filename": filename, "status": status})
        elif operation is Operation.PR_REVIEWS_LIST:
            rid, state, user = item.get("id"), item.get("state"), item.get("user")
            if rid is None or not isinstance(state, str) or not isinstance(user, Mapping) or not isinstance(user.get("login"), str):
                return EvidenceState.UNVERIFIED, []
            normalized.append({"id": rid, "state": state, "user_login": user["login"]})
        elif operation is Operation.CHECK_RUNS_LIST:
            cid, status, conclusion = item.get("id"), item.get("status"), item.get("conclusion")
            if cid is None or not isinstance(status, str):
                return EvidenceState.UNVERIFIED, []
            normalized.append({"id": cid, "status": status, "conclusion": conclusion})
        else:
            return EvidenceState.UNVERIFIED, []
    return EvidenceState.VERIFIED, normalized


def _missing_eligible(request: EvidenceRequest, repository_identity: Mapping[str, Any]) -> bool:
    if repository_identity.get("id") != EXPECTED_REPOSITORY_ID or repository_identity.get("node_id") != EXPECTED_NODE_ID:
        return False
    if request.operation is Operation.CONTENT_GET:
        return bool(request.ref and request.path and validate_content_path(request.path))
    if request.operation is Operation.COMMIT_GET:
        return bool(request.subject)
    if request.operation is Operation.PR_GET:
        try:
            return int(request.subject) > 0
        except (TypeError, ValueError):
            return False
    return False


def _merged_absence_eligible(request: EvidenceRequest) -> bool:
    try:
        return request.operation is Operation.PR_MERGED_CHECK and int(request.subject) > 0
    except (TypeError, ValueError):
        return False


def _derive_collection_fact_state(request: EvidenceRequest, items: Sequence[Mapping[str, Any]]) -> EvidenceState:
    if request.operation is Operation.PR_COMMITS_LIST and request.ref:
        observed = {str(item["sha"]).lower() for item in items}
        if request.ref.lower() not in observed:
            return EvidenceState.STALE
    return EvidenceState.VERIFIED


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


def _record(*, request: EvidenceRequest, state: EvidenceState, capability: CredentialCapability, completeness: CollectionCompleteness | None, payload: Any, repository_identity: Mapping[str, Any] | None) -> EvidenceRecord:
    sanitized = _redact(payload)
    payload_hash = _canonical_hash(sanitized)
    repository_id = repository_identity.get("id") if repository_identity else None
    repository_node_id = repository_identity.get("node_id") if repository_identity else None
    audit = {
        "provider": PROVIDER_ID,
        "repository_alias": request.repository_alias,
        "repository_id": repository_id,
        "repository_node_id": repository_node_id,
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
        repository_id=repository_id,
        repository_node_id=repository_node_id,
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
