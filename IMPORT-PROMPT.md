# SerenityTools import prompt

Import selected SaySol SerenityTools capsules into a Serenity host. Treat
`catalog.yaml`, each selected `capsule.yaml`, and their schemas as the only
authorities for automated changes.

## Required sequence

1. Identify the exact target repository, branch, and HEAD SHA. Require a clean
   or explicitly acknowledged worktree.
2. Inspect host capabilities and write a facts file matching
   `schema/host-facts.schema.json`. Do not infer compatibility from a directory
   name alone.
3. Show catalog choices by maturity. Only `verified` or `released` capsules with
   a manifest may be installed. A `planned`, `design`, or `recipe` item is not
   installable software.
4. Run `python tools/resolve_install.py --catalog catalog.yaml --host <facts.json>
   --select <capsule-id>`. Resolve required dependencies; list optional
   integrations without selecting them automatically.
5. Stop on an unsupported lane, missing capability, dependency cycle, conflict,
   superseded selection, duplicate ownership claim, or ambiguous host target.
6. Present the complete dry-run plan and all human gates. Do not mutate the host
   during resolution.
7. If approved, stage all changes under the catalog transaction directory,
   verify path scope and hashes, then apply them as one transaction.
8. Run the validation ladder: manifest/schema checks, restore/install, compile,
   automated tests, and required behavioral checks.
9. Write or update `.saysol/saysol.lock.yaml` and the per-capsule receipts only
   after successful validation. Never store secrets in either file.
10. Report changed paths, validation evidence, migrations, gates, and resulting
    Git state. On failure, restore pre-transaction files; never reverse an
    already-applied migration automatically.

## Modes

- `install`: add a capsule not present in the lockfile.
- `upgrade`: compare locked and selected manifests, preserving user-owned data.
- `repair`: verify managed hashes and reapply only missing or altered owned data
  after explicit approval.
- `uninstall`: remove capsule-owned artifacts and exact managed insertions;
  applied migrations remain forward-only.

The importer may explain a conflict or propose a manifest correction. It may
not invent edits, dependencies, migrations, destination paths, or compatibility
claims absent from the manifests.
