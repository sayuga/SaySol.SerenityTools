using SaySol.SerenityTools.AdminConfiguration;

var profiles = new DatabaseProfileReference[]
{
    new("local", "LocalDB sandbox", DatabaseProfileKind.LocalDb, "SqlServer", true, false, "Database:LocalDb"),
    new("production", "Production SQL", DatabaseProfileKind.Production, "SqlServer", true, true, "Database:Production")
};

var snapshot = new AdminConfigurationSnapshot(
    4,
    DeploymentEnvironment.Production,
    new BrandingSettings("SaySol Demo", "Demo", "/assets/logo.svg", null, "logistics"),
    profiles,
    DateTimeOffset.UtcNow,
    "admin-proof");

if (snapshot.DatabaseProfiles.Count(x => x.IsActive) != 1)
    throw new InvalidOperationException("A proof snapshot must have exactly one active profile.");

if (AdminConfigurationPermissions.Manage != "Administration:Configuration")
    throw new InvalidOperationException("The stable admin permission changed unexpectedly.");

var forbiddenPropertyFragments = new[] { "ConnectionString", "Password", "SecretValue", "Credential", "TokenValue" };
var publicModelTypes = new[]
{
    typeof(BrandingSettings), typeof(DatabaseProfileReference), typeof(AdminConfigurationSnapshot),
    typeof(AdminConfigurationUpdate), typeof(DatabaseProfileChangeRequest), typeof(ConnectivityStatus)
};

foreach (var property in publicModelTypes.SelectMany(x => x.GetProperties()))
{
    if (forbiddenPropertyFragments.Any(x => property.Name.Contains(x, StringComparison.OrdinalIgnoreCase)))
        throw new InvalidOperationException($"Public configuration model exposes forbidden property {property.Name}.");
}

Console.WriteLine("AdminConfiguration core proof passed.");
