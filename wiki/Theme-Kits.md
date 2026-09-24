# Theme Kits

## Summary

Theme Kits provides reusable semantic design tokens and selectable visual kits
without replacing Serenity's layout engine. Initial kits are Light, Dark,
Logistics, and Future.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Capsule ID | `saysol.serenity.theme-kits` |
| Capsule version | `0.2.0` |
| Wiki documentation version | `1.1.0` |
| Maturity | Implemented core |
| Installation state | **Blocked — Serenity host rendering is unverified** |
| Last reviewed | 2026-09-24 |

| Lane | Serenity | Runtime | Compatibility evidence | Core test | Host installation test |
| --- | --- | --- | --- | --- | --- |
| Supported baseline | 10.5.2 | .NET 10 | Planned | Passed (TypeScript core) | Not tested |

## Intended workflow

The host loads the theme CSS before rendering, resolves an allowed theme key,
and applies it to the document root through `data-saysol-theme`. Components use
semantic variables such as surface, text, border, primary, success, warning,
danger, focus, radius, and shadow.

## Scope and non-goals

Version 0.2.0 includes Light, Dark, Logistics, and Future token sets plus typed
theme selection helpers. It does not rewrite Serenity templates, persist user
preference, manage logos, or guarantee third-party chart colors.

## Architecture and APIs

`applyTheme`, `readTheme`, and `isThemeName` form the TypeScript API. Themes are
CSS-variable contracts rather than Bootstrap/AdminLTE color-class replacements.
Hosts can consume the tokens without the Widget Library.

## Dependencies and integrations

There are no runtime npm, Shared, or capsule dependencies. Widget Library and
Admin Configuration are optional integrations. Theme persistence remains host-owned.

## Security and data integrity

Only allow registered theme keys; never turn user input into a stylesheet URL
or raw CSS. Logo and asset paths must be host-controlled. Themes must retain
visible keyboard focus and appropriate contrast for status and interactive states.

## Installation and configuration

Installation is blocked. The future verified manifest will declare exact asset
placement/imports and must install only one copy of the theme stylesheet.

### Installation testing state

- Manifest/schema validation: passed.
- TypeScript 5.9.3 strict type-check: passed.
- Serenity 10.5.2 asset loading and full layout review: not tested.
- Accessibility, no-flash loading, persistence, upgrade, and uninstall: not tested.

## Validation

Validate navigation, forms, grids, dialogs, buttons, validation messages,
disabled states, charts, responsive layout, print output, contrast, keyboard
focus, reduced motion, and operating-system color preference behavior.

## Upgrade, repair, and uninstall

Upgrades must preserve host/user theme selection and avoid silently renaming
keys. Uninstall removes capsule assets and exact managed imports, then restores
a host-defined default theme. No database migrations exist.

## Troubleshooting and limitations

Third-party components that hard-code colors will not automatically inherit the
tokens. Per-user preference and early-load integration remain host work.

## Source and implementation links

- Capsule: `src/Tools/ThemeKits/`
- Manifest: `src/Tools/ThemeKits/capsule.yaml`
- Evidence ledger: `src/Tools/ThemeKits/EVIDENCE.md`
- Catalog: `catalog.yaml`
