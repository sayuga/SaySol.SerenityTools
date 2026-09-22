# Manifest-driven capsule installation

Status: accepted architecture baseline

## Purpose

Every installable tool capsule carries a `capsule.yaml`. The manifest tells a
developer, installer, or import prompt exactly what the capsule requires and
which bounded changes may be made to a Serenity host.

The manifest is authoritative. `INSTALL-PROMPT.md` explains how to consume it
but cannot add operations that are absent from the manifest.

## Manifest responsibilities

A complete manifest declares:

- capsule identity and version;
- compatible Serenity, .NET, and Node/package-manager lanes;
- required Shared version and optional capsule dependencies;
- NuGet and npm dependencies;
- variables that must be resolved from the target project;
- source files and exact destination templates;
- migration files, destination, ordering, and forward-only behavior;
- bounded edits to existing root or module files;
- navigation, permission, service-registration, and configuration changes;
- validation commands and behavioral checks;
- upgrade rules;
- uninstall behavior and irreversible effects;
- allowed write scope and human approval gates.

## Operation types

| Operation | Use |
| --- | --- |
| `copy` | Place a new capsule-owned file at a resolved target path |
| `merge-json` | Add declared keys without replacing unrelated configuration |
| `insert-after` | Insert declared content after one exact anchor |
| `insert-before` | Insert declared content before one exact anchor |
| `add-package` | Add an exact NuGet or npm dependency |
| `register-service` | Add an exact dependency-injection registration at a declared anchor |
| `register-navigation` | Add a navigation item or section at a declared host location |
| `migration-copy` | Copy a new forward migration into the host migration sequence |
| `verify-only` | Assert a prerequisite or expected host condition without editing |

Arbitrary search-and-replace, generated-file edits, unconstrained scripts, and
recursive copying are not valid manifest operations.

## Installation workflow

1. Read `capsule.yaml`, its schema version, and `INSTALL-PROMPT.md`.
2. Verify the capsule source identity and the exact target repository, branch,
   and HEAD SHA.
3. Check Serenity/.NET compatibility and all required dependencies.
4. Resolve declared variables from manifest discovery rules. Stop if more than
   one target or anchor matches.
5. Produce a dry-run plan listing every create, edit, package, migration, and
   validation action.
6. Obtain any human gates declared by the manifest.
7. Apply only manifest-declared operations inside `allowed_write_roots`.
8. Validate occurrence counts for every bounded edit.
9. Run declared builds/tests and record their terminal results.
10. Write an install receipt containing capsule version, source commit, target
    commit, resolved variables, changed paths, migration state, and validation evidence.

## Migration rules

- A capsule owns migration templates, not the host's applied migration history.
- Installation copies a new migration into the host's normal migration folder
  and assigns ordering according to the manifest strategy.
- The prompt must inspect existing migrations before selecting a number or timestamp.
- An already-applied migration is never edited, renamed, or deleted.
- Uninstalling code does not roll back an applied database migration.
- Schema reversal, when supported, requires a new forward migration and an
  explicit human gate.

## Existing-file edits

Every edit must declare:

- target path template;
- operation type;
- exact text anchor or structured key;
- expected match count;
- content source or literal content;
- whether a human gate is required; and
- the inverse action used during uninstall.

If the target file, anchor, or expected count differs, installation stops and
reports the mismatch. The prompt does not choose a nearby location by intuition.

Example declarations:

```yaml
installation:
  files:
    - id: "copy-import-endpoint"
      operation: "copy"
      source: "dotnet/Endpoints/SpreadsheetImportEndpoint.cs"
      target: "{{WebProjectPath}}/Modules/SaySol/SpreadsheetImport/SpreadsheetImportEndpoint.cs"
      conflict: "fail"

  migrations:
    - id: "install-import-profile-table"
      operation: "migration-copy"
      source: "dotnet/Migrations/SpreadsheetImportProfileMigration.cs"
      target_directory: "{{MigrationsPath}}/DefaultDB"
      ordering: "next-sequence"
      applied_behavior: "never-modify"
      human_gate: "approve-database-change"

  edits:
    - id: "register-import-services"
      operation: "register-service"
      target: "{{WebProjectPath}}/Startup.cs"
      anchor: "services.AddServices();"
      expected_matches: 1
      content: "services.AddSaySolSpreadsheetImport();"
      content_source: null
      human_gate: null
      inverse: "remove-exact-inserted-content"

    - id: "register-import-navigation"
      operation: "register-navigation"
      target: "{{WebProjectPath}}/Modules/Common/Navigation/NavigationItems.cs"
      anchor: "// <saysol-navigation>"
      expected_matches: 1
      content_source: "integration/NavigationItem.cs.txt"
      content: null
      human_gate: null
      inverse: "remove-exact-inserted-content"
```

The paths and anchors above are illustrative. A real capsule must derive them
from a verified host template for each supported Serenity lane.

## Root-level edits

Changes to project files, `package.json`, application startup, navigation,
permissions, configuration, or migration registration are considered root
integration points. They must be separately listed in the manifest and are
never implied by copying the capsule source folder.

## Install receipt

The default receipt path is:

```text
.saysol/installed/<capsule-id>.json
```

The receipt enables deterministic upgrade and uninstall checks. It must not
contain credentials, secrets, connection strings, or uploaded user data.

## Prompt boundary

The import prompt may explain conflicts, propose a manifest update, or ask for a
missing variable. It may not silently expand scope, manufacture migrations,
select among ambiguous projects, or claim success without build evidence.
