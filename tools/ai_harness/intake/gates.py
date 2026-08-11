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


def derive_gates(fields: dict[str, dict[str, Any]], *, repo_root: Path) -> dict[str, Any]:
    risk = fields.get("risk_tier", {})
    risk_value = risk.get("value")
    required = json.loads((repo_root / "config" / "ai_harness" / "gates.v1.json").read_text(encoding="utf-8")).get("risk_minimum_required_gates", {}).get(risk_value, [])
    authoritative = risk.get("status") == AssemblyStatus.AUTHORITATIVE.value
    status = AssemblyStatus.DETERMINISTICALLY_DERIVED.value if authoritative else AssemblyStatus.PROPOSED.value
    gates = []
    for gate_id in required:
        gates.append({
            "gate_id": gate_id,
            "obligation": field(True, origin=FieldOrigin.DETERMINISTIC_DERIVATION, status=status, derivation_rule_ids=[f"GATE-{risk_value}-REQUIRED"]),
            "execution": {"state": "REQUIRED_PENDING"},
            "authority": {"owner_role": GATE_OWNERS[gate_id]},
            "disposition": {"decision": None, "actor": None, "evidence_refs": []},
        })
    return {"status": status if risk_value else AssemblyStatus.MISSING.value, "risk_input": risk_value, "gates": gates, "fail_closed": not authoritative}
