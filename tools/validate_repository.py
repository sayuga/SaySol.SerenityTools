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
    for entry in catalog["capsules"]:
        capsule_id = entry["id"]
        if capsule_id in seen:
            raise ValueError(f"Duplicate catalog ID: {capsule_id}")
        seen.add(capsule_id)
        if not entry["manifest"]:
            continue
        manifest_path = ROOT / entry["manifest"]
        manifest = load_yaml(manifest_path)
        jsonschema.validate(manifest, schemas["capsule-install.schema.json"])
        if manifest["capsule"]["id"] != capsule_id:
            raise ValueError(f"Catalog/manifest ID mismatch: {capsule_id}")
        if manifest["capsule"]["version"] != entry["version"]:
            raise ValueError(f"Catalog/manifest version mismatch: {capsule_id}")

    print(f"Validated {len(schemas)} schemas and {len(seen)} catalog entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
