# OR-NAME-001: Identifier length

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

Keep class and method names within 32 characters. Confirm the boundary for each identifier category; do not generalise one successful compilation.

## Why an agent might trip

A method needs a descriptive name. Suggest a safe name for validateIncomingCustomerAccountStatus and explain your choice.

## Native probe

Create identifiers of 31, 32 and 33 characters for classes, methods, procedures and parameters. Compile separate applications, preserving diagnostics.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White; OpenROAD Names. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-NAME-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C001; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
