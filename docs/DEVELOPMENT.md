# Development guide

This document explains how a wiki idea becomes a supported SerenityTools
integration.

The repository follows the [tool-capsule architecture](architecture/capsule-model.md).
Before implementing a wiki idea, check the
[consolidation map](wiki-modernization/consolidation-map.md) to determine whether
it belongs in an existing capsule, a new capsule, Shared, or documentation only.
Record accepted capsules in the [capsule register](reference/capsule-register.md).
All installable capsules must follow the
[manifest-driven installation protocol](architecture/manifest-installation.md).

## Evidence order

1. Tagged Serenity source and official version-matched documentation.
2. Current Serene or StartSharp generated/sample code for the same version.
3. A build and behavioral test in the supported host lane.
4. Community wiki material as a source of ideas and prior art.

A compiling legacy snippet is not evidence of a supported design.

## Modernization states

1. `inventoried` — source identity and location recorded.
2. `triaged` — topic, legacy indicators, and initial disposition recorded.
3. `source-verified` — current framework APIs and native alternatives checked.
4. `implemented` — package or recipe created with a bounded install surface.
5. `verified` — built and behaviorally exercised in each claimed compatibility lane.
6. `released` — versioned artifact, documentation, and removal instructions published.

## Package acceptance criteria

- Installation is explicit, small, and reversible.
- Host-specific behavior is configuration or a narrow adapter.
- Permissions and server-side authorization are enforced independently of UI.
- Generated Serenity code remains generated; packages do not patch generated files.
- Public APIs do not depend on internal request-handler implementation details.
- Every compatibility statement names an exact tested Serenity version.
- Tests include installation, normal use, invalid input, authorization failure,
  upgrade, and removal.
- Documentation explains purpose, prerequisites, installation, configuration,
  operation, limitations, troubleshooting, and uninstall steps.
- `capsule.yaml` validates against `schema/capsule-install.schema.json` and
  declares every file placement, migration, root integration edit, validation,
  and irreversible effect.
- `INSTALL-PROMPT.md` remains bounded by the manifest and cannot authorize
  undeclared changes.
- Root `catalog.yaml` lists the capsule once, with one canonical delivery type
  and a maturity that reflects its evidence.
- Capsule ownership claims do not collide with another released capsule.
- The dry-run resolver succeeds for every claimed host lane and required
  dependency combination before release.

## Dual-lane validation

Until the existing SaySol applications move from .NET 8, integrations should be
designed against two hosts where practical:

- Serenity 9.2.x on .NET 8 / Visual Studio 2022.
- Serenity 10.5.x on .NET 10 / Visual Studio 2026.

Code shared between lanes belongs in a framework-light core. Serenity-version
adapters should be thin and separate when APIs materially differ.

## Repository discipline

- `docs/wiki-modernization/` records provenance and decisions.
- `docs/design/` contains provisional architecture, never install claims.
- `docs/recipes/` contains versioned, bounded instructions.
- `src/Serenity.SaySolShared/` contains proven cross-capsule infrastructure.
- `src/Tools/<ToolName>/` contains independently installable capsules.
- `samples/` and `tests/` provide the evidence for compatibility labels.

Code begins inside its owning capsule. It is promoted to Shared only after the
shared-promotion criteria are met; speculative generalization is not accepted.

When a newer Serenity version is adopted, update the version ledger, re-run the
affected validation matrix, and narrow compatibility claims if evidence is
incomplete.
