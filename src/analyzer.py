import jsonschema
import json
from typing import Any


def analyze(data: dict[str, Any]):
    schema = {}
    with open("schema.json") as f:
        schema: dict[str, Any] = json.loads(f.read())
    jsonschema.validate(data, schema)
