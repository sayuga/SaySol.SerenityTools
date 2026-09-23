namespace SaySol.SerenityTools.SpreadsheetImport;

public enum CommitPolicy
{
    AllOrNothing,
    ValidRowsOnly
}

public sealed record SpreadsheetImportLimits(
    long MaximumFileBytes,
    int MaximumWorksheets,
    int MaximumRows,
    int MaximumColumns,
    long MaximumExpandedBytes)
{
    public void Validate()
    {
        if (MaximumFileBytes <= 0 || MaximumExpandedBytes < MaximumFileBytes)
            throw new ArgumentOutOfRangeException(nameof(MaximumFileBytes));
        if (MaximumWorksheets <= 0 || MaximumRows <= 0 || MaximumColumns <= 0)
            throw new ArgumentOutOfRangeException(nameof(MaximumRows));
    }
}

public interface ISpreadsheetImportProfile
{
    string Key { get; }
    string Permission { get; }
    string PolicyVersion { get; }
    CommitPolicy CommitPolicy { get; }
    SpreadsheetImportLimits Limits { get; }
    IReadOnlyList<ImportField> Fields { get; }
}
