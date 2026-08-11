from __future__ import annotations

from typing import Any


def human_readable_projection(assembled: dict[str, Any]) -> str:
    lines = ["RTSL-AIH-004 TASK ASSEMBLY", ""]
    for name in sorted(assembled.get("assembled_fields", {})):
        value = assembled["assembled_fields"][name]
        lines.extend([name.upper(), f"Value: {value.get('value')}", f"Origin: {value.get('origin')}", f"Status: {value.get('status')}"])
        if value.get("authority_role"):
            lines.append(f"Authority: {value['authority_role']}")
        evidence = value.get("evidence")
        if isinstance(evidence, dict):
            lines.append(f"AIH-002 evidence state: {evidence.get('original_evidence_state')}")
            if evidence.get("collection_completeness") is not None:
                lines.append(f"Collection completeness: {evidence['collection_completeness']}")
        lines.append("")
    lines.append("ROUTING CANDIDATES")
    for name in ("subsystem_candidate", "owner_candidate"):
        candidate = assembled.get("routing", {}).get(name, {})
        lines.append(f"{name}: {candidate.get('value')} ({candidate.get('status')})")
    lines.extend(["", "GATES"])
    for gate in assembled.get("gates", {}).get("gates", []):
        lines.append(f"{gate['gate_id']}: required, pending")
    if not assembled.get("gates", {}).get("gates"):
        lines.append("None derived")
    lines.extend(["", "MISSING CONTEXT"])
    missing = assembled.get("missing_context", [])
    if missing:
        lines.extend(f"- {item['field']}: {item['category']}" for item in missing)
    else:
        lines.append("None")
    return "\n".join(lines)
