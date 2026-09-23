#!/usr/bin/env python3
"""Resolve SerenityTools capsule selections into a mutation-free install plan."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment concern
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc


class ResolutionError(Exception):
    pass


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream)
    if not isinstance(value, dict):
        raise ResolutionError(f"{path}: expected a YAML object")
    return value


def version_tuple(value: str) -> tuple[int, int, int]:
    match = re.match(r"^(\d+)\.(\d+)(?:\.(\d+))?", value)
    if not match:
        raise ResolutionError(f"Unsupported version value: {value}")
    return tuple(int(part or 0) for part in match.groups())  # type: ignore[return-value]


def satisfies(version: str, expression: str) -> bool:
    actual = version_tuple(version)
    for clause in expression.split():
        match = re.match(r"^(>=|<=|>|<|=)?(.+)$", clause)
        if not match:
            return False
        operator, expected_text = match.groups()
        expected = version_tuple(expected_text)
        if operator == ">=" and not actual >= expected:
            return False
        if operator == "<=" and not actual <= expected:
            return False
        if operator == ">" and not actual > expected:
            return False
        if operator == "<" and not actual < expected:
            return False
        if operator in (None, "=") and actual != expected:
            return False
    return True


def identify_lane(catalog: dict[str, Any], host: dict[str, Any]) -> str:
    matches = [
        lane
        for lane, rule in catalog["compatibility_lanes"].items()
        if satisfies(host["serenity_version"], rule["serenity"])
        and host["dotnet_version"].startswith(rule["dotnet"])
    ]
    if len(matches) != 1:
        raise ResolutionError(
            f"Host must match exactly one compatibility lane; matched {matches or 'none'}"
        )
    return matches[0]


def load_manifests(
    catalog_path: Path, catalog: dict[str, Any]
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    entries = {item["id"]: item for item in catalog.get("capsules", [])}
    if len(entries) != len(catalog.get("capsules", [])):
        raise ResolutionError("Catalog contains duplicate capsule IDs")
    manifests: dict[str, dict[str, Any]] = {}
    for capsule_id, entry in entries.items():
        manifest_path = entry.get("manifest")
        if not manifest_path:
            continue
        path = (catalog_path.parent / manifest_path).resolve()
        manifest = load_yaml(path)
        declared = manifest.get("capsule", {})
        if declared.get("id") != capsule_id:
            raise ResolutionError(f"{path}: capsule ID does not match catalog")
        if entry.get("version") != declared.get("version"):
            raise ResolutionError(f"{path}: capsule version does not match catalog")
        manifest["_path"] = str(path)
        manifests[capsule_id] = manifest
    return entries, manifests


def resolve_selection(
    selected: list[str],
    entries: dict[str, dict[str, Any]],
    manifests: dict[str, dict[str, Any]],
) -> list[str]:
    resolved: list[str] = []
    visiting: list[str] = []

    def visit(capsule_id: str) -> None:
        if capsule_id in resolved:
            return
        if capsule_id in visiting:
            cycle = " -> ".join(visiting + [capsule_id])
            raise ResolutionError(f"Dependency cycle: {cycle}")
        entry = entries.get(capsule_id)
        if not entry:
            raise ResolutionError(f"Unknown capsule: {capsule_id}")
        if entry.get("maturity") not in {"verified", "released"}:
            raise ResolutionError(
                f"{capsule_id} is {entry.get('maturity')}, not installable"
            )
        manifest = manifests.get(capsule_id)
        if not manifest:
            raise ResolutionError(f"{capsule_id} has no install manifest")
        visiting.append(capsule_id)
        for dependency in manifest["dependencies"].get("capsules", []):
            if not dependency.get("optional", False):
                visit(dependency["id"])
        visiting.pop()
        resolved.append(capsule_id)

    for capsule_id in selected:
        visit(capsule_id)
    return resolved


def validate_compatibility(
    capsule_id: str, manifest: dict[str, Any], lane: str, host: dict[str, Any]
) -> None:
    lane_rules = [
        item for item in manifest["compatibility"]["serenity"] if item["lane"] == lane
    ]
    if len(lane_rules) != 1 or lane_rules[0]["evidence"] == "incompatible":
        raise ResolutionError(f"{capsule_id} does not support lane {lane}")
    rule = lane_rules[0]
    if not satisfies(host["serenity_version"], rule["version"]):
        raise ResolutionError(f"{capsule_id} does not support Serenity {host['serenity_version']}")
    if not host["dotnet_version"].startswith(rule["dotnet"]):
        raise ResolutionError(f"{capsule_id} does not support .NET {host['dotnet_version']}")
    capabilities = set(host.get("capabilities", []))
    required = set(manifest["compatibility"].get("required_capabilities", []))
    provided = set(manifest["dependencies"].get("provided_by_host", []))
    missing = sorted((required | provided) - capabilities)
    if missing:
        raise ResolutionError(f"{capsule_id} requires host capabilities: {', '.join(missing)}")


def validate_relationships(order: list[str], manifests: dict[str, dict[str, Any]]) -> None:
    selected = set(order)
    for capsule_id in order:
        dependencies = manifests[capsule_id]["dependencies"]
        conflicts = selected.intersection(dependencies.get("conflicts", []))
        if conflicts:
            raise ResolutionError(f"{capsule_id} conflicts with {', '.join(sorted(conflicts))}")
        superseded = selected.intersection(dependencies.get("supersedes", []))
        if superseded:
            raise ResolutionError(
                f"Remove superseded selection(s) before installing {capsule_id}: "
                + ", ".join(sorted(superseded))
            )


def validate_dependency_versions(
    order: list[str], manifests: dict[str, dict[str, Any]]
) -> None:
    packages: dict[tuple[str, str], tuple[str, str]] = {}
    shared: tuple[str, str] | None = None
    for capsule_id in order:
        dependencies = manifests[capsule_id]["dependencies"]
        for dependency in dependencies.get("capsules", []):
            if dependency["id"] in manifests and dependency["id"] in order:
                actual = manifests[dependency["id"]]["capsule"]["version"]
                if not satisfies(actual, dependency["version"]):
                    raise ResolutionError(
                        f"{capsule_id} requires {dependency['id']} {dependency['version']}; "
                        f"selected version is {actual}"
                    )
        shared_requirement = dependencies.get("shared", {})
        if shared_requirement.get("required"):
            version = shared_requirement.get("version")
            if not version:
                raise ResolutionError(f"{capsule_id} requires Shared without a version")
            if shared and shared[1] != version:
                raise ResolutionError(
                    f"Shared version constraint collision: {shared[0]} requires {shared[1]}, "
                    f"{capsule_id} requires {version}"
                )
            shared = (capsule_id, version)
        for ecosystem in ("nuget", "npm"):
            for package in dependencies.get(ecosystem, []):
                key = (ecosystem, package["id"].lower())
                prior = packages.get(key)
                if prior and prior[1] != package["version"]:
                    raise ResolutionError(
                        f"{ecosystem} version collision for {package['id']}: "
                        f"{prior[0]} requires {prior[1]}, {capsule_id} requires {package['version']}"
                    )
                packages[key] = (capsule_id, package["version"])


def validate_ownership(order: list[str], manifests: dict[str, dict[str, Any]]) -> None:
    claims: dict[tuple[str, str], tuple[str, str]] = {}
    for capsule_id in order:
        manifest = manifests[capsule_id]
        declared = list(manifest.get("ownership", {}).get("claims", []))
        declared.extend(
            {"kind": "path", "key": item["target"], "policy": "exclusive"}
            for item in manifest["installation"].get("files", [])
        )
        for claim in declared:
            key = (claim["kind"], claim["key"])
            prior = claims.get(key)
            if prior and "exclusive" in {prior[1], claim["policy"]}:
                raise ResolutionError(
                    f"Ownership collision for {claim['kind']} {claim['key']}: "
                    f"{prior[0]} and {capsule_id}"
                )
            claims[key] = (capsule_id, claim["policy"])


def build_plan(
    catalog_path: Path, host_path: Path, selected: list[str]
) -> dict[str, Any]:
    catalog = load_yaml(catalog_path)
    with host_path.open(encoding="utf-8") as stream:
        host = json.load(stream)
    repository = host.get("repository", {})
    if not repository.get("worktree_clean", False):
        raise ResolutionError("Host worktree is not clean or has not been acknowledged")
    lane = identify_lane(catalog, host)
    entries, manifests = load_manifests(catalog_path, catalog)
    order = resolve_selection(selected, entries, manifests)
    for capsule_id in order:
        validate_compatibility(capsule_id, manifests[capsule_id], lane, host)
    validate_relationships(order, manifests)
    validate_dependency_versions(order, manifests)
    validate_ownership(order, manifests)

    capsules = []
    for capsule_id in order:
        manifest = manifests[capsule_id]
        install = manifest["installation"]
        capsules.append(
            {
                "id": capsule_id,
                "version": manifest["capsule"]["version"],
                "manifest": manifest["_path"],
                "delivery": manifest["capsule"]["delivery"],
                "files": install.get("files", []),
                "migrations": install.get("migrations", []),
                "edits": install.get("edits", []),
                "human_gates": install.get("human_gates", []),
                "validation": manifest["validation"],
                "optional_integrations": manifest["dependencies"].get("integrates_with", []),
            }
        )
    return {
        "mode": "dry-run",
        "mutates_host": False,
        "host": {
            "root": repository["root"],
            "branch": repository["branch"],
            "head": repository["head"],
            "serenity_version": host["serenity_version"],
            "dotnet_version": host["dotnet_version"],
            "lane": lane,
        },
        "install_order": order,
        "capsules": capsules,
        "lockfile": catalog["defaults"]["lockfile"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--host", type=Path, required=True)
    parser.add_argument("--select", action="append", required=True, dest="selected")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        plan = build_plan(args.catalog.resolve(), args.host.resolve(), args.selected)
    except (KeyError, OSError, ValueError, ResolutionError) as exc:
        print(f"resolution failed: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(plan, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
