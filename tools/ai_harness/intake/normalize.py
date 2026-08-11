from __future__ import annotations

import re
from typing import Any

from ..schemas import WorkState
from .schema import AssemblyStatus, FieldOrigin, field


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def normalize_work_state(value: Any) -> str | None:
    if value is None:
        return None
    text = normalize_text(str(value)).upper().replace("-", "_").replace(" ", "_")
    aliases = {"INPROGRESS": "IN_PROGRESS", "IN_VALIDATION": "IN_VALIDATION", "READYFORRELEASE": "READY_FOR_RELEASE"}
    text = aliases.get(text, text)
    try:
        return WorkState(text).value
    except ValueError:
        return None


def normalize_field(value: dict[str, Any], *, name: str) -> dict[str, Any]:
    result = dict(value)
    if isinstance(result.get("value"), str) and name not in {"work_state", "risk_tier", "priority"}:
        result["value"] = normalize_text(result["value"])
    if name == "work_state":
        result["value"] = normalize_work_state(result.get("value"))
    result.setdefault("origin", FieldOrigin.USER_SUPPLIED.value)
    result.setdefault("status", AssemblyStatus.UNVERIFIED.value)
    if result.get("origin") == FieldOrigin.USER_SUPPLIED.value and result.get("status") == AssemblyStatus.AUTHORITATIVE.value:
        result["status"] = AssemblyStatus.PROPOSED.value
    if result.get("value") is not None and result.get("status") == AssemblyStatus.UNVERIFIED.value:
        result["derivation_rule_ids"] = list(result.get("derivation_rule_ids", []))
    return result
