#!/usr/bin/env python3
"""Validate repository schemas and catalog-to-manifest references."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    schemas = {
        path.name: load_json(path)
        for path in sorted((ROOT / "schema").glob("*.json"))
    }
    for path in (ROOT / "schema").glob("*.json"):
        jsonschema.Draft202012Validator.check_schema(load_json(path))

    catalog = load_yaml(ROOT / "catalog.yaml")
    jsonschema.validate(catalog, schemas["catalog.schema.json"])
    jsonschema.validate(load_json(ROOT / "templates/host-facts.json"), schemas["host-facts.schema.json"])
    jsonschema.validate(load_yaml(ROOT / "templates/ToolCapsule/capsule.yaml"), schemas["capsule-install.schema.json"])

    seen: set[str] = set()
    catalog_entries = {}
    for entry in catalog["capsules"]:
        capsule_id = entry["id"]
        if capsule_id in seen:
            raise ValueError(f"Duplicate catalog ID: {capsule_id}")
        seen.add(capsule_id)
        catalog_entries[capsule_id] = entry
        if not entry["manifest"]:
            continue
        manifest_path = ROOT / entry["manifest"]
        manifest = load_yaml(manifest_path)
        jsonschema.validate(manifest, schemas["capsule-install.schema.json"])
        if manifest["capsule"]["id"] != capsule_id:
            raise ValueError(f"Catalog/manifest ID mismatch: {capsule_id}")
        if manifest["capsule"]["version"] != entry["version"]:
            raise ValueError(f"Catalog/manifest version mismatch: {capsule_id}")

    wiki_registry = load_yaml(ROOT / "wiki/tool-pages.yaml")
    wiki_seen: set[str] = set()
    required_headings = (
        "## Version, compatibility, and installation state",
        "## Installation",
        "### Installation testing state",
        "## Validation",
        "## Upgrade",
    )
    for tool in wiki_registry["tools"]:
        tool_id = tool["id"]
        if tool_id in wiki_seen:
            raise ValueError(f"Duplicate wiki tool ID: {tool_id}")
        wiki_seen.add(tool_id)
        entry = catalog_entries.get(tool_id)
        if not entry:
            raise ValueError(f"Wiki page has no catalog entry: {tool_id}")
        if tool["maturity"] != entry["maturity"]:
            raise ValueError(f"Wiki/catalog maturity mismatch: {tool_id}")
        if tool["delivery"] != entry["delivery"]:
            raise ValueError(f"Wiki/catalog delivery mismatch: {tool_id}")
        if tool["tool_version"] != entry["version"]:
            raise ValueError(f"Wiki/catalog version mismatch: {tool_id}")
        if not tool.get("compatibility"):
            raise ValueError(f"Wiki compatibility is missing: {tool_id}")
        for lane in tool["compatibility"]:
            for field in ("lane", "serenity", "dotnet", "evidence", "core_test", "host_install_test"):
                if field not in lane:
                    raise ValueError(f"Wiki {tool_id} compatibility omits {field}")
        page = ROOT / "wiki" / tool["page"]
        content = page.read_text(encoding="utf-8")
        for heading in required_headings:
            if heading not in content:
                raise ValueError(f"{page}: missing required heading {heading}")

    print(
        f"Validated {len(schemas)} schemas, {len(seen)} catalog entries, "
        f"and {len(wiki_seen)} tool wiki pages."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
