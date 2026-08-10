from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_fixture(category: str, name: str):
    return json.loads((FIXTURES / category / name).read_text(encoding="utf-8"))


def base_task():
    return load_fixture("valid", "FIX-001-valid-tier1.json")
