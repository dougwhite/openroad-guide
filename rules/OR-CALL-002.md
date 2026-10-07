# OR-CALL-002: Unknown arguments

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

An extra named argument is reported as a runtime warning according to contributor observations. Confirm continuation and diagnostics on the target release.

## Why an agent might trip

A caller supplies a named argument absent from a 4GL procedure declaration. Explain the likely diagnostic stage and what to fix.

## Native probe

Call an isolated procedure with an unknown named argument; record compilation, warning and execution trace. Do not equate no thrown exception with no warning.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-CALL-002.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C012; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
