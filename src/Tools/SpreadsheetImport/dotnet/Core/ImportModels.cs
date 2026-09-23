namespace SaySol.SerenityTools.SpreadsheetImport;

public enum MappingStatus
{
    Mapped,
    Unmapped,
    Ambiguous,
    DuplicateTarget
}

public sealed record ImportField(
    string Key,
    string DisplayName,
    bool Required,
    IReadOnlyList<string> Aliases);

public sealed record ColumnMapping(
    int ColumnIndex,
    string Header,
    string? FieldKey,
    MappingStatus Status,
    IReadOnlyList<string> CandidateFieldKeys);

public sealed record ImportIssue(
    string Code,
    string Message,
    int? RowNumber = null,
    int? ColumnIndex = null,
    string? FieldKey = null);

public sealed record PreviewRow(
    int RowNumber,
    IReadOnlyDictionary<string, object?> Values,
    IReadOnlyList<ImportIssue> Issues);

public sealed record ImportPreview(
    string Token,
    string ProfileKey,
    string FileSha256,
    IReadOnlyList<ColumnMapping> Mappings,
    IReadOnlyList<PreviewRow> Rows,
    IReadOnlyList<ImportIssue> Issues,
    DateTimeOffset ExpiresAtUtc);

public sealed record CommitResult(
    int Inserted,
    int Updated,
    int Skipped,
    IReadOnlyList<ImportIssue> Issues);
