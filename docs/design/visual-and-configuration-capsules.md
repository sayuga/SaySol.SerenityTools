# Visual and configuration capsule decisions

Status: initial cores implemented; host integration unverified

## Boundaries

Three independent capsules cover the requested concerns:

| Capsule | Owns | Does not own |
| --- | --- | --- |
| Theme Kits | Semantic tokens, registered theme keys, base palettes | Logo storage, user preference persistence, Serenity layout markup |
| Widget Library | Safe DOM builders and widget CSS | Data authorization, charts/calendar vendors, theme persistence |
| Admin Configuration | Safe settings contracts, profile references, authorization/storage/audit seams | Secret values, arbitrary appsettings editing, database credentials |

They integrate optionally but do not require one another. This keeps each
capsule independently usable and avoids turning a visual preference into a
dependency of security-sensitive configuration.

## Legacy widget source review

Concept source: `sayuga/AdminLTE-Widgets-in-Typscript`, master commit
`2925ee6fc4ab4fa1753798bbe92ea0eddbae883a` (last code push in 2017).

Ideas retained:

- info and statistic cards;
- panels with optional collapse behavior;
- progress and status presentation;
- reusable typed options rather than repeated page markup;
- future chart, calendar, comment, and chat adapters.

Implementation replaced:

- internal TypeScript modules/namespaces;
- decorator-era Serenity registration;
- AdminLTE 2 and legacy Bootstrap classes;
- string element IDs and global document lookup;
- raw `innerHTML` composition and HTML-bearing count/content strings;
- bundled chart/calendar assumptions;
- unowned event listeners and missing disposal contracts.

## Configuration safety decision

Database choices are named profiles. A profile exposes a display label,
provider, environment kind, active/enabled state, and a non-secret reference
key. The referenced connection material remains in a host environment variable,
user-secret store, vault, or equivalent provider.

The browser may never receive the resolved connection string. Switching the
active target is distinct from ordinary branding updates and requires server
authorization, expected revision, a reason, confirmation, human gate, bounded
connectivity check, and audit evidence.

## Shared decision

No new Shared code is introduced. Theme tokens belong to Theme Kits; DOM
builders belong to Widget Library; configuration authorization/storage contracts
belong to Admin Configuration. Promotion will be reconsidered only after another
capsule proves an identical framework-light contract.
