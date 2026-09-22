# Excel export

Manifest: `WIKI-002`

Compatibility: `source-verified` against Serenity 10.5.2. Host validation is
still required before this is labeled `verified`.

## What changed from the wiki article

The wiki article manually serializes the grid request, posts with `fetch`, reads
a blob, and uses `file-saver`. Current Serenity already supplies the request
preparation, visible-column selection, sort preservation, post, and download
flow through `ExcelExportHelper` in `@serenity-is/extensions`.

Use the native helper and keep the server endpoint generated or implemented in
the host application.

## Minimal grid integration

```ts
import { EntityGrid } from "@serenity-is/corelib";
import { ExcelExportHelper } from "@serenity-is/extensions";
import { ProductColumns, ProductRow, ProductService } from "../ServerTypes/Demo";
import { ProductDialog } from "./ProductDialog";

export class ProductGrid extends EntityGrid<ProductRow> {
    protected override getColumnsKey() { return ProductColumns.columnsKey; }
    protected override getDialogType() { return ProductDialog; }
    protected override getRowDefinition() { return ProductRow; }
    protected override getService() { return ProductService.baseUrl; }

    protected override getButtons() {
        const buttons = super.getButtons();

        buttons.push(ExcelExportHelper.createToolButton({
            grid: this,
            service: ProductService.baseUrl + "/ListExcel",
            separator: true
        }));

        return buttons;
    }
}
```

## Required host pieces

- The host includes `@serenity-is/extensions` at a version compatible with its
  Serenity packages.
- The service exposes a `ListExcel` endpoint compatible with the grid's list
  request and permissions.
- The endpoint reuses the same authorization and row-level filtering as the
  normal list endpoint.

## Why this is safer and smaller

- No additional `file-saver` dependency.
- No hand-built service URL.
- The helper sets `Take` and `Skip` for export and carries the current sort.
- Exported columns come from the current grid columns.
- `onViewSubmit` and `editRequest` remain available for host-specific behavior.

## Validation still required

- Build in a Serenity 9.2.x / .NET 8 host.
- Build in a Serenity 10.5.2 / .NET 10 host.
- Confirm permissions, active filters, quick search, sort, column visibility,
  large-result behavior, error handling, and downloaded workbook content.
