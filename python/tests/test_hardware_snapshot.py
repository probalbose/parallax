# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Probal Bose

from parallax_lab.hardware_snapshot import snapshot


def test_snapshot_matches_lab00_contract() -> None:
    result = snapshot()
    assert result["language"] == "python"
    assert result["logical_cpus"] >= 1
    for field in ("total_memory_bytes", "process_memory_bytes", "disk_free_bytes"):
        assert result[field] > 0
    assert result["available_memory_bytes"] >= 0
    assert result["elapsed_ms"] >= 0
