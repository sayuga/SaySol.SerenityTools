# Widget Library

## Summary

Widget Library is a catalog and integration layer for three distinct sources:

1. **Serenity-native UI** already supplied by `@serenity-is/corelib`;
2. **SaySol-native builders** for lightweight dashboard/content components; and
3. **optional external providers** isolated under their own subfolders.

The default rule is to use Serenity before importing another UI system.
AdminLTE is retained as the worked external-provider mapping sample, but it is
not installed or required by this capsule.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Capsule ID | `saysol.serenity.widget-library` |
| Capsule version | `0.3.0` |
| Wiki documentation version | `1.2.0` |
| Native inventory baseline | Serenity tag `10.5.2`, commit `72c270aca67f4848c86d63aec830a2d620629690` |
| Maturity | Implemented catalog and TypeScript core |
| Installation state | **Blocked — Serenity host lifecycle is unverified** |
| AdminLTE sample source | `sayuga/AdminLTE-Widgets-in-Typscript`, commit `2925ee6fc4ab4fa1753798bbe92ea0eddbae883a` |
| Last reviewed | 2026-09-24 |

| Lane | Serenity | Runtime | Compatibility evidence | Core test | Host installation test |
| --- | --- | --- | --- | --- | --- |
| Supported baseline | 10.5.2 | .NET 10 | Native source inventory completed | Passed (TypeScript core) | Not tested |

## Source organization

```text
WidgetLibrary/
├── NATIVE-WIDGET-MAP.md
└── ts/src/
    ├── catalog/
    │   ├── types.ts
    │   └── index.ts
    ├── native/
    │   └── serenity/
    │       └── index.ts
    ├── external/
    │   ├── README.md
    │   └── adminlte/
    │       └── index.ts
    ├── widgets.ts
    └── widgets.css
```

`catalog/types.ts` is the normalized mapping contract. A future external source,
such as a chart package, calendar, Bootstrap widget set, or another dashboard
theme, receives its own `external/<provider>/` folder. Its dependencies and
assets remain optional and isolated.

## Serenity-native inventory

The current map follows Serenity's actual public UI structure instead of treating
every UI control as an AdminLTE-style dashboard card.

| Native family | Principal mapped exports | Typical use |
| --- | --- | --- |
| Foundation | `Widget` | Lifecycle, rendering, element association, disposal, ID prefixes |
| Panels/forms | `BasePanel`, `PropertyPanel`, `PropertyGrid`, `Toolbar`, `ToolbarButton` | Page/panel composition and generated forms |
| Grids | `DataGrid`, `EntityGrid`, `ColumnPickerDialog`, `QuickFilterBar`, `QuickSearchInput`, `SlickPager`, `TreeGridMixin` | Tabular business data, filtering, search, paging, hierarchy |
| Dialogs | `BaseDialog`, `EntityDialog`, `PropertyDialog` | Modal/panel interactions and CRUD |
| Editors | Boolean, date/time, numeric, text, lookup, selection, rich-text, upload, URL, and reCAPTCHA editors | Typed property entry |
| Filtering | `FilterDialog`, `FilterDisplayBar`, `FilterPanel` | Advanced filter construction and display |
| Formatters | Boolean, checkbox, date/time, enum, file, minute, number, and URL formatters | Grid-cell presentation |

The executable catalog records every mapped export's exact Corelib source file,
capabilities, provider, and requirements. Internal and test-only files are not
presented as supported application widgets.

### Native use example

Use Corelib directly when it already supplies the required behavior:

```ts
import { EntityGrid, WidgetProps } from "@serenity-is/corelib";

export class OrdersGrid extends EntityGrid<OrderRow> {
    constructor(props: WidgetProps<{}>) {
        super(props);
    }

    protected getColumnsKey() {
        return "Orders.Order";
    }

    protected getRowDefinition() {
        return OrderRow;
    }
}
```

The Widget Library does not wrap `EntityGrid` merely to rename it. Wrappers are
added only when they simplify a repeated SaySol use case or normalize a genuine
cross-provider difference.

## SaySol-native dashboard builders

Serenity Corelib does not attempt to provide every dashboard-card visual. The
capsule therefore retains small dependency-free builders:

- `createInfoCard`
- `createStatCard`
- `createPanel`
- `createEmptyState`

```ts
import { createInfoCard } from "@saysol/serenity-widget-library";

const card = createInfoCard({
    label: "Open deviations",
    value: "7",
    detail: "2 require QA review",
    tone: "warning",
    progress: 65
});

document.querySelector("#Dashboard")?.append(card);
```

These builders use semantic HTML and `textContent`. They do not require
AdminLTE, accept raw HTML strings, or retrieve arbitrary element IDs.

