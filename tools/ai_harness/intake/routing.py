from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schema import AssemblyStatus, FieldOrigin, field


def load_routing_rules(repo_root: Path) -> list[dict[str, Any]]:
    path = repo_root / "config" / "ai_harness" / "intake-routing.v1.json"
    return json.loads(path.read_text(encoding="utf-8"))["routing_rules"]


def derive_routing(task: dict[str, Any], *, repo_root: Path) -> dict[str, dict[str, Any]]:
    text = " ".join(str(task.get(name, {}).get("value", "")) for name in ("title", "description", "requested_outcome")).lower()
    for rule in load_routing_rules(repo_root):
        if all(term.lower() in text for term in rule.get("terms", [])):
            return {
                "subsystem_candidate": field(rule["candidate_subsystem"], origin=FieldOrigin.DETERMINISTIC_DERIVATION, status=AssemblyStatus.PROPOSED, derivation_rule_ids=[rule["rule_id"]]),
                "owner_candidate": field(rule["candidate_owner"], origin=FieldOrigin.DETERMINISTIC_DERIVATION, status=AssemblyStatus.PROPOSED, derivation_rule_ids=[rule["rule_id"]]),
            }
    return {
        "subsystem_candidate": field(None, status=AssemblyStatus.MISSING),
        "owner_candidate": field(None, status=AssemblyStatus.MISSING),
    }
