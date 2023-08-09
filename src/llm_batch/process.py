import logging
import time
from pathlib import Path
from typing import Any

from langchain import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import OutputParserException
from tqdm import tqdm  # type: ignore

from llm_batch.prompt import get_correction_prompt

logger = logging.getLogger(__name__)


def process_and_validate(
    path: Path,
    document: dict[str, Any],
    llm: Any,
    prompt_template: PromptTemplate,
    parser: PydanticOutputParser,
    max_retries: int,
) -> str | None:
    prompt = prompt_template.format(input_text=document["content"])
    for i in range(max_retries):
        output = llm(prompt)
        try:
            parser.parse(output)  # validates output
            return output  # success
        except OutputParserException as e:
            logger.debug(f"({path}) {e}")
            logger.warning(
                f"Failed to parse output for '{path}'. "
                + "Retrying... ({i+1}/{max_retries})"
            )
            prompt = get_correction_prompt(prompt, output, str(e))
    return None  # max retries exceeded


def process_documents(
    documents: dict[Path, dict],
    prompt_template: PromptTemplate,
    llm: Any,
    parser: PydanticOutputParser,
    max_retries: int = 3,
) -> dict[Path, dict]:
    logger.info("Running LLM on documents")

    start = time.perf_counter()

    for path, document in tqdm(documents.items()):
        document["processed"] = process_and_validate(
            path, document, llm, prompt_template, parser, max_retries
        )
    logger.info(
        f"Processed {len(documents)} documents in {time.perf_counter() - start:.2f}s"
    )

    return documents
