# Widget Library capsule

Version: 0.3.0
Maturity: implemented TypeScript core; not Serenity-host verified

This capsule now starts with Serenity itself. It inventories the public native
UI options in Serenity 10.5.2, keeps the dependency-free SaySol dashboard
builders separate, and provides a provider/mapping contract for optional
external widget systems.

Version 0.3.0 maps native lifecycle widgets, panels, grids, dialogs, editors,
filters, and formatters. The SaySol layer implements info cards, stat cards,
panels, progress, and empty states. It uses ES modules, strict types,
`HTMLElement` targets, `textContent`, semantic elements, accessible labels, and
CSS variables.

`ts/src/external/` is the extension point for optional providers. Its AdminLTE
subfolder is the worked example: it identifies the 2017 source and maps legacy
concepts to native Serenity or SaySol alternatives without copying the old
namespace/decorator code or adding AdminLTE, chart, or calendar dependencies.

See `EVIDENCE.md` for core test results and the remaining host-validation gap.
See `NATIVE-WIDGET-MAP.md` for the current Serenity inventory.
