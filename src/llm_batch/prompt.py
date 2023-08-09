import logging

from langchain import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

logger = logging.getLogger(__name__)


def get_prompt_template(parser: PydanticOutputParser) -> PromptTemplate:
    general_instructions = "Extract the topic and sentiment of the given input text."
    format_instuctions = parser.get_format_instructions()

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


def get_correction_prompt(prompt: str, output: str, error: str) -> str:
    prompt += f"""{output}\n
    ERROR: {error}\n
    CORRECTED JSON:
    """
    return prompt
