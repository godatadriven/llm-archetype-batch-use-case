import logging
from pathlib import Path

from langchain import PromptTemplate

from llm_batch.schema import get_format_instructions

logger = logging.getLogger(__name__)


def get_prompt_template(schema_path: Path) -> PromptTemplate:
    general_instructions = "Extract the topic and sentiment of the given input text."
    format_instuctions = get_format_instructions(schema_path)

    template = """
    {general_instructions}\n
    {format_instructions}\n
    INPUT TEXT: {input_text}\n
    OUTPUT JSON:
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["input_text"],
        partial_variables={
            "general_instructions": general_instructions,
            "format_instructions": format_instuctions,
        },
    )

    return prompt
