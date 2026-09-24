# Serenity tool capsules

Each child directory is one independently installable tool capsule. Capsules may
depend on `Serenity.SaySolShared` but should not depend directly on one another
unless an explicit optional integration is documented.

`SpreadsheetImport` is the first capsule with an implemented framework-light
core. It remains non-installable until its workbook provider, Serenity host
integration, and dual-lane validation are complete. See its local README and
validation ladder for the precise boundary.

Additional implemented-but-unverified cores:

- `ThemeKits` — semantic Light, Dark, Logistics, and Future theme tokens.
- `WidgetLibrary` — typed, accessible dashboard/content widget builders.
- `AdminConfiguration` — admin-only safe configuration contracts and transports.

All remain resolver-blocked until their lane-specific Serenity host validation
is complete.

Use `templates/ToolCapsule/` when creating a capsule. Do not mark a capsule
installable until its manifest validates against the repository schema and its
declared installation has been tested in every claimed Serenity lane.
