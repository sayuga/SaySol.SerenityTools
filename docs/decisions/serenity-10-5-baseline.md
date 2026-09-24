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
