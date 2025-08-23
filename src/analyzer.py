import jsonschema
import json
import logging
from typing import Any
from pathlib import Path
import python_jsonschema_objects as pjs

from jsonschema.exceptions import ValidationError

LOG = logging.getLogger(__name__)
schema_path = Path(__file__).parent.parent / "schema.json"

schema = {}
with open(schema_path) as f:
    schema: dict[str, Any] = json.loads(f.read())


def validate_schema_data(data: dict[str, Any]):
    jsonschema.validate(data, schema)


def analyze(data: dict[str, Any]):
    try:
        validate_schema_data(data)
    except ValidationError as e:
        LOG.warning(f"ValidationError: {e}")
        raise e
    builder = pjs.ObjectBuilder(schema)
    HarAnalyzer = builder.build_classes(any_of="use-first").HarAnalyzer
    har_data = HarAnalyzer(log=data.get("log"))
