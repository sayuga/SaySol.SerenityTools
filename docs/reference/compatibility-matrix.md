# Compatibility matrix

Last reviewed: 2026-09-22

| Lane | Serenity baseline | .NET | Visual Studio | TypeScript registration | Support level |
| --- | --- | --- | --- | --- | --- |
| Current | 10.5.2 | 10 | 2026 | `static [Symbol.typeInfo]` | Primary |
| Legacy supported | 9.2.x | 8 | 2022 | `static [Symbol.typeInfo]` | Maintained for SaySol projects |
| Research | 8.8.1 | 8 | 2022 | decorators common | Source interpretation only |

## Compatibility labels

Each recipe and package must use one of these labels:

- `verified`: built and exercised in the stated host matrix.
- `source-verified`: checked against tagged upstream source, but not yet exercised
  end-to-end in a host application.
- `planned`: proposed compatibility that has not been demonstrated.
- `incompatible`: known not to work without material redesign.
- `historical`: retained only for provenance or conceptual value.

Version ranges are never inferred from a single successful version. A range is
published only after its lower and upper boundaries have been validated.

## Current constraints

- Serenity 10.0.0 is the first .NET 10 line and requires Visual Studio 2026.
- Projects that must remain on Visual Studio 2022 and .NET 8 should stay on the
  Serenity 9.2.x line.
- Serenity 9.0 replaced decorator-first TypeScript registration with the static
  `Symbol.typeInfo` pattern. Decorators remained compatible but are deprecated.
- Serenity 10.5.0 introduced async request handlers and changed behavior
  interfaces. Handler and behavior extensions require a specific sync/async
  compatibility review.
- Serenity 10.5.2 introduced nullable annotation behavior in templates and
  generators. Generated-code expectations must account for the project nullable
  setting.
