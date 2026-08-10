from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .errors import SchemaError, UnknownKernelError
from .evaluator import evaluate_snapshot
from .output import human_summary, write_outputs

EXIT_OK = 0
EXIT_INVALID = 2
EXIT_CONTRADICTORY = 3
EXIT_UNKNOWN_KERNEL = 4
EXIT_POLICY_RECHECK = 5
EXIT_INTERNAL = 6


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rt-study-ai-harness")
    sub = parser.add_subparsers(dest="command", required=True)
    evaluate = sub.add_parser("evaluate", help="evaluate one local task JSON snapshot")
    evaluate.add_argument("input", type=Path)
    evaluate.add_argument("--output-dir", type=Path, required=True, help="explicit harness output directory")
    return parser


def run(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        input_path = args.input.resolve()
        output_dir = args.output_dir.resolve()
        output_targets = {(output_dir / "evaluation.json").resolve(), (output_dir / "audit.json").resolve()}
        if input_path in output_targets:
            raise SchemaError("output directory would overwrite the supplied task input")
        raw = json.loads(input_path.read_text(encoding="utf-8"))
        result = evaluate_snapshot(raw, repo_root=_repo_root())
        if not result["final_policy_recheck"]["passed"]:
            print("INTERNAL_POLICY_RECHECK_FAILURE", file=sys.stderr)
            return EXIT_POLICY_RECHECK
        write_outputs(result, output_dir)
        print(human_summary(result))
        return EXIT_CONTRADICTORY if result["deterministic_status"] == "CONTRADICTORY" else EXIT_OK
    except UnknownKernelError as exc:
        print(f"AUTHORITATIVE_EVALUATION_REFUSED: {exc}", file=sys.stderr)
        return EXIT_UNKNOWN_KERNEL
    except (SchemaError, json.JSONDecodeError, OSError, ValueError, TypeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return EXIT_INVALID
    except Exception as exc:
        print(f"INTERNAL_ERROR: {exc}", file=sys.stderr)
        return EXIT_INTERNAL
