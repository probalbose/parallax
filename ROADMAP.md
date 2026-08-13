# Roadmap

Each lab ends with code, automated correctness tests, hardware metrics, a result
table, and a written conclusion. Exact ordering may change when a prerequisite
or platform constraint makes that useful; the evidence standard does not.

| Lab | Theme | Minimum evidence |
| --- | --- | --- |
| 00 | Hardware and process observer | Shared JSON schema, tests, three runs, comparison report |
| 01 | Arrays and matrix multiplication | Correctness tolerance and performance chart |
| 02 | Linear regression from scratch | Gradients, loss curve, final weights |
| 03 | Automatic differentiation | Manual-versus-autodiff gradient report |
| 04 | MLP batch scaling | Memory/throughput table and quality check |
| 05 | Data-loading pipeline | Queue metrics and bottleneck evidence |
| 06 | Tiny transformer | Shape trace and tiny-corpus overfit |
| 07 | Hardware scaling | Isolated sequence, batch, width, and depth experiments |
| 08 | Manual LoRA | Rank comparison, adapter sizes, quality results |
| 09 | Local LLM fine-tuning | Config, logs, evaluation, and licence-aware artefact policy |
| 10 | Rust training supervisor | Process control, thresholds, structured metrics |
| 11 | Inference service | Ollama integration, typed API, latency metrics |

The curriculum calls these Weeks 1–12; the repository numbers the initial
foundation as Lab 00 so the remaining work can evolve independently.
