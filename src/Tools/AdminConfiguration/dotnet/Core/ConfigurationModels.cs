namespace SaySol.SerenityTools.AdminConfiguration;

public static class AdminConfigurationPermissions
{
    public const string Manage = "Administration:Configuration";
}

public enum DeploymentEnvironment
{
    Development,
    Sandbox,
    Staging,
    Production
}

public enum DatabaseProfileKind
{
    LocalDb,
    Sandbox,
    Production,
    Failover,
    Other
}

public sealed record BrandingSettings(
    string ProjectName,
    string? ShortName,
    string? LogoAssetPath,
    string? FaviconAssetPath,
    string? ThemeKey);

public sealed record DatabaseProfileReference(
    string Key,
    string DisplayName,
    DatabaseProfileKind Kind,
    string Provider,
    bool Enabled,
    bool IsActive,
    string SecretReferenceKey);

public sealed record AdminConfigurationSnapshot(
    long Revision,
    DeploymentEnvironment Environment,
    BrandingSettings Branding,
    IReadOnlyList<DatabaseProfileReference> DatabaseProfiles,
    DateTimeOffset UpdatedAtUtc,
    string UpdatedBy);

public sealed record AdminConfigurationUpdate(
    long ExpectedRevision,
    BrandingSettings Branding);

public sealed record DatabaseProfileChangeRequest(
    long ExpectedRevision,
    string TargetProfileKey,
    string Reason,
    string ConfirmationPhrase);

public sealed record ConnectivityStatus(
    string ProfileKey,
    bool Reachable,
    string StatusCode,
    DateTimeOffset CheckedAtUtc);
