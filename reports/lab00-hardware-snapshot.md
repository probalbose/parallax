# Lab 00 — Hardware and Process Observer

## Environment

- Hardware: Apple Silicon MacBook
- Operating system: macOS
- Python: 3.13.3
- Rust: 1.96.0
- Commit: `ad6eee8`
- Rust build mode: release

## Method

- Ran the Python and Rust hardware observers three times using
  `python scripts/compare_snapshots.py`.
- Verified the shared JSON output contract.
- Ran Ruff, Pytest, Rustfmt, Clippy, and Rust tests before collecting results.
- Kept the system as quiet as practical; no deliberate load was applied.

## Results

| Metric | Python | Rust | Notes |
| --- | ---: | ---: | --- |
| Logical CPUs | 14 | 14 | Identical in all runs |
| Total memory | 38,654,705,664 bytes | 38,654,705,664 bytes | Identical in all runs |
| Process RSS, mean | 20.4 MB | 10.7 MB | Mean across three samples |
| Observer elapsed time | 0 ms | 11.3 ms | Not directly comparable |
| Free disk space | ~436.36 GB | ~436.36 GB | Live-system measurement |

## Interpretation

The implementations agreed on the stable machine facts: 14 logical CPUs and
38,654,705,664 bytes of total memory. Rust used approximately 10.7 MB RSS,
compared with approximately 20.4 MB for Python across three samples. This is a
small observer-process result, not evidence that Rust will necessarily use less
memory for a long-running training workload.

The elapsed-time field is not comparable in this baseline. Python rounds its
sub-millisecond collection time down to zero, while Rust includes a `df`
subprocess when obtaining free disk space. A later lab should measure complete
process startup externally, with higher-resolution timing and equivalent work.

Available-memory values are not directly comparable on macOS: Python's `psutil`
and Rust's `sysinfo` apply different memory-accounting definitions. The small
free-disk differences are expected because the OS changes while each observer
runs.

## Conclusion

Lab 00 establishes a working shared measurement contract. Future labs will use
the same discipline: identical inputs, release-mode Rust benchmarks, repeated
runs, and careful separation of language effects from backend or OS effects.
