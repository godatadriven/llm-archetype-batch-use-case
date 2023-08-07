import logging

from langchain import PromptTemplate

logger = logging.getLogger(__name__)


def process_documents(
    documents: dict[str, str], prompt_template: PromptTemplate, llm
) -> dict[str, str]:
    logger.info("Running LLM on documents")
    ...
    return {"path": "output"}
