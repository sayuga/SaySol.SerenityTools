# Tool Name

## Summary

State the user problem, intended outcome, and whether this is a capsule, recipe,
design, or retired tool.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Capsule ID | `saysol.serenity.example` |
| Tool/capsule version | `0.0.0` or Not packaged |
| Wiki documentation version | `1.0.0` |
| Maturity | Planned |
| Installation state | Blocked, recipe-only, verified, released, or retired |
| Last reviewed | YYYY-MM-DD |
| Source wiki items | List modernization IDs |

| Lane | Serenity | Runtime | Compatibility evidence | Core test | Host installation test |
| --- | --- | --- | --- | --- | --- |
| Legacy | Exact version/range | Exact .NET | Label | State | State |
| Current | Exact version/range | Exact .NET | Label | State | State |

## Intended workflow

Describe the operator's normal sequence and visible results.

## Scope and non-goals

List implemented behavior, exclusions, and boundaries with other capsules.

## Architecture and APIs

Explain the host surface, configuration, optional providers, and Shared usage.

## Dependencies and integrations

Separate required, optional, conflicting, superseded, and host-provided items.

## Security and data integrity

Document permissions, trust boundaries, sensitive data, validation, transactions,
idempotency, logging, and irreversible effects.

## Installation and configuration

Summarize the manifest-driven path. Never add operations absent from
`capsule.yaml`.

### Installation testing state

List schema, resolver, dry-run, host install, upgrade, repair, uninstall,
migration, and rollback evidence separately. Use `not-tested` explicitly rather
than leaving an unknown state blank.

## Validation evidence

Link exact commits/runs and distinguish core, adapter, and host evidence.

## Upgrade, repair, and uninstall

Explain owned files, managed edits, data preservation, migrations, and gates.

## Troubleshooting and limitations

List known failure modes, diagnostic evidence, and current unsupported cases.

## Source and implementation links

Link the capsule, design/recipe, source inventory IDs, and compatibility record.
