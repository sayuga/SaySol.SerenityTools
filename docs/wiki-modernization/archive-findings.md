# Archive review findings

Baseline: 141 pages under `wiki-archive/` at commit
`1c00f72c177fd7410c9f17d992f4d60115b0163a`.

## What the archive contains

The archive is not merely discarded documentation. It mixes several different
kinds of material:

- feature designs that remain useful, such as column-mapped import, optimistic
  concurrency, dynamic navigation, background jobs, audit trails, and reusable editors;
- older implementations tied to namespace TypeScript, `Q`, jQuery, MVC/System.Web,
  Bootstrap-era markup, or retired browser behavior;
- copies or summaries of old official API documentation;
- pointers to samples or gists without enough local content to maintain;
- placeholder pages with no recoverable implementation.

## Measured legacy indicators

The initial source scan found:

| Indicator | Pages |
| --- | ---: |
| jQuery references | 43 |
| namespace-style TypeScript | 37 |
| `Q` API references | 33 |
| decorator registration | 17 |
| ASP.NET MVC/System.Web-era APIs | 14 |
| text copied or summarized from official documentation | 12 |
| external sample/gist pointers | 9 |
| fewer than 10 lines | 13 |
| more than 200 lines | 20 |

These are triage indicators, not automatic rejection rules. A useful behavior
may survive even when its implementation should be replaced completely.

## Initial disposition

| Disposition | Pages |
| --- | ---: |
| Modernization candidates | 86 |
| Security/integrity research required | 12 |
| Replace with version-matched official documentation | 25 |
| Replace with current native Serenity feature | 2 |
| Priority modernization: Excel import | 1 |
| Obsolete implementation retained for history | 5 |
| Placeholder/reject | 10 |

## Consolidation opportunities

Several topics should be handled as families instead of producing one package
or recipe per historical page:

- Excel/PDF/CSV export and Excel import.
- SignalR notification variants.
- Lookup creation, filtering, refresh, and parameterization.
- Grid formatting, selection, sizing, paging, and inline editing.
- Form visibility, readonly state, labels, categories, and default values.
- Attribute pages that should defer to current official API documentation.
- Audit logging, audit-detail UI, and notification-after-save patterns.
- Login layout, user image, startup routing, and navigation customization.

This family approach avoids preserving old duplication and supports the intended
small, composable tool-capsule model.

## Review boundary

Every archive file has now been accounted for and triaged. Only entries promoted
to `source-verified` have been checked closely enough against a tagged current
Serenity source tree to guide implementation. Build compatibility remains a
separate gate.
