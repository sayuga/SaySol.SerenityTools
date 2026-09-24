import type { WidgetCatalogEntry, WidgetProvider } from "./types.js";
import { adminLteLegacyMappings, adminLteLegacyProvider } from "../external/adminlte/index.js";
import { serenityNativeWidgets, serenityProvider } from "../native/serenity/index.js";

export const widgetProviders = [
    serenityProvider,
    adminLteLegacyProvider
] as const satisfies readonly WidgetProvider[];

export const widgetCatalog = [
    ...serenityNativeWidgets,
    ...adminLteLegacyMappings
] as const satisfies readonly WidgetCatalogEntry[];
