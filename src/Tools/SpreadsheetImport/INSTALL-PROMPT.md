# Spreadsheet Import installation prompt

This capsule is not currently installable. Its catalog maturity is
`implemented`, and its compatibility evidence is `planned`.

Use the root `IMPORT-PROMPT.md` and `capsule.yaml` to inspect or dry-run the
capsule. Do not copy it into a host, add packages, create endpoints, register
services, or manufacture migrations until the catalog maturity is `verified`
or `released` and the manifest contains the proven lane-specific operations.

When verification is complete, installation must still:

1. resolve exactly one Serenity host and compatibility lane;
2. enforce every declared ownership claim and allowed write root;
3. install only the adapter for the selected lane;
4. obtain any declared database or root-edit gates;
5. run all declared build and behavioral checks; and
6. write the lockfile and capsule receipt only after successful validation.
