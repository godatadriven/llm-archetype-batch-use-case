import logging
from pathlib import Path
from typing import Any, Literal

import yaml  # type: ignore
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, create_model

logger = logging.getLogger(__name__)

# Using type mapping to avoid using eval
# when loading schema from YAML
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


def get_field_type(_field_type: str) -> Any:
    if _field_type.startswith("Literal["):
        literal_values_str = _field_type[8:-1]  # Extract the values inside the brackets
        literal_values = [x.strip() for x in literal_values_str.split(",")]
        literal_values_parsed = []

        for value in literal_values:
            if value.startswith('"') and value.endswith('"'):
                literal_values_parsed.append(
                    value[1:-1]
                )  # Remove quotes and add as str
            elif value.isdigit():
                literal_values_parsed.append(int(value))  # type: ignore
            else:
                raise ValueError(f"Unsupported value type in Literal: {value}")

        return Literal[*literal_values_parsed]
    else:
        return TYPE_MAPPING.get(_field_type)


def load_schema(schema_path: Path) -> type[BaseModel]:
    logger.info(f"Loading schema from '{schema_path}'")
    with open(schema_path) as f:
        schema = yaml.safe_load(f)

    fields = {}
    for field_name, field_info in schema.items():
        field_description = field_info["description"]
        field_type = get_field_type(field_info["type"])

        if field_type is None:
            raise ValueError(
                f"Unsupported type '{field_type}' for field '{field_name}'"
            )

        fields[field_name] = (
            field_type,
            Field(description=field_description),
        )

    schema_model = create_model("SchemaModel", **fields)  # type: ignore
    return schema_model


def get_output_parser(schema_path: Path) -> PydanticOutputParser:
    return PydanticOutputParser(pydantic_object=load_schema(schema_path))
