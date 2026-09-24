#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.."&&pwd)";target="${1:-}"
[[ -n "$target" && "$target" = /* ]]||{ echo "Usage: $0 /absolute/empty/target" >&2;exit 2; }
[[ ! -e "$target" ]]||{ echo "Refusing to overwrite existing path: $target" >&2;exit 2; }
mkdir -p "$target";cp -R "$repo_root/sandbox/host" "$target/host";cp "$repo_root/sandbox/manifest.yaml" "$target/manifest.yaml";cp "$repo_root/sandbox/global.json" "$target/global.json";cp "$repo_root/sandbox/scripts/instance-sandboxctl.sh" "$target/sandboxctl";mkdir -p "$target/evidence";cp "$repo_root/sandbox/evidence/evidence.template.json" "$target/evidence/";printf '%s\n' 'SaySol disposable sandbox instance' >"$target/.saysol-sandbox-instance";chmod +x "$target/sandboxctl";echo "Instantiated candidate sandbox at $target";echo "Next: cd '$target' && ./sandboxctl validate"
