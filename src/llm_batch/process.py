import logging
from pathlib import Path

from langchain import PromptTemplate

logger = logging.getLogger(__name__)


def process_documents(
    documents: dict[Path, dict], prompt_template: PromptTemplate, llm
) -> dict[Path, dict]:
    logger.info("Running LLM on documents")

    for path, document in documents.items():
        prompt = prompt_template.format(input_text=document["content"])
        output = llm(prompt)

        documents[path]["processed"] = output

        logger.debug(
            "Processed document.\n"
            + f"> PATH: {path}\n> PROMPT: {prompt}\n\n> OUTPUT: {output}"
        )

    return documents
