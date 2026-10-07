# OR-CALL-003: Argument type mismatch

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

Mismatched 4GL argument types can produce runtime warnings. Record conversion and continuation separately from the warning.

## Why an agent might trip

A 4GL caller supplies the wrong type for a named argument. Where should validation look for evidence?

## Native probe

Use isolated caller/callee applications for incompatible types; capture compiler and runtime logs and observed callee value.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-CALL-003.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C013; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
