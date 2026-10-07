# OR-ARRAY-003: InsertRow position

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

InsertRow without a position is expected to insert at row 1, rather than append.

## Why an agent might trip

An application repeatedly calls InsertRow without specifying a position and expects FIFO order. Review.

## Native probe

Insert distinguishable rows; call InsertRow with omitted position and assert ordering. Capture actual signature on installed release.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: How You Can Manipulate Arrays. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-ARRAY-003.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C008; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
