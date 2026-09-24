# Grid Export

## Summary

Grid Export is currently a modern recipe, not an installable capsule. It replaces
legacy hand-written fetch, blob, and file-saver code with Serenity's native
`ExcelExportHelper` and an existing `ListExcel` service.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Catalog ID | `saysol.serenity.grid-export` |
| Tool version | Not packaged |
| Wiki documentation version | `1.1.0` |
| Maturity | Recipe |
| Delivery | Documentation recipe |
| Installation state | **Recipe only — host validation required** |
| Last reviewed | 2026-09-24 |
| Primary guide | `docs/recipes/exporting/excel-export.md` |

| Lane | Serenity | Runtime | Compatibility evidence | Host installation test |
| --- | --- | --- | --- | --- |
| Supported baseline | 10.5.2 | .NET 10 | Source verified | Not tested |

## When to use it

Use this recipe when a grid already has a compatible server-side Excel list
endpoint and the goal is to export the grid's current columns, filters, sorting,
and include-columns state.

## Why it is separate from Spreadsheet Import

Export and import share a file format but not a lifecycle or risk profile.
Export serializes authorized query results. Import accepts untrusted content,
maps it to domain fields, and can mutate data. Combining them would force upload,
validation, token, and transaction dependencies onto a simple export feature.

## Installation

Follow the versioned recipe in the repository. No capsule manifest is required
unless future work adds reusable custom formats or server infrastructure beyond
Serenity's native facilities.

### Installation testing state

- Native API comparison against Serenity 10.5.2 source: passed.
- Serenity 10.5.2 host compilation and export behavior: not tested.
- Permission, filtering, sorting, visible-column, and large-result behavior:
  pending host validation.
- Upgrade/uninstall testing: not applicable while delivery remains a recipe.

## Security and authorization

The server endpoint remains the authorization boundary. Hiding an export button
does not secure data. The export request must preserve the grid's active request
state and the endpoint must enforce the appropriate list/read permission.

## Validation

Confirm that:

- the exported columns match the current grid selection;
- filters and sorting are preserved;
- unauthorized users cannot call the endpoint directly;
- large exports remain within host limits;
- localized captions and value formatting are acceptable for the target lane.

## Upgrade and removal

Because this is a bounded recipe using native APIs, removal means deleting the
button/helper invocation and any now-unused imports. There are no migrations,
receipts, or capsule-owned database objects.
