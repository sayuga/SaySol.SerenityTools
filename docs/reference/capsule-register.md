# Capsule register

This register tracks planned and implemented Serenity tool capsules. A planned
entry is an architectural grouping, not a claim that code exists.

| Capsule | State | Primary scope | Shared dependency candidates |
| --- | --- | --- | --- |
| `SpreadsheetImport` | Design | Upload, map, preview, validate, and commit spreadsheet data | Results, validation contracts, compatibility adapter; temporary tokens remain local initially |
| `GridExport` | Recipe/analysis | Native Excel/PDF export plus reviewed CSV option | None until custom cross-format code is demonstrated |
| `NotificationCenter` | Planned | Real-time user/group notifications and notification UI | Current user, permission abstraction, results |
| `LookupToolkit` | Planned | Lookup filtering, parameters, refresh, cache invalidation, and grid use | Stable field identifiers, results |
| `FormState` | Planned | Readonly, visibility, labels, categories, defaults, and messages | UI compatibility adapter after reuse is proven |
| `SignatureEditor` | Planned | Modern SignaturePad Serenity editor | Registration and localization conventions |
| `ColorEditor` | Planned | Modern color editor | Registration and localization conventions |
| `GridPaging` | Planned | Next/previous and no-count paging | Grid lifecycle adapter after reuse is proven |
| `GridSelection` | Planned | Radio/single and related row selection behavior | Grid lifecycle adapter after reuse is proven |
| `GridLayout` | Planned | Sizing, columns, formatters, persistence, and full-size layout | Grid lifecycle and persisted-setting contracts |
| `GridEditing` | Planned | Direct editing and master/detail editing controls | Form-state contract only if decoupled |
| `AuditTrail` | Planned | Durable audit capture and audit-detail UI | Current user, time provider, results |
| `BackgroundJobs` | Planned | Provider-neutral job definitions and optional schedulers | Context propagation and results |
| `FileTransfer` | Planned | Upload/download workflow and optional storage providers | File metadata and temporary-token contracts after proven reuse |
| `NavigationToolkit` | Planned | Startup route and dynamic navigation | Current user and permissions |
| `LoginExperience` | Planned | Login presentation and user imagery | Localization conventions |
| `DirectoryAuthentication` | Research | Environment-specific directory identity integration | Current-user contract only |
| `OptimisticConcurrency` | Research | Row-version conflict detection and UX | Conflict result contract |
| `MultiDatabaseRouting` | Research | Controlled database/tenant routing | Connection context if reused |
| `InAppHelp` | Research | Optional help authoring and contextual help | Authorization and storage contracts after proven reuse |

## Register update rule

When a wiki article is source-verified, its review must state:

1. whether it maps to an existing capsule;
2. whether it should merge with another article;
3. whether any reusable portion is a Shared candidate;
4. whether that candidate has enough proven consumers to be promoted; and
5. what new dependencies the decision adds to a consumer project.
