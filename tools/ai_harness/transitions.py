from __future__ import annotations

from typing import Any

TERMINAL_STATES = {"COMPLETE", "REJECTED", "CANCELLED"}


def allowed_targets(current: str, matrix: dict[str, Any]) -> set[str]:
    targets = set(matrix["transitions"].get(current, []))
    return targets


def transition_enumerated(task: dict[str, Any], target: str, matrix: dict[str, Any]) -> bool:
    current = task["work_state"]
    if current == "PAUSED":
        previous = (task.get("pause") or {}).get("previous_state")
        return target == previous or target in set(matrix["transitions"].get("PAUSED", []))
    if current == "BLOCKED":
        previous = (task.get("blocker") or {}).get("previous_state")
        return target == previous or target in set(matrix["transitions"].get("BLOCKED", []))
    return target in allowed_targets(current, matrix)


def resume_target_valid(task: dict[str, Any], target: str) -> bool:
    current = task["work_state"]
    if current == "PAUSED":
        previous = (task.get("pause") or {}).get("previous_state")
        return target == previous or target in {"BLOCKED", "CANCELLED"}
    if current == "BLOCKED":
        previous = (task.get("blocker") or {}).get("previous_state")
        return target == previous or target in {"PAUSED", "CANCELLED"}
    return True
