# Spreadsheet Import evidence ledger

Evidence is additive. Passing the core-runtime checks below does not establish
Serenity-host compatibility or make the capsule installable.

## Core proof — 2026-09-23

- Repository commit: `0c2bc2d12473a1e92a0e70798fc6e19e5408f02a`
- GitHub Actions run: <https://github.com/sayuga/SaySol.SerenityTools/actions/runs/35898197164>
- Repository contracts: passed
- Python resolver/capsule tests: 8 passed
- TypeScript 5.9.3 strict type-check: passed
- .NET 10 core compile and executable proof: passed

The executable proof covers normalized header matching, explicit aliases,
unmapped columns, ambiguous aliases, duplicate targets, import-limit validation,
and the Serenity 10 adapter identity.

The original run also compiled the framework-light core on .NET 8. That result
is retained only as historical evidence and does not establish or imply support
for Serenity versions below 10.5. The legacy adapter and active test lane were
removed when the repository baseline changed to Serenity 10.5+.

## Upstream references

- Serenity 10.5.2 source tag: commit
  `72c270aca67f4848c86d63aec830a2d620629690` in `serenity-is/Serenity`.
- ClosedXML candidate workbook provider: 0.105.0. This dependency is not yet
  included in the capsule; it requires its own bounded-reader implementation
  and hostile-workbook tests before adoption.

## Evidence still required

The complete host validation ladder remains in `VALIDATION.md`. In particular,
no Serenity package was referenced by the core proof, no endpoint was registered,
and no upload, workbook, token, authorization, transaction, or database behavior
has been exercised in a Serenity application.
