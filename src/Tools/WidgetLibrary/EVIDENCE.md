# Widget Library evidence ledger

Evidence is additive. Passing the core checks below does not establish
Serenity-host compatibility or make the capsule installable.

## Core proof — 2026-09-24

- Repository commit: `78cce317912c089b41bc2998888b83d392753c7a`
- GitHub Actions run: <https://github.com/sayuga/SaySol.SerenityTools/actions/runs/35946788597>
- Repository contracts and manifest validation: passed
- Python capsule tests: passed (11-test repository suite)
- TypeScript 5.9.3 strict type-check: passed
- Raw-HTML API guard (`innerHTML`/`insertAdjacentHTML`): passed
- Text-content API guard: passed

The legacy design source was reviewed at commit
`2925ee6fc4ab4fa1753798bbe92ea0eddbae883a`. Version 0.1.0 retains the widget
concepts while replacing the legacy namespace, decorator, ID-lookup, raw-HTML,
and AdminLTE 2 coupling.

## Native inventory — 2026-09-24

- Serenity tag: `10.5.2`
- Serenity source commit: `72c270aca67f4848c86d63aec830a2d620629690`
- Public export surface reviewed: `packages/corelib/src/index.ts`
- UI source families reviewed: widgets, datagrid, dialogs, editors, filtering,
  formatters, and helpers
- Executable map: `ts/src/native/serenity/index.ts`
- External mapping sample: `ts/src/external/adminlte/index.ts`

This is source-level compatibility evidence. It does not replace compilation
and rendering inside a Serenity 10.5.2 host.

## Evidence still required

Neither Serenity lane has bundled or rendered the widgets in a real host.
Lifecycle/disposal, accessibility, responsive behavior, theme combinations,
upgrade, repair, and uninstall remain unverified.
