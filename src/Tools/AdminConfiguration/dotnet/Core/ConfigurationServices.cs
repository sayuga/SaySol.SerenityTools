namespace SaySol.SerenityTools.AdminConfiguration;

public interface IAdminConfigurationAuthorization
{
    ValueTask DemandAsync(string permission, CancellationToken cancellationToken);
}

public interface IAdminConfigurationStore
{
    ValueTask<AdminConfigurationSnapshot> ReadAsync(CancellationToken cancellationToken);

    ValueTask<AdminConfigurationSnapshot> UpdateBrandingAsync(
        AdminConfigurationUpdate update,
        string actorId,
        CancellationToken cancellationToken);

    ValueTask<AdminConfigurationSnapshot> ChangeDatabaseProfileAsync(
        DatabaseProfileChangeRequest request,
        string actorId,
        CancellationToken cancellationToken);
}

public interface IDatabaseConnectivityProbe
{
    ValueTask<ConnectivityStatus> ProbeAsync(
        DatabaseProfileReference profile,
        CancellationToken cancellationToken);
}

public interface IConfigurationAuditSink
{
    ValueTask RecordAsync(
        string action,
        string actorId,
        long previousRevision,
        long resultingRevision,
        IReadOnlyDictionary<string, string?> safeChanges,
        CancellationToken cancellationToken);
}
