# OR-CALL-004: Objects and BYREF

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

Object mutation through a passed reference differs from replacing the caller variable. BYREF affects replacement semantics.

## Why an agent might trip

A method receives an object and mutates an attribute. Must the argument be BYREF for the caller to observe that mutation?

## Native probe

Compare mutation and reassignment with and without BYREF, recording identity and attribute values after return.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: How You Can Call 4GL Procedures. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-CALL-004.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C014; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
