# openroad-guide

Compact, testable OpenROAD guidance for coding agents. MIT, copyright Doug White. Standalone project; no CI or gorak integration automation.

## Start here

Read [OPENROAD.md](OPENROAD.md). Its 16 rules are candidate hypotheses, not established facts. Detailed articles live in `rules/`. The native suite currently contains seven uncompiled starter tests and nine explicit skips with probe specifications. None have been run in OpenROAD. Some tests cover only part of a rule.

## Three suites

1. [Compliance](tests/compliance/README.md): establish the actual runtime behaviour using the gorak applications in `guide_tests/` and `UnitTestFramework/` and the supplied Actian UnitTestFramework.
2. [Baseline](tests/baseline/README.md): prepare a clean workspace for Codex with the task only.
3. [Guided](tests/guided/README.md): prepare the same task with OPENROAD.md and detailed articles.

Start with compliance. Fix native syntax and application packaging against your installed gorak/OpenROAD versions, implement isolated UI and diagnostic probes, then record evidence and promote each rule. The starter does not claim a working native application until it compiles and runs locally.

## Local checks

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests/harness -v
```

## Manual Codex evaluations (later)

```sh
python3 tools/evaluate.py prepare baseline C001
python3 tools/evaluate.py prepare guided C001 --allow-candidates
python3 tools/evaluate.py report results/example.json
```

Preparation prints a temporary workspace path. Start a fresh Codex session there and give it `TASK.md`; save its answer and session transcript outside the workspace. Do not reuse a session between conditions. The guide is deliberately gated while rules remain candidates. `--allow-candidates` is for pilot investigations only.

Evaluation is manual initially. No second model's opinion establishes runtime truth. Prefer native execution for coding tasks once fixtures exist, with human review for unnecessary allocations, unsafe changes and explanations. Publish unchanged performance and regressions too.

See [CONTRIBUTING.md](CONTRIBUTING.md), [coverage](rules/manifest.json), and [third-party notices](THIRD_PARTY_NOTICES.md).
