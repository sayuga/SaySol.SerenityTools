# Capsule installation prompt

Install this capsule into the identified Serenity host using `capsule.yaml` as
the authoritative instruction set.

1. Report the capsule ID/version and exact target repository, branch, and HEAD SHA.
2. Verify the target's Serenity and .NET versions against the manifest.
3. Resolve only variables declared in the manifest. Stop on missing or ambiguous values.
4. Produce a dry-run table of files, migrations, existing-file edits, packages,
   human gates, and validation steps before changing the host.
5. Do not edit generated Serenity files.
6. Apply only declared operations inside `allowed_write_roots`.
7. For bounded edits, require the declared target, anchor, and occurrence count.
8. Never modify or remove an applied migration. Use a new forward migration only
   when the manifest explicitly declares it and the required gate is approved.
9. Run every declared validation step and treat repository/build evidence as
   authoritative over a success summary.
10. Write the declared install receipt and report all changed paths, unresolved
    items, validation results, and the resulting Git state.

If the manifest is incomplete for this host, stop and propose a manifest change.
Do not improvise an installation that the manifest does not describe.
