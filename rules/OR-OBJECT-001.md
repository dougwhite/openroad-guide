# OR-OBJECT-001: Reference assignment

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

Assigning an object reference aliases the object. Changing its attributes through either reference affects the same instance.

## Why an agent might trip

A backup object is assigned from the current object, then edited. Will the original remain unchanged?

## Native probe

Assign a custom object to another reference; mutate an attribute; assert original changed. Contrast creating another instance.

```text
METHOD testReferenceAlias() =
DECLARE
    original = GuideRow;
    alias = GuideRow DEFAULT NULL;
ENDDECLARE
BEGIN
    original.value = 10;
    alias = original;
    alias.value = 20;
    G_Assert.assertEquals(expectedInteger = 20, actualInteger = original.value, errortext = 'Assignment shares object');
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Reference Variables. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-OBJECT-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C009; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
