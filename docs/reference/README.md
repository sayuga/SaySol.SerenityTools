# Serenity reference system

This directory records the facts that affect SaySol.SerenityTools compatibility.
It is intentionally smaller than the Serenity changelog: only changes that alter
installation, extension code, generated code, build tooling, or runtime behavior
belong here.

## Updating the reference

For each Serenity release adopted by this project:

1. Record the exact upstream tag and commit.
2. Review official release notes and the tagged source.
3. Add material changes to `version-ledger.md`.
4. Re-evaluate every manifest entry and package compatibility claim.
5. Run the validation matrix before widening a supported version range.

Official release notes and tagged source take priority over community examples.
GitHub evidence takes priority over summaries produced by an agent or contributor.
