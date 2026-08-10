from __future__ import annotations

from pathlib import Path
from typing import Any
from .canonical import canonical_bytes


def _exclusive_write(path: Path, payload: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(payload)
        handle.write(b"\n")


def write_outputs(result: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    evaluation_path = output_dir / "evaluation.json"
    audit_path = output_dir / "audit.json"
    if evaluation_path.exists() or audit_path.exists():
        raise FileExistsError("refusing to overwrite existing harness output")
    evaluation = {k: v for k, v in result.items() if k != "audit_record"}
    created: list[Path] = []
    try:
        _exclusive_write(evaluation_path, canonical_bytes(evaluation))
        created.append(evaluation_path)
        _exclusive_write(audit_path, canonical_bytes(result["audit_record"]))
        created.append(audit_path)
    except Exception:
        for path in created:
            path.unlink(missing_ok=True)
        raise
    return evaluation_path, audit_path


def human_summary(result: dict[str, Any]) -> str:
    rec = result["recommendation"]
    return f"status={result['deterministic_status']} transition={rec.get('requested_transition')} permitted={str(rec.get('requested_transition_permitted')).lower()} recheck={str(result['final_policy_recheck']['passed']).lower()}"
