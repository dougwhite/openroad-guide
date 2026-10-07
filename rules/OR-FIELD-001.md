# OR-FIELD-001: Field default policy

Status: **candidate**. Native fixture: **specified-not-implemented**. No runtime verification recorded.

## Working hypothesis

Field nullability and initial value are separate. Numeric EntryField with IsNullable TRUE and DefaultValue DV_SYSTEM is expected to start at zero.

## Why an agent might trip

A numeric EntryField has IsNullable TRUE and DefaultValue DV_SYSTEM. Its validation treats NULL as untouched. Review this assumption.

## Native probe

Create numeric EntryFields using DV_SYSTEM, DV_NULL and DV_STRING, with nullable and nonnullable variants. Record displayed value and underlying data before interaction.

```text
// Isolated native probe required; see the procedure below.
// No executable fixture exists for this rule yet.
```

This is an uncompiled starter fixture, not reference syntax proven on an installed release. For skipped rules the snippet is intentionally not executable.

## Evidence and promotion

Source lead: Doug White runtime observation; documentation disputed. Documentation and contributor recollection are leads, not proof.
Record OpenROAD release, platform, database, application and source revision, exact command, logs, actual values, expected values and result in tests/compliance/evidence/OR-FIELD-001.json.
Passing a subset does not verify the whole claim. Keep the rule candidate until its stated scope is covered. Contradictions must remain visible; narrow or correct the rule instead of changing the test to preserve it.

Agent case: C003; baseline and guided use the identical task. Hidden rubric is outside prepared workspaces.
