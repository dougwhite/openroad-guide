# OpenROAD guidance

All rules below are **candidates**, pending native compliance tests. Use them as hypotheses to investigate, not proof. This initial snapshot is for validation; do not deploy it as established guidance yet. Read the linked article when the concise scope is insufficient.

- [OR-NAME-001](rules/OR-NAME-001.md) — Keep class and method names within 32 characters. Confirm the boundary for each identifier category; do not generalise one successful compilation.
- [OR-DEFAULT-001](rules/OR-DEFAULT-001.md) — An omitted scalar default still supplies a value. Nullable integer declarations without DEFAULT NULL are expected to start at zero.
- [OR-FIELD-001](rules/OR-FIELD-001.md) — Field nullability and initial value are separate. Numeric EntryField with IsNullable TRUE and DefaultValue DV_SYSTEM is expected to start at zero.
- [OR-EVENT-001](rules/OR-EVENT-001.md) — RETURN in a frame event handler returns from the frame. It is not a local early exit from the handler.
- [OR-EVENT-002](rules/OR-EVENT-002.md) — Use RESUME to end event processing and resume frame operation. Treat RESUME NEXT as a distinct event-chain operation.
- [OR-ARRAY-001](rules/OR-ARRAY-001.md) — Live OpenROAD array rows start at index 1. Zero is not the first live row.
- [OR-ARRAY-002](rules/OR-ARRAY-002.md) — Writing the next sequential array row can create it. Do not assume writing an arbitrary index fills a gap.
- [OR-ARRAY-003](rules/OR-ARRAY-003.md) — InsertRow without a position is expected to insert at row 1, rather than append.
- [OR-OBJECT-001](rules/OR-OBJECT-001.md) — Assigning an object reference aliases the object. Changing its attributes through either reference affects the same instance.
- [OR-DEFAULT-002](rules/OR-DEFAULT-002.md) — A class-typed declaration can implicitly instantiate an object. DEFAULT NULL suppresses that initial instance.
- [OR-CALL-001](rules/OR-CALL-001.md) — 4GL callers can omit declared arguments; the callee uses defaults. Do not apply strict positional language arity assumptions.
- [OR-CALL-002](rules/OR-CALL-002.md) — An extra named argument is reported as a runtime warning according to contributor observations. Confirm continuation and diagnostics on the target release.
- [OR-CALL-003](rules/OR-CALL-003.md) — Mismatched 4GL argument types can produce runtime warnings. Record conversion and continuation separately from the warning.
- [OR-CALL-004](rules/OR-CALL-004.md) — Object mutation through a passed reference differs from replacing the caller variable. BYREF affects replacement semantics.
- [OR-NULL-001](rules/OR-NULL-001.md) — Ordinary equality with NULL does not test nullness. Use IS NULL or IS NOT NULL.
- [OR-FRAME-001](rules/OR-FRAME-001.md) — CALLFRAME, OPENFRAME and GOTOFRAME have different lifetime and return semantics. Do not substitute one merely to modernise syntax.
