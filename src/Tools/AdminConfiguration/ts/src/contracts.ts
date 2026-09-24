export type DeploymentEnvironment = "development" | "sandbox" | "staging" | "production";
export type DatabaseProfileKind = "localdb" | "sandbox" | "production" | "failover" | "other";

export interface BrandingSettings {
    projectName: string;
    shortName?: string;
    logoAssetPath?: string;
    faviconAssetPath?: string;
    themeKey?: string;
}

export interface DatabaseProfileReference {
    key: string;
    displayName: string;
    kind: DatabaseProfileKind;
    provider: string;
    enabled: boolean;
    isActive: boolean;
    secretReferenceKey: string;
}

export interface AdminConfigurationSnapshot {
    revision: number;
    environment: DeploymentEnvironment;
    branding: BrandingSettings;
    databaseProfiles: readonly DatabaseProfileReference[];
    updatedAtUtc: string;
    updatedBy: string;
}

export interface AdminConfigurationTransport {
    read(): Promise<AdminConfigurationSnapshot>;
    updateBranding(expectedRevision: number, branding: BrandingSettings): Promise<AdminConfigurationSnapshot>;
    requestDatabaseProfileChange(expectedRevision: number, targetProfileKey: string, reason: string, confirmationPhrase: string): Promise<AdminConfigurationSnapshot>;
}
