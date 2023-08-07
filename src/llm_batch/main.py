import logging
from pathlib import Path

from llm_batch.data import load_documents
from llm_batch.model import get_llm
from llm_batch.output import store_output
from llm_batch.process import process_documents
from llm_batch.prompt import get_prompt_template

logging.basicConfig(
    level=logging.INFO,
    # format="%(levelname)s: %(asctime)s [%(filename)s:%(lineno)d] - %(message)s",
    format="%(levelname)s: [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def main(input_dir, output_dir, model_name):
    logging.info("Running LLM Batch")

    documents = load_documents(Path(input_dir))

    llm = get_llm(model_name)
    prompt_template = get_prompt_template()

    processed = process_documents(documents, prompt_template, llm)

    store_output(processed, Path(output_dir))


if __name__ == "__main__":
    # TODO: add argument parsing or CLI interface
    # TODO: add schema (path) so user can specify desired output structure
    #       as now it is hardcoded in prompt.py
    main("data/input_txt", "output", "gpt4")
