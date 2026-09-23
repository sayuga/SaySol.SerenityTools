# SaySol.SerenityTools

Reusable, version-aware tools and recipes for Serenity applications.

The project converts useful Serenity community patterns into small integrations
that are easy to install, configure, validate, and later upgrade. It does not
replace Serenity's official documentation or copy legacy wiki code without
review. Every adopted pattern is traced to its source and tested against an
explicit Serenity compatibility lane.

## Compatibility lanes

| Lane | Serenity | Runtime and IDE | Purpose |
| --- | --- | --- | --- |
| Current | 10.5.x | .NET 10 / Visual Studio 2026 | New development and forward-looking packages |
| Legacy supported | 9.2.x | .NET 8 / Visual Studio 2022 | Existing SaySol projects and controlled migration |
| Research only | 8.8.1 | Historical baseline | Original community-wiki compatibility point |

See [the compatibility matrix](docs/reference/compatibility-matrix.md) before
using a recipe or package.

Contributors should follow the [development guide](docs/DEVELOPMENT.md). The
complete wiki census is split between the detailed
[active-page manifest](docs/wiki-modernization/manifest.yaml) and the
[141-page archive manifest](docs/wiki-modernization/archive-manifest.md).

Implementations follow the [tool-capsule architecture](docs/architecture/capsule-model.md):
shared cross-capsule infrastructure lives in `Serenity.SaySolShared`, while each
tool remains independently installable under `src/Tools/`.

Installation is manifest-driven. Each released capsule declares file placement,
migrations, bounded host edits, validation, upgrade, and uninstall behavior in
`capsule.yaml`; see the [installation protocol](docs/architecture/manifest-installation.md).
The root [catalog](catalog.yaml) controls discovery and the
[import prompt](IMPORT-PROMPT.md) drives selection. Multi-capsule compatibility,
dependencies, host capabilities, and ownership collisions can be checked with
the read-only [resolver](tools/resolve_install.py); see the
[orchestration design](docs/architecture/import-orchestration.md).

## Repository map

- `docs/reference/` — version baselines, important framework changes, and upgrade policy
- `docs/wiki-modernization/` — active-page inventory and expanding modernization ledger
- `docs/recipes/` — rewritten, versioned, copy-safe integration guides
- `docs/design/` — package and installer designs that are not yet released code
- `src/` — reusable packages after a design passes validation
- `tests/` — package-level and Serenity-host integration tests
- `samples/` — minimal Serenity host applications used to prove installation
- `schema/` — catalog, capsule, host-facts, and lockfile contracts
- `tools/` — read-only resolution now; transactional install tooling later

## Modernization rule

A wiki article is not considered modernized merely because its syntax compiles.
It must have a traceable source, a supported version range, a minimal install
surface, a removal path, and validation in a representative Serenity host.

## First modernization track

The first active track is export/import:

1. Excel export: replace hand-written fetch/download code with Serenity's native
   `ExcelExportHelper` and an existing `ListExcel` service.
2. Excel import: design a reusable upload, preview, column-map, validate, and
   commit workflow with a small host registration surface.

The export recipe is ready for technical validation. The import design is
documented but is not yet an installable package.