## External-provider contract

Every external provider must declare:

- stable provider ID and display name;
- exact package version or source commit;
- license and source repository;
- required CSS, JavaScript, fonts, and other assets;
- normalized widget mappings and known native replacements;
- security and lifecycle constraints;
- compatibility and host-test evidence; and
- explicit installation selection.

Merely appearing in the catalog must never install the provider.

### Reading the catalog

```ts
import { widgetCatalog, widgetProviders } from "@saysol/serenity-widget-library";

const nativeGridOptions = widgetCatalog.filter(entry =>
    entry.providerId === "serenity-corelib-10.5" &&
    entry.category === "grid" &&
    entry.status === "available"
);

const optionalProviders = widgetProviders.filter(provider =>
    !provider.requiredByDefault
);
```

## AdminLTE mapping sample

The AdminLTE sample demonstrates how an older or external visual system is
evaluated before import.

| AdminLTE concept | Preferred mapping | State | Reason |
| --- | --- | --- | --- |
| Info Box | `createInfoCard` | Mapped | Common metric/icon/progress behavior without AdminLTE |
| Small Box | `createStatCard` | Mapped | Common metric/tone/action behavior |
| Box | `BasePanel` or `createPanel` | Mapped | Choose Serenity lifecycle or lightweight content panel |
| Progress | SaySol card/native `<progress>` | Mapped | Browser-native accessible primitive |
| Todo/Product List | `DataGrid` when record-backed | Mapped | Native sorting, filtering, paging, and authorization patterns |
| User Widget | Future optional adapter | Planned | No direct native equivalent |
| Timeline | Future optional adapter | Planned | No direct native equivalent |
| Direct Chat | Not carried forward | Deferred | Needs authorization, retention, transport, and moderation design |
| Chart | Separate provider adapter | Planned | Vendor dependency and license must remain explicit |
| FullCalendar | Separate provider adapter | Planned | Vendor assets and event lifecycle must remain explicit |

The sample folder contains mapping metadata, not vendored AdminLTE code. If an
AdminLTE implementation is later selected, that same folder will own the exact
package/import configuration, adapters, license record, and tests.

## Security and data integrity

- Dynamic SaySol content is emitted as text.
- Server authorization controls all data shown by any widget.
- External providers cannot silently add scripts, stylesheets, remote fonts, or
  transitive chart/calendar packages.
- User-provided raw HTML, script fragments, icon markup, and event strings are
  not part of the normalized contract.
- External URLs and actions require host validation.
- Provider adapters must dispose listeners and vendor instances when their
  Serenity host widget is destroyed.

## Installation and configuration

Installation remains blocked. A verified manifest must eventually install the
catalog and SaySol layer without modifying Corelib or adding any external
provider. The import prompt must separately ask which, if any, external provider
the user wants.

### Installation testing state

- Serenity 10.5.2 source inventory: completed.
- AdminLTE legacy source inventory and mapping: completed.
- Manifest/schema validation for version 0.2.0: passed; 0.3.0 pending CI.
- TypeScript 5.9.3 strict type-check for version 0.2.0: passed; 0.3.0 pending CI.
- Native/external provider separation contract test: passed.
- Serenity 10.5.2 bundling/lifecycle test: not tested.
- Keyboard, screen reader, responsive, upgrade, and uninstall tests: not tested.

## Validation

Validate native export availability, text escaping, action/link behavior,
progress bounds, keyboard and screen-reader behavior, responsive layouts,
repeated rendering, listener disposal, theme compatibility, authorization
failures, provider asset ownership, and clean uninstall.

## Upgrade, repair, and uninstall

Native inventory updates are tied to a specific Serenity tag/commit. An upgrade
must diff exports and classify additions, removals, and renamed APIs before the
baseline changes. External providers version independently. Repair may replace
only capsule/provider-owned files. Uninstall removes selected provider assets
without altering Corelib or deleting host dashboard content.

## Source and implementation links

- Capsule: `src/Tools/WidgetLibrary/`
- Native map: `src/Tools/WidgetLibrary/NATIVE-WIDGET-MAP.md`
- Native catalog: `src/Tools/WidgetLibrary/ts/src/native/serenity/index.ts`
- External provider convention: `src/Tools/WidgetLibrary/ts/src/external/README.md`
- AdminLTE mapping sample: `src/Tools/WidgetLibrary/ts/src/external/adminlte/index.ts`
- Legacy concept source: <https://github.com/sayuga/AdminLTE-Widgets-in-Typscript>
- Manifest: `src/Tools/WidgetLibrary/capsule.yaml`
- Evidence ledger: `src/Tools/WidgetLibrary/EVIDENCE.md`
