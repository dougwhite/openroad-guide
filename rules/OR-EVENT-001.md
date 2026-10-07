# OR-EVENT-001: RETURN in events

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

RETURN in a frame event handler returns from the frame. It is not a local early exit from the handler.

## Why an agent might trip

An event handler returns early on invalid input using RETURN. The window must stay open. Review and correct the flow.

## Native probe

Use a child frame and parent trace. RETURN from child event must close child and resume parent; preserve trace. Run separately from the test runner frame.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White; Return Statement. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-EVENT-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C004; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
