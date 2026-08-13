# Contributing to Parallax

Thank you for helping make LLM systems measurements more useful and less
misleading. Small, focused changes are easiest to review and release.

## Before you start

Open an issue for a new lab, a substantial design change, or an unfamiliar
dependency. Check the [roadmap](ROADMAP.md) first; each lab has an intended
scope and evidence standard.

By contributing, you agree that code contributions are licensed under
Apache-2.0. Do not contribute model weights, adapters, tokenizers, secrets,
private data, or material you do not have the right to publish.

## Development

Use Python 3.11+ and stable Rust. Keep the Python and Rust implementations
independently runnable. The commands used in CI are:

```bash
python -m pip install -e "./python[dev]"
python -m pytest python/tests
python -m ruff check python scripts
cargo fmt --manifest-path rust/Cargo.toml --check
cargo clippy --manifest-path rust/Cargo.toml --all-targets -- -D warnings
cargo test --manifest-path rust/Cargo.toml
```

## Experiment contract

Performance claims must state the commit, platform, framework/backend, seed,
configuration, warm-up method, number of runs, and what changed. Change one
material variable at a time. Benchmark Rust in release mode. Treat numerical
differences as tolerances, not exact equality, when appropriate.

Keep reproducible configs in `shared/configs/`, schemas in `shared/schemas/`,
and small expected outputs in `shared/expected_outputs/`. Commit compact CSV or
JSON summaries and the written conclusion; do not commit generated weights,
adapters, raw traces, or local model caches.

## Pull requests

Use the pull-request template. A good PR has one purpose, tests that demonstrate
the claim, clear documentation, and no unrelated formatting churn. Maintainers
may ask for a smaller PR or for additional evidence before merging.

Report security issues privately as described in [SECURITY.md](SECURITY.md), not
through a public issue.
