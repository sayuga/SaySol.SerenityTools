# Serenity native widget map

Baseline: Serenity `10.5.2`, source commit
`72c270aca67f4848c86d63aec830a2d620629690`.

The executable inventory is in `ts/src/native/serenity/index.ts`. It maps the
public application-facing exports of `@serenity-is/corelib` to their exact
Serenity source paths and capabilities. The map covers:

| Family | Principal native options |
| --- | --- |
| Lifecycle and composition | `Widget`, `BasePanel`, `PropertyPanel`, `PropertyGrid`, `Toolbar`, `ToolbarButton` |
| Data presentation | `DataGrid`, `EntityGrid`, `ColumnPickerDialog`, `QuickFilterBar`, `QuickSearchInput`, `SlickPager`, `TreeGridMixin` |
| Dialogs | `BaseDialog`, `EntityDialog`, `PropertyDialog` |
| Editors | Boolean, tree, combo, date/time, number, email, enum, rich text, lookup, mask, password, radio, select, text, upload, URL, and reCAPTCHA editors |
| Filtering | `FilterDialog`, `FilterDisplayBar`, `FilterPanel` |
| Grid formatting | Boolean, checkbox, date/time, enum, download, minute, number, and URL formatters |

This is a source inventory, not a claim that every item is a dashboard card.
Serenity provides the application UI primitives first. SaySol dashboard cards
sit above those primitives, while third-party visual systems remain optional.
