from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Sequence

from ..github_readonly.provider import EvidenceRecord, EvidenceRequest, Operation, validate_content_path
from .authority import authority_conflict, validate_authoritative_field
from .normalize import normalize_field, normalize_text
from .output import build_output
from .projection import safe_v0_projection
from .provenance import evidence_snapshot
from .routing import derive_routing
from .schema import AssemblyStatus, FieldOrigin, field, validate_intake_request


def build_github_content_requests(raw: dict[str, Any]) -> list[EvidenceRequest]:
    """Create only explicit AIH-002 requests; this function performs no network I/O."""
    requests: list[EvidenceRequest] = []
    for item in raw.get("references", {}).get("github_content_requests", []):
        if "*" in item["path"]:
            raise ValueError("wildcard or recursive content paths are prohibited")
        validate_content_path(item["path"])
        requests.append(EvidenceRequest(item["repository_alias"], Operation.CONTENT_GET, item.get("requested_fact", item["path"]), ref=item["ref"], path=item["path"]))
    return requests


def _claim_fields(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    task = raw.get("task", {})
    for name in ("task_id", "title", "description", "requested_outcome"):
        if name in task:
            result[name] = normalize_field(task[name], name=name)
    for name, value in raw.get("governance_claims", {}).items():
        result[name] = normalize_field(value, name=name)
    return result


def _authoritative_facts(raw: dict[str, Any], fields: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    facts = raw.get("authoritative_facts", [])
    if not isinstance(facts, list):
        return []
    by_field: dict[str, list[dict[str, Any]]] = {}
    for candidate in facts:
        if not isinstance(candidate, dict) or not isinstance(candidate.get("field"), str):
            continue
        by_field.setdefault(candidate["field"], []).append(candidate)
    for name, candidates in by_field.items():
        conflict = authority_conflict([validate_authoritative_field(name, c) for c in candidates])
        chosen = validate_authoritative_field(name, candidates[0], conflicting=conflict)
        fields[name] = chosen
    return facts


def _missing(fields: dict[str, dict[str, Any]], raw: dict[str, Any]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    if not fields.get("task_id", {}).get("value") or not fields.get("title", {}).get("value"):
        result.append({"field": "task_id/title", "category": "MISSING_IDENTITY"})
    for name, category in (("priority", "MISSING_AUTHORITATIVE_PRIORITY"), ("risk_tier", "MISSING_AUTHORITATIVE_RISK"), ("work_state", "MISSING_WORK_STATE")):
        if fields.get(name, {}).get("status") != AssemblyStatus.AUTHORITATIVE.value:
            result.append({"field": name, "category": category})
    risk = fields.get("risk_tier", {})
    if risk.get("value") in {"TIER_2", "TIER_3"} and fields.get("clinical_disposition", {}).get("status") != AssemblyStatus.AUTHORITATIVE.value:
        result.append({"field": "clinical_disposition", "category": "MISSING_CLINICAL_AUTHORITY"})
    state = fields.get("work_state", {}).get("value")
    contract = raw.get("pause") if state == "PAUSED" else raw.get("blocker") if state == "BLOCKED" else None
    if state in {"PAUSED", "BLOCKED"} and not isinstance(contract, dict):
        result.append({"field": "pause/blocker", "category": "MISSING_PAUSE_CONTRACT" if state == "PAUSED" else "MISSING_BLOCKER_CONTRACT"})
    return result


def assemble_intake(raw: dict[str, Any], *, repo_root: Path, evidence: Sequence[EvidenceRecord] = ()) -> dict[str, Any]:
    validate_intake_request(raw)
    normalized = deepcopy(raw)
    fields = _claim_fields(normalized)
    _authoritative_facts(normalized, fields)
    routing = derive_routing(fields, repo_root=repo_root)
    refs = normalized.get("references", {})
    issue_refs = [{"value": n, "semantic_role": "PROVENANCE_IDENTIFIER", "retrieval_authorized": False} for n in refs.get("issue_numbers", [])]
    evidence_items = evidence_snapshot(evidence)
    for item in evidence_items:
        if item["collection_completeness"] is None:
            continue
    assembled = {
        "intake_schema_version": "1",
        "assembled_fields": fields,
        "routing": routing,
        "references": {
            "issue_numbers": issue_refs,
            "pull_request_numbers": refs.get("pull_request_numbers", []),
            "commit_shas": refs.get("commit_shas", []),
            "source_refs": refs.get("source_refs", refs.get("document_refs", [])),
            "github_content_requests": [dict(x) for x in refs.get("github_content_requests", [])],
        },
        "evidence_snapshot": evidence_items,
        "missing_context": _missing(fields, normalized),
        "contradictions": [name for name, value in fields.items() if value.get("status") == AssemblyStatus.CONTRADICTORY.value],
        "proposals": {name: value for name, value in {**fields, **routing}.items() if value.get("status") == AssemblyStatus.PROPOSED.value},
        "configuration": {
            "assembler_version": "RTSL-AIH-004-V1.1",
            "routing_registry_version": "RTSL-AIH-004-ROUTING-1",
            "policy_profile_version": "RTSL-AIH-V0-POLICY-1",
            "canonicalization_profile": "RTSL-CANONICAL-RECORD-1",
        },
    }
    assembled["v0_projection"] = safe_v0_projection(assembled)
    return build_output(assembled)
