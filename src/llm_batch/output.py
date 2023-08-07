import logging
import os

logger = logging.getLogger(__name__)


def store_output(outputs: dict[str, str], output_dir: str) -> None:
    ...
    logger.info(f"Stored {len(outputs)} outputs in '{output_dir}'")
