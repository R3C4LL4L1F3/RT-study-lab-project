from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from .audit import build_audit_record
from .canonical import sha256_hex
from .policy import classify_status, evaluate_rules, final_policy_recheck, transition_permitted
from .schemas import load_config, validate_task


def _next_action(task: dict[str, Any], status: str, allowed: bool) -> str:
    target = task.get("requested_transition")
    if not target:
        return "No state transition requested; review deterministic findings."
    if allowed:
        return f"Transition to {target} is deterministically legal for the supplied snapshot; human/project authority still applies."
    if status == "CONTRADICTORY":
        return "Resolve contradictory authoritative facts before any advancement."
    if status == "INCOMPLETE":
        return "Satisfy missing mandatory evidence/gates/identity before advancement."
    return "Correct invalid record or prohibited transition before advancement."


def evaluate_snapshot(raw: dict[str, Any], *, repo_root: Path, corrupt_candidate_for_test: bool = False) -> dict[str, Any]:
    config = load_config(repo_root)
    task = validate_task(deepcopy(raw), config)
    input_hash = sha256_hex(task)
    rules = evaluate_rules(task, config)
    status = classify_status(rules)
    allowed = transition_permitted(task, rules)
    recommendation = {
        "deterministic_status": status,
        "requested_transition": task.get("requested_transition"),
        "requested_transition_permitted": allowed,
        "next_action": _next_action(task, status, allowed),
    }
    if corrupt_candidate_for_test:
        recommendation["requested_transition_permitted"] = True
    fresh_rules = evaluate_rules(task, config)
    recheck_passed, recheck_problems = final_policy_recheck(task, recommendation, rules, fresh_rules)
    deterministic_payload = {
        "task_id": task["task_id"], "policy_profile": "RTSL-AIH-V0-POLICY-1", "schema_version": "1",
        "kernel": task["kernel"], "rules": rules, "recommendation": recommendation,
    }
    deterministic_hash = sha256_hex(deterministic_payload)
    findings_hash = sha256_hex(rules)
    audit = build_audit_record(task=task, input_hash=input_hash, rule_results=rules, recommendation=recommendation, deterministic_hash=deterministic_hash, findings_hash=findings_hash, recheck_passed=recheck_passed, recheck_problems=recheck_problems)
    return {
        "schema_version": "1", "policy_profile": "RTSL-AIH-V0-POLICY-1", "serialization_profile": "RTSL-CANONICAL-RECORD-1",
        "input_sha256": input_hash, "deterministic_findings_sha256": findings_hash, "deterministic_result_sha256": deterministic_hash, "deterministic_status": status,
        "deterministic_findings": rules, "recommendation": recommendation, "final_policy_recheck": audit["final_policy_recheck"], "audit_record": audit,
    }
