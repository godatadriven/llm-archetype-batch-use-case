import logging
from pathlib import Path

import typer

from llm_batch.data import load_documents
from llm_batch.model import get_llm
from llm_batch.output import store_output
from llm_batch.process import process_documents
from llm_batch.prompt import get_prompt_template

logger = logging.getLogger(__name__)

app = typer.Typer()


@app.callback()
def callback():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


@app.command()
def batch(
    model_name: str = typer.Option(
        default="gpt-3", help="LLM to use (e.g. gpt-3/4, palm-2, ...)."
    ),
    input_dir: Path = typer.Option(
        default="data/input_txt",
        help="Input directory with the text data to be processed.",
    ),
    output_dir: Path = typer.Option(
        default="output",
        help="Output directory where the processed data will be stored.",
    ),
    schema_path: Path = typer.Option(
        default="schema.yaml",
        help="Path to schema defining which info should be extracted from input text.",
    ),
):
    logging.info("Running LLM Batch")

    documents = load_documents(input_dir)

    llm = get_llm(model_name)
    prompt_template = get_prompt_template(schema_path)

    processed = process_documents(documents, prompt_template, llm)

    store_output(processed, output_dir)
