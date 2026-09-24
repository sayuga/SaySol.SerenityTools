# External widget providers

Each optional provider gets its own subfolder. A provider folder owns its source
identity, version range, dependency/asset requirements, normalized mappings,
security notes, validation state, and adapter exports. External packages are
never installed merely because the Widget Library capsule is installed.

Use `adminlte/` as the mapping example. It records the legacy source and maps
its concepts to Serenity-native or SaySol-native options without making
AdminLTE a dependency. A future imported provider must also include its license,
exact package version or commit, asset imports, and host-validation evidence.
