# Tool Catalog

The machine-readable catalog is `catalog.yaml`. This page is its human-readable
companion and must not claim a higher maturity than the catalog.

## Available documentation

| Tool | Maturity | Delivery | Installable | Wiki |
| --- | --- | --- | --- | --- |
| Spreadsheet Import | Implemented | Combined .NET/TypeScript | No | [Guide](Spreadsheet-Import.md) |
| Grid Export | Recipe | Recipe | No capsule required | [Guide](Grid-Export.md) |

## Planned capsule families

The following groupings are registered but do not yet have capsule directories
or individual operational pages:

- Notification Center
- Lookup Toolkit
- Form State
- Signature Editor
- Color Editor
- Grid Paging
- Grid Selection
- Grid Layout
- Grid Editing
- Audit Trail
- Background Jobs
- File Transfer
- Navigation Toolkit
- Login Experience
- Directory Authentication
- Optimistic Concurrency
- Multi-Database Routing
- In-App Help

A dedicated page is created when a tool reaches `design`, `recipe`, or
`implemented`. Empty pages for speculative tools are avoided because they tend
to look like support commitments.

## Selection rule

Do not copy folders directly based on this page. Use the root import prompt and
resolver. A tool that is visible here may still be intentionally blocked from
installation while its compatibility evidence is incomplete.
