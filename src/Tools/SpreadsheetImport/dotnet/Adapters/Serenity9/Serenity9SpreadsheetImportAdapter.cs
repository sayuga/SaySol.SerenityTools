namespace SaySol.SerenityTools.SpreadsheetImport.Adapters.Serenity9;

/// <summary>
/// Serenity 9.2 integration seam. Framework-specific authorization is added
/// only after compilation against the pinned .NET 8 proof host.
/// </summary>
public abstract class Serenity9SpreadsheetImportAdapter : ISerenitySpreadsheetImportAdapter
{
    public string Lane => "net8";
    public string MinimumSerenityVersion => "9.2.0";

    public abstract ValueTask DemandPermissionAsync(
        string permission,
        CancellationToken cancellationToken);
}
