# Serenity wiki modernization

The upstream Serenity wiki is community-maintained and distinct from official
framework documentation. Its current repository snapshot contains 156 Markdown
files: 15 active root files and 141 files retained under `wiki-archive/`.

The first-pass manifest currently covers only the 15 active root files. It is
therefore an active-page manifest, not yet a complete wiki manifest. The archive
census and technical review must be completed before this project claims full
wiki coverage. The archive includes useful material such as the extended Excel
import and column-mapping article.

## Source baseline

- Repository: `serenity-is/Serenity.wiki`
- Commit: `1c00f72c177fd7410c9f17d992f4d60115b0163a`
- Commit date: 2025-06-22
- Stated compatibility: Serenity 8.8.1
- Modernization target reviewed here: Serenity 10.5.2
- Secondary supported target: Serenity 9.2.x

## Dispositions

- `modernize`: rewrite as a current recipe or reusable package.
- `replace-native`: point users to a framework-native feature and document only
  the minimal integration.
- `research`: useful concept, but implementation requires security or architecture work.
- `archive`: historically useful but not a current integration candidate.
- `reject`: empty, placeholder, unsafe, or too incomplete to publish as guidance.
- `meta`: wiki navigation or contribution content, not a product integration.

The machine-readable source of truth for the completed scope is `manifest.yaml`.
Modernized recipes must link back to their manifest ID and source URL.
