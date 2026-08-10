from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from typing import Any

CANONICAL_PROFILE = "RTSL-CANONICAL-RECORD-1"


def _normalize_timestamp(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        raise ValueError("timestamp must include an explicit UTC offset")
    dt = dt.astimezone(timezone.utc).replace(microsecond=0)
    return dt.isoformat().replace("+00:00", "Z")


def normalize(value: Any, *, key: str | None = None) -> Any:
    """Normalize JSON-compatible data for deterministic serialization."""
    if isinstance(value, dict):
        return {
            str(k): normalize(v, key=str(k))
            for k, v in sorted(value.items(), key=lambda item: str(item[0]))
        }
    if isinstance(value, list):
        return [normalize(v) for v in value]
    if isinstance(value, tuple):
        return [normalize(v) for v in value]
    if isinstance(value, bool) or value is None or isinstance(value, (int, str)):
        if isinstance(value, str) and key and (
            key.endswith("_at") or key in {"timestamp", "evaluated_at"}
        ) and value:
            return _normalize_timestamp(value)
        return value
    if isinstance(value, float):
        if not value.is_integer():
            raise TypeError("RTSL-CANONICAL-RECORD-1 V0 permits integers, not floats")
        return int(value)
    raise TypeError(f"unsupported canonical value type: {type(value).__name__}")


def canonical_bytes(value: Any) -> bytes:
    normalized = normalize(value)
    return json.dumps(
        normalized,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256_hex(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()
