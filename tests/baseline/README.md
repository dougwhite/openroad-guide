# Baseline suite

Shared tasks: ../agent/cases. Hidden rule mappings and rubrics: ../agent/rubrics. Do not copy rubrics into the agent workspace.

Prepare with `python3 tools/evaluate.py prepare baseline C001`.
Run Codex in the emitted directory in a fresh session. Review inherited user/global instructions and disable OpenROAD-specific memory or instructions for both arms. A temporary directory isolates repository files, not global agent configuration. Record tools and environment; do not allow access to this source repo during baseline. Cases are intentionally short neutral tasks, though they are explicit rule probes, not validated subtle coding benchmarks yet.

Use identical model/version/settings/tools/task in both arms; randomise order and repeat trials. Review against the same hidden rubric after both answers exist. Do not use the guided answer as ground truth. Record raw transcripts and outcomes including regressions. If article-read telemetry is unavailable, report unknown, never zero.
