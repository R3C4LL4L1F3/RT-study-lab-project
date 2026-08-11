from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schema import AssemblyStatus, FieldOrigin, field

GATE_OWNERS = {
    "CLINICAL_EVIDENCE": "CLINICAL_VALIDATION_SOURCES",
    "ARCHITECTURE": "PLANNING_ARCHITECTURE",
    "IMPLEMENTATION": "PLANNING_ARCHITECTURE",
    "INDEPENDENT_REVIEW": "QA_REGRESSION_RELEASE",
    "QA": "QA_REGRESSION_RELEASE",
    "GITHUB_PROVENANCE": "GITHUB_PR_DOCUMENTATION",
    "RELEASE": "MASTER_PROJECT_CONTROL",
}


def derive_gates(
    fields: dict[str, dict[str, Any]],
    *,
    repo_root: Path,
    governance_profile: str | None = None,
) -> dict[str, Any]:
    risk = fields.get("risk_tier", {})
    risk_value = risk.get("value")
    gates_config = json.loads((repo_root / "config" / "ai_harness" / "gates.v1.json").read_text(encoding="utf-8"))
    autonomy = json.loads((repo_root / "config" / "ai_harness" / "autonomy.v1.json").read_text(encoding="utf-8"))
    controlled = governance_profile == autonomy.get("profile_id")
    required = gates_config.get("risk_minimum_required_gates", {}).get(risk_value, [])
    independent = fields.get("independent_review_requirement", {})
    conditional_not_required = bool(
        controlled
        and risk_value == "TIER_2"
        and independent.get("status") == AssemblyStatus.AUTHORITATIVE.value
        and independent.get("value") is False
    )
    if controlled and risk_value == "TIER_2" and independent.get("status") == AssemblyStatus.AUTHORITATIVE.value:
        required = list(autonomy.get("tier_2_minimum_required_gates_when_controlled", []))
        if independent.get("value") is True:
            required.append("INDEPENDENT_REVIEW")
        elif conditional_not_required:
            required.append("INDEPENDENT_REVIEW")
    elif controlled and risk_value == "TIER_3":
        required = list(autonomy.get("tier_3_minimum_required_gates_when_controlled", []))
    authoritative = risk.get("status") == AssemblyStatus.AUTHORITATIVE.value
    status = AssemblyStatus.DETERMINISTICALLY_DERIVED.value if authoritative else AssemblyStatus.PROPOSED.value
    gates = []
    for gate_id in required:
        is_conditional_not_required = conditional_not_required and gate_id == "INDEPENDENT_REVIEW"
        gate = {
            "gate_id": gate_id,
            "obligation": field(
                not is_conditional_not_required,
                origin=FieldOrigin.DETERMINISTIC_DERIVATION,
                status=status,
                derivation_rule_ids=[f"GATE-{risk_value}-REQUIRED"],
                **({
                    "condition": {
                        "type": "CONDITIONAL_CONTRACT",
                        "ref": independent.get("contract_ref"),
                        "authority_role": "MASTER_PROJECT_CONTROL",
                    }
                } if is_conditional_not_required else {}),
            ),
            "execution": {"state": "NOT_REQUIRED" if is_conditional_not_required else "REQUIRED_PENDING"},
            "authority": {"owner_role": GATE_OWNERS[gate_id]},
            "disposition": {"decision": None, "actor": None, "evidence_refs": []},
        }
        gates.append(gate)
    return {
        "status": status if risk_value else AssemblyStatus.MISSING.value,
        "risk_input": risk_value,
        "governance_profile": governance_profile or "CURRENT_KERNEL",
        "gates": gates,
        "fail_closed": not authoritative,
    }
