# Spreadsheet Import validation ladder

The capsule must not be marked `verified` until both host lanes complete the
same evidence ladder.

The repository CI compiles and executes the framework-light core proof under
both .NET 8 and .NET 10 and type-checks the transport contracts. Those checks
protect the core but do not satisfy the Serenity-host rows below.
The first passing run is recorded in `EVIDENCE.md`.

| Stage | Serenity 9.2 / .NET 8 | Serenity 10.5 / .NET 10 |
| --- | --- | --- |
| Manifest and ownership validation | Pending | Pending |
| Restore and compile | Pending | Pending |
| Profile discovery and permission denial | Pending | Pending |
| Valid workbook preview | Pending | Pending |
| Ambiguous and duplicate header rejection | Pending | Pending |
| File/row/column/decompression limit rejection | Pending | Pending |
| Lookup ambiguity and missing lookup behavior | Pending | Pending |
| Token user/profile/hash binding | Pending | Pending |
| Commit revalidation and transaction policy | Pending | Pending |
| Formula and correction-export safety | Pending | Pending |
| Upgrade, repair, and uninstall dry run | Pending | Pending |

The proof workbook must cover strings, decimals, booleans, enums, nulls, dates,
duplicate keys, and a foreign-key lookup. Exact package versions and terminal
build/test output must be recorded before a compatibility claim changes.
