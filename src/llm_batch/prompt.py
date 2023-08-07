import logging

from langchain import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator

logger = logging.getLogger(__name__)


class OutputJSON(BaseModel):
    topic: str = Field(description="Topic of the text")
    sentiment: str = Field(description="Sentiment of the text")

    @validator("sentiment")
    def topic_is_one_word(cls, v):
        if " " in v:
            raise ValueError("Sentiment must be one word")
        return v


def get_output_parser() -> PydanticOutputParser:
    return PydanticOutputParser(pydantic_object=OutputJSON)


def get_format_instructions() -> str:
    parser = get_output_parser()
    return parser.get_format_instructions()


def get_prompt_template() -> PromptTemplate:
    general_instructions = "Extract the topic and sentiment of the given input text."
    format_instuctions = get_format_instructions()

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
