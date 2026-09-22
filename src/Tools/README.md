# Serenity tool capsules

Each child directory is one independently installable tool capsule. Capsules may
depend on `Serenity.SaySolShared` but should not depend directly on one another
unless an explicit optional integration is documented.

The first planned capsule is `SpreadsheetImport`. Capsule directories are
created when implementation begins; speculative empty packages are avoided.

Use `templates/ToolCapsule/` when creating a capsule. Do not mark a capsule
installable until its manifest validates against the repository schema and its
declared installation has been tested in every claimed Serenity lane.
