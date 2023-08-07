import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def get_document_paths(folder_path: Path) -> list[Path]:
    if not os.path.isdir(folder_path):
        raise ValueError(f"'{folder_path}' is not a directory")

    paths = []
    for fname in os.listdir(folder_path):
        document_path = folder_path / fname
        if os.path.isfile(document_path):
            paths.append(document_path)
    return paths


def get_document_contents(document_paths: list[Path]) -> dict[Path, dict]:
    document_contents: dict[Path, dict] = {}
    for path in document_paths:
        document_contents[path] = {}
        with open(path, "r") as f:
            document_contents[path]["content"] = f.read()
    return document_contents


def load_documents(folder_path: Path) -> dict[Path, dict]:
    logger.info(f"Loading documents from '{folder_path}'")

    document_paths = get_document_paths(folder_path)
    documents = get_document_contents(document_paths)

    logger.info(f"Found {len(documents)} documents")
    return documents
