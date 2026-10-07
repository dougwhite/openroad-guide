# OR-DEFAULT-002: Implicit object creation

Status: **candidate**. Native fixture: **unrun-draft**. No runtime verification recorded.

## Working hypothesis

A class-typed declaration can implicitly instantiate an object. DEFAULT NULL suppresses that initial instance.

## Why an agent might trip

A class-typed local without DEFAULT NULL is followed by an unconditional Create call. Review whether the initial allocation is necessary.

## Native probe

Assert implicit GuideRow is nonnull and GuideRow DEFAULT NULL is null. Add constructor instrumentation in a follow-up probe.

```text
METHOD testObjectDefaults() =
DECLARE
    implicitObject = GuideRow;
    deferredObject = GuideRow DEFAULT NULL;
ENDDECLARE
BEGIN
    G_Assert.assertNotNull(actual = implicitObject, errortext = 'Implicit object creation');
    G_Assert.assertNull(actual = deferredObject, errortext = 'Deferred object creation');
END
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: How You Can Initialize Variables. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-DEFAULT-002.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C010; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
