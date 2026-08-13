// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 Probal Bose

use std::process::Command;

#[test]
fn snapshot_matches_lab00_contract() {
    let output = Command::new(env!("CARGO_BIN_EXE_hardware_snapshot"))
        .output()
        .expect("run snapshot");
    assert!(output.status.success());
    let value: serde_json::Value = serde_json::from_slice(&output.stdout).expect("parse JSON");
    assert_eq!(value["language"], "rust");
    assert!(value["logical_cpus"].as_u64().unwrap() >= 1);
    assert!(value["total_memory_bytes"].as_u64().unwrap() > 0);
    assert!(value["process_memory_bytes"].as_u64().unwrap() > 0);
    assert!(value["disk_free_bytes"].as_u64().unwrap() > 0);
}
