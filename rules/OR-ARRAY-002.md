# OR-ARRAY-002: Array growth

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

Writing the next sequential array row can create it. Do not assume writing an arbitrary index fills a gap.

## Why an agent might trip

An empty array is populated by assigning row 1, then row 3. Review whether the missing row is automatically filled.

## Native probe

Write rows 1 and 2, assert LastRow; attempt row 4 in isolated diagnostic probe and capture error.

```text
METHOD testSequentialGrowth() =
DECLARE
    rows = ARRAY OF GuideRow;
ENDDECLARE
BEGIN
    rows[1] = GuideRow.Create();
    rows[2] = GuideRow.Create();
    G_Assert.assertEquals(expectedInteger = 2, actualInteger = rows.LastRow, errortext = 'Sequential growth');
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: How You Can Manipulate Arrays. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-ARRAY-002.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C007; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
