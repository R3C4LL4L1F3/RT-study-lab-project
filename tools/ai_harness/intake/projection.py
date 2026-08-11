from __future__ import annotations

from typing import Any

from .schema import AssemblyStatus

AUTHORITATIVE_FIELDS = ("task_id", "title", "priority", "risk_tier", "work_state")


def safe_v0_projection(assembled: dict[str, Any]) -> dict[str, Any]:
    """Project only validated authoritative governance fields; proposals stay outside V0."""
    fields = assembled.get("assembled_fields", {})
    projection: dict[str, Any] = {}
    blocked: list[str] = []
    for name in AUTHORITATIVE_FIELDS:
        envelope = fields.get(name)
        if not isinstance(envelope, dict) or envelope.get("status") != AssemblyStatus.AUTHORITATIVE.value:
            if name in {"priority", "risk_tier", "work_state"}:
                blocked.append(name)
            continue
        projection[name] = envelope.get("value")
    gates = assembled.get("gates", {})
    if gates.get("status") == AssemblyStatus.DETERMINISTICALLY_DERIVED.value:
        projection["gates"] = gates.get("gates", [])
    return {
        "task": projection,
        "projection_status": "READY" if not blocked else "INCOMPLETE",
        "blocked_authority_fields": blocked,
        "fail_closed": bool(blocked),
    }
