#!/usr/bin/env bash
set -euo pipefail
target="${1:-}";[[ -n "$target" && "$target" = /* && "$target" != / ]]||{ echo "Usage: $0 /absolute/sandbox/instance" >&2;exit 2; };[[ -f "$target/.saysol-sandbox-instance" ]]||{ echo "Refusing: marker not found in $target" >&2;exit 2; };echo "Copy evidence out of $target/evidence before disposal.";find "$target" -depth -delete;echo "Disposed sandbox instance: $target"
