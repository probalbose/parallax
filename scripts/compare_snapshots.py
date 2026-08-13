# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Probal Bose

"""Run both Lab 00 implementations, validate the shared JSON contract, and record results."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"language", "logical_cpus", "total_memory_bytes", "available_memory_bytes", "process_memory_bytes", "disk_free_bytes", "elapsed_ms"}


def run(command: list[str]) -> dict[str, Any]:
    completed = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(completed.stdout)


def validate(record: dict[str, Any], language: str) -> None:
    if set(record) != REQUIRED:
        raise ValueError(f"expected exactly {sorted(REQUIRED)}, got {sorted(record)}")
    if record["language"] != language:
        raise ValueError(f"expected language {language}, got {record['language']}")
    for name in REQUIRED - {"language"}:
        if not isinstance(record[name], int) or isinstance(record[name], bool) or record[name] < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    for name in ("logical_cpus", "total_memory_bytes", "process_memory_bytes", "disk_free_bytes"):
        if record[name] <= 0:
            raise ValueError(f"{name} must be positive")


def git_commit() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def append_result(record: dict[str, Any], commit: str) -> None:
    fields = ["run_id", "git_commit", "language", "logical_cpus", "total_memory_bytes", "available_memory_bytes", "process_memory_bytes", "disk_free_bytes", "elapsed_ms"]
    with (ROOT / "experiments" / "results.csv").open("a", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields).writerow({"run_id": f"lab00-{record['language']}", "git_commit": commit, **record})


def main() -> int:
    try:
        python = run([sys.executable, "python/src/parallax_lab/hardware_snapshot.py"])
        rust = run(["cargo", "run", "--quiet", "--manifest-path", "rust/Cargo.toml", "--release", "--bin", "hardware_snapshot"])
        validate(python, "python")
        validate(rust, "rust")
        commit = git_commit()
        for record in (python, rust):
            append_result(record, commit)
        print(f"{'Metric':<25}{'Python':>18}{'Rust':>18}")
        for field in ("elapsed_ms", "process_memory_bytes", "logical_cpus", "total_memory_bytes", "disk_free_bytes"):
            print(f"{field:<25}{python[field]:>18}{rust[field]:>18}")
    except (OSError, subprocess.CalledProcessError, ValueError, json.JSONDecodeError) as error:
        print(f"comparison failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
