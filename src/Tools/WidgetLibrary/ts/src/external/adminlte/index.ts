import type { WidgetCatalogEntry, WidgetProvider } from "../../catalog/types.js";

export const adminLteLegacyProvider = {
    id: "external.adminlte.legacy-sayuga",
    displayName: "AdminLTE legacy Sayuga sample",
    kind: "external",
    version: "2017@2925ee6fc4ab4fa1753798bbe92ea0eddbae883a",
    repository: "https://github.com/sayuga/AdminLTE-Widgets-in-Typscript",
    requiredByDefault: false,
    notes: "Mapping sample only. No AdminLTE CSS, JavaScript, chart, or calendar dependency is bundled."
} as const satisfies WidgetProvider;

function mapping(
    legacyName: string,
    category: WidgetCatalogEntry["category"],
    status: WidgetCatalogEntry["status"],
    replacementId: string | undefined,
    capabilities: readonly string[],
    notes: string
): WidgetCatalogEntry {
    return {
        id: `external.adminlte.${legacyName.toLowerCase().replaceAll(" ", "-")}`,
        displayName: legacyName,
        category,
        providerId: adminLteLegacyProvider.id,
        status,
        replacementId,
        requires: [],
        capabilities,
        notes
    };
}

/** Worked example for translating an external widget set into the catalog. */
export const adminLteLegacyMappings = [
    mapping("Info Box", "dashboard", "mapped", "saysol.createInfoCard", ["metric", "icon", "progress"],
        "Prefer the dependency-free SaySol card unless exact AdminLTE rendering is required."),
    mapping("Small Box", "dashboard", "mapped", "saysol.createStatCard", ["metric", "tone", "action"],
        "The SaySol stat card covers the common dashboard-summary use case."),
    mapping("Box", "panel", "mapped", "saysol.createPanel", ["header", "body", "collapse"],
        "Serenity BasePanel is the native lifecycle option; SaySol Panel is the lightweight content option."),
    mapping("Progress", "dashboard", "mapped", "saysol.createInfoCard", ["progress"],
        "Use the native HTML progress element exposed by the SaySol card."),
    mapping("Todo List", "content", "mapped", "serenity.DataGrid", ["list", "status", "actions"],
        "Use DataGrid for server-backed records; a small semantic list is sufficient for local content."),
    mapping("Product List", "content", "mapped", "serenity.DataGrid", ["list", "image", "value"],
        "Use DataGrid when sorting/filtering/paging is needed."),
    mapping("User Widget", "content", "adapter-planned", undefined, ["profile", "image", "actions"],
        "No direct Serenity-native equivalent; implement only when a host use case is approved."),
    mapping("Timeline", "content", "adapter-planned", undefined, ["chronology", "status"],
        "No direct Serenity-native equivalent."),
    mapping("Direct Chat", "communication", "not-carried-forward", undefined, ["messages", "participants"],
        "Requires a dedicated authorization, retention, transport, and moderation design."),
    mapping("Chart", "visualization", "adapter-planned", undefined, ["chart"],
        "Keep chart vendors in a separate optional adapter with an explicit dependency and license."),
    mapping("FullCalendar", "calendar", "adapter-planned", undefined, ["calendar", "events"],
        "Keep FullCalendar in a separate optional adapter with explicit version and asset ownership.")
] as const satisfies readonly WidgetCatalogEntry[];
