# Compatibility

## Supported baseline

| Lane | Serenity baseline | Runtime | Purpose |
| --- | --- | --- | --- |
| Supported | 10.5.2 | .NET 10 | Initial validation benchmark for all new and updated tools |
| Historical | Earlier versions | Not tested | Source interpretation and provenance only |

Compatibility is asserted per capsule, not globally. A successful framework-
light build does not prove that a Serenity endpoint, handler, grid, dialog, or
registration API works in the same lane.

## Evidence labels

- `planned` — intended support that has not been demonstrated.
- `source-verified` — compared with pinned official source but not run in a host.
- `verified` — compiled and behaviorally exercised in the stated host.
- `incompatible` — known to require material redesign.
- `historical` — retained for provenance, not supported use.

Exact build evidence belongs in each tool's evidence ledger. Compatibility
ranges are narrowed when either boundary lacks evidence.

`10.5+` is the repository's compatibility floor. It does not mean every later
10.x release is automatically verified; evidence is recorded against exact
versions, beginning with 10.5.2. Serenity versions below 10.5 are not tested,
supported, or included in installation claims.
