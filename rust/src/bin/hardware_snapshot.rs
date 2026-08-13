// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 Probal Bose

use serde::Serialize;
use std::{env, error::Error, process::Command, time::Instant};
use sysinfo::System;

#[derive(Debug, Serialize)]
struct HardwareSnapshot {
    language: &'static str,
    logical_cpus: usize,
    total_memory_bytes: u64,
    available_memory_bytes: u64,
    process_memory_bytes: u64,
    disk_free_bytes: u64,
    elapsed_ms: u128,
}

fn free_disk_bytes() -> Result<u64, Box<dyn Error>> {
    let cwd = env::current_dir()?;
    let output = Command::new("df").arg("-kP").arg(cwd).output()?;
    if !output.status.success() {
        return Err("df failed".into());
    }
    let line = String::from_utf8(output.stdout)?
        .lines()
        .nth(1)
        .ok_or("missing df output")?
        .to_owned();
    let fields: Vec<&str> = line.split_whitespace().collect();
    let available_kib: u64 = fields
        .get(3)
        .ok_or("missing available disk field")?
        .parse()?;
    Ok(available_kib * 1024)
}

fn main() -> Result<(), Box<dyn Error>> {
    let started = Instant::now();
    let mut system = System::new_all();
    system.refresh_all();
    let current_pid = sysinfo::get_current_pid()?;
    let process_memory_bytes = system
        .process(current_pid)
        .map(|process| process.memory())
        .unwrap_or_default();
    let snapshot = HardwareSnapshot {
        language: "rust",
        logical_cpus: system.cpus().len().max(1),
        total_memory_bytes: system.total_memory(),
        available_memory_bytes: system.available_memory().max(system.free_memory()),
        process_memory_bytes,
        disk_free_bytes: free_disk_bytes()?,
        elapsed_ms: started.elapsed().as_millis(),
    };
    println!("{}", serde_json::to_string(&snapshot)?);
    Ok(())
}
