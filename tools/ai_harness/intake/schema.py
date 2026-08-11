from __future__ import annotations

from enum import Enum
from typing import Any

from ..errors import SchemaError


class FieldOrigin(str, Enum):
    USER_SUPPLIED = "USER_SUPPLIED"
    AUTHORITATIVE_SOURCE = "AUTHORITATIVE_SOURCE"
    DETERMINISTIC_DERIVATION = "DETERMINISTIC_DERIVATION"
    GITHUB_EVIDENCE = "GITHUB_EVIDENCE"
    SYSTEM_DEFAULT = "SYSTEM_DEFAULT"


class AssemblyStatus(str, Enum):
    AUTHORITATIVE = "AUTHORITATIVE"
    DETERMINISTICALLY_DERIVED = "DETERMINISTICALLY_DERIVED"
    PROPOSED = "PROPOSED"
    UNVERIFIED = "UNVERIFIED"
    MISSING = "MISSING"
    CONTRADICTORY = "CONTRADICTORY"


def field(value: Any = None, *, origin: FieldOrigin | str = FieldOrigin.USER_SUPPLIED,
          status: AssemblyStatus | str = AssemblyStatus.UNVERIFIED, **metadata: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "value": value,
        "origin": origin.value if isinstance(origin, Enum) else origin,
        "status": status.value if isinstance(status, Enum) else status,
    }
    result.update(metadata)
    return result


def _field(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaError(f"{name} must be an object")
    if "origin" in value and value["origin"] not in {x.value for x in FieldOrigin}:
        raise SchemaError(f"{name}.origin is invalid")
    if "status" in value and value["status"] not in {x.value for x in AssemblyStatus}:
        raise SchemaError(f"{name}.status is invalid")
    return value


def validate_intake_request(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise SchemaError("intake_request must be an object")
    if raw.get("intake_schema_version", "1") != "1":
        raise SchemaError("unsupported intake_schema_version")
    task = raw.get("task")
    if not isinstance(task, dict):
        raise SchemaError("intake_request.task must be an object")
    for name in ("task_id", "title", "description", "requested_outcome"):
        if name in task:
            _field(task[name], f"task.{name}")
    claims = raw.get("governance_claims", {})
    if not isinstance(claims, dict):
        raise SchemaError("governance_claims must be an object")
    for name, value in claims.items():
        _field(value, f"governance_claims.{name}")
    references = raw.get("references", {})
    if not isinstance(references, dict):
        raise SchemaError("references must be an object")
    for name in ("issue_numbers", "pull_request_numbers", "commit_shas", "source_refs", "document_refs", "github_content_requests"):
        if name in references and not isinstance(references[name], list):
            raise SchemaError(f"references.{name} must be an array")
    for item in references.get("github_content_requests", []):
        if not isinstance(item, dict):
            raise SchemaError("github_content_requests entries must be objects")
        for required in ("repository_alias", "ref", "path"):
            if not isinstance(item.get(required), str) or not item[required]:
                raise SchemaError(f"github_content_requests.{required} is required")
    return raw
