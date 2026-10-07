# OR-FRAME-001: Frame invocation

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

CALLFRAME, OPENFRAME and GOTOFRAME have different lifetime and return semantics. Do not substitute one merely to modernise syntax.

## Why an agent might trip

Replace CALLFRAME with OPENFRAME to make a dialog responsive. What caller assumptions must be reviewed?

## Native probe

Use parent and child trace frames to test blocking, concurrent execution, return value and replacement separately.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Differences Among the Frame-invoking Statements. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-FRAME-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C016; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
