# Version change ledger

This is a curated upgrade ledger, not a duplicate of Serenity's changelog.

| Version | Material change | Impact on this repository | Required action |
| --- | --- | --- | --- |
| 8.8.1 | Wiki's stated compatibility baseline | Starting point for legacy article review | Never assume 8.8.1 code is current |
| 9.0.0 | Decorator registration deprecated in favor of `static [Symbol.typeInfo]` | Editors, formatters, widgets, and sample code | Rewrite registrations and import generated namespace constants where available |
| 9.2.x | Final .NET 8 line | VS 2022 compatibility lane | Maintain a separate validation host and avoid .NET 10-only APIs |
| 10.0.0 | First .NET 10 version; VS 2026 required | Major host/toolchain boundary | Do not claim 10.x support based on a 9.2 build |
| 10.3.7 | More service-registration helpers, including upload storage | Installer simplification opportunity | Prefer supported registration extensions when available |
| 10.4.0 | Connection-key fallback, docs redesign, stricter HTML handling, removed overloads | Data/storage recipes and UI renderers | Review connection assumptions and HTML-returning formatters |
| 10.5.0 | Async handlers and behaviors; generated handlers now async | Any server extension that touches request handlers | Implement or derive from explicit sync/async behavior contracts and accept cancellation tokens |
| 10.5.1 | Official docs can display older versions | Reference workflow | Link to the matching official-doc version during review |
| 10.5.2 | Nullable annotations in templates/generators; async unit-of-work additions | Generated code, analyzers, server package APIs | Validate with `annotations` and optionally `enable`; prefer async transaction APIs in async code |

## Upgrade review checklist

- Runtime/SDK and IDE requirement changed?
- NuGet or npm package names changed?
- Type registration or generated typings changed?
- Handler, behavior, endpoint, or dependency-injection contracts changed?
- Security defaults, HTML handling, upload handling, or authentication changed?
- A custom integration is now available natively?
- Installation or removal can be reduced to one registration call?
