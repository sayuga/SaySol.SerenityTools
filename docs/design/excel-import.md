# Excel import package design

Manifest: `ARC-053`

Status: design only; no installable package has been published.

Source article: [Excel Import Extended — Column Mapping and Import Value Type Handling](https://github.com/serenity-is/Serenity/wiki/Excel-Import-Extended---Column-Mapping-and-Import-Value-Type-Handling)

## Goal

Add a safe Excel import to an existing Serenity entity with a small host-facing
surface: install the package, register it, declare the target row and policy,
then let a standard prompt handle upload, mapping, preview, validation, and
commit.

## Intended host experience

```csharp
services.AddSaySolSerenityExcelImport();
```

```csharp
[SaySolExcelImport(
    Permission = ProductRow.PermissionKeys.Insert,
    UniqueKey = nameof(ProductRow.ProductName))]
public sealed class ProductImportProfile : ExcelImportProfile<ProductRow>
{
}
```

```ts
buttons.push(createExcelImportButton({
    profile: "Demo.Product",
    onImported: () => this.refresh()
}));
```

The exact API is provisional. It must be proven against generated Serenity
types before becoming public.

## What is retained from the archived implementation

The archived article contains several ideas worth carrying forward:

- Match workbook columns to application fields instead of depending on column order.
- Allow missing optional columns without corrupting the target row.
- Route values through type-specific conversion and validation.
- Support lookup resolution from one or several source columns.
- Return row-specific warnings and conversion failures to the user.
- Separate reusable import infrastructure from entity-specific mapping policy.

## What must be replaced

The legacy implementation depends on namespace-style TypeScript, decorators,
`Q` helpers, display titles as persistent mapping keys, manual per-field switch
blocks, `dynamic`/`object` values, and direct insertion of related records during
conversion. Those patterns are too brittle for a reusable current package.

The modern package must instead use stable field identifiers plus explicit
aliases, typed conversion results, a preview token, deterministic lookup policy,
and a transaction-controlled commit stage. Creating a missing lookup row must be
an explicit profile policy and visible preview action—not a conversion side
effect.

The Serenity 10.5.2 public source includes the shared `ExcelImportRequest` and
`ExcelImportResponse` contracts and uses ClosedXML for spreadsheet work. It does
not provide the reusable column-mapping workflow described here, so this remains
a valid SaySol tool rather than a duplicate of a complete native feature.

## Workflow

1. Upload `.xlsx` into temporary storage.
2. Read workbook headers and a bounded preview; do not commit.
3. Propose mappings using exact normalized names, aliases, and optional saved
   profiles. Never silently choose an ambiguous mapping.
4. Prompt the user to confirm or correct the mapping.
5. Parse values using the target field metadata and declared culture/time-zone
   policy.
6. Validate required values, lengths, enums, lookups, duplicates, and host
   business rules.
7. Show row- and cell-level errors with a downloadable correction report.
8. Commit only valid rows under an explicit all-or-nothing or partial policy.
9. Return counts and durable audit evidence; purge temporary content according
   to policy.

## Package boundaries

- `SaySol.SerenityTools.ExcelImport.Abstractions` — profiles, requests,
  responses, mapping and validation contracts.
- `SaySol.SerenityTools.ExcelImport` — workbook parsing and orchestration.
- `@saysol/serenity-excel-import` — standard button, mapping dialog, preview,
  and results UI.
- Host adapter — the target row, permissions, lookup resolvers, transaction
  policy, and domain validation.

## Non-negotiable controls

- Use Serenity permissions on discovery, preview, and commit endpoints.
- Do not trust workbook MIME type, extension, formulas, or displayed values.
- Enforce file-size, worksheet, row, column, and decompression limits.
- Treat formulas as data or reject them according to policy; never execute them.
- Prevent CSV/formula injection in generated correction files.
- Resolve lookups deterministically and report ambiguity.
- Keep preview tokens short-lived and bound to user, profile, and file hash.
- Revalidate on commit; preview is not authorization.
- Use an idempotency key and define duplicate behavior.
- Record who imported what, when, under which mapping and policy version.

## Version strategy

The UI should isolate Serenity-specific imports behind a thin adapter. Server
profiles should avoid inheriting directly from request-handler internals. This
reduces the effect of the 10.5 async-handler transition and makes separate
9.2.x and 10.5.x adapters possible if required.

## First proof target

Build a minimal product-like entity with strings, decimals, booleans, enums,
nullable values, and a foreign-key lookup. Validate the same workbook through
both supported Serenity lanes before stabilizing the public API.
