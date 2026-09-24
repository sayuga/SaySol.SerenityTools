#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")"&&pwd)";command="${1:-help}"
case "$command" in
validate) log="$root/evidence/baseline-$(date -u +%Y%m%dT%H%M%SZ).log";exec > >(tee "$log") 2>&1;dotnet --version|grep -E '^10\.';node --version|grep -E '^v24\.';dotnet tool restore --tool-manifest "$root/host/.config/dotnet-tools.json";dotnet restore "$root/host/SaySolSandbox.Web.csproj" --use-lock-file;npm install --package-lock-only --ignore-scripts --prefix "$root/host";npm ci --ignore-scripts --prefix "$root/host";npm run build --prefix "$root/host";dotnet build "$root/host/SaySolSandbox.Web.csproj" -c Release --no-restore;dotnet run --project "$root/host/SaySolSandbox.Web.csproj" -c Release --no-build -- --validate-baseline;echo "SAYSOL SANDBOX BASELINE: PASS";;
clean) rm -f "$root/host/App_Data/SaySolSandbox.sqlite";echo "Database reset; run validate.";;
*) echo "Usage: ./sandboxctl {validate|clean}";;
esac
