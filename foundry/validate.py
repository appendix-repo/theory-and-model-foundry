"""Validation against the draft v0 theory-object schema (appendix Section 4, Annex A).

Two layers:
1. JSON Schema (draft 2020-12) validation, using the schema exactly as published.
2. Rules that appendix Section 4.1 states in prose but that the v0 JSON Schema
   does not encode (for example, "`closed` requires a named `checker`").
   These are checked in code here and reported separately, so that a reader
   can see which design principles the schema enforces by itself.
"""
from jsonschema import Draft202012Validator

from .io import load_schema


def _sub(schema, name):
    return {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}


def validator(def_name=None):
    schema = load_schema()
    target = schema if def_name is None else _sub(schema, def_name)
    return Draft202012Validator(target)


def errors(obj, def_name=None):
    return [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}"
            for e in validator(def_name).iter_errors(obj)]


def prose_rule_violations(obj):
    """Section 4.1 rules not expressed in the v0 JSON Schema."""
    out = []
    for d in obj.get("derivations", []) or []:
        if d.get("status") == "closed" and not d.get("checker"):
            out.append(f"{d['@id']}: status 'closed' without a named checker (principle 3)")
    for a in obj.get("assumptions", []) or []:
        if a.get("explicitness") == "surfaced" and not a.get("surfacedBy"):
            out.append(f"{a['@id']}: surfaced assumption without surfacedBy (principle 4)")
    return out
