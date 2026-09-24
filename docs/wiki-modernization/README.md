# Serenity wiki modernization

The upstream Serenity wiki is community-maintained and distinct from official
framework documentation. Its current repository snapshot contains 156 Markdown
files: 15 active root files and 141 files retained under `wiki-archive/`.

The YAML manifest covers the 15 active root files in detail. The companion
`archive-manifest.md` accounts for all 141 archived files and gives each an
initial category and disposition. Together they provide complete file-level
coverage of the current 156-file snapshot. Archive entries marked `triaged`
still require current-source verification before they can claim compatibility.

## Source baseline

- Repository: `serenity-is/Serenity.wiki`
- Commit: `1c00f72c177fd7410c9f17d992f4d60115b0163a`
- Commit date: 2025-06-22
- Stated compatibility: Serenity 8.8.1
- Modernization target reviewed here: Serenity 10.5.2
- Minimum supported target: Serenity 10.5.x
- Earlier versions: provenance and concept research only; no compatibility testing

## Dispositions

- `modernize`: rewrite as a current recipe or reusable package.
- `replace-native`: point users to a framework-native feature and document only
  the minimal integration.
- `research`: useful concept, but implementation requires security or architecture work.
- `archive`: historically useful but not a current integration candidate.
- `reject`: empty, placeholder, unsafe, or too incomplete to publish as guidance.
- `meta`: wiki navigation or contribution content, not a product integration.

The machine-readable active-page source of truth is `manifest.yaml`; the full
archive census is `archive-manifest.md`. Modernized recipes must link back to
their manifest ID and source URL.
