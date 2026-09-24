# Widget Library

## Summary

Widget Library provides small, typed builders for reusable dashboard and content
components. It modernizes concepts from the 2017
`sayuga/AdminLTE-Widgets-in-Typscript` repository without copying its obsolete
namespace, decorator, AdminLTE 2, element-ID, or raw-HTML implementation.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Capsule ID | `saysol.serenity.widget-library` |
| Capsule version | `0.1.0` |
| Wiki documentation version | `1.0.1` |
| Maturity | Implemented core |
| Installation state | **Blocked — Serenity host lifecycle is unverified** |
| Legacy source | `sayuga/AdminLTE-Widgets-in-Typscript`, commit `2925ee6fc4ab4fa1753798bbe92ea0eddbae883a` |
| Last reviewed | 2026-09-24 |

| Lane | Serenity | Runtime | Compatibility evidence | Core test | Host installation test |
| --- | --- | --- | --- | --- | --- |
| Legacy | 9.2.x | .NET 8 | Planned | Passed (TypeScript core) | Not tested |
| Current | 10.5.2 | .NET 10 | Planned | Passed (TypeScript core) | Not tested |

## Intended workflow

Import one builder, pass typed text/data/action options, receive an `HTMLElement`,
and append it to a host-owned target. The caller owns placement and disposal.

## Scope and non-goals

Version 0.1.0 includes info cards, stat cards, collapsible panels, progress, and
empty states. Charts, FullCalendar, chat, comments, feeds, and vendor adapters
are deferred because they have separate dependencies and security lifecycles.

## Architecture and APIs

Builders take `HTMLElement`/`Node` values and use `textContent`; they do not look
up arbitrary element IDs or accept raw HTML. Styling consumes semantic SaySol
variables with fallbacks, so Theme Kits is optional.

## Dependencies and integrations

No runtime dependencies. Theme Kits is an optional integration. Chart and
calendar libraries will be separate adapters rather than mandatory dependencies.

## Security and data integrity

Dynamic content is emitted as text. URLs remain explicit action properties and
must be validated by the host. User-provided icon markup, scripts, event strings,
and raw HTML are not supported. Server authorization still controls all widget data.

## Installation and configuration

Installation is blocked. A verified manifest will declare exact TypeScript/CSS
placement and bundler integration without installing AdminLTE implicitly.

### Installation testing state

- Legacy source inventory and redesign decision: completed.
- Manifest/schema validation: passed.
- TypeScript 5.9.3 strict type-check: passed.
- Serenity 9.2 bundling/lifecycle test: not tested.
- Serenity 10.5.2 bundling/lifecycle test: not tested.
- Keyboard, screen reader, responsive, upgrade, and uninstall tests: not tested.

## Validation

Validate text escaping, link behavior, progress bounds, focus, collapse state,
screen-reader names, keyboard use, responsive grids, repeated rendering,
listener disposal, all theme kits, and host authorization failures.

## Upgrade, repair, and uninstall

Upgrades preserve public option names or document migrations. Repair may replace
only capsule-owned assets. Uninstall removes assets/imports without deleting host
dashboard content. There are no migrations.

## Troubleshooting and limitations

The capsule does not reproduce every AdminLTE widget. Vendor-backed charts and
calendars require future adapter capsules or optional modules.

## Source and implementation links

- Capsule: `src/Tools/WidgetLibrary/`
- Legacy concept source: <https://github.com/sayuga/AdminLTE-Widgets-in-Typscript>
- Manifest: `src/Tools/WidgetLibrary/capsule.yaml`
- Evidence ledger: `src/Tools/WidgetLibrary/EVIDENCE.md`
