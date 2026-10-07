# OR-DEFAULT-001: Scalar defaults

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

An omitted scalar default still supplies a value. Nullable integer declarations without DEFAULT NULL are expected to start at zero.

## Why an agent might trip

A nullable integer local is declared without a default. A guard uses IS NULL to detect whether it has been assigned. Review that guard.

## Native probe

Assert integer and varchar defaults; contrast nullable integer with explicit DEFAULT NULL. Extend to other types separately.

```text
METHOD testScalarDefaults() =
DECLARE
    n = INTEGER;
    explicitNull = INTEGER DEFAULT NULL;
    s = VARCHAR(30);
ENDDECLARE
BEGIN
    G_Assert.assertEquals(expectedInteger = 0, actualInteger = n, errortext = 'Implicit integer default');
    G_Assert.assertNull(actualInteger = explicitNull, errortext = 'Explicit DEFAULT NULL');
    G_Assert.assertEquals(expectedVarchar = '', actualVarchar = s, errortext = 'Implicit varchar default');
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White; How You Can Initialize Variables. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-DEFAULT-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C002; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
