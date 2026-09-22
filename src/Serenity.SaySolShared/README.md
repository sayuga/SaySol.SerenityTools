# Serenity.SaySolShared

Shared infrastructure for independently installable Serenity tool capsules.

This directory is intentionally documentation-only until the first capsule
implementation establishes a proven shared contract. Code is promoted here
only under the rules in `docs/architecture/capsule-model.md`.

Planned top-level implementation areas:

- `dotnet/` — framework-light contracts and version adapters.
- `ts/` — registration, stable identifier, localization, and UI lifecycle contracts.

Feature-specific behavior belongs in its tool capsule, not here.
