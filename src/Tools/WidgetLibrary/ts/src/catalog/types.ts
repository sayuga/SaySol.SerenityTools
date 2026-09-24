export type WidgetSourceKind = "serenity-native" | "saysol-native" | "external";

export type WidgetCategory =
    | "foundation"
    | "panel"
    | "grid"
    | "dialog"
    | "editor"
    | "filter"
    | "formatter"
    | "dashboard"
    | "visualization"
    | "calendar"
    | "communication"
    | "content";

export type WidgetMappingStatus =
    | "available"
    | "mapped"
    | "adapter-planned"
    | "not-carried-forward";

export interface WidgetProvider {
    id: string;
    displayName: string;
    kind: WidgetSourceKind;
    version: string;
    packageName?: string;
    repository?: string;
    requiredByDefault: boolean;
    notes: string;
}

export interface WidgetCatalogEntry {
    id: string;
    displayName: string;
    category: WidgetCategory;
    providerId: string;
    status: WidgetMappingStatus;
    exportName?: string;
    sourcePath?: string;
    replacementId?: string;
    requires: readonly string[];
    capabilities: readonly string[];
    notes?: string;
}
