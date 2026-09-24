# Installation Model

SerenityTools is designed for a “select capsules, preview changes, approve, and
apply” workflow rather than copying the entire repository into an application.

## Import sequence

1. Import or reference the SerenityTools source.
2. Read `catalog.yaml` and display tools by maturity.
3. Inspect the target host and produce facts for Serenity, .NET, capabilities,
   repository, branch, HEAD, and worktree state.
4. Select one or more verified/released capsules.
5. Run the resolver to expand dependencies and detect conflicts.
6. Review the dry-run plan, including files, packages, root edits, migrations,
   ownership claims, validation, and human gates.
7. Stage and apply the approved transaction.
8. Validate, then write `.saysol/saysol.lock.yaml` and capsule receipts.

## Installation records

| Record | Purpose |
| --- | --- |
| `catalog.yaml` | What exists and whether it is selectable |
| `capsule.yaml` | Exact operations authorized for one capsule |
| `.saysol/saysol.lock.yaml` | Resolved versions and manifest hashes installed in a host |
| `.saysol/installed/<id>.json` | Paths, edits, migrations, and evidence for one capsule |

## Safety behavior

Installation stops on ambiguous projects or anchors, unsupported lanes,
dependency cycles, package-version conflicts, ownership collisions, missing
capabilities, or an unapproved human gate. Applied database migrations are
forward-only and are not automatically removed during uninstall.

## Current implementation status

The resolver is read-only. Transaction staging, apply, repair, and uninstall
execution remain planned. Until that apply engine exists and a capsule is
verified, manifests document and validate intent but do not authorize manual
approximation of missing operations.
