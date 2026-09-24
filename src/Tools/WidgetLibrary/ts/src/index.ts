export { createEmptyState, createInfoCard, createPanel, createStatCard } from "./widgets.js";
export type { InfoCardOptions, PanelOptions, WidgetAction, WidgetTone } from "./widgets.js";
export { widgetCatalog, widgetProviders } from "./catalog/index.js";
export type {
    WidgetCatalogEntry,
    WidgetCategory,
    WidgetMappingStatus,
    WidgetProvider,
    WidgetSourceKind
} from "./catalog/types.js";
export { serenityNativeWidgets, serenityProvider } from "./native/serenity/index.js";
export {
    adminLteLegacyMappings,
    adminLteLegacyProvider
} from "./external/adminlte/index.js";
