# Compatibility

## Supported lanes

| Lane | Serenity baseline | Runtime | Purpose |
| --- | --- | --- | --- |
| Current | 10.5.2 | .NET 10 | New development and forward-looking packages |
| Legacy supported | 9.2.x | .NET 8 | Existing SaySol applications and controlled migration |
| Research | 8.8.1 | .NET 8 | Historical source interpretation only |

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
