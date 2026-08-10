from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from .canonical import sha256_hex


def build_audit_record(*, task: dict[str, Any], input_hash: str, rule_results: list[dict[str, str]], recommendation: dict[str, Any], deterministic_hash: str, findings_hash: str, recheck_passed: bool, recheck_problems: list[str]) -> dict[str, Any]:
    evaluated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    run_id = "AIH-RUN-" + sha256_hex({"input_sha256": input_hash, "policy_profile": "RTSL-AIH-V0-POLICY-1", "schema_version": "1", "evaluated_at": evaluated_at})[:16].upper()
    record = {
        "harness_run_id": run_id,
        "harness_version": "0.1",
        "schema_version": "1",
        "policy_profile": "RTSL-AIH-V0-POLICY-1",
        "kernel_version_ref": task["kernel"]["version_ref"],
        "evaluated_at": evaluated_at,
        "input": {"serialization_profile": "RTSL-CANONICAL-RECORD-1", "hash_algorithm": "SHA-256", "sha256": input_hash},
        "deterministic_rules_evaluated": [r["rule_id"] for r in rule_results],
        "deterministic_findings": rule_results,
        "deterministic_findings_sha256": findings_hash,
        "initial_evaluation_status": recommendation["deterministic_status"],
        "final_policy_recheck": {"performed": True, "passed": recheck_passed, "findings_hash": findings_hash, "problems": recheck_problems},
        "recommendation": recommendation,
        "output": {"serialization_profile": "RTSL-CANONICAL-RECORD-1", "hash_algorithm": "SHA-256", "sha256": deterministic_hash},
    }
    record["audit_content_sha256"] = sha256_hex(record)
    return record
