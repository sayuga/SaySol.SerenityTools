namespace SaySol.SerenityTools.SpreadsheetImport;

public sealed record PreviewTokenBinding(
    string Token,
    string UserId,
    string ProfileKey,
    string FileSha256,
    DateTimeOffset ExpiresAtUtc);

public interface IPreviewTokenStore
{
    ValueTask StoreAsync(PreviewTokenBinding binding, CancellationToken cancellationToken);
    ValueTask<PreviewTokenBinding?> ConsumeAsync(string token, CancellationToken cancellationToken);
}

public interface IWorkbookReader
{
    ValueTask<ImportPreview> PreviewAsync(
        Stream workbook,
        ISpreadsheetImportProfile profile,
        string userId,
        CancellationToken cancellationToken);
}

public interface IImportCommitter
{
    ValueTask<CommitResult> CommitAsync(
        ImportPreview preview,
        ISpreadsheetImportProfile profile,
        string userId,
        string idempotencyKey,
        CancellationToken cancellationToken);
}

public interface ISpreadsheetImportAuthorization
{
    ValueTask<bool> IsAllowedAsync(
        string userId,
        string permission,
        CancellationToken cancellationToken);
}
