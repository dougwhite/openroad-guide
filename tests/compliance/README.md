# Native compliance

Applications: `UnitTestFramework` (unaltered uploaded export) and `guide_tests` (draft fixtures). Root gorak.json uses the supplied test entry format, with application guide_tests and component runtests. Application include serialization must be checked against your gorak version before importing. No native execution has occurred here.

On your Windows OpenROAD workstation, from the repository root:

```sh
gorak config --backend local --vnode <vnode> --database <source-database>
gorak sync --push --dry-run
gorak sync --push
gorak compile guide_tests
gorak test --trace
```

The application folders are direct children of the project root, matching gorak's documented layout. Use a disposable source database. Confirm UnitTestFramework is included in guide_tests and `combine` imports with INTEGER return type. Synchronise disk changes before testing: gorak test executes database source. Check `gorak --help` against your installed version. Command/layout references: https://github.com/dougwhite/gorak/blob/master/docs/commands.md and https://github.com/dougwhite/gorak/blob/master/docs/files.md .

For direct runtime execution after importing:

```text
w4gldev rundbapp <database> guide_tests -Lguide-tests.log -Tyes
```

Set OR_UNITTEST_GEN_XML_STATS=TRUE, OR_UNITTEST_TESTDIR to an existing output directory, and OR_UNITTEST_STATSFILE_XML to a distinct output filename. Consult the framework Helper source for your export's exact options. It imports kernel32.dll/GetTickCount64, so this uploaded version is Windows-specific. A non-Windows port requires a separately reviewed replacement.

Exit 0 indicates framework success; 1 indicates failures/errors; 2 can indicate skipped tests. Skips are expected initially and never establish a rule. Ensure both GuideCoreTests and GuidePendingTests appear in logs; do not accept an empty report. Seven draft methods assert core behaviours; nine pending rules explicitly skip. Sequential growth does not yet prove gap behaviour; index-one success does not establish every invalid index behaviour.

Read each probes/ file before implementing the remaining fixtures. UI RETURN tests must use disposable child frames, never the framework runner. Compiler-negative tests and warning tests run in separate probe applications and preserve raw diagnostics. Do not intentionally break the main suite compilation to test an identifier limit.

Copy evidence/template.json for each rule and attach logs with tested version and source commit. Only promote the exact tested scope. This suite is the first development milestone; agent suites are pilots until native evidence exists.
