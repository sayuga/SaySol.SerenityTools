# Serenity 10.5+ compatibility baseline

Status: accepted  
Effective: 2026-09-24

All SaySol.SerenityTools development, modernization, installation design, and
host validation begins at Serenity 10.5 on .NET 10. Serenity 10.5.2 is the first
exact validation benchmark.

## Consequences

- Capsule manifests declare only the `net10` compatibility lane with a minimum
  Serenity version of 10.5.0.
- CI compiles .NET capsule proofs on .NET 10 only.
- New adapters use current Serenity registration, handler, behavior, nullable,
  and TypeScript conventions.
- Versions earlier than 10.5 may be examined to understand source provenance or
  migrations, but they are not supported and receive no regression testing.
- A successful framework-light build on an older runtime is not compatibility
  evidence.
- `10.5+` is an intended floor, not an unlimited claim. Each verified range must
  still be supported by exact-version host evidence.

The change deliberately removes the earlier Serenity 9 adapter and validation
lane so future work cannot accidentally imply legacy support.

## Validation evidence

- Repository commit: `34ba96e3b8a0bf9735735c799676081bbc157eb5`
- GitHub Actions run: <https://github.com/sayuga/SaySol.SerenityTools/actions/runs/36045449950>
- Repository contracts and 14 Python tests: passed
- All TypeScript capsule checks: passed
- Spreadsheet Import and Admin Configuration .NET 10 proofs: passed
- GitHub Wiki synchronization: passed
