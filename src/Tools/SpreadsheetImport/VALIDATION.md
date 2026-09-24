# Spreadsheet Import validation ladder

The capsule must not be marked `verified` until the Serenity 10.5.2 baseline
host completes the evidence ladder.

The repository CI compiles and executes the framework-light core proof under
.NET 10 and type-checks the transport contracts. Those checks
protect the core but do not satisfy the Serenity-host rows below.
The first passing run is recorded in `EVIDENCE.md`.

| Stage | Serenity 10.5.2 / .NET 10 |
| --- | --- |
| Manifest and ownership validation | Pending |
| Restore and compile | Pending |
| Profile discovery and permission denial | Pending |
| Valid workbook preview | Pending |
| Ambiguous and duplicate header rejection | Pending |
| File/row/column/decompression limit rejection | Pending |
| Lookup ambiguity and missing lookup behavior | Pending |
| Token user/profile/hash binding | Pending |
| Commit revalidation and transaction policy | Pending |
| Formula and correction-export safety | Pending |
| Upgrade, repair, and uninstall dry run | Pending |

The proof workbook must cover strings, decimals, booleans, enums, nulls, dates,
duplicate keys, and a foreign-key lookup. Exact package versions and terminal
build/test output must be recorded before a compatibility claim changes.
