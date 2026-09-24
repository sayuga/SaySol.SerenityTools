#!/usr/bin/env bash
set -euo pipefail
fail=0
check(){ if command -v "$1" >/dev/null 2>&1;then echo "PASS $1: $($1 --version 2>/dev/null|head -1)";else echo "FAIL $1 is required" >&2;fail=1;fi; }
check git;check dotnet;check node;check npm
if ((fail));then echo "SAYSOL SANDBOX PREFLIGHT: FAIL";exit 1;fi
[[ "$(dotnet --version)" == 10.* ]]||{ echo "FAIL .NET SDK must be 10.x" >&2;exit 1; }
[[ "$(node --version)" == v24.* ]]||{ echo "FAIL Node must be 24.x" >&2;exit 1; }
echo "SAYSOL SANDBOX PREFLIGHT: PASS"
