import type { WidgetCatalogEntry, WidgetProvider } from "../../catalog/types.js";

const corelib = "@serenity-is/corelib";
const sourceRoot = "packages/corelib/src/ui";

export const serenityProvider = {
    id: "serenity-corelib-10.5",
    displayName: "Serenity Core Library",
    kind: "serenity-native",
    version: "10.5.2-source-baseline",
    packageName: corelib,
    repository: "https://github.com/serenity-is/Serenity",
    requiredByDefault: true,
    notes: "Host-provided. Inventory verified against Serenity tag 10.5.2 at commit 72c270aca67f4848c86d63aec830a2d620629690."
} as const satisfies WidgetProvider;

function native(
    exportName: string,
    category: WidgetCatalogEntry["category"],
    sourcePath: string,
    capabilities: readonly string[],
    notes?: string
): WidgetCatalogEntry {
    return {
        id: `serenity.${exportName}`,
        displayName: exportName,
        category,
        providerId: serenityProvider.id,
        status: "available",
        exportName,
        sourcePath: `${sourceRoot}/${sourcePath}`,
        requires: [corelib],
        capabilities,
        notes
    };
}

/**
 * Public, application-facing UI inventory exported by @serenity-is/corelib.
 * Internal helpers and test-only types are intentionally excluded.
 */
export const serenityNativeWidgets = [
    native("Widget", "foundation", "widgets/widget.ts", ["lifecycle", "rendering", "disposal", "id-prefix"]),
    native("BasePanel", "panel", "widgets/basepanel.ts", ["panel-lifecycle", "layout"]),
    native("PropertyPanel", "panel", "widgets/propertypanel.ts", ["property-items", "form-layout"]),
    native("PropertyGrid", "panel", "widgets/propertygrid.tsx", ["form-generation", "editor-binding"]),
    native("Toolbar", "panel", "widgets/toolbar.tsx", ["commands", "hotkeys", "visibility"]),
    native("ToolbarButton", "panel", "widgets/toolbar.tsx", ["command", "icon", "disabled-state"]),

    native("DataGrid", "grid", "datagrid/datagrid.tsx", ["sorting", "filtering", "paging", "persistence"]),
    native("EntityGrid", "grid", "datagrid/entitygrid.ts", ["entity-dialog", "authorization", "crud"]),
    native("ColumnPickerDialog", "grid", "datagrid/columnpickerdialog.tsx", ["column-selection"]),
    native("QuickFilterBar", "grid", "datagrid/quickfilterbar.tsx", ["quick-filters"]),
    native("QuickSearchInput", "grid", "datagrid/quicksearchinput.tsx", ["search"]),
    native("SlickPager", "grid", "datagrid/slickpager.tsx", ["paging"]),
    native("TreeGridMixin", "grid", "datagrid/treegridmixin.ts", ["hierarchy", "expand-collapse"]),

    native("BaseDialog", "dialog", "dialogs/basedialog.tsx", ["dialog-lifecycle", "responsive-layout"]),
    native("EntityDialog", "dialog", "dialogs/entitydialog.tsx", ["entity-crud", "authorization", "localization"]),
    native("PropertyDialog", "dialog", "dialogs/propertydialog.tsx", ["property-grid", "validation"]),

    native("BooleanEditor", "editor", "editors/booleaneditor.tsx", ["boolean-input"]),
    native("CheckTreeEditor", "editor", "editors/checktreeeditor.tsx", ["tree-selection", "multi-select"]),
    native("ComboBoxEditor", "editor", "editors/comboboxeditor.tsx", ["combobox"]),
    native("DateEditor", "editor", "editors/dateeditor.tsx", ["date-input"]),
    native("DateTimeEditor", "editor", "editors/datetimeeditor.tsx", ["date-time-input"]),
    native("DateYearEditor", "editor", "editors/dateyeareditor.ts", ["year-input"]),
    native("DecimalEditor", "editor", "editors/decimaleditor.tsx", ["decimal-input"]),
    native("EmailAddressEditor", "editor", "editors/emailaddresseditor.tsx", ["email-address"]),
    native("EmailEditor", "editor", "editors/emaileditor.tsx", ["email-address", "domain"]),
    native("EnumEditor", "editor", "editors/enumeditor.ts", ["enum-selection"]),
    native("HtmlContentEditor", "editor", "editors/htmlcontenteditor.tsx", ["rich-text"]),
    native("IntegerEditor", "editor", "editors/integereditor.tsx", ["integer-input"]),
    native("LookupEditor", "editor", "editors/lookupeditor.ts", ["lookup", "cascade"]),
    native("MaskedEditor", "editor", "editors/maskededitor.tsx", ["input-mask"]),
    native("PasswordEditor", "editor", "editors/passwordeditor.tsx", ["password-input"]),
    native("RadioButtonEditor", "editor", "editors/radiobuttoneditor.tsx", ["single-selection"]),
    native("Recaptcha", "editor", "editors/recaptcha.ts", ["bot-challenge"], "Requires host-side reCAPTCHA configuration."),
    native("SelectEditor", "editor", "editors/selecteditor.ts", ["selection"]),
    native("ServiceLookupEditor", "editor", "editors/servicelookupeditor.ts", ["remote-lookup"]),
    native("StringEditor", "editor", "editors/stringeditor.tsx", ["text-input"]),
    native("TextAreaEditor", "editor", "editors/textareaeditor.ts", ["multiline-text"]),
    native("TimeEditor", "editor", "editors/timeeditor.ts", ["time-input"]),
    native("FileUploadEditor", "editor", "editors/uploadeditors.tsx", ["single-file-upload"]),
    native("ImageUploadEditor", "editor", "editors/uploadeditors.tsx", ["single-image-upload"]),
    native("MultipleFileUploadEditor", "editor", "editors/uploadeditors.tsx", ["multi-file-upload"]),
    native("MultipleImageUploadEditor", "editor", "editors/uploadeditors.tsx", ["multi-image-upload"]),
    native("URLEditor", "editor", "editors/urleditor.ts", ["url-input"]),

    native("FilterDialog", "filter", "filtering/filterdialog.tsx", ["advanced-filter-dialog"]),
    native("FilterDisplayBar", "filter", "filtering/filterdisplaybar.tsx", ["active-filter-summary"]),
    native("FilterPanel", "filter", "filtering/filterpanel.tsx", ["advanced-filter-builder"]),

    native("BooleanFormatter", "formatter", "formatters/booleanformatter.tsx", ["boolean-display"]),
    native("CheckboxFormatter", "formatter", "formatters/checkboxformatter.tsx", ["checkbox-display"]),
    native("DateFormatter", "formatter", "formatters/dateformatter.ts", ["date-display"]),
    native("DateTimeFormatter", "formatter", "formatters/datetimeformatter.ts", ["date-time-display"]),
    native("EnumFormatter", "formatter", "formatters/enumformatter.ts", ["enum-display"]),
    native("FileDownloadFormatter", "formatter", "formatters/filedownloadformatter.tsx", ["download-link"]),
    native("MinuteFormatter", "formatter", "formatters/minuteformatter.ts", ["minute-display"]),
    native("NumberFormatter", "formatter", "formatters/numberformatter.ts", ["number-display"]),
    native("UrlFormatter", "formatter", "formatters/urlformatter.tsx", ["url-link"])
] as const satisfies readonly WidgetCatalogEntry[];
