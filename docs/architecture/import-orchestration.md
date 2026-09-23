# Toolset import orchestration

Status: dry-run resolver implemented; transactional apply engine planned

## Authority chain

The root importer uses four layers, each with a narrower responsibility:

| Artifact | Responsibility |
| --- | --- |
| `catalog.yaml` | Discoverable items, maturity, delivery type, compatibility lanes, and manifest location |
| `capsule.yaml` | One capsule's dependencies, ownership, exact changes, gates, and validation |
| `.saysol/saysol.lock.yaml` | Versions, source identity, manifest hashes, and receipts actually installed in a host |
| `.saysol/installed/<id>.json` | Changed paths, bounded edits, migration state, and validation evidence for one capsule |

The catalog does not authorize host changes. It points to a capsule manifest;
the manifest is the authority for those changes. The lockfile records resolved
state but cannot expand the manifest's scope.

## Discovery and selection

Catalog maturity controls whether an item may be selected:

- `planned`, `design`, and `recipe` are visible but not installable;
- `implemented` has code but insufficient compatibility evidence;
- `verified` and `released` are installable when a manifest is present;
- `retired` remains discoverable for upgrade and removal guidance.

Delivery types are `source-copy`, `nuget`, `npm`, `combined`, `recipe`, and
`migration-only`. One canonical type is declared per catalog version so an
importer never installs both source and package representations accidentally.

## Resolution boundaries

`tools/resolve_install.py` is read-only. It:

1. identifies exactly one host compatibility lane;
2. rejects a dirty or unacknowledged worktree;
3. loads only verified/released manifests referenced by the catalog;
4. expands required capsule dependencies in dependency-first order;
5. checks Serenity, .NET, and declared host capabilities;
6. rejects cycles, conflicts, superseded co-selections, and exclusive ownership collisions;
7. returns files, migrations, edits, gates, validations, and optional integrations as JSON.

Example:

```bash
python tools/resolve_install.py \
  --catalog catalog.yaml \
  --host host-facts.json \
  --select saysol.serenity.some-released-capsule \
  --output install-plan.json
```

The resolver does not copy files, edit a host, run package managers, write a
lockfile, or approve gates. Those operations belong to the future transactional
apply engine.

## Ownership and collisions

Capsules declare claims for paths, routes, permissions, navigation keys, type
keys, database objects, and configuration keys. Policies are:

- `exclusive` — only one selected capsule may claim the key;
- `shared-merge` — multiple manifests may contribute through a bounded merge;
- `host-owned` — the capsule integrates with the key but does not own it.

Copied target paths are implicit exclusive claims. Package version convergence,
resolved edit anchors, and collisions against an existing host lockfile will be
added before the apply engine is enabled.

## Transaction design

The apply phase must stage a complete change set under
`.saysol/transactions/<transaction-id>`, record original hashes, and validate
allowed roots before touching the host. A failed pre-migration transaction must
restore original files. An applied migration remains forward-only and changes
the recovery path into repair or a new compensating migration with a human gate.

## Shared infrastructure

`Serenity.SaySolShared` remains componentized. A capsule declares the smallest
Shared component and compatible version it consumes. Installing one Shared
component must not pull unrelated feature dependencies into the host.
