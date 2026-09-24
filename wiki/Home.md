# SaySol SerenityTools Wiki

SaySol SerenityTools converts useful Serenity community patterns into
version-aware, independently installable tool capsules. This wiki is the
operator-facing guide: use it to decide whether a tool fits your project, what
it changes, how it is configured, and how it is validated or removed.

## Start here

- [Tool Catalog](Tool-Catalog.md) — maturity, compatibility, and availability.
- [Installation Model](Installation-Model.md) — catalog selection, dry run,
  human gates, lockfiles, receipts, upgrades, and uninstall.
- [Spreadsheet Import](Spreadsheet-Import.md) — first implemented capsule.
- [Grid Export](Grid-Export.md) — current recipe using native Serenity export.
- [Theme Kits](Theme-Kits.md) — reusable Light, Dark, Logistics, and Future themes.
- [Widget Library](Widget-Library.md) — typed dashboard and content widgets.
- [Admin Configuration](Admin-Configuration.md) — admin-only safe configuration surface.
- [Compatibility](Compatibility.md) — supported Serenity lanes and evidence labels.

## Status language

| Status | Meaning |
| --- | --- |
| Planned | Grouping or concept only; no implementation claim |
| Design | Architecture is documented but code is not implemented |
| Recipe | Reviewed host instructions, not an installable capsule |
| Implemented | Code exists but required compatibility evidence is incomplete |
| Verified | Required validation passed for explicitly named host lanes |
| Released | Versioned artifact is available for supported use |
| Retired | Preserved for upgrade/removal history, not new installation |

Only `verified` and `released` capsules with a valid manifest are installable.
The root resolver enforces that boundary.

## Documentation boundary

Each tool has three documentation layers:

1. This wiki page explains the tool to evaluators, operators, and host developers.
2. The capsule `README.md` defines its technical package boundary and APIs.
3. `capsule.yaml` is the machine authority for installation and removal.

If prose conflicts with a manifest, installation stops until the conflict is
corrected. Wiki instructions never authorize undeclared host changes.
