# Admin Configuration capsule

Version: 0.2.0
Maturity: implemented contracts; not Serenity-host verified

Admin Configuration defines a standardized administrator-only landing surface
for safe application identity, branding, environment display, database-profile
references, and health state.

It never returns, accepts, logs, or stores database connection strings,
credentials, tokens, or secret values. `LocalDB`, sandbox/failover, and
production targets are represented by non-secret profile keys whose actual
connections remain in environment variables, user secrets, a vault, or another
host-owned configuration provider.

Authorization must be enforced by the server for page access, read, update,
probe, and target-change operations. A hidden navigation link is not security.
Updates require an expected revision to prevent administrators overwriting each
other, and environment/database target changes require an auditable human gate.

No database schema or migration is included in 0.2.0. Persistence is an explicit
provider decision to be proven in both Serenity host lanes.

See `EVIDENCE.md` for core test results and the remaining host-validation gap.
