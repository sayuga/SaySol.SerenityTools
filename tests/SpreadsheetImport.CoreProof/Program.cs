using SaySol.SerenityTools.SpreadsheetImport;
using SaySol.SerenityTools.SpreadsheetImport.Adapters.Serenity10;

var fields = new ImportField[]
{
    new("ProductName", "Product Name", true, ["Name"]),
    new("UnitPrice", "Unit Price", true, ["Price", "Cost"]),
    new("CategoryId", "Category", false, ["Category Name"]),
    new("AlternateCost", "Alternate Cost", false, ["Cost"])
};

var mappings = ColumnMappingResolver.Resolve(
    ["Product name", "PRICE", "Unknown", "Category Name", "ProductName", "Cost"],
    fields);

Expect(mappings[0], MappingStatus.Mapped, "ProductName");
Expect(mappings[1], MappingStatus.Mapped, "UnitPrice");
Expect(mappings[2], MappingStatus.Unmapped, null);
Expect(mappings[3], MappingStatus.Mapped, "CategoryId");
Expect(mappings[4], MappingStatus.DuplicateTarget, "ProductName");
Expect(mappings[5], MappingStatus.Ambiguous, null);

if (ColumnMappingResolver.Normalize("  Ünít-price ") != "ÜNÍTPRICE")
    throw new InvalidOperationException("Header normalization contract failed.");

var limits = new SpreadsheetImportLimits(1_000_000, 1, 10_000, 100, 10_000_000);
limits.Validate();

try
{
    new SpreadsheetImportLimits(0, 1, 1, 1, 0).Validate();
    throw new InvalidOperationException("Invalid limits were accepted.");
}
catch (ArgumentOutOfRangeException)
{
    // Expected.
}

if (new Net10ProofAdapter().Lane != "net10")
    throw new InvalidOperationException("Compatibility adapters reported the wrong lane.");

Console.WriteLine("SpreadsheetImport core proof passed.");

static void Expect(ColumnMapping mapping, MappingStatus status, string? fieldKey)
{
    if (mapping.Status != status || mapping.FieldKey != fieldKey)
        throw new InvalidOperationException(
            $"Column {mapping.ColumnIndex}: expected {status}/{fieldKey}, got {mapping.Status}/{mapping.FieldKey}.");
}

sealed class Net10ProofAdapter : Serenity10SpreadsheetImportAdapter
{
    public override ValueTask DemandPermissionAsync(string permission, CancellationToken cancellationToken) =>
        ValueTask.CompletedTask;
}
