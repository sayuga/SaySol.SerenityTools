# Widget Library capsule

Version: 0.1.0  
Maturity: implemented TypeScript core; not Serenity-host verified

This capsule modernizes the concepts in
`sayuga/AdminLTE-Widgets-in-Typscript` (2017): info boxes, statistic boxes,
panels, progress indicators, lists, charts, and calendar surfaces.

Version 0.1.0 implements the safe common foundation—info cards, stat cards,
panels, progress, and empty states. It uses ES modules, strict types,
`HTMLElement` targets, `textContent`, semantic elements, accessible labels, and
CSS variables. It does not copy the old namespace/decorator code, depend on
AdminLTE 2 classes, accept raw HTML strings, or bundle chart/calendar vendors.

Charts, calendars, chat, and comments remain separate future adapters because
they add independent dependencies, security concerns, and lifecycles.

See `EVIDENCE.md` for core test results and the remaining host-validation gap.
