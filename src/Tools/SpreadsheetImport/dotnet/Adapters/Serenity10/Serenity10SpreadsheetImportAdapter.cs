namespace SaySol.SerenityTools.SpreadsheetImport.Adapters.Serenity10;

/// <summary>
/// Serenity 10.5 async integration seam. Framework-specific authorization is
/// added only after compilation against the pinned .NET 10 proof host.
/// </summary>
public abstract class Serenity10SpreadsheetImportAdapter : ISerenitySpreadsheetImportAdapter
{
    public string Lane => "net10";
    public string MinimumSerenityVersion => "10.5.0";

    public abstract ValueTask DemandPermissionAsync(
        string permission,
        CancellationToken cancellationToken);
}
