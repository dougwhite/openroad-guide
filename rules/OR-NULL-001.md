# OR-NULL-001: NULL comparisons

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

Ordinary equality with NULL does not test nullness. Use IS NULL or IS NOT NULL.

## Why an agent might trip

Review an IF amount = NULL guard and suggest the intended test.

## Native probe

Assert branch behaviour of x = NULL and x IS NULL for explicitly null x; capture installed compiler acceptance.

```text
METHOD testNullGuard() =
DECLARE
    n = INTEGER DEFAULT NULL;
    visited = INTEGER DEFAULT 0;
ENDDECLARE
BEGIN
    IF n = NULL THEN
        visited = 1;
    ENDIF;
    G_Assert.assertEquals(expectedInteger = 0, actualInteger = visited, errortext = 'Equality does not detect NULL');
    IF n IS NULL THEN
        visited = 2;
    ENDIF;
    G_Assert.assertEquals(expectedInteger = 2, actualInteger = visited, errortext = 'IS NULL detects NULL');
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Nulls in Expressions. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-NULL-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C015; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
