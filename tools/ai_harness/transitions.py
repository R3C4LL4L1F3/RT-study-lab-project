from __future__ import annotations

from typing import Any

TERMINAL_STATES = {"COMPLETE", "REJECTED", "CANCELLED"}


def allowed_targets(current: str, matrix: dict[str, Any]) -> set[str]:
    return set(matrix["transitions"].get(current, []))


def previous_state_provenance_valid(task: dict[str, Any], matrix: dict[str, Any]) -> bool:
    current = task["work_state"]
    if current not in {"PAUSED", "BLOCKED"}:
        return True
    record = task.get("pause") if current == "PAUSED" else task.get("blocker")
    previous = (record or {}).get("previous_state")
    if not isinstance(previous, str) or previous not in matrix["transitions"]:
        return False
    return current in allowed_targets(previous, matrix)


def transition_enumerated(
    task: dict[str, Any],
    target: str,
    matrix: dict[str, Any],
    *,
    allow_bounded_completion: bool = False,
) -> bool:
    current = task["work_state"]
    if current in {"PAUSED", "BLOCKED"}:
        record = task.get("pause") if current == "PAUSED" else task.get("blocker")
        previous = (record or {}).get("previous_state")
        if target == previous:
            return previous_state_provenance_valid(task, matrix)
    if (
        allow_bounded_completion
        and current == "IN_VALIDATION"
        and target == "COMPLETE"
        and task.get("completion_scope", "BOUNDED_TASK") == "BOUNDED_TASK"
    ):
        release_gate = next((g for g in task.get("gates", []) if g.get("gate_id") == "RELEASE"), None)
        return not bool(release_gate and (release_gate.get("obligation") or {}).get("required"))
    return target in allowed_targets(current, matrix)


def _evidence_present(values: Any) -> bool:
    return isinstance(values, list) and bool(values) and all(isinstance(v, str) and v.strip() for v in values)


def resume_target_valid(task: dict[str, Any], target: str, matrix: dict[str, Any]) -> bool:
    current = task["work_state"]
    if current == "PAUSED":
        pause = task.get("pause") or {}
        previous = pause.get("previous_state")
        if target != previous:
            return target in {"BLOCKED", "CANCELLED"}
        return (
            previous_state_provenance_valid(task, matrix)
            and pause.get("resume_condition_satisfied") is True
            and _evidence_present(pause.get("resume_evidence_refs"))
        )
    if current == "BLOCKED":
        blocker = task.get("blocker") or {}
        previous = blocker.get("previous_state")
        if target != previous:
            return target in {"PAUSED", "CANCELLED"}
        return (
            previous_state_provenance_valid(task, matrix)
            and blocker.get("unblock_condition_satisfied") is True
            and _evidence_present(blocker.get("unblock_evidence_refs"))
        )
    return True
