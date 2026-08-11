from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..canonical import CANONICAL_PROFILE, sha256_hex
from .human import human_readable_projection


def build_output(assembled: dict[str, Any], *, run_id: str | None = None) -> dict[str, Any]:
    assembled = dict(assembled)
    assembled["human_readable_projection"] = human_readable_projection(assembled)
    canonical_payload = {k: v for k, v in assembled.items() if k not in {"run_metadata", "deterministic_hash", "human_readable_projection"}}
    return {
        "assembled_task_snapshot": {
            "snapshot_schema_version": "1",
            "canonical_payload": canonical_payload,
            "human_readable_projection": assembled["human_readable_projection"],
            "deterministic_hash": {
                "algorithm": "SHA-256",
                "canonicalization_profile": CANONICAL_PROFILE,
                "value": sha256_hex(canonical_payload),
            },
            "run_metadata": {
                "run_id": run_id or "",
                "execution_started_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            },
        }
    }
