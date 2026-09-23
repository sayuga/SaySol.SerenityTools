namespace SaySol.SerenityTools.SpreadsheetImport.Adapters;

public interface ISerenitySpreadsheetImportAdapter
{
    string Lane { get; }
    string MinimumSerenityVersion { get; }

    ValueTask DemandPermissionAsync(
        string permission,
        CancellationToken cancellationToken);
}
