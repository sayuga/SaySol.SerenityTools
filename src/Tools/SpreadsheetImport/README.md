# Spreadsheet Import capsule

Version: 0.1.0  
Maturity: implemented core; not installable or compatibility-verified

Spreadsheet Import provides framework-light contracts and deterministic column
mapping for a future Serenity upload, preview, validation, and commit workflow.
It modernizes archived wiki item `ARC-053` without retaining its decorator,
namespace, display-title-key, dynamic-value, or conversion-side-effect patterns.

## Current scope

Included now:

- stable field keys and explicit aliases;
- deterministic header normalization and mapping;
- explicit unmapped, ambiguous, and duplicate-target outcomes;
- bounded import limits and profile contracts;
- typed preview, validation, token-store, and commit interfaces;
- separate Serenity 9.2 and 10.5 adapter seams;
- TypeScript request/response contracts;
- a manifest declaring intended placement and ownership.

Not included yet:

- a ClosedXML workbook reader;
- temporary file/token persistence;
- Serenity endpoints, permission integration, or dependency injection registration;
- mapping/preview dialog and grid button;
- database migrations;
- compiled host evidence for either compatibility lane.

The root resolver therefore rejects this capsule while its catalog maturity is
`implemented`. It may move to `verified` only after the proof-host checklist in
`VALIDATION.md` passes.

## Layout

- `dotnet/Core` — framework-light contracts and mapping behavior.
- `dotnet/Adapters/Serenity9` — .NET 8 / Serenity 9.2 adapter seam.
- `dotnet/Adapters/Serenity10` — .NET 10 / Serenity 10.5 adapter seam.
- `ts/src` — transport contracts with no direct Serenity dependency yet.
- `capsule.yaml` — bounded installation intent.
- `INSTALL-PROMPT.md` — capsule-specific prompt boundary.
- `VALIDATION.md` — evidence required before release.

## Shared decision

Nothing in this increment is promoted to `Serenity.SaySolShared`. Mapping and
preview contracts currently have only one consumer. If FileTransfer or another
capsule later proves identical token, validation, or operation-result behavior,
the shared-promotion rule will be reevaluated with real consumers.

## Migration decision

Version 0.1.0 owns no database objects and declares no migrations. Durable audit
storage, saved mappings, and token persistence remain host-provider decisions
until their cross-host requirements are proven. Adding schema later requires a
new manifest version and an explicit database-change gate.

## Security boundary

These contracts do not authorize a user or trust uploaded content. A host
adapter must enforce permissions independently on discovery, preview, and
commit; bind preview tokens to user/profile/file hash; enforce workbook limits;
and revalidate all data inside the commit transaction.
