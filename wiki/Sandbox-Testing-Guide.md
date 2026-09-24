# Sandbox Testing Guide

The sandbox is the canonical clean control host. The current manifest says
candidate-unvalidated; it is not an approved baseline.

**Do not test a SaySol tool against a sandbox that has not first passed baseline validation.**

## Prerequisites

Use Git, .NET SDK 10.x, Node 24.x, and npm 11.x. Serenity packages and sergen
use the published pins corelib 10.5.1 and tsbuild 10.4.0; NuGet packages and
sergen are 10.5.2. Verify and instantiate:

    git --version
    dotnet --version
    node --version
    npm --version
    ./sandbox/scripts/preflight.sh
    ./sandbox/scripts/instantiate.sh /tmp/saysol-sandbox-run-001
    cd /tmp/saysol-sandbox-run-001
    ./sandboxctl validate

There is no approved tag yet. Until promotion, use a reviewed commit and record
its SHA. After owner promotion, clone the repository and check out
sandbox/v1.0.0-serenity-10.5.2. Confirm approved: true, owner, date, and the
matching tag in the manifest.

Validation restores dependencies and sergen, builds frontend and backend,
creates/migrates SQLite, loads deterministic seed data, and checks counts.
Success ends with SAYSOL SANDBOX BASELINE: PASS.

Expected state is 30 customers, 6 categories, 30 products, 8 employees, 4
warehouses, 100 orders, 300 details, and 120 inventory records, with seed
identity SaySolSandboxSeed/v1.

## Start and smoke test

    dotnet run --project host/SaySolSandbox.Web.csproj
    curl --fail http://127.0.0.1:5088/health/baseline
    curl --fail http://127.0.0.1:5088/api/customers
    dotnet tool restore --tool-manifest host/.config/dotnet-tools.json
    dotnet sergen --version

## Install, test, and preserve evidence

Only after baseline PASS, apply each selected capsule INSTALL-PROMPT.md and
capsule.yaml to the disposable instance. Then run:

    npm run build --prefix host
    dotnet build host/SaySolSandbox.Web.csproj --configuration Release
    ./sandboxctl validate

Multiple capsules may share an instance only for intentional combination
testing. Record every ID/version/SHA. Never promote a modified instance.

Create evidence from sandbox/evidence/evidence.template.json, validate against
the schema, and preserve logs outside the instance. Record baseline/Serenity
versions, repository and capsule SHAs, installation, backend/frontend,
migration, functional, security, and cleanup results.

## Reset and dispose

    ./sandboxctl clean
    ./sandboxctl validate
    ./sandbox/scripts/dispose.sh /tmp/saysol-sandbox-run-001

Disposal refuses paths without the marker. Copy evidence first.

## Troubleshooting and upgrades

- Install .NET 10 if dotnet is missing.
- Never bypass version mismatches or float pinned dependencies.
- Treat restore failure as a candidate defect.
- On seed failure, create a fresh instance rather than editing control data.
- Missing final PASS means capsule testing is invalid.

An upgrade is a new candidate: update dependencies, regenerate where needed,
validate cleanly, regress verified capsules, review, obtain explicit owner
approval, then create the immutable tag.
