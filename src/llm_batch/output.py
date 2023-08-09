import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def store_output(outputs: dict[Path, dict], output_dir: Path) -> None:
    logger.info("Storing results...")

    if not os.path.exists(output_dir):
        logger.info(f"Creating output directory '{output_dir}'")
    os.makedirs(output_dir, exist_ok=True)

    for path, document in outputs.items():
        if document["processed"] is None:
            logger.warning(f"Skipping '{path}' due to processing error")
            continue
        output_path = os.path.join(output_dir, path.name)

        output_path = os.path.splitext(output_path)[0] + ".json"
        with open(output_path, "w") as f:
            f.write(document["processed"])
    logger.info(f"Stored {len(outputs)} outputs in '{output_dir}'")
