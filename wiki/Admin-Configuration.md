# Admin Configuration

## Summary

Admin Configuration defines an administrator-only landing page for safe,
basic application settings: displayed project name, approved logo/favicon asset
paths, theme key, environment identity, database-profile labels, active target,
and connectivity status.

## Version, compatibility, and installation state

| Property | Current value |
| --- | --- |
| Capsule ID | `saysol.serenity.admin-configuration` |
| Capsule version | `0.1.0` |
| Wiki documentation version | `1.0.1` |
| Maturity | Implemented contracts |
| Installation state | **Blocked — authorization and persistence are unverified** |
| Required permission | `Administration:Configuration` |
| Last reviewed | 2026-09-24 |

| Lane | Serenity | Runtime | Compatibility evidence | Core test | Host installation test |
| --- | --- | --- | --- | --- | --- |
| Legacy | 9.2.x | .NET 8 | Planned | Passed | Not tested |
| Current | 10.5.2 | .NET 10 | Planned | Passed | Not tested |

## Intended workflow

An authorized administrator opens one configuration landing page, reviews the
current environment and safe database-profile metadata, updates branding with
an expected revision, probes an approved profile, or requests a guarded target
change with a reason and explicit confirmation phrase. Every change is audited.

## Scope and non-goals

The capsule models branding, deployment environment, LocalDB/sandbox/production/
failover profile references, optimistic revision control, connectivity status,
authorization, storage, and audit interfaces. It does not expose secrets, act as
a general appsettings editor, or permit arbitrary connection-string entry.

## Architecture and APIs

The server returns `AdminConfigurationSnapshot` containing only safe metadata.
`SecretReferenceKey` names a host-owned environment/vault entry; it is not the
secret. Branding updates and database-profile changes are separate commands so
the higher-risk operation can require a dedicated gate and audit record.

## Dependencies and integrations

The host must provide permission and configuration providers. Theme Kits,
Widget Library, and Audit Trail are optional. No Shared dependency is required.

## Security and data integrity

- Enforce authorization server-side on page, read, update, probe, and switch.
- Never return/store/log connection strings, passwords, tokens, or secret values.
- Use expected revision checks to reject stale concurrent updates.
- Require a reason, confirmation, and human gate for database-profile changes.
- Allow only preconfigured profile keys; never accept arbitrary server/database input.
- Redact probe failures and use bounded timeouts to avoid infrastructure disclosure.
- Record actor, action, prior/result revision, safe changed fields, and outcome.

## Installation and configuration

Installation is blocked. Version 0.1.0 declares no navigation edits, startup
registration, persistence provider, or migrations because those host operations
have not yet been proven.

### Installation testing state

- Contract compilation on .NET 8/.NET 10 and manifest/schema validation: passed.
- Non-secret model review: completed.
- Serenity 9.2 permission/navigation/endpoint test: not tested.
- Serenity 10.5.2 permission/navigation/endpoint test: not tested.
- Persistence, concurrency, profile switch, audit, upgrade, and uninstall: not tested.

## Validation

Test direct unauthorized API calls, forged role/UI state, stale revisions,
unknown profiles, missing secret references, timeouts, failed probes, concurrent
admins, audit failure, production confirmation, response/log redaction, XSS in
display fields, logo path restrictions, and restart behavior.

## Upgrade, repair, and uninstall

Upgrades preserve branding and profile keys. Repair must not overwrite host
secret providers. Uninstall removes navigation/endpoints and capsule-owned safe
settings only after export/approval. Applied migrations would remain forward-only;
none exist in 0.1.0.

## Troubleshooting and limitations

This is not a secrets-management interface. A profile reported unavailable may
reflect a redacted provider/configuration failure; detailed secret diagnostics
belong in protected server operations, not the browser response.

## Source and implementation links

- Capsule: `src/Tools/AdminConfiguration/`
- Manifest: `src/Tools/AdminConfiguration/capsule.yaml`
- Evidence ledger: `src/Tools/AdminConfiguration/EVIDENCE.md`
- Installation architecture: `docs/architecture/manifest-installation.md`
