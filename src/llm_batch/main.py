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


def main(model_name: str, input_dir: Path, output_dir: Path, schema_path: Path):
    logging.info("Running LLM Batch")

    documents = load_documents(input_dir)

    llm = get_llm(model_name)
    prompt_template = get_prompt_template(schema_path)

    processed = process_documents(documents, prompt_template, llm)

    store_output(processed, output_dir)


if __name__ == "__main__":
    # TODO: add argument parsing or CLI interface
    main(
        "gpt-3",
        Path("data/input_txt"),
        Path("output"),
        Path("schema.yaml"),
    )
