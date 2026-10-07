# OR-ARRAY-001: Array origin

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

Live OpenROAD array rows start at index 1. Zero is not the first live row.

## Why an agent might trip

Review a loop visiting rows from 0 through LastRow minus 1.

## Native probe

Assert assignment and access at 1; probe zero separately. Test deleted-row indexing independently before documenting it.

```text
METHOD testArrayOrigin() =
DECLARE
    rows = ARRAY OF GuideRow;
ENDDECLARE
BEGIN
    rows[1] = GuideRow.Create();
    rows[1].value = 17;
    G_Assert.assertEquals(expectedInteger = 1, actualInteger = rows.LastRow, errortext = 'First live row');
    G_Assert.assertEquals(expectedInteger = 17, actualInteger = rows[1].value, errortext = 'Row one value');
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White; How You Can Manipulate Arrays. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-ARRAY-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C006; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
