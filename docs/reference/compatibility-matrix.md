# Compatibility matrix

Last reviewed: 2026-09-24

| Lane | Serenity baseline | .NET | Visual Studio | TypeScript registration | Support level |
| --- | --- | --- | --- | --- | --- |
| Supported baseline | 10.5.2 | 10 | 2026 | `static [Symbol.typeInfo]` | Primary and only active lane |
| Historical source | Earlier versions | Not tested | Not tested | Varies | Concept interpretation only |

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
- Serenity versions below 10.5 are not supported or tested by this repository.
- Serenity 9.0 replaced decorator-first TypeScript registration with the static
  `Symbol.typeInfo` pattern. Decorators remained compatible but are deprecated.
- Serenity 10.5.0 introduced async request handlers and changed behavior
  interfaces. Handler and behavior extensions require a specific sync/async
  compatibility review.
- Serenity 10.5.2 introduced nullable annotation behavior in templates and
  generators. Generated-code expectations must account for the project nullable
  setting.
- `10.5+` states the intended compatibility floor. Until later 10.x boundaries
  are tested, exact evidence remains tied to 10.5.2.
