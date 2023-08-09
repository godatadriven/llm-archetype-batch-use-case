import logging
from pathlib import Path

import yaml  # type: ignore
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, create_model

logger = logging.getLogger(__name__)

# Using type mapping to avoid using eval
TYPE_MAPPING = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list[str]": list[str],
    "list[int]": list[int],
    "list[float]": list[float],
    "list[bool]": list[bool],
}


def load_schema(schema_path: Path) -> type[BaseModel]:
    logger.info(f"Loading schema from '{schema_path}'")
    with open(schema_path) as f:
        schema = yaml.safe_load(f)

    fields = {}
    for field_name, field_info in schema.items():
        _field_type = field_info["type"]
        field_description = field_info["description"]
        field_type = TYPE_MAPPING.get(_field_type)

        if field_type is None:
            raise ValueError(
                f"Unsupported type '{_field_type}' for field '{field_name}'"
            )

        fields[field_name] = fields[field_name] = (
            field_type,
            Field(default=None, description=field_description),
        )

    schema_model = create_model("SchemaModel", **fields)
    return schema_model


def get_format_instructions(schema_path: Path) -> str:
    parser = PydanticOutputParser(
        pydantic_object=load_schema(schema_path)
    )  # type: ignore
    return parser.get_format_instructions()
