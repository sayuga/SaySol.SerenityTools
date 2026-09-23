using System.Text;

namespace SaySol.SerenityTools.SpreadsheetImport;

public static class ColumnMappingResolver
{
    public static IReadOnlyList<ColumnMapping> Resolve(
        IReadOnlyList<string> headers,
        IReadOnlyList<ImportField> fields)
    {
        ArgumentNullException.ThrowIfNull(headers);
        ArgumentNullException.ThrowIfNull(fields);

        var candidates = BuildCandidateIndex(fields);
        var mappings = new List<ColumnMapping>(headers.Count);
        var mappedTargets = new HashSet<string>(StringComparer.Ordinal);

        for (var index = 0; index < headers.Count; index++)
        {
            var header = headers[index] ?? string.Empty;
            var normalized = Normalize(header);
            if (!candidates.TryGetValue(normalized, out var matchingFields))
            {
                mappings.Add(new(index, header, null, MappingStatus.Unmapped, []));
                continue;
            }

            var keys = matchingFields.Select(x => x.Key).Distinct(StringComparer.Ordinal).Order().ToArray();
            if (keys.Length > 1)
            {
                mappings.Add(new(index, header, null, MappingStatus.Ambiguous, keys));
                continue;
            }

            var fieldKey = keys[0];
            var status = mappedTargets.Add(fieldKey)
                ? MappingStatus.Mapped
                : MappingStatus.DuplicateTarget;
            mappings.Add(new(index, header, fieldKey, status, keys));
        }

        return mappings;
    }

    public static string Normalize(string value)
    {
        ArgumentNullException.ThrowIfNull(value);
        var result = new StringBuilder(value.Length);
        foreach (var character in value.Normalize(NormalizationForm.FormKC))
        {
            if (char.IsLetterOrDigit(character))
                result.Append(char.ToUpperInvariant(character));
        }
        return result.ToString();
    }

    private static Dictionary<string, List<ImportField>> BuildCandidateIndex(
        IReadOnlyList<ImportField> fields)
    {
        var result = new Dictionary<string, List<ImportField>>(StringComparer.Ordinal);
        foreach (var field in fields)
        {
            if (string.IsNullOrWhiteSpace(field.Key))
                throw new ArgumentException("Every field requires a stable key.", nameof(fields));

            foreach (var candidate in new[] { field.Key, field.DisplayName }.Concat(field.Aliases))
            {
                var normalized = Normalize(candidate);
                if (normalized.Length == 0)
                    continue;
                if (!result.TryGetValue(normalized, out var matches))
                    result[normalized] = matches = [];
                matches.Add(field);
            }
        }
        return result;
    }
}
