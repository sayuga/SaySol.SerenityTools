# Wiki-to-capsule consolidation map

This map determines whether overlapping wiki functionality becomes one capsule,
shared infrastructure, a documentation-only reference, or separate tools.
Archive IDs refer to `archive-manifest.md`; active IDs refer to `manifest.yaml`.

## Approved consolidation families

| Capsule or outcome | Representative wiki items | Decision | Shared candidate |
| --- | --- | --- | --- |
| `SpreadsheetImport` | ARC-053 and the original Serenity Excel import sample it extends | One dedicated import capsule | Operation results, validation messages, temporary-operation tokens after a second consumer |
| `GridExport` | WIKI-002, WIKI-003, ARC-092 through ARC-095 | Merge duplicate Excel/PDF instructions and related CSV/export guidance; expose formats as optional features | Grid request/visible-column capture only if custom code remains beyond native helpers |
| `NotificationCenter` | ARC-001, ARC-077, ARC-091, ARC-127 | Merge SignalR variants and notification UI concepts into one current ASP.NET Core/Serenity notification capsule | Current-user abstraction and standard operation results |
| `LookupToolkit` | ARC-005, ARC-016, ARC-069, ARC-083 through ARC-086, ARC-099, ARC-100 | Merge lookup parameterization, filtering, refresh, direct-grid editing, and cache invalidation behind one coherent API | Stable field identifiers and operation results |
| `FormState` | ARC-090, ARC-101 through ARC-103, ARC-119 through ARC-124, ARC-132, ARC-133, ARC-138, ARC-139 | Merge readonly, visibility, labels, categories, defaults, and field messages | DOM/widget compatibility adapter if also required elsewhere |
| `SignatureEditor` | ARC-028 and ARC-104 | Merge duplicate SignaturePad implementations into one editor capsule | Registration/localized text conventions |
| `ColorEditor` | ARC-012 and ARC-113 | Merge duplicate color-picker material; reject empty page as an implementation source | Registration/localized text conventions |
| `GridPaging` | WIKI-007 and ARC-065 | Merge next/previous and no-total-count paging approaches into one configurable paging capsule | Grid lifecycle adapter if reused by other grid capsules |
| `GridSelection` | ARC-071 and selection portions of grid samples | One focused selection capsule | Grid lifecycle adapter after reuse is proven |
| `GridLayout` | ARC-058, ARC-073 through ARC-076, ARC-128, ARC-129 | Merge sizing, column-picker, formatter, width, full-size, and detail-height patterns where APIs overlap | Grid lifecycle and persisted-settings contracts |
| `GridEditing` | ARC-005, ARC-013, ARC-070 and related inline/master-detail editing | Merge direct editing, conditional edit links, and sortable detail behavior only after interaction design review | Form-state contracts only if no coupling is introduced |
| `AuditTrail` | ARC-006 and ARC-007; coordinate with WIKI-012 | Merge audit storage and audit-detail presentation; replace old handlers with current behavior/handler contracts | Current-user, operation result, and time-provider abstractions |
| `BackgroundJobs` | ARC-008 and ARC-009 | Merge queue-processing and Hangfire concepts into provider-neutral job contracts with optional adapters | Current-user context propagation and operation results |
| `FileTransfer` | ARC-002, ARC-054, ARC-055 and WIKI-008 | Consolidate upload confirmation, large upload, download, and storage-provider concerns only at the contract level; keep storage implementations optional | Temporary tokens, file metadata, operation results |
| `NavigationToolkit` | ARC-010, ARC-021, ARC-118, ARC-126 | Merge startup routing, dynamic navigation, and navigation grouping | Permission/current-user abstractions |
| `LoginExperience` | ARC-115, ARC-131, ARC-137 | Merge login appearance and user-image ideas; keep authentication itself out of this capsule | Localized texts only |
| `DirectoryAuthentication` | WIKI-004 | Remains a separate security-sensitive adapter, not part of LoginExperience | Current-user contract only; credential validation never shared |
| `OptimisticConcurrency` | ARC-020 | Separate data-integrity capsule | Operation conflict result contract |
| `MultiDatabaseRouting` | ARC-017 and ARC-019 | Merge database-selection ideas into one reviewed routing architecture | Connection-context abstraction only if other capsules consume it |
| `InAppHelp` | WIKI-001 | Separate optional feature module | Upload/storage and authorization contracts only after stable shared consumers exist |

## Documentation-only groups

The Entity Framework attribute pages, framework-attribute index, FAQ, and
troubleshooting copies do not become capsules. Their durable value is captured
as lessons or version-matched links to official documentation. Reimplementing
official API reference content would create an avoidable maintenance fork.

## Items that should not be merged merely because they mention the same file type

- `SpreadsheetImport` and `GridExport`: import mutates data and requires preview,
  validation, authorization, transaction, and idempotency controls; export does not.
- `FileTransfer` and `DatabaseUploadStorage`: the interface may be shared, while a
  database-backed storage provider remains an optional implementation.
- `LoginExperience` and `DirectoryAuthentication`: presentation and authentication
  have different threat models and deployment requirements.
- `AuditTrail` and `NotificationCenter`: audit evidence must remain durable and
  independent even if audit events can optionally trigger notifications.
- `BackgroundJobs` and email/notification tools: scheduling is infrastructure;
  message delivery is a consumer or adapter.

## Shared extraction candidates by confidence

| Candidate | Confidence | Decision |
| --- | --- | --- |
| Standard operation/validation result contracts | High | Add to Shared with first implemented capsule |
| Stable type-name and field-identifier helpers | High | Add to Shared when the first editor/import capsule needs them |
| Compatibility-lane adapter boundary | High | Establish in Shared before dual-lane implementation |
| Current-user and permission abstraction | Medium | Add after AuditTrail and NotificationCenter requirements align |
| Temporary upload/preview token | Medium | Keep in SpreadsheetImport until FileTransfer proves identical needs |
| Grid lifecycle helper | Medium | Keep local until two grid capsules share tested behavior |
| Workbook reader/writer abstraction | Low | Keep in SpreadsheetImport; export currently relies on native Serenity helpers |
| Generic repository or base request handler | Rejected | Too coupled to framework internals and the 10.5 async transition |
