# Serenity wiki modernization

The upstream Serenity wiki is community-maintained and distinct from official
framework documentation. Its current repository snapshot contains 15 Markdown
files. Two are empty and two contain only placeholder text.

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

The machine-readable source of truth is `manifest.yaml`. Modernized recipes must
link back to their manifest ID and source URL.
