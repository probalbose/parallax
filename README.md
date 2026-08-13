# Parallax

> **Status:** early-stage, open for contributors. The first release establishes
> the Lab 00 baseline and the public project contract.

**A paired Python–Rust laboratory for measuring what LLM training actually costs on real hardware.**

Every experiment is implemented twice, because one measurement is a number and two are a conclusion.

---

## Why "Parallax"

You cannot infer distance from a single observation. You need two sightlines and the angle between them. The same holds here: a single benchmark tells you that a training step took 84 ms, but not *why* — whether the cost sat in the interpreter, the kernel, the allocator, or the data loader. Implementing the same problem in Python and in Rust, against the same seed, config and tolerance, gives the second sightline.

The name also carries its own warning. *Parallax error* is what happens when you read an instrument from the wrong angle and record a confidently wrong value. Most of the methodology in this repository — warmups, release builds, three runs minimum, one variable at a time, compute time separated from data-loading time — exists to guard against exactly that.

## What this is

A twelve-week curriculum working from language and hardware fundamentals up to real LLM fine-tuning and production serving, on Apple Silicon. Python handles experimentation, training and analysis; Rust handles memory-explicit implementations, data pipelines, process supervision and delivery. Neither language is a subject in itself — both are instruments for seeing where the cost lives.

Roughly:

| Weeks | Focus |
|------:|-------|
| 1–2 | System observation, arrays, matrix multiplication and backend dispatch |
| 3–5 | Manual gradients, automatic differentiation, batch scaling |
| 6–8 | Data pipelines, a tiny transformer, hardware-scaling experiments |
| 9–10 | Manual LoRA, then real fine-tuning of a small instruct model |
| 11–12 | Rust training supervisor, Ollama serving and API performance |

Every week produces code, measurements and a written conclusion. The written conclusion is not optional — it is the deliverable that distinguishes this from a tutorial.

The public roadmap turns this programme into small, reviewable milestones. See
[`ROADMAP.md`](ROADMAP.md) for the twelve labs and their definition of done.

## Layout

```
parallax/
├── python/          experiments, training, analysis
├── rust/            memory-explicit implementations, pipelines, supervision
├── shared/          configs, synthetic data, expected outputs
├── experiments/     results.csv and hardware snapshots
├── notebooks/
├── reports/         weekly written conclusions
└── scripts/         run_python.sh, run_rust.sh, compare_runs.py
```

Both languages read the same experiment configuration, so comparisons stay valid:

```json
{
  "experiment_id": "matmul-001",
  "seed": 42,
  "matrix_size": 1024,
  "iterations": 100,
  "warmup_iterations": 10,
  "dtype": "float32"
}
```

## Ground rules

- Correctness before performance. Compare floating-point results against an explicitly documented tolerance.
- Change one variable at a time.
- Benchmark Rust in release mode (`cargo run --release`, `cargo bench`). A debug-build comparison is not a result.
- Warm up, then measure. Three runs minimum for anything you intend to cite.
- Record both framework-reported memory and OS process memory.
- A run that completes while heavily swapping is not a successful run.

---

## Licensing

Three licences, because a software licence is the wrong instrument for data or prose.

| Content | Licence | File |
|---|---|---|
| Source code — `python/`, `rust/`, `scripts/` | Apache-2.0 | [`LICENSE`](LICENSE) |
| Documentation, reports, written analysis | CC BY-NC-ND 4.0 | [`LICENSE-DOCS`](LICENSE-DOCS) |
| Synthetic datasets and experiment results | CC0-1.0 | [`LICENSE-DATA`](LICENSE-DATA) |

**The code is fully permissive. The writing is not.** Take the code, modify it, sell what you build with it — Apache-2.0 rather than MIT because it carries an explicit patent grant and a defensive termination clause, which removes an ambiguity that makes corporate legal teams hesitate.

The prose is a different matter. The weekly reports here are early drafts of a book, so commercial and derivative rights in the written material are reserved. You may read, share and quote it with attribution; you may not sell it or publish a modified version without asking. `LICENSE-DOCS` includes an additional permission so that forks and contributors can still edit documentation freely — the NoDerivatives term is aimed at republication of the writing, not at normal open-source work.

Attribution notices and third-party terms are in [`NOTICE`](NOTICE).

### Model weights are not covered by any of the above

This repository contains **no** pretrained weights, tokenizers or trained adapters. They are gitignored and must be fetched from source under their own licences.

This matters more than it sounds. A LoRA adapter trained against a Meta Llama base model is a *derivative of that model*. It stays under the Llama Community Licence — acceptable-use policy, MAU threshold, and the requirement that derivative model names begin with "Llama" — regardless of what this repository's `LICENSE` says. You cannot relicense it Apache-2.0.

If you want fine-tuning artefacts you can redistribute freely, start from a permissively licensed base such as Qwen2.5-1.5B-Instruct or SmolLM2-1.7B-Instruct (both Apache-2.0). Either works with MLX-LM.

When publishing any adapter, state its base model and that model's licence explicitly.

### Applying the licence to new source files

Add the SPDX identifier at the top of each file:

```python
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Probal Bose
```

```rust
// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 Probal Bose
```

---

Copyright © 2026 Probal Bose.

## Quick start: Lab 00

Lab 00 is the cross-language hardware and process observer. It establishes the
first shared schema, tests, and comparison workflow used by every later lab.

```bash
# Python 3.11+
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e "./python[dev]"
python python/src/parallax_lab/hardware_snapshot.py

# Rust stable
cargo run --manifest-path rust/Cargo.toml --release --bin hardware_snapshot

# Run both and record one comparable result.
python scripts/compare_snapshots.py
```

The comparison script appends a compact record to `experiments/results.csv`.
Run it at least three times before drawing a conclusion.

## Contributing and project rules

Contributions are welcome, especially a small, well-evidenced lab improvement.
Please read these before opening an issue or pull request:

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — development, experiment, and PR rules
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — community expectations
- [`SECURITY.md`](SECURITY.md) — private vulnerability reporting
- [`GOVERNANCE.md`](GOVERNANCE.md) — maintainer decisions and release authority
- [`RELEASING.md`](RELEASING.md) — versioning, tags, and release process

Issues and pull requests use templates that ask for the evidence needed to
evaluate a performance claim. A benchmark change without a reproducible config,
raw-enough summary, and written interpretation is incomplete by design.

## Releases

Parallax follows [Semantic Versioning](https://semver.org/). Releases are
signed annotated tags named `vMAJOR.MINOR.PATCH`; a pushed tag creates the
corresponding GitHub release and release notes. The initial project baseline is
`v0.1.0`.
