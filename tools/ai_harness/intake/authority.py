from __future__ import annotations

import re
from typing import Any

from .schema import AssemblyStatus, FieldOrigin

AUTHORITY_BY_FIELD = {
    "priority": ("MASTER", "MASTER_PROJECT_CONTROL"),
    "risk_tier": ("MASTER", "MASTER_PROJECT_CONTROL"),
    "owner": ("MASTER", "MASTER_PROJECT_CONTROL"),
    "subsystem": ("MASTER", "MASTER_PROJECT_CONTROL"),
    "work_state": ("MASTER", "MASTER_PROJECT_CONTROL"),
    "clinical_disposition": ("CLINICAL", "CLINICAL_VALIDATION_AND_SOURCES"),
    "architecture_disposition": ("ARCHITECTURE", "PLANNING_ARCHITECTURE"),
    "qa_disposition": ("QA", "QA_REGRESSION_RELEASE"),
}
SOURCE_PREFIXES = ("project-control://", "clinical://", "architecture://", "qa://", "github://")


def _valid_source_ref(ref: Any) -> bool:
    return isinstance(ref, str) and bool(ref.strip()) and ref.startswith(SOURCE_PREFIXES) and len(ref.split("://", 1)[1]) > 0


def validate_authoritative_field(field_name: str, candidate: dict[str, Any], *, conflicting: bool = False) -> dict[str, Any]:
    domain_role = AUTHORITY_BY_FIELD.get(field_name)
    source_refs = candidate.get("source_refs", [])
    role = candidate.get("authority_role")
    checks = {
        "domain_recognized": domain_role is not None,
        "authority_role_recognized": domain_role is not None and role in domain_role,
        "source_ref_valid": isinstance(source_refs, list) and bool(source_refs) and all(_valid_source_ref(x) for x in source_refs),
        "source_applicable_to_field": domain_role is not None and candidate.get("applicable_field", field_name) == field_name,
        "provenance_valid": bool(candidate.get("source_revision")) and isinstance(candidate.get("source_revision"), str),
        "unresolved_authoritative_contradiction": not conflicting,
    }
    result = dict(candidate)
    result["authority_validation"] = {**checks, "result": "VALID" if all(checks.values()) else "INVALID"}
    if conflicting:
        result["status"] = AssemblyStatus.CONTRADICTORY.value
    elif all(checks.values()):
        result["origin"] = FieldOrigin.AUTHORITATIVE_SOURCE.value
        result["status"] = AssemblyStatus.AUTHORITATIVE.value
    else:
        result["status"] = AssemblyStatus.UNVERIFIED.value
    return result


def authority_conflict(candidates: list[dict[str, Any]]) -> bool:
    values = {c.get("value") for c in candidates if c.get("status") == AssemblyStatus.AUTHORITATIVE.value}
    return len(values) > 1
