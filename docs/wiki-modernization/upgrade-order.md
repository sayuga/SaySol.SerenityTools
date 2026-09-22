# Wiki modernization order

| Order | Manifest ID | Topic | Planned result | Reason |
| --- | --- | --- | --- | --- |
| 1 | WIKI-002 | Excel export | Native-helper recipe | Fast, low-risk simplification and foundation for import UX |
| 2 | New track | Excel import with column mapping | Reusable package | Highest operational value and explicit project priority |
| 3 | WIKI-003 | PDF export | Native-helper recipe | Similar low-risk replacement of legacy syntax |
| 4 | WIKI-012 | Request handler lifecycle | Versioned reference | 10.5 async changes affect many future server tools |
| 5 | WIKI-007 | Next/previous pager | Grid extension | Contained UI modernization candidate |
| 6 | WIKI-008 | Database upload storage | Hardened provider or rejection record | High value but high integrity/security burden |
| 7 | WIKI-004 | Directory authentication | Architecture guide, not password shim | Security-sensitive and environment-dependent |
| 8 | WIKI-009 | Exception logging | Provider-neutral observability recipe | Security, privacy, and retention review needed |
| 9 | WIKI-001 | In-app help | Optional feature module | Large product surface; separate from core tooling |

Empty, placeholder, and wiki-navigation pages remain in the manifest for
completeness but will not be converted into recipes.
