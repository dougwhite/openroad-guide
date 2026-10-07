# OR-CALL-001: Omitted named arguments

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

4GL callers can omit declared arguments; the callee uses defaults. Do not apply strict positional language arity assumptions.

## Why an agent might trip

A 4GL method declares two defaulted parameters but a caller supplies only one by name. Is this necessarily an invalid call?

## Native probe

Call a method with all arguments, omitted arguments and reversed named order; assert resulting defaults and values.

```text
METHOD testOmittedArguments() =
BEGIN
    G_Assert.assertEquals(expectedInteger = 12, actualInteger = CurObject.combine(), errortext = 'Both omitted');
    G_Assert.assertEquals(expectedInteger = 32, actualInteger = CurObject.combine(left = 3), errortext = 'Right omitted');
    G_Assert.assertEquals(expectedInteger = 45, actualInteger = CurObject.combine(right = 5, left = 4), errortext = 'Named order');
END

METHOD combine(left = INTEGER DEFAULT 1, right = INTEGER DEFAULT 2) =
BEGIN
    RETURN left * 10 + right;
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White; How You Can Call 4GL Procedures. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-CALL-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C011; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
