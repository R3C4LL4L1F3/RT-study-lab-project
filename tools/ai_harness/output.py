from __future__ import annotations

from pathlib import Path
from typing import Any
from .canonical import canonical_bytes


def write_outputs(result: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    evaluation_path = output_dir / "evaluation.json"
    audit_path = output_dir / "audit.json"
    evaluation = {k: v for k, v in result.items() if k != "audit_record"}
    evaluation_path.write_bytes(canonical_bytes(evaluation) + b"\n")
    audit_path.write_bytes(canonical_bytes(result["audit_record"]) + b"\n")
    return evaluation_path, audit_path


def human_summary(result: dict[str, Any]) -> str:
    rec = result["recommendation"]
    return f"status={result['deterministic_status']} transition={rec.get('requested_transition')} permitted={str(rec.get('requested_transition_permitted')).lower()} recheck={str(result['final_policy_recheck']['passed']).lower()}"
