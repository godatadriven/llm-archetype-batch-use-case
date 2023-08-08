import json
from pathlib import Path

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, create_model

TYPE_MAPPING = {
    "str": str,
    "int": int,
    "list[str]": list[str],
    "list[int]": list[int],
}


def load_schema(schema_path: Path) -> BaseModel:
    with open(schema_path) as f:
        schema = json.load(f)

    fields = {}
    for field_name, field_info in schema.items():
        field_type = field_info["type"]
        field_description = field_info["description"]
        field_type = TYPE_MAPPING.get(field_type)

        fields[field_name] = fields[field_name] = (
            field_type,
            Field(default=None, description=field_description),
        )

    schema_model = create_model("SchemaModel", **fields)  # type: ignore
    return schema_model


def get_format_instructions(schema_path: Path) -> str:
    parser = PydanticOutputParser(
        pydantic_object=load_schema(schema_path)
    )  # type: ignore
    return parser.get_format_instructions()
