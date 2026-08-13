# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Probal Bose

"""Emit the Lab 00 hardware snapshot JSON contract."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from time import perf_counter_ns

import psutil


def snapshot() -> dict[str, int | str]:
    """Collect an OS-level snapshot using the shared Lab 00 field names."""
    started_ns = perf_counter_ns()
    memory = psutil.virtual_memory()
    process = psutil.Process()
    disk = shutil.disk_usage(Path.cwd())
    return {
        "language": "python",
        "logical_cpus": psutil.cpu_count(logical=True) or 1,
        "total_memory_bytes": memory.total,
        "available_memory_bytes": memory.available,
        "process_memory_bytes": process.memory_info().rss,
        "disk_free_bytes": disk.free,
        "elapsed_ms": (perf_counter_ns() - started_ns) // 1_000_000,
    }


def main() -> int:
    try:
        print(json.dumps(snapshot(), separators=(",", ":")))
    except OSError as error:  # pragma: no cover - defensive command boundary
        print(f"hardware snapshot failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
