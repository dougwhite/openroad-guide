# OR-EVENT-002: RESUME and event flow

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

Use RESUME to end event processing and resume frame operation. Treat RESUME NEXT as a distinct event-chain operation.

## Why an agent might trip

Explain whether RESUME and RESUME NEXT are interchangeable in chained frame events.

## Native probe

Trace chained handlers with RESUME and RESUME NEXT. Confirm subsequent handler execution and frame survival for each.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White; Resume Statement. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-EVENT-002.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C005; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
