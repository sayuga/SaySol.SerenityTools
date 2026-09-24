# Spreadsheet Import

## Summary

Spreadsheet Import is intended to give Serenity applications a consistent,
safe workflow for uploading `.xlsx` data, mapping workbook columns to stable
field keys, previewing conversions and errors, and committing authorized rows.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Capsule ID | `saysol.serenity.spreadsheet-import` |
| Capsule version | `0.2.0` |
| Wiki documentation version | `1.1.0` |
| Maturity | Implemented core |
| Installation state | **Blocked — host integration is unverified** |
| Last reviewed | 2026-09-24 |
| Source wiki item | `ARC-053` |

| Lane | Serenity | Runtime | Compatibility evidence | Core test | Host installation test |
| --- | --- | --- | --- | --- | --- |
| Supported baseline | 10.5.2 | .NET 10 | Planned | Passed | Not tested |

The capsule is visible in the catalog but the resolver correctly blocks it. Its
framework-light core has passed .NET 10, TypeScript, schema, and
repository tests; actual Serenity host integration remains unverified.

## Intended user workflow

1. Select an import profile permitted for the current user.
2. Upload an `.xlsx` file into bounded temporary storage.
3. Inspect headers and a limited row preview without changing the database.
4. Map source columns using stable keys, explicit aliases, and user confirmation.
5. Convert and validate values using the profile's culture and domain policy.
6. Review row/cell errors and any proposed lookup actions.
7. Commit under an all-or-nothing or valid-rows-only policy.
8. Record counts, policy version, mapping, user, file hash, and audit evidence.

## Implemented behavior

The 0.2.0 core provides:

- stable field keys, display names, and aliases;
- Unicode-aware header normalization;
- explicit mapped, unmapped, ambiguous, and duplicate-target outcomes;
- file, worksheet, row, column, and expanded-size limit contracts;
- typed preview rows, issues, commit results, and token bindings;
- authorization, workbook-reader, token-store, and commit interfaces;
- a Serenity 10.5+ adapter seam;
- TypeScript preview/commit transport contracts.

## Not implemented yet

- ClosedXML workbook reader and hostile-workbook tests;
- temporary upload and preview-token persistence;
- Serenity endpoints and permission-service bindings;
- dependency-injection registration;
- mapping dialog, grid button, preview, and results UI;
- entity-specific conversion and lookup providers;
- commit transaction implementation;
- saved mappings or capsule-owned database schema.

## Mapping behavior

Headers are normalized with Unicode compatibility normalization, letters and
digits are retained, and comparison is case-insensitive through invariant
uppercase output. A header may match a stable field key, display name, or
explicit alias.

The resolver never silently selects between two matching fields. A repeated
column targeting an already-mapped field is reported as `duplicate-target`.
Unknown columns remain `unmapped`. Required-field enforcement occurs during
preview validation, after the mapping is confirmed.

## Security controls

A complete host implementation must:

- enforce permissions separately on profile discovery, preview, and commit;
- validate extension, package structure, limits, and decompression size;
- reject or treat formulas strictly as data and never execute them;
- bind short-lived preview tokens to user, profile, and file SHA-256;
- revalidate permissions and data inside the commit transaction;
- require an idempotency key and deterministic duplicate policy;
- prevent spreadsheet-formula injection in correction exports;
- make lookup creation an explicit previewed policy, never a conversion side effect.

## Dependencies and Shared

The capsule currently has no `Serenity.SaySolShared` dependency. Its contracts
remain local until at least one other capsule proves an identical reusable need.
Potential future integrations with File Transfer and Audit Trail are optional,
not hidden dependencies.

ClosedXML 0.105.0 is the current workbook-provider candidate, but it has not
been added to the manifest. Provider adoption requires a bounded implementation
and adversarial workbook validation first.

## Database and migrations

Version 0.2.0 owns no database objects and installs no migrations. Saved mapping,
token, and audit persistence remain host-provider decisions. Any future schema
must arrive in a new manifest version with an explicit database-change gate.

## Installation

Installation is intentionally unavailable. Do not manually copy the capsule,
invent endpoint registration, or add migrations. The manifest has no mutating
operations and includes a `capsule-not-yet-verified` human gate.

### Installation testing state

- Catalog selection guard: passed; `implemented` capsules are rejected.
- Manifest schema validation: passed.
- Dependency and ownership resolution tests: passed.
- .NET 10 framework-light core proof: passed.
- TypeScript contract type-check: passed.
- Serenity 10.5.2 host installation: not tested.
- Upgrade, repair, uninstall, and rollback behavior: not tested in a host.

## Validation evidence

The core proof passed on .NET 10 and TypeScript. See the
capsule `EVIDENCE.md` for the exact commit and GitHub Actions run. Host validation
must additionally cover permission denial, upload limits, malicious workbooks,
lookup ambiguity, token binding, commit revalidation, transaction behavior,
upgrade, repair, and uninstall.

## Upgrade and uninstall

There is no supported host installation to upgrade or uninstall yet. Once
released, upgrades will use manifest differences and preserve user-owned files.
Uninstall will remove only capsule-owned files and exact managed insertions;
applied migrations, if later introduced, will remain forward-only.

## Source and implementation links

- Capsule: `src/Tools/SpreadsheetImport/`
- Technical design: `docs/design/excel-import.md`
- Archived source inventory: `ARC-053`
- Compatibility matrix: `docs/reference/compatibility-matrix.md`
